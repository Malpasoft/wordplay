// Word Play Student API — Join teacher via invite code
// POST /api/student/join-teacher
// Request: { invite_code }
// Response: { message, teacher_id } or { error }

function verifyToken(token, db) {
  return db.prepare('SELECT user_id FROM auth_tokens WHERE token = ? AND expires_at > ?')
    .bind(token, Date.now())
    .first()
    .then(row => row ? row.user_id : null);
}

async function getUserRole(userId, db) {
  const user = await db.prepare('SELECT role FROM users WHERE id = ?')
    .bind(userId)
    .first();
  return user ? user.role : null;
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}

export async function onRequestPost(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const studentId = await verifyToken(token, context.env.DB);
    if (!studentId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    const userRole = await getUserRole(studentId, context.env.DB);
    if (userRole !== 'student') {
      return json({ error: 'Student access required' }, 403);
    }

    const body = await context.request.json();
    const { invite_code } = body;

    if (!invite_code) {
      return json({ error: 'invite_code is required' }, 400);
    }

    const now = Date.now();

    // Find the invite code
    const inviteCode = await context.env.DB.prepare(
      'SELECT id, teacher_id, expires_at, revoked, max_uses, uses_count FROM invite_codes WHERE code = ?'
    )
      .bind(invite_code.toUpperCase())
      .first();

    if (!inviteCode) {
      return json({ error: 'Invalid invite code.' }, 400);
    }

    // Check if code is revoked
    if (inviteCode.revoked) {
      return json({ error: 'This invite code has been revoked.' }, 400);
    }

    // Check if code is expired
    if (inviteCode.expires_at < now) {
      return json({ error: 'This invite code has expired.' }, 400);
    }

    // Check if code has reached max uses
    if (inviteCode.max_uses > 0 && inviteCode.uses_count >= inviteCode.max_uses) {
      return json({ error: 'This invite code has reached its use limit.' }, 400);
    }

    const teacherId = inviteCode.teacher_id;

    // Check if student is already linked to this teacher
    const existing = await context.env.DB.prepare(
      'SELECT id FROM student_teachers WHERE student_id = ? AND teacher_id = ?'
    )
      .bind(studentId, teacherId)
      .first();

    if (existing) {
      return json({ error: 'You are already joined to this teacher\'s class.' }, 400);
    }

    // Link student to teacher
    await context.env.DB.prepare(
      'INSERT INTO student_teachers (student_id, teacher_id) VALUES (?, ?)'
    )
      .bind(studentId, teacherId)
      .run();

    // Increment uses count
    await context.env.DB.prepare(
      'UPDATE invite_codes SET uses_count = uses_count + 1, updated_at = ? WHERE id = ?'
    )
      .bind(now, inviteCode.id)
      .run();

    return json({
      message: 'Successfully joined the class.',
      teacher_id: teacherId
    }, 200);
  } catch (error) {
    console.error('Join teacher error:', error);
    return json({ error: 'Failed to join teacher.' }, 500);
  }
}
