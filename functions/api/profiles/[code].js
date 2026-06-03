// GET /api/profiles/:code  — load all profiles for a sync code
// PUT /api/profiles/:code  — save profiles array (full replace)
export async function onRequest(context) {
  const { env, params, request } = context;
  const code = params.code;

  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, PUT, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  };

  if (request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers });
  }

  if (!env.DB) {
    return new Response(JSON.stringify({ error: 'DB not bound' }), { status: 503, headers });
  }

  if (code.length < 8 || code.length > 64) {
    return new Response(JSON.stringify({ error: 'Invalid sync code' }), { status: 400, headers });
  }

  if (request.method === 'GET') {
    const rows = await env.DB.prepare(
      'SELECT slug, name, l1, level, goals, notes, updated_at FROM profiles WHERE sync_code = ? ORDER BY id'
    ).bind(code).all();

    const updated_at = rows.results.length
      ? rows.results.reduce((a, b) => a.updated_at > b.updated_at ? a : b).updated_at
      : null;

    return new Response(JSON.stringify({ profiles: rows.results, updated_at }), { headers });
  }

  if (request.method === 'PUT') {
    let body;
    try { body = await request.json(); } catch {
      return new Response(JSON.stringify({ error: 'Invalid JSON' }), { status: 400, headers });
    }

    const profiles = Array.isArray(body.profiles) ? body.profiles : [];
    const now = new Date().toISOString();

    const stmts = profiles.map(p =>
      env.DB.prepare(
        `INSERT INTO profiles (sync_code, slug, name, l1, level, goals, notes, updated_at)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
         ON CONFLICT(sync_code, slug) DO UPDATE SET
           name=excluded.name, l1=excluded.l1, level=excluded.level,
           goals=excluded.goals, notes=excluded.notes, updated_at=excluded.updated_at`
      ).bind(code, p.slug || '', p.name || '', p.l1 || '', p.level || '', p.goals || '', p.notes || '', now)
    );

    if (stmts.length > 0) {
      await env.DB.batch(stmts);
    }

    return new Response(JSON.stringify({ ok: true, saved: stmts.length, updated_at: now }), { headers });
  }

  return new Response(JSON.stringify({ error: 'Method not allowed' }), { status: 405, headers });
}
