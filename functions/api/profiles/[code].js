// Cloudflare Pages Function: GET/POST /api/profiles/:code
// Stores teacher profiles in D1 keyed by a shared passphrase.
// B1 upgrade path: add auth middleware + /api/profiles (cookie-based) without
// removing this route — existing clients keep working during the transition.

const MAX_BODY = 512 * 1024;

export async function onRequestGet({ params, env }) {
  const code = params.code || '';
  if (!isValidCode(code)) {
    return json({ error: 'code must be 8–64 characters' }, 400);
  }
  const row = await env.DB.prepare(
    'SELECT data, updated_at FROM teacher_profiles WHERE code = ?'
  ).bind(code).first();
  if (!row) {
    return json({ profiles: [], updated_at: null });
  }
  return json({ profiles: JSON.parse(row.data), updated_at: row.updated_at });
}

export async function onRequestPost({ params, env, request }) {
  const code = params.code || '';
  if (!isValidCode(code)) {
    return json({ error: 'code must be 8–64 characters' }, 400);
  }
  const contentLength = parseInt(request.headers.get('content-length') || '0');
  if (contentLength > MAX_BODY) {
    return json({ error: 'payload too large' }, 413);
  }
  let body;
  try {
    body = await request.json();
  } catch {
    return json({ error: 'invalid JSON' }, 400);
  }
  if (!Array.isArray(body.profiles)) {
    return json({ error: 'profiles must be an array' }, 400);
  }
  const now = Date.now();
  await env.DB.prepare(
    `INSERT INTO teacher_profiles (code, data, updated_at)
     VALUES (?, ?, ?)
     ON CONFLICT(code) DO UPDATE SET data = excluded.data, updated_at = excluded.updated_at`
  ).bind(code, JSON.stringify(body.profiles), now).run();
  return json({ ok: true, updated_at: now });
}

function isValidCode(c) {
  return typeof c === 'string' && c.length >= 8 && c.length <= 64;
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}
