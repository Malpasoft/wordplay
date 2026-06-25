// POST /api/auth/reset
// Body: { token, password }
// Consumes a valid reset token and sets a new PBKDF2 password hash.

import { makePasswordHash } from '../_lib/crypto.js';

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}

export async function onRequestPost(context) {
  try {
    const { token, password } = await context.request.json();

    if (!token || !password) {
      return json({ error: 'Token and new password are required.' }, 400);
    }

    if (password.length < 8) {
      return json({ error: 'Password must be at least 8 characters.' }, 400);
    }

    const now = Date.now();
    const row = await context.env.DB.prepare(
      'SELECT id, user_id FROM password_resets WHERE token = ? AND used = 0 AND expires_at > ?'
    ).bind(token, now).first();

    if (!row) {
      return json({ error: 'This reset link is invalid or has expired.' }, 400);
    }

    // Generate new salt + PBKDF2 hash
    const passwordHash = await makePasswordHash(password);

    // Update password and mark token used in one go
    await context.env.DB.prepare(
      'UPDATE users SET password_hash = ?, updated_at = ? WHERE id = ?'
    ).bind(passwordHash, now, row.user_id).run();

    await context.env.DB.prepare(
      'UPDATE password_resets SET used = 1 WHERE id = ?'
    ).bind(row.id).run();

    // Revoke all active sessions so old sessions can't continue
    await context.env.DB.prepare(
      'DELETE FROM auth_tokens WHERE user_id = ?'
    ).bind(row.user_id).run();

    return json({ ok: true });
  } catch (err) {
    console.error('[reset]', err);
    return json({ error: 'Internal server error.' }, 500);
  }
}
