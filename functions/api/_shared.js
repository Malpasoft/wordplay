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
