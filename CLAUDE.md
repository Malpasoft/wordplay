# Word Play — Project Guide

> **This file is the single source of truth.** Project rules, architecture, backend, design
> system, git workflow, conventions, engine contracts, and pedagogy all live here — there is
> only ever one place to update. The only other living docs are: `CONTRIBUTING.md` (branch/PR
> workflow), `PEDAGOGY.md` (learning-design rules + checks), `SYLLABUS.md` (Cambridge mapping),
> `CLOUDFLARE_SETUP.md` (one-time D1 setup), and `TECH_DEBT.md` (open debt register).
>
> **Check `TECH_DEBT.md` before large refactors.**

## Who you're working with

**Em** — freelance English teacher in Catalunya, Spain. Works via GitHub + Claude Code (remote
sessions). Does not run local code, has no IDE. Direct, brief, no filler, no flattery; pushes
back on padded responses. Values: clean minimal formatting (no decorative emoji), amber-only
accent, finishing/polishing existing content over new features, constructive pushback when
she's wrong. Annoyed by: AI over-explaining instead of doing, silent drift from established
patterns, and Spanish-specific content leaking into the main English course.

## Project

Multi-language language-learning site (English, Spanish, French) on Cloudflare Pages.
Vanilla HTML/CSS/JS frontend, no build system — **but it is not a pure static site.** It is
backed by **Cloudflare Pages Functions + a D1 (SQLite) database** providing user accounts,
token auth, and cross-device progress sync (see *Architecture & Backend* below). localStorage
is a write-through cache, not the system of record. Teacher tools (calendar, profiles, dev-hub,
builder, coverage) live at root level. ≈2.5k HTML pages — see `coverage.html` for the live map.

**Repo:** `malpasoft/wordplay` · **Live:** `https://wordplay-38t.pages.dev` (Pages project
`wordplay-38t`) → auto-deploys from `main`.

### Course architecture

Homepage = 3 language cards → language hub → courses for that language.

| Hub | Course | Dir | UI lang | Levels | Exams |
|---|---|---|---|---|---|
| `/english/` | Main English | `a/ b/ c/` | en | A1–C2 | KET PET FCE CAE CPE |
| `/english/` | English for Spanish speakers | `es/` | es | A1–B2 | — |
| `/english/` | English for French speakers | `fr/` | fr | A1–B2 | — |
| `/espanol/` | Main Spanish | `espanol/` | es | A1–C2 ✅ | DELE ✅ |
| `/espanol/` | Spanish for English speakers | `espanol-en/` | en | A1–B2 | — |
| `/francais/` | Main French | `francais/` | fr | A1–C2 ✅ | DELF/DALF |
| `/francais/` | French for EN / ES speakers | `francais-en/ ✅ · francais-es/ (planned)` | en / es | A1–B2 | — |

**Rule: L1-mediated courses run A1–B2 only.** At C1+, learners continue in the main course
taught in the target language (each L1 landing page has a handoff card). es/ and espanol-en/
C1+C2 were deleted June 2026; `_redirects` covers old URLs.

### Per-chapter standard

- **Grammar**: index · slides (Lesson) · worksheet (Review) · game (Mastery) · printables
- **Vocab**: index · flashcards · slides (word list) · game (Mastery) · match
- **Writing**: index · slides · worksheet · game · printables
- Exam prep follows the FCE model (`b/b2/fce/`): about · strategy · writing-overview ·
  part-N (index + graded practice) · mock-1..3 (timed).

### Content state (high level)

- **English (`a/ b/ c/`)** — complete A1–C2 (grammar, vocab, writing all enriched). Two
  intentional "applied-grammar" vocab chapters (c1, c2) have no flashcards by design.
- **`es/`** — grammar (107 `gramatica/` chapters) ✅, writing (26) ✅, vocab flashcards ✅,
  vocab games ✅.
- **`espanol-en/`** — A1 + A2 complete; B1+B2 complete (June 2026). C1/C2 removed (L1 rule).
- **`fr/`** — A1+A2+B1+B2 complete. Vocab slides use English-only descriptions (not yet
  bilingual like `es/`) — tracked in TECH_DEBT.md (D7).
