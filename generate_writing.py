#!/usr/bin/env python3
"""Universal writing chapter generator for Word Play.

Usage:
  python3 generate_writing.py content.json

JSON shape:
{
  "level": "b2",          -- a1/a2/b1/b2/c1
  "slug": "essay",        -- directory name
  "label": "The Essay",   -- display title
  "subtitle": "Plan and write a balanced discursive essay",
  "slides": [
    { "h2": "Slide title", "intro": "Optional intro.", "rows": [["Label","Content"]], "wo": "Watch-out tip." }
  ],
  "game_items": [
    { "id": "id1", "term": "Term", "meaning": "Definition", "synonym": "Synonym",
      "example": "Sentence with <b>bold</b>.", "completion": "Sentence with ______.", "answer": "answer" }
  ]
}

The generator outputs:
  {band}/{level}/writing/{slug}/slides.html
  {band}/{level}/writing/{slug}/worksheet.html  (writing prompt template)
  {band}/{level}/writing/{slug}/game.html
  {band}/{level}/writing/{slug}/printables.html
"""
import json, os, sys, re

BASE = os.environ.get("WP_SITE", os.path.dirname(os.path.abspath(__file__)))

BAND_MAP = {'a1':'a','a2':'a','b1':'b','b2':'b','c1':'c','c2':'c'}
WP_LOGO = ('<svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px">'
           '<rect width="32" height="32" rx="4" fill="currentColor"/>'
           '<text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" '
           'font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>')

def depth(level):
    return "../../../../"

def header(level, label):
    level_upper = level.upper()
    d = depth(level)
    return (f'<header class="site-header"><div class="site-header-inner">'
            f'<a href="../index.html" class="back back-link">{level_upper} Writing</a>'
            f'<a href="{d}index.html" class="brand">{WP_LOGO}Word Play</a>'
            f'<button class="dark-toggle" onclick="toggleDark()">&#9680; Dark</button>'
            f'</div></header>')

def breadcrumb(level, label, page):
    level_upper = level.upper()
    d = depth(level)
    return (f'<div class="breadcrumb"><a href="{d}index.html">Home</a><span>&#8250;</span>'
            f'<a href="../../index.html">{level_upper}</a><span>&#8250;</span>'
            f'<a href="../index.html">Writing</a><span>&#8250;</span>'
            f'<strong>{label} &#8212; {page}</strong></div>')

def chapter_nav(active):
    tabs = [("slides.html","Lesson"),("worksheet.html","Practice"),("game.html","Game"),("printables.html","Printables")]
    items = '\n    '.join(f'<a href="{h}" class="chapter-nav-btn{"  active" if h==active else ""}">{l}</a>' for h,l in tabs)
    return f'<nav class="chapter-nav">\n    {items}\n  </nav>'

def render_slide(s):
    h = ''
    if s.get("intro"): h += f'<p style="font-size:1.05rem;color:var(--ink);margin-bottom:14px">{s["intro"]}</p>'
    for r in s.get("rows", []):
        h += (f'<div class="overview-row"><div class="overview-label">{r[0]}</div>'
              f'<div class="overview-desc">{r[1]}</div></div>')
    if s.get("wo"): h += f'<div class="watch-out">{s["wo"]}</div>'
    return f'<div class="slide"><div class="slide-card"><div class="slide-header"><h2>{s["h2"]}</h2></div>{h}</div></div>'

