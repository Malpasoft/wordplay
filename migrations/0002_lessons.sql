-- Lesson slots for the teacher calendar.
-- Same D1 database as teacher_profiles — same one-time Cloudflare binding setup.
CREATE TABLE IF NOT EXISTS lessons (
  id          TEXT    PRIMARY KEY,
  code        TEXT    NOT NULL,
  title       TEXT    NOT NULL DEFAULT '',
  student_ids TEXT    NOT NULL DEFAULT '[]',  -- JSON array of student id strings
  date        TEXT    NOT NULL,               -- "YYYY-MM-DD" (lexsort-safe)
  time_start  TEXT    NOT NULL,               -- "HH:MM"
  time_end    TEXT    NOT NULL,               -- "HH:MM"
  type        TEXT    NOT NULL DEFAULT '1on1',-- '1on1'|'group'|'academy'|'school'|'online'
  location    TEXT    NOT NULL DEFAULT '',
  notes       TEXT    NOT NULL DEFAULT '',
  created_at  INTEGER NOT NULL,
  updated_at  INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_lessons_code_date ON lessons (code, date);
