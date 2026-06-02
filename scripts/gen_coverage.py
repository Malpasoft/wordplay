#!/usr/bin/env python3
"""
Generate coverage.html — a teacher-facing content status report.
Shows which chapters are complete, stub, or missing across both
English and Spanish tracks.

Run from repo root:
    python3 scripts/gen_coverage.py
"""
import json, os, re, glob
from datetime import date

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEARCH_INDEX = os.path.join(BASE, 'shared', 'search-index.json')
OUT = os.path.join(BASE, 'coverage.html')

PLACEHOLDER_RE = re.compile(r'<!--[^>]*PLACEHOLDER[^>]*-->|<!--[^>]*stub[^>]*-->', re.IGNORECASE)
WORDS_RE = re.compile(r'(?:const|var)\s+WORDS\s*=\s*\[')
WORDS_CONTENT_RE = re.compile(r'(?:const|var)\s+WORDS\s*=\s*\[(.*?)\];', re.DOTALL)
SLIDE_RE = re.compile(r'class=["\']slide["\']')


def rel(path):
    return path.replace(BASE + '/', '')


def count_words(content):
    m = WORDS_CONTENT_RE.search(content)
    if not m:
        return 0
    return len(re.findall(r'"word"\s*:', m.group(1)))


def assess_file(path):
    """Return 'complete' | 'stub' | 'missing'."""
    if not path or not os.path.exists(path):
        return 'missing'
    content = open(path, encoding='utf-8').read()
    if PLACEHOLDER_RE.search(content):
        return 'stub'
    return 'complete'


def assess_flashcards(path):
    if not path or not os.path.exists(path):
        return 'missing'
    content = open(path, encoding='utf-8').read()
    if PLACEHOLDER_RE.search(content):
        return 'stub'
    if not WORDS_RE.search(content):
        return 'stub'
    if count_words(content) < 5:
        return 'stub'
    return 'complete'


def assess_slides(path):
    if not path or not os.path.exists(path):
        return 'missing'
    content = open(path, encoding='utf-8').read()
    if PLACEHOLDER_RE.search(content):
        return 'stub'
    slide_count = len(SLIDE_RE.findall(content))
    if slide_count < 2:
        return 'stub'
    return 'complete'


def worst(statuses):
    if 'missing' in statuses:
        return 'missing'
    if 'stub' in statuses:
        return 'stub'
    return 'complete'


def scan_english():
    """Scan a/ b/ c/ tracks. Returns list of chapter dicts."""
    chapters = []
    for level_dir in ['a/a1','a/a2','b/b1','b/b2','c/c1','c/c2']:
        level_code = level_dir.split('/')[-1].upper()
        for section_dir in ['grammar','vocabulary','writing']:
            section_path = os.path.join(BASE, level_dir, section_dir)
            if not os.path.isdir(section_path):
                continue
            for chapter_dir in sorted(os.listdir(section_path)):
                chapter_path = os.path.join(section_path, chapter_dir)
                if not os.path.isdir(chapter_path):
                    continue
                index_path = os.path.join(chapter_path, 'index.html')
                if not os.path.exists(index_path):
                    continue

                # Get title from index
                idx_content = open(index_path, encoding='utf-8').read()
                title_m = re.search(r'<h1[^>]*>(.*?)</h1>', idx_content, re.DOTALL)
                title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else chapter_dir

                slides = os.path.join(chapter_path, 'slides.html')
                worksheet = os.path.join(chapter_path, 'worksheet.html')
                game = os.path.join(chapter_path, 'game.html')
                flashcards = os.path.join(chapter_path, 'flashcards.html')

                slides_status = assess_slides(slides)

                if section_dir == 'vocabulary':
                    fc_status = assess_flashcards(flashcards)
                    game_status = assess_file(game)
                    overall = worst([slides_status, fc_status])
                    details = {'slides': slides_status, 'flashcards': fc_status, 'game': game_status}
                elif section_dir == 'writing':
                    ws_status = assess_file(worksheet)
                    overall = worst([slides_status, ws_status])
                    details = {'slides': slides_status, 'worksheet': ws_status}
                else:  # grammar
                    ws_status = assess_file(worksheet)
                    game_status = assess_file(game)
                    overall = worst([slides_status, ws_status])
                    details = {'slides': slides_status, 'worksheet': ws_status, 'game': game_status}

                url = f'/{level_dir}/{section_dir}/{chapter_dir}/index.html'
                chapters.append({
                    'track': 'en',
                    'level': level_code,
                    'section': section_dir,
                    'title': title,
                    'url': url,
                    'status': overall,
                    'details': details,
                })
    return chapters


