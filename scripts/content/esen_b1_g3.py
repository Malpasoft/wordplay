# -*- coding: utf-8 -*-
"""espanol-en B1 grammar content — batch 3 (chapters G11-G15)."""

CHAPTERS = {

'modal-could-might-advanced': dict(
  num='G11', short='Could & Might', title='Could & Might — Posibilidad en español',
  subtitle='podría, a lo mejor, quizás: expressing possibility and past ability',
  slides=[
    ('Two ways to say "could" in the past', None,
     '<p class="slide-explanation">English "could" hides two different Spanish past tenses. For general past ability, use the imperfect <b>podía</b>; for managing to do something on one occasion, use the preterite <b>pude</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>De niño podía correr muy rápido.</b> (As a child I could run very fast — general ability.)</p>'
     '<p style="margin-top:8px"><b>Por fin pude abrir la puerta.</b> (I finally managed to open the door — one occasion.)</p></div>'
     '<p style="margin-top:16px">Rule of thumb: could = <b>podía</b>; managed to / succeeded in = <b>pude</b>.</p>'),
    ('Podría — could / might for the future', None,
     '<p class="slide-explanation">For polite suggestions and future possibility, Spanish uses the conditional <b>podría</b> — exactly like English "could/might".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Podríamos ir al cine esta noche.</b> (We could go to the cinema tonight.)</p>'
     '<p style="margin-top:8px"><b>¿Podrías ayudarme con esto?</b> (Could you help me with this?)</p>'
     '<p style="margin-top:8px"><b>Podría llover mañana.</b> (It might rain tomorrow.)</p></div>'
     '<p style="margin-top:16px">Conjugation is regular: podría, podrías, podría, podríamos, podríais, podrían.</p>'),
    ('A lo mejor — maybe, with the indicative', None,
     '<p class="slide-explanation">The everyday way to say "maybe" is <b>a lo mejor</b> — and the good news for learners is that it always takes the ordinary <b>indicative</b>, never the subjunctive.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>A lo mejor voy mañana.</b> (Maybe I will go tomorrow.)</p>'
     '<p style="margin-top:8px"><b>A lo mejor está enfermo.</b> (Maybe he is ill.)</p></div>'
     '<p style="margin-top:16px">In conversation, a lo mejor is the safest "maybe" — no special verb forms needed.</p>'),
    ('Quizás and tal vez — maybe, with the subjunctive', None,
     '<p class="slide-explanation"><b>Quizás</b> (or quizá) and <b>tal vez</b> also mean "maybe", but they usually take the <b>subjunctive</b> when the doubt is real.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Quizás venga más tarde.</b> (Maybe he will come later — venga = subjunctive of venir.)</p>'
     '<p style="margin-top:8px"><b>Tal vez sea verdad.</b> (Maybe it is true — sea = subjunctive of ser.)</p></div>'
     '<p style="margin-top:16px">With the indicative (quizás viene) the speaker sounds more certain. At B1, learn the pattern quizás + subjunctive.</p>'),
    ('Puede que + subjunctive', None,
     '<p class="slide-explanation">A very common B1 structure: <b>puede que + subjunctive</b> = "it may be that / might".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Puede que llegue tarde.</b> (I might arrive late.)</p>'
     '<p style="margin-top:8px"><b>Puede que no lo sepan.</b> (They might not know.)</p></div>'
     '<p style="margin-top:16px">Your possibility toolkit: <b>a lo mejor</b> + indicative · <b>quizás / tal vez</b> + subjunctive · <b>puede que</b> + subjunctive · <b>podría</b> + infinitive.</p>'),
  ],
  traps=[
    ('Pude nadar cuando era niño.', '<strong>Podía</strong> nadar cuando era niño.', 'General past ability uses the imperfect podía — pude means "I managed to" on one occasion'),
    ('A lo mejor venga mañana.', 'A lo mejor <strong>viene</strong> mañana.', 'A lo mejor always takes the indicative — never the subjunctive'),
    ('Puede que viene esta tarde.', 'Puede que <strong>venga</strong> esta tarde.', 'Puede que requires the subjunctive: puede que venga'),
    ('¿Puedes ayudarme? (to a stranger, too direct)', '¿<strong>Podría(s)</strong> ayudarme?', 'The conditional podría softens requests — like English "could you" vs "can you"'),
    ('Quizás es tarde, no sé...', 'Quizás <strong>sea</strong> tarde.', 'When the doubt is real, quizás takes the subjunctive: quizás sea'),
  ],
  summary=[
    ('Past ability', 'podía + infinitive', 'Podía correr muy rápido.'),
    ('Managed to', 'pude + infinitive', 'Por fin pude abrir la puerta.'),
    ('Could (future/polite)', 'podría + infinitive', '¿Podrías ayudarme?'),
    ('Maybe + indicative', 'a lo mejor + indicative', 'A lo mejor voy mañana.'),
    ('Maybe + subjunctive', 'quizás / tal vez + subjunctive', 'Quizás venga más tarde.'),
    ('Might', 'puede que + subjunctive', 'Puede que llegue tarde.'),
  ],
  ex1=('Choose the right form', 'Possibility and past ability.', [
    ('De joven, mi abuelo ______ levantar 100 kilos.', ['podía', 'pudo', 'podría'], 'podía',
     'General past ability → imperfect: podía levantar.'),
    ('Ayer por fin ______ terminar el proyecto.', ['pude', 'podía', 'puedo'], 'pude',
     'Managed to (one occasion) → preterite: pude terminar.'),
    ('______ ir a la playa este fin de semana, ¿no?', ['Podríamos', 'Pudimos', 'Podíamos'], 'Podríamos',
     'A suggestion about the future → conditional: podríamos ir.'),
    ('A lo mejor ______ a vernos el domingo.', ['viene', 'venga', 'vendría'], 'viene',
     'A lo mejor + INDICATIVE: a lo mejor viene.'),
    ('Puede que ______ tarde al trabajo.', ['llegue', 'llega', 'llegaré'], 'llegue',
     'Puede que + SUBJUNCTIVE: puede que llegue.'),
    ('Quizás ______ verdad lo que dice.', ['sea', 'es', 'será'], 'sea',
     'Quizás + subjunctive when doubt is real: quizás sea.'),
  ]),
  ex2=('Type the missing form', 'Write the Spanish verb form.', [
    ('Could you (tú) help me? → ¿______ ayudarme? (conditional of poder)', 'podrías',
     'Polite request → conditional: ¿PODRÍAS ayudarme?'),
    ('Maybe he is ill. → A lo mejor ______ enfermo. (estar, indicative)', 'está',
     'A lo mejor + indicative: a lo mejor ESTÁ enfermo.'),
    ('It might rain. → Puede que ______. (llover, subjunctive: llueva/llueve?)', 'llueva',
     'Puede que + subjunctive: puede que LLUEVA.'),
    ('As a child I could swim. → De niño ______ nadar. (poder, imperfect)', 'podía',
     'General past ability → imperfect: PODÍA nadar.'),
    ('We finally managed to enter. → Por fin ______ entrar. (poder, preterite, nosotros)', 'pudimos',
     'Managed to → preterite: PUDIMOS entrar.'),
  ]),
  ex3=('Which sentence is correct?', 'Watch the mood after each "maybe".', [
    ('Maybe they will come:', ['A lo mejor vienen.', 'A lo mejor vengan.', 'A lo mejor vendrán venga.'], 'A lo mejor vienen.',
     'A lo mejor + indicative: vienen.'),
    ('He might not know:', ['Puede que no lo sepa.', 'Puede que no lo sabe.', 'Puede que no lo sabrá.'], 'Puede que no lo sepa.',
     'Puede que + subjunctive: sepa (from saber).'),
    ('Could you (usted) open the window?', ['¿Podría abrir la ventana?', '¿Pudo abrir la ventana?', '¿Podía abrir la ventana?'], '¿Podría abrir la ventana?',
     'Polite request → conditional podría.'),
    ('I could read at age four (ability):', ['Podía leer a los cuatro años.', 'Pude leer a los cuatro años.', 'Podría leer a los cuatro años.'], 'Podía leer a los cuatro años.',
     'General ability in the past → imperfect podía.'),
    ('Maybe it is true:', ['Tal vez sea verdad.', 'Tal vez siendo verdad.', 'Tal vez fuera será verdad.'], 'Tal vez sea verdad.',
     'Tal vez + present subjunctive: sea.'),
  ]),
  game_desc='Each possibility structure passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('podia', 'podía', 'could (general past ability)', 'imperfect of poder', 'De niño <b>podía</b> correr muy rápido.', 'De niño ______ correr muy rápido. (could)', 'podía', ),
    ('pude', 'pude', 'I managed to (one occasion)', 'preterite of poder', 'Por fin <b>pude</b> abrir la puerta.', 'Por fin ______ abrir la puerta. (managed to)', 'pude'),
    ('podria', 'podría', 'could / might (conditional)', 'polite or future', '¿<b>Podrías</b> ayudarme con esto?', '¿______ ayudarme con esto? (could you, tú)', 'podrías'),
    ('a-lo-mejor', 'a lo mejor', 'maybe — always + indicative', 'everyday maybe', '<b>A lo mejor</b> voy mañana.', 'A lo ______ voy mañana. (maybe)', 'mejor'),
    ('quizas', 'quizás + subjunctive', 'maybe — with real doubt', 'formal maybe', '<b>Quizás venga</b> más tarde.', 'Quizás ______ más tarde. (he may come — subjunctive)', 'venga'),
    ('tal-vez', 'tal vez', 'maybe / perhaps', 'synonym of quizás', '<b>Tal vez</b> sea verdad.', 'Tal ______ sea verdad. (maybe)', 'vez'),
    ('puede-que', 'puede que + subjunctive', 'it may be that / might', 'possibility', '<b>Puede que</b> llegue tarde.', '______ que llegue tarde. (it may be)', 'puede'),
    ('podriamos', 'podríamos', 'we could (suggestion)', 'suggesting plans', '<b>Podríamos</b> ir al cine esta noche.', '______ ir al cine esta noche. (we could)', 'podríamos'),
  ],
),

