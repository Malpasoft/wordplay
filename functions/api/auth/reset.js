// POST /api/auth/reset
// Body: { token, password }
// Consumes a valid reset token and sets a new PBKDF2 password hash.

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}

async function hashPassword(password, salt) {
  const encoder = new TextEncoder();
  const keyMaterial = await crypto.subtle.importKey(
    'raw',
    encoder.encode(password),
    { name: 'PBKDF2' },
    false,
    ['deriveBits']
  );
  const bits = await crypto.subtle.deriveBits(
    { name: 'PBKDF2', hash: 'SHA-256', salt: encoder.encode(salt), iterations: 100000 },
    keyMaterial,
    256
  );
  return Array.from(new Uint8Array(bits)).map(b => b.toString(16).padStart(2, '0')).join('');
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

    // Generate new salt + hash
    const saltChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let salt = '';
    const saltBytes = crypto.getRandomValues(new Uint8Array(8));
    for (let i = 0; i < 8; i++) salt += saltChars[saltBytes[i] % saltChars.length];

    const hash = await hashPassword(password, salt);
    const passwordHash = hash + ':' + salt;

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
