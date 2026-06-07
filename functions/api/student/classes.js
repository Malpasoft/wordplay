// Word Play Student API — Get enrolled classes
// GET /api/student/classes
// Response: { classes: [{id, name, teacher_id, level, description, enrolled_at}, ...] } or { error }

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

export async function onRequestGet(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const userId = await verifyToken(token, context.env.DB);
    if (!userId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    const userRole = await getUserRole(userId, context.env.DB);
    if (userRole !== 'student') {
      return json({ error: 'Student access required' }, 403);
    }

    // Get the student record for this user
    const student = await context.env.DB.prepare(
      'SELECT id FROM students WHERE user_id = ?'
    )
      .bind(userId)
      .first();

    if (!student) {
      return json({ classes: [] }, 200);
    }

    // Fetch classes enrolled via class_enrollments
    const result = await context.env.DB.prepare(`
      SELECT
        c.id,
        c.name,
        c.teacher_id,
        c.level,
        c.description,
        ce.enrolled_at
      FROM classes c
      INNER JOIN class_enrollments ce ON c.id = ce.class_id
      WHERE ce.student_id = ?
      ORDER BY c.created_at DESC
    `).bind(student.id).all();

    const classes = (result.results || []).map(c => ({
      id: c.id,
      name: c.name,
      teacher_id: c.teacher_id,
      level: c.level || null,
      description: c.description || null,
      enrolled_at: c.enrolled_at
    }));

    return json({ classes }, 200);
  } catch (error) {
    console.error('Get classes error:', error);
    return json({ error: 'Failed to fetch classes' }, 500);
  }
}