- **`espanol/`** — A1–C2 complete ✅; DELE exam prep A1–C2 (hub + about + mock-1 each) ✅.
- **`francais/`** — A1–C2 complete ✅ (grammar, vocab, writing; 146 chapters).
- **`francais-en/`** — A1–B2 complete ✅ (grammar, vocab, writing; 98 chapters). Vocab
  has bilingual `slides.html` word-lists; grammar games gap the answer from the French
  example (contexto), and all game/worksheet/slides load `i18n.js` for English UI labels.
- **`francais-es/`** — planned (only the landing page exists; A1–B2 levels not yet built).
- **Exam prep** — KET (a2) and PET (b1) fully rebuilt (graded parts + writing-overview +
  3 mocks each); FCE complete; CAE/CPE mocks 1–3 complete ✅ and linked from the C1/C2
  hubs (`c/c1/cae/`, `c/c2/cpe/`); DELE A1–C2 complete ✅.

---

## Architecture & Backend

The frontend is static vanilla HTML/CSS/JS. The backend is **Cloudflare Pages Functions**
(`functions/api/**`) over a **D1 SQLite** database. Source of truth for these facts is the
code itself: `wrangler.jsonc`, `migrations/*.sql`, `functions/api/`, `shared/store.js`,
`shared/auth.js` — read those before changing anything here.

- **D1 binding:** `DB` → database `wordplay_db` (id in `wrangler.jsonc`). Schema lives in
  `migrations/*.sql` (apply via the Cloudflare dashboard console or `wrangler d1 execute`;
  always `CREATE TABLE IF NOT EXISTS` so re-runs are safe). Core tables: `users`
  (incl. `email_verified`, `privacy_consent`, `consent_at`, `l1`, `target_lang`, `goal`),
  `auth_tokens`, `password_resets`, `chapter_results`, `mistake_log`, `user_xp`, `students`,
  `classes`, `class_enrollments`, `lessons`, `invite_codes` (teacher-based),
  `class_invite_codes` (class-based), `availability`, `booking_requests`,
  `rate_limit_log`, plus the legacy `teacher_profiles`.
- **Auth (`shared/auth.js`, loaded as `/shared/auth.js?v=1`):** email + password accounts.
  Passwords stored as PBKDF2 `hash:salt` in `users.password_hash`. Login/signup issue a
  7-day **bearer token** persisted in `auth_tokens`. Client caches token + user in
  localStorage keys `wp_token` / `wp_user`. Helpers: `getAuthToken`, `getCurrentUser`,
  `isLoggedIn`, `isAdmin/isTeacher/isStudent`, `setAuthState`, `clearAuthState`,
  `authenticatedFetch` (adds `Authorization: Bearer …`), `requireAuth`/`requireTeacher`/
  `requireStudent`/`requireAdmin`, `logout`.
  Roles: `admin` · `teacher` · `student`.
- **Email (`functions/api/_lib/email.js`):** thin Resend wrapper used for password reset
  and signup verification (and booking-confirmation emails). Needs Cloudflare secrets
  `RESEND_API_KEY`, `RESEND_FROM`, `SITE_URL` (see `CLOUDFLARE_SETUP.md`). If unset, email is
  skipped (logged) — auth still works. Signup records `privacy_consent`; GDPR export/delete
  endpoints back the dashboard's "Your data" panel.
- **Student-facing pages:** `dashboard.html` (progress + "My courses" navigator + weak-spots
  analytics + WhatsApp + GDPR), `book.html` (lesson booking), `login`/`signup`/`reset.html`,
  `privacy.html` / `terms.html`. Teacher booking lives in `teacher-bookings.html`.
- **Progress sync (`shared/store.js`):** localStorage is a write-through cache. Every result
  writes `wordplay_progress` locally, then a debounced (~1.5s) push plus a `pagehide` flush
  send progress to the API. On page load, signed-in users auto-pull and merge. Conflict
  resolution is last-write-wins by newer timestamp / higher pct / max XP+streak. If the user
  isn't logged in (or D1 is unreachable), everything still works localStorage-only.

