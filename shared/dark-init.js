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


// Dashboard link injection — all pages except the dashboard itself
(function(){
  function injectDashLink() {
    var inner = document.querySelector('.site-header-inner');
    if (!inner) return;
    if (inner.querySelector('.header-dash')) return;
    var brand = inner.querySelector('.brand');
    if (!brand) return;
    if (window.location.pathname.indexOf('dashboard') !== -1) return;
    var dash = document.createElement('a');
    dash.className = 'header-dash';
    dash.textContent = 'Dashboard';
    var href = brand.getAttribute('href') || 'index.html';
    dash.href = href.replace('index.html', 'dashboard.html');
    dash.style.cssText = 'color:#A8B4C6;font-size:.78rem;font-weight:600;padding:4px 10px;border-radius:6px;text-decoration:none;border:1px solid rgba(255,255,255,.2);white-space:nowrap;';
    inner.insertBefore(dash, inner.lastElementChild);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectDashLink);
  } else {
    injectDashLink();
  }
})();

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

// QR code button — lets teachers share the current page with students
(function(){
  function injectQR() {
    var inner = document.querySelector('.site-header-inner');
    if (!inner || inner.querySelector('.qr-toggle')) return;
    var btn = document.createElement('button');
    btn.className = 'qr-toggle';
    btn.textContent = 'QR';
    btn.setAttribute('aria-label', 'Show QR code for this page');
    btn.onclick = openQRModal;
    inner.appendChild(btn);
  }
  function openQRModal() {
    var modal = document.getElementById('wp-qr-modal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'wp-qr-modal';
      modal.innerHTML =
        '<div class="wp-qr-box">' +
        '<img class="wp-qr-img" width="220" height="220" alt="QR code">' +
        '<p class="wp-qr-url"></p>' +
        '<button class="wp-qr-close">Close</button>' +
        '</div>';
      modal.querySelector('.wp-qr-close').onclick = function(){ modal.style.display = 'none'; };
      modal.onclick = function(e){ if (e.target === modal) modal.style.display = 'none'; };
      document.body.appendChild(modal);
    }
    var url = window.location.href;
    modal.querySelector('.wp-qr-img').src =
      'https://api.qrserver.com/v1/create-qr-code/?size=220x220&data=' + encodeURIComponent(url);
    modal.querySelector('.wp-qr-url').textContent = url;
    modal.style.display = 'flex';
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectQR);
  } else { injectQR(); }
})();

// Group Dark + QR as a connected pill after both are injected
(function(){
  function groupUtils() {
    var inner = document.querySelector('.site-header-inner');
    if (!inner || inner.querySelector('.header-utils')) return;
    var darkBtn = inner.querySelector('.dark-toggle');
    var qrBtn = inner.querySelector('.qr-toggle');
    if (!darkBtn || !qrBtn) return;
    var utils = document.createElement('div');
    utils.className = 'header-utils';
    inner.insertBefore(utils, darkBtn);
    utils.appendChild(darkBtn);
    utils.appendChild(qrBtn);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', groupUtils);
  } else { groupUtils(); }
})();
