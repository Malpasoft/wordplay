# Word Play — Cloudflare D1 Setup

A single Cloudflare D1 database (`wordplay_db`, binding `DB`) backs the whole app: user
accounts + token auth, student progress sync, classes/lessons/invite codes, and the teacher
tools (`calendar.html`, `profile.html`). **This is a one-time setup.** Until it is done — or
for logged-out users — the site still works, falling back to localStorage-only (single
browser, no cross-device sync). The full table list and API contracts are in **CLAUDE.md →
Architecture & Backend**; this file covers provisioning and verification.

> **Status: UNVERIFIED in code.** Whether the D1 database is actually created and bound
> lives in the Cloudflare dashboard, not the repo (there is no `wrangler.toml`). If
> cross-device sync isn't working, the steps below have not been completed on the
> Cloudflare side. Confirm in the dashboard.

---

## What's already in the repo

| Piece | Path | Role |
|-------|------|------|
| Profiles table | `migrations/0001_teacher_profiles.sql` | `teacher_profiles (code, data, updated_at, user_id)` |
| Lessons table | `migrations/0002_lessons.sql` | `lessons (id, code, title, student_ids, date, …)` + index |
| Profiles API | `functions/api/profiles/[code].js` | GET/POST `/api/profiles/:code` |
| Lessons API | `functions/api/lessons/[code].js` | GET/POST `/api/lessons/:code` |

- **Database name expected:** `wordplay_db`
- **Binding name expected:** `DB` (functions call `env.DB`)
- Both tables live in the **same** D1 database — one binding serves both.
- The legacy profiles/lessons routes (`/api/profiles/:code`, `/api/lessons/:code`) authenticate
  with a shared passphrase (`wordplay_sync_code`, 8–64 chars) stored in the browser. The newer
  account system (signup/login → 7-day bearer tokens, see CLAUDE.md) supersedes this for student
  progress; the `user_id` columns link passphrase-era rows to real accounts.

---

## One-time setup (Cloudflare dashboard + wrangler)

### Option A — Cloudflare dashboard (no local tooling)

1. **Workers & Pages → D1 → Create database.** Name it exactly `wordplay_db`.
2. Open the DB → **Console** tab → paste and run the contents of
   `migrations/0001_teacher_profiles.sql`, then `migrations/0002_lessons.sql`.
3. **Workers & Pages → your Pages project (`wordplay-38t`) → Settings → Functions →
   D1 database bindings → Add binding.**
   - Variable name: `DB`
   - D1 database: `wordplay_db`
4. **Redeploy** the Pages project (Deployments → Retry/redeploy latest, or push any commit).
   Bindings only take effect on a fresh deploy.

### Option B — wrangler CLI (if working locally)

```bash
npx wrangler d1 create wordplay_db
# copy the database_id wrangler prints

npx wrangler d1 execute wordplay_db --remote --file=migrations/0001_teacher_profiles.sql
npx wrangler d1 execute wordplay_db --remote --file=migrations/0002_lessons.sql
```

Then add the binding either in the dashboard (step 3 above) or via a `wrangler.toml`:

```toml
name = "wordplay-38t"
pages_build_output_dir = "."

[[d1_databases]]
binding = "DB"
database_name = "wordplay_db"
database_id = "<paste-the-id-from-create>"
```

Commit `wrangler.toml` and redeploy. (Note: the repo has no `wrangler.toml` today — the
binding is dashboard-only unless you add one.)

---

## How to verify it's live

1. Open `https://wordplay-38t.pages.dev/api/profiles/testtesttest` in a browser.
   - **Working:** `{"profiles":[],"updated_at":null}`
   - **Not set up:** a 500 error or HTML error page (means `env.DB` is undefined).
2. In `profile.html`, set a sync passphrase, add a student, then open the same passphrase
   on a second device — the student should appear.

---

## API contract (for future work / auth migration)

**Profiles** — `/api/profiles/:code`
- `GET` → `{ profiles: [...], updated_at }`
- `POST { profiles: [...] }` → upserts whole array → `{ ok: true, updated_at }`

**Lessons** — `/api/lessons/:code`
- `GET ?from=YYYY-MM-DD&to=YYYY-MM-DD` → `{ lessons: [...] }` (no range → all)
- `POST { action:"upsert", lesson:{...} }` → `{ ok:true }`
- `POST { action:"delete", id:"..." }` → deletes (code-guarded) → `{ ok:true }`
- `POST { action:"bulk", lessons:[...] }` → batch upsert (recurring slots) → `{ ok:true, count }`

`student_ids` is stored as a JSON string, parsed back to an array on GET.

---

## Environment variables / secrets (new — Phase 1)

Two secrets are needed for email (password reset + verification). Add them in:
**Workers & Pages → wordplay-38t → Settings → Environment variables → Add secret**

| Variable | Value | Notes |
|----------|-------|-------|
| `RESEND_API_KEY` | `re_xxxx…` | Get from resend.com (free tier: 3k/mo). Create an account, add a domain or use `onboarding@resend.dev` for testing. |
| `RESEND_FROM` | `Word Play <noreply@yourdomain.com>` | Must match a verified sender in Resend. For testing use `onboarding@resend.dev`. |
| `SITE_URL` | `https://wordplay-38t.pages.dev` | Used to build reset/verify links in emails. |

Until `RESEND_API_KEY` is set, email calls are skipped (logged as a warning) — signup, login, and
password requests still work without email, but no emails will be sent.

---

## Adding new migrations

Number them sequentially (next is `0009_*.sql`). Run them the same way (dashboard console or
`wrangler d1 execute`). Always `CREATE TABLE IF NOT EXISTS` / `CREATE INDEX IF NOT EXISTS`
so re-running is safe.

**New migrations to apply (Phases 1–4) — run in order:**
```bash
npx wrangler d1 execute wordplay_db --remote --file=migrations/0009_password_resets.sql
npx wrangler d1 execute wordplay_db --remote --file=migrations/0010_mistake_log.sql
npx wrangler d1 execute wordplay_db --remote --file=migrations/0011_booking.sql
npx wrangler d1 execute wordplay_db --remote --file=migrations/0012_user_profile.sql
npx wrangler d1 execute wordplay_db --remote --file=migrations/0013_class_invite_codes.sql
npx wrangler d1 execute wordplay_db --remote --file=migrations/0014_booking_unique_slot.sql
npx wrangler d1 execute wordplay_db --remote --file=migrations/0015_error_log.sql
```
Or paste each file's contents into the D1 dashboard console. They add: password-reset +
email-verification + consent + learner-profile columns, the mistake-analytics table, and the
booking tables. (The `ALTER TABLE` lines run once; re-running them errors harmlessly if the
column already exists.)

---

*The account system is already live: the same D1 DB holds `users`, `auth_tokens`,
`chapter_results`, `user_xp`, and the class/lesson/invite tables (see `migrations/*.sql` and
CLAUDE.md → Architecture & Backend). The `user_id` columns link passphrase-era rows to accounts.*
