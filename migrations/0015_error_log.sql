-- B4: lightweight production error monitoring. The /api middleware writes a row
-- for any unhandled throw or any 5xx response, so launch issues are visible
-- (viewable via GET /api/admin/errors, admin only). Best-effort; never blocks a request.
CREATE TABLE IF NOT EXISTS error_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  path TEXT,
  method TEXT,
  status INTEGER,
  message TEXT,
  stack TEXT,
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000)
);
CREATE INDEX IF NOT EXISTS idx_error_log_created ON error_log(created_at);
