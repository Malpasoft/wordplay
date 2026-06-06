// Word Play Progress Sync API
// GET /api/progress/[user_id] — fetch user's progress from D1
// POST /api/progress/[user_id] — save user's progress to D1 (last-write-wins merge)

function verifyToken(token, db) {
  return db.prepare('SELECT user_id FROM auth_tokens WHERE token = ? AND expires_at > ?')
    .bind(token, Date.now())
    .first()
    .then(row => row ? row.user_id : null);
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}

export async function onRequestGet(context) {
  try {
    const { user_id } = context.params;
    const authHeader = context.request.headers.get('Authorization');

    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const tokenUserId = await verifyToken(token, context.env.DB);

    if (!tokenUserId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    // Users can only access their own progress, or admins can access any
    const user = await context.env.DB.prepare('SELECT role FROM users WHERE id = ?')
      .bind(tokenUserId)
      .first();

    if (user.role !== 'admin' && parseInt(user_id) !== tokenUserId) {
      return json({ error: 'Cannot access another user\'s progress' }, 403);
    }

    const progress = await context.env.DB.prepare(
      'SELECT progress_data, updated_at FROM student_progress WHERE user_id = ?'
    )
      .bind(parseInt(user_id))
      .first();

    if (!progress) {
      return json({ progress: {}, updated_at: Date.now() });
    }

    return json({
      progress: JSON.parse(progress.progress_data),
      updated_at: progress.updated_at
    });
  } catch (error) {
    console.error('Progress fetch error:', error);
    return json({ error: 'Failed to fetch progress' }, 500);
  }
}

export async function onRequestPost(context) {
  try {
    const { user_id } = context.params;
    const authHeader = context.request.headers.get('Authorization');

    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const tokenUserId = await verifyToken(token, context.env.DB);

    if (!tokenUserId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    // Users can only save their own progress, or admins can save any
    const user = await context.env.DB.prepare('SELECT role FROM users WHERE id = ?')
      .bind(tokenUserId)
      .first();

    if (user.role !== 'admin' && parseInt(user_id) !== tokenUserId) {
      return json({ error: 'Cannot save another user\'s progress' }, 403);
    }

    const body = await context.request.json();
    const clientData = body;
    const clientUpdatedAt = body.updated_at || Date.now();

    // Fetch existing progress from D1
    const existing = await context.env.DB.prepare(
      'SELECT progress_data, updated_at FROM student_progress WHERE user_id = ?'
    )
      .bind(parseInt(user_id))
      .first();

    let mergedData = clientData;

    if (existing) {
      // Last-write-wins: use whichever has the later updated_at
      if (existing.updated_at > clientUpdatedAt) {
        mergedData = JSON.parse(existing.progress_data);
      }
    }

    const now = Date.now();
    mergedData.updated_at = now;

    // Upsert progress record
    if (existing) {
      await context.env.DB.prepare(
        'UPDATE student_progress SET progress_data = ?, updated_at = ? WHERE user_id = ?'
      )
        .bind(JSON.stringify(mergedData), now, parseInt(user_id))
        .run();
    } else {
      await context.env.DB.prepare(
        'INSERT INTO student_progress (user_id, progress_data, updated_at) VALUES (?, ?, ?)'
      )
        .bind(parseInt(user_id), JSON.stringify(mergedData), now)
        .run();
    }

    return json({
      ok: true,
      progress: mergedData,
      updated_at: now
    });
  } catch (error) {
    console.error('Progress save error:', error);
    return json({ error: 'Failed to save progress' }, 500);
  }
}
