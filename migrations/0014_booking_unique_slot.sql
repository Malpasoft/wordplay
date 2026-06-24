-- A3: Close the check-then-insert race on booking requests.
-- A partial unique index prevents two active (pending/confirmed) bookings for the same
-- teacher slot, while still allowing re-requests after a decline/cancel.
CREATE UNIQUE INDEX IF NOT EXISTS idx_booking_active_slot
  ON booking_requests(teacher_id, date, start_time)
  WHERE status IN ('pending', 'confirmed');