'modal-must-should-advanced': dict(
  num='G12', short='Must & Should', title='Must & Should — Obligación en español',
  subtitle='deber, tener que, hay que: obligation, advice and deduction',
  slides=[
    ('Tener que — the everyday "have to"', None,
     '<p class="slide-explanation">The most common way to express obligation is <b>tener que + infinitive</b>. It conjugates like tener and works in every tense.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Tengo que estudiar esta noche.</b> (I have to study tonight.)</p>'
     '<p style="margin-top:8px"><b>Tuvimos que esperar dos horas.</b> (We had to wait two hours.)</p></div>'
     '<p style="margin-top:16px">Tener que expresses external, practical obligation — deadlines, rules, circumstances.</p>'),
    ('Deber — should / must (advice and duty)', None,
     '<p class="slide-explanation"><b>Deber + infinitive</b> expresses moral duty or strong advice. In the conditional (<b>debería</b>) it softens to English "should".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Debes descansar más.</b> (You must rest more.)</p>'
     '<p style="margin-top:8px"><b>Deberías hablar con ella.</b> (You should talk to her.)</p></div>'
     '<p style="margin-top:16px">Debería is the polite adviser\'s form — perfect for giving recommendations in writing exams.</p>'),
    ('Deber de — deduction, not obligation', None,
     '<p class="slide-explanation">Add <b>de</b> and the meaning changes completely: <b>deber de + infinitive</b> = deduction ("must be" in the sense of probability).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Deben de ser las diez.</b> (It must be ten o\'clock — I deduce.)</p>'
     '<p style="margin-top:8px"><b>Debe de estar cansado.</b> (He must be tired — guessing.)</p></div>'
     '<p style="margin-top:16px">Compare: <b>Debe estudiar</b> (he must study — duty) vs <b>Debe de estudiar mucho</b> (he must study a lot — I deduce it from his grades).</p>'),
    ('Hay que — impersonal obligation', None,
     '<p class="slide-explanation"><b>Hay que + infinitive</b> states what "one must" do — no subject, totally impersonal. English has no exact equivalent; the closest is "you have to / it is necessary to".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hay que reservar con antelación.</b> (You have to book in advance.)</p>'
     '<p style="margin-top:8px"><b>Hay que tener paciencia.</b> (One must be patient.)</p></div>'
     '<p style="margin-top:16px">Use hay que for rules and general advice; use tengo que when the obligation is yours personally.</p>'),
    ('Saying what you must NOT do', None,
     '<p class="slide-explanation">Careful — the negatives don\'t map onto English neatly.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>No debes fumar aquí.</b> (You mustn\'t smoke here — prohibition.)</p>'
     '<p style="margin-top:8px"><b>No tienes que venir.</b> (You don\'t have to come — no obligation, it\'s optional!)</p>'
     '<p style="margin-top:8px"><b>No hay que pagar entrada.</b> (You don\'t need to pay an entrance fee.)</p></div>'
     '<p style="margin-top:16px">English speakers\' classic trap: <b>no tener que</b> = absence of obligation, NOT prohibition. "You mustn\'t" = no debes.</p>'),
  ],
  traps=[
    ('Debo de estudiar para el examen. (meaning duty)', '<strong>Debo estudiar</strong> para el examen.', 'Obligation is deber WITHOUT de — deber de means "probably"'),
    ('Es necesario que comprar pan.', '<strong>Hay que</strong> comprar pan.', 'Impersonal obligation is hay que + infinitive — simple and natural'),
    ('No tienes que fumar aquí. (meaning prohibition)', '<strong>No debes</strong> fumar aquí.', 'No tener que = "don\'t have to" (optional). Prohibition needs no deber'),
    ('Tengo que estudiar, tengo que trabajar, tengo que... (overuse)', 'Variety: <strong>debo / hay que / debería</strong>', 'Vary your obligation verbs — examiners reward range'),
    ('Deberías de hablar con ella.', '<strong>Deberías hablar</strong> con ella.', 'Advice = debería + infinitive without de (deber de = deduction only)'),
  ],
  summary=[
    ('Have to', 'tener que + infinitive', 'Tengo que estudiar esta noche.'),
    ('Must / duty', 'deber + infinitive', 'Debes descansar más.'),
    ('Should', 'debería + infinitive', 'Deberías hablar con ella.'),
    ('Must be (deduction)', 'deber de + infinitive', 'Deben de ser las diez.'),
    ('Impersonal', 'hay que + infinitive', 'Hay que reservar con antelación.'),
    ('Don\'t have to vs mustn\'t', 'no tener que ≠ no deber', 'No tienes que venir. / No debes fumar.'),
  ],
  ex1=('Choose the right obligation', 'tener que, deber, deber de or hay que?', [
    ('______ reservar mesa — el restaurante siempre está lleno. (impersonal)', ['Hay que', 'Tiene que', 'Debe de'], 'Hay que',
     'General rule, no subject → HAY QUE reservar.'),
    ('Son las diez y no ha llegado. ______ estar enfermo.', ['Debe de', 'Debe', 'Hay que'], 'Debe de',
     'Deduction → DEBER DE: debe de estar enfermo.'),
    ('Mañana ______ levantarme a las seis. (personal obligation)', ['tengo que', 'hay que', 'debo de'], 'tengo que',
     'Personal, practical obligation → TENGO QUE levantarme.'),
    ('______ comer menos azúcar — te lo dice el médico. (advice)', ['Deberías', 'Tendrás que', 'Habrá que'], 'Deberías',
     'Advice → conditional DEBERÍAS comer.'),
    ('No ______ pagar — la entrada es gratis.', ['hay que', 'debes de', 'deberías de'], 'hay que',
     'No need to pay (no obligation) → NO HAY QUE pagar.'),
    ('"You mustn\'t use your phone in class" = No ______ usar el móvil en clase.', ['debes', 'tienes que', 'debes de'], 'debes',
     'Prohibition → NO DEBES. (No tienes que = it\'s optional!)'),
  ]),
  ex2=('Translate the obligation', 'Type the missing Spanish words.', [
    ('I have to work on Saturday. → ______ que trabajar el sábado. (one word)', 'tengo',
     'Personal obligation: TENGO que trabajar.'),
    ('You (tú) should rest. → ______ descansar. (conditional of deber)', 'deberías',
     'Advice → DEBERÍAS descansar.'),
    ('One must be patient. → ______ que tener paciencia. (impersonal, one word)', 'hay',
     'Impersonal → HAY que tener paciencia.'),
    ('It must be late (deduction). → Debe ______ ser tarde. (one word)', 'de',
     'Deduction = deber DE: debe DE ser tarde.'),
    ('We had to wait. → ______ que esperar. (preterite of tener, nosotros)', 'tuvimos',
     'Past obligation → TUVIMOS que esperar.'),
  ]),
  ex3=('Don\'t have to or mustn\'t?', 'The negatives are the B1 trap — choose carefully.', [
    ('La entrada es gratis: no ______ pagar.', ['tienes que', 'debes', 'debes de'], 'tienes que',
     'No obligation (it\'s free) → no TIENES QUE pagar.'),
    ('Está prohibido: no ______ aparcar aquí.', ['debes', 'tienes que', 'hay'], 'debes',
     'Prohibition → no DEBES aparcar.'),
    ('Which sentence gives advice?', ['Deberías acostarte antes.', 'Debes de acostarte antes.', 'Hay que acostarse tú.'], 'Deberías acostarte antes.',
     'Debería + infinitive = should. Deber de = deduction; hay que is impersonal.'),
    ('Which sentence is a deduction?', ['Debe de ganar mucho dinero.', 'Debe ganar mucho dinero.', 'Tiene que ganar mucho dinero ya.'], 'Debe de ganar mucho dinero.',
     'Deber DE = he must (probably) earn a lot.'),
    ('"It is necessary to recycle" (impersonal):', ['Hay que reciclar.', 'Tienes que reciclar tú.', 'Debe de reciclar.'], 'Hay que reciclar.',
     'Impersonal rule → HAY QUE reciclar.'),
  ]),
  game_desc='Each obligation structure passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('tener-que', 'tener que', 'to have to (practical obligation)', 'tengo que...', '<b>Tengo que</b> estudiar esta noche.', '______ que estudiar esta noche. (I have to)', 'tengo'),
    ('deber', 'deber + infinitive', 'must (duty, strong advice)', 'duty', '<b>Debes</b> descansar más.', '______ descansar más. (you must)', 'debes'),
    ('deberia', 'debería', 'should (softened advice)', 'conditional of deber', '<b>Deberías</b> hablar con ella.', '______ hablar con ella. (you should)', 'deberías'),
    ('deber-de', 'deber de', 'must (deduction / probability)', 'probably', '<b>Debe de</b> estar cansado.', 'Debe ______ estar cansado. (deduction marker)', 'de'),
    ('hay-que', 'hay que', 'one must / you have to (impersonal)', 'impersonal', '<b>Hay que</b> reservar con antelación.', '______ que reservar con antelación. (one must)', 'hay'),
    ('no-tener-que', 'no tener que', 'don\'t have to (optional!)', 'no obligation', '<b>No tienes que</b> venir si no quieres.', 'No ______ que venir si no quieres. (don\'t have to)', 'tienes'),
    ('no-deber', 'no deber', 'mustn\'t (prohibition)', 'prohibition', '<b>No debes</b> fumar aquí.', 'No ______ fumar aquí. (mustn\'t)', 'debes'),
    ('tuve-que', 'tuve que', 'I had to (past obligation)', 'preterite', '<b>Tuvimos que</b> esperar dos horas.', '______ que esperar dos horas. (we had to)', 'tuvimos'),
  ],
),

