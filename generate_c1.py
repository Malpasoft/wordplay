"""Generate C1 grammar chapters from JSON content.
Usage:
  python3 generate_c1.py c1_content.json
  WP_SITE=/path/to/site python3 generate_c1.py c1_content.json

JSON shape is identical to a2_content_part*.json — see README.md.
"""
import json, os, sys

BASE = os.environ.get("WP_SITE", os.path.dirname(os.path.abspath(__file__)))
LEVEL = "c1"
BAND = "c"
SHARED = "../../../../shared/"

WP_LOGO = '<svg width="20" height="20" viewBox="0 0 32 32" style="vertical-align:middle;margin-right:8px"><rect width="32" height="32" rx="4" fill="currentColor"/><text x="16" y="22" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="15" fill="white" letter-spacing="-0.5">WP</text></svg>'

def header(slug):
    return f'''<header class="site-header">
  <div class="site-header-inner">
    <a href="../../index.html" class="back back-link">C1 Grammar</a>
    <a href="../../../../index.html" class="brand">{WP_LOGO}Word Play</a>
    <button class="dark-toggle" onclick="toggleDark()">&#9680; Dark</button>
  </div>
</header>'''

def breadcrumb(label, current):
    return f'''<div class="breadcrumb">
  <a href="../../../../index.html">Home</a><span>›</span>
  <a href="../../index.html">C1</a><span>›</span>
  <a href="../index.html">Grammar</a><span>›</span>
  <strong>{label} — {current}</strong>
</div>'''

def chapter_nav(active):
    tabs = [("slides.html","Lesson"),("worksheet.html","Practice"),("game.html","Game"),("printables.html","Printables")]
    items = [f'<a href="{h}" class="chapter-nav-btn{"  active" if h==active else ""}">{l}</a>' for h,l in tabs]
    return f'<nav class="chapter-nav">{"".join(items)}</nav>'

def render_slide(s):
    html = ""
    if s.get("intro"):
        html += f'<p style="font-size:1.05rem;color:var(--ink);margin-bottom:14px">{s["intro"]}</p>'
    for row in s.get("rows", []):
        html += f'<div class="overview-row"><div class="overview-label">{row[0]}</div><div class="overview-desc">{row[1]}</div></div>'
    if s.get("watch_out"):
        html += f'<div class="watch-out">{s["watch_out"]}</div>'
    if s.get("cta"):
        html += '<div class="deck-cta"><a href="worksheet.html" class="btn-cta">Practice now</a></div>'
    return f'''<div class="slide"><div class="slide-card">
  <div class="slide-header"><h2>{s["h2"]}</h2></div>
  {html}
</div></div>'''

