// ══════════════════════════════════════════════════════════════════
// worksheet.js v2 — question-by-question quiz with 3 lives
// Reads questions from existing form HTML + window.ANSWERS/EXPLANATIONS
// Per-chapter pages need no changes — data API is unchanged.
// ══════════════════════════════════════════════════════════════════

(function () {
  'use strict';

  // ── Language detection (via i18n module) ─────────────────────────
  // window.i18n.isSpanish() checks LEVEL or html lang attribute
  var isEs = window.i18n ? window.i18n.isSpanish(window.LEVEL) : ((window.LEVEL || '').indexOf('es-') === 0 || document.documentElement.lang === 'es');
  var getString = window.i18n ? window.i18n.getString : function(key) { return key; };

  var L = {
    check:       getString('ws_check'),
    next:        getString('ws_next'),
    correct:     getString('ws_correct'),
    wrong:       getString('ws_wrong'),
    correctAns:  getString('ws_correctAns'),
    remaining:   getString('ws_remaining'),
    typeHere:    getString('ws_typeHere'),
    mcLabel:     getString('ws_mcLabel'),
    fillLabel:   getString('ws_fillLabel'),
    transLabel:  getString('ws_transLabel'),
    prevBest:    getString('ws_prevBest'),
    completed:   getString('ws_completed'),
    wellDone:    getString('ws_wellDone'),
    keepGoing:   getString('ws_keepGoing'),
    noLives:     getString('ws_noLives'),
    firstPass:   getString('ws_firstPass'),
    tryAgain:    getString('ws_tryAgain'),
    gameBtn:     getString('ws_gameBtn'),
    seeResults:  getString('ws_seeResults'),
    back:        getString('ws_back'),
  };

  // ── Helpers ──────────────────────────────────────────────────────
  function norm(s) {
    return (s || '').toLowerCase().trim()
      .replace(/[.!?,;:]$/g, '')
      .replace(/\s+/g, ' ')
      .replace(/[‘’`]/g, "'")
      .replace(/[“”]/g, '"');
  }
  function isTextCorrect(answerObj, userVal) {
    if (!answerObj) return false;
    var u = norm(userVal);
    if (!u) return false;
    if (u === norm(answerObj.answer)) return true;
    return (answerObj.accept || []).some(function (a) { return u === norm(a); });
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c];
    });
  }
  function shuffle(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = arr[i]; arr[i] = arr[j]; arr[j] = t;
    }
    return arr;
  }

  // ── Extract questions from existing HTML form ────────────────────
  var questions = [];
  var sectionMeta = {};

  document.querySelectorAll('section.exercise').forEach(function (section) {
    var sId = section.id;
    var titleEl = section.querySelector('.ex-title');
    sectionMeta[sId] = { title: titleEl ? titleEl.textContent.trim() : sId, qKeys: [] };

    section.querySelectorAll('.q').forEach(function (qEl) {
      var mcGroup   = qEl.querySelector('.choice-group');
      var textInput = qEl.querySelector('input[type="text"]');
      var qTextEl   = qEl.querySelector('.q-text');
      var srcEl     = qEl.querySelector('.traduce-src');
      var qText     = qTextEl ? qTextEl.textContent.trim() : '';
      var srcText   = srcEl   ? srcEl.textContent.trim()   : '';
      var q         = null;

      if (mcGroup) {
        var qKey = mcGroup.dataset.q;
        q = {
          type: 'mc', qKey: qKey, sectionId: sId,
          text: qText,
          options: Array.from(mcGroup.querySelectorAll('.choice-btn')).map(function (b) { return b.dataset.value; }),
          correct: mcGroup.dataset.answer,
          accept: [],
        };
      } else if (textInput) {
        var qKey2 = textInput.dataset.q;
        var ans   = (window.ANSWERS || {})[qKey2] || {};
        q = {
          type: srcText ? 'translate' : 'fill', qKey: qKey2, sectionId: sId,
          text: srcText || qText,
          correct: ans.answer || '',
          accept: ans.accept || [],
        };
      }

      if (q) {
        if (window.EXPLANATIONS && window.EXPLANATIONS[q.qKey]) q.explanation = window.EXPLANATIONS[q.qKey];
        questions.push(q);
        sectionMeta[sId].qKeys.push(q.qKey);
      }
    });
  });

  // ── Error boundary: show message if no questions found ────────────
  if (!questions.length) {
    var msgEl = document.createElement('div');
    msgEl.style.cssText = 'padding:20px;background:var(--paper);border:1px solid var(--muted);border-radius:8px;color:var(--ink);font-family:var(--font-sans);line-height:1.5;margin:40px 20px;max-width:500px';
    msgEl.innerHTML = '<strong>Worksheet Error:</strong> No questions found on this page. The worksheet may not be configured correctly.<br><br><a href="index.html" style="color:var(--amber);text-decoration:none">← Back to chapter</a>';
    var container = document.querySelector('.container') || document.body;
    container.insertBefore(msgEl, container.firstChild);
    return;
  }

  // ── Hide legacy form + results panel ────────────────────────────
  var formEl   = document.getElementById('worksheet');
  var oldRes   = document.getElementById('results');
  if (formEl)  formEl.style.display  = 'none';
  if (oldRes)  oldRes.style.display  = 'none';

  // ── Quiz state ───────────────────────────────────────────────────
  var MAX_LIVES     = 3;
  var queue         = questions.slice();
  var lives         = MAX_LIVES;
  var totalQ        = questions.length;
  var answeredQ     = 0;           // questions correctly answered (removed from queue)
  var firstPassOK   = 0;           // correct on first attempt ever
  var seenOnce      = {};          // qKey → true once shown
  var perSection    = {};
  questions.forEach(function (q) {
    if (!perSection[q.sectionId]) perSection[q.sectionId] = { correct: 0, total: 0 };
    perSection[q.sectionId].total++;
  });
  var currentQ  = null;
  var checked   = false;
  var autoTimer = null;

  // ── Inject styles ────────────────────────────────────────────────
  var css = document.createElement('style');
  css.textContent = [
    '#wsq{max-width:720px;margin:0 auto;padding:0 20px 80px}',
    '#wsq-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;font-family:var(--font-sans);font-size:.78rem}',
    '#wsq-counter{color:var(--muted);font-weight:600}',
    '#wsq-lives{display:flex;gap:4px}',
    '.wsq-heart{display:inline-flex;align-items:center;transition:opacity .2s;color:#e05a4a}',
    'body.dark .wsq-heart{color:#f08070}',
    '.wsq-heart.lost{opacity:.18;color:var(--muted)}',
    '#wsq-bar{height:4px;background:var(--hairline);border-radius:2px;margin-bottom:20px;overflow:hidden}',
    '#wsq-bar-fill{height:100%;background:var(--amber);border-radius:2px;transition:width .35s}',
    '#wsq-card{background:var(--paper);border:1.5px solid var(--hairline);border-radius:10px;padding:28px 24px;margin-bottom:14px;transition:border-color .25s,background .25s}',
    '#wsq-card.ok{border-color:var(--green);background:rgba(46,125,82,.04)}',
    '#wsq-card.bad{border-color:var(--amber);background:rgba(184,134,11,.04)}',
    'body.dark #wsq-card{background:#1a1a1a;border-color:rgba(255,255,255,.1)}',
    'body.dark #wsq-card.ok{background:rgba(76,175,130,.07)}',
    'body.dark #wsq-card.bad{background:rgba(201,160,80,.07)}',
    '#wsq-qtype{font-family:var(--font-sans);font-size:.58rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--amber);margin-bottom:8px}',
    '#wsq-qtext{font-family:Georgia,serif;font-size:1.08rem;font-weight:700;color:var(--ink);line-height:1.45;margin-bottom:18px}',
    'body.dark #wsq-qtext{color:#f0f0f0}',
    '#wsq-opts{display:flex;flex-direction:column;gap:8px}',
    '.wsq-opt{padding:11px 16px;border:1.5px solid var(--hairline);border-radius:6px;background:var(--paper);color:var(--ink);font-family:var(--font-sans);font-size:.9rem;cursor:pointer;text-align:left;transition:border-color .15s,background .15s;width:100%}',
    '.wsq-opt:hover:not(:disabled){border-color:var(--amber);background:rgba(184,134,11,.04)}',
    '.wsq-opt.sel{border-color:var(--amber);background:rgba(184,134,11,.08);font-weight:700}',
    '.wsq-opt.right{border-color:var(--green);background:rgba(46,125,82,.07);font-weight:700;color:var(--green)}',
    '.wsq-opt.miss{border-color:var(--red);opacity:.7}',
    'body.dark .wsq-opt{background:#1a1a1a;color:#f0f0f0;border-color:rgba(255,255,255,.15)}',
    'body.dark .wsq-opt.sel{background:rgba(201,160,80,.12);border-color:var(--amber)}',
    'body.dark .wsq-opt.right{background:rgba(76,175,130,.12);color:var(--green)}',
    '#wsq-fill-wrap{display:flex;flex-direction:column;gap:8px}',
    '#wsq-fill{padding:10px 14px;font-family:var(--font-sans);font-size:.95rem;border:1.5px solid var(--hairline);border-radius:6px;background:var(--paper);color:var(--ink);box-sizing:border-box;width:100%;max-width:420px}',
    '#wsq-fill:focus{outline:none;border-color:var(--amber)}',
    'body.dark #wsq-fill{background:#1a1a1a;color:#f0f0f0;border-color:rgba(255,255,255,.2)}',
    '#wsq-fb{margin-top:10px;font-family:var(--font-sans);font-size:.88rem;font-weight:700;display:none}',
    '#wsq-fb.ok{color:var(--green)}',
    '#wsq-fb.bad{color:var(--red)}',
    '#wsq-expl{margin-top:12px;padding:10px 14px;background:rgba(184,134,11,.08);border-left:3px solid var(--amber);font-family:var(--font-sans);font-size:.8rem;color:var(--ink);line-height:1.55;border-radius:0 4px 4px 0;display:none}',
    'body.dark #wsq-expl{background:rgba(201,160,80,.1);color:#e0e0e0}',
    '#wsq-btns{display:flex;gap:10px;margin-top:16px;align-items:center}',
    '#wsq-check{padding:10px 26px;background:var(--ink);color:var(--paper);font-family:var(--font-sans);font-size:.76rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;border:0;border-radius:4px;cursor:pointer;transition:opacity .15s}',
    '#wsq-check:disabled{opacity:.3;cursor:default}',
    'body.dark #wsq-check{background:#e8e8e8;color:#111}',
    '#wsq-next{padding:10px 26px;background:var(--amber);color:#1A1A1A;font-family:var(--font-sans);font-size:.76rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;border:0;border-radius:4px;cursor:pointer;display:none}',
    '#wsq-done{max-width:720px;margin:0 auto;padding:0 20px 80px}',
    '#wsq-done-card{text-align:center;padding:36px 24px;background:var(--cream-deep);border:1.5px solid var(--hairline);border-radius:10px}',
    'body.dark #wsq-done-card{background:#1a1a1a;border-color:rgba(255,255,255,.1)}',
    '#wsq-prev{display:flex;align-items:center;gap:10px;padding:10px 16px;margin-bottom:20px;background:var(--cream-deep);border-radius:6px;font-family:var(--font-sans);font-size:.8rem;color:var(--muted)}',
    'body.dark #wsq-prev{background:#1a1a1a;border:1px solid rgba(255,255,255,.08)}',
  ].join('');
  document.head.appendChild(css);

  // ── Build quiz HTML ──────────────────────────────────────────────
  var quiz = document.createElement('div');
  quiz.id = 'wsq';
  quiz.innerHTML = [
    '<div id="wsq-bar"><div id="wsq-bar-fill" style="width:0%"></div></div>',
    '<div id="wsq-top">',
      '<span id="wsq-counter"></span>',
      '<div id="wsq-lives"></div>',
    '</div>',
    '<div id="wsq-card">',
      '<div id="wsq-qtype"></div>',
      '<div id="wsq-qtext"></div>',
      '<div id="wsq-opts"></div>',
      '<div id="wsq-fill-wrap" style="display:none">',
        '<input id="wsq-fill" type="text" autocomplete="off" spellcheck="false">',
      '</div>',
      '<div id="wsq-fb"></div>',
      '<div id="wsq-expl"></div>',
    '</div>',
    '<div id="wsq-btns">',
      '<button id="wsq-check" disabled>' + L.check + '</button>',
      '<button id="wsq-next">' + L.next + ' &#8594;</button>',
    '</div>',
  ].join('');

  // Previous best banner
  try {
    if (window.FCEStore && window.CHAPTER_ID && window.LEVEL) {
      var pg = JSON.parse(localStorage.getItem('wordplay_progress') || '{}');
      var sv = pg[window.LEVEL] && pg[window.LEVEL][window.CHAPTER_ID];
      if (sv && sv.pct) {
        var pb = document.createElement('div');
        pb.id = 'wsq-prev';
        var pc = sv.pct >= 80 ? 'var(--green)' : sv.pct >= 50 ? 'var(--amber)' : 'var(--red)';
        pb.innerHTML = '<span>' + L.prevBest + '</span><strong style="color:' + pc + ';font-size:.95rem">' + sv.pct + '%</strong>';
        quiz.insertBefore(pb, quiz.firstChild);
      }
    }
  } catch (e) {}

  var formParent = formEl ? formEl.parentNode : (document.querySelector('.container') || document.body);
  formParent.insertBefore(quiz, formEl || null);

  // ── DOM refs ─────────────────────────────────────────────────────
  var $ = function (id) { return document.getElementById(id); };
  var elCounter = $('wsq-counter');
  var elLives   = $('wsq-lives');
  var elBarFill = $('wsq-bar-fill');
  var elCard    = $('wsq-card');
  var elQType   = $('wsq-qtype');
  var elQText   = $('wsq-qtext');
  var elOpts    = $('wsq-opts');
  var elFillWr  = $('wsq-fill-wrap');
  var elInput   = document.querySelector('#wsq-fill-wrap > input');
  var elFb      = $('wsq-fb');
  var elExpl    = $('wsq-expl');
  var elCheck   = $('wsq-check');
  var elNext    = $('wsq-next');

  // ── Render lives ─────────────────────────────────────────────────
  function renderLives() {
    elLives.innerHTML = '';
    for (var i = 0; i < MAX_LIVES; i++) {
      var h = document.createElement('span');
      h.className = 'wsq-heart' + (i >= lives ? ' lost' : '');
      h.innerHTML = '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="currentColor" d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>';
      elLives.appendChild(h);
    }
  }

  // ── Update header ────────────────────────────────────────────────
  function updateHeader() {
    elCounter.textContent = (totalQ - answeredQ) + ' ' + L.remaining;
    if (elBarFill) elBarFill.style.width = Math.round((answeredQ / totalQ) * 100) + '%';
    renderLives();
  }

  // ── Show question ────────────────────────────────────────────────
  function showQ(q) {
    currentQ = q;
    checked  = false;
    if (autoTimer) { clearTimeout(autoTimer); autoTimer = null; }

    elCard.className = '';
    elFb.style.display   = 'none';
    elExpl.style.display = 'none';
    elCheck.style.display = '';
    elNext.style.display = 'none';
    elCheck.disabled = true;
    elNext.textContent = L.next + ' →';

    elQType.textContent = q.type === 'mc' ? L.mcLabel : (q.type === 'translate' ? L.transLabel : L.fillLabel);
    elQText.innerHTML   = esc(q.text);

    if (q.type === 'mc') {
      elOpts.style.display  = '';
      elFillWr.style.display = 'none';
      var opts = shuffle(q.options.slice());
      elOpts.innerHTML = opts.map(function (o) {
        return '<button type="button" class="wsq-opt" data-v="' + esc(o) + '">' + esc(o) + '</button>';
      }).join('');
      elOpts.querySelectorAll('.wsq-opt').forEach(function (btn) {
        btn.addEventListener('click', function () {
          if (checked) return;
          elOpts.querySelectorAll('.wsq-opt').forEach(function (b) { b.classList.remove('sel'); });
          this.classList.add('sel');
          elCheck.disabled = false;
        });
      });
    } else {
      elOpts.style.display   = 'none';
      elFillWr.style.display = '';
      elInput.value    = '';
      elInput.disabled = false;
      setTimeout(function () { elInput.focus(); }, 60);
      elInput.oninput   = function () { elCheck.disabled = !elInput.value.trim(); };
      elInput.onkeydown = function (e) { if (e.key === 'Enter' && !elCheck.disabled) elCheck.click(); };
    }

    updateHeader();
  }

  // ── Check ────────────────────────────────────────────────────────
  function doCheck() {
    if (checked || !currentQ) return;
    checked = true;
    var q = currentQ;
    var correct = false;
    var selBtn  = null;

    if (q.type === 'mc') {
      selBtn  = elOpts.querySelector('.wsq-opt.sel');
      correct = selBtn && selBtn.dataset.v === q.correct;
      elOpts.querySelectorAll('.wsq-opt').forEach(function (btn) {
        btn.disabled = true;
        if (btn.dataset.v === q.correct) btn.classList.add('right');
        else if (btn === selBtn && !correct) btn.classList.add('miss');
      });
    } else {
      correct = isTextCorrect({ answer: q.correct, accept: q.accept }, elInput.value);
      elInput.disabled = true;
    }

    elCard.className = correct ? 'ok' : 'bad';
    elFb.className   = 'wsq-fb ' + (correct ? 'ok' : 'bad');
    elFb.innerHTML   = correct
      ? ('✓ ' + L.correct)
      : (L.wrong + '. ' + L.correctAns + ' <strong>' + esc(q.correct) + '</strong>');
    elFb.style.display = 'block';

    if (q.explanation) {
      elExpl.innerHTML     = q.explanation;
      elExpl.style.display = 'block';
    }

    elCheck.style.display = 'none';
    elNext.style.display  = 'block';

    // Track first-pass
    if (!seenOnce[q.qKey]) {
      seenOnce[q.qKey] = true;
      if (correct) firstPassOK++;
    }

    if (correct) {
      answeredQ++;
      perSection[q.sectionId].correct++;
      var idx = queue.indexOf(q);
      if (idx !== -1) queue.splice(idx, 1);
      // Auto-advance after 1.5 s
      autoTimer = setTimeout(function () { elNext.click(); }, 1500);
    } else {
      lives--;
      var idx2 = queue.indexOf(q);
      if (idx2 !== -1) { queue.splice(idx2, 1); queue.push(q); }
      if (lives <= 0) elNext.textContent = L.seeResults;
    }

    updateHeader();
  }

  // ── Next ─────────────────────────────────────────────────────────
  function doNext() {
    if (autoTimer) { clearTimeout(autoTimer); autoTimer = null; }
    if (queue.length === 0 || lives <= 0) { finish(); return; }
    showQ(queue[0]);
  }

  // ── Finish ───────────────────────────────────────────────────────
  function finish() {
    quiz.style.display = 'none';

    var pct     = totalQ ? Math.round((firstPassOK / totalQ) * 100) : 0;
    var success = lives > 0 && queue.length === 0;

    // Save progress
    if (window.FCEStore && window.CHAPTER_ID) {
      var pEx = {};
      Object.keys(perSection).forEach(function (sId) {
        pEx[sId] = { correct: perSection[sId].correct, total: perSection[sId].total };
      });
      try { FCEStore.saveResult(window.CHAPTER_ID, firstPassOK, totalQ, pEx); } catch (e) {}
      if (success && pct >= 50) try { FCEStore.addXP(20); } catch (e) {}
    }

    var pctColor = pct >= 80 ? 'var(--green)' : pct >= 50 ? 'var(--amber)' : 'var(--red)';

    var gameCTA = success
      ? '<a href="game.html" style="display:inline-block;padding:13px 32px;background:var(--amber);color:#1A1A1A;font-family:var(--font-sans);font-size:.8rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;border-radius:5px">' + L.gameBtn + ' &#8594;</a><br>'
      : '';
    var retryBtn = '<button onclick="location.reload()" style="display:inline-block;margin-top:12px;padding:11px 26px;background:transparent;color:var(--ink);font-family:var(--font-sans);font-size:.76rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;border:1.5px solid var(--hairline);border-radius:4px;cursor:pointer">' + L.tryAgain + '</button>';

    var done = document.createElement('div');
    done.id = 'wsq-done';
    done.innerHTML = [
      '<div id="wsq-done-card">',
        '<div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2.5px;text-transform:uppercase;color:var(--amber);margin-bottom:8px">' + (success ? L.completed : L.noLives) + '</div>',
        '<h2 style="font-family:Georgia,serif;font-size:2rem;font-weight:700;color:var(--ink);margin:0 0 10px">' + (success ? L.wellDone : L.keepGoing) + '</h2>',
        '<p style="font-family:var(--font-sans);font-size:.88rem;color:var(--muted);margin:0 0 24px">' + L.firstPass + ' <strong style="color:' + pctColor + '">' + firstPassOK + ' / ' + totalQ + ' (' + pct + '%)</strong></p>',
        gameCTA,
        retryBtn,
        '<br><a href="index.html" style="display:inline-block;margin-top:16px;font-family:var(--font-sans);font-size:.78rem;color:var(--muted);text-decoration:none">' + L.back + '</a>',
      '</div>',
    ].join('');

    var footer = document.querySelector('.site-footer');
    if (footer) footer.before(done);
    else document.body.appendChild(done);
  }

  // ── Wire events ──────────────────────────────────────────────────
  elCheck.addEventListener('click', doCheck);
  elNext.addEventListener('click',  doNext);

  // ── Start ────────────────────────────────────────────────────────
  renderLives();
  if (queue.length) showQ(queue[0]);

})();