'modal-would': dict(
  num='G13', short='Would', title='Would — El condicional simple',
  subtitle='me gustaría, sería, haría: wishes, politeness and hypotheticals',
  slides=[
    ('The conditional: one ending, every verb', None,
     '<p class="slide-explanation">Spanish "would" is a real tense — the <b>condicional simple</b>. Add the same endings to the whole infinitive: <b>-ía, -ías, -ía, -íamos, -íais, -ían</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>hablar → hablaría</b> (I would speak) &nbsp;·&nbsp; <b>comer → comería</b> (I would eat)</p>'
     '<p style="margin-top:8px"><b>vivir → viviría</b> (I would live) &nbsp;·&nbsp; <b>ser → sería</b> (I would be)</p></div>'
     '<p style="margin-top:16px">The endings never change — and they attach to the infinitive, not a stem. Viviría = vivir + ía.</p>'),
    ('Me gustaría — the most useful "would"', None,
     '<p class="slide-explanation"><b>Me gustaría + infinitive</b> (I would like to...) is probably the highest-value B1 phrase — essential for wishes, plans and exam tasks.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Me gustaría viajar por Sudamérica.</b> (I would like to travel around South America.)</p>'
     '<p style="margin-top:8px"><b>Nos gustaría reservar una mesa.</b> (We would like to book a table.)</p></div>'
     '<p style="margin-top:16px">It works like gustar: the person is me/te/le/nos/os/les — <b>le gustaría</b> = he/she would like.</p>'),
    ('The irregular twelve', None,
     '<p class="slide-explanation">The same twelve verbs that are irregular in the future are irregular in the conditional — same shortened stems.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>tener → tendría</b> · <b>poder → podría</b> · <b>hacer → haría</b> · <b>decir → diría</b></p>'
     '<p style="margin-top:8px"><b>salir → saldría</b> · <b>venir → vendría</b> · <b>saber → sabría</b> · <b>querer → querría</b></p>'
     '<p style="margin-top:8px"><b>haber → habría</b> · <b>poner → pondría</b> · <b>valer → valdría</b> · <b>caber → cabría</b></p></div>'
     '<p style="margin-top:16px">If you know the future stem (tendr-, har-, dir-), you already know the conditional.</p>'),
    ('Politeness and advice', None,
     '<p class="slide-explanation">The conditional softens anything — requests, opinions, advice. It is the polite register of Spanish.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Te importaría cerrar la ventana?</b> (Would you mind closing the window?)</p>'
     '<p style="margin-top:8px"><b>Yo en tu lugar, hablaría con él.</b> (If I were you, I would talk to him.)</p>'
     '<p style="margin-top:8px"><b>¿Sería posible cambiar la reserva?</b> (Would it be possible to change the booking?)</p></div>'
     '<p style="margin-top:16px">"Yo en tu lugar..." or "Yo que tú..." + conditional is the classic advice formula.</p>'),
    ('Hypotheticals — the door to the subjunctive', None,
     '<p class="slide-explanation">The conditional pairs with the imperfect subjunctive for unreal situations: <b>Si + imperfect subjunctive, conditional</b>. You will master the subjunctive part later — recognise the pattern now.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Si tuviera dinero, viajaría más.</b> (If I had money, I would travel more.)</p>'
     '<p style="margin-top:8px"><b>Si pudiera, te ayudaría.</b> (If I could, I would help you.)</p></div>'
     '<p style="margin-top:16px">Memorise <b>si tuviera... / si pudiera...</b> as chunks — they unlock a whole exam task type.</p>'),
  ],
  traps=[
    ('Me gustaría que viajar más.', 'Me gustaría <strong>viajar</strong> más.', 'Same subject → me gustaría + infinitive directly, no que'),
    ('Yo quería un café, por favor. (too blunt in shops? No—)', 'Yo <strong>querría / quisiera</strong> un café, por favor.', 'For polite requests, the conditional querría (or quisiera) is the refined form'),
    ('Si tendría dinero, viajaría.', 'Si <strong>tuviera</strong> dinero, viajaría.', 'Never conditional after si — the if-clause takes the imperfect subjunctive'),
    ('Haría = haria (no accent)', '<strong>haría</strong>', 'Every conditional ending carries an accent on the í: -ía, -ías, -íamos'),
    ('Me gustaríamos visitar Madrid.', 'Nos <strong>gustaría</strong> visitar Madrid.', 'Gustar agrees with the thing liked (visitar = singular) — the person is a pronoun: NOS gustaría'),
  ],
  summary=[
    ('Formation', 'infinitive + -ía endings', 'hablaría · comería · viviría'),
    ('I would like', 'me gustaría + infinitive', 'Me gustaría viajar.'),
    ('Irregulars', 'tendría · haría · diría · podría', 'same stems as the future'),
    ('Polite request', 'querría / quisiera · ¿te importaría...?', '¿Te importaría cerrar la ventana?'),
    ('Advice', 'yo en tu lugar + conditional', 'Yo en tu lugar, hablaría con él.'),
    ('Hypothetical', 'si + imperf. subjunctive, conditional', 'Si tuviera dinero, viajaría.'),
  ],
  ex1=('Form the conditional', 'Infinitive + -ía — watch the twelve irregulars.', [
    ('Yo ______ más si tuviera tiempo. (viajar)', ['viajaría', 'viajara', 'viajaré'], 'viajaría',
     'Regular conditional: viajar + ía = VIAJARÍA.'),
    ('¿Qué ______ tú en mi lugar? (hacer)', ['harías', 'hacerías', 'hicieras'], 'harías',
     'Hacer is irregular: har- + ías = HARÍAS.'),
    ('Me ______ reservar una mesa para dos. (gustar)', ['gustaría', 'gustarían', 'gusto'], 'gustaría',
     'Me GUSTARÍA + infinitive — gustar agrees with the infinitive (singular).'),
    ('Ellos ______ venir mañana. (poder)', ['podrían', 'poderían', 'pudieran'], 'podrían',
     'Poder is irregular: podr- + ían = PODRÍAN.'),
    ('¿______ posible cambiar la fecha? (ser)', ['Sería', 'Será siendo', 'Fuera'], 'Sería',
     'Polite enquiry → conditional: ¿SERÍA posible...?'),
    ('Nosotros no ______ eso nunca. (decir)', ['diríamos', 'deciríamos', 'dijéramos'], 'diríamos',
     'Decir is irregular: dir- + íamos = DIRÍAMOS.'),
  ]),
  ex2=('Type the conditional form', 'Accents matter: -ía.', [
    ('tener, yo → Si fuera rico, ______ una casa en la playa.', 'tendría',
     'Tener → tendr- + ía = TENDRÍA.'),
    ('salir, nosotros → Con mejor tiempo, ______ más.', 'saldríamos',
     'Salir → saldr- + íamos = SALDRÍAMOS.'),
    ('venir, ella → Dijo que ______ a las ocho.', 'vendría',
     'Venir → vendr- + ía = VENDRÍA (reported future = conditional).'),
    ('saber, tú → ¿______ decirme la hora? (polite)', 'sabrías',
     'Saber → sabr- + ías = SABRÍAS.'),
    ('vivir, yo → Me encantaría: ______ en Sevilla.', 'viviría',
     'Regular: vivir + ía = VIVIRÍA.'),
  ]),
  ex3=('Politeness and hypotheticals', 'Choose the natural sentence.', [
    ('Ordering politely in a café:', ['Querría un café con leche, por favor.', 'Quiero café ya.', 'Querré un café con leche.'], 'Querría un café con leche, por favor.',
     'The conditional querría (or quisiera) is the polite order.'),
    ('Would you mind opening the door?', ['¿Te importaría abrir la puerta?', '¿Te importa que abrir la puerta?', '¿Importarías abrir la puerta?'], '¿Te importaría abrir la puerta?',
     '¿Te importaría + infinitive? = would you mind...?'),
    ('Giving advice:', ['Yo en tu lugar, estudiaría más.', 'Yo en tu lugar, estudiara más.', 'Yo en tu lugar, estudiaré más.'], 'Yo en tu lugar, estudiaría más.',
     'Yo en tu lugar + CONDITIONAL: estudiaría.'),
    ('If I had time, I would help you:', ['Si tuviera tiempo, te ayudaría.', 'Si tendría tiempo, te ayudaría.', 'Si tuviera tiempo, te ayudara.'], 'Si tuviera tiempo, te ayudaría.',
     'Si + imperfect subjunctive (tuviera), conditional in the main clause (ayudaría).'),
    ('We would like to book a room:', ['Nos gustaría reservar una habitación.', 'Nos gustaríamos reservar una habitación.', 'Gustaríamos reservar una habitación.'], 'Nos gustaría reservar una habitación.',
     'NOS gustaría — gustar stays singular, the person is the pronoun.'),
  ]),
  game_desc='Each conditional form passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('gustaria', 'me gustaría', 'I would like (to)', 'wishes', '<b>Me gustaría</b> viajar por Sudamérica.', 'Me ______ viajar por Sudamérica. (would like)', 'gustaría'),
    ('haria', 'haría', 'I/he would do (irregular har-)', 'hacer', '¿Qué <b>harías</b> tú en mi lugar?', '¿Qué ______ tú en mi lugar? (would you do)', 'harías'),
    ('tendria', 'tendría', 'I/he would have (irregular tendr-)', 'tener', 'Si fuera rico, <b>tendría</b> un barco.', 'Si fuera rico, ______ un barco. (I would have)', 'tendría'),
    ('seria', 'sería', 'it would be', 'ser', '¿<b>Sería</b> posible cambiar la reserva?', '¿______ posible cambiar la reserva? (would it be)', 'sería'),
    ('querria', 'querría / quisiera', 'I would like (polite order)', 'politeness', '<b>Querría</b> un café con leche, por favor.', '______ un café con leche, por favor. (I would like)', 'querría'),
    ('importaria', '¿te importaría...?', 'would you mind...?', 'polite request', '¿<b>Te importaría</b> cerrar la ventana?', '¿Te ______ cerrar la ventana? (would you mind)', 'importaría'),
    ('en-tu-lugar', 'yo en tu lugar...', 'if I were you... (advice)', 'advice formula', '<b>Yo en tu lugar</b>, hablaría con él.', 'Yo en tu ______, hablaría con él. (if I were you)', 'lugar'),
    ('si-tuviera', 'si tuviera..., ...ía', 'if I had..., I would...', 'hypothetical', 'Si <b>tuviera</b> dinero, viajaría más.', 'Si ______ dinero, viajaría más. (if I had)', 'tuviera'),
  ],
),