def scan_spanish():
    """Scan es/ track. Returns list of chapter dicts."""
    # Section name mapping: filesystem dir → display name
    SECTION_MAP = {
        'gramatica': 'grammar',
        'vocabulary': 'vocabulary',
        'writing': 'writing',
    }
    chapters = []
    for level_code in ['A1','A2','B1','B2','C1','C2']:
        level_dir = os.path.join(BASE, 'es', level_code.lower())
        for section_dir in sorted(os.listdir(level_dir)) if os.path.isdir(level_dir) else []:
            section_path = os.path.join(level_dir, section_dir)
            if not os.path.isdir(section_path):
                continue
            # Map ES section dirs to canonical section names
            section_key = section_dir.lower()
            if section_key in ('gramatica', 'gramática'):
                section_canonical = 'grammar'
            elif section_key in ('vocabulary', 'vocabulario'):
                section_canonical = 'vocabulary'
            elif section_key in ('writing', 'escritura'):
                section_canonical = 'writing'
            else:
                continue

            for chapter_dir in sorted(os.listdir(section_path)):
                chapter_path = os.path.join(section_path, chapter_dir)
                if not os.path.isdir(chapter_path):
                    continue
                index_path = os.path.join(chapter_path, 'index.html')
                if not os.path.exists(index_path):
                    continue

                idx_content = open(index_path, encoding='utf-8').read()
                title_m = re.search(r'<h1[^>]*>(.*?)</h1>', idx_content, re.DOTALL)
                title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else chapter_dir

                slides = os.path.join(chapter_path, 'slides.html')
                worksheet = os.path.join(chapter_path, 'worksheet.html')
                game = os.path.join(chapter_path, 'game.html')
                flashcards = os.path.join(chapter_path, 'flashcards.html')

                slides_status = assess_slides(slides)

                if section_canonical == 'vocabulary':
                    fc_status = assess_flashcards(flashcards)
                    game_status = assess_file(game)
                    overall = worst([slides_status, fc_status])
                    details = {'slides': slides_status, 'flashcards': fc_status, 'game': game_status}
                elif section_canonical == 'writing':
                    ws_status = assess_file(worksheet)
                    overall = worst([slides_status, ws_status])
                    details = {'slides': slides_status, 'worksheet': ws_status}
                else:
                    ws_status = assess_file(worksheet)
                    game_status = assess_file(game)
                    overall = worst([slides_status, ws_status])
                    details = {'slides': slides_status, 'worksheet': ws_status, 'game': game_status}

                url = f'/es/{level_code.lower()}/{section_dir}/{chapter_dir}/index.html'
                chapters.append({
                    'track': 'es',
                    'level': level_code,
                    'section': section_canonical,
                    'section_dir': section_dir,
                    'title': title,
                    'url': url,
                    'status': overall,
                    'details': details,
                })
    return chapters


def build_summary(chapters):
    summary = {}
    for c in chapters:
        key = (c['track'], c['level'], c['section'])
        if key not in summary:
            summary[key] = {'complete': 0, 'stub': 0, 'missing': 0, 'total': 0}
        summary[key][c['status']] += 1
        summary[key]['total'] += 1
    return summary


