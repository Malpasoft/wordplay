// Booking requests.
// GET  /api/bookings — list bookings for the caller (student: own; teacher: incoming)
// POST /api/bookings — student creates a booking request
//      Body: { date, start_time, end_time, note }

import { verifyToken, json } from '../_shared.js';

const TIME_RE = /^([01]\d|2[0-3]):[0-5]\d$/;
const DATE_RE = /^\d{4}-\d{2}-\d{2}$/;

export async function onRequestGet(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader?.startsWith('Bearer ')) return json({ error: 'Unauthorized' }, 401);
    const user = await verifyToken(authHeader.replace('Bearer ', ''), context.env);
    if (!user) return json({ error: 'Invalid or expired token' }, 401);

    const db = context.env.DB;
    let rows;
    if (user.role === 'teacher' || user.role === 'admin') {
      rows = await db.prepare(
        `SELECT b.id, b.student_id, b.date, b.start_time, b.end_time, b.note, b.status, b.created_at,
                u.email AS student_email
         FROM booking_requests b JOIN users u ON b.student_id = u.id
         WHERE b.teacher_id = ? ORDER BY b.date DESC, b.start_time DESC`
      ).bind(user.id).all();
    } else {
      rows = await db.prepare(
        `SELECT b.id, b.teacher_id, b.date, b.start_time, b.end_time, b.note, b.status, b.created_at,
                u.email AS teacher_email
         FROM booking_requests b JOIN users u ON b.teacher_id = u.id
         WHERE b.student_id = ? ORDER BY b.date DESC, b.start_time DESC`
      ).bind(user.id).all();
    }

    return json({ bookings: rows.results || [] });
  } catch (err) {
    console.error('[bookings GET]', err);
    return json({ error: 'Failed to load bookings' }, 500);
  }
}

export async function onRequestPost(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader?.startsWith('Bearer ')) return json({ error: 'Unauthorized' }, 401);
    const user = await verifyToken(authHeader.replace('Bearer ', ''), context.env);
    if (!user) return json({ error: 'Invalid or expired token' }, 401);
    if (user.role !== 'student') return json({ error: 'Only students can request bookings.' }, 403);

    const { date, start_time, end_time, note } = await context.request.json();
    if (!DATE_RE.test(date || '') || !TIME_RE.test(start_time || '') || !TIME_RE.test(end_time || '')) {
      return json({ error: 'Invalid date or time.' }, 400);
    }
    if (end_time <= start_time) return json({ error: 'End time must be after start time.' }, 400);

    const db = context.env.DB;
    // Resolve the student's teacher
    const link = await db.prepare(
      'SELECT teacher_id FROM student_teachers WHERE student_id = ? LIMIT 1'
    ).bind(user.id).first();
    if (!link) return json({ error: 'You are not linked to a teacher yet. Use your teacher\'s invite code first.' }, 400);

    // Prevent duplicate pending/confirmed request for the same slot
    const dupe = await db.prepare(
      `SELECT id FROM booking_requests
       WHERE teacher_id = ? AND date = ? AND start_time = ? AND status IN ('pending','confirmed')`
    ).bind(link.teacher_id, date, start_time).first();
    if (dupe) return json({ error: 'That slot is already requested or booked.' }, 409);

    const now = Date.now();
    const res = await db.prepare(
      `INSERT INTO booking_requests (student_id, teacher_id, date, start_time, end_time, note, status, created_at, updated_at)
       VALUES (?, ?, ?, ?, ?, ?, 'pending', ?, ?)`
    ).bind(user.id, link.teacher_id, date, start_time, end_time, (note || '').slice(0, 300), now, now).run();

    return json({ ok: true, id: res.meta.last_row_id, status: 'pending' }, 201);
  } catch (err) {
    console.error('[bookings POST]', err);
    return json({ error: 'Failed to create booking' }, 500);
  }
}
