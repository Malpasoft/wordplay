// GET /api/auth/verify-email?token=<token>
// Marks the user's email as verified.
// Tokens are the same one-time reset tokens issued at signup (stored in password_resets
// with a special 72-hour expiry and type='verify').

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}

export async function onRequestGet(context) {
  try {
    const url = new URL(context.request.url);
    const token = url.searchParams.get('token');

    if (!token) {
      return json({ error: 'Verification token is required.' }, 400);
    }

    const now = Date.now();
    const row = await context.env.DB.prepare(
      'SELECT id, user_id FROM password_resets WHERE token = ? AND used = 0 AND expires_at > ?'
    ).bind(token, now).first();

    if (!row) {
      return json({ error: 'This verification link is invalid or has expired.' }, 400);
    }

    await context.env.DB.prepare(
      'UPDATE users SET email_verified = 1 WHERE id = ?'
    ).bind(row.user_id).run();

    await context.env.DB.prepare(
      'UPDATE password_resets SET used = 1 WHERE id = ?'
    ).bind(row.id).run();

    return json({ ok: true });
  } catch (err) {
    console.error('[verify-email]', err);
    return json({ error: 'Internal server error.' }, 500);
  }
}