HTML_TEMPLATE = '''\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<title>Content Coverage | Word Play</title>
<link rel="stylesheet" href="shared/base.css?v=v123">
<script src="shared/dark-init.js?v=v109"></script>
<style>
.cov-wrap{max-width:1100px;margin:0 auto;padding:24px 16px}
h1{font-size:1.6rem;color:var(--navy);margin:0 0 4px}
.cov-meta{font-family:var(--font-sans);font-size:.78rem;color:var(--muted);margin-bottom:24px}
.track-tabs{display:flex;gap:8px;margin-bottom:24px}
.track-tab{font-family:var(--font-sans);font-size:.72rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:8px 20px;border-radius:4px;border:1.5px solid var(--hairline);background:transparent;color:var(--ink);cursor:pointer;transition:all .15s}
.track-tab.active{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.track-panel{display:none}.track-panel.active{display:block}
.level-block{margin-bottom:32px}
.level-head{display:flex;align-items:center;gap:12px;margin-bottom:12px;cursor:pointer;user-select:none}
.level-badge{font-family:var(--font-sans);font-size:.65rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);border:1.5px solid var(--amber);border-radius:3px;padding:2px 8px}
.level-title{font-size:1.1rem;font-weight:700;color:var(--navy)}
.level-stats{font-family:var(--font-sans);font-size:.75rem;color:var(--muted);margin-left:auto}
.level-toggle{font-family:var(--font-sans);font-size:.72rem;color:var(--muted);margin-left:8px}
.level-body{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:10px}
.level-body.collapsed{display:none}
.section-group{margin-bottom:8px}
.section-label{font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--muted);margin-bottom:6px;padding:0 2px}
.ch-card{display:flex;align-items:center;gap:10px;padding:8px 12px;border-radius:6px;border:1px solid var(--hairline);background:var(--paper);text-decoration:none;transition:border-color .15s;font-size:.85rem;color:var(--ink)}
.ch-card:hover{border-color:var(--ink)}
.ch-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
.dot-complete{background:#27ae60}
.dot-stub{background:var(--amber)}
.dot-missing{background:#c0392b}
.ch-title{flex:1;font-weight:600}
.ch-detail{font-family:var(--font-sans);font-size:.62rem;color:var(--muted);margin-left:auto;white-space:nowrap}
.legend{display:flex;gap:16px;margin-bottom:20px;font-family:var(--font-sans);font-size:.72rem;color:var(--muted)}
.legend-item{display:flex;align-items:center;gap:6px}
.legend-dot{width:9px;height:9px;border-radius:50%}
.summary-bar{display:flex;align-items:center;gap:8px;margin-bottom:20px;font-family:var(--font-sans);font-size:.82rem}
.bar-wrap{flex:1;height:8px;background:var(--hairline);border-radius:4px;overflow:hidden;display:flex}
.bar-seg{height:100%;transition:width .3s}
.bar-complete{background:#27ae60}
.bar-stub{background:var(--amber)}
.bar-missing{background:#c0392b}
.filter-row{display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap}
.filter-btn{font-family:var(--font-sans);font-size:.66rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:5px 12px;border-radius:3px;border:1.5px solid var(--hairline);background:transparent;color:var(--muted);cursor:pointer}
.filter-btn.active{border-color:var(--ink);color:var(--ink);background:transparent}
.no-match{padding:24px;text-align:center;color:var(--muted);font-family:var(--font-sans);font-size:.82rem}
@media(prefers-color-scheme:dark){
  .ch-card{background:var(--paper)}
}
</style>
</head>
<body>
<header class="site-header"><div class="site-header-inner">
  <a href="index.html" class="back back-link" aria-label="Back"></a>
  <a href="index.html" class="brand">Word Play</a>
  <button class="dark-toggle" onclick="toggleDark()">&#9680; Dark</button>
</div></header>
<div class="cov-wrap">
  <h1>Content Coverage</h1>
  <p class="cov-meta">Generated __DATE__ &mdash; __TOTAL__ chapters across both tracks</p>

  <div class="legend">
    <div class="legend-item"><div class="legend-dot dot-complete"></div>Complete</div>
    <div class="legend-item"><div class="legend-dot dot-stub"></div>Stub / needs content</div>
    <div class="legend-item"><div class="legend-dot dot-missing"></div>Missing files</div>
  </div>

  <div class="track-tabs">
    <button class="track-tab active" onclick="switchTrack('en',this)">English (A&ndash;C)</button>
    <button class="track-tab" onclick="switchTrack('es',this)">Spanish (ES)</button>
  </div>

  <div id="track-en" class="track-panel active"></div>
  <div id="track-es" class="track-panel"></div>
</div>

<footer class="site-footer">Word Play &middot; Cambridge English A1&rarr;C2</footer>

<script>
var CHAPTERS = __CHAPTERS_JSON__;

function switchTrack(track, btn) {
  document.querySelectorAll('.track-tab').forEach(function(b){b.classList.remove('active')});
  btn.classList.add('active');
  document.querySelectorAll('.track-panel').forEach(function(p){p.classList.remove('active')});
  document.getElementById('track-'+track).classList.add('active');
}

function dotClass(status) {
  return 'ch-dot dot-' + status;
}

function detailStr(details) {
  var parts = [];
  Object.keys(details).forEach(function(k) {
    if (details[k] !== 'complete') parts.push(k + ':' + details[k]);
  });
  return parts.join(' ');
}

function buildLevelBlock(track, level, chapters) {
  var sectionOrder = ['grammar','vocabulary','writing'];
  var sectionLabels = {grammar:'Grammar',vocabulary:'Vocabulary',writing:'Writing'};
  var complete = chapters.filter(function(c){return c.status==='complete'}).length;
  var stub = chapters.filter(function(c){return c.status==='stub'}).length;
  var missing = chapters.filter(function(c){return c.status==='missing'}).length;
  var total = chapters.length;
  var pct = Math.round(complete/total*100);

  var html = '<div class="level-block" data-level="'+level+'" data-track="'+track+'">';
  html += '<div class="level-head" onclick="toggleLevel(this)">';
  html += '<span class="level-badge">'+level+'</span>';
  html += '<span class="level-title">'+levelName(level)+'</span>';
  html += '<span class="level-stats">'+complete+'/'+total+' complete ('+pct+'%)</span>';
  html += '<span class="level-toggle">&#9660;</span>';
  html += '</div>';

  html += '<div style="display:flex;align-items:center;gap:8px;margin-bottom:12px;font-family:var(--font-sans);font-size:.72rem;color:var(--muted)">';
  html += '<div style="flex:1;height:6px;background:var(--hairline);border-radius:3px;overflow:hidden;display:flex">';
  html += '<div class="bar-seg bar-complete" style="width:'+Math.round(complete/total*100)+'%"></div>';
  html += '<div class="bar-seg bar-stub" style="width:'+Math.round(stub/total*100)+'%"></div>';
  html += '<div class="bar-seg bar-missing" style="width:'+Math.round(missing/total*100)+'%"></div>';
  html += '</div>';
  if (stub > 0) html += '<span style="color:var(--amber)">'+stub+' stub</span>';
  if (missing > 0) html += '<span style="color:#c0392b">'+missing+' missing</span>';
  html += '</div>';

  html += '<div class="level-body">';
  sectionOrder.forEach(function(sec) {
    var secChapters = chapters.filter(function(c){return c.section===sec});
    if (!secChapters.length) return;
    html += '<div class="section-group">';
    html += '<div class="section-label">'+sectionLabels[sec]+'</div>';
    secChapters.forEach(function(c) {
      var detail = detailStr(c.details);
      html += '<a class="ch-card" href="'+c.url+'" data-status="'+c.status+'">';
      html += '<div class="'+dotClass(c.status)+'"></div>';
      html += '<span class="ch-title">'+c.title+'</span>';
      if (detail) html += '<span class="ch-detail">'+detail+'</span>';
      html += '</a>';
    });
    html += '</div>';
  });
  html += '</div></div>';
  return html;
}

function levelName(code) {
  var names = {A1:'Beginner',A2:'Elementary',B1:'Intermediate',B2:'Upper Intermediate',C1:'Advanced',C2:'Proficiency'};
  return names[code] || code;
}

function toggleLevel(head) {
  var body = head.parentElement.querySelector('.level-body');
  var toggle = head.querySelector('.level-toggle');
  if (body.classList.contains('collapsed')) {
    body.classList.remove('collapsed');
    toggle.innerHTML = '&#9660;';
  } else {
    body.classList.add('collapsed');
    toggle.innerHTML = '&#9658;';
  }
}

function render() {
  ['en','es'].forEach(function(track) {
    var panel = document.getElementById('track-'+track);
    var levels = ['A1','A2','B1','B2','C1','C2'];
    var html = '';
    levels.forEach(function(level) {
      var chaps = CHAPTERS.filter(function(c){return c.track===track && c.level===level});
      if (!chaps.length) return;
      html += buildLevelBlock(track, level, chaps);
    });
    panel.innerHTML = html;
  });
}

render();
</script>
</body>
</html>
'''


