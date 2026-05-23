// ══════════════════════════════════════════════════════════════════
// card-exercise.js — one-question-at-a-time interactive grading
// Replaces the submit-all worksheet with an instant-feedback card flow
// Requires: window.ANSWERS, window.EXPLANATIONS (set by each worksheet)
// ══════════════════════════════════════════════════════════════════
(function() {
  var form = document.getElementById('worksheet');
  if (!form || !window.ANSWERS) return;

  // ── Extract all questions from the form DOM ───────────────────
  var questions = [];
  var contextCache = {}; // section id → HTML of reading context

  form.querySelectorAll('section.exercise').forEach(function(section) {
    var sectionId = section.id || '';
    var contextEl = section.querySelector('.reading-context');
    if (contextEl) contextCache[sectionId] = contextEl.innerHTML;

    section.querySelectorAll('.q').forEach(function(qEl, qIdxInSection) {
      var cg  = qEl.querySelector('.choice-group[data-q]');
      var inp = qEl.querySelector('input[data-q]');
      var qtEl = qEl.querySelector('.q-text');
      var qHTML = qtEl ? qtEl.innerHTML : qEl.innerHTML;

      if (cg) {
        var opts = [];
        cg.querySelectorAll('.choice-btn').forEach(function(b) {
          opts.push({ value: b.dataset.value, label: b.textContent.trim() });
        });
        questions.push({
          id: cg.dataset.q,
          type: 'mcq',
          html: qHTML,
          options: opts,
          sectionId: sectionId,
          firstInSection: qIdxInSection === 0
        });
      } else if (inp) {
        questions.push({
          id: inp.dataset.q,
          type: 'text',
          html: qHTML,
          placeholder: inp.getAttribute('placeholder') || 'type your answer…',
          sectionId: sectionId,
          firstInSection: qIdxInSection === 0
        });
      }
    });
  });

  if (!questions.length) return;

  var total   = questions.length;
  var current = 0;
  var score   = 0;
  var lastSectionId = null;

  // Hide the original form and any static results block
  form.style.display = 'none';
  var staticResults = document.getElementById('results');
  if (staticResults) staticResults.style.display = 'none';
  // Also hide submit/reset buttons that may be outside the form
  document.querySelectorAll('.submit-wrap').forEach(function(el) { el.style.display = 'none'; });

  // Create card container
  var container = document.createElement('div');
  container.id = 'card-exercise';
  container.innerHTML =
    '<div class="ce-progress-bar"><div class="ce-progress-fill" id="ceProgressFill" style="width:0%"></div></div>' +
    '<div class="ce-counter" id="ceCounter">1 of ' + total + '</div>' +
    '<div id="ceCardWrap"></div>';
  form.parentNode.insertBefore(container, form);

  // ── Helpers ───────────────────────────────────────────────────
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function(c) {
      return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];
    });
  }

  function getAns(id) {
    var a = window.ANSWERS[id];
    if (!a) return { answer: '', accept: [] };
    if (typeof a === 'string') return { answer: a, accept: [] };
    return { answer: a.answer || '', accept: a.accept || [] };
  }

  function norm(s) {
    return (s || '').toLowerCase().trim()
      .replace(/[.!?,;:]$/, '').replace(/\s+/g, ' ')
      .replace(/[‘’`]/g, "'").replace(/[“”]/g, '"');
  }

  function isCorrect(id, userVal) {
    var a = getAns(id);
    var u = norm(userVal);
    if (!u) return false;
    if (u === norm(a.answer)) return true;
    return a.accept.some(function(alt) { return u === norm(alt); });
  }

  // ── Render current card ───────────────────────────────────────
  function render(idx) {
    var q   = questions[idx];
    var pct = Math.round((idx / total) * 100);
    document.getElementById('ceProgressFill').style.width = pct + '%';
    document.getElementById('ceCounter').textContent = (idx + 1) + ' of ' + total;

    var html = '<div class="ce-card">';
    html += '<div class="ce-question-num">Question ' + (idx + 1) + '</div>';

    // Show reading context only at the first question of its section
    if (q.firstInSection && q.sectionId && contextCache[q.sectionId] && q.sectionId !== lastSectionId) {
      html += '<div class="ce-context">' + contextCache[q.sectionId] + '</div>';
      lastSectionId = q.sectionId;
    }

    html += '<div class="ce-question-text">' + q.html + '</div>';

    if (q.type === 'mcq') {
      html += '<div class="ce-options" id="ceOptions">';
      q.options.forEach(function(opt) {
        html += '<button class="ce-option-btn" data-value="' + esc(opt.value) + '" onclick="ceSelect(this)">' + esc(opt.label) + '</button>';
      });
      html += '</div>';
    } else {
      html += '<div class="ce-text-wrap">';
      html += '<input type="text" id="ceTextInput" class="ce-text-input" autocomplete="off" spellcheck="false" placeholder="' + esc(q.placeholder) + '">';
      html += '<button class="ce-check-btn" onclick="ceCheck()">Check</button>';
      html += '</div>';
    }

    html += '<div class="ce-feedback" id="ceFeedback"></div>';
    html += '<button class="ce-next-btn" id="ceNextBtn" onclick="ceNext()">' +
            (idx < total - 1 ? 'Next question →' : 'See results →') + '</button>';
    html += '</div>';

    document.getElementById('ceCardWrap').innerHTML = html;

    if (q.type === 'text') {
      var ti = document.getElementById('ceTextInput');
      if (ti) {
        ti.focus();
        ti.addEventListener('keydown', function(e) { if (e.key === 'Enter') ceCheck(); });
      }
    }
  }

  // ── MCQ selection ─────────────────────────────────────────────
  window.ceSelect = function(btn) {
    var q = questions[current];
    var correct = isCorrect(q.id, btn.dataset.value);
    if (correct) score++;

    document.querySelectorAll('.ce-option-btn').forEach(function(b) {
      b.disabled = true;
      var isChosen  = b === btn;
      var isCorrectAns = isCorrect(q.id, b.dataset.value);
      if (isCorrectAns) b.classList.add('ce-correct');
      else if (isChosen) b.classList.add('ce-wrong');
    });

    showFeedback(q.id, correct, null);
  };

  // ── Text check ────────────────────────────────────────────────
  window.ceCheck = function() {
    var q   = questions[current];
    var inp = document.getElementById('ceTextInput');
    if (!inp || inp.disabled) return;
    var userVal = inp.value.trim();
    var correct = isCorrect(q.id, userVal);
    if (correct) score++;

    inp.disabled = true;
    inp.classList.add(correct ? 'ce-correct' : 'ce-wrong');
    var checkBtn = inp.parentNode ? inp.parentNode.querySelector('.ce-check-btn') : null;
    if (checkBtn) checkBtn.disabled = true;

    var correctAnswer = correct ? null : getAns(q.id).answer;
    showFeedback(q.id, correct, correctAnswer);
  };

  // ── Show feedback + reveal Next button ────────────────────────
  function showFeedback(id, correct, correctAnswer) {
    var expl = window.EXPLANATIONS ? (window.EXPLANATIONS[id] || '') : '';
    var fb   = document.getElementById('ceFeedback');
    fb.className = 'ce-feedback ' + (correct ? 'ce-fb-correct' : 'ce-fb-wrong');
    fb.style.display = 'block';

    var msg = correct ? '<strong>Correct!</strong>' : '<strong>Not quite.</strong>';
    if (!correct && correctAnswer) msg += ' The answer is: <em>' + esc(correctAnswer) + '</em>.';
    if (expl) msg += ' ' + expl;
    fb.innerHTML = msg;

    var nb = document.getElementById('ceNextBtn');
    if (nb) nb.style.display = 'block';
  }

  // ── Advance ───────────────────────────────────────────────────
  window.ceNext = function() {
    current++;
    if (current >= total) showResults();
    else render(current);
  };

  // ── Results screen ────────────────────────────────────────────
  function showResults() {
    var pct = Math.round((score / total) * 100);
    document.getElementById('ceProgressFill').style.width = '100%';
    document.getElementById('ceCounter').textContent = 'Complete';

    var pass = pct >= 70;
    document.getElementById('ceCardWrap').innerHTML =
      '<div class="ce-results">' +
      '<div class="ce-results-score">' + score + ' / ' + total + '</div>' +
      '<div class="ce-results-pct">' + pct + '%</div>' +
      '<div class="ce-results-msg">' + (pass ? 'Well done — try the mastery game!' : 'Keep going — try again for a better score.') + '</div>' +
      '<a href="game.html" class="ce-results-cta">Mastery game →</a>' +
      '<button class="ce-results-retry" onclick="ceRetry()">Try again</button>' +
      '</div>';

    // Save progress
    try {
      var lvl  = window.LEVEL || '';
      var chId = window.CHAPTER_ID || '';
      if (lvl && chId) {
        var raw  = localStorage.getItem('wordplay_progress');
        var data = raw ? JSON.parse(raw) : {};
        data[lvl] = data[lvl] || {};
        var prev = data[lvl][chId];
        if (!prev || pct > (prev.pct || 0)) {
          data[lvl][chId] = { pct: pct, done: pass, date: new Date().toISOString() };
          localStorage.setItem('wordplay_progress', JSON.stringify(data));
        }
      }
    } catch(e) {}
  }

  // ── Retry ─────────────────────────────────────────────────────
  window.ceRetry = function() {
    current = 0;
    score   = 0;
    lastSectionId = null;
    render(0);
  };

  // Init
  render(0);
})();
