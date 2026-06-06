// GET /api/students — List all students for logged-in teacher
// POST /api/students — Create a new student with auto-generated user account and passcode

import { verifyToken, json, requireRole } from '../_shared.js';

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

// Generate a random 6-character alphanumeric passcode
function generatePasscode() {
  return Math.random().toString(36).substring(2, 8).toUpperCase();
}

// Hash a password using simple PBKDF2 (Cloudflare Workers has built-in crypto)
async function hashPassword(password) {
  const encoder = new TextEncoder();
  const data = encoder.encode(password);
  const salt = crypto.getRandomValues(new Uint8Array(32));

  // PBKDF2: 100K iterations
  const key = await crypto.subtle.pbkdf2(data, salt, 100000, 32, 'SHA-256');

  // Return base64 encoded salt + hash
  const saltB64 = btoa(String.fromCharCode(...salt));
  const hashB64 = btoa(String.fromCharCode(...new Uint8Array(key)));
  return `${saltB64}:${hashB64}`;
}

async function handleCreateStudent(user, request, env) {
  try {
    requireRole(user, ['admin', 'teacher']);
  } catch (e) {
    return json({ error: e.message }, 403);
  }

  const body = await request.json();
  const { name, class_id } = body;

  if (!name) return json({ error: 'Name required' }, 400);

  const db = env.DB;
  const teacherId = user.role === 'admin' ? body.teacher_id : user.id;
  const now = Date.now();

  try {
    // Generate passcode and auto-generate email from name
    const passcode = generatePasscode();
    const autoEmail = `student_${Date.now().toString(36)}@wordplay.local`;
    const passwordHash = await hashPassword(passcode);

    // Create user account for student
    const userResult = await db.prepare(`
      INSERT INTO users (email, password_hash, role, created_at, updated_at)
      VALUES (?, ?, 'student', ?, ?)
    `).bind(autoEmail, passwordHash, now, now).run();

    const userId = userResult.meta.last_row_id;

    // Create student record linked to user
    const studentResult = await db.prepare(`
      INSERT INTO students (user_id, teacher_id, name, status, created_at, updated_at)
      VALUES (?, ?, ?, 'active', ?, ?)
    `).bind(userId, teacherId, name, now, now).run();

    const studentId = studentResult.meta.last_row_id;

    // If class_id provided, enroll student in class
    if (class_id) {
      await db.prepare(`
        INSERT INTO class_enrollments (class_id, student_id, enrolled_at)
        VALUES (?, ?, ?)
      `).bind(class_id, studentId, now).run();
    }

    // Return student info including passcode for teacher to share
    return json({
      id: studentId,
      user_id: userId,
      name,
      email: autoEmail,
      passcode,  // Teacher-only: share this with student
      teacher_id: teacherId,
      class_id: class_id || null
    }, 201);
  } catch (err) {
    console.error('Create student error:', err);
    return json({ error: err.message }, 400);
  }
}