### API contracts (`functions/api/**`)

All non-auth routes require `Authorization: Bearer <token>`. JSON in/out.

| Method · Path | Purpose |
|---|---|
| `POST /api/auth/signup` | Create account (email, password, level); PBKDF2 hash; returns token + user. Rate-limited per IP. |
| `POST /api/auth/login` | Verify password; returns token + `{user_id,email,role,l1,target_lang}`. |
| `POST /api/auth/logout` | Revoke the bearer token. |
| `POST /api/auth/request-reset` · `POST /api/auth/reset` | Forgot-password: email a 1-hour reset link, then set new password (revokes sessions). |
| `GET /api/auth/verify-email` | Mark email verified via a signup-issued token. |
| `GET·POST /api/student/progress` | Pull / push normalized progress (chapter_results + user_xp). Preferred sync route. |
| `GET·POST /api/student/mistakes` | Batch-record wrong answers; aggregated weakness report (by skill/chapter). |
| `GET /api/student/export` · `DELETE /api/student/delete-account` | GDPR: download all data / delete account (password-confirmed). |
| `GET·POST /api/availability` | Teacher weekly booking windows (POST replaces all; teacher only). |
| `GET·POST /api/bookings` · `PUT /api/bookings/[id]` | Student requests a slot; teacher confirms/declines (emails student); cancel. |
| `GET·POST /api/progress/[user_id]` | Legacy per-user progress (array or nested object). |
| `GET·POST /api/teacher/students` · `DELETE /api/teacher/students/[id]` | Teacher's student roster. |
| `POST /api/teacher/invite-code` · `POST /api/student/join-teacher` | Invite-code enrolment. |
| `GET·POST /api/classes` · `GET·PUT /api/classes/[id]` · `GET /api/classes/[id]/invite-code` | Class management. |
| `POST /api/lessons` · `GET·PUT·DELETE /api/lessons/[id]` | Lesson calendar events. |
| `GET /api/analytics/class/[teacher_id]` | Teacher analytics dashboard. |
| `GET /api/admin/users` · `POST /api/admin/migrate-progress` · `POST /api/setup` | Admin / one-time setup. |
| `GET·POST /api/profiles/[code]` · `/api/lessons/[code]` | Legacy passphrase-era teacher sync (superseded by token auth). |

One-time D1 provisioning (dashboard binding, migrations, verify) is in `CLOUDFLARE_SETUP.md`.

---

## Design System

- **Accent colour: amber only.** Always use `var(--amber)` — never hardcode a hex.
  Its real values are `#B8860B` (light mode) / `#C9A050` (dark mode). No second accent
  colour: no teal, gold, navy, or per-card colours.
  - **Allowed exception — activity-card type colours:** chapter hub `index.html` pages use
    `--ac-color` on activity cards. Lesson/practice cards: `var(--amber)`. Game cards:
    `#2E7D52` (green). Print cards: `#6B6B6B` (grey). These type colours are intentional UX
    and are **not** a design-system violation.
- **Background:** `var(--paper)` = `#F7F3EE` (warm parchment) / `#0E0E0E` dark. Ink text
  `var(--ink)` = `#1A1A1A` / `#F0F0F0` dark.
- **Clean, no-emoji UI.** The only symbols used as UI are `◐`/`◑` (dark-mode toggle) and
  `◆` (streak badge). A `.claude/hooks/design-check.sh` hook enforces this automatically
  on every edit — you don't need to police it manually.
- **SVG hearts** are used in match.html and worksheet.js for lives/hearts display. Use the
  standard path with `fill="currentColor"` so CSS color tokens drive the tint — never use
  the `♥`/`♡` Unicode glyphs (they trigger the hook).
- **Dark mode works on every element** — use `!important` overrides in CSS where needed.
- **`class="deck-body"`** on the `<body>` of every `slides.html` lesson page.
- **`class="sect-card"`** for section cards on level hub pages — never inline
  `onmouseover`/`onmouseout`.

