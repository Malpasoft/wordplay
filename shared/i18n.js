// ══════════════════════════════════════════════════════════════════
// i18n.js — Shared internationalization utility
// Detects Spanish vs English and provides centralized L10N_STRINGS
// Consumers: game.js, worksheet.js, card-exercise.js, deck.js
// ══════════════════════════════════════════════════════════════════

(function () {
  'use strict';

  /**
   * Detect if the current page is in Spanish track.
   * Checks: DATA.level starts with 'es-' OR html lang='es'
   * @returns {boolean} true if Spanish, false if English
   */
  function isSpanish(level) {
    level = level || window.LEVEL || '';
    return level.indexOf('es-') === 0 || document.documentElement.lang === 'es';
  }

  /**
   * Centralized string catalog for all UI language.
   * Add all language pairs here — no hardcoded strings in modules.
   * Structure: { key: { es: '...', en: '...' } }
   */
  var L10N_STRINGS = {
    // game.js strings
    game_start:       { es: 'Empezar',                           en: 'Start' },
    game_resume:      { es: 'Continuar',                         en: 'Resume' },
    game_newGame:     { es: 'Empezar de nuevo',                  en: 'New game' },
    game_check:       { es: 'Comprobar',                         en: 'Check' },
    game_next:        { es: 'Continuar',                         en: 'Continue' },
    game_correct:     { es: '¡Correcto!',                        en: 'Correct!' },
    game_wrong:       { es: 'Incorrecto',                        en: 'Incorrect' },
    game_answer:      { es: 'Respuesta:',                        en: 'Answer:' },
    game_placeholder: { es: 'Escribe en inglés…',                en: 'Type your answer…' },
    game_sigLabel:    { es: 'Significado',                       en: 'Meaning' },
    game_ctxLabel:    { es: 'Contexto',                          en: 'Context' },
    game_prodLabel:   { es: 'Producción',                        en: 'Production' },
    game_sigSub:      { es: '¿Qué significa esta expresión?',    en: 'What does this expression mean?' },
    game_ctxSub:      { es: 'Completa la frase',                 en: 'Complete the sentence' },
    game_prodSub:     { es: 'Escribe la expresión en inglés',    en: 'Write the English expression' },
    game_desc_prefix: { es: 'conceptos clave · 3 rondas cada uno · llega a',
                        en: 'key concepts · 3 rounds each · reach' },
    game_toWin_suffix:{ es: 'para ganar',                        en: 'to win' },
    game_hint:        { es: 'Aciertos consecutivos del mismo concepto y rachas entre conceptos añaden puntos extra.',
                        en: 'Consecutive correct answers on the same concept and streaks across concepts add bonus points.' },

    // worksheet.js strings
    ws_check:         { es: 'Comprobar',                         en: 'Check' },
    ws_next:          { es: 'Siguiente',                         en: 'Next' },
    ws_correct:       { es: 'Correcto',                          en: 'Correct' },
    ws_wrong:         { es: 'Incorrecto',                        en: 'Incorrect' },
    ws_correctAns:    { es: 'Respuesta correcta:',               en: 'Correct answer:' },
    ws_remaining:     { es: 'restantes',                         en: 'remaining' },
    ws_typeHere:      { es: 'Escribe tu respuesta',              en: 'Type your answer' },
    ws_mcLabel:       { es: 'Elige la respuesta correcta',       en: 'Choose the correct answer' },
    ws_fillLabel:     { es: 'Rellena el hueco',                  en: 'Fill in the blank' },
    ws_transLabel:    { es: 'Traduce al inglés',                 en: 'Translate into English' },
    ws_prevBest:      { es: 'Mejor puntuación anterior:',        en: 'Previous best:' },
    ws_completed:     { es: 'Repaso completado',                 en: 'Review complete' },
    ws_wellDone:      { es: '¡Buen trabajo!',                    en: 'Well done!' },
    ws_keepGoing:     { es: '¡Sigue practicando!',               en: 'Keep practising!' },
    ws_noLives:       { es: 'Sin vidas',                         en: 'Out of lives' },
    ws_firstPass:     { es: 'A la primera:',                     en: 'First-pass score:' },
    ws_tryAgain:      { es: 'Intentar de nuevo',                 en: 'Try again' },
    ws_gameBtn:       { es: 'Ir al Juego de Dominio',            en: 'Start Mastery Game' },
    ws_seeResults:    { es: 'Ver resultados',                    en: 'See results' },
    ws_back:          { es: '← Volver al capítulo',              en: '← Back to chapter' },

    // deck.js strings
    deck_reviewStart:  { es: 'Empezar el Repaso',                 en: 'Start Review' },
    deck_complete:     { es: '¡Lección completada!',              en: 'Lesson complete!' },
    deck_wellDone:     { es: '¡Bien hecho!',                      en: 'Well done!' },
    deck_ready:        { es: 'Has terminado la lección. ¿Listo para repasar?', en: "You've finished this lesson. Ready to test yourself?" },
  };

  /**
   * Get a localized string by key.
   * @param {string} key - L10N_STRINGS key (e.g., 'game_start')
   * @param {boolean} [isEs] - Override Spanish detection (optional)
   * @returns {string} Localized string, or key if not found
   */
  function getString(key, isEs) {
    if (isEs === undefined) {
      isEs = window.i18n.isSpanish();
    }
    var entry = L10N_STRINGS[key];
    if (!entry) {
      console.warn('[i18n] Missing key: ' + key);
      return key;
    }
    return isEs ? entry.es : entry.en;
  }

  // Export to window.i18n namespace
  window.i18n = {
    isSpanish: isSpanish,
    L10N_STRINGS: L10N_STRINGS,
    getString: getString,
  };

})();
