/* ══════════════════════════════════════════════════════════════════
   WORD PLAY — Chapter Game Engine v2
   ══════════════════════════════════════════════════════════════════

   4-stage spaced-repetition mastery game.
   Stages 0-3 = Meaning / Recognition / In-context / Production.
   Stage 4 = MASTERED.

   Two-miss rule: stage regression only after two consecutive misses.
   Auto-advance on correct (1.2 s). Manual Continue on wrong.
   ══════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function playTone(correct) {
    try {
      var ctx = new (window.AudioContext || window.webkitAudioContext)();
      if (correct) {
        [[660,0],[880,0.1]].forEach(function(pair) {
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

  function init() {
    if (!window.GAME_DATA) {
      console.warn('GAME_DATA not defined');
      return;
    }

    const DATA = window.GAME_DATA;
    const ITEMS = DATA.items;
    const STORAGE_KEY = DATA.storageKey || ('game_' + DATA.level + '_' + DATA.chapterId);
    const STAGES = 4;

    // ── Build play screen from a single clean template ────────────
    // This replaces whatever static HTML the game.html has in .game-play,
    // making game.js the single source of truth for the play-card layout.
    (function buildPlayScreen() {
      var play = document.querySelector('#gamePlay .game-play');
      if (!play) return;
      play.innerHTML =
        '<div class="gp-prog"><div class="gp-prog-fill" id="gProgressBar" style="width:0%"></div></div>' +
        '<div class="gp-meta">' +
          '<span class="gp-badge" id="gModeTag"></span>' +
          '<span class="gp-counter">' +
            '<span class="gp-streak" id="gStreakBadge"></span>' +
            '<span id="gProgressTxt">0 / ' + ITEMS.length + '</span>' +
          '</span>' +
        '</div>' +
        '<div class="game-term" id="gTerm"></div>' +
        '<div class="game-prompt" id="gPrompt"></div>' +
        '<div class="game-options" id="gOptions"></div>' +
        '<div class="game-feedback" id="gFeedback"></div>' +
        '<div class="game-example" id="gExample" style="display:none"></div>' +
        '<div class="gp-actions">' +
          '<button id="gBtnHint" class="gp-link" type="button">Need a hint?</button>' +
          '<button id="gBtnNext" class="game-btn primary" style="display:none">Continue</button>' +
        '</div>';
    })();

    // ── DOM refs ─────────────────────────────────────────────────
    function q(id) { return document.getElementById(id); }
    const screens = {
      start:      q('gameStart'),
      play:       q('gamePlay'),
      completion: q('gameCompletion'),
    };
    const el = {
      startMastered:    q('gStartMastered'),
      startTotal:       q('gStartTotal'),
      startLifetime:    q('gStartLifetime'),
      resumeSection:    q('gResumeSection'),
      btnResume:        q('gBtnResume'),
      btnNewFromResume: q('gBtnNewFromResume'),
      btnStart:         q('gBtnStart'),
      modeTag:     q('gModeTag'),
      term:        q('gTerm'),
      prompt:      q('gPrompt'),
      options:     q('gOptions'),
      feedback:    q('gFeedback'),
      example:     q('gExample'),
      btnNext:     q('gBtnNext'),
      btnHint:     q('gBtnHint'),
      streakBadge: q('gStreakBadge'),
      progressBar: q('gProgressBar'),
      progressTxt: q('gProgressTxt'),
      refToggle:   q('gRefToggle'),
      refBody:     q('gRefBody'),
      refList:     q('gRefList'),
      finalScore:   q('gFinalScore'),
      finalStreak:  q('gFinalStreak'),
      finalPct:     q('gFinalPct'),
      masteryMap:   q('gMasteryMap'),
      btnPlayAgain: q('gBtnPlayAgain'),
      toast: q('gToast'),
    };

    var autoAdvanceTimer = null;

    // ── State ────────────────────────────────────────────────────
    let state = {
      items: [],
      score: 0,
      streak: 0,
      bestStreak: 0,
      currentId: null,
      currentStage: 0,
      answered: false,
      hintUsed: false,
      completed: false,
      questionNum: 0,
    };

    // ── Stage definitions ─────────────────────────────────────────
    const STAGE_DEFS = [
      {
        tag: 'Stage 1 — Meaning',
        sub: 'What does this term mean?',
        showTerm: (item) => item.term,
        correct: (item) => item.meaning,
        pool: (items) => items.map(i => i.meaning),
      },
      {
        tag: 'Stage 2 — Recognition',
        sub: 'Which term matches this definition?',
        showTerm: (item) => item.meaning,
        correct: (item) => item.term,
        pool: (items) => items.map(i => i.term),
      },
      {
        tag: 'Stage 3 — In context',
        sub: 'Complete the sentence correctly',
        showTerm: (item) => item.completion
          ? item.completion.replace('______', '□ □ □ □ □ □')
          : item.meaning,
        correct: (item) => item.answer || item.term,
        pool: (items) => items.map(i => i.answer || i.term),
      },
      {
        tag: 'Stage 4 — Production',
        sub: 'Find a synonym or related term',
        showTerm: (item) => item.term,
        correct: (item) => item.synonym,
        pool: (items) => items.map(i => i.synonym),
      },
    ];

    // ── Persistence ──────────────────────────────────────────────
    function saveState() {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify({
          items: state.items,
          score: state.score,
          streak: state.streak,
          bestStreak: state.bestStreak,
          currentId: state.currentId,
          currentStage: state.currentStage,
          completed: state.completed,
          questionNum: state.questionNum,
        }));
      } catch (e) {}
    }

    function loadState() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (!raw) return false;
        const saved = JSON.parse(raw);
        const ids = new Set(ITEMS.map(i => i.id));
        saved.items = (saved.items || []).filter(i => ids.has(i.id));
        if (saved.items.length === 0) return false;
        Object.assign(state, saved);
        return true;
      } catch (e) { return false; }
    }

    function clearState() {
      try { localStorage.removeItem(STORAGE_KEY); } catch (e) {}
    }

    function updateStoreProgress() {
      if (!window.FCEStore || !DATA.chapterId || !DATA.level) return;
      const mastered = state.items.filter(i => i.stage >= STAGES).length;
      if (mastered > 0) FCEStore.saveGameResult(DATA.chapterId, mastered, ITEMS.length);
    }

    function freshState() {
      state = {
        items: ITEMS.map(i => ({ id: i.id, stage: 0, misses: 0, consecutiveMisses: 0, lastAnswered: -99 })),
        score: 0, streak: 0, bestStreak: 0,
        currentId: null, currentStage: 0,
        answered: false, hintUsed: false, completed: false,
        questionNum: 0,
      };
    }

    // ── Helpers ──────────────────────────────────────────────────
    function shuffle(arr) {
      const a = [...arr];
      for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
      }
      return a;
    }

    function getItem(id)      { return ITEMS.find(i => i.id === id); }
    function getItemState(id) { return state.items.find(i => i.id === id); }

    function showScreen(name) {
      Object.entries(screens).forEach(([k, scr]) => {
        if (!scr) return;
        scr.classList.toggle('active', k === name);
      });
    }

    function toast(msg, dur) {
      if (!el.toast) return;
      dur = dur || 2000;
      el.toast.textContent = msg;
      el.toast.classList.add('show');
      setTimeout(() => el.toast.classList.remove('show'), dur);
    }

    // ── Start screen ─────────────────────────────────────────────
    function renderStart() {
      const mastered = state.items.filter(i => i.stage >= STAGES).length;
      if (el.startMastered) el.startMastered.textContent = mastered;
      if (el.startTotal)    el.startTotal.textContent = ITEMS.length;
      if (el.startLifetime && window.FCEStore && DATA.level && DATA.chapterId) {
        try {
          var lv = FCEStore.getLevel(DATA.level);
          var key = 'wordplay_game_' + DATA.chapterId;
          var lt = (lv.results || {})[key];
          el.startLifetime.textContent = lt ? lt.mastered + '/' + lt.total + ' (' + lt.pct + '%)' : '—';
        } catch(e) { if (el.startLifetime) el.startLifetime.textContent = '—'; }
      }
      const hasSaved = state.items.some(i => i.stage > 0 || i.misses > 0) && !state.completed;
      if (el.resumeSection) el.resumeSection.style.display = hasSaved ? 'block' : 'none';
      showScreen('start');
    }

    // ── Pick next item ─────────────────────────────────────────────
    function nextItem() {
      if (autoAdvanceTimer) { clearTimeout(autoAdvanceTimer); autoAdvanceTimer = null; }

      // Reset card and slide in from right (handles post-swipe invisible state too)
      var playCard = document.querySelector('.game-play');
      if (playCard) {
        playCard.style.transition = 'none';
        playCard.style.transform = 'translateX(28px)';
        playCard.style.opacity = '0';
        void playCard.offsetHeight;
        playCard.style.transition = 'transform 0.2s ease-out, opacity 0.18s ease-out';
        playCard.style.transform = '';
        playCard.style.opacity = '';
        setTimeout(function() { playCard.style.transition = ''; }, 220);
      }

      state.answered = false;
      state.hintUsed = false;
      if (el.feedback) { el.feedback.textContent = ''; el.feedback.className = 'game-feedback'; }
      if (el.example)  { el.example.textContent = ''; el.example.style.display = 'none'; }
      if (el.btnNext)  el.btnNext.style.display = 'none';

      const pool = state.items.filter(i => {
        if (i.stage >= STAGES) return false;
        const recentlyAnswered = (state.questionNum - i.lastAnswered) < 2;
        const poolSize = state.items.filter(j => j.stage < STAGES).length;
        if (recentlyAnswered && poolSize > 1) return false;
        return true;
      });

      if (pool.length === 0) {
        state.completed = true;
        updateStoreProgress();
        clearState();
        renderCompletion();
        return;
      }

      // Weighted selection: prioritise high consecutive misses, then low stage
      const weighted = pool.map(i => {
        let w = 1;
        w += i.consecutiveMisses * 3;
        w += (STAGES - i.stage) * 0.5;
        return { i, w };
      });
      const total = weighted.reduce((s, x) => s + x.w, 0);
      let rand = Math.random() * total;
      let chosen = weighted[0].i;
      for (const x of weighted) {
        rand -= x.w;
        if (rand <= 0) { chosen = x.i; break; }
      }

      state.currentId = chosen.id;
      state.currentStage = chosen.stage;
      state.questionNum++;
      renderQuestion();
    }

    // ── Render question ───────────────────────────────────────────
    function renderQuestion() {
      const item = getItem(state.currentId);
      const stage = state.currentStage;
      const def = STAGE_DEFS[stage];

      if (el.modeTag) el.modeTag.textContent = def.tag;

      if (el.term) {
        if (stage === 2 && item.completion) {
          el.term.innerHTML = item.completion.replace('______', '<span class="game-gap">______</span>');
        } else {
          el.term.textContent = def.showTerm(item);
        }
      }
      if (el.prompt) el.prompt.textContent = def.sub;

      const correct = def.correct(item);
      const allAnswers = def.pool(ITEMS).filter(x => x && x !== correct);
      const distractors = shuffle(allAnswers).slice(0, 3);
      const options = shuffle([correct, ...distractors]);

      if (el.options) {
        el.options.innerHTML = options.map((opt, i) =>
          `<button class="game-option" data-val="${encodeURIComponent(opt)}" data-idx="${i}">${opt}</button>`
        ).join('');
        el.options.querySelectorAll('.game-option').forEach(btn => {
          btn.addEventListener('click', () => handleAnswer(btn));
        });
      }

      if (el.btnHint) el.btnHint.disabled = false;

      updateProgressUI();
    }

    // ── Handle answer ─────────────────────────────────────────────
    function handleAnswer(btn, isReveal) {
      if (state.answered) return;
      state.answered = true;
      isReveal = !!isReveal;

      const item    = getItem(state.currentId);
      const st      = getItemState(state.currentId);
      const def     = STAGE_DEFS[state.currentStage];
      const correct = def.correct(item);
      const userVal = decodeURIComponent(btn.dataset.val);
      const acceptList = (item.accept || []);
      const isCorrect = !isReveal && (userVal === correct || acceptList.includes(userVal));

      el.options.querySelectorAll('.game-option').forEach(b => {
        b.disabled = true;
        const bVal = decodeURIComponent(b.dataset.val);
        if (bVal === correct || (item.accept || []).includes(bVal)) b.classList.add('correct');
        else if (b === btn && !isCorrect) b.classList.add('wrong');
      });
      if (el.btnHint) el.btnHint.disabled = true;
      playTone(isCorrect);

      st.lastAnswered = state.questionNum;

      if (isCorrect) {
        st.stage = Math.min(st.stage + 1, STAGES);
        st.consecutiveMisses = 0;
        state.streak++;
        if (state.streak > state.bestStreak) state.bestStreak = state.streak;

        const points = state.hintUsed ? 4 : 10;
        state.score += points;

        const feedbackMsg = state.streak >= 3
          ? 'Correct! ◆ ' + state.streak + ' streak'
          : 'Correct!';
        if (el.feedback) { el.feedback.textContent = feedbackMsg; el.feedback.className = 'game-feedback correct'; }
        if (st.stage >= STAGES) {
          const brittle = st.misses > 2;
          toast(brittle ? item.term + ' mastered — took some tries!' : item.term + ' mastered!');
          updateStoreProgress();
        }
      } else {
        st.consecutiveMisses++;
        st.misses++;
        state.streak = 0;

        if (st.consecutiveMisses >= 2) {
          st.stage = Math.max(st.stage - 1, 0);
          const msg = isReveal ? 'Answer: "' + correct + '"' : 'Wrong again — "' + correct + '". Moving back a stage.';
          if (el.feedback) { el.feedback.textContent = msg; el.feedback.className = 'game-feedback wrong'; }
        } else {
          const msg = isReveal ? 'Answer: "' + correct + '"' : 'Not quite — the answer is "' + correct + '"';
          if (el.feedback) { el.feedback.textContent = msg; el.feedback.className = 'game-feedback wrong'; }
        }
      }

      if (el.example && item.example) {
        el.example.innerHTML = item.example;
        el.example.style.display = 'block';
      }

      if (state.items.every(i => i.stage >= STAGES)) {
        state.completed = true;
        updateProgressUI();
        saveState();
        setTimeout(() => { updateStoreProgress(); clearState(); renderCompletion(); }, 1400);
        return;
      }

      if (isCorrect) {
        if (el.btnNext) el.btnNext.style.display = 'none';
        autoAdvanceTimer = setTimeout(function() {
          autoAdvanceTimer = null;
          nextItem();
        }, 1200);
      } else {
        if (el.btnNext) el.btnNext.style.display = 'inline-flex';
      }
      updateProgressUI();
      saveState();
    }

    // ── Hint ──────────────────────────────────────────────────────
    function showHint() {
      if (state.answered) return;
      state.hintUsed = true;
      const item = getItem(state.currentId);
      const def  = STAGE_DEFS[state.currentStage];
      const correct = def.correct(item);
      const hint = correct.split(' ').map(w => w[0] + '…').join(' ');
      if (el.feedback) { el.feedback.textContent = 'Hint: ' + hint; el.feedback.className = 'game-feedback'; }
      if (el.btnHint) el.btnHint.disabled = true;
    }

    // ── Progress UI ───────────────────────────────────────────────
    function updateProgressUI() {
      const mastered = state.items.filter(i => i.stage >= STAGES).length;
      const pct = Math.round((mastered / ITEMS.length) * 100);
      if (el.progressBar) el.progressBar.style.width = pct + '%';
      if (el.progressTxt) el.progressTxt.textContent = mastered + ' / ' + ITEMS.length;
      if (el.streakBadge) el.streakBadge.textContent = state.streak >= 3 ? '◆ ' + state.streak + '  ' : '';
      renderReference();
    }

    // ── Reference panel ───────────────────────────────────────────
    function renderReference() {
      if (!el.refList) return;
      el.refList.innerHTML = ITEMS.map(item => {
        const st = getItemState(item.id);
        const stage = st ? st.stage : 0;
        const brittle = st && st.misses > 2 && stage >= STAGES;
        const pips = Array.from({ length: STAGES }, (_, i) =>
          `<div class="ref-stage-pip ${i < stage ? (brittle ? 'filled-brittle' : 'filled') : ''}"></div>`
        ).join('');
        return `<div class="game-ref-item">
          <span class="ref-term">${item.term}</span>
          <div class="ref-stage-track">${pips}</div>
          <div class="ref-def">${item.meaning}</div>
          <div class="ref-ex">${item.example || ''}</div>
        </div>`;
      }).join('');
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
      for (var i = 0; i < 32; i++) {
        var p = document.createElement('div');
        var sz = 6 + Math.random() * 6;
        p.style.cssText = 'position:fixed;top:-12px;width:' + sz + 'px;height:' + sz + 'px;border-radius:' + Math.round(Math.random()) + 'px;background:' + colors[Math.floor(Math.random() * colors.length)] + ';left:' + (5 + Math.random() * 90) + '%;animation:cfFall ' + (1.8 + Math.random() * 2.2) + 's ' + (Math.random() * 0.5) + 's ease-in forwards;z-index:999;pointer-events:none';
        document.body.appendChild(p);
        setTimeout(function(el) { if (el.parentNode) el.parentNode.removeChild(el); }, 4500, p);
      }
    }

    // ── Completion screen ─────────────────────────────────────────
    function renderCompletion() {
      if (el.finalScore)  el.finalScore.textContent  = state.score;
      if (el.finalStreak) el.finalStreak.textContent = state.bestStreak;
      const mastered = state.items.filter(i => i.stage >= STAGES).length;
      if (el.finalPct) el.finalPct.textContent = Math.round((mastered / ITEMS.length) * 100) + '%';

      if (el.masteryMap) {
        const strong     = state.items.filter(i => i.stage >= STAGES && i.misses <= 1);
        const brittle    = state.items.filter(i => i.stage >= STAGES && i.misses > 1);
        const unmastered = state.items.filter(i => i.stage < STAGES);

        let html = '';
        if (strong.length) {
          html += '<div class="mastery-group"><div class="mastery-group-label" style="color:var(--green)">Strong (' + strong.length + ')</div>';
          html += strong.map(i => `<span class="mastery-chip strong">${getItem(i.id).term}</span>`).join('');
          html += '</div>';
        }
        if (brittle.length) {
          html += '<div class="mastery-group"><div class="mastery-group-label" style="color:var(--amber)">Mastered — review again (' + brittle.length + ')</div>';
          html += brittle.map(i => `<span class="mastery-chip brittle">${getItem(i.id).term}</span>`).join('');
          html += '</div>';
        }
        if (unmastered.length) {
          html += '<div class="mastery-group"><div class="mastery-group-label" style="color:var(--red)">Needs more practice (' + unmastered.length + ')</div>';
          html += unmastered.map(i => `<span class="mastery-chip unmastered">${getItem(i.id).term}</span>`).join('');
          html += '</div>';
        }
        el.masteryMap.innerHTML = html;
      }

      showScreen('completion');
      setTimeout(triggerConfetti, 400);
    }

    // ── Event listeners ───────────────────────────────────────────
    if (el.btnStart)         el.btnStart.addEventListener('click',         () => { freshState(); saveState(); showScreen('play'); nextItem(); });
    if (el.btnResume)        el.btnResume.addEventListener('click',        () => { showScreen('play'); nextItem(); });
    if (el.btnNewFromResume) el.btnNewFromResume.addEventListener('click', () => { freshState(); saveState(); showScreen('play'); nextItem(); });
    if (el.btnNext)          el.btnNext.addEventListener('click',          function() {
      if (autoAdvanceTimer) { clearTimeout(autoAdvanceTimer); autoAdvanceTimer = null; }
      nextItem();
    });
    if (el.btnHint)          el.btnHint.addEventListener('click',          showHint);
    if (el.btnPlayAgain)     el.btnPlayAgain.addEventListener('click',     () => { freshState(); showScreen('play'); nextItem(); });
    if (el.refToggle)        el.refToggle.addEventListener('click',        () => {
      const body = el.refBody;
      if (body) { body.classList.toggle('open'); el.refToggle.textContent = body.classList.contains('open') ? '▲ Reference' : '▼ Reference'; }
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', e => {
      if (screens.play && !screens.play.classList.contains('active')) return;
      if (e.key >= '1' && e.key <= '4' && !state.answered) {
        const btns = el.options ? el.options.querySelectorAll('.game-option') : [];
        const btn = btns[parseInt(e.key) - 1];
        if (btn && !btn.disabled) btn.click();
      }
      if ((e.key === 'Enter' || e.key === ' ') && state.answered && el.btnNext && el.btnNext.style.display !== 'none') {
        if (autoAdvanceTimer) { clearTimeout(autoAdvanceTimer); autoAdvanceTimer = null; }
        nextItem();
      }
      if (e.key === 'h' && !state.answered) showHint();
    });

    // ── Swipe to advance (after answering) ────────────────────────
    var swStartX=0, swStartY=0, swActive=false, swDelta=0, swCard=null;

    document.addEventListener('touchstart', function(e) {
      if (!state.answered || state.completed || e.touches.length > 1) return;
      var card = document.querySelector('.game-play');
      if (!card) return;
      swStartX = e.touches[0].clientX;
      swStartY = e.touches[0].clientY;
      swActive = false; swDelta = 0;
      swCard = card;
      swCard.style.transition = 'none';
    }, { passive: true });

    document.addEventListener('touchmove', function(e) {
      if (!swCard) return;
      var dx = e.touches[0].clientX - swStartX;
      var dy = e.touches[0].clientY - swStartY;
      if (!swActive) {
        if (Math.abs(dy) > Math.abs(dx) + 8) { swCard = null; return; }
        if (Math.abs(dx) < 8) return;
        swActive = true;
      }
      e.preventDefault();
      swDelta = dx;
      var fade = 1 - Math.min(1, Math.abs(dx) / (window.innerWidth * 0.55));
      swCard.style.transform = 'translateX(' + dx + 'px)';
      swCard.style.opacity = Math.max(0.25, fade);
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
        card.style.transform = 'translateX(' + (-window.innerWidth * 1.3) + 'px) rotate(-18deg)';
        card.style.opacity = '0';
        setTimeout(nextItem, 270);
      } else {
        card.style.transition = 'transform .22s ease-out, opacity .22s ease-out';
        card.style.transform = ''; card.style.opacity = '';
        setTimeout(function() { card.style.transition = ''; }, 230);
      }
    }, { passive: true });

    // ── Boot ──────────────────────────────────────────────────────
    const hasSaved = loadState();
    if (!hasSaved) freshState();
    renderStart();
    renderReference();
  }

})();