'past-perfect': dict(
  num='G14', short='Past Perfect', title='Past Perfect — El pluscuamperfecto',
  subtitle='había hecho: what had already happened before another past moment',
  slides=[
    ('The past before the past', None,
     '<p class="slide-explanation">The <b>pluscuamperfecto</b> describes an action completed <b>before another past action</b> — exactly like English "had done". Form: imperfect of haber + past participle.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Cuando llegué, el tren ya había salido.</b> (When I arrived, the train had already left.)</p>'
     '<p style="margin-top:8px"><b>No conocía Madrid porque nunca había estado allí.</b> (I didn\'t know Madrid because I had never been there.)</p></div>'
     '<p style="margin-top:16px">If English says "had + past participle", Spanish says <b>había + participio</b>. The mapping is one-to-one.</p>'),
    ('Forming it: había + participio', None,
     '<p class="slide-explanation">Conjugate <b>haber</b> in the imperfect; the participle never changes.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>había · habías · había · habíamos · habíais · habían</b> + participio</p>'
     '<p style="margin-top:8px">hablar → <b>hablado</b> · comer → <b>comido</b> · vivir → <b>vivido</b></p>'
     '<p style="margin-top:8px"><b>Habíamos terminado antes de las ocho.</b> (We had finished before eight.)</p></div>'
     '<p style="margin-top:16px">Nothing can come between haber and the participle: ya, nunca, todavía go BEFORE había or after the participle.</p>'),
    ('The irregular participles', None,
     '<p class="slide-explanation">The same irregular participles you met with the pretérito perfecto return here — learn them as a block.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>hacer → hecho</b> · <b>ver → visto</b> · <b>decir → dicho</b> · <b>escribir → escrito</b></p>'
     '<p style="margin-top:8px"><b>poner → puesto</b> · <b>volver → vuelto</b> · <b>abrir → abierto</b> · <b>romper → roto</b> · <b>morir → muerto</b></p></div>'
     '<p style="margin-top:16px"><b>Nunca había visto el mar.</b> (I had never seen the sea.) — visto, never "veído".</p>'),
    ('Ya and todavía no', None,
     '<p class="slide-explanation">Two adverbs supercharge the pluscuamperfecto: <b>ya</b> (already) and <b>todavía no</b> (not yet).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Cuando llamaste, ya había salido.</b> (When you called, I had already left.)</p>'
     '<p style="margin-top:8px"><b>A los veinte años todavía no había viajado en avión.</b> (At twenty I still hadn\'t flown.)</p></div>'
     '<p style="margin-top:16px">Position: ya/todavía no before había — <b>ya había salido</b>, not "había ya salido".</p>'),
    ('Telling stories with three past tenses', None,
     '<p class="slide-explanation">B1 storytelling combines three tenses: <b>indefinido</b> for events, <b>imperfecto</b> for background, <b>pluscuamperfecto</b> for what happened even earlier.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Llegué</b> tarde a la estación. (event) <b>Llovía</b> mucho. (background) El tren ya <b>había salido</b>. (earlier past)</p></div>'
     '<p style="margin-top:16px">In stories and in the estilo indirecto (G10), the pluscuamperfecto is what the indefinido becomes one step back: "Compré pan" → Dijo que había comprado pan.</p>'),
  ],
  traps=[
    ('Cuando llegué, el tren ya salió.', 'Cuando llegué, el tren ya <strong>había salido</strong>.', 'Earlier-past actions need the pluscuamperfecto, not a second indefinido'),
    ('Había ya terminado.', '<strong>Ya había</strong> terminado.', 'ya goes before había — nothing splits haber + participle'),
    ('Nunca había veído algo así.', 'Nunca había <strong>visto</strong> algo así.', 'ver has an irregular participle: visto'),
    ('Habían escrito la carta ellos dos. — but "la carta estaba escribida"', 'la carta estaba <strong>escrita</strong>', 'escribir → escrito — irregular participle, also when used as adjective'),
    ('Cuando llegamos, la película había empezada.', 'la película había <strong>empezado</strong>.', 'After haber the participle is invariable — always -o, no agreement'),
  ],
  summary=[
    ('Use', 'past before another past', 'Cuando llegué, ya había salido.'),
    ('Form', 'había/habías... + participio', 'habíamos terminado'),
    ('Participles', '-ado / -ido', 'hablado · comido · vivido'),
    ('Irregulars', 'hecho · visto · dicho · puesto · vuelto', 'Nunca había visto el mar.'),
    ('Adverbs', 'ya / todavía no + había', 'Ya había salido. / Todavía no había comido.'),
    ('Invariable', 'participle never agrees after haber', 'La película había empezado.'),
  ],
  ex1=('Pluscuamperfecto or not?', 'Find the action that happened first.', [
    ('Cuando llegamos al cine, la película ya ______. (empezar)', ['había empezado', 'empezó', 'empezaba'], 'había empezado',
     'The film started BEFORE we arrived → pluscuamperfecto.'),
    ('No reconocí la ciudad porque ______ mucho. (cambiar)', ['había cambiado', 'cambió', 'cambiaba'], 'había cambiado',
     'The change happened before I looked → había cambiado.'),
    ('Era la primera vez que ______ paella. (yo, probar)', ['había probado', 'probé', 'probaba'], 'había probado',
     '"First time I had tried" → pluscuamperfecto.'),
    ('Ayer ______ a mi abuela. (yo, visitar — simple past event)', ['visité', 'había visitado', 'visitaba'], 'visité',
     'A simple completed event yesterday → indefinido: visité.'),
    ('Estaba cansado porque no ______ bien. (dormir)', ['había dormido', 'durmió', 'duerme'], 'había dormido',
     'The bad sleep came before being tired → había dormido.'),
    ('Nunca ______ un castillo tan grande. (nosotros, ver)', ['habíamos visto', 'vimos nunca', 'veíamos'], 'habíamos visto',
     'Nunca + pluscuamperfecto with irregular participle VISTO.'),
  ]),
  ex2=('Build the form', 'había + participle — watch the irregulars.', [
    ('hacer → Cuando volví, ya ______ ______ la cena. (ellos — two words)', 'habían hecho',
     'Hacer → HECHO: habían hecho la cena.'),
    ('escribir → A los diez años ya ______ ______ su primer cuento. (ella — two words)', 'había escrito',
     'Escribir → ESCRITO: había escrito.'),
    ('volver → Todavía no ______ ______ de vacaciones. (yo — two words)', 'había vuelto',
     'Volver → VUELTO: había vuelto.'),
    ('comer → No tenía hambre porque ya ______ ______. (yo — two words)', 'había comido',
     'Regular: había COMIDO.'),
    ('poner → ¿Quién ______ ______ la mesa antes de la fiesta? (two words)', 'había puesto',
     'Poner → PUESTO: había puesto la mesa.'),
  ]),
  ex3=('Story time', 'Choose the version with the right tense mix.', [
    ('When I got home, my brother had eaten everything:', ['Cuando llegué a casa, mi hermano se había comido todo.', 'Cuando llegaba a casa, mi hermano se comió todo.', 'Cuando había llegado, mi hermano comía todo.'], 'Cuando llegué a casa, mi hermano se había comido todo.',
     'Arrival = indefinido (llegué); the eating happened earlier = pluscuamperfecto.'),
    ('She told me she had bought the tickets:', ['Me dijo que había comprado las entradas.', 'Me dijo que compró comprado las entradas.', 'Me dijo que compraba las entradas ya.'], 'Me dijo que había comprado las entradas.',
     'Reported indefinido → pluscuamperfecto: había comprado.'),
    ('I had never flown before that trip:', ['Nunca había volado antes de ese viaje.', 'Nunca volé antes volando.', 'Nunca había volada antes.'], 'Nunca había volado antes de ese viaje.',
     'Nunca + había + invariable participle VOLADO.'),
    ('The train had already left:', ['El tren ya había salido.', 'El tren había ya salido.', 'El tren ya salía había.'], 'El tren ya había salido.',
     'Ya before había — nothing between haber and participle.'),
    ('We were tired because we had walked 20 km:', ['Estábamos cansados porque habíamos caminado 20 km.', 'Estuvimos cansados porque caminamos habido 20 km.', 'Éramos cansados porque habíamos caminando.'], 'Estábamos cansados porque habíamos caminado 20 km.',
     'Background state = imperfecto; earlier cause = pluscuamperfecto.'),
  ]),
  game_desc='Each pluscuamperfecto form passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('habia-salido', 'había salido', 'had left (past before past)', 'pluscuamperfecto', 'Cuando llegué, el tren ya <b>había salido</b>.', 'Cuando llegué, el tren ya había ______. (left)', 'salido'),
    ('habia', 'había + participio', 'had + past participle', 'formation', 'No <b>había</b> estado nunca en Madrid.', 'No ______ estado nunca en Madrid. (I had)', 'había'),
    ('hecho', 'hecho', 'done/made — irregular participle of hacer', 'hacer → hecho', 'Ya habían <b>hecho</b> la cena.', 'Ya habían ______ la cena. (made)', 'hecho'),
    ('visto', 'visto', 'seen — irregular participle of ver', 'ver → visto', 'Nunca había <b>visto</b> el mar.', 'Nunca había ______ el mar. (seen)', 'visto'),
    ('escrito', 'escrito', 'written — irregular participle of escribir', 'escribir → escrito', 'Ya había <b>escrito</b> la carta.', 'Ya había ______ la carta. (written)', 'escrito'),
    ('ya', 'ya + había', 'already — goes before había', 'position', 'Cuando llamaste, <b>ya</b> había salido.', 'Cuando llamaste, ______ había salido. (already)', 'ya'),
    ('todavia-no', 'todavía no había...', 'had not yet...', 'not yet', '<b>Todavía no</b> había comido.', '______ no había comido. (still / yet)', 'todavía'),
    ('vuelto', 'vuelto', 'returned — irregular participle of volver', 'volver → vuelto', 'Todavía no había <b>vuelto</b> de vacaciones.', 'Todavía no había ______ de vacaciones. (returned)', 'vuelto'),
  ],
),

