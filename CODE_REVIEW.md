# Code Review: Progress Syncing Implementation

**Reviewed Files:**
1. `functions/api/student/progress.js` (NEW)
2. `shared/store.js` (MODIFIED)

---

## File 1: functions/api/student/progress.js

### Architecture & Design

✅ **Correct endpoint placement**
- Located at `/functions/api/student/progress.js` → routes to `/api/student/progress`
- RESTful design: GET for read, POST for write
- Mirrors existing `/api/progress/[user_id].js` pattern but with simplified token-based routing

✅ **Authentication pattern**
- Uses Bearer token from `Authorization` header
- Reuses `verifyToken()` function matching `auth.js` pattern
- Checks both presence and expiry of token via `expires_at > Date.now()`
- Returns 401 for invalid/missing tokens

⚠️ **Authorization gap** (minor)
- Endpoint correctly extracts `user_id` from token
- Does NOT need to accept `user_id` in path (route is uniform for logged-in user)
- Client always syncs to their own progress (implicit via token)
- This is correct; just different from `/api/progress/[user_id]` which supports user_id param

### POST Endpoint Analysis

#### Input Validation
✅ **Payload format validation**
```javascript
if (!payload || typeof payload !== 'object') {
  return json({ error: 'Invalid payload' }, 400);
}
```
- Catches null/undefined/string inputs
- Prevents crashes on malformed JSON

✅ **Handles both chapter formats**
```javascript
if (typeof payload.chapters === 'object' && payload.chapters !== null) {
  // Handle nested format: { chapters: { a1: { to-be: {...} } } }
}
if (Array.isArray(payload.chapters)) {
  // Handle flat format: { chapters: [{level: 'a1', slug: 'to-be', ...}] }
}
```
- Client sends nested format (from `shared/store.js`)
- Also handles flat format for flexibility
- **Best practice**: Accept both to prevent breaking changes

⚠️ **Potential issue: Both handlers could match**
- If `payload.chapters` is an array (which is also an object), first check would pass
- Current code: Second check would never execute if first matches
- **Recommendation**: Reorder to check `Array.isArray()` first:
```javascript
if (Array.isArray(payload.chapters)) {
  // flat array format
} else if (typeof payload.chapters === 'object' && payload.chapters !== null) {
  // nested object format
}
```

#### Chapter Insertion Logic
✅ **Proper SQL with ON CONFLICT**
```javascript
INSERT INTO chapter_results (...) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
ON CONFLICT(user_id, level, chapter_slug) DO UPDATE SET
  score=excluded.score, total=excluded.total, pct=excluded.pct,
  date=excluded.date, updated_at=excluded.updated_at
```
- Handles duplicate submissions gracefully (idempotent)
- Uses prepared statements (safe from SQL injection)
- Updates only relevant columns, preserves created_at

✅ **Timestamp handling**
```javascript
const now = Date.now();
// ... INSERT with updated_at=now
```
- Uses current time for server-side updated_at
- Correct: server decides timestamp, prevents clock-skew issues

✅ **XP/Streak aggregation**
```javascript
xp=MAX(xp, excluded.xp),
streak=MAX(streak, excluded.streak),
```
- Takes maximum of local vs server (no loss)
- Correct for "XP never decreases" semantics
- Note: Should this use server's max, or allow both to accumulate? Current approach is safe.

#### Response Format
✅ **Clear, structured response**
```javascript
{
  status: 'synced',
  updated_at: now,
  chapters_synced: chapters.length
}
```
- Confirms sync success
- Includes server timestamp (for client to track)
- Reports how many chapters were synced (useful for debugging)

❌ **Missing: updated_at in database response**
- Client might want to compare `client_updated_at` vs `server_updated_at` for merge decisions
- Current implementation handles merge on GET (pull), but POST doesn't return server state
- **Not critical** since client uses last-write-wins anyway, but could be informational

### GET Endpoint Analysis

✅ **Correct query pattern**
```javascript
const chapters = await context.env.DB.prepare(
  'SELECT level, chapter_slug, score, total, pct, date FROM chapter_results WHERE user_id = ?'
).bind(userId).all();

const xpRow = await context.env.DB.prepare(
  'SELECT xp, streak, last_day, updated_at FROM user_xp WHERE user_id = ?'
).bind(userId).first();
```
- Fetches all chapters for user (efficient with index on user_id)
- Fetches XP/streak as single row (primary key lookup)
- Uses prepared statements

✅ **Reconstruction logic**
```javascript
for (const ch of chapters.results || []) {
  if (!progress[ch.level]) progress[ch.level] = {};
  progress[ch.level][ch.chapter_slug] = {
    score: ch.score,
    total: ch.total,
    pct: ch.pct,
    date: ch.date
  };
}
```
- Converts flat table rows back to nested structure
- Matches client's expected format (mirrors `shared/store.js`)
- Defensive: `chapters.results || []` handles null

