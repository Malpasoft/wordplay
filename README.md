# Word Play

A complete Cambridge English learning website, from A1 (beginner) to C2 (mastery). Built by Em — a freelance English teacher in Catalunya — with Claude (Anthropic's AI) as a coding collaborator.

**Live site:** https://delicate-mode-2bce.emi-dom123.workers.dev/

---

## What this is

Word Play is a static educational website that runs entirely in the browser. There is no backend, no database, no login system — every student's progress is stored privately in their own browser. Students can use it without creating an account.

The site covers the complete Cambridge English curriculum across **six levels** (A1, A2, B1, B2, C1, C2). For each level, there are:

- **Grammar chapters** — a lesson, a practice worksheet, a mastery game, and a printable worksheet
- **Vocabulary topics** — flashcards, a mini-lesson, and a 4-stage mastery game
- **Writing chapters** — task instructions, model answers, and a live writing grader
- **Cambridge exam prep** — full strategy + practice for FCE (B2), CAE (C1), and CPE (C2)

---

## Content snapshot

| Level | Grammar | Vocabulary | Writing | Exam prep |
|-------|---------|------------|---------|-----------|
| A1    | 25      | 6          | 3       | —         |
| A2    | 18      | 6          | 3       | —         |
| B1    | 19      | 11         | 3       | —         |
| B2    | 20      | 16         | 5       | **FCE** (full)  |
| C1    | 17      | 7          | 5       | **CAE** (strategy + per-part guides) |
| C2    | 11      | 7          | 2       | **CPE** (strategy + per-part guides) |

- **822 HTML pages** total
- **110 grammar chapters** — every one has lesson, worksheet, game, printables
- **53 vocab topics** — every one has 10–12 standardised game items
- **All worksheets are auto-graded** with per-question explanations
- **All games use a 4-stage mastery system** (recognition → meaning → context → production)

---

## How students use it

1. They open the homepage (or follow a link to a specific lesson).
2. They read the lesson slides.
3. They practise on the worksheet (instant grading + explanations).
4. They play the mastery game (4 stages per word/structure).
5. Their progress is saved locally in their browser. The next time they open the site, their dashboard shows their progress.

Students can also:
- Take a **placement test** to find their level
- See a **progress dashboard** with XP and radar charts
- Print a **completion certificate** for any finished level
- Use the **dark mode** toggle in the header

---

## Maintaining the site (non-technical guide)

### Quick changes (text only)

If you want to fix a typo or change wording on a single page:

1. Open the HTML file in any text editor (TextEdit on Mac, Notepad on Windows).
2. Find the text and edit it carefully — **never edit anything inside angle brackets like `<div class="...">`**, only edit the visible text between tags.
3. Save the file.
4. Re-upload the file to Cloudflare Workers.

### Bigger changes (new content, structural changes)

Use Claude (claude.ai) and follow these steps:

1. Download the latest zip (e.g. `WordPlay_v89.zip`).
2. Start a new Claude conversation. Upload the zip.
3. Paste this prompt to orient Claude:

   > "I am continuing work on Word Play, my Cambridge English learning website. I am attaching the latest zip. Please read `AI_HANDOVER.md` first, then `SESSION_CONTEXT.md`. After that, I want to: [describe your change]."

4. Let Claude work. It will produce a new zip.
5. Download the new zip and upload to Cloudflare.

### Deployment to Cloudflare Workers

1. Log in to Cloudflare at https://dash.cloudflare.com
2. Go to **Workers & Pages → your worker** (currently `delicate-mode-2bce`)
3. Click **Edit code**
4. Either upload the whole zip's `site/` contents, OR replace files one by one
5. Click **Save and Deploy**

### Force browsers to load updated files

After each upload, the site uses a version number (`?v=v89`) on all CSS/JS files. This makes browsers fetch the new versions instead of using cached copies. You don't need to do anything for this to work — it's automatic.

If you ever update the CSS/JS by hand and want to force a refresh, bump the version in `version.json` and ask Claude to re-cache-bust the HTML files.

---

## What NOT to do

- **Do not edit anything inside `shared/` unless you know what you're doing.** Those files power every page.
- **Do not delete or rename folders.** The site uses relative paths — moving anything will break links.
- **Do not save HTML files with rich text formatting** (e.g. from Word). Use a plain text editor.
- **Do not commit student data** — there is no database, but if you ever add one, never log or share student progress.

---

## File structure (overview)

```
site/
  index.html                     homepage
  dashboard.html                 student progress dashboard
  placement-test.html            20-question level finder
  progress-certificate.html      printable PDF certificate
  404.html                       not-found page
  favicon.svg
  README.md                      this file
  SESSION_CONTEXT.md             technical context for AI assistants
  AI_HANDOVER.md                 full handover documentation
  version.json                   version tracker

  shared/                        all CSS & JS engines (do not edit lightly)
    base.css, slides.css, worksheet.css, game.css
    store.js, deck.js, worksheet.js, game.js, writing-grader.js,
    sentence-grader.js, dark-init.js

  a/a1/   a/a2/                  Beginner & Elementary
  b/b1/   b/b2/                  Intermediate & Upper-Intermediate
  c/c1/   c/c2/                  Advanced & Mastery

    index.html                   level home
    grammar/                     grammar chapters
    vocabulary/                  vocab topics
    writing/                     writing tasks
    certificate.html             per-level certificate

  b/b2/fce/                      FCE exam prep (B2 First)
  c/c1/cae/                      CAE exam prep (C1 Advanced)
  c/c2/cpe/                      CPE exam prep (C2 Proficiency)
```

---

## Credits

- **Curriculum, content, vision:** Em (English teacher, Catalunya)
- **Code generation:** Claude (Anthropic)
- **Hosting:** Cloudflare Workers (free tier)
- **All content is original** — no Cambridge IP used; everything is teacher-authored

---

## Version

See `version.json` for the current build number. Bump it whenever you ship a meaningful change.
