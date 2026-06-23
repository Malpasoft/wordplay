// Teacher availability windows.
// GET  /api/availability?teacher_id=N — list windows (student linked to teacher, or the teacher)
// POST /api/availability — replace the teacher's windows (teacher only)
//      Body: { windows: [{ weekday, start_time, end_time, slot_minutes }] }

import { verifyToken, json } from './_shared.js';

export async function onRequestGet(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader?.startsWith('Bearer ')) return json({ error: 'Unauthorized' }, 401);
    const user = await verifyToken(authHeader.replace('Bearer ', ''), context.env);
    if (!user) return json({ error: 'Invalid or expired token' }, 401);

    const db = context.env.DB;
    const url = new URL(context.request.url);
    let teacherId = parseInt(url.searchParams.get('teacher_id') || '0');

    // Students may omit teacher_id — derive from their teacher link
    if (!teacherId && user.role === 'student') {
      const link = await db.prepare(
        'SELECT teacher_id FROM student_teachers WHERE student_id = ? LIMIT 1'
      ).bind(user.id).first();
      if (link) teacherId = link.teacher_id;
    }
    if (!teacherId && (user.role === 'teacher' || user.role === 'admin')) {
      teacherId = user.id;
    }
    if (!teacherId) return json({ windows: [], teacher_id: null });

    const rows = await db.prepare(
      'SELECT id, weekday, start_time, end_time, slot_minutes FROM availability WHERE teacher_id = ? ORDER BY weekday, start_time'
    ).bind(teacherId).all();

    return json({ teacher_id: teacherId, windows: rows.results || [] });
  } catch (err) {
    console.error('[availability GET]', err);
    return json({ error: 'Failed to load availability' }, 500);
  }
}

export async function onRequestPost(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader?.startsWith('Bearer ')) return json({ error: 'Unauthorized' }, 401);
    const user = await verifyToken(authHeader.replace('Bearer ', ''), context.env);
    if (!user) return json({ error: 'Invalid or expired token' }, 401);
    if (user.role !== 'teacher' && user.role !== 'admin') {
      return json({ error: 'Teacher access required' }, 403);
    }

    const body = await context.request.json();
    const windows = Array.isArray(body.windows) ? body.windows.slice(0, 50) : [];
    const db = context.env.DB;

    // Replace-all semantics: clear then insert
    await db.prepare('DELETE FROM availability WHERE teacher_id = ?').bind(user.id).run();

    const re = /^([01]\d|2[0-3]):[0-5]\d$/;
    let inserted = 0;
    for (const w of windows) {
      const wd = parseInt(w.weekday);
      if (isNaN(wd) || wd < 0 || wd > 6) continue;
      if (!re.test(w.start_time) || !re.test(w.end_time)) continue;
      if (w.end_time <= w.start_time) continue;
      const slot = Math.min(240, Math.max(15, parseInt(w.slot_minutes) || 60));
      await db.prepare(
        'INSERT INTO availability (teacher_id, weekday, start_time, end_time, slot_minutes) VALUES (?, ?, ?, ?, ?)'
      ).bind(user.id, wd, w.start_time, w.end_time, slot).run();
      inserted++;
    }

    return json({ ok: true, inserted });
  } catch (err) {
    console.error('[availability POST]', err);
    return json({ error: 'Failed to save availability' }, 500);
  }
}
