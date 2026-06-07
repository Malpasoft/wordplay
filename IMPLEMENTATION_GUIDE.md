# Progress Syncing Implementation Guide

## Overview

This implementation adds **bidirectional progress syncing** between localStorage and D1 database, enabling seamless multi-device learning. Students can complete lessons on one device and continue on another without losing data.

## Files Created

### 1. `functions/api/student/progress.js`
**New endpoint for student progress syncing**

**Endpoints:**
- `POST /api/student/progress` — Save progress to D1
  - Request: `{ chapters: {...}, xp: N, streak: N, lastDay: ISO_DATE }`
  - Response: `{ status: 'synced', updated_at: timestamp, chapters_synced: N }`
  
- `GET /api/student/progress` — Fetch progress from D1
  - Headers: `Authorization: Bearer <token>`
  - Response: `{ chapters: {...}, xp: N, streak: N, updated_at: timestamp, server_updated_at: timestamp }`

**Key Features:**
- Token-based authentication via Bearer tokens from `auth_tokens` table
- Deep-merge conflict resolution: prefers newer timestamps, then higher percentages
- Supports both nested and flat chapter formats
- XP/streak: takes maximum of local vs server (no data loss)
- 5-second timeout protection to prevent page hangs

**Database Tables Used:**
- `chapter_results` — Per-chapter scores (normalized from nested structure)
- `user_xp` — XP and streak tracking

---

## Files Modified

### 2. `shared/store.js`
**Added new sync methods + auto-sync lifecycle**

**New Methods:**
```javascript
FCEStore.syncProgress()
  // Sends local progress to /api/student/progress via POST
  // Called every 1.5s if user is logged in
  // Gracefully handles offline mode (silent failure, retries next session)

FCEStore.pullProgress()
  // Fetches progress from /api/student/progress via GET
  // Merges server state into local storage using last-write-wins
  // Called once on page load (if logged in)
  // Returns: { status: 'merged', chapters, updated_at, server_updated_at }
```

**Auto-Sync Behavior:**
1. **Page Load**: Automatically calls `pullProgress()` if user is logged in
   - Merges server progress with local progress
   - Server state takes precedence if newer, else local wins
   - Prevents stale data from overwriting recent local work

2. **Page Unload**: Existing `pagehide` listener calls `syncProgress()`
   - Sends accumulated changes to server before user leaves
   - Uses `keepalive: true` so request survives page close

3. **Scheduled Sync**: Every 1.5 seconds, calls `doPushNormalized()` 
   - Batches progress updates to avoid hammering server
   - Debounced: only fires if changes since last push

---

## Sync Workflow (Multi-Device Example)

### Scenario: Phone → Laptop
1. **Phone (11:00 AM)**
   - User opens `/a1/grammar/to-be/worksheet.html`
   - `shared/store.js` loads; calls `pullProgress()` → merges server state
   - User completes worksheet: 8/10 correct
   - `saveResult('to-be', 8, 10)` calls `schedulePush()`
   - After 1.5s, `doPushNormalized()` POSTs to `/api/student/progress`
   - Request contains: `{ chapters: {a1: {to-be: {score: 8, pct: 80, date: ...}}}, xp: 120, ... }`
   - Server stores in D1: `chapter_results` table

2. **Laptop (11:05 AM)**
   - User opens `/a1/vocabulary/family/flashcards.html`
   - `shared/store.js` loads; calls `pullProgress()` → fetches from D1
   - Response includes the "to-be" result from phone (8/10, 80%)
   - Client merges: local is empty for "to-be", so uses server value
   - localStorage now contains: `{ a1: { to-be: {score: 8, pct: 80, date: ...}, ... } }`
   - User can see phone progress on laptop dashboard

3. **Back to Phone (11:20 AM)**
   - User opens dashboard
   - `pullProgress()` fetches latest state including laptop work
   - All progress across devices is visible

---

## Conflict Resolution

When pulling server progress or merging on page load, the system uses **last-write-wins** with timestamp-based ordering:

```javascript
// For each chapter:
if (server_date > local_date) {
  use server version
} else if (local_date > server_date) {
  use local version
} else if (local_date === server_date) {
  use higher percentage (student made progress)
}

// For XP/streak:
keep Math.max(local, server)  // No loss of points or streaks
```

---

## Testing Checklist

### Unit Tests (for endpoint)
- [ ] POST `/api/student/progress` with valid token saves chapters
- [ ] POST `/api/student/progress` with invalid token returns 401
- [ ] POST `/api/student/progress` with missing chapters returns 400
- [ ] GET `/api/student/progress` with valid token returns chapters
- [ ] GET `/api/student/progress` reconstructs nested structure correctly
- [ ] Nested format and array format both work on POST

### Integration Tests (localStorage ↔ D1)
- [ ] `FCEStore.syncProgress()` POSTs to correct endpoint
- [ ] `FCEStore.pullProgress()` GETs from correct endpoint
- [ ] Page load triggers `pullProgress()` automatically
- [ ] Page unload triggers `syncProgress()` via pagehide listener
- [ ] Merge preserves newer timestamps
- [ ] Merge preserves higher percentages when dates match
- [ ] Merge takes maximum XP
- [ ] Merge takes maximum streak

### Multi-Device Flow (Manual Test)
**Device 1 (Phone):**
1. Open DevTools Console
2. Log in via `/login.html`
3. Open `/a1/grammar/to-be/worksheet.html`
4. Complete worksheet (e.g., 7/10 correct)
5. Verify localStorage shows: `wordplay_progress: {a1: {to-be: {score: 7, pct: 70, ...}}}`
6. Wait 1.5s, verify network tab shows POST to `/api/student/progress`
7. Check network response: `{ status: 'synced', chapters_synced: 1 }`

