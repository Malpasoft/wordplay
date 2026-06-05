// ══════════════════════════════════════════════════════════════════
// deck.js — one-at-a-time lesson slides with swipe + button nav
// ══════════════════════════════════════════════════════════════════

// ── Confetti ─────────────────────────────────────────────────────
function triggerConfetti() {
  if (!document.getElementById('cf-kf')) {
    var s = document.createElement('style');
    s.id = 'cf-kf';
    s.textContent = '@keyframes cfFall{to{transform:translateY(105vh) rotate(480deg);opacity:0}}';
    document.head.appendChild(s);
  }
  var colors = ['#C9A050','#E8A020','#B8860B','#FFD080','#F0C060','#D4A030'];
  for (var i = 0; i < 32; i++) {
    var p = document.createElement('div');
    var sz = 6 + Math.random() * 6;
    p.style.cssText = 'position:fixed;top:-12px;width:' + sz + 'px;height:' + sz + 'px;border-radius:' + Math.round(Math.random()) + 'px;background:' + colors[Math.floor(Math.random() * colors.length)] + ';left:' + (5 + Math.random() * 90) + '%;animation:cfFall ' + (1.8 + Math.random() * 2.2) + 's ' + (Math.random() * 0.5) + 's ease-in forwards;z-index:999;pointer-events:none';
    document.body.appendChild(p);
    setTimeout(function(el) { if (el.parentNode) el.parentNode.removeChild(el); }, 4500, p);
  }
}

