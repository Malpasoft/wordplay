// GET /api/admin/errors — recent production errors (admin only).
// Supports ?limit=N (default 50, max 200).

import { verifyToken, json, requireRole } from '../_shared.js';

export async function onRequestGet(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader?.startsWith('Bearer ')) return json({ error: 'Unauthorized' }, 401);
    const user = await verifyToken(authHeader.replace('Bearer ', ''), context.env);
    if (!user) return json({ error: 'Invalid or expired token' }, 401);
    try { requireRole(user, ['admin']); } catch (e) { return json({ error: e.message }, 403); }

    const url = new URL(context.request.url);
    const limit = Math.min(200, Math.max(1, parseInt(url.searchParams.get('limit') || '50')));

    const rows = await context.env.DB.prepare(
      'SELECT id, path, method, status, message, created_at FROM error_log ORDER BY created_at DESC LIMIT ?'
    ).bind(limit).all();

    return json({ errors: rows.results || [] });
  } catch (err) {
    console.error('[admin/errors]', err);
    return json({ error: 'Failed to load errors' }, 500);
  }
}