'prepositions-time': dict(
  num='G15', short='Time Prepositions', title='Time Prepositions — Hace, desde, durante',
  subtitle='hace dos años, desde 2020, durante el verano: locating events in time',
  slides=[
    ('Hace — "ago", but in front', None,
     '<p class="slide-explanation">English "ago" comes after the time; Spanish <b>hace</b> comes BEFORE it. This single difference causes endless mistakes.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Llegué hace dos horas.</b> (I arrived two hours ago.)</p>'
     '<p style="margin-top:8px"><b>Hace tres años visitamos Perú.</b> (Three years ago we visited Peru.)</p></div>'
     '<p style="margin-top:16px">Pattern: <b>hace + time + indefinido</b>. Never put hace after the time expression.</p>'),
    ('Desde and desde hace — since and for', None,
     '<p class="slide-explanation"><b>Desde</b> + a date/moment = since. <b>Desde hace</b> + a duration = for. And crucially, Spanish uses the <b>present tense</b> where English uses "have been".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Vivo aquí desde 2020.</b> (I have lived here since 2020.)</p>'
     '<p style="margin-top:8px"><b>Estudio español desde hace dos años.</b> (I have been studying Spanish for two years.)</p></div>'
     '<p style="margin-top:16px">English speakers\' trap: "I have lived here for 2 years" → <b>Vivo</b> aquí desde hace 2 años — present tense, because the action continues.</p>'),
    ('Durante and por — during / for a duration', None,
     '<p class="slide-explanation"><b>Durante</b> covers both English "during" and "for" with finished durations.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Vivimos en Roma durante cinco años.</b> (We lived in Rome for five years — finished.)</p>'
     '<p style="margin-top:8px"><b>Durante el verano trabajo en un hotel.</b> (During the summer I work in a hotel.)</p></div>'
     '<p style="margin-top:16px">Compare: finished period → durante + indefinido; still continuing → desde hace + present.</p>'),
    ('Por and de with parts of the day', None,
     '<p class="slide-explanation">Parts of the day take <b>por</b> (no clock time) or <b>de</b> (with clock time).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Por la mañana</b> estudio. (In the morning I study.)</p>'
     '<p style="margin-top:8px">La clase es <b>a las diez de la mañana</b>. (The class is at ten in the morning.)</p>'
     '<p style="margin-top:8px"><b>Por la noche</b> vemos una serie. (At night we watch a series.)</p></div>'
     '<p style="margin-top:16px">Never "en la mañana" in Spain — it\'s <b>por la mañana</b> (Latin America does say en la mañana, but learn the Castilian norm first).</p>'),
    ('Hasta, dentro de, a partir de', None,
     '<p class="slide-explanation">Three more tools to place events precisely.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>hasta</b> = until — Trabajo <b>hasta las seis</b>. (I work until six.)</p>'
     '<p style="margin-top:8px"><b>dentro de</b> = in (future) — Vuelvo <b>dentro de una hora</b>. (I\'ll be back in an hour.)</p>'
     '<p style="margin-top:8px"><b>a partir de</b> = from... on — <b>A partir de mañana</b>, dieta. (From tomorrow on, diet.)</p></div>'
     '<p style="margin-top:16px">Trap: English "in an hour" (future) is <b>dentro de</b> una hora — NOT "en una hora", which means it takes an hour.</p>'),
  ],
  traps=[
    ('Llegué dos horas hace.', 'Llegué <strong>hace dos horas</strong>.', 'hace goes BEFORE the time period — the opposite of English "ago"'),
    ('He vivido aquí desde hace dos años. (still living)', '<strong>Vivo</strong> aquí desde hace dos años.', 'Continuing situations use the PRESENT with desde (hace) — not the perfect'),
    ('Vuelvo en una hora. (meaning "an hour from now")', 'Vuelvo <strong>dentro de</strong> una hora.', '"In an hour" (future point) = dentro de una hora'),
    ('Estudio en la mañana.', 'Estudio <strong>por la mañana</strong>.', 'Parts of the day take por in Castilian Spanish: por la mañana/tarde/noche'),
    ('Trabajé durante de cinco años allí.', 'Trabajé <strong>durante cinco años</strong> allí.', 'durante goes directly before the duration — no de'),
  ],
  summary=[
    ('Ago', 'hace + time (before!)', 'Llegué hace dos horas.'),
    ('Since', 'desde + date · present tense', 'Vivo aquí desde 2020.'),
    ('For (continuing)', 'desde hace + duration · present', 'Estudio español desde hace dos años.'),
    ('For (finished)', 'durante + duration · indefinido', 'Vivimos en Roma durante cinco años.'),
    ('Parts of day', 'por la mañana · a las diez de la mañana', 'Por la noche vemos una serie.'),
    ('Until / in / from', 'hasta · dentro de · a partir de', 'Vuelvo dentro de una hora.'),
  ],
  ex1=('Choose the time preposition', 'hace, desde, durante, por...', [
    ('Visitamos Granada ______ tres años. (ago)', ['hace', 'desde', 'durante'], 'hace',
     '"Three years ago" → HACE tres años.'),
    ('Vivo en este barrio ______ 2019. (since)', ['desde', 'hace', 'durante'], 'desde',
     'Since a date → DESDE 2019.'),
    ('Estudio español ______ hace un año. (for, continuing)', ['desde', 'durante', 'a partir de'], 'desde',
     'For + continuing → DESDE HACE un año.'),
    ('Trabajé en Londres ______ dos años. (for, finished)', ['durante', 'desde hace', 'dentro de'], 'durante',
     'Finished period → DURANTE dos años + indefinido.'),
    ('No me llames ______ la mañana — duermo. (in the morning)', ['por', 'en', 'a'], 'por',
     'Part of the day → POR la mañana.'),
    ('El examen empieza ______ las nueve ______ la mañana.', ['a / de', 'por / por', 'en / a'], 'a / de',
     'Clock time: A las nueve DE la mañana.'),
  ]),
  ex2=('Translate the time expression', 'Type the missing Spanish word(s).', [
    ('I arrived two hours ago. → Llegué ______ dos horas. (one word)', 'hace',
     'Ago → HACE before the time: hace dos horas.'),
    ('I\'ll be back in ten minutes. → Vuelvo ______ de diez minutos. (one word)', 'dentro',
     'Future "in" → DENTRO de diez minutos.'),
    ('I work until six. → Trabajo ______ las seis. (one word)', 'hasta',
     'Until → HASTA las seis.'),
    ('From Monday on → a ______ del lunes (one word)', 'partir',
     'From... on → a PARTIR de.'),
    ('I have been living here for five years. → ______ aquí desde hace cinco años. (vivir — watch the tense!)', 'vivo',
     'Continuing action → PRESENT tense: VIVO aquí desde hace cinco años.'),
  ]),
  ex3=('Which sentence is right?', 'The tense matters as much as the preposition.', [
    ('I have known her since January (still know her):', ['La conozco desde enero.', 'La conocí desde enero.', 'La he conocido desde hace enero.'], 'La conozco desde enero.',
     'Continuing → present: la CONOZCO desde enero.'),
    ('We lived there for ten years (we moved away):', ['Vivimos allí durante diez años.', 'Vivimos allí desde hace diez años.', 'Vivimos allí dentro de diez años.'], 'Vivimos allí durante diez años.',
     'Finished period → DURANTE + indefinido.'),
    ('The shop opens at 9 in the morning:', ['La tienda abre a las nueve de la mañana.', 'La tienda abre a las nueve por la mañana.', 'La tienda abre en las nueve de mañana.'], 'La tienda abre a las nueve de la mañana.',
     'Clock time + part of day → a las nueve DE la mañana.'),
    ('See you in a week:', ['Nos vemos dentro de una semana.', 'Nos vemos en una semana hace.', 'Nos vemos hasta una semana.'], 'Nos vemos dentro de una semana.',
     'Future "in" → DENTRO DE una semana.'),
    ('It has been raining for hours:', ['Llueve desde hace horas.', 'Llovió desde horas.', 'Ha llovido durante hace horas.'], 'Llueve desde hace horas.',
     'Continuing → present + desde hace: LLUEVE desde hace horas.'),
  ]),
  game_desc='Each time expression passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('hace', 'hace + tiempo', 'ago (goes before the time!)', 'ago', 'Llegué <b>hace</b> dos horas.', 'Llegué ______ dos horas. (ago)', 'hace'),
    ('desde', 'desde', 'since + date/moment', 'since', 'Vivo aquí <b>desde</b> 2020.', 'Vivo aquí ______ 2020. (since)', 'desde'),
    ('desde-hace', 'desde hace + duración', 'for (continuing) — with the present tense', 'for', 'Estudio español <b>desde hace</b> dos años.', 'Estudio español desde ______ dos años. (for)', 'hace'),
    ('durante', 'durante', 'during / for (finished period)', 'duration', 'Vivimos en Roma <b>durante</b> cinco años.', 'Vivimos en Roma ______ cinco años. (for)', 'durante'),
    ('por-la-manana', 'por la mañana', 'in the morning (no clock time)', 'parts of day', 'Estudio <b>por</b> la mañana.', 'Estudio ______ la mañana. (in)', 'por'),
    ('hasta', 'hasta', 'until', 'until', 'Trabajo <b>hasta</b> las seis.', 'Trabajo ______ las seis. (until)', 'hasta'),
    ('dentro-de', 'dentro de', 'in (a future point): in an hour', 'future in', 'Vuelvo <b>dentro de</b> una hora.', 'Vuelvo ______ de una hora. (in)', 'dentro'),
    ('a-partir-de', 'a partir de', 'from... on', 'starting point', '<b>A partir de</b> mañana, dieta.', 'A ______ de mañana, dieta. (from ... on)', 'partir'),
  ],
),

}
