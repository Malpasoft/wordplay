// Bee mascot state manager and click handler.
// Manages animation state (idle, fly, spell, walk, happy, sad).
// Single click listener cycles through all states.

(function() {
  'use strict';

  var ALLOWED_STATES = ['idle', 'fly', 'spell', 'walk', 'happy', 'sad'];
  var STATE_CYCLE = ['idle', 'happy', 'fly', 'spell', 'walk', 'sad'];
  var MASCOT_KEY = 'wordplay_bee_state';
  var ANIMATION_DURATION = 3000; // ms
  var IDLE_STATE = 'idle';

  var currentState = IDLE_STATE;
  var autoRevertTimer = null;
  var mascot = null;

  // Initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    try {
      mascot = document.getElementById('mascot');
      if (!mascot) return; // Mascot not on this page

      // Load saved state from localStorage
      var savedState = localStorage.getItem(MASCOT_KEY);
      if (savedState && ALLOWED_STATES.indexOf(savedState) !== -1) {
        currentState = savedState;
        applyState(currentState);
      }

      // Attach click handler
      mascot.addEventListener('click', handleClick);

      // Keyboard a11y: space/enter also click
      mascot.addEventListener('keydown', function(e) {
        if (e.key === ' ' || e.key === 'Enter') {
          e.preventDefault();
          handleClick();
        }
      });

    } catch (e) {
      console.error('Mascot init failed:', e);
    }
  }

  function handleClick() {
    try {
      // Clear any pending auto-revert
      if (autoRevertTimer) clearTimeout(autoRevertTimer);

      // Cycle to next state
      var currentIdx = STATE_CYCLE.indexOf(currentState);
      var nextIdx = (currentIdx + 1) % STATE_CYCLE.length;
      var nextState = STATE_CYCLE[nextIdx];

      setBeeState(nextState);

      // Auto-revert to idle after animation duration
      if (nextState !== IDLE_STATE) {
        autoRevertTimer = setTimeout(function() {
          setBeeState(IDLE_STATE);
        }, ANIMATION_DURATION);
      }

    } catch (e) {
      console.error('Click handler failed:', e);
    }
  }

  function setBeeState(stateName) {
    try {
      // Validate state
      if (ALLOWED_STATES.indexOf(stateName) === -1) {
        console.warn('Invalid bee state:', stateName);
        return;
      }

      if (!mascot) return;

      // Remove all state classes
      ALLOWED_STATES.forEach(function(state) {
        mascot.classList.remove('bee-' + state);
      });

      // Apply new state
      mascot.classList.add('bee-' + stateName);
      currentState = stateName;

      // Persist to localStorage
      localStorage.setItem(MASCOT_KEY, stateName);

    } catch (e) {
      console.error('setBeeState failed:', e);
    }
  }

  function applyState(stateName) {
    // Apply state without persisting (used on init)
    if (!mascot || ALLOWED_STATES.indexOf(stateName) === -1) return;
    ALLOWED_STATES.forEach(function(state) {
      mascot.classList.remove('bee-' + state);
    });
    mascot.classList.add('bee-' + stateName);
    currentState = stateName;
  }

  // Expose API for external control (e.g., from game.js, worksheet.js)
  window.setBeeState = setBeeState;

})();
