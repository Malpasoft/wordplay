// ══════════════════════════════════════════════════════════════════
// dark-init.js — dark/light mode toggle
// ══════════════════════════════════════════════════════════════════
//
// Reads localStorage key "wordplay_dark" ("1" = dark mode on).
// Applies class "dark" to document.body immediately (in <head>) to
// prevent a flash of the wrong theme on page load.
//
// USAGE
//   Load in <head> (not deferred): <script src="shared/dark-init.js"></script>
//   Toggle button: <button class="dark-toggle" onclick="toggleDark()">Dark</button>
//   toggleDark() is exposed globally.
// ══════════════════════════════════════════════════════════════════
(function() {
  function applyDark() {
    var isDark = localStorage.getItem('wordplay_dark') === '1';
    if (isDark) document.body.classList.add('dark');
    document.querySelectorAll('.dark-toggle').forEach(function(btn) {
      btn.textContent = isDark ? '\u25d1 Light' : '\u25d0 Dark';
    });
  }
  if (document.body) {
    applyDark();
  } else {
    document.addEventListener('DOMContentLoaded', applyDark);
  }
})();

function toggleDark() {
  var on = document.body.classList.toggle('dark');
  localStorage.setItem('wordplay_dark', on ? '1' : '0');
  document.querySelectorAll('.dark-toggle').forEach(function(btn) {
    btn.textContent = on ? '\u25d1 Light' : '\u25d0 Dark';
  });
}


// Back to top button — appears on long pages
(function(){
  if (typeof document === 'undefined') return;
  function setup() {
    if (document.getElementById('back-to-top')) return;
    var btn = document.createElement('button');
    btn.id = 'back-to-top';
    btn.setAttribute('aria-label', 'Back to top');
    btn.innerHTML = '&#8593;';
    btn.onclick = function() { window.scrollTo({top:0, behavior:'smooth'}); };
    document.body.appendChild(btn);
    window.addEventListener('scroll', function() {
      if (window.scrollY > 400) btn.classList.add('visible');
      else btn.classList.remove('visible');
    }, {passive:true});
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setup);
  } else { setup(); }
})();
