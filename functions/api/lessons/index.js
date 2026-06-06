// GET /api/lessons?class_id=X — List lessons for a class
// POST /api/lessons — Create a lesson

import { verifyToken, json, requireRole } from '../_shared.js';

export async function onRequest(context) {
  const { request, env } = context;
  const token = request.headers.get('Authorization')?.replace('Bearer ', '');

  if (!token) return json({ error: 'Unauthorized' }, 401);

  const user = await verifyToken(token, env);
  if (!user) return json({ error: 'Invalid token' }, 401);

  if (request.method === 'GET') {
    return handleGetLessons(user, request, env);
  } else if (request.method === 'POST') {
    return handleCreateLesson(user, request, env);
  }
  return json({ error: 'Method not allowed' }, 405);
}

async function handleGetLessons(user, request, env) {
  try {
    requireRole(user, ['admin', 'teacher', 'student']);
  } catch (e) {
    return json({ error: e.message }, 403);
  }

  const url = new URL(request.url);
  const classId = url.searchParams.get('class_id');

  if (!classId) {
    return json({ error: 'class_id required' }, 400);
  }

  const db = env.DB;

  // Check access: teacher can see own class lessons, student can see their enrolled classes
  if (user.role === 'teacher') {
    const classOwner = await db.prepare(`
      SELECT teacher_id FROM classes WHERE id = ?
    `).bind(classId).first();

    if (!classOwner || classOwner.teacher_id !== user.id) {
      return json({ error: 'Access denied' }, 403);
    }
  } else if (user.role === 'student') {
    // Check if student is enrolled
    const enrolled = await db.prepare(`
      SELECT ce.id FROM class_enrollments ce
      JOIN students s ON ce.student_id = s.id
      WHERE ce.class_id = ? AND s.user_id = ?
    `).bind(classId, user.id).first();

    if (!enrolled) {
      return json({ error: 'Not enrolled in this class' }, 403);
    }
  }

  const result = await db.prepare(`
    SELECT * FROM lessons
    WHERE class_id = ?
    ORDER BY date ASC
  `).bind(classId).all();

  return json(result.results || []);
}

async function handleCreateLesson(user, request, env) {
  try {
    requireRole(user, ['admin', 'teacher']);
  } catch (e) {
    return json({ error: e.message }, 403);
  }

  const body = await request.json();
  const { class_id, date, time_start, time_end, chapter_slug, title, type, level, location, notes } = body;

  if (!class_id || !date || !title) {
    return json({ error: 'class_id, date, and title required' }, 400);
  }

  const db = env.DB;

  // Verify teacher owns this class
  const classOwner = await db.prepare(`
    SELECT teacher_id FROM classes WHERE id = ?
  `).bind(class_id).first();

  if (!classOwner || (user.role === 'teacher' && classOwner.teacher_id !== user.id)) {
    return json({ error: 'Access denied' }, 403);
  }

  const now = Date.now();

  try {
    const result = await db.prepare(`
      INSERT INTO lessons (class_id, date, time_start, time_end, chapter_slug, title, type, level, location, notes, created_at, updated_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `).bind(class_id, date, time_start || null, time_end || null, chapter_slug || null, title, type || '1on1', level || null, location || null, notes || null, now, now).run();

    return json({
      id: result.meta.last_row_id,
      class_id,
      date,
      time_start,
      time_end,
      chapter_slug,
      title,
      type: type || '1on1',
      level,
      location,
      notes
    }, 201);
  } catch (err) {
    console.error('Create lesson error:', err);
    return json({ error: err.message }, 400);
  }
}