def build_slides(ch):
    slides_html = "\n".join(render_slide(s) for s in ch["slides"])
    n = len(ch["slides"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>C1 · {ch["label"]} — Lesson | Word Play</title>
<link rel="stylesheet" href="{SHARED}base.css">
<link rel="stylesheet" href="{SHARED}slides.css">
<script src="{SHARED}dark-init.js"></script>
</head>
<body>
<div class="deck-progress"><div class="deck-progress-fill" id="deck-progress-fill"></div></div>
{header(ch["slug"])}
<div class="container">
  {breadcrumb(ch["label"], "Lesson")}
  <div class="chapter-num">Ch {ch["num"]}</div>
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
<footer class="site-footer">Word Play · Cambridge English A1&#8594;C2</footer>
<script src="{SHARED}store.js"></script>
<script>window.LEVEL="c1";window.CHAPTER_ID="{ch["slug"]}";</script>
<script src="{SHARED}deck.js"></script>
</body></html>'''

def build_worksheet(ch):
    ex1 = ch["worksheet"]["ex1"]
    ex2 = ch["worksheet"]["ex2"]
    mc = ""
    for i, q in enumerate(ex1["questions"], 1):
        opts = "".join(f'<button type="button" class="choice-btn" data-value="{o}">{o}</button>' for o in q["options"])
        mc += f'<div class="q"><span class="q-num">{i}</span><div class="q-text">{q["q"]}</div><div class="choice-group" data-q="e1q{i}" data-answer="{q["answer"]}">{opts}</div></div>\n'
    fi = ""
    ans_js = ""
    for i, q in enumerate(ex2["questions"], 1):
        fi += f'<div class="q"><span class="q-num">{i}</span><div class="q-text">{q["q"]}</div><input type="text" class="fill-in" data-q="e2q{i}" placeholder="Your answer..."></div>\n'
        acc = ", ".join(f'"{a}"' for a in q.get("accept", []))
        ans_js += f'  e2q{i}: {{answer: "{q["answer"]}", accept: [{acc}]}},\n'
    total = len(ex1["questions"]) + len(ex2["questions"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>C1 · {ch["label"]} — Practice | Word Play</title>
<link rel="stylesheet" href="{SHARED}base.css">
<link rel="stylesheet" href="{SHARED}worksheet.css">
<script src="{SHARED}dark-init.js"></script>
</head>
<body>
{header(ch["slug"])}
<div class="container">
  {breadcrumb(ch["label"], "Practice")}
  <div class="chapter-num">Ch {ch["num"]}</div>
  <h1>{ch["label"]}</h1>
  <p class="chapter-subtitle">{ch["subtitle"]}</p>
  {chapter_nav("worksheet.html")}
  <form id="worksheet">
    <section class="exercise" id="ex1">
      <div class="ex-head">Exercise 1</div>
      <div class="ex-title">{ex1["title"]}</div>
      <div class="ex-meta">{len(ex1["questions"])} points</div>
      {mc}
    </section>
    <section class="exercise" id="ex2">
      <div class="ex-head">Exercise 2</div>
      <div class="ex-title">{ex2["title"]}</div>
      <div class="ex-meta">{len(ex2["questions"])} points</div>
      {fi}
    </section>
    <div class="submit-wrap">
      <button type="submit" class="submit-btn">Check answers</button>
      <button type="button" class="reset-btn" onclick="resetAll()">Clear</button>
    </div>
  </form>
  <div id="results" class="results-panel">
    <div class="score-row"><span class="score-label">Score</span><span id="score-got">0</span><span class="score-sep">/</span><span id="score-total">0</span><span class="score-pct-badge" id="score-pct">0%</span></div>
    <div id="exercise-breakdown"></div>
    <div id="breakdown"></div>
    <button class="try-again-btn" onclick="tryAgain()">Try again</button>
  </div>
</div>
<footer class="site-footer">Word Play · Cambridge English A1&#8594;C2</footer>
<script src="{SHARED}store.js"></script>
<script>
window.LEVEL="c1"; window.CHAPTER_ID="{ch["slug"]}";
window.TOTAL_POINTS={total};
window.ANSWERS={{{ans_js}}};
window.EXERCISE_TITLES={{ex1:"{ex1["title"]}",ex2:"{ex2["title"]}"}};
</script>
<script src="{SHARED}worksheet.js"></script>
</body></html>'''

def build_game(ch):
    import json as _j
    items_js = _j.dumps(ch["game"], ensure_ascii=False, indent=4)
    n = len(ch["game"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>C1 · {ch["label"]} — Game | Word Play</title>
<link rel="stylesheet" href="{SHARED}base.css">
<link rel="stylesheet" href="{SHARED}game.css">
<script src="{SHARED}dark-init.js"></script>
</head>
<body>
{header(ch["slug"])}
<div class="container">
  {breadcrumb(ch["label"], "Game")}
  <div class="chapter-num">Ch {ch["num"]}</div>
  <h1>{ch["label"]}</h1>
  <p class="chapter-subtitle">{ch["subtitle"]}</p>
  {chapter_nav("game.html")}
  <div id="gameStart" class="game-screen active"><div class="game-start-card">
    <div class="game-start-title">{ch["label"]}</div>
    <div class="game-start-meta"><span id="gStartMastered">0</span> / <span id="gStartTotal">{n}</span> mastered &nbsp;&middot;&nbsp; Lifetime: <span id="gStartLifetime">&#8212;</span></div>
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
    <div id="gTerm" class="game-term"></div>
    <div id="gPrompt" class="game-prompt"></div>
    <div id="gOptions" class="game-options"></div>
    <div id="gFeedback" class="game-feedback"></div>
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
<footer class="site-footer">Word Play · Cambridge English A1&#8594;C2</footer>
<script src="{SHARED}store.js"></script>
<script>
window.LEVEL="c1"; window.CHAPTER_ID="{ch["slug"]}";
window.GAME_DATA={{chapterId:"{ch["slug"]}",level:"c1",title:"{ch["label"]}",storageKey:"wordplay_game_c1_{ch["slug"]}",items:{items_js}}};
</script>
<script src="{SHARED}game.js"></script>
</body></html>'''

def build_printable(ch):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="theme-color" content="#1A1A1A">
<link rel="icon" href="../../../../favicon.svg" type="image/svg+xml">
<title>C1 · {ch["label"]} — Printable | Word Play</title>
<link rel="stylesheet" href="{SHARED}base.css">
<script src="{SHARED}dark-init.js"></script>
<style>
@media print{{.site-header,.chapter-nav,.breadcrumb,.no-print{{display:none!important}}body{{background:white;color:black}}}}
.ps{{max-width:680px;margin:0 auto}}.ps-title{{font-size:1.4rem;font-weight:700;font-family:Georgia,serif;margin-bottom:20px;padding-bottom:10px;border-bottom:2px solid var(--hairline)}}
.ps-sec{{margin-bottom:22px}}.ps-sec h3{{font-family:var(--font-sans);font-size:.68rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);margin-bottom:10px}}
.ps-line{{border-bottom:1px solid var(--hairline);min-height:28px;margin-bottom:10px;padding-bottom:4px;font-size:.9rem}}
</style>
</head>
<body>
{header(ch["slug"])}
<div class="container">
  {breadcrumb(ch["label"], "Printable")}
  {chapter_nav("printables.html")}
  <div class="no-print" style="background:var(--cream-deep);border-radius:6px;padding:10px 14px;margin:16px 0;font-family:var(--font-sans);font-size:.78rem;color:var(--muted)">Press <strong>Ctrl+P</strong> to print.</div>
  <div class="ps">
    <div class="ps-title">{ch["label"]}</div>
    <div class="ps-sec"><h3>Exercise 1 — Write 4 sentences using {ch["label"]}</h3>
      <div class="ps-line"></div><div class="ps-line"></div><div class="ps-line"></div><div class="ps-line"></div>
    </div>
    <div class="ps-sec"><h3>Exercise 2 — Translation practice</h3>
      <div class="ps-line"></div><div class="ps-line"></div><div class="ps-line"></div><div class="ps-line"></div>
    </div>
    <div class="ps-sec"><h3>Exercise 3 — Notes from the lesson</h3>
      <div class="ps-line"></div><div class="ps-line"></div><div class="ps-line"></div><div class="ps-line"></div><div class="ps-line"></div>
    </div>
    <p style="font-family:var(--font-sans);font-size:.7rem;color:var(--muted);text-align:center;margin-top:24px;border-top:1px solid var(--hairline);padding-top:12px">Word Play · Cambridge English C1 · {ch["label"]}</p>
  </div>
</div>
<footer class="site-footer">Word Play · Cambridge English A1&#8594;C2</footer>
</body></html>'''

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_c1.py content.json")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        chapters = json.load(f)
    if isinstance(chapters, dict):
        chapters = [chapters]
    for ch in chapters:
        d = os.path.join(BASE, BAND, LEVEL, "grammar", ch["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "slides.html"), "w") as f: f.write(build_slides(ch))
        with open(os.path.join(d, "worksheet.html"), "w") as f: f.write(build_worksheet(ch))
        with open(os.path.join(d, "game.html"), "w") as f: f.write(build_game(ch))
        with open(os.path.join(d, "printables.html"), "w") as f: f.write(build_printable(ch))
        print(f"Built: {ch['slug']} ({len(ch['slides'])} slides, {len(ch['worksheet']['ex1']['questions'])+len(ch['worksheet']['ex2']['questions'])} worksheet Qs, {len(ch['game'])} game items)")
    print(f"Done — {len(chapters)} chapter(s) generated.")
