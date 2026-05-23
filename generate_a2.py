import os
"""Generate A2 chapters from JSON content."""
import json, os, sys

BASE = os.environ.get('WP_SITE', os.path.join(os.path.dirname(os.path.abspath(__file__))))
SHARED = '../../../../shared/'
HUB = '../../../../a/a2/index.html'

WP_LOGO = '<svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>'

def header(level_label, slug):
    return f'''<header class="site-header">
  <div class="site-header-inner">
    <a href="../../index.html" class="back back-link">A2 Grammar</a>
    <a href="../../index.html" class="brand">{WP_LOGO}Word Play</a>
    <button class="dark-toggle" onclick="toggleDark()">&#9680; Dark</button>
  </div>
</header>'''

def breadcrumb(slug, label, current):
    return f'''<div class="breadcrumb">
  <a href="../../../../index.html">Home</a><span>›</span>
  <a href="../../index.html">A2</a><span>›</span>
  <a href="../index.html">Grammar</a><span>›</span>
  <strong>{label} — {current}</strong>
</div>'''

def chapter_nav(active):
    tabs = [('slides.html','Lesson'), ('worksheet.html','Practice'), ('game.html','Game'), ('printables.html','Printables')]
    items = []
    for href, label in tabs:
        cls = 'chapter-nav-btn active' if href == active else 'chapter-nav-btn'
        items.append(f'<a href="{href}" class="{cls}">{label}</a>')
    return f'<nav class="chapter-nav">{"".join(items)}</nav>'

def render_slide(s):
    rows_html = ''
    if s.get('intro'):
        rows_html += f'<p style="font-size:1.05rem;color:var(--ink);margin-bottom:14px">{s["intro"]}</p>'
    for row in s.get('rows', []):
        label, desc = row
        rows_html += f'<div class="overview-row"><div class="overview-label">{label}</div><div class="overview-desc">{desc}</div></div>'
    if s.get('watch_out'):
        rows_html += f'<div class="watch-out">{s["watch_out"]}</div>'
    if s.get('cta'):
        rows_html += '<div class="deck-cta"><a href="worksheet.html" class="btn-cta">Practice now</a></div>'
    
    return f'''<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2>{s["h2"]}</h2></div>
  {rows_html}
</div></div>'''

def build_slides(ch, level='a2'):
    slides_html = '\n'.join(render_slide(s) for s in ch['slides'])
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>A2 · {ch['label']} — Lesson | Word Play</title>
<link rel="stylesheet" href="../../../../shared/base.css">
<link rel="stylesheet" href="../../../../shared/slides.css">
<script src="../../../../shared/dark-init.js"></script>
</head>
<body>
<div class="deck-progress"><div class="deck-progress-fill" id="deck-progress-fill"></div></div>
{header('A2 · Grammar', ch['slug'])}
<div class="container">
  {breadcrumb(ch['slug'], ch['label'], 'Lesson')}
  <div class="chapter-num">Ch {ch['num']}</div>
  <h1>{ch['label']}</h1>
  <p class="chapter-subtitle">{ch['subtitle']}</p>
  {chapter_nav('slides.html')}
  
  <div id="slide-deck">
    {slides_html}
  </div>
  
  <div class="deck-footer">
    <button id="prevBtn" class="deck-nav-btn" onclick="prevSlide()">‹ Prev</button>
    <span id="slide-counter" class="slide-counter">1 / {len(ch['slides'])}</span>
    <button id="nextBtn" class="deck-nav-btn" onclick="nextSlide()">Next ›</button>
  </div>
