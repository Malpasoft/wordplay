// ══════════════════════════════════════════════════════════════════
// game.js v2 — Dominio model
// 4 key items × 3 question types, score toward 100 points to win
// GAME_DATA interface unchanged; per-chapter HTML needs no edits.
// ══════════════════════════════════════════════════════════════════


// ── Game Configuration (magic numbers extracted) ───────────────────
// Window-scoped for discovery and tuning. Consumers read but do not modify.
window.GAME_CONFIG = {
  SCORE_GOAL: 100,        // Points to reach to win a game
  BONUSES: {
    same:  5,             // Bonus for 2+ consecutive correct on same concept
    cross: 3              // Bonus for 3+ consecutive correct across concepts
  },
  AUDIO_TONES: {
    correct: [            // Two-tone correct answer sound (Hz, delay)
      [660, 0],           // 660 Hz at start
      [880, 0.1]          // 880 Hz at 100ms delay
    ],
    error: {
      frequency: 160,     // Hz for error buzz
      duration: 0.22      // Seconds
    }
  },
  CONFETTI: {
    count: 32,            // Number of confetti particles to emit
    fallDuration: [1.8, 2.2], // Min/max animation duration in seconds
    staggerDelay: 0.5,    // Max random stagger between particles
    lifetime: 4500        // Milliseconds before DOM cleanup
  }
};