**Design tokens (`base.css`):**
```css
--amber:   #B8860B (light) / #C9A050 (dark)   /* only accent — always var(--amber) */
--paper:   #F7F3EE (light) / #0E0E0E (dark)   /* background */
--ink:     #1A1A1A (light) / #F0F0F0 (dark)   /* text */
--cream:   #F0EBE0 (light) / #1A1A1A (dark)   /* card backgrounds */
--hairline:#E0D8CC (light) / #2E2E2E (dark)   /* borders */
--muted:   #6B6560 (light) / #9A9590 (dark)   /* secondary text */
```

---

## Git Workflow & Deployment

- **Develop on the session's feature branch — never commit directly to `main`.** Each session
  is told its branch name (branch names change per session; don't hardcode one here). Commit there as you go.
- **Deploy:** `git push origin HEAD:main` — Cloudflare Pages auto-deploys `main` (~2 min).
  Then keep the feature branch in sync: `git push -u origin <feature-branch>`.
- After completing a task, commit and push — don't stop before deploying.
- For large tasks, commit after each logical sub-task so a session interruption doesn't
  lose progress.
- If a visual change doesn't appear after deploy, suspect the Cloudflare edge cache.

---

## Cache-Busting (shared assets) — CRITICAL

**WHY THIS MATTERS:** Cloudflare Pages caches all `shared/` files for 1 year
(`max-age=31536000, immutable`). Without a version bump, **every deployment will serve
stale code forever** — users won't see any fixes or updates. This has caused
production outages (blank pages, hanging loads). The version parameter (`?v=vNN`) is
the ONLY way to force a cache refresh.

**When a shared file changes:**

1. **Identify the file** — e.g., `shared/store.js`, `shared/base.css`
2. **Bump its version** — increment `?v=vNN` to the next number across all HTML files
   - Use: `python3 bump-versions.py` (automates all HTML updates)
   - OR use `/ship` skill (safer, but slower)
   - Manual edits: prone to missing files — avoid
3. **Commit the version bumps** together with the code change
4. **The pre-commit hook enforces this** — commits are blocked if shared files are modified
   without version bumps

**Current versions (this list is canonical; kept in sync by the hook):**
- `base.css`: v125
- `dark-init.js`: v112
- `store.js`: v108
- `game.js`: v113
- `worksheet.js`: v109
- `deck.js`: v114
- `game.css`: v112
- `writing-grader.js`: v105
- `sentence-grader.js`: v104
- `mascot.js`: v3
- `slides.css`: v115
- `worksheet.css`: v107
- `print.css`: v102
- `i18n.js`: v124
- `print.js`: v102
- `auth.js`: v1

**Mascot assets** (added Q2 2026):
- `shared/mascot.css` — sprite animation rules (versions with `index.html`)
- `shared/mascot.js` — state manager & click handler (versions with `index.html`)
- `shared/mascot-bee.png` — sprite sheet image (versions with `index.html`)
- All cached 1 year; PNG also matches `/shared/*.png` rule in `_headers`

**Example commit:**
```
fix: sanitize innerHTML in game.js to prevent XSS

Bump game.js version from v110 to v111 across all HTML files.
Updated via bump-versions.py to ensure Cloudflare cache refresh.
```

`version.json` is a coarse project-state marker only — not a per-asset version.

---

## Bulk Edits

- **Prefer targeted `Edit` calls per file** over scripts that rewrite many HTML files at
  once — batch scripts have repeatedly produced orphaned tags, duplicate blocks, wrong data.
- If a script is genuinely needed (50+ files), verify output on 2–3 sample files first.
- **Never** use `sed`/`awk` to rewrite HTML — use Python with explicit string matching.
- Before any templated fix, `grep` for **all** structural/whitespace variants first.
  Grammar pages and Spanish/vocab pages often differ in whitespace — confirm the file
  count per variant matches expectation before running.

---

## Verification

- Verify visual changes with Playwright across **desktop, dark mode, and mobile (360px)**
  before calling them done.
- Never claim a value/state is "already correct" from memory — re-read the actual source
  line (and show a screenshot when it's a rendering question) before concluding.
- `python3 scripts/pedagogy_check.py` must stay at 0 failures before pushing; run
  `scripts/validate_inline_js.py` on touched HTML and `scripts/check_links.py` after nav changes.

---

## Pedagogy Principles (non-negotiable)

Full rules + automated checks are in `PEDAGOGY.md`. In short:

- Every worksheet question has an EXPLANATION — no exceptions.
- Grading is deterministic — never ask students to self-assess open production.
- Audio pronunciation on all vocab flashcards (Web Speech API, `lang='en-GB'`, `rate=0.9`).
- Flashcards auto-complete after viewing all cards.
- **Dominio Mastery Game (game.js):** 4 key items × 3 question types (significado/meaning, contexto/context, produccion/production). Score toward 100 points. Win = score ≥ 100 AND all 4 items correct. Correct answer = 10 pts (+5 same-item run bonus, +3 cross-item streak bonus). Wrong = -3 pts, requeue. Grading: significado/contexto = MC exact match; produccion = norm'd text match or item.accept[] aliases. See game.js JSDoc for full algorithm.
- Match game (match.html): 3 lives, each word must be matched to its definition twice to win. Mastery saved to localStorage (and synced to D1 for signed-in users) on win.

---

## MCP Configuration

- MCP servers go in `.mcp.json` at the project root — **not** in `.claude/settings.json`.

---

## Appendix — Engine contracts (`shared/`)

Engines have no dependencies/imports; pages link them with independent `?v=vNN` versions.
Roles: `base.css` layout+tokens+dark · `slides.css`+`deck.js` lesson decks · `game.css`+
`game.js` 4-stage mastery · `store.js` progress/XP wrapper + D1 sync · `worksheet.js`
auto-grader · `auth.js` accounts/tokens · `print.js` print modal · `dark-init.js` dark toggle.

**Lesson (`slides.html`)** — `<body class="deck-body">`, then:
```html
<script>window.LEVEL="a1"; window.CHAPTER_ID="animals";</script>
<script src="…/shared/store.js?v=v107"></script>
<script src="…/shared/deck.js?v=v114"></script>
```

**Worksheet (`worksheet.html`)** — every `ANSWERS` key must also be in `EXPLANATIONS`:
```html
<script>
window.CHAPTER_ID="slug"; window.LEVEL="a2"; window.TOTAL_POINTS=N;
window.ANSWERS      = { q1:"answer", … };
window.EXPLANATIONS = { q1:"reason", … };
</script>
```

**Game (`game.html`)** — `window.GAME_DATA = { chapterId, level, title, storageKey:
"wordplay_game_<level>_<slug>", items:[{id,term,meaning,synonym,example,completion,answer}] }`
(8–12 items).

**Two flashcard templates — never mix them:**
- *Old (A1 vocab only):* `STORAGE_KEY='wordplay_vocab_a1_<slug>_mastered'`,
  `WORDS=[{word,definition,example,pronunciation}]`, `renderCard()`, `markMastered()`.
- *New (A2–C2):* `MASTERY_KEY='wordplay_vocab_<level>_<slug>_mastered'`, `SLUG`, `LEVEL`,
  `WORDS=[{word,ipa,def,ex}]`, `showCard()`, `markMastered()`.

**Match (`match.html`):** `MASTERY_KEY`, `PROG_KEY=<level>`, `SLUG`,
`TOTAL_NEEDED=WORDS.length*2` (each word matched twice), 3 lives. Generated by
`builder.html` (`generateMatch`) or `scripts/gen_match.py` in bulk.

**localStorage schema (write-through cache; mirrored to D1 for signed-in users):**
```
wordplay_progress = { a1: {
  'slides_<chapterId>':        {done,date},
  '<chapterId>':               {pct,done},        // worksheet
  'wordplay_game_<chapterId>': {pct},             // game score
  'vocab_mastered_<topic>':    {done,date},       // flashcard mastery
}, a2:{…}, … }
wordplay_dark = "1" | "0"
wp_token, wp_user                                 // auth (see shared/auth.js)
```
Dashboard counts vocab mastered per level via `lv['vocab_mastered_'+slug].done`.
