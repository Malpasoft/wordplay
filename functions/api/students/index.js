// GET /api/students — List all students for logged-in teacher
// POST /api/students — Create a new student (teacher-created or self-signup)

export async function onRequest(context) {
  const { request, env } = context;
  const token = request.headers.get('Authorization')?.replace('Bearer ', '');

  if (!token) return json({ error: 'Unauthorized' }, 401);

  const user = await verifyToken(token, env);
  if (!user) return json({ error: 'Invalid token' }, 401);

  if (request.method === 'GET') {
    return handleGetStudents(user, env);
  } else if (request.method === 'POST') {
    return handleCreateStudent(user, request, env);
  }
  return json({ error: 'Method not allowed' }, 405);
}

async function handleGetStudents(user, env) {
  // Teachers see their own students; admins see all
  const db = env.DB;
  const isAdmin = user.role === 'admin';
  const teacherId = isAdmin ? null : user.id;

  const query = isAdmin
    ? `SELECT s.*, c.id as class_id, c.name as class_name
       FROM students s
       LEFT JOIN class_enrollments ce ON s.id = ce.student_id
       LEFT JOIN classes c ON ce.class_id = c.id
       ORDER BY s.updated_at DESC`
    : `SELECT s.*, c.id as class_id, c.name as class_name
       FROM students s
       LEFT JOIN class_enrollments ce ON s.id = ce.student_id
       LEFT JOIN classes c ON ce.class_id = c.id
       WHERE s.teacher_id = ?
       ORDER BY s.updated_at DESC`;

  const params = isAdmin ? [] : [teacherId];
  const students = await db.prepare(query).bind(...params).all();

  return json(students.results || []);
}

async function handleCreateStudent(user, request, env) {
  if (user.role !== 'admin' && user.role !== 'teacher') {
    return json({ error: 'Only teachers can create students' }, 403);
  }

  const body = await request.json();
  const { name, email, class_id } = body;

  if (!name) return json({ error: 'Name required' }, 400);

  const db = env.DB;
  const teacherId = user.role === 'admin' ? body.teacher_id : user.id;

  try {
    // Create student record (no user_id yet if teacher-created without account)
    const stmt = db.prepare(`
      INSERT INTO students (teacher_id, name, email, status, created_at, updated_at)
      VALUES (?, ?, ?, 'active', ?, ?)
    `);
    const now = Date.now();
    const result = await stmt.bind(teacherId, name, email || null, now, now).run();

    const studentId = result.meta.last_row_id;

    // If class_id provided, enroll student
    if (class_id) {
      await db.prepare(`
        INSERT INTO class_enrollments (class_id, student_id, enrolled_at)
        VALUES (?, ?, ?)
      `).bind(class_id, studentId, now).run();
    }

    return json({ id: studentId, name, email, teacher_id: teacherId }, 201);
  } catch (err) {
    console.error('Create student error:', err);
    return json({ error: err.message }, 400);
  }
}

// Helper: Verify token (reused across APIs)
async function verifyToken(token, env) {
  const db = env.DB;
  const result = await db.prepare(`
    SELECT u.id, u.email, u.role
    FROM auth_tokens at
    JOIN users u ON at.user_id = u.id
    WHERE at.token = ? AND at.expires_at > ?
    LIMIT 1
  `).bind(token, Date.now()).first();

  return result;
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}
