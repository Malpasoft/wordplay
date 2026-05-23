// ══════════════════════════════════════════════════════════════════
// deck.js — lesson slide navigation and progress tracking
// ══════════════════════════════════════════════════════════════════
//
// WHAT THIS FILE DOES
// Handles navigation between .slide elements on lesson pages.
// Tracks which slide the student reached and marks lesson as complete
// when they reach the last slide.
//
// REQUIRES on the page (before this script):
//   window.LEVEL      — e.g. "a1"
//   window.CHAPTER_ID — e.g. "to-be"
//
// EXPECTED HTML
//   <div id="slide-deck">
//     <div class="slide">...</div>   ← one per slide
//   </div>
//   <button onclick="prevSlide()">← Prev</button>
//   <span id="slide-counter">1 / 4</span>
//   <button onclick="nextSlide()">Next →</button>
//
// PROGRESS STORAGE
//   wordplay_slides_{level}_{slug}          — current slide index
//   wordplay_slides_{level}_{slug}_complete — "1" when last slide reached
// ══════════════════════════════════════════════════════════════════
(function() {
  var slides = document.querySelectorAll('.slide');
  if (!slides.length) return;
  
  var counter = document.getElementById('slide-counter');
  var current = 0;
  
  // Storage key for this chapter (window.CHAPTER_ID set by slides.html)
  var chapterId = window.CHAPTER_ID || '';
  var level = window.LEVEL || '';
  var slideKey = chapterId ? 'wordplay_slides_' + level + '_' + chapterId : null;
  var completeKey = chapterId ? 'wordplay_slides_' + level + '_' + chapterId + '_complete' : null;
  
  function show(idx) {
    slides.forEach(function(s, i) { s.style.display = i === idx ? 'block' : 'none'; });
    current = idx;
    if (counter) counter.textContent = 'Slide ' + (idx + 1) + ' of ' + slides.length;
    
    // Update slide progress bar
    var bar = document.getElementById('deck-progress-fill');
    if (bar) bar.style.width = Math.round(((idx + 1) / slides.length) * 100) + '%';
    
    
    // Save current slide index
    if (slideKey) {
      try { localStorage.setItem(slideKey, String(idx)); } catch(e) {}
    }
    
    // Mark complete on last slide
    if (idx === slides.length - 1) {
      // Save legacy key
      if (completeKey) { try { localStorage.setItem(completeKey, '1'); } catch(e) {} }
      // Save to FCEStore
      if (window.FCEStore && chapterId && level) {
        try {
          var raw = localStorage.getItem('wordplay_progress');
          var data = raw ? JSON.parse(raw) : {};
          data[level] = data[level] || {};
          if (!data[level]['slides_' + chapterId]) {
            data[level]['slides_' + chapterId] = { done: true, date: new Date().toISOString() };
            localStorage.setItem('wordplay_progress', JSON.stringify(data));
          }
        } catch(e) {}
      }
      // Show completion banner (only once per session)
      if (window.FCEStore && window.FCEStore.touchStreak) {
        try { window.FCEStore.touchStreak(); } catch(e) {}
      }
      showLessonCompleteBanner();
    }
    
    // Toggle prev/next button states
    var prevBtn = document.getElementById('deck-prev');
    var nextBtn = document.getElementById('deck-next');
    if (prevBtn) prevBtn.disabled = idx === 0;
    if (nextBtn) nextBtn.disabled = idx === slides.length - 1;
  }
  

  // ── Lesson complete banner ────────────────────────────────────
  function showLessonCompleteBanner() {
    if (document.getElementById('lesson-complete-banner')) return;
    var banner = document.createElement('div');
    banner.id = 'lesson-complete-banner';
    banner.style.cssText = [
      'position:fixed;bottom:80px;left:50%;transform:translateX(-50%)',
      'background:var(--amber,#B8860B);color:#1A1A1A',
      'font-family:var(--font-sans,system-ui,sans-serif);font-size:.75rem',
      'font-weight:800;letter-spacing:1.5px;text-transform:uppercase',
      'padding:10px 24px;border-radius:6px',
      'box-shadow:0 4px 20px rgba(0,0,0,.35)',
      'z-index:200;white-space:nowrap',
      'animation:lessonBannerIn .3s ease-out'
    ].join(';');
    banner.innerHTML = '&#10003; Lesson complete &nbsp;&#183;&nbsp; <a href="worksheet.html" style="color:#1A1A1A;font-weight:900;text-decoration:underline">Practice now</a>';
    // Inject keyframe if not present
    if (!document.getElementById('lesson-banner-style')) {
      var sty = document.createElement('style');
      sty.id = 'lesson-banner-style';
      sty.textContent = '@keyframes lessonBannerIn{from{opacity:0;transform:translate(-50%,16px)}to{opacity:1;transform:translate(-50%,0)}}';
      document.head.appendChild(sty);
    }
    document.body.appendChild(banner);
    // Auto-dismiss after 6 s
    setTimeout(function() {
      banner.style.transition = 'opacity .4s';
      banner.style.opacity = '0';
      setTimeout(function() { if (banner.parentNode) banner.parentNode.removeChild(banner); }, 450);
    }, 6000);
  }

  window.nextSlide = function() { if (current < slides.length - 1) show(current + 1); };
  window.prevSlide = function() { if (current > 0) show(current - 1); };

  // Wire click listeners to the fixed-position nav buttons
  var prevBtn2 = document.getElementById('deck-prev');
  var nextBtn2 = document.getElementById('deck-next');
  if (prevBtn2) prevBtn2.addEventListener('click', function() { window.prevSlide(); });
  if (nextBtn2) nextBtn2.addEventListener('click', function() { window.nextSlide(); });
  window.goToSlide = function(n) { if (n >= 0 && n < slides.length) show(n); };
  
  // Restore last position
  var lastIdx = 0;
  if (slideKey) {
    try {
      var saved = localStorage.getItem(slideKey);
      if (saved !== null) {
        var n = parseInt(saved, 10);
        if (!isNaN(n) && n >= 0 && n < slides.length) lastIdx = n;
      }
    } catch(e) {}
  }
  show(lastIdx);
  
  // Keyboard nav
  document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowRight' || e.key === 'PageDown') { e.preventDefault(); window.nextSlide(); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); window.prevSlide(); }
  });
  
  // Touch swipe
  var startX = 0;
  document.addEventListener('touchstart', function(e) { startX = e.touches[0].clientX; });
  document.addEventListener('touchend', function(e) {
    var dx = e.changedTouches[0].clientX - startX;
    if (Math.abs(dx) > 50) {
      if (dx < 0) window.nextSlide();
      else window.prevSlide();
    }
  });
})();