(function () {
  'use strict';

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // ── Error boundary: user-facing message for missing data ──────────
  function showErrorMessage(msg) {
    var gameStart = document.getElementById('gameStart');
    if (!gameStart) return;
    var msgEl = document.createElement('div');
    msgEl.className = 'game-error-message';
    msgEl.style.cssText = 'padding:20px;background:var(--paper);border:1px solid var(--muted);border-radius:8px;color:var(--ink);font-family:var(--font-sans);line-height:1.5;margin:20px 0';

    var strong = document.createElement('strong');
    strong.textContent = 'Game Error: ';
    msgEl.appendChild(strong);

    var msgSpan = document.createElement('span');
    msgSpan.textContent = msg;
    msgEl.appendChild(msgSpan);

    msgEl.appendChild(document.createElement('br'));
    msgEl.appendChild(document.createElement('br'));

    var link = document.createElement('a');
    link.href = 'index.html';
    link.style.cssText = 'color:var(--amber);text-decoration:none';
    link.textContent = '← Back to chapter';
    msgEl.appendChild(link);

    gameStart.innerHTML = '';
    gameStart.appendChild(msgEl);
  }

  function init() {
    // ── Error boundary: ensure GAME_DATA is present ─────────────────
    if (!window.GAME_DATA) {
      showErrorMessage('Game data not found. Please ensure this page is loaded from a valid chapter.');
      return;
    }

    var DATA      = window.GAME_DATA;
    var ALL_ITEMS = DATA.items || [];
    var ITEMS     = ALL_ITEMS.slice(0, 4);
    if (!ITEMS.length) {
      showErrorMessage('No game items found. The chapter may not have content configured for this game.');
      return;
    }

    var STORAGE_KEY = DATA.storageKey || ('game_' + (DATA.level || '') + '_' + (DATA.chapterId || ''));
    var SCORE_GOAL  = window.GAME_CONFIG.SCORE_GOAL;

    // ── Language (via i18n module) ────────────────────────────────
    // window.i18n.isSpanish() checks DATA.level or html lang attribute
    var isEs = window.i18n ? window.i18n.isSpanish(DATA.level) : ((DATA.level || '').indexOf('es-') === 0) || (document.documentElement.lang === 'es');
    var getString = window.i18n ? window.i18n.getString : function(key) { return key; };

    var L = {
      start:      getString('game_start'),
      resume:     getString('game_resume'),
      newGame:    getString('game_newGame'),
      check:      getString('game_check'),
      next:       getString('game_next'),
      correct:    getString('game_correct'),
      wrong:      getString('game_wrong'),
      answer:     getString('game_answer'),
      placeholder:getString('game_placeholder'),
      sigLabel:   getString('game_sigLabel'),
      ctxLabel:   getString('game_ctxLabel'),
      prodLabel:  getString('game_prodLabel'),
      sigSub:     getString('game_sigSub'),
      ctxSub:     getString('game_ctxSub'),
      prodSub:    getString('game_prodSub'),
      toWin:      '/ ' + SCORE_GOAL + ' ' + getString('game_toWin_suffix'),
      desc:       ITEMS.length + ' ' + getString('game_desc_prefix') + ' ' + SCORE_GOAL + ' ' + (isEs ? 'puntos' : 'points'),
      hint:       getString('game_hint'),
      bestScore:  isEs ? 'Mejor puntuación:' : 'Best score:',
      dominio:    isEs ? '¡Dominio alcanzado!' : 'Mastery achieved!',
      wellDone:   isEs ? '¡Bien hecho!'      : 'Well done!',
      finalScore: isEs ? 'Puntuación:'       : 'Score:',
      printBtn:   isEs ? 'Ir a Imprimibles →' : 'Go to Printables →',
      backBtn:    isEs ? '← Volver al capítulo' : '← Back to chapter',
      bonusSame:  isEs ? '+5 racha mismo concepto' : '+5 same-concept run',
      bonusCross: isEs ? '+3 racha entre conceptos' : '+3 cross-concept streak',
      refOpen:    isEs ? '▼ Referencia — todas las palabras' : '▼ Reference — all words',
      refClose:   isEs ? '▲ Referencia' : '▲ Reference',
    };

    // ── Audio ─────────────────────────────────────────────────────
    function playTone(correct) {
      try {
        var ctx = new (window.AudioContext || window.webkitAudioContext)();
        if (correct) {
          window.GAME_CONFIG.AUDIO_TONES.correct.forEach(function(pair) {
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
          var errTone = window.GAME_CONFIG.AUDIO_TONES.error;
          var o = ctx.createOscillator(), g = ctx.createGain();
          o.connect(g); g.connect(ctx.destination);
          o.type = 'sawtooth'; o.frequency.value = errTone.frequency;
          g.gain.setValueAtTime(0.18, ctx.currentTime);
          g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + errTone.duration);
          o.start(); o.stop(ctx.currentTime + errTone.duration);
          try { navigator.vibrate && navigator.vibrate([50, 20, 50]); } catch(e2) {}
        }
        setTimeout(function() { try { ctx.close(); } catch(e2) {} }, 1200);
      } catch(e) {}
    }

    // ── Confetti ──────────────────────────────────────────────────
    function triggerConfetti() {
      if (!document.getElementById('cf-kf')) {
        var s = document.createElement('style');
        s.id = 'cf-kf';
        s.textContent = '@keyframes cfFall{to{transform:translateY(105vh) rotate(480deg);opacity:0}}';
        document.head.appendChild(s);
      }
      var colors = ['#C9A050','#E8A020','#D4B060','#B8860B','#F5D080','#C9A050'];
      var cfg = window.GAME_CONFIG.CONFETTI;
      for (var i = 0; i < cfg.count; i++) {
        var p = document.createElement('div');
        var sz = 6 + Math.random() * 6;
        var duration = cfg.fallDuration[0] + Math.random() * (cfg.fallDuration[1] - cfg.fallDuration[0]);
        var stagger = Math.random() * cfg.staggerDelay;
        p.style.cssText = 'position:fixed;top:-12px;width:' + sz + 'px;height:' + sz + 'px;border-radius:' + Math.round(Math.random()) + 'px;background:' + colors[Math.floor(Math.random() * colors.length)] + ';left:' + (5 + Math.random() * 90) + '%;animation:cfFall ' + duration + 's ' + stagger + 's ease-in forwards;z-index:999;pointer-events:none';
        document.body.appendChild(p);
        setTimeout(function(el) { if (el.parentNode) el.parentNode.removeChild(el); }, cfg.lifetime, p);
      }
    }

    // ── Helpers ───────────────────────────────────────────────────
    function shuffle(arr) {
      var a = arr.slice();
      for (var i = a.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var t = a[i]; a[i] = a[j]; a[j] = t;
      }
      return a;
    }

    function norm(s) {
      return (s || '').toLowerCase().trim()
        .replace(/[.!?,;:]$/g, '').replace(/\s+/g, ' ').replace(/[''`]/g, "'");
    }

    function esc(s) {
      return String(s || '').replace(/[&<>"']/g, function(c) {
        return { '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' }[c];
      });
    }

    function getItem(id) {
      for (var i = 0; i < ITEMS.length; i++) {
        if (ITEMS[i].id === id) return ITEMS[i];
      }
      return null;
    }

    // ── Queue ─────────────────────────────────────────────────────
    function buildQueue() {
      var q = [];
      ITEMS.forEach(function(item) {
        q.push({ itemId: item.id, qtype: 'significado' });
        q.push({ itemId: item.id, qtype: 'contexto'    });
        q.push({ itemId: item.id, qtype: 'produccion'  });
      });
      return shuffle(q);
    }

    // ── Persistence ───────────────────────────────────────────────
    function getBestScore() {
      try { return parseInt(localStorage.getItem(STORAGE_KEY + '_best') || '0', 10); } catch(e) { return 0; }
    }
    function saveBestScore(score) {
      try {
        if (score > getBestScore()) localStorage.setItem(STORAGE_KEY + '_best', String(score));
      } catch(e) {}
    }

    function saveState() {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify({
          score:        state.score,
          bestStreak:   state.bestStreak,
          crossStreak:  state.crossStreak,
          lastItemId:   state.lastItemId,
          sameRunCount: state.sameRunCount,
          itemCorrect:  state.itemCorrect,
          queue:        state.queue,
        }));
      } catch(e) {}
    }

    function loadState() {
      try {
        var raw = localStorage.getItem(STORAGE_KEY);
        if (!raw) return false;
        var saved = JSON.parse(raw);
        if (!saved || !saved.queue || !saved.queue.length) return false;
        var validIds = {};
        ITEMS.forEach(function(i) { validIds[i.id] = true; });
        var validQ = saved.queue.filter(function(q) { return validIds[q.itemId]; });
        if (!validQ.length) return false;
        state = {
          score:        saved.score       || 0,
          bestStreak:   saved.bestStreak  || 0,
          crossStreak:  saved.crossStreak || 0,
          lastItemId:   saved.lastItemId  || null,
          sameRunCount: saved.sameRunCount|| 0,
          itemCorrect:  saved.itemCorrect || {},
          queue:        validQ,
        };
        return true;
      } catch(e) { return false; }
    }

    function clearState() {
      try { localStorage.removeItem(STORAGE_KEY); } catch(e) {}
    }

    // ── State ─────────────────────────────────────────────────────
    var state = null;
    var autoTimer = null;
    var currentQItem = null;

    function freshState() {
      state = {
        score:        0,
        bestStreak:   0,
        crossStreak:  0,
        lastItemId:   null,
        sameRunCount: 0,
        itemCorrect:  {},
        queue:        buildQueue(),
      };
    }

    // ── Build play screen ─────────────────────────────────────────
    (function buildPlayScreen() {
      var play = document.querySelector('#gamePlay .game-play');
      if (!play) return;
      play.innerHTML =
        '<div class="gp-prog"><div class="gp-prog-fill" id="gProgressBar" style="width:0%"></div></div>' +
        '<div class="gp-meta">' +
          '<span class="gp-badge" id="gQTypeTag"></span>' +
          '<div class="gp-counter">' +
            '<span class="gp-streak" id="gStreakBadge" style="display:none">◆ 3 </span>' +
            '<span id="gScoreLabel">0</span>' +
            '<span style="color:var(--muted);font-size:.68rem;margin-left:3px">' + L.toWin + '</span>' +
          '</div>' +
        '</div>' +
        '<div class="game-term" id="gTerm"></div>' +
        '<div class="game-prompt" id="gPrompt"></div>' +
        '<div class="game-options" id="gOptions"></div>' +
        '<div class="gp-input-wrap" id="gInputWrap" style="display:none">' +
          '<input id="gInput" type="text" autocomplete="off" spellcheck="false" placeholder="' + L.placeholder + '">' +
          '<button id="gBtnCheck" class="game-btn primary">' + L.check + '</button>' +
        '</div>' +
        '<div class="game-feedback" id="gFeedback"></div>' +
        '<div class="game-example" id="gExample" style="display:none"></div>' +
        '<div class="gp-actions">' +
          '<button id="gBtnNext" class="game-btn primary" style="display:none">' + L.next + '</button>' +
        '</div>';
    })();

    // ── Update start screen text ──────────────────────────────────
    (function updateStartScreen() {
      var allPs = document.querySelectorAll('#gameStart .game-start p');
      if (allPs[0]) allPs[0].textContent = L.desc;
      if (allPs[1]) allPs[1].textContent = L.hint;
      var mastEl = document.getElementById('gStartMastered');
      if (mastEl) {
        var best = getBestScore();
        mastEl.textContent = best > 0 ? (L.bestScore + ' ' + best) : '';
      }
    })();

    // ── DOM refs ──────────────────────────────────────────────────
    function $$(id) { return document.getElementById(id); }
    var screens = {
      start:      $$('gameStart'),
      play:       $$('gamePlay'),
      completion: $$('gameCompletion'),
    };
    var el = {
      resumeSection:    $$('gResumeSection'),
      btnResume:        $$('gBtnResume'),
      btnNewFromResume: $$('gBtnNewFromResume'),
      btnStart:         $$('gBtnStart'),
      qTypeTag:    $$('gQTypeTag'),
      term:        $$('gTerm'),
      prompt:      $$('gPrompt'),
      options:     $$('gOptions'),
      inputWrap:   $$('gInputWrap'),
      input:       $$('gInput'),
      btnCheck:    $$('gBtnCheck'),
      feedback:    $$('gFeedback'),
      example:     $$('gExample'),
      btnNext:     $$('gBtnNext'),
      streakBadge: $$('gStreakBadge'),
      progressBar: $$('gProgressBar'),
      scoreLabel:  $$('gScoreLabel'),
      refToggle:   $$('gRefToggle'),
      refBody:     $$('gRefBody'),
      refList:     $$('gRefList'),
    };

    // ── Screen management ─────────────────────────────────────────
    function showScreen(name) {
      Object.keys(screens).forEach(function(k) {
        var scr = screens[k];
        if (scr) scr.classList.toggle('active', k === name);
      });
      if (name === 'play') {
        requestAnimationFrame(function() {
          var card = document.querySelector('#gamePlay .game-play');
          if (!card) return;
          var nav = document.querySelector('.site-header');
          var top = card.getBoundingClientRect().top + window.pageYOffset - (nav ? nav.getBoundingClientRect().height : 0) - 12;
          window.scrollTo({ top: Math.max(0, top), behavior: 'smooth' });
        });
      }
    }

    // ── Score bar ─────────────────────────────────────────────────
    function updateScoreBar() {
      var pct = Math.min(100, Math.round((state.score / SCORE_GOAL) * 100));
      if (el.progressBar) el.progressBar.style.width = pct + '%';
      if (el.scoreLabel)  el.scoreLabel.textContent  = state.score;
      if (el.streakBadge) {
        if (state.crossStreak >= 3) {
          el.streakBadge.textContent = '◆ ' + state.crossStreak + ' ';
          el.streakBadge.style.display = '';
        } else {
          el.streakBadge.style.display = 'none';
        }
      }
    }

    // ── Show question ─────────────────────────────────────────────
    function showQ(qItem) {
      currentQItem = qItem;
      if (autoTimer) { clearTimeout(autoTimer); autoTimer = null; }

      var playCard = document.querySelector('#gamePlay .game-play');
      if (playCard) {
        playCard.style.transition = 'none';
        playCard.style.transform  = 'translateX(28px)';
        playCard.style.opacity    = '0';
        void playCard.offsetHeight;
        playCard.style.transition = 'transform .2s ease-out, opacity .18s ease-out';
        playCard.style.transform  = '';
        playCard.style.opacity    = '';
        setTimeout(function() { playCard.style.transition = ''; }, 220);
      }

      var item = getItem(qItem.itemId);
      var type = qItem.qtype;

      if (el.feedback) { el.feedback.textContent = ''; el.feedback.className = 'game-feedback'; }
      if (el.example)  { el.example.textContent  = ''; el.example.style.display = 'none'; }
      if (el.btnNext)  el.btnNext.style.display   = 'none';

      // Question type label
      var labels = { significado: L.sigLabel, contexto: L.ctxLabel, produccion: L.prodLabel };
      if (el.qTypeTag) el.qTypeTag.textContent = labels[type] || type;

      if (type === 'significado') {
        // Show English term → pick Spanish meaning
        if (el.term)   el.term.textContent   = item.term;
        if (el.prompt) el.prompt.textContent = L.sigSub;
        if (el.options)   el.options.style.display   = '';
        if (el.inputWrap) el.inputWrap.style.display = 'none';
        renderMC(
          item.meaning,
          ITEMS.filter(function(i) { return i.id !== item.id; }).map(function(i) { return i.meaning; })
        );
      } else if (type === 'contexto') {
        // Show gapped sentence → pick/type answer
        if (el.term) {
          var sent = item.completion || item.example || '';
          if (sent) {
            var parts = esc(sent).split('_____');
            el.term.innerHTML = '';
            for (var p = 0; p < parts.length; p++) {
              if (p > 0) {
                var gap = document.createElement('span');
                gap.className = 'game-gap';
                gap.textContent = '_____';
                el.term.appendChild(gap);
              }
              var txt = document.createTextNode(parts[p]);
              el.term.appendChild(txt);
            }
          } else {
            el.term.textContent = item.term;
          }
        }
        if (el.prompt) el.prompt.textContent = L.ctxSub;
        if (el.options)   el.options.style.display   = '';
        if (el.inputWrap) el.inputWrap.style.display = 'none';
        renderMC(
          item.answer || item.term,
          ITEMS.filter(function(i) { return i.id !== item.id; }).map(function(i) { return i.answer || i.term; })
        );
      } else {
        // produccion: show Spanish meaning → type English term
        if (el.term)   el.term.textContent   = item.meaning;
        if (el.prompt) el.prompt.textContent = L.prodSub;
        if (el.options)   el.options.style.display   = 'none';
        if (el.inputWrap) el.inputWrap.style.display = '';
        if (el.input) {
          el.input.value    = '';
          el.input.disabled = false;
        }
        if (el.btnCheck) el.btnCheck.disabled = true;
        setTimeout(function() { if (el.input) el.input.focus(); }, 80);
      }

      updateScoreBar();
    }

    // ── MC options ────────────────────────────────────────────────
    function renderMC(correct, distractorPool) {
      if (!el.options) return;
      var opts = shuffle([correct].concat(shuffle(distractorPool).slice(0, 3)));
      el.options.innerHTML = opts.map(function(o) {
        return '<button type="button" class="game-option" data-v="' + esc(o) + '">' + esc(o) + '</button>';
      }).join('');
      el.options.querySelectorAll('.game-option').forEach(function(btn) {
        btn.addEventListener('click', function() {
          gradeAnswer(btn.dataset.v);
        });
      });
    }

    // ── Grade answer ──────────────────────────────────────────────
    /**
     * GAME ALGORITHM: Dominio Mastery Model
     *
     * The game implements a 4-stage mastery progression:
     * 1. ITEM MASTERY: Each of 4 key items must be answered correctly once (significado, contexto, produccion).
     *    All 3 question types = 12 total questions (4 items × 3 types).
     *
     * 2. SCORING: Each correct answer = 10 points.
     *    - Bonuses apply on top of base 10 points:
     *      * Same-concept run (sameRunCount >= 2): +5 bonus (stay focused)
     *      * Cross-concept streak (crossStreak >= 3): +3 bonus (prove flexibility)
     *    - Incorrect answer: lose 3 points (min 0). Requeue at end. Resets both streaks.
     *
     * 3. WIN CONDITION: Score >= SCORE_GOAL (100 points) AND all 4 items correct.
     *    Without both, the game loops with fresh questions. After win, save to localStorage.
     *
     * 4. GRADING LOGIC:
     *    - significado (meaning): MC from 4 options (correct + 3 distractors). Exact match.
     *    - contexto (context): MC from gapped sentence. Exact match or accept[] variants.
     *    - produccion (production): Free-form text input → correct term (case-insensitive,
     *      punctuation-insensitive, or any item.accept[] alias).
     *
     * @param {string} userVal - The user's answer (from input field or selected button)
     */
    function gradeAnswer(userVal) {
      if (!currentQItem) return;
      var qItem  = currentQItem;
      var item   = getItem(qItem.itemId);
      var type   = qItem.qtype;
      var correct = (type === 'contexto') ? (item.answer || item.term) : item.term;

      var isCorrect = false;
      if (type === 'produccion') {
        isCorrect = norm(userVal) === norm(correct) ||
          (item.accept || []).some(function(a) { return norm(userVal) === norm(a); });
      } else {
        isCorrect = userVal === correct;
      }

      // Disable options / input
      if (el.options) {
        el.options.querySelectorAll('.game-option').forEach(function(btn) {
          btn.disabled = true;
          if (btn.dataset.v === correct)              btn.classList.add('correct');
          else if (btn.dataset.v === userVal && !isCorrect) btn.classList.add('wrong');
        });
      }
      if (el.input)    el.input.disabled    = true;
      if (el.btnCheck) el.btnCheck.disabled = true;

      playTone(isCorrect);

      // ── Score ──────────────────────────────────────────────────
      var bonusMsg = '';
      if (isCorrect) {
        var pts = 10;
        var prevId = state.lastItemId;
        state.lastItemId = item.id;

        if (prevId !== null && prevId === item.id) {
          // Same-item run: previous correct was same item
          state.sameRunCount++;
          state.crossStreak = 0;
          if (state.sameRunCount >= 2) { pts += window.GAME_CONFIG.BONUSES.same; bonusMsg = L.bonusSame; }
        } else if (prevId !== null && prevId !== item.id) {
          // Different item: extend cross-item streak
          state.crossStreak++;
          state.sameRunCount = 1;
          if (state.crossStreak > state.bestStreak) state.bestStreak = state.crossStreak;
          if (state.crossStreak >= 3) { pts += window.GAME_CONFIG.BONUSES.cross; bonusMsg = L.bonusCross; }
        } else {
          // First correct answer ever
          state.crossStreak = 0;
          state.sameRunCount = 1;
        }

        state.score += pts;
        state.itemCorrect[item.id] = true;

        // Remove from queue
        var idx = state.queue.indexOf(qItem);
        if (idx !== -1) state.queue.splice(idx, 1);
      } else {
        state.score        = Math.max(0, state.score - 3);
        state.crossStreak  = 0;
        state.sameRunCount = 0;
        // Requeue at end
        var idx2 = state.queue.indexOf(qItem);
        if (idx2 !== -1) { state.queue.splice(idx2, 1); state.queue.push(qItem); }
      }

      // ── Feedback ──────────────────────────────────────────────
      if (el.feedback) {
        el.feedback.className = 'game-feedback ' + (isCorrect ? 'correct' : 'wrong');
        el.feedback.innerHTML = '';

        if (isCorrect) {
          var checkMark = document.createTextNode('✓ ' + L.correct);
          el.feedback.appendChild(checkMark);

          if (bonusMsg) {
            el.feedback.appendChild(document.createTextNode('  '));
            var em = document.createElement('em');
            em.textContent = bonusMsg;
            el.feedback.appendChild(em);
          }
        } else {
          var errorMsg = document.createTextNode(L.wrong + '. ' + L.answer + ' ');
          el.feedback.appendChild(errorMsg);

          var strong = document.createElement('strong');
          strong.textContent = correct;
          el.feedback.appendChild(strong);
        }
      }
      if (item.example && el.example) {
        el.example.textContent = item.example;
        el.example.style.display = 'block';
      }

      updateScoreBar();
      renderReference();

      // ── Win check ─────────────────────────────────────────────
      var allItemsCorrect = ITEMS.every(function(i) { return state.itemCorrect[i.id]; });
      if (state.score >= SCORE_GOAL && allItemsCorrect) {
        saveBestScore(state.score);
        if (window.FCEStore && DATA.chapterId && DATA.level) {
          try { FCEStore.saveGameResult(DATA.chapterId, ITEMS.length, ITEMS.length); } catch(e) {}
          try { FCEStore.addXP(30); } catch(e) {}
        }
        saveState();
        autoTimer = setTimeout(function() {
          autoTimer = null;
          clearState();
          renderCompletion();
        }, 1500);
        return;
      }

      saveState();

      if (isCorrect) {
        autoTimer = setTimeout(function() { autoTimer = null; nextQ(); }, 1200);
      } else {
        if (el.btnNext) el.btnNext.style.display = 'block';
      }
    }

    // ── Next question ─────────────────────────────────────────────
    function nextQ() {
      if (autoTimer) { clearTimeout(autoTimer); autoTimer = null; }
      if (!state.queue.length) {
        // Rebuild with any items not yet answered correctly
        var missing = ITEMS.filter(function(i) { return !state.itemCorrect[i.id]; });
        if (!missing.length) { renderCompletion(); return; }
        var extra = [];
        missing.forEach(function(item) {
          extra.push({ itemId: item.id, qtype: 'significado' });
          extra.push({ itemId: item.id, qtype: 'contexto'    });
          extra.push({ itemId: item.id, qtype: 'produccion'  });
        });
        state.queue = shuffle(extra);
      }
      showQ(state.queue[0]);
    }

    // ── Reference panel ───────────────────────────────────────────
    function renderReference() {
      if (!el.refList) return;
      el.refList.innerHTML = '';
      ITEMS.forEach(function(item) {
        var done = state && state.itemCorrect && state.itemCorrect[item.id];

        var itemDiv = document.createElement('div');
        itemDiv.className = 'game-ref-item';

        var termSpan = document.createElement('span');
        termSpan.className = 'ref-term';
        termSpan.textContent = item.term + (done ? ' ✓' : '');
        itemDiv.appendChild(termSpan);

        var defDiv = document.createElement('div');
        defDiv.className = 'ref-def';
        defDiv.textContent = item.meaning;
        itemDiv.appendChild(defDiv);

        var exDiv = document.createElement('div');
        exDiv.className = 'ref-ex';
        exDiv.textContent = item.example || '';
        itemDiv.appendChild(exDiv);

        el.refList.appendChild(itemDiv);
      });
    }

    // ── Completion screen ─────────────────────────────────────────
    function renderCompletion() {
      var comp = document.querySelector('#gameCompletion .game-complete');
      if (comp) {
        comp.innerHTML = '';

        var titleDiv = document.createElement('div');
        titleDiv.style.cssText = 'font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2.5px;text-transform:uppercase;color:var(--amber);margin-bottom:8px';
        titleDiv.textContent = DATA.title || (DATA.chapterId || '');
        comp.appendChild(titleDiv);

        var h2 = document.createElement('h2');
        h2.style.cssText = 'font-family:Georgia,serif;font-size:2rem;font-weight:700;color:var(--ink);margin:0 0 10px';
        h2.textContent = L.dominio;
        comp.appendChild(h2);

        var scoreP = document.createElement('p');
        scoreP.style.cssText = 'font-family:var(--font-sans);font-size:.88rem;color:var(--muted);margin:0 0 24px';
        scoreP.appendChild(document.createTextNode(L.finalScore + ' '));
        var scoreStrong = document.createElement('strong');
        scoreStrong.textContent = state.score;
        scoreP.appendChild(scoreStrong);
        comp.appendChild(scoreP);

        var printLink = document.createElement('a');
        printLink.href = 'printables.html';
        printLink.style.cssText = 'display:inline-block;padding:14px 36px;background:var(--amber);color:#1A1A1A;font-family:var(--font-sans);font-size:.82rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;border-radius:5px';
        printLink.textContent = L.printBtn;
        comp.appendChild(printLink);

        comp.appendChild(document.createElement('br'));
        comp.appendChild(document.createElement('br'));

        var backLink = document.createElement('a');
        backLink.href = 'index.html';
        backLink.style.cssText = 'font-family:var(--font-sans);font-size:.78rem;color:var(--muted);text-decoration:none';
        backLink.textContent = L.backBtn;
        comp.appendChild(backLink);
      }
      showScreen('completion');
      setTimeout(triggerConfetti, 300);
    }

    // ── Start screen ──────────────────────────────────────────────
    function renderStart() {
      var hasSaved = state && state.queue && state.queue.length < (ITEMS.length * 3);
      if (el.resumeSection) el.resumeSection.style.display = hasSaved ? 'block' : 'none';
      if (el.btnStart)      el.btnStart.style.display      = hasSaved ? 'none'  : '';
      showScreen('start');
    }

    // ── Input events ──────────────────────────────────────────────
    if (el.input) {
      el.input.addEventListener('input', function() {
        if (el.btnCheck) el.btnCheck.disabled = !el.input.value.trim();
      });
      el.input.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && el.btnCheck && !el.btnCheck.disabled) el.btnCheck.click();
      });
    }
    if (el.btnCheck) {
      el.btnCheck.addEventListener('click', function() {
        if (!currentQItem || !el.input) return;
        gradeAnswer(el.input.value);
      });
    }

    // ── Button wiring ─────────────────────────────────────────────
    if (el.btnStart) {
      el.btnStart.addEventListener('click', function() {
        freshState(); saveState(); renderReference(); showScreen('play'); nextQ();
      });
    }
    if (el.btnResume) {
      el.btnResume.addEventListener('click', function() {
        renderReference(); showScreen('play'); nextQ();
      });
    }
    if (el.btnNewFromResume) {
      el.btnNewFromResume.addEventListener('click', function() {
        freshState(); saveState(); renderReference(); showScreen('play'); nextQ();
      });
    }
    if (el.btnNext) {
      el.btnNext.addEventListener('click', function() {
        if (autoTimer) { clearTimeout(autoTimer); autoTimer = null; }
        nextQ();
      });
    }
    if (el.refToggle) {
      el.refToggle.addEventListener('click', function() {
        if (el.refBody) {
          el.refBody.classList.toggle('open');
          el.refToggle.textContent = el.refBody.classList.contains('open') ? L.refClose : L.refOpen;
        }
      });
    }

    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
      if (!screens.play || !screens.play.classList.contains('active')) return;
      if (!currentQItem) return;
      var type = currentQItem.qtype;
      if (type !== 'produccion' && e.key >= '1' && e.key <= '4') {
        var btns = el.options ? el.options.querySelectorAll('.game-option') : [];
        var btn  = btns[parseInt(e.key, 10) - 1];
        if (btn && !btn.disabled) btn.click();
      }
      if ((e.key === 'Enter' || e.key === ' ') && el.btnNext && el.btnNext.style.display !== 'none') {
        e.preventDefault(); el.btnNext.click();
      }
    });

    // ── Touch swipe to advance (after answering) ──────────────────
    var swX=0, swY=0, swActive=false, swDelta=0, swCard=null;
    document.addEventListener('touchstart', function(e) {
      if (!currentQItem || e.touches.length > 1) return;
      if (!el.btnNext || el.btnNext.style.display === 'none') return;
      var card = document.querySelector('.game-play');
      if (!card) return;
      swX = e.touches[0].clientX; swY = e.touches[0].clientY;
      swActive = false; swDelta = 0; swCard = card;
      swCard.style.transition = 'none';
    }, { passive: true });
    document.addEventListener('touchmove', function(e) {
      if (!swCard) return;
      var dx = e.touches[0].clientX - swX, dy = e.touches[0].clientY - swY;
      if (!swActive) {
        if (Math.abs(dy) > Math.abs(dx) + 8) { swCard = null; return; }
        if (Math.abs(dx) < 8) return;
        swActive = true;
      }
      e.preventDefault();
      swDelta = dx;
      swCard.style.transform = 'translateX(' + dx + 'px)';
      swCard.style.opacity   = String(Math.max(0.25, 1 - Math.abs(dx) / (window.innerWidth * 0.55)));
    }, { passive: false });
    document.addEventListener('touchend', function() {
      if (!swCard) return;
      var card = swCard; swCard = null;
      if (!swActive || Math.abs(swDelta) < 30) {
        card.style.transition = 'transform .22s ease-out, opacity .22s ease-out';
        card.style.transform = ''; card.style.opacity = '';
        setTimeout(function() { card.style.transition = ''; }, 230);
        return;
      }
      if (swDelta < 0) {
        card.style.transition = 'transform .26s ease-in, opacity .22s ease-in';
        card.style.transform  = 'translateX(' + (-window.innerWidth * 1.3) + 'px) rotate(-18deg)';
        card.style.opacity    = '0';
        setTimeout(nextQ, 270);
      } else {
        card.style.transition = 'transform .22s ease-out, opacity .22s ease-out';
        card.style.transform = ''; card.style.opacity = '';
        setTimeout(function() { card.style.transition = ''; }, 230);
      }
    }, { passive: true });

    // ── Boot ──────────────────────────────────────────────────────
    var hasSaved = loadState();
    if (!hasSaved) freshState();
    renderStart();
    renderReference();
  }

})();