def build_slides(ch):
    d = depth(ch["level"])
    slides_html = "\n".join(render_slide(s) for s in ch["slides"])
    n = len(ch["slides"])
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{d}favicon.svg" type="image/svg+xml">
<title>{ch["level"].upper()} Writing \xb7 {ch["label"]} \u2014 Lesson | Word Play</title>
<link rel="stylesheet" href="{d}shared/base.css">
<link rel="stylesheet" href="{d}shared/slides.css">
<script src="{d}shared/dark-init.js"></script>
</head><body>
<div class="deck-progress"><div class="deck-progress-fill" id="deck-progress-fill"></div></div>
{header(ch["level"], ch["label"])}
<div class="container">
  {breadcrumb(ch["level"], ch["label"], "Lesson")}
  <div class="chapter-num">Writing</div>
  <h1>{ch["label"]}</h1>
  <p class="chapter-subtitle">{ch["subtitle"]}</p>
  {chapter_nav("slides.html")}
  <div id="slide-deck">{slides_html}</div>
  <div class="deck-nav">
    <button class="deck-btn" onclick="prevSlide()" id="deck-prev" disabled>&#8592; Prev</button>
    <span class="deck-counter" id="slide-counter">1 / {n}</span>
    <button class="deck-btn primary" onclick="nextSlide()" id="deck-next">Next &#8594;</button>
  </div>
</div>
<footer class="site-footer">Word Play \xb7 Cambridge English A1\u2192C2</footer>
<script src="{d}shared/store.js"></script>
<script>window.LEVEL="{ch["level"]}";window.CHAPTER_ID="{ch["slug"]}";</script>
<script src="{d}shared/deck.js"></script>
</body></html>"""

def build_worksheet(ch):
    d = depth(ch["level"])
    prompt = ch.get("prompt", f"Write a {ch['label'].lower()} of 140\u2013190 words on the following task:")
    task = ch.get("task", "Your teacher wants you to write on this topic. Use ideas from the lesson.")
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{d}favicon.svg" type="image/svg+xml">
<title>{ch["level"].upper()} Writing \xb7 {ch["label"]} \u2014 Practice | Word Play</title>
<link rel="stylesheet" href="{d}shared/base.css">
<link rel="stylesheet" href="{d}shared/worksheet.css">
<script src="{d}shared/dark-init.js"></script>
</head><body>
{header(ch["level"], ch["label"])}
<div class="container">
  {breadcrumb(ch["level"], ch["label"], "Practice")}
  <div class="chapter-num">Writing</div>
  <h1>{ch["label"]}</h1>
  <p class="chapter-subtitle">{ch["subtitle"]}</p>
  {chapter_nav("worksheet.html")}
  <div style="background:var(--cream-deep);border:1px solid var(--hairline);border-radius:8px;padding:20px;margin-bottom:24px">
    <div style="font-family:var(--font-sans);font-size:.65rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">Writing Task</div>
    <p style="font-size:.95rem;color:var(--ink);margin-bottom:10px">{prompt}</p>
    <p style="font-size:.92rem;color:var(--ink);font-style:italic">{task}</p>
    <p style="font-family:var(--font-sans);font-size:.72rem;color:var(--muted);margin-top:10px">Write your answer in 140\u2013190 words.</p>
  </div>
  <form id="worksheet">
    <section class="exercise" id="ex1">
      <div class="ex-head">Your answer</div>
      <div class="q">
        <textarea data-q="writing1" data-answer-sample="(Model answer visible after submission)" 
          rows="12" style="width:100%;padding:12px;font-family:var(--font-serif);font-size:.95rem;border:1.5px solid var(--hairline);border-radius:4px;resize:vertical;background:var(--paper);color:var(--ink)"
          placeholder="Write your {ch['label'].lower()} here..."></textarea>
      </div>
    </section>
    <div class="submit-wrap">
      <button type="submit" class="submit-btn">Submit</button>
    </div>
  </form>
  <div id="results" class="results-panel">
    <div class="score-row"><span class="score-label">Submitted</span><span class="score-pct-badge" id="score-pct">✓</span></div>
    <div id="exercise-breakdown"></div>
    <div id="breakdown"></div>
    <button class="try-again-btn" onclick="tryAgain()">Edit</button>
  </div>
</div>
<footer class="site-footer">Word Play \xb7 Cambridge English A1\u2192C2</footer>
<script src="{d}shared/store.js"></script>
<script>
window.LEVEL="{ch["level"]}"; window.CHAPTER_ID="{ch["slug"]}";
window.TOTAL_POINTS=1;
window.ANSWERS={{"writing1":{{answer:"(see model)",accept:[]}}}};
window.EXERCISE_TITLES={{ex1:"{ch["label"]} — writing task"}};
</script>
<script src="{d}shared/worksheet.js"></script>
</body></html>"""

