// Thin wrapper around Resend's transactional email API.
// Requires RESEND_API_KEY Cloudflare secret and RESEND_FROM env var
// (e.g. "Word Play <noreply@wordplay-38t.pages.dev>").
// See CLOUDFLARE_SETUP.md for provisioning instructions.

export async function sendEmail({ to, subject, html, env }) {
  const apiKey = env.RESEND_API_KEY;
  const from = env.RESEND_FROM || 'Word Play <noreply@wordplay.app>';

  if (!apiKey) {
    console.warn('[email] RESEND_API_KEY not set — email not sent to', to);
    return { ok: false, error: 'Email service not configured' };
  }

  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey}`
    },
    body: JSON.stringify({ from, to, subject, html })
  });

  if (!res.ok) {
    const body = await res.text().catch(() => '');
    console.error('[email] Resend error', res.status, body);
    return { ok: false, error: `Resend ${res.status}` };
  }

  return { ok: true };
}
