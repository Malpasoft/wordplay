// ══════════════════════════════════════════════════════════════════
// deck.js — lesson block layout with scroll-based progress tracking
// All slides visible simultaneously; progress tracked as you read
// ══════════════════════════════════════════════════════════════════
(function() {
  var slides = document.querySelectorAll('.slide');
  if (!slides.length) return;

  var chapterId = window.CHAPTER_ID || '';
  var level     = window.LEVEL || '';
  var slideKey   = chapterId ? 'wordplay_slides_' + level + '_' + chapterId : null;
  var completeKey = chapterId ? 'wordplay_slides_' + level + '_' + chapterId + '_complete' : null;

  // Show all slides (block layout)
  slides.forEach(function(s) { s.style.display = 'block'; });

  var highestSeen = 0;
  var completed   = false;

  function updateProgress(idx) {
    if (idx <= highestSeen && idx !== slides.length - 1) return;
    highestSeen = Math.max(highestSeen, idx);

    var pct = Math.round(((idx + 1) / slides.length) * 100);
    var bar = document.getElementById('deck-progress-fill');
    if (bar) bar.style.width = pct + '%';

    if (slideKey) { try { localStorage.setItem(slideKey, String(idx)); } catch(e) {} }

    if (idx === slides.length - 1 && !completed) {
      completed = true;
      markComplete();
    }
  }

  // IntersectionObserver: fire when each slide is ≥30% visible
  if (window.IntersectionObserver) {
    var obs = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var idx = Array.from(slides).indexOf(entry.target);
          if (idx >= 0) updateProgress(idx);
        }
      });
    }, { threshold: 0.3 });
    slides.forEach(function(s) { obs.observe(s); });
  } else {
    // Fallback for old browsers: mark complete after 4s
    setTimeout(function() { if (!completed) { completed = true; markComplete(); } }, 4000);
  }

  // ── Mark lesson complete ──────────────────────────────────────
  function markComplete() {
    if (completeKey) { try { localStorage.setItem(completeKey, '1'); } catch(e) {} }

    if (chapterId && level) {
      try {
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

  // ── Completion banner ─────────────────────────────────────────
  function showLessonCompleteBanner() {
    if (document.getElementById('lesson-complete-banner')) return;
    var banner = document.createElement('div');
    banner.id = 'lesson-complete-banner';
    banner.style.cssText = [
      'position:fixed;bottom:24px;left:50%;transform:translateX(-50%)',
      'background:var(--amber,#B8860B);color:#1A1A1A',
      'font-family:var(--font-sans,system-ui,sans-serif);font-size:.75rem',
      'font-weight:800;letter-spacing:1.5px;text-transform:uppercase',
      'padding:10px 24px;border-radius:6px',
      'box-shadow:0 4px 20px rgba(0,0,0,.35)',
      'z-index:200;white-space:nowrap',
      'animation:lessonBannerIn .3s ease-out'
    ].join(';');
    banner.innerHTML = '&#10003; Lesson complete &nbsp;&#183;&nbsp; <a href="worksheet.html" style="color:#1A1A1A;font-weight:900;text-decoration:underline">Practice now</a>';

    if (!document.getElementById('lesson-banner-style')) {
      var sty = document.createElement('style');
      sty.id  = 'lesson-banner-style';
      sty.textContent = '@keyframes lessonBannerIn{from{opacity:0;transform:translate(-50%,16px)}to{opacity:1;transform:translate(-50%,0)}}';
      document.head.appendChild(sty);
    }
    document.body.appendChild(banner);

    setTimeout(function() {
      banner.style.transition = 'opacity .4s';
      banner.style.opacity = '0';
      setTimeout(function() { if (banner.parentNode) banner.parentNode.removeChild(banner); }, 450);
    }, 7000);
  }

  // ── Keyboard: arrow keys scroll to prev/next slide ────────────
  function currentSlideIdx() {
    var best = 0, minDist = Infinity;
    slides.forEach(function(s, i) {
      var dist = Math.abs(s.getBoundingClientRect().top - 80);
      if (dist < minDist) { minDist = dist; best = i; }
    });
    return best;
  }

  window.nextSlide = function() {
    var n = currentSlideIdx();
    if (n < slides.length - 1) slides[n + 1].scrollIntoView({ behavior: 'smooth', block: 'start' });
  };
  window.prevSlide = function() {
    var n = currentSlideIdx();
    if (n > 0) slides[n - 1].scrollIntoView({ behavior: 'smooth', block: 'start' });
  };
  window.goToSlide = function(n) {
    if (n >= 0 && n < slides.length) slides[n].scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowRight' || e.key === 'PageDown') { e.preventDefault(); window.nextSlide(); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); window.prevSlide(); }
  });
})();
