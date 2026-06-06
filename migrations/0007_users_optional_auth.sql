-- Modify users table to support optional email/password
-- Allows teacher-created students without login credentials (yet)

-- SQLite doesn't support ALTER COLUMN, so we recreate the table
-- Backup old schema first
ALTER TABLE users RENAME TO users_backup;

-- Create new users table with optional email/password
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE,
  password_hash TEXT,
  role TEXT NOT NULL CHECK (role IN ('admin', 'teacher', 'student')),
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  updated_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000)
);

-- Restore data from backup
INSERT INTO users (id, email, password_hash, role, created_at, updated_at)
SELECT id, email, password_hash, role, created_at, updated_at FROM users_backup;

-- Drop backup
DROP TABLE users_backup;

-- Recreate indexes
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_role ON users(role);