</div>
<footer class="site-footer">Word Play · Cambridge English A1→C2</footer>
<script>window.CHAPTER_ID = '{ch['slug']}'; window.LEVEL = '{level}';</script>
<script src="../../../../shared/deck.js"></script>
</body>
</html>'''

def build_worksheet(ch, level='a2'):
    ws = ch['worksheet']
    
    # Build ex1 (multiple choice)
    ex1_qs = []
    for i, q in enumerate(ws['ex1']['questions'], 1):
        opts = ''.join(f'<button type="button" class="choice-btn" data-value="{o}">{o}</button>' for o in q['options'])
        ex1_qs.append(f'''<div class="q"><span class="q-num">{i}</span>
    <div class="q-text">{q["q"]}</div>
    <div class="choice-group" data-q="e1q{i}" data-answer="{q["answer"]}">{opts}</div>
  </div>''')
    ex1_html = '\n'.join(ex1_qs)
    
    # Build ex2 (fill-in)
    ex2_qs = []
    answers_obj = {}
    for i, q in enumerate(ws['ex2']['questions'], 1):
        ex2_qs.append(f'''<div class="q"><span class="q-num">{i}</span>
    <div class="q-text">{q["q"].replace("_____", '<input type="text" data-q="e2q' + str(i) + '" style="width:140px">')}</div>
  </div>''')
        entry = {'answer': q['answer']}
        if 'accept' in q: entry['accept'] = q['accept']
        answers_obj[f'e2q{i}'] = entry
    ex2_html = '\n'.join(ex2_qs)
    
    # JS answers object
    answers_js_parts = []
    for k, v in answers_obj.items():
        parts = [f'answer:"{v["answer"]}"']
        if 'accept' in v:
            accepts = ','.join(f'"{a}"' for a in v['accept'])
            parts.append(f'accept:[{accepts}]')
        answers_js_parts.append(f'{k}:{{{",".join(parts)}}}')
    answers_js = ',\n  '.join(answers_js_parts)
    
    total = len(ws['ex1']['questions']) + len(ws['ex2']['questions'])
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>A2 · {ch['label']} — Practice | Word Play</title>
<link rel="stylesheet" href="../../../../shared/base.css">
<link rel="stylesheet" href="../../../../shared/worksheet.css">
<script src="../../../../shared/dark-init.js"></script>
</head>
<body>
{header('A2 · Grammar', ch['slug'])}
<div class="container">
  {breadcrumb(ch['slug'], ch['label'], 'Practice')}
  <div class="chapter-num">Ch {ch['num']}</div>
  <h1>{ch['label']}</h1>
  <p class="chapter-subtitle">{ch['subtitle']}</p>
  {chapter_nav('worksheet.html')}
  
  <section class="exercise" id="ex1">
    <div class="ex-head">Exercise 1</div>
    <div class="ex-title">{ws['ex1']['title']}</div>
    <div class="ex-meta">{len(ws['ex1']['questions'])} points</div>
    {ex1_html}
  </section>
  
  <section class="exercise" id="ex2">
    <div class="ex-head">Exercise 2</div>
    <div class="ex-title">{ws['ex2']['title']}</div>
    <div class="ex-meta">{len(ws['ex2']['questions'])} points</div>
    {ex2_html}
  </section>
  
  <div class="submit-wrap" style="max-width:800px;margin:24px auto;padding:0 20px;display:flex;gap:10px">
    <button onclick="checkAnswers()" style="flex:1;padding:12px;background:var(--ink);color:var(--paper);font-family:var(--font-sans);font-size:.8rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;border:none;border-radius:4px;cursor:pointer">Check Answers</button>
    <button onclick="resetAll()" style="padding:12px 20px;background:transparent;color:var(--ink);font-family:var(--font-sans);font-size:.8rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;border:1.5px solid var(--hairline);border-radius:4px;cursor:pointer">Reset</button>
  </div>
  
  <div id="results" style="max-width:800px;margin:24px auto 0;padding:0 20px;display:none">
    <div style="background:var(--paper);border:1px solid var(--hairline);border-radius:8px;padding:20px 24px">
      <div style="display:flex;align-items:center;gap:20px;margin-bottom:16px">
        <div style="font-family:var(--font-sans)">
          <span style="font-size:2rem;font-weight:800;color:var(--ink)" id="score-got">0</span>
          <span style="font-size:1rem;color:var(--muted)"> / </span>
          <span style="font-size:1rem;color:var(--muted)" id="score-total">0</span>
        </div>
        <div style="flex:1">
          <div style="font-family:var(--font-sans);font-size:1.1rem;font-weight:700;color:var(--ink)" id="score-pct">0%</div>
          <div style="font-family:var(--font-sans);font-size:.7rem;color:var(--muted);text-transform:uppercase;letter-spacing:1px">Score</div>
          <div id="pass-msg" class="pass-msg"></div>
        </div>
        <button onclick="resetAll()" style="font-family:var(--font-sans);font-size:.7rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:8px 14px;border-radius:4px;border:1.5px solid var(--hairline);background:transparent;color:var(--ink);cursor:pointer">Try again</button>
      </div>
      <div style="margin-top:14px;padding-top:14px;border-top:1px solid var(--hairline)">
        <div style="font-family:var(--font-sans);font-size:.65rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);margin-bottom:8px">By exercise</div>
        <div id="exercise-breakdown"></div>
      </div>
      <div id="breakdown"></div>
    </div>
  </div>
</div>
<footer class="site-footer">Word Play · Cambridge English A1→C2</footer>
<script>
window.CHAPTER_ID = '{ch['slug']}';
window.LEVEL = '{level}';
window.TOTAL_POINTS = {total};
window.ANSWERS = {{
  {answers_js}
}};
window.EXERCISE_TITLES = {{
  ex1: "Exercise 1 — {ws['ex1']['title']}",
  ex2: "Exercise 2 — {ws['ex2']['title']}"
}};
</script>
<script src="../../../../shared/worksheet.js"></script>
</body>
</html>'''

