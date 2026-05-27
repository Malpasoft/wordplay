/* ══════════════════════════════════════════════════════════════════
   WORD PLAY — Chapter Game Engine v2
   ══════════════════════════════════════════════════════════════════

   PEDAGOGICAL DESIGN NOTES
   ─────────────────────────
   The previous engine used a 4-stage linear ladder (Meaning →
   Synonym → Identify → Complete) with simple stage increment/
   decrement. This works but has several weaknesses:
   
   1. FIXED STAGE ORDER — Every item always goes through the same
      4 stages in the same order. Learners who already know Stage 1
      must click through it to reach the more productive stages.
   
   2. NO SPACED REPETITION — Items are re-presented based only on
      miss count weighting, not on time elapsed. True SRS uses
      increasing intervals (1 → 4 → 10 → 30 min → 1 day...).
      We can approximate this within a session.

   3. BINARY CORRECT/WRONG — No partial credit. A hint-assisted
      correct answer scores the same as a spontaneous one (except
      for -5 points). This undermines the hint's pedagogical role.

   4. NO CONFIDENCE DIMENSION — Learners can't signal "I know this"
      to skip stages, which frustrates stronger students.

   5. STAGE REGRESSION ON FIRST MISS — Regressing a stage on one
      wrong answer is punitive and not supported by memory research.
      (Two consecutive misses → regression is more appropriate.)

   NEW DESIGN
   ──────────
   Stages (0-4):
     0 — Receptive: see term + example → choose meaning (4-MCQ)
     1 — Productive: see meaning → choose term (reverse MCQ)
     2 — Contextual: see gapped sentence → choose correct answer
     3 — Generative: see term → choose correct use in context
     4 — MASTERED

   Key changes:
   • "I know this" button on stages 0-1: jumps item to stage 2,
     saves time for confident learners, signals self-assessment
   • Two-miss rule: item only regresses stage after TWO consecutive
     misses on that item (not one)
   • Confidence scoring: 
       Spontaneous correct = 10pts
       Hint-assisted correct = 4pts
       "I know this" then correct at 2 = 8pts
       "I know this" then wrong = regresses back to 0
   • Interval weighting within session:
       Items just answered (< 2 questions ago) = excluded from pool
       Items with misses > 1 = higher weight
       Items at stage 0 with no attempts = medium weight
   • On completion: show mastery map — which items are strong vs
     which are "brittle" (mastered but with many misses along the way)

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
      btnReveal:   q('gBtnReveal'),
      btnKnow:     q('gBtnKnow'),
      btnSaveQuit: q('gBtnSaveQuit'),
      progressBar: q('gProgressBar'),
      progressTxt: q('gProgressTxt'),
      score:       q('gScore'),
      streak:      q('gStreak'),
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

    // ── State ────────────────────────────────────────────────────
    // item state: { id, stage, misses, consecutiveMisses, lastAnswered(questionNum), selfAsserted }
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
      questionNum: 0,       // global question counter for interval logic
    };

    // ── Stage definitions ─────────────────────────────────────────
    const STAGE_DEFS = [
      {
        tag: 'Stage 1 \u2014 Meaning',
        sub: 'What does this term mean?',
        // show term, ask for meaning
        showTerm: (item) => item.term,
        correct: (item) => item.meaning,
        pool: (items) => items.map(i => i.meaning),
        canKnow: true,  // "I know this" available
      },
      {
        tag: 'Stage 2 \u2014 Recognition',
        sub: 'Which term matches this definition?',
        // show meaning, ask for term (reverse)
        showTerm: (item) => item.meaning,
        correct: (item) => item.term,
        pool: (items) => items.map(i => i.term),
        canKnow: true,
      },
      {
        tag: 'Stage 3 \u2014 In context',
        sub: 'Complete the sentence correctly',
        // show gapped sentence, ask for answer
        showTerm: (item) => item.completion
          ? item.completion.replace('______', '\u25a1 \u25a1 \u25a1 \u25a1 \u25a1 \u25a1')
          : item.meaning,
        correct: (item) => item.answer || item.term,
        pool: (items) => items.map(i => i.answer || i.term),
        canKnow: false,
      },
      {
        tag: 'Stage 4 \u2014 Production',
        sub: 'Find a synonym or related term',
        // show term, ask for synonym
        showTerm: (item) => item.term,
        correct: (item) => item.synonym,
        pool: (items) => items.map(i => i.synonym),
        canKnow: false,
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
        items: ITEMS.map(i => ({ id: i.id, stage: 0, misses: 0, consecutiveMisses: 0, lastAnswered: -99, selfAsserted: false })),
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
      Object.entries(screens).forEach(([k, el]) => {
        if (!el) return;
        el.classList.toggle('active', k === name);
      });
    }

    function toast(msg, dur = 2000) {
      if (!el.toast) return;
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
    // Spaced repetition within session:
    //   - Never pick the item answered in the last 2 questions (unless only 1 item)
    //   - Weight by consecutive misses (more misses = higher priority)
    //   - Weight by stage (lower stage = higher priority if multiple same-miss items)
    function nextItem() {
      state.answered = false;
      state.hintUsed = false;
      if (el.feedback) { el.feedback.textContent = ''; el.feedback.className = 'game-feedback'; }
      if (el.example)  { el.example.textContent = ''; el.example.style.display = 'none'; }
      if (el.btnNext)  el.btnNext.style.display = 'none';

      const pool = state.items.filter(i => {
        if (i.stage >= STAGES) return false;
        // Exclude recently answered items (interval spacing), unless no choice
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
        w += i.consecutiveMisses * 3;   // miss weight: urgent review
        w += (STAGES - i.stage) * 0.5;  // stage weight: prefer unmastered
        if (i.selfAsserted) w *= 0.5;   // self-asserted: slightly lower priority
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

      // Stage tag with progress dots
      if (el.modeTag) {
        el.modeTag.textContent = def.tag;
      }
      // Stage dots (persistent element)
      let dotsEl = document.querySelector('.stage-dots');
      if (!dotsEl && el.modeTag) {
        dotsEl = document.createElement('div');
        dotsEl.className = 'stage-dots';
        dotsEl.style.cssText = 'display:flex;gap:5px;margin-top:6px;justify-content:center';
        el.modeTag.insertAdjacentElement('afterend', dotsEl);
      }
      if (dotsEl) {
        dotsEl.innerHTML = Array.from({length: STAGES}, (_, i) => {
          const filled = i <= stage;
          return `<span style="width:10px;height:10px;border-radius:50%;display:inline-block;background:${filled ? 'var(--amber)' : 'var(--hairline)'};border:1.5px solid ${filled ? 'var(--amber)' : 'rgba(26,26,26,0.2)'}"></span>`;
        }).join('');
      }

      // Term display
      const termText = def.showTerm(item);
      if (el.term) {
        if (stage === 2 && item.completion) {
          el.term.innerHTML = item.completion.replace('______', '<span class="game-gap">______</span>');
        } else {
          el.term.textContent = termText;
        }
      }
      if (el.prompt) el.prompt.textContent = def.sub;

      // "I know this" button visibility
      if (el.btnKnow) {
        el.btnKnow.style.display = def.canKnow ? 'inline-flex' : 'none';
      }

      // Build answer options
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

      if (el.btnHint)   { el.btnHint.disabled = false; }
      if (el.btnReveal) { el.btnReveal.disabled = false; }

      updateProgressUI();
    }

    // ── Handle answer ─────────────────────────────────────────────
    function handleAnswer(btn, isReveal = false) {
      if (state.answered) return;
      state.answered = true;

      const item    = getItem(state.currentId);
      const st      = getItemState(state.currentId);
      const def     = STAGE_DEFS[state.currentStage];
      const correct = def.correct(item);
      const userVal = decodeURIComponent(btn.dataset.val);
      const acceptList = (item.accept || []);
      const isCorrect = !isReveal && (userVal === correct || acceptList.includes(userVal));

      // Mark buttons
      el.options.querySelectorAll('.game-option').forEach(b => {
        b.disabled = true;
        const bVal = decodeURIComponent(b.dataset.val);
        if (bVal === correct || (item.accept || []).includes(bVal)) b.classList.add('correct');
        else if (b === btn && !isCorrect) b.classList.add('wrong');
      });
      if (el.btnHint)   el.btnHint.disabled = true;
      if (el.btnReveal) el.btnReveal.disabled = true;
      if (el.btnKnow)   el.btnKnow.disabled = true;
      playTone(isCorrect);

      // Track last answered for interval spacing
      st.lastAnswered = state.questionNum;

      if (isCorrect) {
        // Advance stage
        st.stage = Math.min(st.stage + 1, STAGES);
        st.consecutiveMisses = 0;
        state.streak++;
        if (state.streak > state.bestStreak) state.bestStreak = state.streak;

        // Scoring: hint = 4pts, self-asserted then correct = 8pts, spontaneous = 10pts
        const points = state.hintUsed ? 4 : (st.selfAsserted && state.currentStage === 2 ? 8 : 10);
        state.score += points;

        const feedbackMsg = state.streak >= 3
          ? `Correct! \uD83D\uDD25 ${state.streak} streak`
          : 'Correct!';
        if (el.feedback) { el.feedback.textContent = feedbackMsg; el.feedback.className = 'game-feedback correct'; }
        if (st.stage >= STAGES) {
          // Show mastery toast
          const brittle = st.misses > 2;
          toast(brittle ? `${item.term} mastered \u2014 took some tries!` : `${item.term} mastered!`);
          updateStoreProgress();
        }
      } else {
        // Two-consecutive-miss rule for regression
        st.consecutiveMisses++;
        st.misses++;
        state.streak = 0;

        if (st.selfAsserted) {
          // Self-asserted then wrong: full regression to 0, clear assertion
          st.stage = 0;
          st.selfAsserted = false;
          if (el.feedback) { el.feedback.textContent = `Not quite — the answer is "${correct}". Resetting to Stage 1.`; el.feedback.className = 'game-feedback wrong'; }
        } else if (st.consecutiveMisses >= 2) {
          // Two consecutive misses: regress one stage
          st.stage = Math.max(st.stage - 1, 0);
          const msg = isReveal ? `Answer: "${correct}"` : `Wrong again \u2014 "${correct}". Moving back a stage.`;
          if (el.feedback) { el.feedback.textContent = msg; el.feedback.className = 'game-feedback wrong'; }
        } else {
          // First miss: just show answer, no regression
          const msg = isReveal ? `Answer: "${correct}"` : `Not quite \u2014 the answer is "${correct}"`;
          if (el.feedback) { el.feedback.textContent = msg; el.feedback.className = 'game-feedback wrong'; }
        }
      }

      // Show example sentence
      if (el.example && item.example) {
        el.example.innerHTML = item.example;
        el.example.style.display = 'block';
      }

      if (el.btnNext) el.btnNext.style.display = 'inline-flex';
      updateProgressUI();
      saveState();

      // Auto-complete check
      if (state.items.every(i => i.stage >= STAGES)) {
        state.completed = true;
        setTimeout(() => { updateStoreProgress(); clearState(); renderCompletion(); }, 1400);
      }
    }

    // ── "I know this" button ──────────────────────────────────────
    // Jumps item to Stage 3 (In context) — learner self-asserts knowledge
    // If they then get Stage 3 correct, they score 8pts and advance normally
    // If they get Stage 3 wrong, they regress to Stage 0
    function handleKnowThis() {
      if (state.answered) return;
      const st = getItemState(state.currentId);
      if (!st) return;
      st.stage = 2;           // jump to contextual stage
      st.selfAsserted = true; // flag for scoring/regression
      state.answered = false;
      state.currentStage = 2;
      if (el.feedback) {
        el.feedback.textContent = 'Great \u2014 now prove it in context!';
        el.feedback.className = 'game-feedback';
      }
      renderQuestion();
      toast('Jumped to Stage 3 \u2014 complete the sentence to confirm.');
    }

    // ── Hint ──────────────────────────────────────────────────────
    function showHint() {
      if (state.answered) return;
      state.hintUsed = true;
      const item = getItem(state.currentId);
      const def  = STAGE_DEFS[state.currentStage];
      const correct = def.correct(item);
      // Show first letter of each word
      const hint = correct.split(' ').map(w => w[0] + '\u2026').join(' ');
      if (el.feedback) { el.feedback.textContent = 'Hint: ' + hint; el.feedback.className = 'game-feedback'; }
      if (el.btnHint) el.btnHint.disabled = true;
    }

    // ── Reveal ────────────────────────────────────────────────────
    function reveal() {
      if (state.answered) return;
      const item = getItem(state.currentId);
      const def  = STAGE_DEFS[state.currentStage];
      const correct = def.correct(item);
      const btns = el.options ? el.options.querySelectorAll('.game-option') : [];
      let fakeBtn = null;
      btns.forEach(b => { if (decodeURIComponent(b.dataset.val) === correct) fakeBtn = b; });
      handleAnswer(fakeBtn || btns[0], true);
    }

    // ── Progress UI ───────────────────────────────────────────────
    function updateProgressUI() {
      const mastered = state.items.filter(i => i.stage >= STAGES).length;
      const pct = Math.round((mastered / ITEMS.length) * 100);
      if (el.progressBar) el.progressBar.style.width = pct + '%';
      if (el.progressTxt) el.progressTxt.textContent = mastered + ' / ' + ITEMS.length + ' mastered';
      if (el.score)  el.score.textContent = state.score;
      if (el.streak) el.streak.textContent = state.streak;
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

    // ── Confetti celebration ──────────────────────────────────────
    function triggerConfetti() {
      if (!document.getElementById('cf-kf')) {
        var s = document.createElement('style');
        s.id = 'cf-kf';
        s.textContent = '@keyframes cfFall{to{transform:translateY(105vh) rotate(480deg);opacity:0}}';
        document.head.appendChild(s);
      }
      var colors = ['#C9A050','#4CAF82','#E05A4A','#4AABB8','#F0F0F0','#C9A050'];
      for (var i = 0; i < 32; i++) {
        var p = document.createElement('div');
        var sz = 6 + Math.random() * 6;
        p.style.cssText = 'position:fixed;top:-12px;width:' + sz + 'px;height:' + sz + 'px;border-radius:' + Math.round(Math.random()) + 'px;background:' + colors[Math.floor(Math.random() * colors.length)] + ';left:' + (5 + Math.random() * 90) + '%;animation:cfFall ' + (1.8 + Math.random() * 2.2) + 's ' + (Math.random() * 0.5) + 's ease-in forwards;z-index:999;pointer-events:none';
        document.body.appendChild(p);
        setTimeout(function(el) { if (el.parentNode) el.parentNode.removeChild(el); }, 4500, p);
      }
    }

    // ── Completion screen ─────────────────────────────────────────
    // Mastery map: categorise items as Strong / Brittle / Shaky
    function renderCompletion() {
      if (el.finalScore)  el.finalScore.textContent  = state.score;
      if (el.finalStreak) el.finalStreak.textContent = state.bestStreak;
      const mastered = state.items.filter(i => i.stage >= STAGES).length;
      if (el.finalPct)    el.finalPct.textContent    = Math.round((mastered / ITEMS.length) * 100) + '%';

      // Mastery map
      if (el.masteryMap) {
        const strong   = state.items.filter(i => i.stage >= STAGES && i.misses <= 1);
        const brittle  = state.items.filter(i => i.stage >= STAGES && i.misses > 1);
        const unmastered = state.items.filter(i => i.stage < STAGES);

        let html = '';
        if (strong.length) {
          html += '<div class="mastery-group"><div class="mastery-group-label" style="color:var(--green)">\u2713 Strong (' + strong.length + ')</div>';
          html += strong.map(i => `<span class="mastery-chip strong">${getItem(i.id).term}</span>`).join('');
          html += '</div>';
        }
        if (brittle.length) {
          html += '<div class="mastery-group"><div class="mastery-group-label" style="color:var(--amber)">\u26a0 Mastered but review again (' + brittle.length + ')</div>';
          html += brittle.map(i => `<span class="mastery-chip brittle">${getItem(i.id).term}</span>`).join('');
          html += '</div>';
        }
        if (unmastered.length) {
          html += '<div class="mastery-group"><div class="mastery-group-label" style="color:var(--red)">\u2715 Needs more practice (' + unmastered.length + ')</div>';
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
    if (el.btnNext)          el.btnNext.addEventListener('click',          nextItem);
    if (el.btnHint)          el.btnHint.addEventListener('click',          showHint);
    if (el.btnReveal)        el.btnReveal.addEventListener('click',        reveal);
    if (el.btnKnow)          el.btnKnow.addEventListener('click',          handleKnowThis);
    if (el.btnPlayAgain)     el.btnPlayAgain.addEventListener('click',     () => { freshState(); showScreen('play'); nextItem(); });
    if (el.btnSaveQuit)      el.btnSaveQuit.addEventListener('click',      () => { saveState(); toast('Progress saved'); setTimeout(() => { showScreen('start'); renderStart(); }, 600); });
    if (el.refToggle)        el.refToggle.addEventListener('click',        () => {
      const body = el.refBody;
      if (body) { body.classList.toggle('open'); el.refToggle.textContent = body.classList.contains('open') ? '\u25b2 Reference' : '\u25bc Reference'; }
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', e => {
      if (screens.play && !screens.play.classList.contains('active')) return;
      if (e.key >= '1' && e.key <= '4' && !state.answered) {
        const btns = el.options ? el.options.querySelectorAll('.game-option') : [];
        const btn = btns[parseInt(e.key) - 1];
        if (btn && !btn.disabled) btn.click();
      }
      if ((e.key === 'Enter' || e.key === ' ') && state.answered && el.btnNext && el.btnNext.style.display !== 'none') nextItem();
      if (e.key === 'h' && !state.answered) showHint();
      if (e.key === 'k' && !state.answered) handleKnowThis();
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
