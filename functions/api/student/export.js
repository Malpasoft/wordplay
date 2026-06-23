// GET /api/student/export
// Returns all data held for the authenticated student as JSON (GDPR Art. 20).

import { verifyToken, json } from '../_shared.js';

export async function onRequestGet(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader?.startsWith('Bearer ')) return json({ error: 'Unauthorized' }, 401);

    const user = await verifyToken(authHeader.replace('Bearer ', ''), context.env);
    if (!user) return json({ error: 'Invalid or expired token' }, 401);

    const db = context.env.DB;

    const [userRow, xpRow, chapters, progress] = await Promise.all([
      db.prepare('SELECT id, email, role, email_verified, created_at FROM users WHERE id = ?')
        .bind(user.id).first(),
      db.prepare('SELECT xp, streak, last_day, updated_at FROM user_xp WHERE user_id = ?')
        .bind(user.id).first(),
      db.prepare('SELECT level, chapter_slug, score, total, pct, date FROM chapter_results WHERE user_id = ? ORDER BY date DESC')
        .bind(user.id).all(),
      db.prepare('SELECT progress_data, updated_at FROM student_progress WHERE user_id = ?')
        .bind(user.id).first()
    ]);

    const payload = {
      exported_at: new Date().toISOString(),
      account: userRow,
      xp: xpRow,
      chapter_results: chapters.results || [],
      legacy_progress: progress?.progress_data ? JSON.parse(progress.progress_data) : null
    };

    return new Response(JSON.stringify(payload, null, 2), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Content-Disposition': 'attachment; filename="wordplay-data-export.json"'
      }
    });
  } catch (err) {
    console.error('[student/export]', err);
    return json({ error: 'Internal server error.' }, 500);
  }
}
