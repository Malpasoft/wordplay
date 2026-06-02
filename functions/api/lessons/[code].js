// Cloudflare Pages Function: GET/POST /api/lessons/:code
// Stores teacher lesson slots in D1, keyed by the same shared passphrase as profiles.
// Same D1 database (wordplay_db) — different table, no extra Cloudflare setup needed.

const MAX_BODY = 512 * 1024;
const ISO_DATE = /^\d{4}-\d{2}-\d{2}$/;
const HH_MM = /^\d{2}:\d{2}$/;
const VALID_TYPES = new Set(['1on1', 'group', 'academy', 'school', 'online']);

export async function onRequestGet({ params, env, request }) {
  const code = params.code || '';
  if (!isValidCode(code)) {
    return json({ error: 'code must be 8–64 characters' }, 400);
  }

  const url = new URL(request.url);
  const from = url.searchParams.get('from') || '';
  const to   = url.searchParams.get('to')   || '';

  if ((from && !ISO_DATE.test(from)) || (to && !ISO_DATE.test(to))) {
    return json({ error: 'from/to must be YYYY-MM-DD' }, 400);
  }

  let result;
  if (from && to) {
    result = await env.DB.prepare(
      'SELECT * FROM lessons WHERE code = ? AND date >= ? AND date <= ? ORDER BY date, time_start'
    ).bind(code, from, to).all();
  } else {
    result = await env.DB.prepare(
      'SELECT * FROM lessons WHERE code = ? ORDER BY date, time_start'
    ).bind(code).all();
  }

  const lessons = (result.results || []).map(function(row) {
    return Object.assign({}, row, {
      student_ids: JSON.parse(row.student_ids || '[]')
    });
  });
  return json({ lessons });
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

  const { action } = body;

  if (action === 'upsert') {
    return handleUpsert(env, code, body.lesson);
  } else if (action === 'delete') {
    return handleDelete(env, code, body.id);
  } else if (action === 'bulk') {
    return handleBulk(env, code, body.lessons);
  }
  return json({ error: 'unknown action' }, 400);
}

async function handleUpsert(env, code, lesson) {
  const err = validateLesson(lesson);
  if (err) return json({ error: err }, 400);

  const now = Date.now();
  await env.DB.prepare(`
    INSERT INTO lessons (id, code, title, student_ids, date, time_start, time_end,
                         type, location, notes, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(id) DO UPDATE SET
      title=excluded.title, student_ids=excluded.student_ids,
      date=excluded.date, time_start=excluded.time_start, time_end=excluded.time_end,
      type=excluded.type, location=excluded.location, notes=excluded.notes,
      updated_at=excluded.updated_at
  `).bind(
    lesson.id, code,
    lesson.title || '',
    JSON.stringify(Array.isArray(lesson.student_ids) ? lesson.student_ids : []),
    lesson.date, lesson.time_start, lesson.time_end,
    lesson.type || '1on1',
    lesson.location || '',
    lesson.notes || '',
    lesson.created_at || now, now
  ).run();

  return json({ ok: true, updated_at: now });
}

async function handleDelete(env, code, id) {
  if (!id || typeof id !== 'string') return json({ error: 'id required' }, 400);
  await env.DB.prepare(
    'DELETE FROM lessons WHERE id = ? AND code = ?'
  ).bind(id, code).run();
  return json({ ok: true });
}

async function handleBulk(env, code, lessons) {
  if (!Array.isArray(lessons) || lessons.length === 0) {
    return json({ error: 'lessons must be a non-empty array' }, 400);
  }
  if (lessons.length > 52) {
    return json({ error: 'bulk limit is 52 lessons' }, 400);
  }

  const now = Date.now();
  const stmts = lessons.map(function(l) {
    return env.DB.prepare(`
      INSERT INTO lessons (id, code, title, student_ids, date, time_start, time_end,
                           type, location, notes, created_at, updated_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
      ON CONFLICT(id) DO UPDATE SET
        title=excluded.title, student_ids=excluded.student_ids,
        date=excluded.date, time_start=excluded.time_start, time_end=excluded.time_end,
        type=excluded.type, location=excluded.location, notes=excluded.notes,
        updated_at=excluded.updated_at
    `).bind(
      l.id, code,
      l.title || '',
      JSON.stringify(Array.isArray(l.student_ids) ? l.student_ids : []),
      l.date, l.time_start, l.time_end,
      l.type || '1on1',
      l.location || '',
      l.notes || '',
      l.created_at || now, now
    );
  });

  await env.DB.batch(stmts);
  return json({ ok: true, count: lessons.length });
}

function validateLesson(l) {
  if (!l || typeof l !== 'object') return 'lesson object required';
  if (!l.id || typeof l.id !== 'string' || l.id.length > 64) return 'valid lesson.id required';
  if (!l.date || !ISO_DATE.test(l.date)) return 'lesson.date must be YYYY-MM-DD';
  if (!l.time_start || !HH_MM.test(l.time_start)) return 'lesson.time_start must be HH:MM';
  if (!l.time_end   || !HH_MM.test(l.time_end))   return 'lesson.time_end must be HH:MM';
  if (l.type && !VALID_TYPES.has(l.type)) return 'invalid lesson.type';
  return null;
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
