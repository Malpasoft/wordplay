// ══════════════════════════════════════════════════════════════════
// dark-init.js — dark mode, dashboard link, XP badge, search, QR
// ══════════════════════════════════════════════════════════════════
// Capture path to shared/ while the script is executing (synchronous)
var _SHARED = (document.currentScript || {src:''}).src.replace(/dark-init\.js[^/]*$/, '') || 'shared/';

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
      document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && modal.style.display !== 'none') modal.style.display = 'none'; });
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

// XP badge — shows level name + mini progress bar
(function(){
  function injectXP() {
    var inner = document.querySelector('.site-header-inner');
    if (!inner || inner.querySelector('.header-xp') || !window.FCEStore) return;
    var lv   = FCEStore.getXPLevel();
    var pct  = lv.pct;
    var next = lv.max ? lv.xp + ' / ' + lv.max : lv.xp + ' XP';
    // The level badge doubles as the dashboard link (top-right "account" spot)
    var badge = document.createElement('a');
    badge.className = 'header-xp';
    badge.title = lv.label + ' · ' + next + ' XP · Open your dashboard';
    var onDash = window.location.pathname.indexOf('dashboard') !== -1;
    if (!onDash) {
      var brand = inner.querySelector('.brand');
      var href  = (brand && brand.getAttribute('href')) || 'index.html';
      badge.href = href.replace('index.html', 'dashboard.html');
    }
    badge.innerHTML =
      '<span class="header-xp-label">' + lv.label + '</span>' +
      '<div class="header-xp-bar"><div class="header-xp-fill" style="width:' + pct + '%"></div></div>' +
      '<span class="header-xp-go" aria-hidden="true">&#8250;</span>';
    inner.appendChild(badge);   // last element → far-right account corner
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectXP);
  } else { injectXP(); }
})();

// Chapter search — icon expands into an inline field within the header bar
(function(){
  var _loaded  = false;
  var _inner   = null;
  var _inline  = null;
  var _input   = null;
  var _panel   = null;
  var _results = null;

  function injectSearch() {
    var inner = document.querySelector('.site-header-inner');
    if (!inner || inner.querySelector('.header-search-btn')) return;
    _inner = inner;

    var btn = document.createElement('button');
    btn.className = 'header-search-btn';
    btn.setAttribute('aria-label', 'Search chapters');
    btn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>';
    btn.onclick = toggleSearch;

    var utils = inner.querySelector('.header-utils');
    if (utils) inner.insertBefore(btn, utils);
    else inner.appendChild(btn);
  }

  function ensureUI() {
    if (_inline) return;
    // Inline field inside the header bar
    _inline = document.createElement('div');
    _inline.className = 'header-search-inline';
    _inline.innerHTML =
      '<input type="search" placeholder="Search chapters…" autocomplete="off" aria-label="Search chapters">' +
      '<button class="header-search-close" aria-label="Close search">&times;</button>';
    _input = _inline.querySelector('input');
    _inner.appendChild(_inline);

    // Results drop into a panel below the header
    _panel = document.createElement('div');
    _panel.className = 'header-search-panel';
    _panel.innerHTML = '<div class="header-search-results"></div>';
    _results = _panel.querySelector('.header-search-results');
    var header = document.querySelector('.site-header');
    if (header && header.parentNode) header.after(_panel);
    else document.body.insertBefore(_panel, document.body.firstChild);

    _input.addEventListener('input', onInput);
    _input.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeSearch(); });
    _inline.querySelector('.header-search-close').onclick = closeSearch;
    document.addEventListener('click', function(e) {
      if (!_inner.classList.contains('searching')) return;
      if (!_inner.contains(e.target) && !_panel.contains(e.target)) closeSearch();
    }, true);
  }

  function toggleSearch() {
    ensureUI();
    if (_inner.classList.contains('searching')) { closeSearch(); return; }
    _inner.classList.add('searching');
    _input.value = '';
    _results.innerHTML = '';
    _panel.style.display = 'none';
    setTimeout(function() { _input.focus(); }, 40);
    loadSearch();
  }

  function closeSearch() {
    if (_inner) _inner.classList.remove('searching');
    if (_panel) _panel.style.display = 'none';
  }

  function loadSearch() {
    if (_loaded || !window.WPSearch) {
      if (!window.WPSearch) {
        var s = document.createElement('script');
        s.src = _SHARED + 'search.js?v=v101';
        s.onload = function() { _loaded = true; if (_input && _input.value) onInput(); };
        document.head.appendChild(s);
      }
      return;
    }
    WPSearch.load(_SHARED + 'search-index.json', function() { if (_input && _input.value) onInput(); });
    _loaded = true;
  }

  function onInput() {
    if (!_results) return;
    var q = _input ? _input.value.trim() : '';
    if (!q) { _results.innerHTML = ''; _panel.style.display = 'none'; return; }
    if (!window.WPSearch) { loadSearch(); return; }
    if (!_loaded) {
      WPSearch.load(_SHARED + 'search-index.json', function() { onInput(); });
      _loaded = true;
      return;
    }
    var hits = WPSearch.search(q);
    _panel.style.display = 'block';
    if (!hits.length) {
      _results.innerHTML = '<div class="sr-empty">No chapters found</div>';
      return;
    }
    _results.innerHTML = hits.map(function(h) {
      return '<a href="' + h.url + '" class="sr-item">' +
        '<span class="sr-title">' + h.title + '</span>' +
        '<span class="sr-meta">' + h.level + ' · ' + h.section + '</span>' +
      '</a>';
    }).join('');
    _results.querySelectorAll('.sr-item').forEach(function(a) {
      a.addEventListener('click', closeSearch);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectSearch);
  } else { injectSearch(); }
})();
