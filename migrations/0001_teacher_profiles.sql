-- Teacher student profiles
CREATE TABLE IF NOT EXISTS profiles (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  sync_code  TEXT    NOT NULL,
  slug       TEXT    NOT NULL,
  name       TEXT    NOT NULL DEFAULT '',
  l1         TEXT    NOT NULL DEFAULT '',
  level      TEXT    NOT NULL DEFAULT '',
  goals      TEXT    NOT NULL DEFAULT '',
  notes      TEXT    NOT NULL DEFAULT '',
  updated_at TEXT    NOT NULL DEFAULT (datetime('now')),
  UNIQUE(sync_code, slug)
);
CREATE INDEX IF NOT EXISTS idx_profiles_code ON profiles(sync_code);
