# -*- coding: utf-8 -*-
"""espanol-en B2 grammar content — batch 3 (chapters G11-G15)."""

CHAPTERS = {

'passive-voice': dict(
  num='G11', short='The Passive Voice', title='The Passive Voice — El pasivo',
  subtitle='Ser + participle, estar + participle, and how Spanish avoids the passive',
  slides=[
    ('The passive with ser + participle', None,
     '<p class="slide-explanation">The <b>ser passive</b> emphasises the action and who performed it (the agent, with <b>por</b>). It is common in formal and written Spanish.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>La ley fue aprobada por el parlamento.</b> (The law was approved by parliament.)</p>'
     '<p style="margin-top:8px"><b>El cuadro ha sido restaurado por expertos.</b> (The painting has been restored by experts.)</p>'
     '<p style="margin-top:8px">Structure: <b>ser (conjugated) + past participle (agreeing with subject) + por + agent</b></p></div>'),
    ('Ser vs estar + participle', None,
     '<p class="slide-explanation"><b>Ser</b> passive = action in progress (dynamic); <b>estar</b> + participle = resulting state (stative).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>La tienda fue cerrada a las ocho.</b> (The shop was closed at eight — the action of closing.)</p>'
     '<p style="margin-top:8px"><b>La tienda estaba cerrada.</b> (The shop was closed — the state, the result.)</p>'
     '<p style="margin-top:8px">If you can add "por alguien" → ser. If you describe a state → estar.</p></div>'),
    ('The se pasivo — the most common passive in Spanish', None,
     '<p class="slide-explanation">Spanish speakers usually prefer the <b>se pasivo</b> (impersonal-passive with se) over the ser passive, especially in speech.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Se aprobó la ley.</b> (The law was passed / They passed the law.)</p>'
     '<p style="margin-top:8px"><b>Se venden pisos aquí.</b> (Flats are sold here / Flats for sale here.)</p>'
     '<p style="margin-top:8px"><b>Se habla español.</b> (Spanish is spoken here.)</p></div>'
     '<p style="margin-top:12px">Key: the verb agrees with the logical subject (la ley → se aprobó; pisos → se venden).</p>'),
    ('Impersonal se for unknown agent', None,
     '<p class="slide-explanation">When the agent is unknown or irrelevant, use <b>se + 3rd person singular</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Se dice que…</b> (It is said that… / People say…)</p>'
     '<p style="margin-top:8px"><b>Se cree que el proyecto empezará en enero.</b> (It is believed that…)</p>'
     '<p style="margin-top:8px"><b>¿Cómo se dice "rainbow" en español?</b> (How do you say…?)</p></div>'),
    ('Passives with object pronouns', None,
     '<p class="slide-explanation">When the passive has a personal object, use the indirect-object passive or se pasivo carefully.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Me fue concedida la beca.</b> (I was granted the scholarship.) — literary</p>'
     '<p style="margin-top:8px"><b>Se me concedió la beca.</b> (I was granted the scholarship.) — more natural</p>'
     '<p style="margin-top:8px"><b>Le fue enviada la carta.</b> (She was sent the letter.)</p></div>'),
  ],
  traps=[
    ('La ley era aprobada ayer.', 'La ley <strong>fue aprobada</strong> ayer.', 'Past passive action uses ser in the indefinido (fue), not the imperfecto (era), for a specific completed event'),
    ('Se vendieron muchos pisos.', 'Correct! <strong>Se vendieron</strong> muchos pisos — the verb agrees with pisos (plural).', 'Se pasivo: verb agrees with the logical subject: pisos (pl.) → se vendieron'),
    ('El museo fue abierto a las diez. (state)', 'El museo <strong>estaba abierto</strong> a las diez.', 'A state (the museum being open) → estar + participle. Ser + participle = the action of opening'),
    ('Se hablan inglés en Australia.', 'Se habla inglés en Australia.', 'Impersonal se + singular = se habla (even for a non-countable concept like a language)'),
    ('El ladrón fue detenido por la policía. (passive)', 'Correct! <strong>El ladrón fue detenido por la policía</strong> — ser passive with agent (por la policía).', 'Ser passive with by = correct when the agent is mentioned: fue detenido por la policía'),
  ],
  summary=[
    ('Ser passive', 'ser + pp (agreeing) + por + agent', 'La ley fue aprobada por el parlamento.'),
    ('Estar + pp', 'estar + pp = resulting state', 'La tienda estaba cerrada. (state)'),
    ('Se pasivo', 'se + verb (3rd p., agrees with subject)', 'Se vendieron mil entradas.'),
    ('Impersonal se', 'se + 3rd sing. (no specific subject)', 'Se dice que va a llover.'),
    ('With pronoun', 'se + indirect pronoun + verb', 'Se me concedió la beca.'),
    ('Se pasivo rule', 'Verb agrees with logical subject', 'Se vende piso (sing.) / Se venden pisos (pl.)'),
  ],
  ex1=('Choose the right passive form', 'Tap the best option for each gap.', [
    ('La novela ______ por Cervantes en el siglo XVII.', ['fue escrita', 'estaba escrita', 'se escribía'], 'fue escrita',
     'Ser passive with named agent (por Cervantes) + specific historical event → fue escrita (ser + pp, indefinido).'),
    ('Cuando llegamos, la puerta ya ______ .', ['estaba abierta', 'fue abierta', 'se abrió'], 'estaba abierta',
     'The door being in an open state when we arrived = estar + participle: estaba abierta.'),
    ('______ tres coches en el aparcamiento. (There are cars for sale — se pasivo)', ['Se venden', 'Se vende', 'Son vendidos'], 'Se venden',
     'Se pasivo with plural noun: tres coches (pl.) → se venden (3rd pl.).'),
    ('______ que el presidente va a dimitir. (It is said that)', ['Se dice', 'Se dicen', 'Dicen que se'], 'Se dice',
     'Impersonal se + 3rd singular: se dice que (it is said that). The verb stays singular.'),
    ('El puente ______ el año pasado por ingenieros alemanes.', ['fue construido', 'estaba construido', 'se construía'], 'fue construido',
     'Ser passive: specific past construction + named agent (ingenieros alemanes) → fue construido (ser + pp).'),
    ('______ las nuevas normas desde el lunes. (The new rules will apply — se pasivo)', ['Se aplicarán', 'Se aplicará', 'Serán aplicadas'], 'Se aplicarán',
     'Se pasivo with plural noun (las normas) → verb agrees: se aplicarán (future plural).'),
  ]),
  ex2=('Complete with the right passive', 'Type the missing word — no accents needed.', [
    ('La sentencia ______ dictada por el juez a las doce. (was — ser passive)', 'fue',
     'Ser passive (past): fue dictada — ser (indefinido) + past participle (agreeing with la sentencia, f.sing.).'),
    ('Cuando llegué, la ventana ya ______ abierta. (was — state)', 'estaba',
     'State (window already open as a result) = estar + participle: estaba abierta.'),
    ('Se ______ piso en este edificio. (a flat is for sale)', 'vende',
     'Se pasivo + singular noun (piso) → se vende (3rd sing.).'),
    ('______ cree que el cambio climático es urgente. (It is believed)', 'se',
     'Impersonal se: Se cree que… (It is believed that…). The se is the impersonal marker.'),
    ('Se ______ concedió el premio. (She was awarded — with indirect obj. pronoun)', 'le',
     'Se + indirect object pronoun + verb: se le concedió el premio (she was awarded the prize).'),
  ]),
  ex3=('Passive choices', 'Choose the correct analysis or form.', [
    ('Which sentence uses the ser passive correctly?', ['El edificio fue demolido por la empresa constructora.', 'El edificio estaba demolido por la empresa.', 'El edificio se demolió por la empresa.'], 'El edificio fue demolido por la empresa constructora.',
     'Ser + pp + por + agent = the full ser passive. Se pasivo does not take por + agent.'),
    ('Which sentence describes a state (not an action)?', ['El puente estaba roto cuando llegamos.', 'El puente fue roto ayer.', 'Se rompió el puente ayer.'], 'El puente estaba roto cuando llegamos.',
     'Estar + participle = resulting state. Fue roto and se rompió describe the action of breaking.'),
    ('Which se pasivo is correct?', ['Se venden entradas aquí.', 'Se vende entradas aquí.', 'Se vendieron entradas ayer — se vende entradas mañana.'], 'Se venden entradas aquí.',
     'Se pasivo: entradas (f.pl.) → se venden (3rd pl.). Verb always agrees with the logical subject.'),
    ('Which expresses "it is said that"?', ['Se dice que las elecciones serán en junio.', 'Se dicen que las elecciones serán en junio.', 'Dicen se que las elecciones serán en junio.'], 'Se dice que las elecciones serán en junio.',
     'Impersonal se dice que + subordinate clause = it is said that. Always singular; que cannot be omitted.'),
    ('Which correctly uses a passive with an indirect object pronoun?', ['Se le notificó el resultado.', 'Se le notificaron el resultado.', 'Le fue notificadas el resultado.'], 'Se le notificó el resultado.',
     'Se + le (indirect obj. pronoun) + verb (agrees with el resultado, m.sing.) → se le notificó.'),
  ]),
  game_desc='Master the passive voice in Spanish: ser + participle, estar + participle for states, and the se pasivo. Reach 100 points to win.',
  items=[
    ('fue-aprobada', 'fue aprobada', 'was approved (ser passive, f.)', 'ser passive past', 'La ley <b>fue aprobada</b> por el parlamento en mayo.', 'La ley ______ ______ por el parlamento. (was approved)', 'fue aprobada'),
    ('estaba-cerrada', 'estaba cerrada', 'was closed (state)', 'estar + participle state', 'Cuando llegué, la tienda <b>estaba cerrada</b>.', 'Cuando llegué, la tienda ______ ______ . (was closed — state)', 'estaba cerrada'),
    ('se-venden', 'se venden', 'are sold / for sale', 'se pasivo plural', '<b>Se venden</b> pisos en este edificio.', '______ ______ pisos en este edificio. (are sold)', 'se venden'),
    ('se-dice-que', 'se dice que', 'it is said that', 'impersonal se', '<b>Se dice que</b> el proyecto empezará pronto.', '______ ______ ______ el proyecto empezará pronto. (it is said that)', 'se dice que'),
    ('fue-construido', 'fue construido por', 'was built by (ser passive)', 'ser passive with agent', 'El estadio <b>fue construido por</b> una empresa española.', 'El estadio ______ ______ ______ una empresa española. (was built by)', 'fue construido por'),
    ('se-aplican', 'se aplican', 'are applied (se pasivo)', 'se pasivo formal', '<b>Se aplican</b> las mismas normas en todos los países.', '______ ______ las mismas normas en todos los países. (are applied)', 'se aplican'),
    ('se-le-concedio', 'se le concedió', 'she/he was granted', 'se + indirect obj.', '<b>Se le concedió</b> la beca por sus méritos académicos.', '______ ______ ______ la beca por sus méritos. (was granted)', 'se le concedio'),
    ('se-cree-que', 'se cree que', 'it is believed that', 'impersonal belief', '<b>Se cree que</b> el cambio climático es la mayor amenaza.', '______ ______ ______ el cambio climático es urgente. (it is believed that)', 'se cree que'),
  ],
),

'perfect-forms': dict(
  num='G12', short='Advanced Perfect Forms', title='Advanced Perfect Forms — Habré terminado antes de las cinco',
  subtitle='Future perfect, conditional perfect, and past subjunctive perfect',
  slides=[
    ('Futuro perfecto — will have done', None,
     '<p class="slide-explanation">The <b>futuro perfecto</b> (future perfect) expresses an action that will be complete before a future moment. It also expresses present probability.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Formation:</b> habré/habrás/habrá/habremos/habréis/habrán + participio</p>'
     '<p style="margin-top:8px"><b>Habré terminado</b> antes de las cinco. (I will have finished before five.)</p>'
     '<p style="margin-top:8px"><b>¿Habrás comido?</b> (Will you have eaten by then? / I wonder if you have eaten.)</p></div>'
     '<p style="margin-top:12px">Present probability: <b>Ya habrán llegado.</b> (They must have arrived by now.)</p>'),
    ('Condicional perfecto — would have done', None,
     '<p class="slide-explanation">The <b>condicional perfecto</b> is the main clause of type 3 and mixed conditionals, and also expresses past probability.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Formation:</b> habría/habrías/habría/habríamos/habríais/habrían + participio</p>'
     '<p style="margin-top:8px"><b>Lo habría hecho</b> si hubiera podido. (I would have done it if I had been able to.)</p>'
     '<p style="margin-top:8px"><b>Habría llegado</b> tarde — había mucho tráfico. (He must have arrived late — there was a lot of traffic.)</p></div>'),
    ('Pluscuamperfecto de subjuntivo', None,
     '<p class="slide-explanation">The <b>pluscuamperfecto de subjuntivo</b> (past perfect subjunctive) appears in the if-clause of type 3 conditionals and after certain conjunctions.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Formation:</b> hubiera/hubieras/hubiera/hubiéramos/hubierais/hubieran + participio</p>'
     '<p style="margin-top:8px"><b>Si hubiera sabido</b>, te lo habría dicho. (If I had known, I would have told you.)</p>'
     '<p style="margin-top:8px"><b>No creía que hubieran llegado</b> ya. (I didn\'t think they had already arrived.)</p></div>'),
    ('Subjuntivo perfecto — present context', None,
     '<p class="slide-explanation">The <b>perfecto de subjuntivo</b> (haya + pp) is used in present/future subjunctive contexts where the subordinate action is completed.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Formation:</b> haya/hayas/haya/hayamos/hayáis/hayan + participio</p>'
     '<p style="margin-top:8px"><b>Espero que haya llegado</b> bien. (I hope she has arrived safely.)</p>'
     '<p style="margin-top:8px"><b>No creo que hayan terminado</b> todavía. (I don\'t think they have finished yet.)</p></div>'),
    ('Sequence of tenses with perfects', None,
     '<p class="slide-explanation">The choice of perfect tense in a subordinate clause depends on the tense in the main clause.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Espero que haya llegado.</b> (Present main → subjuntivo perfecto)</p>'
     '<p style="margin-top:8px"><b>Esperaba que hubiera llegado.</b> (Past main → pluscuamperfecto subj.)</p>'
     '<p style="margin-top:8px"><b>Si hubiera estudiado, habría aprobado.</b> (Type 3: pluscuam. subj. → cond. perfecto)</p></div>'),
  ],
  traps=[
    ('Si habría sabido, te lo diría.', 'Si <strong>hubiera sabido</strong>, te lo habría dicho.', 'In the if-clause: NEVER conditional — use pluscuamperfecto de subjuntivo (hubiera sabido)'),
    ('Habré llegado — probability in the past.', '<strong>Habría llegado</strong> = past probability. <strong>Habré llegado</strong> = future-before-future.', 'Futuro perfecto (habré) = future completion or present probability; condicional perfecto (habría) = past probability or type 3 result'),
    ('No creo que han llegado.', 'No creo que <strong>hayan llegado</strong>.', 'Negative belief triggers subjunctive: no creo que + hayan (subjuntivo perfecto)'),
    ('Para las cinco, habremos terminado. (for)', 'Para las cinco, habremos terminado. — Correct! <strong>Para</strong> + time = by that time with futuro perfecto.', 'Para + time expression + futuro perfecto = will have done by then. Correct usage.'),
    ('Esperaba que han llegado.', 'Esperaba que <strong>hubieran llegado</strong>.', 'Past main verb (esperaba) → pluscuamperfecto de subjuntivo (hubieran llegado) in the subordinate clause'),
  ],
  summary=[
    ('Futuro perfecto', 'habré/habrás/habrá… + pp', 'Para mañana, habré terminado el informe.'),
    ('Condicional perfecto', 'habría/habrías/habría… + pp', 'Lo habría hecho si hubiera podido.'),
    ('Pluscuam. subj.', 'hubiera/hubieras/hubiera… + pp', 'Si hubiera sabido, habría venido.'),
    ('Subjuntivo perfecto', 'haya/hayas/haya… + pp', 'Espero que haya llegado bien.'),
    ('Sequence', 'Espero que + haya / Esperaba que + hubiera', 'Espero que haya comido. Esperaba que hubiera comido.'),
    ('If-clause rule', 'Never conditional in if-clause', 'Si hubiera tenido (NOT si habría tenido)'),
  ],
  ex1=('Choose the right advanced perfect form', 'Tap the correct option.', [
    ('Para el viernes, ______ el proyecto. (we will have finished)', ['habremos terminado', 'habríamos terminado', 'hayamos terminado'], 'habremos terminado',
     'Futuro perfecto: habremos terminado = we will have finished (before a future deadline).'),
    ('Si ______ antes, lo habríamos visto. (we had left)', ['hubiéramos salido', 'habríamos salido', 'hayamos salido'], 'hubiéramos salido',
     'If-clause of type 3 conditional: pluscuamperfecto de subjuntivo (hubiéramos salido).'),
    ('No creo que el paquete ______ todavía. (has arrived)', ['haya llegado', 'hubiera llegado', 'habrá llegado'], 'haya llegado',
     'Negative belief in present context + completion: no creo que + hayan llegado (subjuntivo perfecto).'),
    ('______ tarde — había un atasco enorme. (She must have arrived late)', ['Habría llegado', 'Habrá llegado', 'Hubiera llegado'], 'Habría llegado',
     'Past probability = condicional perfecto: habría llegado (she must have arrived / would have arrived).'),
    ('Espero que ______ bien. (they have eaten)', ['hayan comido', 'hubieran comido', 'habrán comido'], 'hayan comido',
     'Espero que + subjuntivo perfecto (present hope about completed action): hayan comido.'),
    ('______ te lo habría dicho antes. (If I had known)', ['Si hubiera sabido', 'Si habría sabido', 'Si he sabido'], 'Si hubiera sabido',
     'Type 3 if-clause: si + pluscuamperfecto de subjuntivo (hubiera sabido). Never conditional.'),
  ]),
  ex2=('Complete the perfect form', 'Type the missing word — no accents needed.', [
    ('Para las seis, ______ terminado la reunión. (we will have — futuro perfecto)', 'habremos',
     'Futuro perfecto (nosotros): habremos terminado = we will have finished.'),
    ('Si ______ sabido, te lo habría dicho. (I had known — if-clause)', 'hubiera',
     'Pluscuamperfecto de subjuntivo (yo): si hubiera sabido = if I had known.'),
    ('No creo que ______ llegado todavía. (they have — subjuntivo perfecto)', 'hayan',
     'Subjuntivo perfecto (ellos): hayan llegado — after no creo que (present negative belief).'),
    ('Lo ______ hecho si hubiera tenido tiempo. (I would have)', 'habria',
     'Condicional perfecto (yo): lo habría hecho = I would have done it.'),
    ('Esperaba que ______ terminado antes. (they had — pluscuam. subj.)', 'hubieran',
     'Past main verb (esperaba) → pluscuamperfecto de subjuntivo: hubieran terminado.'),
  ]),
  ex3=('Perfect tense analysis', 'Choose the correct analysis.', [
    ('What does "Para el lunes habrá llegado" mean?', ['She will have arrived by Monday.', 'She must have arrived by Monday.', 'She would have arrived by Monday.'], 'She will have arrived by Monday.',
     'Futuro perfecto (habrá llegado) + para + future time = she will have done X by Monday.'),
    ('Which is the correct type 3 conditional?', ['Si hubiera trabajado más, habría aprobado.', 'Si habría trabajado más, habría aprobado.', 'Si hubiera trabajado más, hubiera aprobado.'], 'Si hubiera trabajado más, habría aprobado.',
     'Type 3: si + pluscuam. subj. (hubiera trabajado) + cond. perfecto (habría aprobado). If-clause NEVER takes conditional.'),
    ('Which correctly uses the subjuntivo perfecto?', ['Espero que hayan llegado bien.', 'Espero que hubieran llegado bien.', 'Espero que habrán llegado bien.'], 'Espero que hayan llegado bien.',
     'Espero que (present trigger) + completed action = subjuntivo perfecto (hayan llegado).'),
    ('Which correctly expresses past probability?', ['Habría perdido el tren — siempre llega tarde.', 'Habrá perdido el tren — siempre llega tarde.', 'Hubiera perdido el tren — siempre llega tarde.'], 'Habría perdido el tren — siempre llega tarde.',
     'Past probability (deduction about the past) = condicional perfecto: habría perdido.'),
    ('Which requires the pluscuamperfecto de subjuntivo?', ['Esperaba que hubieran terminado.', 'Espero que hayan terminado.', 'Espero que habrán terminado.'], 'Esperaba que hubieran terminado.',
     'Past main verb (esperaba) → pluscuamperfecto de subjuntivo in the subordinate: hubieran terminado.'),
  ]),
  game_desc='Master advanced perfect forms in Spanish: future perfect, conditional perfect, and both subjunctive perfects. Reach 100 points to win.',
  items=[
    ('habre-terminado', 'habré terminado', 'I will have finished', 'futuro perfecto', 'Para las cinco, <b>habré terminado</b> el informe.', 'Para las cinco, ______ ______ el informe. (I will have finished)', 'habre terminado'),
    ('habria-hecho', 'lo habría hecho', 'I would have done it', 'condicional perfecto', 'Lo <b>habría hecho</b> si me lo hubieran pedido.', 'Lo ______ ______ si me lo hubieran pedido. (I would have done it)', 'habria hecho'),
    ('hubiera-sabido', 'si hubiera sabido', 'if I had known', 'pluscuam. subj. if-clause', '<b>Si hubiera sabido</b> la verdad, no habría ido.', '______ ______ ______ la verdad, no habría ido. (if I had known)', 'si hubiera sabido'),
    ('hayan-llegado', 'hayan llegado', 'have arrived (subjuntivo perf.)', 'subjuntivo perfecto', 'Espero que <b>hayan llegado</b> bien.', 'Espero que ______ ______ bien. (have arrived — subjuntive)', 'hayan llegado'),
    ('habriamos-terminado', 'habríamos terminado', 'we would have finished', 'cond. perfecto plural', '<b>Habríamos terminado</b> antes si hubiera habido más personal.', '______ ______ antes si hubiera habido más personal. (we would have finished)', 'habriamos terminado'),
    ('para-el-lunes', 'para el lunes habrá', 'by Monday she will have', 'futuro perfecto deadline', '<b>Para el lunes habrá</b> llegado la respuesta.', '______ ______ ______ llegado la respuesta. (by Monday will have)', 'para el lunes habre'),
    ('hubieran-llegado', 'hubieran llegado', 'had arrived (pluscuam. subj.)', 'pluscuam. subj. subordinate', 'Esperaba que <b>hubieran llegado</b> antes de la cena.', 'Esperaba que ______ ______ antes de la cena. (had arrived — subjuntive)', 'hubieran llegado'),
    ('no-habria-dicho', 'no lo habría dicho', 'I would not have said it', 'cond. perfecto negative', '<b>No lo habría dicho</b> si hubiera sabido las consecuencias.', '______ ______ ______ si hubiera sabido las consecuencias. (I would not have said it)', 'no lo habria dicho'),
  ],
),

'phrasal-verbs': dict(
  num='G13', short='Spanish Multi-Word Verbs', title='Spanish Multi-Word Verbs — Salir con, contar con, dar con',
  subtitle='High-frequency verb+preposition combinations that trip up English speakers',
  slides=[
    ('Why Spanish multi-word verbs are different', None,
     '<p class="slide-explanation">Spanish does not have phrasal verbs like English (get up, turn off). Instead, it uses <b>verb + preposition/particle</b> combinations where the preposition changes the meaning significantly. These must be learned as units.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>contar</b> (to count / tell) → <b>contar con</b> (to count on, rely on)</p>'
     '<p style="margin-top:8px"><b>dar</b> (to give) → <b>dar con</b> (to come across, find) · <b>darse cuenta de</b> (to realise)</p>'
     '<p style="margin-top:8px"><b>salir</b> (to leave) → <b>salir con</b> (to go out with, date) · <b>salir adelante</b> (to get through, succeed)</p></div>'),
    ('Contar con, echar de menos, darse cuenta de', None,
     '<p class="slide-explanation">Three essential combinations with meanings that do not translate literally.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>contar con:</b> Siempre puedo <b>contar con</b> mis amigos. (I can always count on my friends.)</p>'
     '<p style="margin-top:8px"><b>echar de menos:</b> <b>Echo de menos</b> a mi familia. (I miss my family.) — verb + particle</p>'
     '<p style="margin-top:8px"><b>darse cuenta de:</b> No me di cuenta de que era tan tarde. (I didn\'t realise it was so late.)</p></div>'),
    ('Llevar, ponerse, quedarse combinations', None,
     '<p class="slide-explanation">These verbs form important combinations when combined with prepositions or adjectives.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>llevar + time + gerundio:</b> Llevo tres años estudiando español. (I have been studying for three years.)</p>'
     '<p style="margin-top:8px"><b>ponerse a:</b> Me puse a llorar. (I started to cry.) — sudden start of action</p>'
     '<p style="margin-top:8px"><b>quedarse con:</b> Me quedé con esa idea. (I kept / was left with that idea.)</p>'
     '<p style="margin-top:8px"><b>quedarse sin:</b> Me quedé sin palabras. (I was left speechless.)</p></div>'),
    ('Dar: common combinations', None,
     '<p class="slide-explanation"><b>Dar</b> forms many high-frequency combinations at B2.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>dar con:</b> Al final <b>di con</b> la solución. (I finally came across / hit upon the solution.)</p>'
     '<p style="margin-top:8px"><b>darse cuenta de:</b> Se dio cuenta del error. (She realised the mistake.)</p>'
     '<p style="margin-top:8px"><b>dar lugar a:</b> Esto <b>dio lugar a</b> un malentendido. (This led to a misunderstanding.)</p>'
     '<p style="margin-top:8px"><b>dar por:</b> Lo <b>dieron por</b> perdido. (They gave it up as lost.)</p></div>'),
    ('Echar, tirar, salir combinations', None,
     '<p class="slide-explanation">More B2-level combinations with common verbs.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>echar de menos:</b> to miss someone/something</p>'
     '<p style="margin-top:8px"><b>echar a perder:</b> Echó a perder la oportunidad. (He wasted / ruined the opportunity.)</p>'
     '<p style="margin-top:8px"><b>salir adelante:</b> A pesar de todo, salieron adelante. (Despite everything, they got through.)</p>'
     '<p style="margin-top:8px"><b>tirar de:</b> Hay que tirar de imaginación. (You have to draw on imagination.)</p></div>'),
  ],
  traps=[
    ('Me falta de mi familia. (I miss)', '<strong>Echo de menos</strong> a mi familia. / <strong>Extraño</strong> a mi familia.', 'To miss someone = echar de menos (or extrañar in LatAm). Faltar means to be lacking/missing (me falta dinero)'),
    ('Me di cuenta que era tarde.', 'Me di cuenta <strong>de que</strong> era tarde.', 'Darse cuenta de que — the de que is obligatory: realise (of) the fact that…'),
    ('Al final encontré con la solución.', 'Al final <strong>di con</strong> la solución.', 'To come upon / hit upon a solution = dar con (not encontrar con)'),
    ('Llevé tres años a estudiar español.', '<strong>Llevo tres años estudiando</strong> español.', 'Llevar + time + gerundio = to have been doing X for Y time. No a, no infinitive'),
    ('Esto dio lugar de un error.', 'Esto dio lugar <strong>a</strong> un error.', 'Dar lugar a (not de) = to give rise to, lead to'),
  ],
  summary=[
    ('Count on / rely on', 'contar con + noun/infinitive', 'Cuento con tu ayuda.'),
    ('Miss', 'echar de menos + a + person / noun', 'Echo de menos a mis amigos.'),
    ('Realise', 'darse cuenta de que + clause', 'Me di cuenta de que tenía razón.'),
    ('Have been doing', 'llevar + time + gerundio', 'Llevo dos horas esperando.'),
    ('Start to (suddenly)', 'ponerse a + infinitive', 'Se puso a reír.'),
    ('Lead to', 'dar lugar a + noun', 'La lluvia dio lugar a inundaciones.'),
  ],
  ex1=('Choose the right combination', 'Tap the correct preposition or particle.', [
    ('Siempre puedo contar ______ ti en los momentos difíciles.', ['con', 'de', 'a'], 'con',
     'Contar con = to count on / rely on. The preposition is con.'),
    ('Me di cuenta ______ que era demasiado tarde para volver.', ['de que', 'que', 'de'], 'de que',
     'Darse cuenta de que + clause — both de and que are required.'),
    ('Llevo dos años ______ en esta empresa. (working)', ['trabajando', 'trabajar', 'trabajo'], 'trabajando',
     'Llevar + time + gerundio (trabajando) = I have been working for two years.'),
    ('Al final ______ con la respuesta que buscaba. (I hit upon)', ['di', 'encontré', 'llegué'], 'di',
     'Dar con = to come across / hit upon. Fui di con (indefinido): al final di con la respuesta.'),
    ('De repente se puso ______ cantar una canción. (started)', ['a', 'de', 'que'], 'a',
     'Ponerse a + infinitive = to start suddenly doing something. The preposition is a.'),
    ('Esta decisión dio lugar ______ muchos problemas.', ['a', 'de', 'con'], 'a',
     'Dar lugar a = to lead to / give rise to. The preposition is a, not de.'),
  ]),
  ex2=('Complete the multi-word verb', 'Type the missing word — no accents needed.', [
    ('Echo de ______ a mis amigos del colegio. (I miss)', 'menos',
     'Echar de menos = to miss. The fixed phrase is echar de menos + a + person.'),
    ('Me di cuenta de ______ habían salido sin mí. (that)', 'que',
     'Darse cuenta de que + clause. Both de and que are required.'),
    ('Se puso a ______ cuando oyó la noticia. (to cry — suddenly)', 'llorar',
     'Ponerse a + infinitive: se puso a llorar = she suddenly started to cry.'),
    ('Llevo una hora ______ el problema. (working on)', 'estudiando',
     'Llevar + time + gerundio: llevo una hora estudiando = I have been studying for an hour.'),
    ('La huelga dio lugar ______ una crisis en la empresa. (to)', 'a',
     'Dar lugar a = to lead to/give rise to. The preposition is a.'),
  ]),
  ex3=('Multi-word verb comprehension', 'Choose the best meaning or form.', [
    ('What does "contar con" mean?', ['to count on / rely on', 'to count up to', 'to tell about'], 'to count on / rely on',
     'Contar con = to count on / rely on. Contar alone = to count or to tell a story.'),
    ('What is the correct form of "to miss" in Spanish?', ['echar de menos a', 'faltar de', 'contar con'], 'echar de menos a',
     'Echar de menos + a + person = to miss someone. Faltar = to be lacking; contar con = to count on.'),
    ('What does "darse cuenta de que" require after it?', ['a complete clause', 'an infinitive', 'a noun only'], 'a complete clause',
     'Darse cuenta de que + subject + verb = to realise that… The full clause is required.'),
    ('What does "ponerse a + infinitive" express?', ['the sudden start of an action', 'an ongoing action', 'a completed action'], 'the sudden start of an action',
     'Ponerse a + infinitive = to suddenly start doing something — often emotional or unexpected.'),
    ('Which sentence uses "dar lugar a" correctly?', ['La tormenta dio lugar a inundaciones graves.', 'La tormenta dio lugar de inundaciones.', 'La tormenta dio lugar con inundaciones.'], 'La tormenta dio lugar a inundaciones graves.',
     'Dar lugar a = to lead to / give rise to. Always followed by a + noun.'),
  ]),
  game_desc='Master Spanish multi-word verb combinations: contar con, echar de menos, darse cuenta, and more. Reach 100 points to win.',
  items=[
    ('contar-con', 'contar con', 'to count on, rely on', 'essential combination', 'Siempre puedo <b>contar con</b> mis amigos.', 'Siempre puedo ______ ______ mis amigos. (count on)', 'contar con'),
    ('echar-de-menos', 'echar de menos', 'to miss (someone)', 'key combination', '<b>Echo de menos</b> a mi familia cuando viajo.', '______ ______ ______ a mi familia cuando viajo. (I miss)', 'echar de menos'),
    ('darse-cuenta', 'darse cuenta de que', 'to realise that', 'reflexive combination', 'No me <b>di cuenta de que</b> era tan tarde.', 'No me ______ ______ ______ ______ era tan tarde. (realised that)', 'darse cuenta de que'),
    ('llevar-gerundio', 'llevo… estudiando', 'I have been studying for…', 'duration with gerundio', '<b>Llevo</b> tres años <b>estudiando</b> español.', '______ tres años ______ español. (I have been studying)', 'llevo estudiando'),
    ('ponerse-a', 'ponerse a', 'to start to (suddenly)', 'sudden start', 'Se <b>puso a</b> llorar al oír la noticia.', 'Se ______ ______ llorar al oír la noticia. (started to)', 'ponerse a'),
    ('dar-con', 'dar con', 'to come across, hit upon', 'discovery', 'Al final <b>di con</b> la respuesta correcta.', 'Al final ______ ______ la respuesta correcta. (I hit upon)', 'dar con'),
    ('dar-lugar-a', 'dio lugar a', 'led to, gave rise to', 'cause-effect', 'El error <b>dio lugar a</b> una gran confusión.', 'El error ______ ______ ______ una gran confusión. (led to)', 'dio lugar a'),
    ('quedarse-sin', 'quedarse sin', 'to be left without', 'result combination', 'Después del discurso, me <b>quedé sin</b> palabras.', 'Después del discurso, me ______ ______ palabras. (was left without)', 'quedarse sin'),
  ],
),

'reflexive-verbs': dict(
  num='G14', short='Advanced Reflexive Verbs', title='Advanced Reflexive Verbs — Se me olvidó, se nos acabó',
  subtitle='Accidental events, reciprocal verbs, and the involuntary se',
  slides=[
    ('Reflexive verbs: a brief overview', None,
     '<p class="slide-explanation">At B2, you need to go beyond the basic reflexives (levantarse, ducharse) to three advanced uses: reciprocal, accidental/involuntary, and pronominal verbs with changed meaning.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Reciprocal:</b> Se escriben cada semana. (They write to each other every week.)</p>'
     '<p style="margin-top:8px"><b>Involuntary:</b> Se me olvidó el nombre. (I forgot the name — it slipped my mind.)</p>'
     '<p style="margin-top:8px"><b>Changed meaning:</b> ir → irse (to leave) · quedar → quedarse (to stay, to remain)</p></div>'),
    ('Reciprocal reflexives — each other', None,
     '<p class="slide-explanation">Plural reflexive pronouns (nos, os, se) can express that the action is mutual.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Se ayudan mutuamente.</b> (They help each other.)</p>'
     '<p style="margin-top:8px"><b>Nos conocimos en una conferencia.</b> (We met each other at a conference.)</p>'
     '<p style="margin-top:8px"><b>Siempre se discuten.</b> — ambiguous; add <b>el uno al otro / mutuamente</b> to clarify.</p></div>'),
    ('The involuntary se — accidental events', None,
     '<p class="slide-explanation">Spanish has a special construction for accidents and unintended events: <b>se + indirect object pronoun + verb + subject</b>. The person is the indirect object, not the agent.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Se me olvidó el libro.</b> (I forgot the book — literally: the book forgot itself to me.)</p>'
     '<p style="margin-top:8px"><b>Se nos acabó la leche.</b> (We ran out of milk.)</p>'
     '<p style="margin-top:8px"><b>Se le cayó el móvil.</b> (He/She dropped the phone.)</p></div>'
     '<p style="margin-top:12px">Key: the verb agrees with the thing (el libro → olvidó; la leche → acabó; el móvil → cayó).</p>'),
    ('Verbs with changed meaning when reflexive', None,
     '<p class="slide-explanation">Many important verbs have different meanings with and without the reflexive pronoun.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>ir → irse:</b> ir = to go · irse = to leave, to go away</p>'
     '<p style="margin-top:8px"><b>quedar → quedarse:</b> quedar = to arrange/to remain · quedarse = to stay</p>'
     '<p style="margin-top:8px"><b>llevar → llevarse:</b> llevar = to carry · llevarse bien con = to get on well with</p>'
     '<p style="margin-top:8px"><b>perder → perderse:</b> perder = to lose · perderse = to get lost / to miss out on</p></div>'),
    ('Se as passive and impersonal marker', None,
     '<p class="slide-explanation">At B2, se also appears in formal passive and impersonal constructions — a key overlap to recognise.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Se habla español.</b> (Spanish is spoken here.) — se pasivo</p>'
     '<p style="margin-top:8px"><b>Se vive bien aquí.</b> (Life is good here / One lives well here.) — impersonal</p>'
     '<p style="margin-top:8px"><b>Se me cayeron los papeles.</b> (I dropped my papers.) — involuntary</p></div>'),
  ],
  traps=[
    ('Se me olvidé el nombre.', '<strong>Se me olvidó</strong> el nombre.', 'Involuntary se: the verb agrees with the THING (el nombre, singular → olvidó), not with me'),
    ('Se nos acabaron la leche.', 'Se nos <strong>acabó</strong> la leche.', 'La leche is singular → acabó (not acabaron). Verb agrees with the grammatical subject (the thing).'),
    ('Me olvidé del nombre.', 'Se me olvidó el nombre. OR Me olvidé de él.', 'Olvidarse de = I forgot (voluntary forgetfulness). Se me olvidó = it slipped my mind (accidental). Both correct but different nuances.'),
    ('Se ayudan el uno con el otro.', 'Se ayudan <strong>el uno al otro</strong>.', 'Reciprocal with ayudar: el uno al otro (indirect object). El uno con el otro is used with estar, vivir etc.'),
    ('Nos fuimos a casa y quedamos allí.', 'Nos fuimos a casa y <strong>nos quedamos</strong> allí.', 'To stay = quedarse (reflexive): nos quedamos. Quedar without se = to arrange to meet or to have left over'),
  ],
  summary=[
    ('Reciprocal', 'se/nos/os + verb = each other', 'Se llaman todos los días.'),
    ('Involuntary', 'se + me/te/le/nos/os/les + verb (agrees with thing)', 'Se me cayó el vaso.'),
    ('Involuntary verbs', 'olvidar, caer, acabar, romper, perder, escapar', 'Se nos perdieron las llaves.'),
    ('Changed meaning', 'ir → irse; quedar → quedarse; perder → perderse', 'Me fui / Me quedé / Me perdí.'),
    ('Verb agreement', 'Verb agrees with the thing (subject), not the person', 'Se le cayeron los libros (pl.).'),
    ('Clarify reciprocal', 'mutuamente / el uno al otro', 'Se ayudan el uno al otro.'),
  ],
  ex1=('Choose the right reflexive form', 'Tap the correct option for each gap.', [
    ('______ las llaves. (I lost my keys — accidental)', ['Se me perdieron', 'Se me perdió', 'Me perdí'], 'Se me perdieron',
     'Involuntary se: las llaves (f.pl.) → se me perdieron (3rd plural). The verb agrees with las llaves.'),
    ('______ el móvil al suelo. (She dropped her phone)', ['Se le cayó', 'Se le cayeron', 'Se cayó'], 'Se le cayó',
     'Involuntary: el móvil (m.sing.) → se le cayó. The verb is singular.'),
    ('______ muy bien desde el primer día. (They got on well with each other)', ['Se llevan', 'Se lleva', 'Llevan'], 'Se llevan',
     'Reciprocal + llevarse bien con = to get on well with. They (ellos) → se llevan.'),
    ('______ la sal en la sopa. (She put too much salt — accidental)', ['Se le echó', 'Se le echaron', 'Le echó'], 'Se le echó',
     'Involuntary: la sal (f.sing.) → se le echó (3rd sing.). Too much salt ended up in the soup.'),
    ('Después de cenar, ______ en casa de sus amigos. (they stayed)', ['se quedaron', 'quedaron', 'se fueron'], 'se quedaron',
     'To stay = quedarse: se quedaron. Quedar (without se) = to arrange to meet; irse = to leave.'),
    ('Se conocieron en la universidad y ______ desde entonces. (they have helped each other)', ['se han ayudado', 'se ayudaron', 'se han ayudado mutuamente'], 'se han ayudado mutuamente',
     'Reciprocal + mutuamente = they have helped each other. Both options are correct; mutuamente clarifies.'),
  ]),
  ex2=('Complete the reflexive sentence', 'Type the missing word — no accents needed.', [
    ('Se ______ el bolso en el autobús. (She left it behind — accidental)', 'le',
     'Involuntary se + indirect object pronoun: se LE olvidó el bolso = she accidentally left behind her bag.'),
    ('Se nos ______ el azúcar. (We ran out of — the sugar)', 'acabo',
     'El azúcar (m.sing.) → se nos acabó (3rd sing.). Acabarse = to run out.'),
    ('Al salir, ______ a toda prisa. (they left quickly)', 'se fueron',
     'Irse = to leave/go away (reflexive). Se fueron = they left (3rd pl. indefinido of irse).'),
    ('Se ______ el cristal al caer. (the glass broke — accidental)', 'rompio',
     'El cristal (m.sing.) → se rompió. Romperse (involuntary) = to break (accidentally).'),
    ('Nos ______ bien desde el principio. (we got on well)', 'llevamos',
     'Llevarse bien = to get on well. Nos llevamos (1st pl. present of llevar + nos).'),
  ]),
  ex3=('Reflexive analysis', 'Choose the correct interpretation.', [
    ('What does "se me olvidó el paraguas" mean?', ['I forgot my umbrella (accidentally).', 'I intentionally left my umbrella.', 'My umbrella was forgotten by someone.'], 'I forgot my umbrella (accidentally).',
     'Se me olvidó = accidental forgetting — the umbrella "forgot itself to me". No blame assigned.'),
    ('Why is "se le cayeron los libros" plural?', ['Because los libros is plural.', 'Because "le" is plural.', 'Because "se" is plural.'], 'Because los libros is plural.',
     'In the involuntary se construction, the verb agrees with the thing (los libros, pl.) → cayeron.'),
    ('Which sentence uses a reciprocal reflexive?', ['Se escriben cartas el uno al otro.', 'Se le escribió una carta.', 'Se escribe una carta aquí.'], 'Se escriben cartas el uno al otro.',
     'El uno al otro clarifies the reciprocal meaning: they write letters to each other.'),
    ('What is the difference between "ir" and "irse"?', ['"Irse" means to leave/go away; "ir" means to go somewhere.', '"Irse" means to walk; "ir" means to run.', 'There is no difference.'], '"Irse" means to leave/go away; "ir" means to go somewhere.',
     'Ir = to go to a destination; irse = to leave, depart. ¿Adónde vas? (ir) vs Ya me voy (irse).'),
    ('Which is the correct involuntary construction for "we ran out of water"?', ['Se nos acabó el agua.', 'Se nos acabaron el agua.', 'Nos se acabó el agua.'], 'Se nos acabó el agua.',
     'El agua (f.sing., treated as m.sing. with el) → se nos acabó (3rd sing.). Pronoun order: se first.'),
  ]),
  game_desc='Master advanced reflexive verbs in Spanish: accidental events with se, reciprocal verbs, and verbs that change meaning with the reflexive. Reach 100 points to win.',
  items=[
    ('se-me-olvido', 'se me olvidó', 'I forgot (accidentally)', 'involuntary se singular', '<b>Se me olvidó</b> el libro en casa.', '______ ______ ______ el libro en casa. (I forgot — accidental)', 'se me olvido'),
    ('se-nos-acabo', 'se nos acabó', 'we ran out of', 'involuntary se plural subject', '<b>Se nos acabó</b> la gasolina en la autopista.', '______ ______ ______ la gasolina en la autopista. (we ran out of)', 'se nos acabo'),
    ('se-le-cayeron', 'se le cayeron', 'she/he dropped (pl.)', 'involuntary se plural thing', '<b>Se le cayeron</b> todos los papeles.', '______ ______ ______ todos los papeles. (she dropped — pl.)', 'se le cayeron'),
    ('se-llevan', 'se llevan bien', 'they get on well', 'reciprocal llevarse bien', '<b>Se llevan</b> muy bien desde que se conocieron.', '______ ______ muy bien desde que se conocieron. (they get on)', 'se llevan'),
    ('irse', 'irse', 'to leave, go away', 'reflexive changed meaning', 'Después de la reunión, <b>se fue</b> sin decir nada.', 'Después de la reunión, ______ sin decir nada. (left)', 'se fue'),
    ('quedarse', 'quedarse', 'to stay, remain', 'reflexive changed meaning', 'Decidieron <b>quedarse</b> en casa esa noche.', 'Decidieron ______ en casa esa noche. (stay)', 'quedarse'),
    ('se-rompieron', 'se rompieron', 'they broke (accidental, pl.)', 'involuntary rupture', '<b>Se rompieron</b> dos vasos durante la mudanza.', '______ ______ dos vasos durante la mudanza. (broke — accidental)', 'se rompieron'),
    ('el-uno-al-otro', 'el uno al otro', 'each other (with direct obj.)', 'reciprocal clarifier', 'Se ayudan <b>el uno al otro</b> en todo momento.', 'Se ayudan ______ ______ ______ ______ en todo momento.', 'el uno al otro'),
  ],
),

'reported-speech-advanced': dict(
  num='G15', short='Advanced Reported Speech', title='Advanced Reported Speech — Dijo que vendría',
  subtitle='Full backshift rules, reporting questions and commands, and tense mapping',
  slides=[
    ('The principle of backshift', None,
     '<p class="slide-explanation">When we report what someone said in the past, the tenses in the reported clause shift <b>one step back</b> in time. This "backshift" is systematic.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Original: <b>«Tengo hambre.»</b> → Reported: Dijo que <b>tenía</b> hambre.</p>'
     '<p style="margin-top:8px">Original: <b>«Vendré mañana.»</b> → Reported: Dijo que <b>vendría</b>.</p>'
     '<p style="margin-top:8px">Original: <b>«He terminado.»</b> → Reported: Dijo que <b>había terminado</b>.</p></div>'),
    ('The full backshift table', None,
     '<p class="slide-explanation">Every tense shifts exactly one step back when the reporting verb is in the past.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Present → Imperfecto:</b> «Estoy cansado» → Dijo que estaba cansado.</p>'
     '<p style="margin-top:8px"><b>Futuro → Condicional:</b> «Iré» → Dijo que iría.</p>'
     '<p style="margin-top:8px"><b>Perfecto → Pluscuamperfecto:</b> «He visto» → Dijo que había visto.</p>'
     '<p style="margin-top:8px"><b>Indefinido → Pluscuamperfecto:</b> «Fui» → Dijo que había ido.</p>'
     '<p style="margin-top:8px"><b>Imperfecto → Imperfecto:</b> «Vivía allí» → Dijo que vivía allí. (no change)</p></div>'),
    ('Reporting questions', None,
     '<p class="slide-explanation">Reported questions use <b>si</b> (for yes/no) or the question word, followed by normal word order (no inversion).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Direct: <b>«¿Vienes mañana?»</b> → Preguntó <b>si vendría</b> al día siguiente.</p>'
     '<p style="margin-top:8px">Direct: <b>«¿Dónde vives?»</b> → Me preguntó <b>dónde vivía</b>.</p>'
     '<p style="margin-top:8px">Direct: <b>«¿Qué has hecho?»</b> → Preguntó <b>qué había hecho</b>.</p></div>'
     '<p style="margin-top:12px">Note: no question marks in reported questions; question word + normal word order.</p>'),
    ('Reporting commands and requests', None,
     '<p class="slide-explanation">Direct commands become <b>infinitive structures</b> in reported speech.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Positive command: <b>«¡Cierra la puerta!»</b> → Le dijo que <b>cerrara</b> la puerta. (subjuntivo)</p>'
     '<p style="margin-top:8px">Positive: → Le <b>pidió que cerrara</b> la puerta. (más natural)</p>'
     '<p style="margin-top:8px">Negative: <b>«No salgas tarde.»</b> → Le pidió que <b>no saliera</b> tarde.</p></div>'
     '<p style="margin-top:12px">Commands in reported speech → imperfecto de subjuntivo (cerrara, saliera).</p>'),
    ('Changing pronouns, places, and times', None,
     '<p class="slide-explanation">Reported speech also adjusts pronouns, demonstratives, and time expressions.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>hoy → aquel día</b> · <b>mañana → al día siguiente</b> · <b>ayer → el día anterior</b></p>'
     '<p style="margin-top:8px"><b>aquí → allí</b> · <b>este → aquel</b> · <b>yo → él/ella</b></p>'
     '<p style="margin-top:8px">Direct: <b>«Hoy vengo aquí.»</b> → Dijo que <b>aquel día iba allí</b>.</p></div>'),
  ],
  traps=[
    ('Dijo que está cansado.', 'Dijo que <strong>estaba</strong> cansado.', 'Backshift: present (está) → imperfecto (estaba) when reporting verb is past'),
    ('Preguntó que dónde vivía. (reported question)', 'Preguntó <strong>dónde vivía</strong>. (no que after question word)', 'Reported questions: question word + clause, no que between. Dijo que… vs Preguntó dónde… (no que)'),
    ('Le dijo que cerrar la puerta. (command)', 'Le dijo que <strong>cerrara</strong> la puerta.', 'Reported commands use the imperfecto de subjuntivo (cerrara), not the infinitive'),
    ('Dijo que «iré» mañana. (reported)', 'Dijo que <strong>iría</strong> al día siguiente.', 'Futuro (iré) backshifts to condicional (iría); mañana → al día siguiente'),
    ('Preguntó si vendrías. (asked if you were coming)', 'Preguntó si <strong>vendría</strong>. (3rd person!)', 'In reported speech, the persons shift: ¿Vienes (tú)? → Preguntó si (yo) vendría. Check who is speaking to whom.'),
  ],
  summary=[
    ('Present → imperfecto', '«Estoy aquí» → Dijo que estaba allí.', 'está → estaba'),
    ('Futuro → condicional', '«Iré» → Dijo que iría.', 'iré → iría'),
    ('Perfecto → pluscuamperfecto', '«He comido» → Dijo que había comido.', 'he comido → había comido'),
    ('Reported questions', 'Preguntó si / Preguntó dónde/qué/cuándo…', 'Preguntó si vendría. / Preguntó qué había hecho.'),
    ('Reported commands', 'Le pidió que + imperfecto subj.', 'Le pidió que cerrara la puerta.'),
    ('Time expressions', 'hoy→aquel día; mañana→al día siguiente; ayer→el día anterior', 'Dijo que al día siguiente iría.'),
  ],
  ex1=('Choose the right reported form', 'Tap the correct backshift.', [
    ('«Tengo mucho trabajo.» → Dijo que ______ mucho trabajo.', ['tenía', 'tiene', 'ha tenido'], 'tenía',
     'Present (tengo) backshifts to imperfecto (tenía) in reported speech with past reporting verb.'),
    ('«Vendré mañana.» → Dijo que ______ al día siguiente.', ['vendría', 'vendrá', 'viniera'], 'vendría',
     'Futuro (vendré) backshifts to condicional (vendría). Mañana → al día siguiente.'),
    ('«He terminado el proyecto.» → Dijo que ______ el proyecto.', ['había terminado', 'terminó', 'ha terminado'], 'había terminado',
     'Perfecto (he terminado) backshifts to pluscuamperfecto (había terminado).'),
    ('«¿Dónde vives?» → Preguntó ______ .', ['dónde vivía', 'que dónde vivía', 'si dónde vivía'], 'dónde vivía',
     'Reported question with question word: preguntó + question word + clause (no que between).'),
    ('«¡Abre la ventana!» → Le pidió que ______ la ventana.', ['abriera', 'abra', 'abrió'], 'abriera',
     'Reported command: pedir que + imperfecto de subjuntivo (abriera). Never use the imperative directly.'),
    ('«¿Vienes mañana?» → Preguntó si ______ al día siguiente.', ['vendría', 'vendrías', 'vendrá'], 'vendría',
     'Reported yes/no question: si + backshifted verb. Futuro (vienes/vendrás) → condicional (vendría).'),
  ]),
  ex2=('Complete the reported speech', 'Type the missing word — no accents needed.', [
    ('«Estoy muy cansado.» → Dijo que ______ muy cansado. (backshift)', 'estaba',
     'Present (estoy) → imperfecto (estaba) in reported speech with past reporting verb.'),
    ('«Llegué ayer.» → Dijo que ______ llegado el día anterior. (backshift)', 'habia',
     'Indefinido (llegué) → pluscuamperfecto (había llegado) in reported speech.'),
    ('«¿Qué has hecho?» → Preguntó qué ______ hecho. (backshift)', 'habia',
     'Perfecto (has hecho) → pluscuamperfecto (había hecho). Reported question: preguntó qué había hecho.'),
    ('«¡No salgas tarde!» → Le pidió que no ______ tarde. (reported command)', 'saliera',
     'Reported negative command: le pidió que no + imperfecto de subjuntivo (saliera).'),
    ('«Mañana iré.» → Dijo que ______ al día siguiente. (backshift)', 'iria',
     'Futuro (iré) → condicional (iría). Mañana → al día siguiente.'),
  ]),
  ex3=('Reported speech analysis', 'Choose the correct option.', [
    ('Which backshift is correct for "yo tengo hambre"?', ['Dijo que tenía hambre.', 'Dijo que tiene hambre.', 'Dijo que ha tenido hambre.'], 'Dijo que tenía hambre.',
     'Present (tengo) → imperfecto (tenía) — the standard first-step backshift with a past reporting verb.'),
    ('How do you report the question "¿Dónde vives?"?', ['Preguntó dónde vivía.', 'Preguntó que dónde vivía.', 'Preguntó si dónde vivía.'], 'Preguntó dónde vivía.',
     'Reported question with question word: preguntó + question word + normal clause. No que between.'),
    ('How do you report the command "¡Come más!"?', ['Le dijo que comiera más.', 'Le dijo que come más.', 'Le dijo comer más.'], 'Le dijo que comiera más.',
     'Reported command: decir/pedir + que + imperfecto de subjuntivo (comiera).'),
    ('Which time expression change is correct?', ['"Mañana" becomes "al día siguiente" in reported speech.', '"Mañana" stays "mañana" in reported speech.', '"Mañana" becomes "ayer" in reported speech.'], '"Mañana" becomes "al día siguiente" in reported speech.',
     'Time expressions shift in reported speech: mañana → al día siguiente; hoy → aquel día; ayer → el día anterior.'),
    ('Which sentence has a reported speech error?', ['Preguntó que dónde vivía.', 'Dijo que tenía frío.', 'Preguntó si vendría.'], 'Preguntó que dónde vivía.',
     'Reported questions with a question word do NOT take que: preguntó dónde (not preguntó que dónde).'),
  ]),
  game_desc='Master advanced reported speech in Spanish: backshift rules, reporting questions, and reporting commands. Reach 100 points to win.',
  items=[
    ('dijo-que-tenia', 'dijo que tenía', 'said that she had (backshift)', 'present → imperfecto', 'María <b>dijo que tenía</b> mucho trabajo.', 'María ______ ______ ______ mucho trabajo. (said she had)', 'dijo que tenia'),
    ('dijo-que-vendria', 'dijo que vendría', 'said she would come (futuro→cond.)', 'futuro → condicional', 'Dijo que <b>vendría</b> al día siguiente.', 'Dijo que ______ al día siguiente. (said she would come)', 'dijo que vendria'),
    ('habia-terminado', 'había terminado', 'had finished (backshift)', 'perfecto → pluscuamperfecto', 'Dijo que <b>había terminado</b> el proyecto.', 'Dijo que ______ ______ el proyecto. (had finished)', 'habia terminado'),
    ('pregunto-donde', 'preguntó dónde', 'asked where', 'reported question (place)', 'Me <b>preguntó dónde</b> vivía.', 'Me ______ ______ vivía. (asked where)', 'pregunto donde'),
    ('pregunto-si', 'preguntó si', 'asked whether', 'reported yes/no question', 'Me <b>preguntó si</b> vendría a la fiesta.', 'Me ______ ______ vendría a la fiesta. (asked whether)', 'pregunto si'),
    ('le-pidio-que', 'le pidió que + imperfecto subj.', 'asked her to (command)', 'reported command', 'Le <b>pidió que cerrara</b> la puerta.', 'Le ______ ______ ______ cerrara la puerta. (asked her to)', 'le pidio que'),
    ('al-dia-siguiente', 'al día siguiente', 'the next day', 'time expression shift', 'Dijo que vendría <b>al día siguiente</b>.', 'Dijo que vendría ______ ______ ______ . (the next day)', 'al dia siguiente'),
    ('aquel-dia', 'aquel día', 'that day', 'time expression shift', 'Dijo que <b>aquel día</b> no podía venir.', 'Dijo que ______ ______ no podía venir. (that day)', 'aquel dia'),
  ],
),

}