(function() {
  var slides = Array.from(document.querySelectorAll('.slide'));
  if (!slides.length) return;

  var chapterId = window.CHAPTER_ID || '';
  var level     = window.LEVEL || '';
  var total     = slides.length;
  var current   = 0;
  var completed = false;

  // ── Init: hide all slides except first ──────────────────────────
  slides.forEach(function(s, i) { s.style.display = i === 0 ? 'block' : 'none'; });

  // ── Update buttons + progress bar ────────────────────────────────
  function updateUI() {
    var prevBtn = document.getElementById('deck-prev');
    var nextBtn = document.getElementById('deck-next');
    var counter = document.getElementById('slide-counter');
    var bar     = document.getElementById('deck-progress-fill');
    var pct     = Math.round(((current + 1) / total) * 100);

    if (prevBtn) prevBtn.disabled = current === 0;
    if (nextBtn) {
      nextBtn.disabled = false;
      // Always "Next →" — the completion screen handles the post-lesson CTA
      nextBtn.innerHTML = 'Next &#9654;';
    }
    if (counter) counter.textContent = (current + 1) + ' / ' + total;
    if (bar) bar.style.width = pct + '%';

    if (chapterId && level) {
      try { localStorage.setItem('wordplay_slides_' + level + '_' + chapterId, String(current)); } catch(e) {}
    }
  }

  // ── Navigate to a specific slide index ───────────────────────────
  function goTo(idx) {
    if (idx === current || idx < 0 || idx >= total) return;
    slides[current].style.display = 'none';
    current = idx;
    var s = slides[current];
    s.style.display = 'block';
    s.classList.remove('slide-anim');
    void s.offsetHeight;
    s.classList.add('slide-anim');
    updateUI();
  }

  // ── Public navigation ────────────────────────────────────────────
  window.nextSlide = function() {
    if (current < total - 1) {
      goTo(current + 1);
    } else {
      // Last slide → show completion screen
      if (!completed) { completed = true; markComplete(); }
      showCompletionScreen();
    }
  };
  window.prevSlide = function() { if (current > 0) goTo(current - 1); };
  window.goToSlide = function(n) { if (n >= 0 && n < total) goTo(n); };

  // ── Wire buttons ─────────────────────────────────────────────────
  var prevBtn = document.getElementById('deck-prev');
  var nextBtn = document.getElementById('deck-next');
  if (prevBtn && !prevBtn.getAttribute('onclick')) prevBtn.addEventListener('click', window.prevSlide);
  if (nextBtn && !nextBtn.getAttribute('onclick')) nextBtn.addEventListener('click', window.nextSlide);

  // ── Keyboard nav ─────────────────────────────────────────────────
  document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowRight' || e.key === 'PageDown') { e.preventDefault(); window.nextSlide(); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); window.prevSlide(); }
  });

  // ── Touch swipe ──────────────────────────────────────────────────
  var swipeStartX = 0, swipeStartY = 0;
  var swipeActive = false, swipeDelta = 0;
  var swipeCard = null;

  function getActiveCard() {
    return slides[current] && slides[current].querySelector('.slide-card');
  }

  document.addEventListener('touchstart', function(e) {
    if (e.touches.length > 1) return;
    swipeStartX = e.touches[0].clientX;
    swipeStartY = e.touches[0].clientY;
    swipeActive = false;
    swipeDelta = 0;
    swipeCard = getActiveCard();
    if (swipeCard) swipeCard.style.transition = 'none';
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
    swipeCard.style.opacity = Math.max(0.25, fade);
  }, { passive: false });

  document.addEventListener('touchend', function() {
    if (!swipeCard) return;
    var card = swipeCard;
    swipeCard = null;
    if (!swipeActive || Math.abs(swipeDelta) < 30) {
      card.style.transition = 'transform .22s ease-out, opacity .22s ease-out';
      card.style.transform = '';
      card.style.opacity = '';
      setTimeout(function() { card.style.transition = ''; }, 230);
      return;
    }
    var dir = swipeDelta < 0 ? -1 : 1;
    var flyX = dir * window.innerWidth * 1.3;
    var flyRot = dir * -18;
    card.style.transition = 'transform .26s ease-in, opacity .22s ease-in';
    card.style.transform = 'translateX(' + flyX + 'px) rotate(' + flyRot + 'deg)';
    card.style.opacity = '0';
    setTimeout(function() {
      card.style.transition = 'none';
      card.style.transform = '';
      card.style.opacity = '';
      if (dir < 0) window.nextSlide();
      else window.prevSlide();
    }, 270);
  }, { passive: true });

  // ── Mark lesson complete ─────────────────────────────────────────
  function markComplete() {
    if (chapterId && level) {
      try {
        localStorage.setItem('wordplay_slides_' + level + '_' + chapterId + '_complete', '1');
        var raw  = localStorage.getItem('wordplay_progress');
        var data = raw ? JSON.parse(raw) : {};
        data[level] = data[level] || {};
        if (!data[level]['slides_' + chapterId]) {
          data[level]['slides_' + chapterId] = { done: true, date: new Date().toISOString() };
          localStorage.setItem('wordplay_progress', JSON.stringify(data));
        }
      } catch(e) {}
    }
    if (window.FCEStore) {
      try { window.FCEStore.touchStreak(); } catch(e) {}
      try { window.FCEStore.addXP(10); } catch(e) {}
    }
  }

  // ── Completion screen (replaces the slide deck) ───────────────────
  function showCompletionScreen() {
    var deckWrap = document.querySelector('.slide-deck');
    var deckNav  = document.querySelector('.deck-nav');
    var bar      = document.getElementById('deck-progress-fill');

    if (deckWrap) deckWrap.style.display = 'none';
    if (deckNav)  deckNav.style.display  = 'none';
    if (bar) bar.style.width = '100%';

    if (document.getElementById('deck-complete')) return;

    triggerConfetti();

    // Language detection via i18n module
    var isEs = window.i18n ? window.i18n.isSpanish(window.LEVEL) : ((window.LEVEL || '').indexOf('es-') === 0 || document.documentElement.lang === 'es');
    var getString = window.i18n ? window.i18n.getString : function(key) { return key; };
    var reviewLabel = getString('deck_reviewStart');
    var completeLabel = getString('deck_complete');
    var wellDoneLabel = getString('deck_wellDone');
    var readyLabel = getString('deck_ready');
    var backLabel = getString('ws_back');

    var screen = document.createElement('div');
    screen.id = 'deck-complete';
    screen.style.cssText = 'max-width:680px;margin:40px auto;padding:0 20px 80px';
    screen.innerHTML = [
      '<div style="text-align:center;padding:40px 28px;background:var(--cream-deep);border:1.5px solid var(--hairline);border-radius:10px">',
        '<div style="font-family:var(--font-sans);font-size:.6rem;font-weight:800;letter-spacing:2.5px;text-transform:uppercase;color:var(--amber);margin-bottom:10px">' + completeLabel + '</div>',
        '<h2 style="font-family:Georgia,serif;font-size:2rem;font-weight:700;color:var(--ink);margin:0 0 10px">' + wellDoneLabel + '</h2>',
        '<p style="font-family:var(--font-sans);font-size:.9rem;color:var(--muted);margin:0 0 28px">' + readyLabel + '</p>',
        '<a href="worksheet.html" style="display:inline-block;padding:14px 36px;background:var(--amber);color:#1A1A1A;font-family:var(--font-sans);font-size:.82rem;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;border-radius:5px">' + reviewLabel + ' &#8594;</a>',
        '<br><br>',
        '<a href="index.html" style="font-family:var(--font-sans);font-size:.78rem;color:var(--muted);text-decoration:none">' + backLabel + '</a>',
      '</div>'
    ].join('');

    var footer = document.querySelector('.site-footer');
    if (footer) footer.before(screen);
    else document.body.appendChild(screen);
  }

  // ── Init ─────────────────────────────────────────────────────────
  updateUI();
})();