def build_game(ch):
    d = depth(ch["level"])
    items = json.dumps(ch.get("game_items", []), ensure_ascii=False, indent=2)
    n = len(ch.get("game_items", []))
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{d}favicon.svg" type="image/svg+xml">
<title>{ch["level"].upper()} Writing \xb7 {ch["label"]} \u2014 Game | Word Play</title>
<link rel="stylesheet" href="{d}shared/base.css">
<link rel="stylesheet" href="{d}shared/game.css">
<script src="{d}shared/dark-init.js"></script>
</head><body>
{header(ch["level"], ch["label"])}
<div class="container">
  {breadcrumb(ch["level"], ch["label"], "Game")}
  <div class="chapter-num">Writing</div>
  <h1>{ch["label"]}</h1>
  <p class="chapter-subtitle">{ch["subtitle"]}</p>
  {chapter_nav("game.html")}
  <div id="gameStart" class="game-screen active"><div class="game-start-card">
    <div class="game-start-title">{ch["label"]} \u2014 Key Phrases</div>
    <div class="game-start-meta"><span id="gStartMastered">0</span> / <span id="gStartTotal">{n}</span> mastered</div>
    <div id="gResumeSection" style="display:none" class="resume-section">
      <button id="gBtnResume" class="game-btn primary">Resume</button>
      <button id="gBtnNewFromResume" class="game-btn ghost">Start over</button>
    </div>
    <button id="gBtnStart" class="game-btn primary">Start</button>
  </div></div>
  <div id="gamePlay" class="game-screen"><div class="game-play-card">
    <div class="game-top-bar"><div class="game-progress-wrap"><div class="game-progress-bar" id="gProgressBar" style="width:0%"></div></div>
    <div class="game-top-stats"><span>Score <strong id="gScore">0</strong></span><span>Streak <strong id="gStreak">0</strong></span></div></div>
    <div id="gModeTag" class="game-mode-tag"></div>
    <div id="gTerm" class="game-term"></div><div id="gPrompt" class="game-prompt"></div>
    <div id="gOptions" class="game-options"></div><div id="gFeedback" class="game-feedback"></div>
    <div id="gExample" class="game-example" style="display:none"></div>
    <div class="game-btn-row">
      <button id="gBtnHint" class="game-btn ghost">Hint [H]</button>
      <button id="gBtnReveal" class="game-btn ghost">Reveal</button>
      <button id="gBtnNext" class="game-btn primary" style="display:none">Next &#8594;</button>
    </div>
    <div class="game-progress-txt" id="gProgressTxt">0 / {n} mastered</div>
    <button id="gBtnSaveQuit" class="game-btn ghost" style="margin-top:12px;width:100%">Save &amp; quit</button>
  </div>
  <div class="game-ref-panel"><button id="gRefToggle" class="game-ref-head">&#9660; Reference</button>
  <div id="gRefBody" class="game-ref-body"><div id="gRefList"></div></div></div></div>
  <div id="gameCompletion" class="game-screen"><div class="game-completion-card">
    <div class="completion-title">Complete!</div>
    <div class="completion-stats">
      <div>Score <strong id="gFinalScore">0</strong></div>
      <div>Best streak <strong id="gFinalStreak">0</strong></div>
      <div>Mastery <strong id="gFinalPct">0%</strong></div>
    </div>
    <button id="gBtnPlayAgain" class="game-btn primary">Play again</button>
  </div></div>
