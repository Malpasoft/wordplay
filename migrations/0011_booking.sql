-- Lesson booking: teacher publishes availability, students request slots,
-- teacher confirms/declines. Self-contained (separate from the legacy lessons calendar).

-- Weekly recurring availability windows set by the teacher.
CREATE TABLE IF NOT EXISTS availability (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  teacher_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  weekday INTEGER NOT NULL,          -- 0=Sunday … 6=Saturday
  start_time TEXT NOT NULL,          -- "HH:MM" 24h
  end_time TEXT NOT NULL,            -- "HH:MM" 24h
  slot_minutes INTEGER NOT NULL DEFAULT 60,
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000)
);
CREATE INDEX IF NOT EXISTS idx_availability_teacher ON availability(teacher_id);

-- Booking requests from students. status: pending | confirmed | declined | cancelled
CREATE TABLE IF NOT EXISTS booking_requests (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  student_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  teacher_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  date TEXT NOT NULL,                -- "YYYY-MM-DD"
  start_time TEXT NOT NULL,          -- "HH:MM"
  end_time TEXT NOT NULL,            -- "HH:MM"
  note TEXT,
  status TEXT NOT NULL DEFAULT 'pending',
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  updated_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000)
);
CREATE INDEX IF NOT EXISTS idx_booking_teacher_date ON booking_requests(teacher_id, date);
CREATE INDEX IF NOT EXISTS idx_booking_student ON booking_requests(student_id);
