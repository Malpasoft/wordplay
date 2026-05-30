// ══════════════════════════════════════════════════════════════════
// print.js v102 — printables hub: modal viewer, download, section printing
// ══════════════════════════════════════════════════════════════════

(function () {
  var SECTIONS = [
    { id: 'ph-lesson',    cls: 'ph-section-lesson',    key: 'lesson',    label: 'Lesson Reference' },
    { id: 'ph-worksheet', cls: 'ph-section-worksheet',  key: 'worksheet', label: 'Review Exercises' },
    { id: 'ph-key',       cls: 'ph-section-key',        key: 'key',       label: 'Answer Key'       },
  ];

  // ─── Wrap sections for @media print scoping ──────────────────
  function wrapSections() {
    for (var m = 0; m < SECTIONS.length; m++) {
      var anchor = document.getElementById(SECTIONS[m].id);
      if (!anchor) continue;

      var wrapper = document.createElement('div');
      wrapper.className = 'ph-section ' + SECTIONS[m].cls;

      anchor.parentNode.insertBefore(wrapper, anchor);
      wrapper.appendChild(anchor);

      var nextAnchorId = m < SECTIONS.length - 1 ? SECTIONS[m + 1].id : null;
      var sibling = wrapper.nextSibling;
      while (sibling) {
        var next = sibling.nextSibling;
        if (nextAnchorId && sibling.id === nextAnchorId) break;
        wrapper.appendChild(sibling);
        sibling = next;
      }
    }
  }

  // ─── Hide cards for sections that don't exist on this page ───
  function hideMissingSections() {
    var cards = document.querySelectorAll('.ph-hub-card');
    for (var i = 0; i < SECTIONS.length; i++) {
      if (!document.getElementById(SECTIONS[i].id) && cards[i]) {
        cards[i].style.display = 'none';
      }
    }
  }

  // ─── Intercept View button clicks → open modal instead ───────
  function interceptViewClicks() {
    var btns = document.querySelectorAll('.ph-hub-btn-view');
    for (var i = 0; i < btns.length; i++) {
      btns[i].addEventListener('click', function (e) {
        e.preventDefault();
        var href = this.getAttribute('href') || '';
        var section = href.replace('#ph-', '');
        wpView(section);
      });
    }
  }

  // ─── Inject Download buttons into each card + "Download all" ─
  function injectDownloadButtons() {
    var cards = document.querySelectorAll('.ph-hub-card');
    for (var i = 0; i < SECTIONS.length; i++) {
      if (!document.getElementById(SECTIONS[i].id)) continue;
      if (!cards[i]) continue;
      var dl = document.createElement('a');
      dl.href = '#';
      dl.className = 'ph-hub-btn-download';
      dl.textContent = 'Download HTML';
      dl.setAttribute('data-section', SECTIONS[i].key);
      dl.addEventListener('click', (function (key) {
        return function (e) { e.preventDefault(); wpDownload(key); };
      })(SECTIONS[i].key));
      cards[i].appendChild(dl);
    }

    // Wrap "Print all" + new "Download all" in a flex row
    var printAll = document.querySelector('.ph-hub-btn-all');
    if (printAll && printAll.parentNode) {
      var row = document.createElement('div');
      row.className = 'ph-hub-actions';
      printAll.parentNode.insertBefore(row, printAll);
      row.appendChild(printAll);
      var dlAll = document.createElement('button');
      dlAll.className = 'ph-hub-btn-all ph-hub-btn-dl-all';
      dlAll.textContent = 'Download all';
      dlAll.addEventListener('click', function () { wpDownloadAll(); });
      row.appendChild(dlAll);
    }
  }

  // ─── Modal: create once, reuse ───────────────────────────────
  function ensureModal() {
    if (document.getElementById('ph-modal')) return;
    var modal = document.createElement('div');
    modal.id = 'ph-modal';
    modal.className = 'ph-modal';
    modal.innerHTML =
      '<div class="ph-modal-scrim"></div>' +
      '<div class="ph-modal-inner">' +
        '<button class="ph-modal-close" aria-label="Close">&#x2715;</button>' +
        '<div class="ph-a4-frame" id="ph-modal-content"></div>' +
      '</div>';
    document.body.appendChild(modal);
    modal.querySelector('.ph-modal-scrim').addEventListener('click', wpCloseModal);
    modal.querySelector('.ph-modal-close').addEventListener('click', wpCloseModal);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') wpCloseModal();
    });
  }

  window.wpCloseModal = function () {
    var modal = document.getElementById('ph-modal');
    if (modal) modal.classList.remove('ph-modal-open');
    document.body.style.overflow = '';
  };

  // ─── Get cleaned content for a section ───────────────────────
  function getSectionContent(section) {
    var wrapper = document.querySelector('.ph-section-' + section);
    if (!wrapper) return null;
    var clone = wrapper.cloneNode(true);
    var strip = ['#ph-' + section, '.ph-hub', '.no-print', '.site-header',
                 '.site-footer', '.breadcrumb', '.chapter-nav'];
    strip.forEach(function (sel) {
      var els = clone.querySelectorAll(sel);
      for (var i = 0; i < els.length; i++) {
        if (els[i].parentNode) els[i].parentNode.removeChild(els[i]);
      }
    });
    return clone;
  }

  // ─── wpView: open modal with section A4 preview ──────────────
  window.wpView = function (section) {
    ensureModal();
    var content = getSectionContent(section);
    if (!content) return;
    var frame = document.getElementById('ph-modal-content');
    frame.innerHTML = '';
    while (content.firstChild) frame.appendChild(content.firstChild);
    var modal = document.getElementById('ph-modal');
    modal.classList.add('ph-modal-open');
    document.body.style.overflow = 'hidden';
    modal.querySelector('.ph-modal-inner').scrollTop = 0;
  };

  // ─── wpPrint: print one section only ─────────────────────────
  window.wpPrint = function (section) {
    document.body.classList.add('wp-print-' + section);
    window.print();
    document.body.classList.remove('wp-print-' + section);
  };

  // ─── Build a minimal standalone HTML document ─────────────────
  function buildDocument(contentHtml, title) {
    return '<!DOCTYPE html><html lang="en"><head>' +
      '<meta charset="UTF-8">' +
      '<meta name="viewport" content="width=device-width,initial-scale=1.0">' +
      '<title>' + (title || 'Word Play Printable') + '</title>' +
      '<style>' +
        '*{margin:0;padding:0;box-sizing:border-box}' +
        'body{font-family:Georgia,"Times New Roman",serif;font-size:11pt;color:#000;' +
             'background:#fff;padding:15mm 18mm 20mm;line-height:1.5}' +
        'h1{font-size:18pt;margin-bottom:3pt}' +
        'h2{font-size:13pt;margin:14pt 0 6pt;border-bottom:0.5pt solid #aaa;padding-bottom:3pt}' +
        '.meta{font-family:Arial,sans-serif;font-size:8pt;color:#666;letter-spacing:1pt;' +
              'text-transform:uppercase;margin-bottom:8pt}' +
        'p{margin-bottom:4pt}' +
        'hr{border:none;border-top:1pt solid #000;margin:8pt 0}' +
        'table{width:100%;border-collapse:collapse;margin-bottom:8pt;font-size:10pt}' +
        'th{font-family:Arial,sans-serif;font-size:8pt;font-weight:bold;background:#f0f0f0;' +
           'padding:5pt 8pt;border:0.5pt solid #ccc;text-align:left}' +
        'td{padding:5pt 8pt;border:0.5pt solid #ccc}' +
        '.q{margin-bottom:8pt;page-break-inside:avoid}' +
        '.q-num{font-family:Arial,sans-serif;font-size:8pt;font-weight:bold;margin-right:4pt}' +
        '.blank{display:inline-block;min-width:60pt;border-bottom:0.5pt solid #000}' +
        '.ans{margin-bottom:3pt;font-size:10pt}' +
        '.ans b{font-family:Arial,sans-serif;font-size:8pt;color:#333;margin-right:4pt}' +
        '.opts{font-family:Arial,sans-serif;font-size:9pt;margin:3pt 0 0 18pt}' +
        '.footer{margin-top:16pt;font-family:Arial,sans-serif;font-size:7pt;color:#999;' +
                'text-align:center;letter-spacing:1pt;text-transform:uppercase}' +
        '.note{font-family:Arial,sans-serif;font-size:8pt;color:#555;font-style:italic;' +
              'margin:3pt 0 6pt}' +
        '.nameline{font-size:9pt;color:#666;margin-bottom:8pt}' +
        '.ps{max-width:100%;margin:0}' +
        '.container{padding:0;max-width:100%}' +
        '.ps-ey{font-family:Arial,sans-serif;font-size:.6rem;font-weight:800;' +
               'letter-spacing:2.5px;text-transform:uppercase;color:#B8860B;margin-bottom:6px}' +
        '.ps-title{font-size:1.5rem;font-weight:700;font-family:Georgia,serif;' +
                  'margin-bottom:20px;padding-bottom:10px;border-bottom:2px solid #E5E5E5}' +
        '.ps-ex{margin-bottom:22px}' +
        '.ps-ex-h{font-family:Arial,sans-serif;font-size:.68rem;font-weight:800;' +
                 'letter-spacing:1.5px;text-transform:uppercase;color:#9A9A9A;margin-bottom:10px}' +
        '.ps-q{padding:8px 0;border-bottom:1px solid #E5E5E5;font-size:.9rem;min-height:28px}' +
        '.ps-blank{display:inline-block;min-width:80px;border-bottom:1.5px solid #1A1A1A}' +
        '@page{size:A4;margin:12mm 15mm 15mm}' +
        '@media print{.no-print,.site-header,.chapter-nav,.breadcrumb{display:none!important}}' +
      '</style>' +
      '</head><body>' + contentHtml + '</body></html>';
  }

  // ─── wpDownload: download one section as HTML file ───────────
  window.wpDownload = function (section) {
    var content = getSectionContent(section);
    if (!content) return;
    var labels = { lesson: 'Lesson Reference', worksheet: 'Review Exercises', key: 'Answer Key' };
    var html = buildDocument(content.innerHTML, 'Word Play — ' + (labels[section] || section));
    var blob = new Blob([html], { type: 'text/html' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'wordplay-' + section + '.html';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
  };

  // ─── wpDownloadAll: download all sections in one HTML file ───
  window.wpDownloadAll = function () {
    var parts = [];
    for (var i = 0; i < SECTIONS.length; i++) {
      var content = getSectionContent(SECTIONS[i].key);
      if (!content) continue;
      if (parts.length > 0) parts.push('<div style="page-break-before:always"></div>');
      parts.push(content.innerHTML);
    }
    if (!parts.length) return;
    var html = buildDocument(parts.join('\n'), 'Word Play — Printables');
    var blob = new Blob([html], { type: 'text/html' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'wordplay-printables.html';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
  };

  // ─── Init ────────────────────────────────────────────────────
  function init() {
    wrapSections();
    hideMissingSections();
    interceptViewClicks();
    injectDownloadButtons();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
