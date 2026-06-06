// POST /api/classes/[id]/invite-code — Generate invite code for a class
// POST /api/classes/join — Join a class using invite code

import { verifyToken, json, requireRole } from '../_shared.js';

export async function onRequest(context) {
  const { request, env, params } = context;
  const token = request.headers.get('Authorization')?.replace('Bearer ', '');

  if (!token) return json({ error: 'Unauthorized' }, 401);

  const user = await verifyToken(token, env);
  if (!user) return json({ error: 'Invalid token' }, 401);

  const url = new URL(request.url);
  if (url.pathname.includes('/invite-code')) {
    if (request.method === 'POST' && url.pathname.includes('/generate')) {
      return handleGenerateCode(user, params, request, env);
    } else if (request.method === 'POST' && url.pathname.includes('/join')) {
      return handleJoinViaCode(user, request, env);
    }
  }

  return json({ error: 'Method not allowed' }, 405);
}

async function handleGenerateCode(user, params, request, env) {
  try {
    requireRole(user, ['admin', 'teacher']);
  } catch (e) {
    return json({ error: e.message }, 403);
  }

  const classId = params.id;
  const db = env.DB;

  // Verify teacher owns this class
  const classData = await db.prepare(`
    SELECT teacher_id FROM classes WHERE id = ?
  `).bind(classId).first();

  if (!classData || (user.role === 'teacher' && classData.teacher_id !== user.id)) {
    return json({ error: 'Access denied' }, 403);
  }

  // Generate unique code (6 alphanumeric chars)
  const code = Math.random().toString(36).substring(2, 8).toUpperCase();
  const expiresAt = Date.now() + (30 * 24 * 60 * 60 * 1000); // 30 days

  try {
    const result = await db.prepare(`
      INSERT INTO invite_codes (class_id, code, created_at, expires_at, max_uses, used_count)
      VALUES (?, ?, ?, ?, -1, 0)
    `).bind(classId, code, Date.now(), expiresAt).run();

    return json({ code, expires_at: expiresAt }, 201);
  } catch (err) {
    console.error('Generate code error:', err);
    return json({ error: err.message }, 400);
  }
}

async function handleJoinViaCode(user, request, env) {
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

  // Get or create student record for this user
  const student = await db.prepare(`
    SELECT id FROM students WHERE user_id = ?
  `).bind(user.id).first();

  let studentId = student?.id;

  if (!studentId) {
    // Create student record if doesn't exist
    const result = await db.prepare(`
      INSERT INTO students (user_id, teacher_id, name, status, created_at, updated_at)
      VALUES (?, (SELECT teacher_id FROM classes WHERE id = ?), ?, 'active', ?, ?)
    `).bind(user.id, inviteData.class_id, user.email, Date.now(), Date.now()).run();

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
