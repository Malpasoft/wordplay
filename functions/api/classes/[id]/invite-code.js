// POST /api/classes/[id]/invite-code/generate — Generate invite code for a class

import { verifyToken, json, requireRole } from '../../_shared.js';

// Cryptographically-random alphanumeric code (uppercase + digits).
function generateCode(len) {
  const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const bytes = crypto.getRandomValues(new Uint8Array(len));
  let out = '';
  for (let i = 0; i < len; i++) out += chars[bytes[i] % chars.length];
  return out;
}

export async function onRequest(context) {
  const { request, env, params } = context;
  const token = request.headers.get('Authorization')?.replace('Bearer ', '');

  if (!token) return json({ error: 'Unauthorized' }, 401);

  const user = await verifyToken(token, env);
  if (!user) return json({ error: 'Invalid token' }, 401);

  if (request.method !== 'POST') {
    return json({ error: 'Method not allowed' }, 405);
  }

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

  // Generate unique code (10 alphanumeric chars, cryptographically random)
  const code = generateCode(10);
  const expiresAt = Date.now() + (30 * 24 * 60 * 60 * 1000); // 30 days

  try {
    const result = await db.prepare(`
      INSERT INTO class_invite_codes (class_id, code, created_at, expires_at, max_uses, used_count)
      VALUES (?, ?, ?, ?, -1, 0)
    `).bind(classId, code, Date.now(), expiresAt).run();

    return json({ code, expires_at: expiresAt }, 201);
  } catch (err) {
    console.error('Generate code error:', err);
    return json({ error: err.message }, 400);
  }
}
