-- Normalize student progress: split blob into surgical rows for efficiency
-- This enables O(1) analytics queries, reduces write volume, and prevents conflicts

-- Per-chapter results (one row = one chapter a student completed)
CREATE TABLE IF NOT EXISTS chapter_results (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  level TEXT NOT NULL,
  chapter_slug TEXT NOT NULL,
  score INTEGER,
  total INTEGER,
  pct INTEGER,
  date TEXT,
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  updated_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  UNIQUE(user_id, level, chapter_slug),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Student XP and streak (one row per student, updated infrequently)
CREATE TABLE IF NOT EXISTS user_xp (
  user_id INTEGER PRIMARY KEY,
  xp INTEGER DEFAULT 0,
  streak INTEGER DEFAULT 0,
  last_day TEXT,
  updated_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Indexes for fast lookups
CREATE INDEX IF NOT EXISTS idx_chapter_results_user_id ON chapter_results(user_id);
CREATE INDEX IF NOT EXISTS idx_chapter_results_level ON chapter_results(level);
CREATE INDEX IF NOT EXISTS idx_chapter_results_user_level ON chapter_results(user_id, level);
