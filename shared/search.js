// ══════════════════════════════════════════════════════════════════
// search.js — client-side chapter search
// Called by dark-init.js after lazy-loading on first keystroke.
// ══════════════════════════════════════════════════════════════════

(function() {
  'use strict';

  var _index = null;
  var _loading = false;

  function norm(s) {
    return (s || '').toLowerCase().replace(/[''`]/g, "'").replace(/[-–—]/g, ' ');
  }

  window.WPSearch = {
    load: function(indexUrl, cb) {
      if (_index) { cb(_index); return; }
      if (_loading) return;
      _loading = true;
      fetch(indexUrl)
        .then(function(r) { return r.json(); })
        .then(function(data) { _index = data; cb(_index); })
        .catch(function() { _index = []; cb(_index); });
    },

    search: function(query) {
      if (!_index || !query.trim()) return [];
      var terms = norm(query).split(/\s+/).filter(Boolean);
      var results = [];
      for (var i = 0; i < _index.length; i++) {
        var item = _index[i];
        var hay = norm(item.title + ' ' + item.level + ' ' + item.section);
        var score = 0;
        for (var t = 0; t < terms.length; t++) {
          if (hay.indexOf(terms[t]) === -1) { score = 0; break; }
          score += (hay.indexOf(terms[t]) === 0 || hay.indexOf(' ' + terms[t]) !== -1) ? 2 : 1;
        }
        if (score > 0) results.push({ item: item, score: score });
      }
      results.sort(function(a, b) { return b.score - a.score; });
      return results.slice(0, 6).map(function(r) { return r.item; });
    }
  };
})();
