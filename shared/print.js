// ══════════════════════════════════════════════════════════════════
// print.js v101 — section-specific printing for printables pages
// ══════════════════════════════════════════════════════════════════

(function () {
  // Wrap print sections at runtime so print.css can target them
  function wrapSections() {
    var markers = [
      { id: 'ph-lesson',    cls: 'ph-section-lesson'    },
      { id: 'ph-worksheet', cls: 'ph-section-worksheet' },
      { id: 'ph-key',       cls: 'ph-section-key'       },
    ];

    for (var m = 0; m < markers.length; m++) {
      var anchor = document.getElementById(markers[m].id);
      if (!anchor) continue;

      var wrapper  = document.createElement('div');
      wrapper.className = 'ph-section ' + markers[m].cls;

      // Insert wrapper before the anchor, then move anchor into it
      anchor.parentNode.insertBefore(wrapper, anchor);
      wrapper.appendChild(anchor);

      // Move subsequent siblings into wrapper until the next section anchor
      var nextAnchorId = m < markers.length - 1 ? markers[m + 1].id : null;
      var sibling = wrapper.nextSibling;
      while (sibling) {
        var next = sibling.nextSibling;
        if (nextAnchorId && sibling.id === nextAnchorId) break;
        wrapper.appendChild(sibling);
        sibling = next;
      }
    }
  }

  // Print only one section
  window.wpPrint = function (section) {
    document.body.classList.add('wp-print-' + section);
    window.print();
    document.body.classList.remove('wp-print-' + section);
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wrapSections);
  } else {
    wrapSections();
  }
})();
