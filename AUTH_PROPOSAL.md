# Word Play — Student Login & User Accounts Proposal

## Current state
All student progress is stored in **browser localStorage**. This means:
- Progress is lost if the student clears their browser data or uses a different device
- No way for teachers to see student progress
- No way for students to sync between phone and laptop
- Works offline (good), but no persistence (bad)

## Proposed phased approach

### Phase 1 — URL token (simplest, no infrastructure)
**How it works:** Each student gets a unique URL like:
`https://delicate-mode-2bce.emi-dom123.workers.dev/?student=maria-garcia-2024`

The site reads the `?student=` parameter and uses it as a localStorage namespace. This means:
- Same device, same browser → progress is remembered
- Different URL token → different progress
- Teacher can share unique links per student
- No passwords, no database, no servers

**Limitations:** Still browser-only. No cross-device sync. Anyone with the URL can see the progress.

**Effort:** ~2 hours. Add 10 lines of JS to store.js.

---

### Phase 2 — Cloudflare D1 database (real persistence)
**How it works:** Add a Cloudflare D1 (SQLite) database to the Worker:
- Students log in with a simple name + code (no email required)
- Progress is saved to the database on every worksheet/game completion
- Students can log in on any device and see their progress
- Teachers get a `/teacher` dashboard showing all student progress

**Architecture:**
```
Student browser → Cloudflare Worker → D1 database
                                   → Static HTML (as now)
```

**Database tables:**
```sql
students (id, name, code, created_at, last_active)
progress (student_id, level, chapter_id, section, score, total, date)
game_results (student_id, level, chapter_id, mastered, total, date)
```

**Effort:** 1-2 sessions with Claude. The Worker already exists — we just add API routes.

**Limitations:** Requires Cloudflare D1 (free tier: 5GB, 5M reads/day — more than enough).

---

### Phase 3 — Teacher dashboard
**How it works:** A `/teacher` page (password-protected) showing:
- List of all students with last-active date
- Per-student progress grid (which chapters completed, scores)
- Class average scores per chapter
- Export to CSV for reporting

**Effort:** 1 session with Claude after Phase 2 is working.

---

### Phase 4 — Email login (optional)
**How it works:** Replace name+code with email-based magic links:
- Student enters email → receives a login link → clicks it → logged in
- No passwords to remember
- Uses Cloudflare Workers + Mailgun/Resend for email

**Effort:** 1-2 sessions. Only needed if you want proper accounts.

---

## Recommendation

**Start with Phase 1** (URL tokens). It takes 2 hours, solves the "which student is this" problem, and requires zero infrastructure. You can deploy it today.

**Move to Phase 2** when you have 10+ students using the site regularly and want to track their progress across devices. This is the real unlock — persistent progress + teacher visibility.

Phases 3 and 4 come naturally after Phase 2.

---

## Spanish course approach

### Option A — Parallel site at `/es/` (recommended)
A separate version of the site under `/es/` with:
- Same 6-level structure (A1→C2)
- Same JS engines (shared/)
- UI text in Spanish (headers, instructions, buttons, labels)
- Grammar explanations include Spanish translations + comparisons
- False-friend warnings and L1-interference notes at every level
- Pronunciation guides comparing Spanish and English sounds

**Pros:** Clean separation. English learners never see Spanish. Each course can evolve independently. Easier to maintain.

**Cons:** More HTML pages to maintain (potentially doubles the page count over time).

### Option B — Toggle/popup layer on existing site
Add a "Espanol" toggle button that:
- Switches instruction text to Spanish
- Shows Spanish translation popups on grammar terms
- Adds L1-interference warnings inline

**Pros:** One set of pages to maintain. Students can switch language on the fly.

**Cons:** Complex JS. Clutters the clean English-only design. Mixing languages in the code makes maintenance harder. Breaks Em's "no Spanish in main course" rule.

### Recommendation
**Option A — parallel `/es/` site.** It respects the clean separation Em wants, uses the same engines, and can be built incrementally (start with A1, expand level by level). The Spanish homepage skeleton is already at `/es/index.html` in v100.

Build order:
1. `/es/a1/` — 5-6 key grammar chapters with Spanish explanations + false-friend notes
2. `/es/a2/` — expand as A1 proves the format works
3. Continue level by level

Each chapter would have the same 4-file structure (slides, worksheet, game, printables) but with bilingual slide content.
