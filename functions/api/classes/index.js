// GET /api/classes — List teacher's classes
// POST /api/classes — Create a new class

import { verifyToken, json } from '../_shared.js';

export async function onRequest(context) {
  const { request, env } = context;
  const token = request.headers.get('Authorization')?.replace('Bearer ', '');

  if (!token) return json({ error: 'Unauthorized' }, 401);

  const user = await verifyToken(token, env);
  if (!user) return json({ error: 'Invalid token' }, 401);

  if (request.method === 'GET') {
    return handleGetClasses(user, env);
  } else if (request.method === 'POST') {
    return handleCreateClass(user, request, env);
  }
  return json({ error: 'Method not allowed' }, 405);
}

async function handleGetClasses(user, env) {
  const db = env.DB;

  if (user.role !== 'admin' && user.role !== 'teacher') {
    return json({ error: 'Only teachers can view classes' }, 403);
  }

  const teacherId = user.role === 'admin' ? null : user.id;

  const query = user.role === 'admin'
    ? `SELECT c.*, COUNT(DISTINCT ce.student_id) as student_count
       FROM classes c
       LEFT JOIN class_enrollments ce ON c.id = ce.class_id
       GROUP BY c.id
       ORDER BY c.created_at DESC`
    : `SELECT c.*, COUNT(DISTINCT ce.student_id) as student_count
       FROM classes c
       LEFT JOIN class_enrollments ce ON c.id = ce.class_id
       WHERE c.teacher_id = ?
       GROUP BY c.id
       ORDER BY c.created_at DESC`;

  const params = user.role === 'admin' ? [] : [teacherId];
  const result = await db.prepare(query).bind(...params).all();

  return json(result.results || []);
}

async function handleCreateClass(user, request, env) {
  if (user.role !== 'admin' && user.role !== 'teacher') {
    return json({ error: 'Only teachers can create classes' }, 403);
  }

  const body = await request.json();
  const { name, level, description } = body;

  if (!name) return json({ error: 'Name required' }, 400);

  const db = env.DB;
  const now = Date.now();

  try {
    const result = await db.prepare(`
      INSERT INTO classes (teacher_id, name, level, description, created_at, updated_at)
      VALUES (?, ?, ?, ?, ?, ?)
    `).bind(user.id, name, level || null, description || null, now, now).run();

    return json({
      id: result.meta.last_row_id,
      teacher_id: user.id,
      name,
      level,
      description,
      student_count: 0
    }, 201);
  } catch (err) {
    console.error('Create class error:', err);
    return json({ error: err.message }, 400);
  }
}
