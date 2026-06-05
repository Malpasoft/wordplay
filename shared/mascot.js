// Bee mascot state manager with frame-based animation.
// Manages animation state (idle, fly, spell, walk, happy, sad).
// Uses JavaScript frame cycling instead of CSS animations for reliability.

(function() {
  'use strict';

  var ALLOWED_STATES = ['idle', 'fly', 'spell', 'walk', 'happy', 'sad'];
  var STATE_CYCLE = ['idle', 'happy', 'fly', 'spell', 'walk', 'sad'];
  var MASCOT_KEY = 'wordplay_bee_state';
  var ANIMATION_DURATION = 3000;
  var IDLE_STATE = 'idle';

  var ROW_OFFSETS = {idle: 0, fly: -48, spell: -96, walk: -144, happy: -192, sad: -240};
  var FRAME_COUNT = 4;
  var FRAME_DURATION = 200; // ms per frame (0.8s / 4 frames)
  var IDLE_FRAME_DURATION = 300; // ms per frame for idle (1.2s / 4 frames)

  var currentState = IDLE_STATE;
  var autoRevertTimer = null;
  var animationFrame = null;
  var mascot = null;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    try {
      mascot = document.getElementById('mascot');
      if (!mascot) return;

      var savedState = localStorage.getItem(MASCOT_KEY);
      if (savedState && ALLOWED_STATES.indexOf(savedState) !== -1) {
        currentState = savedState;
        applyState(currentState);
      } else {
        applyState(IDLE_STATE);
      }

      mascot.addEventListener('click', handleClick);
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
      if (autoRevertTimer) clearTimeout(autoRevertTimer);
      var currentIdx = STATE_CYCLE.indexOf(currentState);
      var nextIdx = (currentIdx + 1) % STATE_CYCLE.length;
      var nextState = STATE_CYCLE[nextIdx];
      setBeeState(nextState);

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
      if (ALLOWED_STATES.indexOf(stateName) === -1) {
        console.warn('Invalid bee state:', stateName);
        return;
      }

      if (!mascot) return;

      ALLOWED_STATES.forEach(function(state) {
        mascot.classList.remove('bee-' + state);
      });

      mascot.classList.add('bee-' + stateName);
      currentState = stateName;
      localStorage.setItem(MASCOT_KEY, stateName);

      startFrameAnimation(stateName);

    } catch (e) {
      console.error('setBeeState failed:', e);
    }
  }

  function applyState(stateName) {
    if (!mascot || ALLOWED_STATES.indexOf(stateName) === -1) return;
    ALLOWED_STATES.forEach(function(state) {
      mascot.classList.remove('bee-' + state);
    });
    mascot.classList.add('bee-' + stateName);
    currentState = stateName;
    startFrameAnimation(stateName);
  }

  function startFrameAnimation(stateName) {
    try {
      if (!mascot) return;

      if (animationFrame) clearInterval(animationFrame);

      var rowOffset = ROW_OFFSETS[stateName];
      var frameIdx = 0;
      var isIdleState = (stateName === IDLE_STATE);
      var frameTiming = isIdleState ? IDLE_FRAME_DURATION : FRAME_DURATION;
      var loopCount = 0;

      function showFrame() {
        var frameX = frameIdx * -48; // 0px, -48px, -96px, -144px
        mascot.style.backgroundPosition = frameX + 'px ' + rowOffset + 'px';

        if (isIdleState) {
          // Idle loops infinitely
          frameIdx = (frameIdx + 1) % FRAME_COUNT;
        } else {
          // Other states: play 4 frames then hold last frame
          if (frameIdx < FRAME_COUNT - 1) {
            frameIdx++;
          }
        }
      }

      showFrame();
      animationFrame = setInterval(showFrame, frameTiming);

    } catch (e) {
      console.error('startFrameAnimation failed:', e);
    }
  }

  window.setBeeState = setBeeState;

})();
