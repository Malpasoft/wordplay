---
name: insights
description: Generate a comprehensive project insights report for Word Play. Audits content coverage, shared engine versions, roadmap status, file health, and pending gaps — then outputs a styled mobile-friendly HTML file for the teacher to download and read on any device. Never commits or pushes anything.
---

# Word Play — Insights Report Skill

Generate a rich, styled HTML insights report covering the current state of the Word Play project. Deliver it as a downloadable file via SendUserFile. Never commit, never push.

## Workflow

Work through all steps below in order. Produce a single output file at the end.

### 1. Gather raw stats

Run these commands and capture their output:

```bash
# File counts by type
find /home/user/wordplay -name "*.html" | grep -v node_modules | wc -l
find /home/user/wordplay/a -name "*.html" | wc -l   # English A1–A2
find /home/user/wordplay/b -name "*.html" | wc -l   # English B1–B2
find /home/user/wordplay/c -name "*.html" | wc -l   # English C1–C2
find /home/user/wordplay/es -name "*.html" | wc -l  # Spanish (ES) track

# Stub detection — files that are placeholders
grep -rl "PLACEHOLDER\|Coming soon\|stub\|TODO" /home/user/wordplay/a /home/user/wordplay/b /home/user/wordplay/c /home/user/wordplay/es --include="*.html" 2>/dev/null | wc -l

# Count by page type
find /home/user/wordplay -name "slides.html" | grep -v node_modules | wc -l
find /home/user/wordplay -name "flashcards.html" | grep -v node_modules | wc -l
find /home/user/wordplay -name "match.html" | grep -v node_modules | wc -l
find /home/user/wordplay -name "game.html" | grep -v node_modules | wc -l
find /home/user/wordplay -name "worksheet.html" | grep -v node_modules | wc -l
find /home/user/wordplay -name "review.html" | grep -v node_modules | wc -l
find /home/user/wordplay -name "printable.html" | grep -v node_modules | wc -l

# Shared engine versions — grep version strings from HTML files
grep -r 'base\.css?v=' /home/user/wordplay/a/a1 --include="*.html" -h | grep -o 'v=[0-9]*' | sort -u | head -3
grep -r 'slides\.css?v=' /home/user/wordplay/a/a1 --include="*.html" -h | grep -o 'v=[0-9]*' | sort -u | head -3
grep -r 'deck\.js?v=' /home/user/wordplay/a/a1 --include="*.html" -h | grep -o 'v=[0-9]*' | sort -u | head -3
grep -r 'game\.js?v=' /home/user/wordplay/a/a1 --include="*.html" -h | grep -o 'v=[0-9]*' | sort -u | head -3
grep -r 'store\.js?v=' /home/user/wordplay/a/a1 --include="*.html" -h | grep -o 'v=[0-9]*' | sort -u | head -3

# Git status
cd /home/user/wordplay && git log --oneline -10
cd /home/user/wordplay && git branch --show-current
cd /home/user/wordplay && git status --short | wc -l

# Pedagogy check
cd /home/user/wordplay && python3 scripts/pedagogy_check.py 2>&1 | tail -5

# Search index size
wc -l /home/user/wordplay/shared/search-index.json 2>/dev/null || echo "not found"
python3 -c "import json; d=json.load(open('/home/user/wordplay/shared/search-index.json')); print(len(d),'chapters indexed')" 2>/dev/null || echo "unreadable"
```

### 2. Per-level content coverage

For each level directory (a1, a2, b1, b2, c1, c2) and for each of es/a1 through es/c2:
- Count total chapter folders
- Count complete chapters (have slides.html + at least one of flashcards.html/game.html)
- Count stub chapters (only index.html or only slides.html with PLACEHOLDER content)
- List any chapters missing slides.html entirely

Use find + bash loops for this — no manual listing.

