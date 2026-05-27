// ══════════════════════════════════════════════════════════════════
// deck.js — one-at-a-time lesson slides with swipe + button nav
// Shows slides one at a time; navigates with buttons, swipe, keyboard
// ══════════════════════════════════════════════════════════════════

// ── Inject Dashboard link into site header ───────────────────────
(function() {
  var inner = document.querySelector('.site-header-inner');
  var brand = inner && inner.querySelector('.brand');
  if (!inner || !brand || inner.querySelector('.header-dash')) return;
  var dash = document.createElement('a');
  dash.className = 'header-dash';
  dash.textContent = 'Dashboard';
  var href = brand.getAttribute('href') || 'index.html';
  dash.href = href.replace('index.html', 'dashboard.html');
  dash.style.cssText = 'color:#A8B4C6;text-decoration:none;font-size:.78rem;font-family:var(--font-sans,-apple-system,sans-serif);font-weight:600;padding:5px 10px;border-radius:4px;border:1px solid rgba(255,255,255,.2);transition:border-color .15s,color .15s';
  dash.onmouseenter = function() { this.style.borderColor='var(--amber)'; this.style.color='var(--amber)'; };
  dash.onmouseleave = function() { this.style.borderColor='rgba(255,255,255,.2)'; this.style.color='#A8B4C6'; };
  inner.insertBefore(dash, inner.lastElementChild);
})();

// ── Confetti celebration ─────────────────────────────────────────
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
      nextBtn.innerHTML = current === total - 1
        ? 'Finish &#10003;' : 'Next &#9654;';
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
    void s.offsetHeight; // force reflow
    s.classList.add('slide-anim');
    updateUI();
    if (current === total - 1 && !completed) { completed = true; markComplete(); }
  }

  // ── Public navigation functions (called by HTML onclick attrs too) ─
  window.nextSlide = function() {
    if (current < total - 1) goTo(current + 1);
    else if (!completed) { completed = true; markComplete(); }
  };
  window.prevSlide = function() { if (current > 0) goTo(current - 1); };
  window.goToSlide = function(n) { if (n >= 0 && n < total) goTo(n); };

  // ── Wire buttons (only if no onclick attribute already) ──────────
  var prevBtn = document.getElementById('deck-prev');
  var nextBtn = document.getElementById('deck-next');
  if (prevBtn && !prevBtn.getAttribute('onclick')) prevBtn.addEventListener('click', window.prevSlide);
  if (nextBtn && !nextBtn.getAttribute('onclick')) nextBtn.addEventListener('click', window.nextSlide);

  // ── Keyboard: arrow keys ─────────────────────────────────────────
  document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowRight' || e.key === 'PageDown') { e.preventDefault(); window.nextSlide(); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); window.prevSlide(); }
  });

  // ── Touch swipe — Tinder-style drag + fly-away ───────────────────
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
    e.preventDefault(); // block scroll during horizontal swipe — stops fixed-element jitter
    swipeDelta = dx;
    var fade = 1 - Math.min(1, Math.abs(dx) / (window.innerWidth * 0.55));
    swipeCard.style.transform = 'translateX(' + dx + 'px)';
    swipeCard.style.opacity = Math.max(0.25, fade);
  }, { passive: false }); // non-passive so preventDefault works

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
    if (window.FCEStore && window.FCEStore.touchStreak) {
      try { window.FCEStore.touchStreak(); } catch(e) {}
    }
    showLessonCompleteBanner();
  }

  // ── Completion banner ─────────────────────────────────────────────
  function showLessonCompleteBanner() {
    if (document.getElementById('lesson-complete-banner')) return;
    if (!document.getElementById('lesson-banner-style')) {
      var sty = document.createElement('style');
      sty.id  = 'lesson-banner-style';
      sty.textContent = '@keyframes lessonBannerIn{from{opacity:0;transform:translate(-50%,14px)}to{opacity:1;transform:translate(-50%,0)}}';
      document.head.appendChild(sty);
    }
    triggerConfetti();
    var banner = document.createElement('div');
    banner.id = 'lesson-complete-banner';
    banner.style.cssText = [
      'position:fixed;bottom:72px;left:50%;transform:translateX(-50%)',
      'background:var(--amber,#B8860B);color:#1A1A1A',
      'font-family:var(--font-sans,system-ui,sans-serif);font-size:.75rem',
      'font-weight:800;letter-spacing:1.5px;text-transform:uppercase',
      'padding:10px 24px;border-radius:6px',
      'box-shadow:0 4px 20px rgba(0,0,0,.25)',
      'z-index:200;white-space:nowrap',
      'animation:lessonBannerIn .3s ease-out'
    ].join(';');
    banner.innerHTML = '&#10003; Lesson complete &nbsp;&middot;&nbsp; <a href="worksheet.html" style="color:#1A1A1A;font-weight:900;text-decoration:underline">Practice now</a>';
    document.body.appendChild(banner);
    setTimeout(function() {
      banner.style.transition = 'opacity .4s';
      banner.style.opacity = '0';
      setTimeout(function() { if (banner.parentNode) banner.parentNode.removeChild(banner); }, 450);
    }, 7000);
  }

  // ── Init ─────────────────────────────────────────────────────────
  updateUI();
})();