def main():
    print('Scanning English track...')
    en_chapters = scan_english()
    print(f'  Found {len(en_chapters)} EN chapters')

    print('Scanning Spanish track...')
    es_chapters = scan_spanish()
    print(f'  Found {len(es_chapters)} ES chapters')

    chapters = en_chapters + es_chapters
    total = len(chapters)

    complete = sum(1 for c in chapters if c['status'] == 'complete')
    stub = sum(1 for c in chapters if c['status'] == 'stub')
    missing = sum(1 for c in chapters if c['status'] == 'missing')

    print(f'\nTotal: {total} | Complete: {complete} | Stub: {stub} | Missing: {missing}')

    # Simplify chapters for JSON (remove section_dir if present)
    for c in chapters:
        c.pop('section_dir', None)

    chapters_json = json.dumps(chapters, ensure_ascii=False)
    html = HTML_TEMPLATE.replace('__CHAPTERS_JSON__', chapters_json)
    html = html.replace('__DATE__', str(date.today()))
    html = html.replace('__TOTAL__', str(total))

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Wrote: {rel(OUT)}')

    # Also write shared/coverage-data.json for profile.html to consume
    json_out = os.path.join(BASE, 'shared', 'coverage-data.json')
    with open(json_out, 'w', encoding='utf-8') as f:
        json.dump({'date': str(date.today()), 'chapters': chapters}, f, ensure_ascii=False)
    print(f'Wrote: {rel(json_out)}')


if __name__ == '__main__':
    main()
