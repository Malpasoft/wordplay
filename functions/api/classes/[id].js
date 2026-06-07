// GET /api/classes/[id] — Get a single class
// PUT /api/classes/[id] — Edit a class
// DELETE /api/classes/[id] — Delete a class

import { verifyToken, json } from '../_shared.js';

export async function onRequest(context) {
  const { request, env, params } = context;
  const token = request.headers.get('Authorization')?.replace('Bearer ', '');

  if (!token) return json({ error: 'Unauthorized' }, 401);

  const user = await verifyToken(token, env);
  if (!user) return json({ error: 'Invalid token' }, 401);

  const classId = params.id;
  const db = env.DB;

  if (request.method === 'GET') {
    return handleGetClass(classId, user, db);
  } else if (request.method === 'PUT') {
    return handleUpdateClass(classId, user, request, db);
  } else if (request.method === 'DELETE') {
    return handleDeleteClass(classId, user, db);
  }
  return json({ error: 'Method not allowed' }, 405);
}

async function handleGetClass(classId, user, db) {
  try {
    const classData = await db.prepare(`
      SELECT c.*, COUNT(DISTINCT ce.student_id) as student_count
      FROM classes c
      LEFT JOIN class_enrollments ce ON c.id = ce.class_id
      WHERE c.id = ?
      GROUP BY c.id
    `).bind(classId).first();

    if (!classData) {
      return json({ error: 'Class not found' }, 404);
    }

    // Verify access
    if (user.role === 'teacher' && classData.teacher_id !== user.id) {
      return json({ error: 'Access denied' }, 403);
    }

    return json(classData);
  } catch (err) {
    console.error('Get class error:', err);
    return json({ error: err.message }, 400);
  }
}

async function handleUpdateClass(classId, user, request, db) {
  // Verify teacher owns this class
  const classData = await db.prepare(`
    SELECT teacher_id FROM classes WHERE id = ?
  `).bind(classId).first();

  if (!classData) {
    return json({ error: 'Class not found' }, 404);
  }

  if (user.role === 'teacher' && classData.teacher_id !== user.id) {
    return json({ error: 'Access denied' }, 403);
  }

  const body = await request.json();
  const { name, level, description } = body;

  if (!name) return json({ error: 'Name required' }, 400);

  try {
    await db.prepare(`
      UPDATE classes
      SET name = ?, level = ?, description = ?, updated_at = ?
      WHERE id = ?
    `).bind(name, level || null, description || null, Date.now(), classId).run();

    const updated = await db.prepare(`
      SELECT c.*, COUNT(DISTINCT ce.student_id) as student_count
      FROM classes c
      LEFT JOIN class_enrollments ce ON c.id = ce.class_id
      WHERE c.id = ?
      GROUP BY c.id
    `).bind(classId).first();

    return json(updated);
  } catch (err) {
    console.error('Update class error:', err);
    return json({ error: err.message }, 400);
  }
}

async function handleDeleteClass(classId, user, db) {
  // Verify teacher owns this class
  const classData = await db.prepare(`
    SELECT teacher_id FROM classes WHERE id = ?
  `).bind(classId).first();

  if (!classData) {
    return json({ error: 'Class not found' }, 404);
  }

  if (user.role === 'teacher' && classData.teacher_id !== user.id) {
    return json({ error: 'Access denied' }, 403);
  }

  try {
    await db.prepare(`
      DELETE FROM classes WHERE id = ?
    `).bind(classId).run();

    return json({ success: true });
  } catch (err) {
    console.error('Delete class error:', err);
    return json({ error: err.message }, 400);
  }
}
