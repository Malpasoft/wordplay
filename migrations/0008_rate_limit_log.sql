-- Rate limiting persistence: track API calls per IP for DDoS protection
CREATE TABLE IF NOT EXISTS rate_limit_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ip TEXT NOT NULL,
  endpoint TEXT NOT NULL,
  timestamp INTEGER NOT NULL,
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000)
);

-- Index for fast lookups: cleanup old entries, count recent attempts
CREATE INDEX IF NOT EXISTS idx_rate_limit_log_ip_endpoint_time
  ON rate_limit_log(ip, endpoint, timestamp);

-- Automatic cleanup: delete entries older than 24 hours (via trigger not supported in SQLite,
-- so cleanup happens in application code via periodic job or on-demand in endpoints)
