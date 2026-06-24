// Shared utilities for all API endpoints

export async function verifyToken(token, env) {
  const db = env.DB;
  const result = await db.prepare(`
    SELECT u.id, u.email, u.role
    FROM auth_tokens at
    JOIN users u ON at.user_id = u.id
    WHERE at.token = ? AND at.expires_at > ?
    LIMIT 1
  `).bind(token, Date.now()).first();

  return result;
}

export function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

export function requireRole(user, allowedRoles) {
  if (!allowedRoles.includes(user.role)) {
    throw new Error(`Requires ${allowedRoles.join(' or ')}`);
  }
}

// D1-backed sliding-window rate limiter (persists across worker restarts).
// identity = stable key for the actor (e.g. `teacher_<id>` or an IP).
// Returns true if the action is allowed, false if the limit is exceeded.
// Fails open (returns true) if the rate_limit_log table is unavailable.
export async function checkRateLimit(db, identity, endpoint, limit, windowMs) {
  const now = Date.now();
  try {
    const since = now - windowMs;
    const row = await db.prepare(
      'SELECT COUNT(*) AS count FROM rate_limit_log WHERE ip = ? AND endpoint = ? AND timestamp > ?'
    ).bind(identity, endpoint, since).first();
    if ((row?.count || 0) >= limit) return false;
    await db.prepare(
      'INSERT INTO rate_limit_log (ip, endpoint, timestamp) VALUES (?, ?, ?)'
    ).bind(identity, endpoint, now).run();
  } catch (e) {
    console.warn('[rate-limit] check failed (allowing):', e.message);
  }
  return true;
}
