// Student mistake analytics
// POST /api/student/mistakes — batch-insert wrong answers { mistakes: [...] }
// GET  /api/student/mistakes — aggregated weakness report for the dashboard
//
// Each mistake: { level, chapter_slug, question_id, skill_tag, expected, given, source }

import { verifyToken, json } from '../_shared.js';

const MAX_BATCH = 100;

export async function onRequestPost(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader?.startsWith('Bearer ')) return json({ error: 'Unauthorized' }, 401);

    const user = await verifyToken(authHeader.replace('Bearer ', ''), context.env);
    if (!user) return json({ error: 'Invalid or expired token' }, 401);

    const body = await context.request.json();
    const mistakes = Array.isArray(body.mistakes) ? body.mistakes.slice(0, MAX_BATCH) : [];
    if (!mistakes.length) return json({ ok: true, inserted: 0 });

    const now = Date.now();
    const db = context.env.DB;
    let inserted = 0;

    for (const m of mistakes) {
      if (!m || !m.level || !m.chapter_slug) continue;
      await db.prepare(
        `INSERT INTO mistake_log (user_id, level, chapter_slug, question_id, skill_tag, expected, given, source, created_at)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`
      ).bind(
        user.id,
        String(m.level).toLowerCase(),
        String(m.chapter_slug).slice(0, 120),
        m.question_id ? String(m.question_id).slice(0, 60) : null,
        m.skill_tag ? String(m.skill_tag).slice(0, 120) : null,
        m.expected != null ? String(m.expected).slice(0, 300) : null,
        m.given != null ? String(m.given).slice(0, 300) : null,
        m.source ? String(m.source).slice(0, 20) : null,
        now
      ).run();
      inserted++;
    }

    return json({ ok: true, inserted });
  } catch (err) {
    console.error('[student/mistakes POST]', err);
    return json({ error: 'Failed to save mistakes' }, 500);
  }
}

export async function onRequestGet(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader?.startsWith('Bearer ')) return json({ error: 'Unauthorized' }, 401);

    const user = await verifyToken(authHeader.replace('Bearer ', ''), context.env);
    if (!user) return json({ error: 'Invalid or expired token' }, 401);

    const db = context.env.DB;

    const [bySkill, byChapter, total, recent] = await Promise.all([
      db.prepare(
        `SELECT skill_tag, COUNT(*) AS count FROM mistake_log
         WHERE user_id = ? AND skill_tag IS NOT NULL
         GROUP BY skill_tag ORDER BY count DESC LIMIT 12`
      ).bind(user.id).all(),
      db.prepare(
        `SELECT level, chapter_slug, COUNT(*) AS count FROM mistake_log
         WHERE user_id = ?
         GROUP BY level, chapter_slug ORDER BY count DESC LIMIT 12`
      ).bind(user.id).all(),
      db.prepare(`SELECT COUNT(*) AS count FROM mistake_log WHERE user_id = ?`)
        .bind(user.id).first(),
      db.prepare(
        `SELECT level, chapter_slug, question_id, skill_tag, expected, given, source, created_at
         FROM mistake_log WHERE user_id = ? ORDER BY created_at DESC LIMIT 30`
      ).bind(user.id).all()
    ]);

    return json({
      total: total?.count || 0,
      by_skill: bySkill.results || [],
      by_chapter: byChapter.results || [],
      recent: recent.results || []
    });
  } catch (err) {
    console.error('[student/mistakes GET]', err);
    return json({ error: 'Failed to load mistakes' }, 500);
  }
}