def build_game(ch, level='a2'):
    items_js = ',\n'.join(
        '{' + ','.join(f'{k}:{json.dumps(v)}' for k,v in item.items()) + '}'
        for item in ch['game']
    )
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>A2 · {ch['label']} — Game | Word Play</title>
<link rel="stylesheet" href="../../../../shared/base.css">
<link rel="stylesheet" href="../../../../shared/game.css">
<script src="../../../../shared/dark-init.js"></script>
</head>
<body>
{header('A2 · Grammar', ch['slug'])}
<div class="container">
  {breadcrumb(ch['slug'], ch['label'], 'Game')}
  <div class="chapter-num">Ch {ch['num']}</div>
  <h1>{ch['label']}</h1>
  <p class="chapter-subtitle">{ch['subtitle']}</p>
  {chapter_nav('game.html')}
  
  <div class="game-wrap" id="gameWrap">
    <!-- game.js renders here -->
  </div>
</div>
<footer class="site-footer">Word Play · Cambridge English A1→C2</footer>
<script>
window.GAME_DATA = {{
  chapterId: '{ch['slug']}',
  level: '{level}',
  title: '{ch['label']}',
  storageKey: 'wordplay_game_{level}_{ch['slug']}',
  items: [
    {items_js}
  ]
}};
</script>
<script src="../../../../shared/store.js"></script>
<script src="../../../../shared/game.js"></script>
</body>
</html>'''

def write_chapter(ch, level='a2'):
    band = 'a' if level[0] == 'a' else ('b' if level[0] == 'b' else 'c')
    d = f'{BASE}/{band}/{level}/grammar/{ch["slug"]}'
    os.makedirs(d, exist_ok=True)
    
    open(f'{d}/slides.html', 'w').write(build_slides(ch, level))
    open(f'{d}/worksheet.html', 'w').write(build_worksheet(ch, level))
    open(f'{d}/game.html', 'w').write(build_game(ch, level))
    print(f'  ✓ {ch["slug"]} (Ch {ch["num"]})')

if __name__ == '__main__':
    json_path = sys.argv[1] if len(sys.argv) > 1 else '/tmp/a2_content_part1.json'
    data = json.load(open(json_path))
    print(f'Building {len(data["chapters"])} A2 chapters...')
    for ch in data['chapters']:
        write_chapter(ch)
    print('Done.')
