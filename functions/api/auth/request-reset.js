// POST /api/auth/request-reset
// Body: { email }
// Issues a short-lived (1-hour) reset token and emails a link.
// Always returns 200 to prevent email enumeration.

import { sendEmail } from '../_lib/email.js';

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}

function generateToken() {
  const bytes = crypto.getRandomValues(new Uint8Array(32));
  return Array.from(bytes).map(b => b.toString(16).padStart(2, '0')).join('');
}

export async function onRequestPost(context) {
  try {
    const { email } = await context.request.json();

    if (!email || typeof email !== 'string') {
      return json({ error: 'Email is required.' }, 400);
    }

    const emailLower = email.toLowerCase().trim();
    const user = await context.env.DB.prepare(
      'SELECT id, email FROM users WHERE email = ?'
    ).bind(emailLower).first();

    // Always return the same response to prevent email enumeration
    if (!user) {
      return json({ ok: true });
    }

    // Expire any existing unused tokens for this user
    await context.env.DB.prepare(
      'UPDATE password_resets SET used = 1 WHERE user_id = ? AND used = 0'
    ).bind(user.id).run();

    const token = generateToken();
    const expiresAt = Date.now() + 60 * 60 * 1000; // 1 hour

    await context.env.DB.prepare(
      'INSERT INTO password_resets (user_id, token, expires_at) VALUES (?, ?, ?)'
    ).bind(user.id, token, expiresAt).run();

    const baseUrl = context.env.SITE_URL || 'https://wordplay-38t.pages.dev';
    const resetUrl = `${baseUrl}/reset.html?token=${token}`;

    await sendEmail({
      to: user.email,
      subject: 'Reset your Word Play password',
      html: `
        <div style="font-family:system-ui,sans-serif;max-width:480px;margin:0 auto;padding:32px 24px">
          <h2 style="font-size:1.4rem;margin:0 0 16px;color:#1A1A1A">Reset your password</h2>
          <p style="color:#444;line-height:1.6;margin:0 0 24px">
            Click the button below to set a new password. This link expires in 1 hour.
          </p>
          <a href="${resetUrl}" style="display:inline-block;padding:12px 24px;background:#B8860B;color:#fff;text-decoration:none;border-radius:4px;font-weight:600">
            Reset password
          </a>
          <p style="color:#999;font-size:.8rem;margin:24px 0 0;line-height:1.5">
            If you did not request this, ignore this email — your password has not changed.
          </p>
        </div>
      `,
      env: context.env
    });

    return json({ ok: true });
  } catch (err) {
    console.error('[request-reset]', err);
    return json({ ok: true }); // still return ok to prevent enumeration
  }
}
