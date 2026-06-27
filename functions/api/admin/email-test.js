// TEMPORARY debug endpoint — admin only. Calls Resend directly and returns the
// raw status + body so we can see why delivery fails. DELETE after diagnosing.
import { verifyTokenId as verifyToken } from '../_shared.js';

// Mirror of the normalizer in _lib/email.js so this debug path exercises the fix.
function normalizeFrom(raw) {
  const s = (raw || '').trim();
  const m = s.match(/<([^>]+)>/);
  if (m) {
    const email = m[1].trim();
    const name = s.slice(0, s.indexOf('<')).trim();
    return `${name || 'Word Play'} <${email}>`;
  }
  return s;
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status, headers: { 'Content-Type': 'application/json' }
  });
}

export async function onRequestPost(context) {
  const authHeader = context.request.headers.get('Authorization') || '';
  if (!authHeader.startsWith('Bearer ')) return json({ error: 'auth' }, 401);
  const userId = await verifyToken(authHeader.replace('Bearer ', ''), context.env.DB);
  if (!userId) return json({ error: 'token' }, 401);
  const user = await context.env.DB.prepare('SELECT role FROM users WHERE id = ?')
    .bind(userId).first();
  if (!user || user.role !== 'admin') return json({ error: 'admin only' }, 403);

  const env = context.env;
  const diag = {
    has_key: !!env.RESEND_API_KEY,
    key_prefix: env.RESEND_API_KEY ? env.RESEND_API_KEY.slice(0, 6) : null,
    from: env.RESEND_FROM || '(unset)',
    site_url: env.SITE_URL || '(unset)'
  };

  if (!env.RESEND_API_KEY) return json({ diag, sent: false, reason: 'no key' });

  const body = await context.request.json().catch(() => ({}));
  const to = body.to || 'emi.dom123@gmail.com';

  let resendStatus = null, resendBody = null, threw = null;
  try {
    const res = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${env.RESEND_API_KEY}`
      },
      body: JSON.stringify({
        from: normalizeFrom(env.RESEND_FROM) || 'Word Play <onboarding@resend.dev>',
        to,
        subject: 'Word Play email test',
        html: '<p>This is a Word Play email delivery test.</p>'
      })
    });
    resendStatus = res.status;
    resendBody = await res.text();
  } catch (e) {
    threw = String(e);
  }

  return json({ diag, to, resendStatus, resendBody, threw });
}
