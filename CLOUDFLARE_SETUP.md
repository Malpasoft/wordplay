# Word Play — Cloudflare D1 Setup

The teacher tools (`calendar.html`, `profile.html`) sync across devices through a
Cloudflare D1 database. **This is a one-time setup.** Until it is done, the tools still
work — they fall back to localStorage-only (single browser, no cross-device sync).

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
- Auth on each route is the shared passphrase (`wordplay_sync_code`, 8–64 chars) stored
  in the browser. No accounts yet — the `user_id` column is reserved for the future auth
  upgrade.

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

## Adding new migrations

Number them sequentially (`0003_*.sql`). Run them the same way (dashboard console or
`wrangler d1 execute`). Always `CREATE TABLE IF NOT EXISTS` / `CREATE INDEX IF NOT EXISTS`
so re-running is safe.

---

*Reserved for the future auth upgrade (AUTH_PROPOSAL.md Phase 3): the same D1 DB will gain
`users`, `credentials`, `progress` tables; the `user_id` columns already present link
passphrase-era rows to real accounts.*
