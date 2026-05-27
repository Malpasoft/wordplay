// ══════════════════════════════════════════════════════════════════
// card-exercise.js v104 — one-question-at-a-time interactive grading
// Requires: window.ANSWERS (set by each worksheet)
// ══════════════════════════════════════════════════════════════════
(function() {
  var form = document.getElementById('worksheet');
  if (!form || !window.ANSWERS) return;

  // ── Extract all questions (form + any section.exercise outside it) ─
  var questions = [];
  var contextCache = {};

  document.querySelectorAll('section.exercise').forEach(function(section) {
    var sectionId = section.id || '';
    var contextEl = section.querySelector('.reading-context');
    if (contextEl) contextCache[sectionId] = contextEl.innerHTML;

    section.querySelectorAll('.q').forEach(function(qEl, qIdxInSection) {
      var cg  = qEl.querySelector('.choice-group[data-q]');
      var inp = qEl.querySelector('input[data-q]');

      // Clone and strip inline inputs/selects from the displayed question HTML
      var qtEl   = qEl.querySelector('.q-text');
      var qClone = (qtEl || qEl).cloneNode(true);
      qClone.querySelectorAll('input, select, textarea').forEach(function(el) { el.remove(); });
      var qHTML  = qClone.innerHTML;

      if (cg) {
        var opts = [];
        cg.querySelectorAll('.choice-btn').forEach(function(b) {
          opts.push({ value: b.dataset.value, label: b.textContent.trim() });
        });
        // Fisher-Yates shuffle display order
        for (var i = opts.length - 1; i > 0; i--) {
          var j = Math.floor(Math.random() * (i + 1));
          var t = opts[i]; opts[i] = opts[j]; opts[j] = t;
        }
        questions.push({
          id: cg.dataset.q,
          type: 'mcq',
          html: qHTML,
          options: opts,
          dataAnswer: cg.dataset.answer || '',
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

  var total        = questions.length;
  var current      = 0;
  var score        = 0;
  var answered     = false;
  var lastSectionId = null;

  // Hide original form, results, submit buttons, and exercises outside the form
  form.style.display = 'none';
  var staticResults = document.getElementById('results');
  if (staticResults) staticResults.style.display = 'none';
  document.querySelectorAll('.submit-wrap').forEach(function(el) { el.style.display = 'none'; });
  document.querySelectorAll('section.exercise').forEach(function(s) {
    if (!form.contains(s)) s.style.display = 'none';
  });

  // Create card container
  var container = document.createElement('div');
  container.id  = 'card-exercise';
  container.innerHTML =
    '<div class="ce-progress-bar"><div class="ce-progress-fill" id="ceProgressFill" style="width:0%"></div></div>' +
    '<div class="ce-counter" id="ceCounter">1 of ' + total + '</div>' +
    '<div id="ceCardWrap"></div>';
  form.parentNode.insertBefore(container, form);

  // ── Audio / haptic feedback ───────────────────────────────────
  function playTone(correct) {
    try {
      var ctx = new (window.AudioContext || window.webkitAudioContext)();
      if (correct) {
        [[660, 0], [880, 0.1]].forEach(function(pair) {
          var o = ctx.createOscillator(), g = ctx.createGain();
          o.connect(g); g.connect(ctx.destination);
          o.type = 'sine'; o.frequency.value = pair[0];
          var t = ctx.currentTime + pair[1];
          g.gain.setValueAtTime(0, t);
          g.gain.linearRampToValueAtTime(0.22, t + 0.01);
          g.gain.exponentialRampToValueAtTime(0.001, t + 0.4);
          o.start(t); o.stop(t + 0.4);
        });
      } else {
        var o = ctx.createOscillator(), g = ctx.createGain();
        o.connect(g); g.connect(ctx.destination);
        o.type = 'sawtooth'; o.frequency.value = 160;
        g.gain.setValueAtTime(0.18, ctx.currentTime);
        g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.22);
        o.start(); o.stop(ctx.currentTime + 0.22);
        try { navigator.vibrate && navigator.vibrate([50, 20, 50]); } catch(e2) {}
      }
      setTimeout(function() { try { ctx.close(); } catch(e2) {} }, 1200);
    } catch(e) {}
  }

  // ── Helpers ───────────────────────────────────────────────────
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function(c) {
      return { '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' }[c];
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
      .replace(/[''`]/g, "'").replace(/[""]/g, '"');
  }

  function isCorrect(q, userVal) {
    var u = norm(userVal);
    if (!u) return false;
    var a = getAns(q.id);
    if (a.answer && u === norm(a.answer)) return true;
    if (a.accept.some(function(alt) { return u === norm(alt); })) return true;
    if (q.dataAnswer && u === norm(q.dataAnswer)) return true;
    return false;
  }

  // ── Render current card ───────────────────────────────────────
  function render(idx) {
    answered = false;
    var q   = questions[idx];
    var pct = Math.round((idx / total) * 100);
    document.getElementById('ceProgressFill').style.width = pct + '%';
    document.getElementById('ceCounter').textContent = (idx + 1) + ' of ' + total;

    var html = '<div class="ce-card">';
    html += '<div class="ce-question-num">Question ' + (idx + 1) + ' of ' + total + '</div>';

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
            (idx < total - 1 ? 'Next &#9654;' : 'See results &#10003;') + '</button>';
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
    var correct = isCorrect(q, btn.dataset.value);
    if (correct) score++;

    document.querySelectorAll('.ce-option-btn').forEach(function(b) {
      b.disabled = true;
      if (isCorrect(q, b.dataset.value)) b.classList.add('ce-correct');
      else if (b === btn)                b.classList.add('ce-wrong');
    });

    playTone(correct);
    showFeedback(q.id, correct, null);
  };

  // ── Text check ────────────────────────────────────────────────
  window.ceCheck = function() {
    var q   = questions[current];
    var inp = document.getElementById('ceTextInput');
    if (!inp || inp.disabled) return;
    var userVal = inp.value.trim();
    var correct = isCorrect(q, userVal);
    if (correct) score++;

    inp.disabled = true;
    inp.classList.add(correct ? 'ce-correct' : 'ce-wrong');
    var checkBtn = inp.parentNode && inp.parentNode.querySelector('.ce-check-btn');
    if (checkBtn) checkBtn.disabled = true;

    var correctAnswer = correct ? null : (getAns(q.id).answer || q.dataAnswer || '');
    playTone(correct);
    showFeedback(q.id, correct, correctAnswer || null);
  };

  // ── Feedback + reveal Next ────────────────────────────────────
  function showFeedback(id, correct, correctAnswer) {
    answered = true;
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
    var pct  = Math.round((score / total) * 100);
    var pass = pct >= 70;
    document.getElementById('ceProgressFill').style.width = '100%';
    document.getElementById('ceCounter').textContent = 'Complete';

    document.getElementById('ceCardWrap').innerHTML =
      '<div class="ce-results">' +
      '<div class="ce-results-score">' + score + ' / ' + total + '</div>' +
      '<div class="ce-results-pct">' + pct + '%</div>' +
      '<div class="ce-results-msg">' +
        (pass ? 'Well done — try the mastery game!' : 'Keep going — try again for a better score.') +
      '</div>' +
      '<a href="game.html" class="ce-results-cta">Mastery game &#9654;</a>' +
      '<button class="ce-results-retry" onclick="ceRetry()">Try again</button>' +
      '</div>';

    try {
      var lvl  = window.LEVEL || '';
      var chId = window.CHAPTER_ID || '';
      if (lvl && chId) {
        var raw  = localStorage.getItem('wordplay_progress');
        var data = raw ? JSON.parse(raw) : {};
        data[lvl] = data[lvl] || {};
        var key  = 'worksheet_' + chId;
        var prev = data[lvl][key];
        if (!prev || pct > (prev.pct || 0)) {
          data[lvl][key] = { pct: pct, done: pass, date: new Date().toISOString() };
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
    answered = false;
    render(0);
  };

  // ── Swipe to advance (only after answering) ───────────────────
  var swipeStartX = 0, swipeStartY = 0;
  var swipeActive = false, swipeDelta = 0;
  var swipeCard   = null;

  document.addEventListener('touchstart', function(e) {
    if (!answered || e.touches.length > 1) return;
    var card = document.querySelector('.ce-card');
    if (!card) return;
    swipeStartX = e.touches[0].clientX;
    swipeStartY = e.touches[0].clientY;
    swipeActive = false;
    swipeDelta  = 0;
    swipeCard   = card;
    swipeCard.style.transition = 'none';
  }, { passive: true });

  document.addEventListener('touchmove', function(e) {
    if (!swipeCard) return;
    var dx = e.touches[0].clientX - swipeStartX;
    var dy = e.touches[0].clientY - swipeStartY;
    if (!swipeActive) {
      if (Math.abs(dy) > Math.abs(dx) + 8) { swipeCard = null; return; }
      if (Math.abs(dx) < 8) return;
      swipeActive = true;
    }
    e.preventDefault();
    swipeDelta = dx;
    var fade = 1 - Math.min(1, Math.abs(dx) / (window.innerWidth * 0.55));
    swipeCard.style.transform = 'translateX(' + dx + 'px)';
    swipeCard.style.opacity   = Math.max(0.25, fade);
  }, { passive: false });

  document.addEventListener('touchend', function() {
    if (!swipeCard) return;
    var card  = swipeCard;
    swipeCard = null;
    if (!swipeActive || Math.abs(swipeDelta) < 30) {
      card.style.transition = 'transform .22s ease-out, opacity .22s ease-out';
      card.style.transform  = '';
      card.style.opacity    = '';
      setTimeout(function() { card.style.transition = ''; }, 230);
      return;
    }
    if (swipeDelta < 0) {
      card.style.transition = 'transform .26s ease-in, opacity .22s ease-in';
      card.style.transform  = 'translateX(' + (-window.innerWidth * 1.3) + 'px) rotate(-18deg)';
      card.style.opacity    = '0';
      setTimeout(window.ceNext, 270);
    } else {
      card.style.transition = 'transform .22s ease-out, opacity .22s ease-out';
      card.style.transform  = '';
      card.style.opacity    = '';
      setTimeout(function() { card.style.transition = ''; }, 230);
    }
  }, { passive: true });

  // Init
  render(0);
})();