⚠️ **Potential issue: Empty user_xp row**
```javascript
if (xpRow) {
  progress.xp = xpRow.xp;
  progress.streak = xpRow.streak;
  progress.lastDay = xpRow.last_day;
}
```
- If user_xp row doesn't exist (brand new user), XP defaults to undefined
- Client expects: `{ xp: 0, streak: 0, lastDay: null }`
- **Recommendation**: Ensure defaults:
```javascript
progress.xp = xpRow?.xp || 0;
progress.streak = xpRow?.streak || 0;
progress.lastDay = xpRow?.last_day || null;
```

✅ **Response includes both timestamps**
```javascript
{
  chapters: progress,
  xp: progress.xp || 0,
  streak: progress.streak || 0,
  updated_at: now,
  server_updated_at: (xpRow && xpRow.updated_at) || now
}
```
- Redundant fields (xp/streak also in chapters), but explicit for client parsing
- Two timestamps for debugging: when client requested vs when server last updated

### Error Handling

✅ **Consistent error responses**
```javascript
if (!authHeader || !authHeader.startsWith('Bearer ')) {
  return json({ error: 'Missing authorization token' }, 401);
}
```
- All errors return JSON with message + status code
- 401 for auth failures, 400 for bad input, 500 for server errors
- Matches API conventions

⚠️ **Logging in catch block**
```javascript
catch (error) {
  console.error('[Student Progress POST] Error:', error);
  return json({ error: 'Failed to save progress' }, 500);
}
```
- Good: logs error for debugging
- Could be more specific (e.g., log user_id, request size) for diagnostics

### Security

✅ **No privilege escalation**
- User can only sync their own progress (verified via token)
- Cannot pass user_id in URL to sync another user's data

✅ **SQL injection prevention**
- All queries use prepared statements with `.bind()`
- No string concatenation in WHERE clauses

⚠️ **Rate limiting not implemented**
- Endpoint could be hammered with rapid POSTs
- Not critical (client already has 1.5s debounce), but could add IP-based rate limit
- Existing `rate_limit_log` table suggests infrastructure exists for this

### Performance

✅ **Efficient queries**
- Index on `chapter_results(user_id)` makes first query O(log n)
- `user_xp` is keyed on user_id, so second query is O(1)
- No N+1 queries

✅ **Batch insert loop**
```javascript
for (const ch of chapters) {
  await context.env.DB.prepare(...).bind(...).run();
}
```
- Loops through chapters and inserts individually
- **Potential improvement**: D1 supports batching, but serial inserts are safe

⚠️ **No transaction**
- If sync fails mid-way (e.g., chapters inserted but XP fails), progress is inconsistent
- **Mitigation**: ON CONFLICT ensures idempotency, so retry is safe
- **Recommendation**: Could wrap in transaction for stricter safety:
```javascript
await context.env.DB.exec('BEGIN TRANSACTION');
try {
  // all inserts
  await context.env.DB.exec('COMMIT');
} catch {
  await context.env.DB.exec('ROLLBACK');
}
```

---

## File 2: shared/store.js

### New Methods: syncProgress() & pullProgress()

✅ **Correct wrappers around existing functions**
```javascript
syncProgress: function() {
  return doPushNormalized();
},

pullProgress: function() {
  // GET /api/student/progress, merge into local
}
```
- `syncProgress()` is simple alias for existing push logic
- `pullProgress()` mirrors `mergeFromD1()` pattern but calls new endpoint

✅ **Proper token/user checking**
```javascript
var token = getAuthToken ? getAuthToken() : null;
var user  = getCurrentUser ? getCurrentUser() : null;
if (!token || !user) return Promise.resolve(null);
```
- Defensive checks: guards against auth.js not being loaded
- Returns resolved promise instead of rejecting (graceful for offline)
- Client code can safely call even if not authenticated

✅ **5-second timeout protection**
```javascript
return Promise.race([
  promise,
  new Promise(function(resolve) {
    setTimeout(function() {
      console.warn('[WordPlay] Pull progress timeout (5s); using local data');
      resolve(load());
    }, 5000);
  })
]);
```
- Prevents page hang if server is slow
- Matches pattern from existing `mergeFromD1()`
- Falls back to local data on timeout (graceful degradation)

