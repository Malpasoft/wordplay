-- A1: Resolve the invite_codes schema conflict.
-- The teacher-based system (functions/api/teacher/invite-code.js, student/join-teacher.js)
-- owns `invite_codes` (teacher_id + uses_count). The class-based system
-- (functions/api/classes/*) gets its own table here so the two no longer collide on
-- one table with incompatible columns.
CREATE TABLE IF NOT EXISTS class_invite_codes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  class_id INTEGER NOT NULL REFERENCES classes(id) ON DELETE CASCADE,
  code TEXT UNIQUE NOT NULL,
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  expires_at INTEGER,
  max_uses INTEGER DEFAULT -1,
  used_count INTEGER DEFAULT 0
);
CREATE INDEX IF NOT EXISTS idx_class_invite_codes_code ON class_invite_codes(code);
CREATE INDEX IF NOT EXISTS idx_class_invite_codes_class ON class_invite_codes(class_id);
