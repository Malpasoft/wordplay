// ══════════════════════════════════════════════════════════════════
// WORKSHEET — shared grading logic (v49: per-exercise check buttons)
// ══════════════════════════════════════════════════════════════════
// Each worksheet page must define (before this script):
//   window.TOTAL_POINTS   — integer, total possible score
//   window.ANSWERS        — object keyed by data-q, with { answer, accept? }
//   window.CHAPTER_ID     — string key e.g. 'ch10'  (for progress saving)
//   window.EXERCISE_TITLES (optional) — { ex1: 'Label', ... }

// ── Choice button handling ────────────────────────────────────────
document.querySelectorAll('.choice-group').forEach(group => {
  group.querySelectorAll('.choice-btn').forEach(btn => {
    btn.type = 'button'; // prevent accidental form submission
    btn.addEventListener('click', () => {
      if (group.classList.contains('ex-submitted')) return;
      group.querySelectorAll('.choice-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      checkExerciseComplete(group.closest('section.exercise'));
    });
  });
});

// Auto-enable Check button when all questions in an exercise are answered
function checkExerciseComplete(section) {
  if (!section) return;
  var allAnswered = true;
  section.querySelectorAll('.choice-group').forEach(g => {
    if (!g.querySelector('.choice-btn.selected')) allAnswered = false;
  });
  section.querySelectorAll('input[type="text"]').forEach(inp => {
    if (!inp.value.trim()) allAnswered = false;
  });
  var checkBtn = section.querySelector('.ex-check-btn');
  if (checkBtn) checkBtn.disabled = !allAnswered;
}

// Auto-check: when filling a text input, re-evaluate completion
document.querySelectorAll('input[type="text"]').forEach(inp => {
  inp.addEventListener('input', () => {
    checkExerciseComplete(inp.closest('section.exercise'));
  });
});

// ── Normalise strings for fuzzy matching ─────────────────────────
function norm(s) {
  return (s || '').toLowerCase().trim()
    .replace(/[.!?,;:]$/g, '')
    .replace(/\s+/g, ' ')
    .replace(/[\u2018\u2019`]/g, "'")
    .replace(/[\u201C\u201D]/g, '"');
}

function isTextCorrect(q, userValue) {
  const key = window.ANSWERS[q];
  if (!key) return false;
  const u = norm(userValue);
  if (!u) return false;
  if (u === norm(key.answer)) return true;
  return (key.accept || []).some(alt => u === norm(alt));
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c])
  );
}

// ── Grade a single exercise section ──────────────────────────────
function gradeSection(section) {
  var score = 0;
  var items = [];

  section.querySelectorAll('.choice-group').forEach(group => {
    var q = group.dataset.q;
    var ans = group.dataset.answer;
    var selected = group.querySelector('.choice-btn.selected');
    var user = selected ? selected.dataset.value : null;
    var correct = user === ans;
    if (correct) score++;
    group.classList.add('ex-submitted');
    group.querySelectorAll('.choice-btn').forEach(b => {
      b.disabled = true;
      if (b.dataset.value === ans) b.classList.add('correct-answer');
      else if (b === selected && !correct) b.classList.add('wrong-answer');
    });
    var qEl = group.closest('.q');
    qEl.classList.add(correct ? 'correct' : 'wrong');
    var fb = qEl.querySelector('.ws-feedback') || document.createElement('div');
    fb.className = 'ws-feedback';
    var explHtml = '';
    if (!correct && window.EXPLANATIONS && window.EXPLANATIONS[q]) {
      explHtml = '<div style="margin-top:6px;padding:7px 11px;background:rgba(184,134,11,.08);border-left:3px solid var(--amber);font-family:var(--font-sans);font-size:.76rem;color:var(--ink);line-height:1.5;border-radius:0 3px 3px 0">&#9432; ' + window.EXPLANATIONS[q] + '</div>';
    }
    fb.innerHTML = correct
      ? '<span style="color:var(--green);font-family:var(--font-sans);font-size:.82rem;font-weight:600">&#10003; Correct</span>'
      : '<span style="color:var(--red);font-family:var(--font-sans);font-size:.82rem">Correct answer: <strong>' + escapeHtml(ans) + '</strong></span>' + explHtml;
    qEl.appendChild(fb);
    items.push({ q, user, ans, correct });
  });

  section.querySelectorAll('input[type="text"]').forEach(inp => {
    var q = inp.dataset.q;
    var user = inp.value;
    var correct = isTextCorrect(q, user);
    if (correct) score++;
    inp.disabled = true;
    var qEl = inp.closest('.q');
    if (qEl && !qEl.classList.contains('correct') && !qEl.classList.contains('wrong')) {
      qEl.classList.add(correct ? 'correct' : 'wrong');
    }
    var correctAns = window.ANSWERS[q]?.answer || '';
    var fb = qEl ? (qEl.querySelector('.ws-feedback') || document.createElement('div')) : null;
    if (fb) {
      fb.className = 'ws-feedback';
      fb.innerHTML = correct
        ? '<span style="color:var(--green);font-family:var(--font-sans);font-size:.82rem;font-weight:600">Correct</span>'
        : '<span style="color:var(--red);font-family:var(--font-sans);font-size:.82rem">Correct answer: <strong>' + escapeHtml(correctAns) + '</strong></span>';
      qEl.appendChild(fb);
    }
    items.push({ q, user: user || '(blank)', ans: correctAns, correct });
  });

  section.querySelectorAll('select').forEach(sel => {
    var q = sel.dataset.q;
    var user = sel.value;
    var ans = sel.dataset.answer;
    var correct = user === ans;
    if (correct) score++;
    sel.disabled = true;
    var qEl = sel.closest('.q');
    if (qEl && !qEl.classList.contains('correct') && !qEl.classList.contains('wrong')) {
      qEl.classList.add(correct ? 'correct' : 'wrong');
    }
    items.push({ q, user: user || '—', ans, correct });
  });

  section.querySelectorAll('textarea').forEach(ta => {
    var q = ta.dataset.q;
    var user = ta.value.trim();
    var written = user.length > 5;
    if (written) score++;
    ta.disabled = true;
    var qEl = ta.closest('.q');
    if (qEl) qEl.classList.add('info');
    items.push({ q, user: user || '(blank)', ans: ta.dataset.answerSample, correct: written, isOpen: true });
  });

  return { score, total: items.length, items };
}

// ── Per-exercise Check button handler ────────────────────────────
function checkExercise(sectionId) {
  var section = document.getElementById(sectionId);
  if (!section || section.classList.contains('graded')) return;

  var result = gradeSection(section);
  section.classList.add('graded');

  var checkBtn = section.querySelector('.ex-check-btn');
  if (checkBtn) checkBtn.style.display = 'none';

  // Show mini score inside the exercise
  var pct = result.total ? Math.round((result.score / result.total) * 100) : 0;
  var color = pct >= 80 ? 'var(--green)' : pct >= 50 ? 'var(--amber)' : 'var(--red)';
  var miniScore = document.createElement('div');
  miniScore.className = 'ex-mini-score';
  miniScore.style.cssText = 'font-family:var(--font-sans);font-size:.82rem;font-weight:700;padding:8px 14px;border-radius:4px;background:var(--cream-deep);border:1px solid var(--hairline);margin-top:12px;display:flex;align-items:center;gap:10px';
  miniScore.innerHTML = '<span style="color:var(--muted)">Exercise score:</span> <span style="color:' + color + '">' + result.score + ' / ' + result.total + ' (' + pct + '%)</span>';
  section.appendChild(miniScore);

  updateFinalSubmitState();
}

function updateFinalSubmitState() {
  var allSections = document.querySelectorAll('section.exercise');
  var allGraded = Array.from(allSections).every(s => s.classList.contains('graded'));
  var submitWrap = document.querySelector('.submit-wrap');
  if (submitWrap) {
    submitWrap.style.display = allGraded ? 'flex' : 'none';
  }
}

// ── Main grading function (full submit) ───────────────────────────
function checkAnswers() {
  if (document.body.classList.contains('submitted')) return;
  let score = 0;
  const breakdown = [];
  const titles = window.EXERCISE_TITLES || {};
  var perExercise = {};

  document.querySelectorAll('section.exercise').forEach(section => {
    const id = section.id;
    const title = titles[id] || section.querySelector('.ex-title')?.textContent || id;
    var result;
    if (!section.classList.contains('graded')) {
      result = gradeSection(section);
      section.classList.add('graded');
      var checkBtn = section.querySelector('.ex-check-btn');
      if (checkBtn) checkBtn.style.display = 'none';
    } else {
      // Already graded — recount from DOM
      var correct = section.querySelectorAll('.q.correct').length;
      var total = section.querySelectorAll('.q').length;
      result = { score: correct, total, items: [] };
    }
    score += result.score;
    perExercise[id] = { correct: result.score, total: result.total };
    if (result.items.length) breakdown.push({ title, items: result.items });
  });

  // Render breakdown
  const breakdownEl = document.getElementById('breakdown');
  if (breakdownEl) {
    breakdownEl.innerHTML = '<h3>Review your answers</h3>' + breakdown.map(section => {
      const itemsHtml = section.items.map(item => {
        const cls = item.isOpen ? 'info' : (item.correct ? 'correct' : 'wrong');
        const mark = item.isOpen ? '~' : (item.correct ? '✓' : '✕');
        var qLabel = item.q.replace(/^e\d+q(\d+)$/i, 'Q$1').toUpperCase();
        let content = '<div class="content"><strong>' + qLabel + '</strong>';
        if (item.isOpen) {
          content += '<span class="your-ans">You wrote: ' + escapeHtml(item.user) + '</span>';
          content += '<span class="correct-ans">Sample: ' + escapeHtml(item.ans) + '</span>';
        } else if (!item.correct) {
          content += '<span class="your-ans">You wrote: ' + escapeHtml(item.user) + '</span>';
          content += '<span class="correct-ans">Answer: ' + escapeHtml(item.ans) + '</span>';
        }
        content += '</div>';
        return '<div class="breakdown-item ' + cls + '"><span class="mark">' + mark + '</span>' + content + '</div>';
      }).join('');
      return '<div class="breakdown-ex"><h4>' + section.title + '</h4>' + itemsHtml + '</div>';
    }).join('');
  }

  const total = window.TOTAL_POINTS;
  document.getElementById('score-got').textContent = score;
  document.getElementById('score-total').textContent = total;
  document.getElementById('score-pct').textContent = Math.round((score / total) * 100) + '%';

  var exBreakdown = document.getElementById('exercise-breakdown');
  if (exBreakdown) {
    var titleMap = window.EXERCISE_TITLES || {};
    var html = '';
    Object.keys(perExercise).forEach(function(exId) {
      var d = perExercise[exId];
      var exPct = d.total ? Math.round((d.correct / d.total) * 100) : 0;
      var color = exPct >= 80 ? 'var(--amber)' : exPct >= 50 ? 'var(--ink)' : 'var(--muted)';
      var label = titleMap[exId] || exId;
      html += '<div class="ex-row" style="display:flex;align-items:center;gap:12px;padding:8px 0;border-bottom:1px solid var(--hairline);font-family:var(--font-sans);font-size:.82rem">';
      html += '<span style="flex:1;color:var(--ink)">' + label + '</span>';
      html += '<span style="color:var(--muted);font-size:.78rem">' + d.correct + '/' + d.total + '</span>';
      html += '<div style="width:80px;height:6px;background:var(--hairline);border-radius:3px;overflow:hidden">';
      html += '<div style="width:' + exPct + '%;height:100%;background:' + color + '"></div></div>';
      html += '<span style="font-weight:700;color:' + color + ';min-width:36px;text-align:right">' + exPct + '%</span>';
      html += '</div>';
    });
    exBreakdown.innerHTML = html;
  }

  if (window.FCEStore && window.CHAPTER_ID) {
    FCEStore.saveResult(window.CHAPTER_ID, score, total, perExercise);
  }

  // Populate pass-msg
  var pm = document.getElementById('pass-msg');
  if (pm) {
    var pct2 = Math.round((score / total) * 100);
    if (pct2 === 100) pm.textContent = 'Perfect score!';
    else if (pct2 >= 80) pm.textContent = 'Great work — nearly perfect!';
    else if (pct2 >= 70) pm.textContent = 'Good job — try again for a higher score.';
    else pm.textContent = 'Keep practising — review the lesson and try again.';
    pm.style.display = 'block';
  }
  document.body.classList.add('submitted');
  document.getElementById('results').classList.add('show');
  document.querySelector('.submit-wrap').style.display = 'none';
  document.getElementById('results').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ── Reset ────────────────────────────────────────────────────────
function resetAll() {
  if (!confirm('Clear all your answers?')) return;
  document.querySelectorAll('input[type="text"], textarea').forEach(i => i.value = '');
  document.querySelectorAll('select').forEach(s => s.value = '');
  document.querySelectorAll('.choice-btn').forEach(b => b.classList.remove('selected'));
  document.querySelectorAll('.ws-feedback').forEach(fb => fb.remove());
  document.querySelectorAll('.ex-mini-score').forEach(ms => ms.remove());
  document.querySelectorAll('section.exercise').forEach(s => {
    s.classList.remove('graded');
    var btn = s.querySelector('.ex-check-btn');
    if (btn) { btn.style.display = ''; btn.disabled = true; }
  });
  updateFinalSubmitState();
}

function tryAgain() {
  document.body.classList.remove('submitted');
  document.getElementById('results').classList.remove('show');
  document.querySelectorAll('input[type="text"], textarea, select').forEach(el => {
    el.disabled = false; el.value = '';
  });
  document.querySelectorAll('.choice-btn').forEach(b => {
    b.disabled = false;
    b.classList.remove('selected', 'correct-answer', 'wrong-answer');
  });
  document.querySelectorAll('.q').forEach(q => q.classList.remove('correct', 'wrong', 'info'));
  document.querySelectorAll('.ws-feedback').forEach(fb => fb.remove());
  document.querySelectorAll('.ex-mini-score').forEach(ms => ms.remove());
  document.querySelectorAll('section.exercise').forEach(s => {
    s.classList.remove('graded');
    var btn = s.querySelector('.ex-check-btn');
    if (btn) { btn.style.display = ''; btn.disabled = true; }
  });
  updateFinalSubmitState();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

document.getElementById('worksheet').addEventListener('submit', e => {
  e.preventDefault();
  checkAnswers();
});

// ── Inject per-exercise Check buttons and hide final Submit initially ──
(function() {
  var sections = document.querySelectorAll('section.exercise');
  sections.forEach(function(section) {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'ex-check-btn';
    btn.textContent = 'Check exercise';
    btn.disabled = true;
    btn.style.cssText = 'margin-top:14px;padding:8px 20px;font-family:var(--font-sans);font-size:.75rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;background:var(--ink);color:var(--paper);border:0;border-radius:3px;cursor:pointer;transition:opacity .15s';
    btn.addEventListener('mouseover', function() { if (!this.disabled) this.style.opacity = '.85'; });
    btn.addEventListener('mouseout', function() { this.style.opacity = '1'; });
    btn.onclick = function() { checkExercise(section.id); };
    btn.addEventListener('disabled', function() { this.style.opacity = '.4'; this.style.cursor = 'default'; });
    section.appendChild(btn);
  });
  // Hide final submit until all exercises are done
  updateFinalSubmitState();

  // Show best score banner if this worksheet was completed before
  (function() {
    try {
      if (!window.FCEStore || !window.CHAPTER_ID) return;
      var data = JSON.parse(localStorage.getItem('wordplay_progress') || '{}');
      var level = window.LEVEL;
      if (!level) return;
      var saved = data[level] && data[level][window.CHAPTER_ID];
      if (!saved || !saved.pct) return;
      var pct = saved.pct;
      var color = pct >= 80 ? 'var(--green)' : pct >= 50 ? 'var(--amber)' : 'var(--red)';
      var label = pct >= 80 ? 'Great score' : pct >= 50 ? 'Good attempt' : 'Keep practising';
      var banner = document.createElement('div');
      banner.style.cssText = 'display:flex;align-items:center;gap:10px;padding:10px 16px;margin-bottom:20px;background:var(--cream-deep,#F0EDE6);border-radius:6px;font-family:var(--font-sans);font-size:.8rem;color:var(--muted)';
      banner.innerHTML = '<span>Previous best:</span><strong style="color:' + color + ';font-size:.95rem">' + pct + '%</strong><span style="color:var(--muted)">&mdash; ' + label + '. Can you beat it?</span>';
      var form = document.getElementById('worksheet');
      if (form) form.insertBefore(banner, form.firstChild);
    } catch(e) {}
  })();
})();