</div>
<div id="gToast" class="game-toast"></div>
<footer class="site-footer">Word Play \xb7 Cambridge English A1\u2192C2</footer>
<script src="{d}shared/store.js"></script>
<script>
window.LEVEL="{ch["level"]}"; window.CHAPTER_ID="{ch["slug"]}";
window.GAME_DATA={{chapterId:"{ch["slug"]}",level:"{ch["level"]}",title:"{ch["label"]}",
  storageKey:"wordplay_game_{ch["level"]}_{ch["slug"]}",items:{items}}};
</script>
<script src="{d}shared/game.js"></script>
</body></html>"""

def build_printable(ch):
    d = depth(ch["level"])
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="{d}favicon.svg" type="image/svg+xml">
<title>{ch["level"].upper()} Writing \xb7 {ch["label"]} \u2014 Printable | Word Play</title>
<link rel="stylesheet" href="{d}shared/base.css">
<script src="{d}shared/dark-init.js"></script>
<style>
@media print{{.site-header,.chapter-nav,.breadcrumb,.no-print{{display:none!important}}body{{background:white}}}}
.ps{{max-width:680px;margin:0 auto}}
.ps-title{{font-size:1.4rem;font-weight:700;font-family:Georgia,serif;margin-bottom:20px;padding-bottom:10px;border-bottom:2px solid var(--hairline)}}
.ps-sec{{margin-bottom:22px}}
.ps-sec h3{{font-family:var(--font-sans);font-size:.68rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);margin-bottom:10px}}
.ps-line{{border-bottom:1px solid var(--hairline);min-height:28px;margin-bottom:10px}}
.write-box{{border:1px solid var(--hairline);border-radius:4px;min-height:220px;padding:12px;margin-top:8px}}
</style>
</head><body>
{header(ch["level"], ch["label"])}
<div class="container">
  {breadcrumb(ch["level"], ch["label"], "Printable")}
  {chapter_nav("printables.html")}
  <div class="no-print" style="background:var(--cream-deep);border-radius:6px;padding:10px 14px;margin:16px 0;font-family:var(--font-sans);font-size:.78rem;color:var(--muted)">Press <strong>Ctrl+P</strong> to print.</div>
  <div class="ps">
    <div class="ps-title">{ch["label"]}</div>
    <div class="ps-sec"><h3>Writing task</h3>
      <div class="ps-line" style="min-height:50px"></div>
    </div>
    <div class="ps-sec"><h3>Planning (notes and key phrases)</h3>
      <div class="ps-line"></div><div class="ps-line"></div>
      <div class="ps-line"></div><div class="ps-line"></div>
    </div>
    <div class="ps-sec"><h3>Your answer (140\u2013190 words)</h3>
      <div class="write-box"></div>
    </div>
    <p style="font-family:var(--font-sans);font-size:.7rem;color:var(--muted);text-align:center;margin-top:24px;border-top:1px solid var(--hairline);padding-top:12px">Word Play \xb7 Cambridge English {ch["level"].upper()} \xb7 {ch["label"]}</p>
  </div>
</div>
<footer class="site-footer">Word Play \xb7 Cambridge English A1\u2192C2</footer>
</body></html>"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_writing.py content.json")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        chapters = json.load(f)
    if isinstance(chapters, dict):
        chapters = [chapters]
    for ch in chapters:
        level = ch["level"]
        band = BAND_MAP.get(level, "b")
        slug = ch["slug"]
        d = os.path.join(BASE, band, level, "writing", slug)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "slides.html"), "w") as f: f.write(build_slides(ch))
        with open(os.path.join(d, "worksheet.html"), "w") as f: f.write(build_worksheet(ch))
        with open(os.path.join(d, "game.html"), "w") as f: f.write(build_game(ch))
        with open(os.path.join(d, "printables.html"), "w") as f: f.write(build_printable(ch))
        print(f"Built: {level}/{slug} ({len(ch.get('slides',[])) } slides, {len(ch.get('game_items',[]))} game items)")
    print(f"Done — {len(chapters)} writing chapter(s) generated.")
