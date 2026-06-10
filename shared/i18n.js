// ══════════════════════════════════════════════════════════════════
// i18n.js — Shared internationalization utility
// Detects the page language (Spanish / French / English) and provides
// the centralized L10N_STRINGS catalog.
// Consumers: game.js, worksheet.js, card-exercise.js, deck.js
// Detection: es → DATA.level starts with 'es-' OR html lang='es'
//            fr → html lang='fr' (used by the fr/ track)
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
   * Detect if the current page is in the French track.
   * @returns {boolean} true if French UI should be used
   */
  function isFrench(level) {
    level = level || window.LEVEL || '';
    return level.indexOf('fr-') === 0 || document.documentElement.lang === 'fr';
  }

  /**
   * Resolve the UI language code for the current page.
   * @returns {string} 'es' | 'fr' | 'en'
   */
  function getLang(level) {
    if (isSpanish(level)) return 'es';
    if (isFrench(level)) return 'fr';
    return 'en';
  }

  /**
   * Centralized string catalog for all UI language.
   * Add all language triples here — no hardcoded strings in modules.
   * Structure: { key: { es: '...', fr: '...', en: '...' } }
   */
  var L10N_STRINGS = {
    // game.js strings
    game_start:       { es: 'Empezar',                           fr: 'Commencer',                       en: 'Start' },
    game_resume:      { es: 'Continuar',                         fr: 'Reprendre',                       en: 'Resume' },
    game_newGame:     { es: 'Empezar de nuevo',                  fr: 'Nouvelle partie',                 en: 'New game' },
    game_check:       { es: 'Comprobar',                         fr: 'Vérifier',                        en: 'Check' },
    game_next:        { es: 'Continuar',                         fr: 'Continuer',                       en: 'Continue' },
    game_correct:     { es: '¡Correcto!',                        fr: 'Correct !',                       en: 'Correct!' },
    game_wrong:       { es: 'Incorrecto',                        fr: 'Incorrect',                       en: 'Incorrect' },
    game_answer:      { es: 'Respuesta:',                        fr: 'Réponse :',                       en: 'Answer:' },
    game_placeholder: { es: 'Escribe en inglés…',                fr: 'Écris en anglais…',               en: 'Type your answer…' },
    game_sigLabel:    { es: 'Significado',                       fr: 'Sens',                            en: 'Meaning' },
    game_ctxLabel:    { es: 'Contexto',                          fr: 'Contexte',                        en: 'Context' },
    game_prodLabel:   { es: 'Producción',                        fr: 'Production',                      en: 'Production' },
    game_sigSub:      { es: '¿Qué significa esta expresión?',    fr: 'Que signifie cette expression ?', en: 'What does this expression mean?' },
    game_ctxSub:      { es: 'Completa la frase',                 fr: 'Complète la phrase',              en: 'Complete the sentence' },
    game_prodSub:     { es: 'Escribe la expresión en inglés',    fr: "Écris l'expression en anglais",   en: 'Write the English expression' },
    game_desc_prefix: { es: 'conceptos clave · 3 rondas cada uno · llega a',
                        fr: 'concepts clés · 3 manches chacun · atteins',
                        en: 'key concepts · 3 rounds each · reach' },
    game_toWin_suffix:{ es: 'para ganar',                        fr: 'pour gagner',                     en: 'to win' },
    game_hint:        { es: 'Aciertos consecutivos del mismo concepto y rachas entre conceptos añaden puntos extra.',
                        fr: 'Les bonnes réponses consécutives sur le même concept et les séries entre concepts donnent des points bonus.',
                        en: 'Consecutive correct answers on the same concept and streaks across concepts add bonus points.' },

    // worksheet.js strings
    ws_check:         { es: 'Comprobar',                         fr: 'Vérifier',                        en: 'Check' },
    ws_next:          { es: 'Siguiente',                         fr: 'Suivant',                         en: 'Next' },
    ws_correct:       { es: 'Correcto',                          fr: 'Correct',                         en: 'Correct' },
    ws_wrong:         { es: 'Incorrecto',                        fr: 'Incorrect',                       en: 'Incorrect' },
    ws_correctAns:    { es: 'Respuesta correcta:',               fr: 'Bonne réponse :',                 en: 'Correct answer:' },
    ws_remaining:     { es: 'restantes',                         fr: 'restantes',                       en: 'remaining' },
    ws_typeHere:      { es: 'Escribe tu respuesta',              fr: 'Écris ta réponse',                en: 'Type your answer' },
    ws_mcLabel:       { es: 'Elige la respuesta correcta',       fr: 'Choisis la bonne réponse',        en: 'Choose the correct answer' },
    ws_fillLabel:     { es: 'Rellena el hueco',                  fr: 'Complète la phrase',              en: 'Fill in the blank' },
    ws_transLabel:    { es: 'Traduce al inglés',                 fr: 'Traduis en anglais',              en: 'Translate into English' },
    ws_prevBest:      { es: 'Mejor puntuación anterior:',        fr: 'Meilleur score précédent :',      en: 'Previous best:' },
    ws_completed:     { es: 'Repaso completado',                 fr: 'Révision terminée',               en: 'Review complete' },
    ws_wellDone:      { es: '¡Buen trabajo!',                    fr: 'Bravo !',                         en: 'Well done!' },
    ws_keepGoing:     { es: '¡Sigue practicando!',               fr: "Continue à t'entraîner !",        en: 'Keep practising!' },
    ws_noLives:       { es: 'Sin vidas',                         fr: 'Plus de vies',                    en: 'Out of lives' },
    ws_firstPass:     { es: 'A la primera:',                     fr: 'Score du premier essai :',        en: 'First-pass score:' },
    ws_tryAgain:      { es: 'Intentar de nuevo',                 fr: 'Réessayer',                       en: 'Try again' },
    ws_gameBtn:       { es: 'Ir al Juego de Dominio',            fr: 'Aller au Jeu de Maîtrise',        en: 'Start Mastery Game' },
    ws_seeResults:    { es: 'Ver resultados',                    fr: 'Voir les résultats',              en: 'See results' },
    ws_back:          { es: '← Volver al capítulo',              fr: '← Retour au chapitre',            en: '← Back to chapter' },

    // deck.js strings
    deck_reviewStart:  { es: 'Empezar el Repaso',                 fr: 'Commencer les exercices',         en: 'Start Review' },
    deck_complete:     { es: '¡Lección completada!',              fr: 'Leçon terminée !',                en: 'Lesson complete!' },
    deck_wellDone:     { es: '¡Bien hecho!',                      fr: 'Bien joué !',                     en: 'Well done!' },
    deck_ready:        { es: 'Has terminado la lección. ¿Listo para repasar?',
                         fr: "Tu as terminé la leçon. Prêt à t'entraîner ?",
                         en: "You've finished this lesson. Ready to test yourself?" },
  };

  /**
   * Get a localized string by key.
   * @param {string} key - L10N_STRINGS key (e.g., 'game_start')
   * @param {boolean} [isEs] - Override Spanish detection (optional, legacy)
   * @returns {string} Localized string, or key if not found
   */
  function getString(key, isEs) {
    var entry = L10N_STRINGS[key];
    if (!entry) {
      console.warn('[i18n] Missing key: ' + key);
      return key;
    }
    var lang;
    if (isEs === undefined) {
      lang = getLang();
    } else {
      lang = isEs ? 'es' : (isFrench() ? 'fr' : 'en');
    }
    return entry[lang] || entry.en;
  }

  // Export to window.i18n namespace
  window.i18n = {
    isSpanish: isSpanish,
    isFrench: isFrench,
    getLang: getLang,
    L10N_STRINGS: L10N_STRINGS,
    getString: getString,
  };

})();