**Device 2 (Laptop):**
1. In same browser, log in with same account
2. Open DevTools Console
3. Run: `FCEStore.pullProgress().then(r => console.log(r))`
4. Verify response includes phone's "to-be" result
5. Check localStorage: should now have phone's progress
6. Open dashboard: phone progress should appear

**Verify Merge Logic:**
1. Phone: add 10 XP → `{xp: 130, ...}`
2. Laptop: has 120 XP locally, pulls 130 from server → keeps 130
3. Phone: has 100 XP locally, pulls 130 from server → keeps 130
4. Both devices converge to same state

### Edge Cases
- [ ] Offline mode: no sync errors, retries next session
- [ ] Network timeout: 5-second timeout prevents page hang
- [ ] Invalid auth token: returns 401, clears session
- [ ] Missing chapters: POST handles empty arrays gracefully
- [ ] Concurrent requests: database constraints prevent duplicates
- [ ] Rapid saves: 1.5s debounce prevents hammering server

### Performance
- [ ] Page load with pullProgress: <200ms (cached)
- [ ] Page unload with syncProgress: completes before page close
- [ ] Large chapter list (100+ chapters): sync completes <1s
- [ ] Database writes: no timeout, uses prepared statements

---

## Database Schema (Already Exists)

### `chapter_results` table
```sql
CREATE TABLE chapter_results (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  level TEXT NOT NULL,
  chapter_slug TEXT NOT NULL,
  score INTEGER,
  total INTEGER,
  pct INTEGER,
  date TEXT,
  created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  updated_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  UNIQUE(user_id, level, chapter_slug),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

### `user_xp` table
```sql
CREATE TABLE user_xp (
  user_id INTEGER PRIMARY KEY,
  xp INTEGER DEFAULT 0,
  streak INTEGER DEFAULT 0,
  last_day TEXT,
  updated_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now') * 1000),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

---

## Code Review Checklist

- [ ] `functions/api/student/progress.js`
  - [x] Token verification before access
  - [x] Authorization check: users can only access own progress
  - [x] Proper error handling with meaningful status codes
  - [x] Input validation on POST payload
  - [x] Deep-merge logic handles all conflict cases
  - [x] Database queries use prepared statements (no SQL injection)
  - [x] ON CONFLICT clauses handle duplicate inserts
  - [x] Response format matches client expectations
  - [x] Comments explain complex merge logic
  - [x] JSON serialization safe (no circular refs)

- [ ] `shared/store.js` changes
  - [x] `syncProgress()` wraps existing `doPushNormalized()`
  - [x] `pullProgress()` uses same timeout pattern as `mergeFromD1()`
  - [x] Auto-pull on DOMContentLoaded works for late scripts
  - [x] Uses existing `getAuthToken()` and `getCurrentUser()`
  - [x] Silent failures don't break page (catch blocks)
  - [x] No hardcoded URLs (uses `/api/student/progress`)
  - [x] Comments match implementation
  - [x] Doesn't break existing `pushToD1()` / `mergeFromD1()` methods

---

## Deployment Steps

1. **No migration needed** — uses existing tables (`chapter_results`, `user_xp`)

2. **Add endpoint file:**
   - Copy `functions/api/student/progress.js` to functions/

3. **Update store.js:**
   - Edit `shared/store.js` to add `syncProgress()`, `pullProgress()`, auto-pull on load

4. **Test in staging:**
   - Verify multi-device sync works (see Testing Checklist)
   - Check no errors in console

5. **Bump shared/store.js version:**
   - Current: `v106`
   - Increment to: `v107`
   - Update all HTML files: `python3 bump-versions.py`

6. **Deploy to main:**
   - `git push origin HEAD:main`
   - Cloudflare Pages auto-deploys (~2 min)

---

## Debugging & Monitoring

### Enable Debug Logging
In browser console:
```javascript
// Check sync is scheduled
localStorage.getItem('wordplay_progress')

// Trigger manual sync
FCEStore.syncProgress().then(r => console.log('Sync:', r))

// Trigger manual pull
FCEStore.pullProgress().then(r => console.log('Pull:', r))

// Check auth state
console.log(getCurrentUser())
console.log(getAuthToken())
```

### Check Network Requests
1. Open DevTools → Network tab
2. Filter: `progress`
3. Look for:
   - `POST /api/student/progress` → check Response for `{ status: 'synced' }`
   - `GET /api/student/progress` → check Response includes chapters

### Check Server Logs
Cloudflare Workers console logs appear in Pages project analytics.
Look for `[Student Progress GET/POST]` messages.

### Common Issues

**Problem: Progress not syncing**
- Solution: Check `getAuthToken()` returns a token (user logged in)
- Solution: Check network tab — request may be blocked by CORS

**Problem: Old progress appearing**
- Solution: Check localStorage doesn't have older `updated_at`
- Solution: Verify merge logic: should prefer newer timestamp

**Problem: Page hangs on load**
- Solution: Check 5-second timeout is triggering (`console.warn`)
- Solution: Check server is responsive via `/api/student/progress` directly

---

## Next Steps (Optional Enhancements)

1. **Persistent Queue**: Store failed syncs in IDB, retry on next session
2. **Real-time Sync**: Use WebSocket for instant multi-device updates
3. **Analytics Dashboard**: Show sync stats per user (last sync time, etc.)
4. **Selective Sync**: Option to sync only specific levels/sections
5. **Offline-First**: Implement Service Worker for full offline support
