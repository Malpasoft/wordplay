// POST /api/classes/join — Join a class using invite code

import { verifyToken, json } from '../_shared.js';

export async function onRequest(context) {
  const { request, env } = context;
  const token = request.headers.get('Authorization')?.replace('Bearer ', '');

  if (!token) return json({ error: 'Unauthorized' }, 401);

  const user = await verifyToken(token, env);
  if (!user) return json({ error: 'Invalid token' }, 401);

  if (request.method !== 'POST') {
    return json({ error: 'Method not allowed' }, 405);
  }

  const body = await request.json();
  const { code } = body;

  if (!code) return json({ error: 'Invite code required' }, 400);

  const db = env.DB;

  // Find and validate code
  const inviteData = await db.prepare(`
    SELECT ic.id, ic.class_id, ic.expires_at, ic.max_uses, ic.used_count
    FROM invite_codes ic
    WHERE ic.code = ? AND (ic.expires_at IS NULL OR ic.expires_at > ?)
    LIMIT 1
  `).bind(code, Date.now()).first();

  if (!inviteData) {
    return json({ error: 'Invalid or expired invite code' }, 400);
  }

  if (inviteData.max_uses !== -1 && inviteData.used_count >= inviteData.max_uses) {
    return json({ error: 'Invite code limit reached' }, 400);
  }

  // Get or create student record for this user (unified system)
  const student = await db.prepare(`
    SELECT id FROM students WHERE user_id = ?
  `).bind(user.id).first();

  let studentId = student?.id;

  if (!studentId) {
    // Auto-create student record linked to user's account
    const now = Date.now();
    const result = await db.prepare(`
      INSERT INTO students (user_id, teacher_id, name, status, created_at, updated_at)
      VALUES (?, (SELECT teacher_id FROM classes WHERE id = ?), ?, 'active', ?, ?)
    `).bind(user.id, inviteData.class_id, user.email || 'Student', now, now).run();

    studentId = result.meta.last_row_id;
  }

  // Check if already enrolled
  const enrolled = await db.prepare(`
    SELECT id FROM class_enrollments
    WHERE class_id = ? AND student_id = ?
  `).bind(inviteData.class_id, studentId).first();

  if (enrolled) {
    return json({ error: 'Already enrolled in this class' }, 400);
  }

  // Enroll student
  await db.prepare(`
    INSERT INTO class_enrollments (class_id, student_id, enrolled_at)
    VALUES (?, ?, ?)
  `).bind(inviteData.class_id, studentId, Date.now()).run();

  // Increment usage
  await db.prepare(`
    UPDATE invite_codes SET used_count = used_count + 1 WHERE id = ?
  `).bind(inviteData.id).run();

  return json({ class_id: inviteData.class_id, student_id: studentId }, 200);
}
