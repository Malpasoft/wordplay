// Word Play Teacher API — Invite code management
// GET /api/teacher/invite-code — list teacher's active invite codes
// POST /api/teacher/invite-code — generate new invite code
// DELETE /api/teacher/invite-code/[code_id] — revoke a code

import { checkRateLimit, verifyTokenId as verifyToken } from '../_shared.js';


async function getUserRole(userId, db) {
  const user = await db.prepare('SELECT role FROM users WHERE id = ?')
    .bind(userId)
    .first();
  return user ? user.role : null;
}

// Generate a random 8-character alphanumeric code
function generateInviteCode() {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  let code = '';
  const bytes = crypto.getRandomValues(new Uint8Array(6));
  for (let i = 0; i < 6; i++) {
    code += chars[bytes[i] % chars.length];
  }
  return code;
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}

export async function onRequestGet(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const teacherId = await verifyToken(token, context.env.DB);
    if (!teacherId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    const userRole = await getUserRole(teacherId, context.env.DB);
    if (userRole !== 'teacher' && userRole !== 'admin') {
      return json({ error: 'Teacher access required' }, 403);
    }

    const now = Date.now();

    // Fetch all non-revoked codes for this teacher
    const codes = await context.env.DB.prepare(
      `SELECT id, code, created_at, expires_at, uses_count, max_uses
       FROM invite_codes
       WHERE teacher_id = ? AND revoked = 0
       ORDER BY created_at DESC`
    ).bind(teacherId).all();

    const result = (codes.results || []).map(c => ({
      id: c.id,
      code: c.code,
      created_at: c.created_at,
      expires_at: c.expires_at,
      uses_count: c.uses_count,
      max_uses: c.max_uses === -1 ? null : c.max_uses,
      is_expired: c.expires_at < now,
      is_exhausted: c.max_uses > 0 && c.uses_count >= c.max_uses
    }));

    return json({ codes: result });
  } catch (error) {
    console.error('List invite codes error:', error);
    return json({ error: 'Failed to fetch invite codes' }, 500);
  }
}

export async function onRequestPost(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const teacherId = await verifyToken(token, context.env.DB);
    if (!teacherId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    const userRole = await getUserRole(teacherId, context.env.DB);
    if (userRole !== 'teacher' && userRole !== 'admin') {
      return json({ error: 'Teacher access required' }, 403);
    }

    // Rate limiting (D1-backed): max 10 codes per minute per teacher
    if (!(await checkRateLimit(context.env.DB, 'teacher_' + teacherId, 'invite-code', 10, 60000))) {
      return json({ error: 'Rate limit exceeded: max 10 codes per minute' }, 429);
    }

    const body = await context.request.json();
    const { days_until_expiry = 30, max_uses = -1 } = body;

    // Validate inputs
    if (days_until_expiry < 1 || days_until_expiry > 365) {
      return json({ error: 'days_until_expiry must be between 1 and 365' }, 400);
    }

    if (max_uses !== -1 && (max_uses < 1 || max_uses > 1000)) {
      return json({ error: 'max_uses must be -1 (unlimited) or between 1 and 1000' }, 400);
    }

    // Generate unique code
    let code;
    let attempts = 0;
    const maxAttempts = 10;

    do {
      code = generateInviteCode();
      const existing = await context.env.DB.prepare(
        'SELECT id FROM invite_codes WHERE code = ?'
      ).bind(code).first();

      if (!existing) break;
      attempts++;
    } while (attempts < maxAttempts);

    if (attempts >= maxAttempts) {
      return json({ error: 'Failed to generate unique code. Please try again.' }, 500);
    }

    const now = Date.now();
    const expiresAt = now + days_until_expiry * 24 * 60 * 60 * 1000;

    // Insert code
    const result = await context.env.DB.prepare(
      `INSERT INTO invite_codes (code, teacher_id, created_at, expires_at, max_uses, uses_count, revoked)
       VALUES (?, ?, ?, ?, ?, ?, 0)`
    )
      .bind(code, teacherId, now, expiresAt, max_uses, 0)
      .run();

    const codeId = result.meta.last_row_id;

    return json({
      id: codeId,
      code: code,
      created_at: now,
      expires_at: expiresAt,
      max_uses: max_uses === -1 ? null : max_uses,
      uses_count: 0,
      expires_in_days: days_until_expiry
    }, 201);
  } catch (error) {
    console.error('Generate invite code error:', error);
    return json({ error: 'Failed to generate invite code' }, 500);
  }
}

export async function onRequestDelete(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const teacherId = await verifyToken(token, context.env.DB);
    if (!teacherId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    const userRole = await getUserRole(teacherId, context.env.DB);
    if (userRole !== 'teacher' && userRole !== 'admin') {
      return json({ error: 'Teacher access required' }, 403);
    }

    const body = await context.request.json();
    const { code_id } = body;

    if (!code_id) {
      return json({ error: 'code_id is required' }, 400);
    }

    // Verify teacher owns this code
    const code = await context.env.DB.prepare(
      'SELECT id FROM invite_codes WHERE id = ? AND teacher_id = ?'
    )
      .bind(code_id, teacherId)
      .first();

    if (!code) {
      return json({ error: 'Code not found or not owned by this teacher' }, 404);
    }

    // Revoke the code
    await context.env.DB.prepare(
      'UPDATE invite_codes SET revoked = 1, updated_at = ? WHERE id = ?'
    )
      .bind(Date.now(), code_id)
      .run();

    return json({ message: 'Code revoked' });
  } catch (error) {
    console.error('Revoke invite code error:', error);
    return json({ error: 'Failed to revoke code' }, 500);
  }
}
