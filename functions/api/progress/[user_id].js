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

// Deep-merge two progress objects without losing data (mirrors store.js):
//  · level maps → union of chapters, keep later-dated (then higher-pct) entry
//  · xp / streak → keep the maximum;  lastDay → keep the later date
function pickEntry(x, y) {
  if (!x) return y;
  if (!y) return x;
  const dx = Date.parse(x.lastDate || x.date || 0) || 0;
  const dy = Date.parse(y.lastDate || y.date || 0) || 0;
  if (dx !== dy) return dx > dy ? x : y;
  return (y.pct || 0) > (x.pct || 0) ? y : x;
}

function mergeProgress(a, b) {
  a = a || {}; b = b || {};
  const out = {};
  const keys = new Set([...Object.keys(a), ...Object.keys(b)]);
  for (const k of keys) {
    const av = a[k], bv = b[k];
    if (k === 'updated_at') continue;
    if (k === 'xp')      { out.xp = Math.max(av || 0, bv || 0); continue; }
    if (k === 'streak')  { out.streak = Math.max(av || 0, bv || 0); continue; }
    if (k === 'lastDay') { out.lastDay = (av || '') > (bv || '') ? av : bv; continue; }
    if (av && bv && typeof av === 'object' && typeof bv === 'object') {
      const level = {};
      const chs = new Set([...Object.keys(av), ...Object.keys(bv)]);
      for (const c of chs) level[c] = pickEntry(av[c], bv[c]);
      out[k] = level;
      continue;
    }
    out[k] = (bv !== undefined ? bv : av);
  }
  return out;
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

    const user = await context.env.DB.prepare('SELECT role FROM users WHERE id = ?')
      .bind(tokenUserId)
      .first();

    if (user.role !== 'admin' && parseInt(user_id) !== tokenUserId) {
      return json({ error: 'Cannot save another user\'s progress' }, 403);
    }

    const payload = await context.request.json();
    const studentId = parseInt(user_id);
    const now = Date.now();

    // Handle normalized format (new): { chapters: [...], xp, streak, lastDay }
    if (Array.isArray(payload.chapters)) {
      // Insert/update each chapter
      for (const ch of payload.chapters) {
        await context.env.DB.prepare(
          `INSERT INTO chapter_results (user_id, level, chapter_slug, score, total, pct, date, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)
           ON CONFLICT(user_id, level, chapter_slug) DO UPDATE SET
             score=excluded.score, total=excluded.total, pct=excluded.pct,
             date=excluded.date, updated_at=excluded.updated_at`
        )
          .bind(studentId, ch.level, ch.slug, ch.score, ch.total, ch.pct, ch.date, now)
          .run();
      }

      // Upsert XP/streak (one row per student, take max on conflict)
      await context.env.DB.prepare(
        `INSERT INTO user_xp (user_id, xp, streak, last_day, updated_at)
         VALUES (?, ?, ?, ?, ?)
         ON CONFLICT(user_id) DO UPDATE SET
           xp=MAX(xp, excluded.xp),
           streak=MAX(streak, excluded.streak),
           last_day=MAX(last_day, excluded.last_day),
           updated_at=excluded.updated_at`
      )
        .bind(studentId, payload.xp || 0, payload.streak || 0, payload.lastDay || null, now)
        .run();

      return json({
        ok: true,
        message: 'Progress saved to normalized schema'
      }, 200);
    }

    // Fallback: handle old blob format for migration period (backward compat)
    const clientData = payload;
    const existing = await context.env.DB.prepare(
      'SELECT progress_data FROM student_progress WHERE user_id = ?'
    )
      .bind(studentId)
      .first();

    let mergedData = clientData;
    if (existing) {
      mergedData = mergeProgress(JSON.parse(existing.progress_data), clientData);
    }

    mergedData.updated_at = now;

    if (existing) {
      await context.env.DB.prepare(
        'UPDATE student_progress SET progress_data = ?, updated_at = ? WHERE user_id = ?'
      )
        .bind(JSON.stringify(mergedData), now, studentId)
        .run();
    } else {
      await context.env.DB.prepare(
        'INSERT INTO student_progress (user_id, progress_data, updated_at) VALUES (?, ?, ?)'
      )
        .bind(studentId, JSON.stringify(mergedData), now)
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
