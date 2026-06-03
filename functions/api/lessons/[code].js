// GET /api/lessons/:code       — load all lessons for a sync code
// PUT /api/lessons/:code       — upsert lessons array
// DELETE /api/lessons/:code    — delete a single lesson by lesson_id (body: {lesson_id})
export async function onRequest(context) {
  const { env, params, request } = context;
  const code = params.code;

  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, PUT, DELETE, OPTIONS',
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
      'SELECT lesson_id, date, student, title, notes, done, updated_at FROM lessons WHERE sync_code = ? ORDER BY date, id'
    ).bind(code).all();

    const updated_at = rows.results.length
      ? rows.results.reduce((a, b) => a.updated_at > b.updated_at ? a : b).updated_at
      : null;

    return new Response(JSON.stringify({ lessons: rows.results, updated_at }), { headers });
  }

  if (request.method === 'PUT') {
    let body;
    try { body = await request.json(); } catch {
      return new Response(JSON.stringify({ error: 'Invalid JSON' }), { status: 400, headers });
    }

    const lessons = Array.isArray(body.lessons) ? body.lessons : [];
    const now = new Date().toISOString();

    const stmts = lessons.map(l =>
      env.DB.prepare(
        `INSERT INTO lessons (sync_code, lesson_id, date, student, title, notes, done, updated_at)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
         ON CONFLICT(sync_code, lesson_id) DO UPDATE SET
           date=excluded.date, student=excluded.student, title=excluded.title,
           notes=excluded.notes, done=excluded.done, updated_at=excluded.updated_at`
      ).bind(code, l.lesson_id || '', l.date || '', l.student || '', l.title || '', l.notes || '', l.done ? 1 : 0, now)
    );

    if (stmts.length > 0) {
      await env.DB.batch(stmts);
    }

    return new Response(JSON.stringify({ ok: true, saved: stmts.length, updated_at: now }), { headers });
  }

  if (request.method === 'DELETE') {
    let body;
    try { body = await request.json(); } catch {
      return new Response(JSON.stringify({ error: 'Invalid JSON' }), { status: 400, headers });
    }

    if (!body.lesson_id) {
      return new Response(JSON.stringify({ error: 'lesson_id required' }), { status: 400, headers });
    }

    await env.DB.prepare(
      'DELETE FROM lessons WHERE sync_code = ? AND lesson_id = ?'
    ).bind(code, body.lesson_id).run();

    return new Response(JSON.stringify({ ok: true }), { headers });
  }

  return new Response(JSON.stringify({ error: 'Method not allowed' }), { status: 405, headers });
}
