// Word Play Student Progress Sync API
// POST /api/student/progress — save student's progress to D1
// GET /api/student/progress — retrieve student's progress from D1
//
// This endpoint provides a simplified interface for client-side progress syncing.
// It handles localStorage ↔ D1 synchronization with last-write-wins conflict resolution.


import { verifyTokenId as verifyToken } from '../_shared.js';
function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}

// Deep-merge progress entries: prefer newer date, then higher percentage
function pickEntry(x, y) {
  if (!x) return y;
  if (!y) return x;
  const dx = Date.parse(x.lastDate || x.date || 0) || 0;
  const dy = Date.parse(y.lastDate || y.date || 0) || 0;
  if (dx !== dy) return dx > dy ? x : y;
  return (y.pct || 0) > (x.pct || 0) ? y : x;
}

function mergeProgress(a, b) {
  a = a || {}; b = b || {};
  const out = {};
  const keys = new Set([...Object.keys(a), ...Object.keys(b)]);

  for (const k of keys) {
    const av = a[k], bv = b[k];
    if (k === 'updated_at') continue;
    if (k === 'xp')      { out.xp = Math.max(av || 0, bv || 0); continue; }
    if (k === 'streak')  { out.streak = Math.max(av || 0, bv || 0); continue; }
    if (k === 'lastDay') { out.lastDay = (av || '') > (bv || '') ? av : bv; continue; }

    // Merge level objects
    if (av && bv && typeof av === 'object' && typeof bv === 'object') {
      const level = {};
      const chs = new Set([...Object.keys(av), ...Object.keys(bv)]);
      for (const c of chs) level[c] = pickEntry(av[c], bv[c]);
      out[k] = level;
      continue;
    }
    out[k] = (bv !== undefined ? bv : av);
  }

  return out;
}

export async function onRequestGet(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');

    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const userId = await verifyToken(token, context.env.DB);

    if (!userId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    // Fetch chapter results from database
    const chapters = await context.env.DB.prepare(
      'SELECT level, chapter_slug, score, total, pct, date FROM chapter_results WHERE user_id = ? ORDER BY level, chapter_slug'
    )
      .bind(userId)
      .all();

    // Fetch XP and streak
    const xpRow = await context.env.DB.prepare(
      'SELECT xp, streak, last_day, updated_at FROM user_xp WHERE user_id = ?'
    )
      .bind(userId)
      .first();

    // Reconstruct progress object (nested by level, then chapter)
    const progress = {};
    for (const ch of chapters.results || []) {
      if (!progress[ch.level]) progress[ch.level] = {};
      progress[ch.level][ch.chapter_slug] = {
        score: ch.score,
        total: ch.total,
        pct: ch.pct,
        date: ch.date
      };
    }

    // Add XP/streak to progress with defaults for new users
    progress.xp = (xpRow && xpRow.xp) || 0;
    progress.streak = (xpRow && xpRow.streak) || 0;
    progress.lastDay = (xpRow && xpRow.last_day) || null;

    const now = Date.now();
    return json({
      chapters: progress,
      xp: progress.xp,
      streak: progress.streak,
      updated_at: now,
      server_updated_at: (xpRow && xpRow.updated_at) || now
    }, 200);
  } catch (error) {
    console.error('[Student Progress GET] Error:', error);
    return json({ error: 'Failed to fetch progress' }, 500);
  }
}

export async function onRequestPost(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');

    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const userId = await verifyToken(token, context.env.DB);

    if (!userId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    const payload = await context.request.json();
    const now = Date.now();

    // Validate payload format
    if (!payload || typeof payload !== 'object') {
      return json({ error: 'Invalid payload' }, 400);
    }

    // Handle flattened array format (check array first, before generic object check)
    if (Array.isArray(payload.chapters)) {
      for (const ch of payload.chapters) {
        await context.env.DB.prepare(
          `INSERT INTO chapter_results (user_id, level, chapter_slug, score, total, pct, date, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)
           ON CONFLICT(user_id, level, chapter_slug) DO UPDATE SET
             score=excluded.score, total=excluded.total, pct=excluded.pct,
             date=excluded.date, updated_at=excluded.updated_at`
        )
          .bind(userId, ch.level, ch.slug, ch.score, ch.total, ch.pct, ch.date, now)
          .run();
      }

      await context.env.DB.prepare(
        `INSERT INTO user_xp (user_id, xp, streak, last_day, updated_at)
         VALUES (?, ?, ?, ?, ?)
         ON CONFLICT(user_id) DO UPDATE SET
           xp=MAX(xp, excluded.xp),
           streak=MAX(streak, excluded.streak),
           last_day=MAX(last_day, excluded.last_day),
           updated_at=excluded.updated_at`
      )
        .bind(userId, payload.xp || 0, payload.streak || 0, payload.lastDay || null, now)
        .run();

      return json({
        status: 'synced',
        updated_at: now,
        chapters_synced: payload.chapters.length
      }, 200);
    }

    // Handle nested object format: { chapters: {level: {slug: {...}}}, xp: N, streak: N }
    if (typeof payload.chapters === 'object' && payload.chapters !== null && !Array.isArray(payload.chapters)) {
      // Flatten nested chapter structure into array format for insertion
      const chapters = [];

      for (const level in payload.chapters) {
        if (!level || typeof payload.chapters[level] !== 'object') continue;

        const levelData = payload.chapters[level];
        for (const slug in levelData) {
          const entry = levelData[slug];
          if (!entry || typeof entry !== 'object' || entry.pct === undefined) continue;

          chapters.push({
            level: level,
            slug: slug,
            score: entry.score || null,
            total: entry.total || null,
            pct: entry.pct,
            date: entry.date || new Date().toISOString()
          });
        }
      }

      // Insert/update each chapter result
      for (const ch of chapters) {
        await context.env.DB.prepare(
          `INSERT INTO chapter_results (user_id, level, chapter_slug, score, total, pct, date, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)
           ON CONFLICT(user_id, level, chapter_slug) DO UPDATE SET
             score=excluded.score, total=excluded.total, pct=excluded.pct,
             date=excluded.date, updated_at=excluded.updated_at`
        )
          .bind(userId, ch.level, ch.slug, ch.score, ch.total, ch.pct, ch.date, now)
          .run();
      }

      // Upsert XP/streak
      await context.env.DB.prepare(
        `INSERT INTO user_xp (user_id, xp, streak, last_day, updated_at)
         VALUES (?, ?, ?, ?, ?)
         ON CONFLICT(user_id) DO UPDATE SET
           xp=MAX(xp, excluded.xp),
           streak=MAX(streak, excluded.streak),
           last_day=MAX(last_day, excluded.last_day),
           updated_at=excluded.updated_at`
      )
        .bind(userId, payload.xp || 0, payload.streak || 0, payload.lastDay || null, now)
        .run();

      return json({
        status: 'synced',
        updated_at: now,
        chapters_synced: chapters.length
      }, 200);
    }

    return json({ error: 'Invalid payload format. Expected {chapters, xp, streak}' }, 400);
  } catch (error) {
    console.error('[Student Progress POST] Error:', error);
    return json({ error: 'Failed to save progress' }, 500);
  }
}
