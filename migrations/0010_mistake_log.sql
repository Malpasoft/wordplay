-- Mistake log: per-question wrong answers for sophisticated weakness analytics.
-- Written by worksheet.js and game.js (batched) for signed-in students.
CREATE TABLE IF NOT EXISTS mistake_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  level TEXT NOT NULL,
  chapter_slug TEXT NOT NULL,
  question_id TEXT,
  skill_tag TEXT,
  expected TEXT,
  given TEXT,
  source TEXT,                      -- 'worksheet' | 'game'
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000)
);

CREATE INDEX IF NOT EXISTS idx_mistake_log_user ON mistake_log(user_id);
CREATE INDEX IF NOT EXISTS idx_mistake_log_user_skill ON mistake_log(user_id, skill_tag);
CREATE INDEX IF NOT EXISTS idx_mistake_log_user_chapter ON mistake_log(user_id, level, chapter_slug);
