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
  const notReady = dbNotReady(env);
  if (notReady) return notReady;
  try {
    const row = await env.DB.prepare(
      'SELECT data, updated_at FROM teacher_profiles WHERE code = ?'
    ).bind(code).first();
    if (!row) {
      return json({ profiles: [], updated_at: null });
    }
    return json({ profiles: JSON.parse(row.data), updated_at: row.updated_at });
  } catch (e) {
    return dbError(e);
  }
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
  const notReady = dbNotReady(env);
  if (notReady) return notReady;
  try {
    const now = Date.now();
    await env.DB.prepare(
      `INSERT INTO teacher_profiles (code, data, updated_at)
       VALUES (?, ?, ?)
       ON CONFLICT(code) DO UPDATE SET data = excluded.data, updated_at = excluded.updated_at`
    ).bind(code, JSON.stringify(body.profiles), now).run();
    return json({ ok: true, updated_at: now });
  } catch (e) {
    return dbError(e);
  }
}

function isValidCode(c) {
  return typeof c === 'string' && c.length >= 8 && c.length <= 64;
}

// Returns a clear 503 if the D1 binding "DB" is missing (one-time Cloudflare
// setup not done), else null. See CLOUDFLARE_SETUP.md.
function dbNotReady(env) {
  if (!env || !env.DB) {
    return json({
      error: 'Cloud sync is not connected yet. In Cloudflare → Pages → ' +
             'wordplay-38t → Settings → Functions, add a D1 binding named ' +
             '"DB" pointing at wordplay_db, then redeploy.',
      reason: 'no_binding'
    }, 503);
  }
  return null;
}

// Turns a thrown D1 error into a plain-language response. A missing table
// means the database is bound but the migrations were never run.
function dbError(e) {
  const msg = (e && e.message) || String(e);
  if (/no such table/i.test(msg)) {
    return json({
      error: 'Database is connected but its tables have not been created. ' +
             'Open Cloudflare → D1 → wordplay_db → Console and run the SQL ' +
             'in migrations/0001_teacher_profiles.sql and 0002_lessons.sql.',
      reason: 'no_table'
    }, 503);
  }
  return json({ error: 'Database error: ' + msg, reason: 'db_error' }, 500);
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}
