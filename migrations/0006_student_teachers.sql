-- Teacher Self-Management: student-teacher relationships
-- Allows teachers to manage their own students without admin intervention

CREATE TABLE IF NOT EXISTS student_teachers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  student_id INTEGER NOT NULL,
  teacher_id INTEGER NOT NULL,
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  updated_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  UNIQUE(student_id, teacher_id),
  FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (teacher_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Indexes for efficient lookups
CREATE INDEX IF NOT EXISTS idx_student_teachers_teacher_id ON student_teachers(teacher_id);
CREATE INDEX IF NOT EXISTS idx_student_teachers_student_id ON student_teachers(student_id);
CREATE INDEX IF NOT EXISTS idx_student_teachers_teacher_student ON student_teachers(teacher_id, student_id);
