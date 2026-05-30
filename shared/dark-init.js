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

// XP badge — shows level name + mini progress bar
(function(){
  function injectXP() {
    var inner = document.querySelector('.site-header-inner');
    if (!inner || inner.querySelector('.header-xp') || !window.FCEStore) return;
    var lv   = FCEStore.getXPLevel();
    var pct  = lv.pct;
    var next = lv.max ? lv.xp + ' / ' + lv.max : lv.xp + ' XP';
    var badge = document.createElement('div');
    badge.className = 'header-xp';
    badge.title = next + ' XP';
    badge.innerHTML =
      '<span class="header-xp-label">' + lv.label + '</span>' +
      '<div class="header-xp-bar"><div class="header-xp-fill" style="width:' + pct + '%"></div></div>';
    var utils = inner.querySelector('.header-utils');
    if (utils) inner.insertBefore(badge, utils);
    else inner.appendChild(badge);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectXP);
  } else { injectXP(); }
})();

// Chapter search — icon in header, panel below
(function(){
  var _loaded = false;
  var _panel  = null;
  var _input  = null;
  var _results = null;

  function injectSearch() {
    var inner = document.querySelector('.site-header-inner');
    if (!inner || inner.querySelector('.header-search-btn')) return;

    var btn = document.createElement('button');
    btn.className = 'header-search-btn';
    btn.setAttribute('aria-label', 'Search chapters');
    btn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>';
    btn.onclick = toggleSearch;

    var utils = inner.querySelector('.header-utils');
    if (utils) inner.insertBefore(btn, utils);
    else inner.appendChild(btn);
  }

  function ensurePanel() {
    if (_panel) return;
    _panel = document.createElement('div');
    _panel.className = 'header-search-panel';
    _panel.innerHTML =
      '<input class="header-search-input" type="search" placeholder="Search chapters…" autocomplete="off">' +
      '<div class="header-search-results"></div>';
    _input   = _panel.querySelector('.header-search-input');
    _results = _panel.querySelector('.header-search-results');

    var header = document.querySelector('.site-header');
    if (header && header.parentNode) header.after(_panel);
    else document.body.insertBefore(_panel, document.body.firstChild);

    _input.addEventListener('input', onInput);
    _input.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') { closeSearch(); }
    });
    document.addEventListener('click', function(e) {
      if (_panel.style.display !== 'none' && !_panel.contains(e.target) &&
          !e.target.closest('.header-search-btn')) {
        closeSearch();
      }
    }, true);
  }

  function toggleSearch() {
    ensurePanel();
    var open = _panel.style.display !== 'none' && _panel.style.display !== '';
    if (open) { closeSearch(); return; }
    _panel.style.display = 'block';
    _input.value = '';
    _results.innerHTML = '';
    setTimeout(function() { _input.focus(); }, 40);
    loadSearch();
  }

  function closeSearch() {
    if (_panel) { _panel.style.display = 'none'; }
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
    if (!q) { _results.innerHTML = ''; return; }
    if (!window.WPSearch) { loadSearch(); return; }
    if (!_loaded) {
      WPSearch.load(_SHARED + 'search-index.json', function() { onInput(); });
      _loaded = true;
      return;
    }
    var hits = WPSearch.search(q);
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
