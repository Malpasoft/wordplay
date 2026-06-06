-- Phase 1: Unified student management system
-- Supports both teacher-created (no account) and self-signup (with account) flows

-- Students: Core identity (independent of auth account)
CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER UNIQUE,
  teacher_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  email TEXT,
  status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'archived')),
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  updated_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
  FOREIGN KEY (teacher_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_students_teacher_id ON students(teacher_id);
CREATE INDEX IF NOT EXISTS idx_students_user_id ON students(user_id);
CREATE INDEX IF NOT EXISTS idx_students_email ON students(email);

-- Classes: Teacher-managed class roster
CREATE TABLE IF NOT EXISTS classes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  teacher_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  level TEXT,
  description TEXT,
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  updated_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  FOREIGN KEY (teacher_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_classes_teacher_id ON classes(teacher_id);

-- Class enrollments: Links students to classes
CREATE TABLE IF NOT EXISTS class_enrollments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  class_id INTEGER NOT NULL,
  student_id INTEGER NOT NULL,
  enrolled_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE,
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
  UNIQUE(class_id, student_id)
);

CREATE INDEX IF NOT EXISTS idx_enrollments_class_id ON class_enrollments(class_id);
CREATE INDEX IF NOT EXISTS idx_enrollments_student_id ON class_enrollments(student_id);

-- Lessons: Calendar events for each class
CREATE TABLE IF NOT EXISTS lessons (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  class_id INTEGER NOT NULL,
  date INTEGER NOT NULL,
  time_start TEXT,
  time_end TEXT,
  chapter_slug TEXT,
  title TEXT NOT NULL,
  type TEXT DEFAULT '1on1' CHECK (type IN ('1on1', 'group', 'academy', 'school', 'online')),
  level TEXT,
  location TEXT,
  notes TEXT,
  student_ids TEXT,
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  updated_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_lessons_class_id ON lessons(class_id);
CREATE INDEX IF NOT EXISTS idx_lessons_date ON lessons(date);

-- Invite codes: Allow teachers to share class joins
CREATE TABLE IF NOT EXISTS invite_codes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  class_id INTEGER NOT NULL,
  code TEXT UNIQUE NOT NULL,
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  expires_at INTEGER,
  max_uses INTEGER DEFAULT -1,
  used_count INTEGER DEFAULT 0,
  FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_invite_codes_code ON invite_codes(code);
CREATE INDEX IF NOT EXISTS idx_invite_codes_class_id ON invite_codes(class_id);

-- Migrate existing student_progress to reference students table
-- (Keep old table but add foreign key when students are migrated)
ALTER TABLE student_progress ADD COLUMN student_id INTEGER REFERENCES students(id) ON DELETE CASCADE;
CREATE INDEX IF NOT EXISTS idx_student_progress_student_id ON student_progress(student_id);
