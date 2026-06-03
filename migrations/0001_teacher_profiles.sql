-- Teacher profile sync table.
-- user_id is NULL until B1 auth is live; reserved for the upgrade path.
CREATE TABLE IF NOT EXISTS teacher_profiles (
  code       TEXT    PRIMARY KEY,
  data       TEXT    NOT NULL DEFAULT '[]',
  updated_at INTEGER NOT NULL,
  user_id    TEXT
);
