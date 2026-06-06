// Word Play Teacher API — Student management (teacher self-service)
// GET /api/teacher/students — list teacher's own students
// POST /api/teacher/students — create new student (rate-limited)
// DELETE /api/teacher/students/[student_id] — remove student from teacher's class

async function hashPassword(password, salt) {
  const encoder = new TextEncoder();
  const keyMaterial = await crypto.subtle.importKey(
    'raw',
    encoder.encode(password),
    { name: 'PBKDF2' },
    false,
    ['deriveBits']
  );
  const bits = await crypto.subtle.deriveBits(
    {
      name: 'PBKDF2',
      hash: 'SHA-256',
      salt: encoder.encode(salt),
      iterations: 100000
    },
    keyMaterial,
    256
  );
  const view = new Uint8Array(bits);
  return Array.from(view).map(b => b.toString(16).padStart(2, '0')).join('');
}

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
    const teacherId = await verifyToken(token, context.env.DB);
    if (!teacherId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    const userRole = await getUserRole(teacherId, context.env.DB);
    if (userRole !== 'teacher' && userRole !== 'admin') {
      return json({ error: 'Teacher access required' }, 403);
    }

    // Fetch teacher's students (via student_teachers join table)
    const students = await context.env.DB.prepare(
      `SELECT u.id, u.email, u.created_at
       FROM users u
       INNER JOIN student_teachers st ON u.id = st.student_id
       WHERE st.teacher_id = ? AND u.role = 'student'
       ORDER BY u.email`
    ).bind(teacherId).all();

    const result = (students.results || []).map(s => ({
      id: s.id,
      email: s.email,
      created_at: s.created_at
    }));

    return json({ students: result });
  } catch (error) {
    console.error('Student list error:', error);
    return json({ error: 'Failed to fetch students' }, 500);
  }
}

// Rate limiting: max 5 students per minute per teacher
const rateLimitStore = new Map();

function checkRateLimit(teacherId) {
  const now = Date.now();
  const key = `teacher_${teacherId}_students`;

  if (!rateLimitStore.has(key)) {
    rateLimitStore.set(key, []);
  }

  const timestamps = rateLimitStore.get(key);

  // Remove timestamps older than 60 seconds
  const recentTimestamps = timestamps.filter(t => now - t < 60000);

  if (recentTimestamps.length >= 5) {
    return false; // Rate limit exceeded
  }

  recentTimestamps.push(now);
  rateLimitStore.set(key, recentTimestamps);
  return true;
}

export async function onRequestPost(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const teacherId = await verifyToken(token, context.env.DB);
    if (!teacherId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    const userRole = await getUserRole(teacherId, context.env.DB);
    if (userRole !== 'teacher' && userRole !== 'admin') {
      return json({ error: 'Teacher access required' }, 403);
    }

    // Rate limiting: 5 students per minute
    if (!checkRateLimit(teacherId)) {
      return json({ error: 'Rate limit exceeded: max 5 students per minute' }, 429);
    }

    const body = await context.request.json();
    const { email, password, name, level } = body;

    if (!email || !password) {
      return json({ error: 'Email and password are required' }, 400);
    }

    if (password.length < 8) {
      return json({ error: 'Password must be at least 8 characters' }, 400);
    }

    const emailLower = email.toLowerCase();

    // Check if email already exists
    const existingUser = await context.env.DB.prepare('SELECT id FROM users WHERE email = ?')
      .bind(emailLower)
      .first();

    if (existingUser) {
      return json({ error: 'Email already in use' }, 409);
    }

    // Generate salt and hash password
    const saltChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let salt = '';
    const saltBytes = crypto.getRandomValues(new Uint8Array(8));
    for (let i = 0; i < 8; i++) {
      salt += saltChars[saltBytes[i] % saltChars.length];
    }

    const hash = await hashPassword(password, salt);
    const passwordHash = hash + ':' + salt;

    // Create user (always as 'student' role)
    const userResult = await context.env.DB.prepare(
      'INSERT INTO users (email, password_hash, role) VALUES (?, ?, ?)'
    )
      .bind(emailLower, passwordHash, 'student')
      .run();

    const studentId = userResult.meta.last_row_id;

    // Link student to teacher via student_teachers
    await context.env.DB.prepare(
      'INSERT INTO student_teachers (student_id, teacher_id) VALUES (?, ?)'
    )
      .bind(studentId, teacherId)
      .run();

    // Initialize empty progress for new student
    await context.env.DB.prepare(
      'INSERT INTO student_progress (user_id, progress_data) VALUES (?, ?)'
    )
      .bind(studentId, '{}')
      .run();

    // Initialize XP record
    await context.env.DB.prepare(
      'INSERT INTO user_xp (user_id, xp, streak) VALUES (?, ?, ?)'
    )
      .bind(studentId, 0, 0)
      .run();

    return json({
      student_id: studentId,
      email: emailLower,
      name: name || emailLower.split('@')[0],
      level: level || 'a1'
    }, 201);
  } catch (error) {
    console.error('Student creation error:', error);
    return json({ error: 'Failed to create student' }, 500);
  }
}

export async function onRequestDelete(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const teacherId = await verifyToken(token, context.env.DB);
    if (!teacherId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    const userRole = await getUserRole(teacherId, context.env.DB);
    if (userRole !== 'teacher' && userRole !== 'admin') {
      return json({ error: 'Teacher access required' }, 403);
    }

    // Parse student_id from URL or body
    let studentId;

    // First try to get from URL params (for /api/teacher/students/123)
    if (context.params && context.params.student_id) {
      studentId = parseInt(context.params.student_id);
    } else {
      // Fall back to body
      const body = await context.request.json();
      studentId = body.student_id;
    }

    if (!studentId) {
      return json({ error: 'Student ID is required' }, 400);
    }

    // Verify teacher owns this student before removal
    const relationship = await context.env.DB.prepare(
      'SELECT id FROM student_teachers WHERE student_id = ? AND teacher_id = ?'
    )
      .bind(studentId, teacherId)
      .first();

    if (!relationship) {
      return json({ error: 'Student not found or not assigned to this teacher' }, 404);
    }

    // Remove student from teacher's class (don't delete user, just unlink)
    await context.env.DB.prepare(
      'DELETE FROM student_teachers WHERE student_id = ? AND teacher_id = ?'
    )
      .bind(studentId, teacherId)
      .run();

    return json({ message: 'Student removed from class' });
  } catch (error) {
    console.error('Student deletion error:', error);
    return json({ error: 'Failed to remove student' }, 500);
  }
}