```bash
for level in a1 a2; do
  dir="/home/user/wordplay/a/$level"
  echo "=== $level ==="
  for section in vocabulary grammar writing; do
    sdir="$dir/$section"
    [ -d "$sdir" ] || continue
    total=$(find "$sdir" -mindepth 1 -maxdepth 1 -type d | wc -l)
    complete=$(find "$sdir" -name "slides.html" | wc -l)
    stub=$(grep -rl "PLACEHOLDER\|Coming soon" "$sdir" --include="*.html" 2>/dev/null | wc -l)
    echo "  $section: $total chapters, $complete with slides, $stub stubs"
  done
done

for level in b1 b2; do
  dir="/home/user/wordplay/b/$level"
  echo "=== $level ==="
  for section in vocabulary grammar writing; do
    sdir="$dir/$section"
    [ -d "$sdir" ] || continue
    total=$(find "$sdir" -mindepth 1 -maxdepth 1 -type d | wc -l)
    complete=$(find "$sdir" -name "slides.html" | wc -l)
    stub=$(grep -rl "PLACEHOLDER\|Coming soon" "$sdir" --include="*.html" 2>/dev/null | wc -l)
    echo "  $section: $total chapters, $complete with slides, $stub stubs"
  done
done

for level in c1 c2; do
  dir="/home/user/wordplay/c/$level"
  echo "=== $level ==="
  for section in vocabulary grammar writing; do
    sdir="$dir/$section"
    [ -d "$sdir" ] || continue
    total=$(find "$sdir" -mindepth 1 -maxdepth 1 -type d | wc -l)
    complete=$(find "$sdir" -name "slides.html" | wc -l)
    stub=$(grep -rl "PLACEHOLDER\|Coming soon" "$sdir" --include="*.html" 2>/dev/null | wc -l)
    echo "  $section: $total chapters, $complete with slides, $stub stubs"
  done
done

# ES track
for level in a1 a2 b1 b2 c1 c2; do
  dir="/home/user/wordplay/es/$level"
  [ -d "$dir" ] || continue
  echo "=== es/$level ==="
  for section in vocabulary grammar writing; do
    sdir="$dir/$section"
    [ -d "$sdir" ] || continue
    total=$(find "$sdir" -mindepth 1 -maxdepth 1 -type d | wc -l)
    complete=$(find "$sdir" -name "slides.html" | wc -l)
    stub=$(grep -rl "PLACEHOLDER\|Coming soon" "$sdir" --include="*.html" 2>/dev/null | wc -l)
    echo "  $section: $total chapters, $complete with slides, $stub stubs"
  done
done
```

### 3. Identify top gaps

From the data above, compile:
- Levels/sections with most stub files (needs content work)
- Any missing page types (e.g. level has vocabulary chapters but no match.html anywhere)
- ES flashcard stubs count
- C1/C2 placeholder chapters

### 4. Roadmap status

Read `/root/.claude/plans/before-we-start-i-zazzy-starfish.md` and the recent git log.
Summarize:
- What's been shipped recently (last 10 commits)
- What's actively in progress
- What's next in the priority queue
- What's parked/horizon

### 5. Builder & dev tools status

Check:
```bash
ls /home/user/wordplay/builder.html && wc -l /home/user/wordplay/builder.html
ls /home/user/wordplay/dev-hub.html 2>/dev/null || echo "dev-hub missing"
ls /home/user/wordplay/scripts/*.py | head -20
```

### 6. Generate the HTML report

Write the report to `/tmp/wordplay-insights.html`.

The report must:
- Be a complete standalone HTML file (no external resources except Google Fonts via a single @import)
- Use the project's design tokens: `--paper:#F7F3EE`, `--ink:#1A1A1A`, `--amber:#B8860B`, `--cream:#F0EBE0`, `--hairline:#E0D8CC`, `--muted:#6B6560`
- Include a dark mode `@media(prefers-color-scheme:dark)` block
- Be fully mobile-readable at 360px width — no overflow, no tiny text
- Include these sections:
  1. **Header** — "Word Play · Insights" + date generated + current branch
  2. **At a Glance** — summary cards showing: total HTML files, total chapters indexed, pedagogy check status, current branch, last commit
  3. **Content Coverage** — table per track (EN / ES) showing for each level×section: total chapters, complete, stubs, percentage done. Use a progress bar per row (amber fill, hairline bg).
  4. **Top Gaps** — numbered list of the biggest content holes to fill
  5. **Shared Engine Versions** — table: asset name | current version | description
  6. **Roadmap Status** — three columns: Done (recent), In Progress, Up Next. Use check/circle/clock icons (text-based: ✓ ○ ◷ — these are content, not UI decoration)
  7. **Builder & Dev Tools** — what tools exist, their purpose
  8. **Footer** — "Generated by Claude Code · Word Play · malpasoft/wordplay"

Style rules:
- Font: system-ui, -apple-system, sans-serif (no Google Fonts needed)
- No emoji in UI chrome. Section icons may use simple Unicode like ◆ ▸ — but sparingly
- Progress bars: `height:6px; border-radius:3px; background:var(--amber)`
- Cards: `background:var(--cream); border:1px solid var(--hairline); border-radius:8px; padding:16px`
- Tables: clean, no outer border, alternating `var(--cream)` rows, sticky header
- Mobile: all tables `overflow-x:auto` wrapper
- "Complete" percentage ≥80% → amber text; <50% → muted red (`#c0392b` light / `#e74c3c` dark)

### 7. Deliver the file

Use SendUserFile to send `/tmp/wordplay-insights.html` to the user with status `normal`.
Caption: "Open in your phone browser — no internet needed."

Do NOT commit, push, or write to the repo at any point.

## Output

The only output is the SendUserFile call. End with a one-sentence summary of the biggest gap found.
