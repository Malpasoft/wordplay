// Update a booking request.
// PUT /api/bookings/[id] — Body: { status: 'confirmed'|'declined'|'cancelled' }
//   teacher: confirm/decline; student: cancel own. On confirm, emails the student.

import { verifyToken, json } from '../_shared.js';
import { sendEmail } from '../_lib/email.js';

export async function onRequestPut(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader?.startsWith('Bearer ')) return json({ error: 'Unauthorized' }, 401);
    const user = await verifyToken(authHeader.replace('Bearer ', ''), context.env);
    if (!user) return json({ error: 'Invalid or expired token' }, 401);

    const id = parseInt(context.params.id);
    const { status } = await context.request.json();
    if (!['confirmed', 'declined', 'cancelled'].includes(status)) {
      return json({ error: 'Invalid status.' }, 400);
    }

    const db = context.env.DB;
    const booking = await db.prepare(
      `SELECT b.*, su.email AS student_email, tu.email AS teacher_email
       FROM booking_requests b
       JOIN users su ON b.student_id = su.id
       JOIN users tu ON b.teacher_id = tu.id
       WHERE b.id = ?`
    ).bind(id).first();

    if (!booking) return json({ error: 'Booking not found.' }, 404);

    // Authorization: teacher can confirm/decline their bookings; student can cancel own
    const isTeacher = (user.role === 'teacher' || user.role === 'admin') && user.id === booking.teacher_id;
    const isOwnerStudent = user.role === 'student' && user.id === booking.student_id;

    if (status === 'cancelled') {
      if (!isOwnerStudent && !isTeacher) return json({ error: 'Not allowed.' }, 403);
    } else {
      if (!isTeacher) return json({ error: 'Only the teacher can confirm or decline.' }, 403);
    }

    await db.prepare(
      'UPDATE booking_requests SET status = ?, updated_at = ? WHERE id = ?'
    ).bind(status, Date.now(), id).run();

    // Notify the student when the teacher confirms or declines
    if ((status === 'confirmed' || status === 'declined') && booking.student_email) {
      const niceDate = booking.date;
      const subject = status === 'confirmed'
        ? `Lesson confirmed: ${niceDate} at ${booking.start_time}`
        : `Lesson request declined: ${niceDate}`;
      const body = status === 'confirmed'
        ? `<p style="color:#444;line-height:1.6">Your lesson on <strong>${niceDate}</strong> at
             <strong>${booking.start_time}–${booking.end_time}</strong> is confirmed. See you then!</p>`
        : `<p style="color:#444;line-height:1.6">Unfortunately your lesson request for
             <strong>${niceDate}</strong> at <strong>${booking.start_time}</strong> could not be confirmed.
             Please pick another slot, or message your teacher.</p>`;
      await sendEmail({
        to: booking.student_email,
        subject,
        html: `<div style="font-family:system-ui,sans-serif;max-width:480px;margin:0 auto;padding:32px 24px">
                 <h2 style="font-size:1.3rem;margin:0 0 12px;color:#1A1A1A">Word Play</h2>${body}
                 <p style="margin-top:20px"><a href="${context.env.SITE_URL || 'https://wordplay-38t.pages.dev'}/book.html"
                   style="color:#B8860B">View your bookings</a></p>
               </div>`,
        env: context.env
      });
    }

    return json({ ok: true, status });
  } catch (err) {
    console.error('[bookings PUT]', err);
    return json({ error: 'Failed to update booking' }, 500);
  }
}
