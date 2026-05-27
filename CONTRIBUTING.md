# Contributing to Word Play

## How this project works

**`main` is production.** Cloudflare Pages auto-deploys every push to `main`. Nothing goes into `main` without the owner ([@Malpasoft](https://github.com/Malpasoft)) reviewing and approving it.

---

## Branch naming

| Who | Branch pattern | Example |
|-----|---------------|---------|
| Claude (Anthropic) | `claude/batch-N` | `claude/batch-2` |
| Grok (xAI) | `grok/topic` | `grok/audit-p0-p1` |
| Owner | `user/topic` | `user/homepage-hero` |
| Experiments | `exp/topic` | `exp/new-game-type` |

Always branch from the latest `main`:
```bash
git fetch origin
git checkout -b your-branch-name origin/main
```

---

## Workflow

```
main  (production — reviewed merges only)
  ↑
  │  PR opened → owner approves → merge
  │
  ├── claude/batch-N     ← Claude works here
  ├── grok/topic         ← Grok works here
  └── user/topic         ← Owner experiments here
```

1. **Do all work on your branch** — never commit directly to `main`
2. **Commit often** — one logical change per commit, clear message
3. **Open a PR** when a batch is ready — title and description in plain English
4. **Owner reviews** the PR, approves or requests changes
5. **Merge** only after explicit approval

---

## Design rules (non-negotiable)

These are enforced on every PR. If your changes violate them, the PR will be sent back.

- **Accent colour: amber only** — `#E8A020` / `var(--amber)`. No teal, no navy, no per-card colours.
- **No emojis** — anywhere in UI or content. Only exceptions: `◐`/`◑` (dark toggle), `◆` (streak badge).
- **Dark mode must work on every element** — use `!important` overrides where needed.
- **`class="deck-body"`** on `<body>` of every `slides.html` page.
- **`class="sect-card"`** for dark section cards on level hub pages — never inline `onmouseover/onmouseout`.
- **Cache-bust** all `shared/` asset URLs with `?v=vNN` when you touch them.
- **Pedagogy check must stay at 0 failures** — run `python3 scripts/pedagogy_check.py` before pushing.

---

## Commit messages

```
type: short description (what changed)

Longer explanation if needed — the WHY, not the what.
```

Types: `fix`, `feat`, `content`, `style`, `refactor`, `docs`

No emojis in commit messages.

---

## File conventions

- **Static site only** — vanilla HTML/CSS/JS, no build step, no npm
- **~822 HTML pages** — prefer targeted `Edit` calls over batch scripts
- **Two flashcard templates** — never mix them:
  - Old (A1 vocab): `STORAGE_KEY`, `WORDS[{word, definition, example, pronunciation}]`, `renderCard()`
  - New (A2–C2): `MASTERY_KEY`, `SLUG`, `LEVEL`, `WORDS[{word, ipa, def, ex}]`, `showCard()`
- **Progress storage**: `wordplay_progress → { a1: { slug: {score,pct,date} } }` in localStorage
- **MCP config** goes in `.mcp.json` at project root — not in `.claude/settings.json`

---

## Pedagogy principles (enforced by `scripts/pedagogy_check.py`)

1. Every worksheet question has an EXPLANATION — no exceptions
2. Grading is deterministic — never ask students to self-assess open production
3. Audio pronunciation on all vocab flashcards (Web Speech API, `lang='en-GB'`, `rate=0.9`)
4. Flashcards auto-complete after viewing all cards; match game after 5 rounds
5. Every grammar slides.html has at least one `.trap-row` (common mistakes slide)
6. Every grammar slides.html ends with a worksheet CTA

---

## PR checklist (before opening)

- [ ] `python3 scripts/pedagogy_check.py` → 0 failures
- [ ] Dark mode tested on changed pages
- [ ] No emojis introduced
- [ ] No new accent colours other than amber
- [ ] Cache-bust version bumped if `shared/` files touched
- [ ] PR description lists what changed in plain English (not code)
