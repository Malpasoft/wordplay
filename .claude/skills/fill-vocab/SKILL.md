# /fill-vocab

Fill one vocabulary chapter with 10 real words. Works in two modes — Opus authors directly
when tokens are available; otherwise emits a paste-ready free-AI prompt that DeepSeek/Gemini
can answer in the correct schema. Either way no hand-editing of HTML or code is required.

## Usage

```
/fill-vocab <track> <level> <slug>
```

Examples:
```
/fill-vocab es a1 colours
/fill-vocab en c1 abstract-nouns
/fill-vocab en c2 literary-devices
```

Tracks: `en` | `es`
Levels: `a1` `a2` `b1` `b2` `c1` `c2`
Slug: matches the chapter directory name (e.g. `abstract-nouns`, `colours`)

---

## Step 1 — Resolve the chapter

Locate the spec file:
```
scripts/chapter_specs/<track>-<level>-vocabulary-<slug>.json
```

Read it to confirm: `lang`, `level`, `slug`, `title`, `subtitle`. If the spec file doesn't
exist, infer those values from the directory path and chapter index page.

Then confirm the target files exist at:
- `<track>/<level>/vocabulary/<slug>/flashcards.html` (must be new template — see Step 3)
- `<track>/<level>/vocabulary/<slug>/game.html`
- `<track>/<level>/vocabulary/<slug>/slides.html`

If any file is missing, report it and stop — don't create new files from scratch.

---

## Step 2 — Decide mode

**Opus mode (default when tokens are available):** proceed to Step 3.

**Free-AI mode:** if the user asks for a prompt to paste into DeepSeek/Gemini, skip to Step 6.

---

## Step 3 — Confirm template (NEVER MIX THESE)

Read the first 30 lines of the chapter's `flashcards.html`. Confirm it uses the **new template**:
- Contains `MASTERY_KEY`, `SLUG`, `LEVEL`, `showCard()`, and `WORDS[{word, ipa, def, ex}]`

If it contains `STORAGE_KEY`, `renderCard()`, or `WORDS[{word, definition, example, pronunciation}]`
— that is the **old template (A1 English only)**. Stop immediately and warn: old template must not
be filled with the new schema. Report which file it is and ask the user how to proceed.

---

## Step 4 — Author the word data (Opus mode)

Generate 10 words for the chapter. Match the level:

| Level | Grade | Vocabulary reference |
|-------|-------|----------------------|
| A1    | beginner | CEFR A1 / DELE A1 common words |
| A2    | elementary | CEFR A2 |
| B1    | intermediate | CEFR B1 / PET-grade |
| B2    | upper-intermediate | CEFR B2 / FCE-grade |
| C1    | advanced | CEFR C1 / CAE-grade |
| C2    | proficient | CEFR C2 / CPE-grade |

For **ES track**: words are English words explained in Spanish (Spanish-explained format).
The `word` field is the English word; `def` and `ex` are in Spanish.

Produce a Python list literal ready to drop straight into the fill script:

```python
[
    {"id": 1, "word": "concept",     "ipa": "/ˈkɒnsept/",  "def": "an idea or principle", "ex": "The concept of gravity explains why objects fall."},
    {"id": 2, "word": "phenomenon",  "ipa": "/fɪˈnɒmɪnən/","def": "a fact or event in nature", "ex": "The aurora borealis is a natural phenomenon."},
    # ... 8 more
]
```

Rules:
- IPA must use British English phonemic transcription (`/slashes/`), consistent with `lang='en-GB'`
- `ex` must be a complete, natural sentence — not a sentence fragment
- No emoji anywhere
- No hardcoded colour values
- All 10 words must be distinct and appropriate to the chapter's theme (`subtitle` field is the hint)

---

## Step 5 — Write and verify (Opus mode)

**EN C1/C2 track:** The fill script is `scripts/fill_en_c1c2_vocab.py`. It uses a `CHAPTERS` dict
keyed by `'<level>/<slug>'`. Find the entry for this chapter (search for the slug in the file), then
replace the placeholder `WORDS` list with the generated list. Use the Edit tool — never sed/awk.

Confirm the pinned version dict `V = dict(base='v123', slides='v115', ...)` still matches the
current shared-asset versions in SESSION_CONTEXT before writing.

**ES track:** use `scripts/fill_chapter.py`. Run it pointed at the target chapter directory.

After writing, run:
```bash
python3 scripts/pedagogy_check.py
```

Must be **0 failures**. Warnings are non-blocking — report them but do not fail.

Also run:
```bash
python3 scripts/check_structure.py
```

Report what was filled. Do NOT commit or push — leave that to `/ship`.

---

## Step 6 — Free-AI mode (paste-ready prompt)

When the user needs a prompt for DeepSeek/Gemini because Opus tokens are low, emit this
prompt block — ready to copy-paste, no editing required:

```
Generate 10 vocabulary items for an English-language learning site.

Chapter: <title> (<subtitle>)
Level: <level_name> (CEFR <LEVEL>)
<ES instruction if track=es: "This is an English course explained in Spanish. The 'word' field is English; 'def' and 'ex' must be in Spanish.">

Output ONLY a valid JSON array, no prose, no markdown fences:
[
  {"id": 1, "word": "...", "ipa": "/.../ (British English)", "def": "...", "ex": "A complete example sentence."},
  {"id": 2, ...},
  ...
  {"id": 10, ...}
]

Rules:
- ipa: British English phonemic transcription in /slashes/
- def: concise definition (10 words or fewer)
- ex: a complete, natural sentence using the word in context
- No emoji. No markdown.
```

After Em pastes the JSON result back, ingest it:
1. Validate it is a list of 10 dicts each with keys `id word ipa def ex`
2. Check every `ex` is a complete sentence (starts uppercase, ends with `.`)
3. Check every `ipa` uses `/slashes/`
4. If valid, proceed to Step 5 (write + verify) exactly as in Opus mode
5. If invalid, show which items fail validation and ask the user to re-paste the corrected JSON
