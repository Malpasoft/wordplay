#!/usr/bin/env python3
"""
Pedagogy compliance checker — run from repo root.
Reports violations against PEDAGOGY.md rules.
"""
import re, os, glob, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
warnings = []
passed = 0

def err(path, msg):
    errors.append(f"  FAIL  {path.replace(BASE+'/', '')}: {msg}")

def warn(path, msg):
    warnings.append(f"  WARN  {path.replace(BASE+'/', '')}: {msg}")

def ok():
    global passed
    passed += 1

def read(path):
    with open(path) as f:
        return f.read()

# ── Check 1: Audio button on all flashcards ───────────────────────────
for path in glob.glob(f'{BASE}/**/flashcards.html', recursive=True):
    h = read(path)
    if 'var WORDS' not in h and 'STORAGE_KEY' not in h:
        continue  # placeholder page, not a real flashcard deck
    if 'speakWord' in h:
        ok()
    else:
        err(path, "missing speakWord (no audio button)")

# ── Check 2: Item count 8–12 ──────────────────────────────────────────
for path in glob.glob(f'{BASE}/**/flashcards.html', recursive=True):
    h = read(path)
    # New template
    m = re.search(r'var WORDS\s*=\s*(\[.*?\]);', h, re.DOTALL)
    if m:
        try:
            count = len(json.loads(m.group(1)))
            if count < 8:
                err(path, f"only {count} words (minimum 8)")
            elif count > 15:
                err(path, f"{count} words (maximum 15)")
            else:
                ok()
        except:
            warn(path, "could not parse WORDS array")

for path in glob.glob(f'{BASE}/**/game.html', recursive=True):
    h = read(path)
    m = re.search(r'"items"\s*:\s*(\[.*?\])\s*\}', h, re.DOTALL)
    if m:
        try:
            count = len(json.loads(m.group(1)))
            if count < 8:
                err(path, f"only {count} game items (minimum 8)")
            elif count > 15:
                err(path, f"{count} game items (maximum 15)")
            else:
                ok()
        except:
            pass

# ── Check 3: ANSWERS / EXPLANATIONS key parity ───────────────────────
for path in glob.glob(f'{BASE}/**/worksheet.html', recursive=True):
    h = read(path)
    ans_keys = set(re.findall(r'(\w+)\s*:\s*\{answer:', h))
    exp_keys = set(re.findall(r'"?(\w+)"?\s*:\s*"', h.split('EXPLANATIONS')[1] if 'EXPLANATIONS' in h else ''))
    if not ans_keys:
        continue
    if 'EXPLANATIONS' not in h:
        err(path, "missing EXPLANATIONS object")
    else:
        missing = ans_keys - exp_keys
        if missing:
            err(path, f"EXPLANATIONS missing keys: {sorted(missing)}")
        else:
            ok()

# ── Check 4: Lesson slides link to worksheet ─────────────────────────
for path in glob.glob(f'{BASE}/**/slides.html', recursive=True):
    h = read(path)
    # Skip vocab slides (no worksheet) and es/ slides
    if '/vocabulary/' in path and '/es/' not in path:
        # vocab slides should link to game
        if 'game.html' not in h:
            warn(path, "vocab lesson has no link to game.html")
        else:
            ok()
    elif '/grammar/' in path or '/gramatica/' in path:
        if 'worksheet.html' not in h:
            err(path, "grammar lesson has no CTA to worksheet.html")
        else:
            ok()

# ── Check 5: Grammar slides have trap-row (common mistakes) ──────────
for path in glob.glob(f'{BASE}/**/grammar/**/slides.html', recursive=True):
    h = read(path)
    if 'trap-row' in h or 'trap-wrong' in h:
        ok()
    else:
        warn(path, "no common-mistakes (trap-row) slide")

# ── Check 6: Three-file completeness for vocab topics ────────────────
for level_dir in glob.glob(f'{BASE}/*/*/vocabulary/'):
    for topic_dir in glob.glob(level_dir + '*/'):
        slug = os.path.basename(topic_dir.rstrip('/'))
        if slug in ('index.html',): continue
        files = os.listdir(topic_dir)
        has_flash = 'flashcards.html' in files
        has_slides = 'slides.html' in files
        has_game = 'game.html' in files
        if has_flash and has_slides and has_game:
            ok()
        else:
            missing = [f for f, v in [('flashcards.html', has_flash), ('slides.html', has_slides), ('game.html', has_game)] if not v]
            warn(topic_dir, f"missing: {', '.join(missing)}")

# ── Report ────────────────────────────────────────────────────────────
print(f"\nPedagogy Check — Word Play")
print(f"{'='*50}")
print(f"  Passed: {passed}")
print(f"  Warnings: {len(warnings)}")
print(f"  Failures: {len(errors)}")
print()

if errors:
    print("FAILURES:")
    for e in sorted(errors):
        print(e)
    print()

if warnings:
    print("WARNINGS:")
    for w in sorted(warnings):
        print(w)
    print()

if not errors and not warnings:
    print("All checks passed.")

import sys
sys.exit(1 if errors else 0)
