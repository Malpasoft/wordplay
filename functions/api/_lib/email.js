// Thin wrapper around Resend's transactional email API.
// Requires RESEND_API_KEY Cloudflare secret and RESEND_FROM env var
// (e.g. "Word Play <noreply@wordplay-38t.pages.dev>").
// See CLOUDFLARE_SETUP.md for provisioning instructions.

// Resend requires the `from` field to be either "email@example.com" or
// "Name <email@example.com>". A value like "<email@example.com>" (empty name)
// is rejected with a 422 validation_error, so we normalize defensively.
function normalizeFrom(raw) {
  const s = (raw || '').trim();
  const m = s.match(/<([^>]+)>/);
  if (m) {
    const email = m[1].trim();
    const name = s.slice(0, s.indexOf('<')).trim();
    return `${name || 'Word Play'} <${email}>`;
  }
  return s; // bare email address, or empty (caller falls back to default)
}

export async function sendEmail({ to, subject, html, env }) {
  const apiKey = env.RESEND_API_KEY;
  const from = normalizeFrom(env.RESEND_FROM) || 'Word Play <noreply@wordplay.app>';

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