✅ **Error handling**
```javascript
.catch(function(err) {
  console.warn('[WordPlay] Pull progress failed, using local:', err.message);
  return load();
});
```
- Silent failure (doesn't throw), page continues
- Logs warning for debugging
- Returns local progress as fallback

⚠️ **Missing: De-duplication check**
- If `pullProgress()` is called twice, both will fetch and merge
- Second call might overwrite first call's local changes with stale server data
- **Mitigation**: Auto-pull only happens once on DOMContentLoaded, manual calls are rare
- **Recommendation**: Could add flag to prevent duplicate pulls:
```javascript
var _hasPulledOnce = false;
pullProgress: function(force) {
  if (_hasPulledOnce && !force) return Promise.resolve(null);
  // ... fetch & merge
  _hasPulledOnce = true;
}
```

### Auto-Pull on Page Load

✅ **Correct timing**
```javascript
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', doPullOnLoad);
} else {
  doPullOnLoad();
}
```
- Checks current document state to avoid race condition
- Handles both early script load and late script injection
- Follows defensive JS pattern

✅ **Graceful fallback**
```javascript
function doPullOnLoad() {
  var token = getAuthToken ? getAuthToken() : null;
  if (token) {
    FCEStore.pullProgress().catch(function(err) {
      console.warn('[WordPlay] Auto-pull on load failed:', err.message);
    });
  }
}
```
- Only pulls if user is logged in (token exists)
- Catches errors (shouldn't happen, but defensive)
- Async (doesn't block page load)

⚠️ **No await - fire and forget**
```javascript
FCEStore.pullProgress().catch(...)
```
- Client doesn't wait for pull to complete before using progress
- **Risk**: Dashboard might show stale data briefly, then update when pull completes
- **Mitigation**: Pull happens early (DOMContentLoaded), most pages load async anyway
- **Not critical** because merge is non-destructive (keeps local if newer)

### Existing Methods (Unchanged)

✅ **No breaking changes**
- Existing `pushToD1()`, `mergeFromD1()`, `saveResult()`, `addXP()` all unchanged
- New methods are additions, not replacements
- Backward compatible

---

## Testing Coverage

### Manual Testing (Required)

✅ **Test Case 1: Single Device Sync**
1. User logs in on Device A
2. User saves a worksheet result
3. After 1.5s, verify POST `/api/student/progress` appears in network tab
4. Verify request body contains correct chapter data
5. Verify response has `{ status: 'synced' }`

✅ **Test Case 2: Multi-Device Pull**
1. User logs in on Device A, completes worksheet (saved to D1)
2. User logs in on Device B with same account
3. Page load triggers `pullProgress()`
4. Verify GET `/api/student/progress` appears in network tab
5. Verify Device B localStorage now contains Device A's worksheet result

✅ **Test Case 3: Conflict Resolution**
1. Device A has 100 XP, Device B has 80 XP
2. Device A pulls from server: should keep 100 (max)
3. Device B pulls from server: should keep 100 (max)
4. Both converge to 100

✅ **Test Case 4: Offline Mode**
1. Device goes offline (DevTools Network → Offline)
2. User saves worksheet result
3. Verify `syncProgress()` fails gracefully (console warning)
4. Verify localStorage still has result
5. User goes online, page loads
6. Verify result is pushed to server

### Unit Tests (Recommended)

```javascript
// Test conflict resolution
const localProg = { a1: { to-be: { pct: 80, date: '2026-01-01T10:00:00Z' } }, xp: 100 };
const serverProg = { a1: { to-be: { pct: 70, date: '2026-01-01T09:00:00Z' } }, xp: 80 };
const merged = mergeProgress(localProg, serverProg);
assert(merged.a1['to-be'].pct === 80, 'Should keep newer (local)');
assert(merged.xp === 100, 'Should keep max XP');

// Test timeout
const slowPromise = new Promise(r => setTimeout(() => r('slow'), 10000));
const raceResult = Promise.race([slowPromise, new Promise(r => setTimeout(() => r('timeout'), 5000))]);
assert(await raceResult === 'timeout', 'Should timeout after 5s');
```

---

## Potential Issues & Recommendations

### Critical Issues
**None identified.** Code is sound for core functionality.

### High Priority
1. **Issue**: Chapter format ambiguity in POST
   - **Current**: Checks `typeof object` before `Array.isArray`
   - **Fix**: Reorder checks (array is subset of object type)

2. **Issue**: Missing defaults in GET response
   - **Current**: If user_xp row doesn't exist, xp/streak are undefined
   - **Fix**: Add `|| 0` defaults

### Medium Priority
3. **Issue**: No transaction wrapping on multi-step POST
   - **Current**: Chapters inserted, then XP updated separately
   - **Risk**: Partial sync on failure
   - **Fix**: Optional, current approach is safe due to idempotency

4. **Issue**: Auto-pull fires async without waiting
   - **Current**: Dashboard might briefly show stale data
   - **Risk**: Low (pull completes within DOMContentLoaded)
   - **Fix**: Could await in some pages (optional)

### Low Priority
5. **Issue**: Rate limiting not enforced
   - **Current**: Client debounces (1.5s), but endpoint is unprotected
   - **Risk**: Low (need auth token, infrastructure exists)
   - **Fix**: Add IP-based rate limit (optional enhancement)

6. **Issue**: Logging doesn't include user_id
   - **Current**: Errors log generic "Failed to save progress"
   - **Risk**: Hard to debug in production
   - **Fix**: Log `user_id` and request size for diagnostics

---

## Summary

### functions/api/student/progress.js
**Grade: A-**
- ✅ Correct architecture, security, error handling
- ⚠️ Minor: Array/object type check order, missing defaults
- 🟢 Production-ready with small polish

### shared/store.js
**Grade: A**
- ✅ Clean additions, no breaking changes
- ✅ Proper async/error handling
- ⚠️ Minor: No explicit wait on auto-pull (acceptable)
- 🟢 Production-ready

### Overall
**Ready to deploy** after addressing:
1. Reorder POST payload validation (array before object)
2. Add defaults to GET response (xp: 0, streak: 0)

Estimated fix time: 5 minutes. Recommend deploying with fixes.
