-- Lesson calendar entries
CREATE TABLE IF NOT EXISTS lessons (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  sync_code   TEXT    NOT NULL,
  lesson_id   TEXT    NOT NULL,
  date        TEXT    NOT NULL,
  student     TEXT    NOT NULL DEFAULT '',
  title       TEXT    NOT NULL DEFAULT '',
  notes       TEXT    NOT NULL DEFAULT '',
  done        INTEGER NOT NULL DEFAULT 0,
  updated_at  TEXT    NOT NULL DEFAULT (datetime('now')),
  UNIQUE(sync_code, lesson_id)
);
CREATE INDEX IF NOT EXISTS idx_lessons_code_date ON lessons(sync_code, date);
