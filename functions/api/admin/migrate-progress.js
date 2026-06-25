// One-time migration: convert old blob-based progress to normalized tables
// GET /api/admin/migrate-progress?token=xxx
// Admin-only. Converts all student_progress blobs to chapter_results + user_xp.
// Idempotent: safe to run multiple times (updates existing, skips duplicates).


import { verifyTokenId as verifyToken } from '../_shared.js';
async function getUserRole(userId, db) {
  const user = await db.prepare('SELECT role FROM users WHERE id = ?')
    .bind(userId)
    .first();
  return user ? user.role : null;
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}

export async function onRequestGet(context) {
  try {
    const url = new URL(context.request.url);
    const token = url.searchParams.get('token');

    if (!token) {
      return json({ error: 'token query param required' }, 400);
    }

    const userId = await verifyToken(token, context.env.DB);
    if (!userId) {
      return json({ error: 'Invalid token' }, 401);
    }

    const role = await getUserRole(userId, context.env.DB);
    if (role !== 'admin') {
      return json({ error: 'Admin only' }, 403);
    }

    // Get all old blob progress records
    const allProgress = await context.env.DB.prepare(
      'SELECT user_id, progress_data FROM student_progress'
    ).all();

    let migrated = 0;
    let skipped = 0;
    const errors = [];

    // Convert each blob to normalized rows
    for (const record of allProgress.results || []) {
      try {
        const progress = JSON.parse(record.progress_data);
        const studentId = record.user_id;

        // Migrate chapters: for each level, for each chapter, create a row
        for (const level in progress) {
          if (!level || ['xp', 'streak', 'updated_at', 'lastDay'].includes(level)) continue;

          const levelData = progress[level];
          if (typeof levelData !== 'object') continue;

          for (const slug in levelData) {
            const entry = levelData[slug];
            if (!entry || typeof entry !== 'object' || entry.pct === undefined) continue;

            // Upsert: update if exists, insert if not (UNIQUE constraint handles it)
            try {
              await context.env.DB.prepare(
                `INSERT INTO chapter_results (user_id, level, chapter_slug, score, total, pct, date)
                 VALUES (?, ?, ?, ?, ?, ?, ?)
                 ON CONFLICT(user_id, level, chapter_slug) DO UPDATE SET
                   score=excluded.score, total=excluded.total, pct=excluded.pct, date=excluded.date`
              )
                .bind(
                  studentId,
                  level,
                  slug,
                  entry.score || null,
                  entry.total || null,
                  entry.pct,
                  entry.date || new Date().toISOString()
                )
                .run();
            } catch (e) {
              errors.push(`Student ${studentId} chapter ${slug}: ${e.message}`);
              continue;
            }
          }
        }

        // Migrate XP/streak: upsert one row per student
        try {
          await context.env.DB.prepare(
            `INSERT INTO user_xp (user_id, xp, streak, last_day)
             VALUES (?, ?, ?, ?)
             ON CONFLICT(user_id) DO UPDATE SET
               xp=excluded.xp, streak=excluded.streak, last_day=excluded.last_day`
          )
            .bind(
              studentId,
              progress.xp || 0,
              progress.streak || 0,
              progress.lastDay || null
            )
            .run();
        } catch (e) {
          errors.push(`Student ${studentId} XP: ${e.message}`);
        }

        migrated++;
      } catch (e) {
        errors.push(`Record ${record.user_id}: ${e.message}`);
        skipped++;
      }
    }

    return json({
      ok: true,
      migrated: migrated,
      skipped: skipped,
      errors: errors,
      message: `Migrated ${migrated} students. Next: test the new tables, then DELETE FROM student_progress WHERE 1=1 to clean up the old blobs.`
    });
  } catch (error) {
    console.error('Migration error:', error);
    return json({ error: 'Migration failed: ' + error.message }, 500);
  }
}
