#!/usr/bin/env python3
"""Generate shared/search-index.json from all chapter index.html files."""
import glob, re, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def extract_h1(content):
    m = re.search(r'<h1[^>]*class="[^"]*chapter-h1[^"]*"[^>]*>([^<]+)</h1>', content)
    if m: return m.group(1).strip()
    m = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if m: return m.group(1).strip()
    return ''

def extract_level_section(content, parts):
    """Extract level (e.g. A1) and section (e.g. Grammar) from title or path."""
    m = re.search(r'<title>([^<]+)</title>', content)
    if m:
        title = m.group(1)
        title = re.sub(r'\s*\|\s*Word Play.*$', '', title)
        # Look for level code: A1, A2, B1, B2, C1, C2, ES-A1 etc
        lm = re.search(r'\b([A-C][12](?:-[A-Z0-9]+)?)\b', title)
        # Look for section keyword
        sm = re.search(r'\b(Grammar|Vocabulary|Writing|Gramática|Vocabulario|Escritura)\b', title, re.I)
        level   = lm.group(1).upper() if lm else parts[1].upper()
        section = sm.group(1).title()  if sm else parts[2].title()
        return (level, section)
    return (parts[1].upper(), parts[2].title())

results = []
pattern = os.path.join(ROOT, '**', 'index.html')
for path in sorted(glob.glob(pattern, recursive=True)):
    rel = os.path.relpath(path, ROOT).replace('\\', '/')
    parts = rel.split('/')
    if len(parts) != 5:
        continue
    with open(path, encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if 'slides.html' not in content and 'game.html' not in content:
        continue
    h1 = extract_h1(content)
    if not h1:
        continue
    level, section = extract_level_section(content, parts)
    results.append({'url': '/' + rel, 'title': h1, 'level': level, 'section': section})

out = os.path.join(ROOT, 'shared', 'search-index.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, separators=(',', ':'))

print(f'Indexed {len(results)} chapters')
