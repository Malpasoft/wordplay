// DELETE /api/lessons/[id] — Delete a lesson

import { verifyToken, json, requireRole } from '../_shared.js';

export async function onRequest(context) {
  const { request, env, params } = context;
  const token = request.headers.get('Authorization')?.replace('Bearer ', '');

  if (!token) return json({ error: 'Unauthorized' }, 401);

  const user = await verifyToken(token, env);
  if (!user) return json({ error: 'Invalid token' }, 401);

  if (request.method !== 'DELETE') {
    return json({ error: 'Method not allowed' }, 405);
  }

  try {
    requireRole(user, ['admin', 'teacher']);
  } catch (e) {
    return json({ error: e.message }, 403);
  }

  const lessonId = params.id;
  const db = env.DB;

  // Verify teacher owns this lesson's class
  const lesson = await db.prepare(`
    SELECT l.id, c.teacher_id
    FROM lessons l
    JOIN classes c ON l.class_id = c.id
    WHERE l.id = ?
  `).bind(lessonId).first();

  if (!lesson) {
    return json({ error: 'Lesson not found' }, 404);
  }

  if (user.role === 'teacher' && lesson.teacher_id !== user.id) {
    return json({ error: 'Access denied' }, 403);
  }

  try {
    await db.prepare('DELETE FROM lessons WHERE id = ?').bind(lessonId).run();
    return json({ success: true }, 200);
  } catch (err) {
    console.error('Delete lesson error:', err);
    return json({ error: err.message }, 400);
  }
}
