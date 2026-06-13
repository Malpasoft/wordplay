# -*- coding: utf-8 -*-
"""espanol-en B2 grammar content — batch 2 (chapters G6-G10)."""

CHAPTERS = {

'inversion': dict(
  num='G6', short='Inversion', title='Inversion — Nunca he visto tal cosa',
  subtitle='Fronted negatives and emphasis that trigger subject-verb inversion',
  slides=[
    ('What is inversion and when does it happen?', None,
     '<p class="slide-explanation">In Spanish, certain adverbs or phrases placed at the start of a sentence push the <b>subject</b> after the <b>verb</b>. This creates emphasis and a more formal, literary register.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Normal: <b>Yo nunca había visto tal cosa.</b></p>'
     '<p style="margin-top:8px">Inverted (emphasised): <b>Nunca había yo visto tal cosa.</b> — formal</p>'
     '<p style="margin-top:8px">Most common in written/formal registers, reported speech, and after direct speech.</p></div>'),
    ('After direct speech', None,
     '<p class="slide-explanation">When the reporting clause follows direct speech, Spanish always inverts subject and verb.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>—No puedo ir —dijo María.</b></p>'
     '<p style="margin-top:8px"><b>—¿Has comido? —preguntó el médico.</b></p>'
     '<p style="margin-top:8px">The pattern is: —Direct speech— + verb + subject. Subject never comes before the verb here.</p></div>'),
    ('Fronted negative adverbs', None,
     '<p class="slide-explanation">Fronting <b>nunca, jamás, apenas, ni siquiera, solo, tampoco</b> for emphasis triggers inversion.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Nunca he visto</b> algo así. → <b>Nunca he visto</b> yo algo así. (more emphatic)</p>'
     '<p style="margin-top:8px"><b>Apenas había terminado</b> de comer <b>cuando</b> llegaron las visitas.</p>'
     '<p style="margin-top:8px"><b>Ni siquiera llamó</b> para avisar.</p></div>'
     '<p style="margin-top:16px">In English these trigger full inversion (Never have I seen…). Spanish uses the subject optionally after the verb.</p>'),
    ('Fronted adverbials of place and manner', None,
     '<p class="slide-explanation">Literary Spanish often fronts place or manner phrases — the subject follows the verb.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Aquí viven los artistas más importantes del siglo.</b></p>'
     '<p style="margin-top:8px"><b>En el fondo del valle se esconden los pueblos más antiguos.</b></p>'
     '<p style="margin-top:8px"><b>Así hablan los que tienen experiencia.</b></p></div>'),
    ('Inversion in questions and exclamations', None,
     '<p class="slide-explanation">Spanish always inverts in direct questions. In exclamations, fronted elements also trigger inversion.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Question: <b>¿Adónde va usted?</b> (Where are you going?) — always inverted</p>'
     '<p style="margin-top:8px">Exclamation: <b>¡Qué raro es este hombre!</b> → <b>¡Qué raro está siendo todo esto!</b></p>'
     '<p style="margin-top:8px">After <b>que</b> in reported questions: <b>Me preguntó que dónde vivía yo.</b></p></div>'),
  ],
  traps=[
    ('—Lo haré —ella dijo.', '—Lo haré —dijo <strong>ella</strong>.', 'After direct speech the reporting verb comes before the subject: dijo ella, not ella dijo'),
    ('Nunca yo he visto algo así.', '<strong>Nunca he visto</strong> yo algo así. / Nunca he visto algo así.', 'When fronting nunca, the adverb comes first, then the verb group, then the optional subject: Nunca he visto (yo)'),
    ('Aquí los artistas viven.', 'Aquí <strong>viven los artistas</strong>.', 'Fronted place adverbs trigger verb-before-subject inversion: aquí viven los artistas'),
    ('Apenas terminé cuando llegan.', 'Apenas <strong>había terminado</strong> cuando <strong>llegaron</strong>.', 'Apenas… cuando expresses two closely timed past events: pluscuamperfecto + indefinido'),
    ('¿Dónde vas tú? (formal, to boss)', '¿Adónde <strong>va usted</strong>?', 'Formal questions use usted with inversion; adónde for movement destinations'),
  ],
  summary=[
    ('Direct speech', '—Text— + verb + subject', '—No sé —respondió ella.'),
    ('Fronted negative', 'Nunca/Jamás/Apenas + verb (+ subject)', 'Nunca había visto yo tal caos.'),
    ('Barely…when', 'Apenas + pluscuamperfecto + cuando + indefinido', 'Apenas había llegado cuando sonó el teléfono.'),
    ('Fronted place', 'Place/manner phrase + verb + subject', 'Aquí viven los mejores pintores.'),
    ('Questions', 'Question word + verb + subject', '¿Adónde va usted?'),
    ('Register', 'Inversion = formal/literary/emphatic', 'Neutral: No había visto nada igual. Formal: Nada igual había visto.'),
  ],
  ex1=('Choose the right order', 'Tap the correct inverted form.', [
    ('Which correctly follows direct speech?', ['—Llegaré tarde —dijo Marcos.', '—Llegaré tarde —Marcos dijo.', '—Llegaré tarde —Marcos ha dicho.'], '—Llegaré tarde —dijo Marcos.',
     'After direct speech: verb (dijo) before subject (Marcos). Never subject-before-verb here.'),
    ('Which uses fronted nunca correctly?', ['Nunca había yo leído un libro tan emocionante.', 'Nunca yo había leído un libro tan emocionante.', 'Yo nunca había leído un libro tan emocionante.'], 'Nunca había yo leído un libro tan emocionante.',
     'Fronted nunca: Nunca + verb group (había leído) + subject (yo). Subject comes after the verb.'),
    ('Which uses apenas…cuando correctly?', ['Apenas había terminado el examen cuando cortaron la luz.', 'Apenas termino el examen cuando cortaron la luz.', 'Apenas había terminado el examen cuando cortan la luz.'], 'Apenas había terminado el examen cuando cortaron la luz.',
     'Apenas + pluscuamperfecto (había terminado) + cuando + indefinido (cortaron) — the classic sequence.'),
    ('Which fronts a place adverbial correctly?', ['Aquí viven las familias más antiguas del pueblo.', 'Aquí las familias más antiguas viven del pueblo.', 'Aquí las familias viven más antiguas.'], 'Aquí viven las familias más antiguas del pueblo.',
     'Fronted aquí triggers inversion: aquí viven (verb) las familias (subject).'),
    ('Which formal question is correct?', ['¿Adónde va usted?', '¿Adónde usted va?', '¿Dónde usted va?'], '¿Adónde va usted?',
     'Questions always invert: adónde (movement) + va (verb) + usted (subject after verb).'),
    ('Which sentence has correct inversion?', ['En el fondo del valle se esconde el pueblo.', 'En el fondo del valle el pueblo se esconde.', 'El pueblo se esconde en el fondo del valle.'], 'En el fondo del valle se esconde el pueblo.',
     'Fronted place phrase + verb (se esconde) + subject (el pueblo) = correct literary inversion.'),
  ]),
  ex2=('Complete with the right order', 'Type the missing word — no accents needed.', [
    ('—No quiero ir —______ ella. (she said)', 'dijo',
     'After direct speech: verb (dijo) then subject (ella). Decir → dijo.'),
    ('______ había llegado al aeropuerto cuando cancelaron el vuelo. (barely)', 'apenas',
     'Apenas + pluscuamperfecto = barely had… — introduces an event that was just completed.'),
    ('Aquí ______ los mejores artesanos de la región. (live)', 'viven',
     'Fronted place (aquí) + inverted verb (viven) + subject (los artesanos).'),
    ('Nunca ______ yo entendido la razón. (I had)', 'habia',
     'Fronted nunca: Nunca había yo entendido — pluscuamperfecto with inverted subject.'),
    ('¿______ va usted tan tarde? (why)', 'por que',
     '¿Por qué va usted? — question word + verb + subject (usted) in formal register.'),
  ]),
  ex3=('Inversion or not?', 'Choose the option with correct or no inversion.', [
    ('Which sentence correctly quotes direct speech?', ['—Vendré mañana —prometió el médico.', '—Vendré mañana —el médico prometió.', '—Vendré mañana —prometió—el médico.'], '—Vendré mañana —prometió el médico.',
     'Reporting verb before subject: prometió el médico. A comma or dash does not separate verb from subject here.'),
    ('Which sentence most naturally fronts a negative adverb?', ['Jamás había escuchado una música tan bella.', 'Jamás una música tan bella había escuchado.', 'Una música tan bella jamás había escuchado yo.'], 'Jamás había escuchado una música tan bella.',
     'Jamás + verb group directly after = the natural fronted form. Other orders sound awkward.'),
    ('Which sentence correctly expresses "barely had they arrived when…"?', ['Apenas habían llegado cuando empezó a llover.', 'Apenas llegaron cuando empezaba a llover.', 'Apenas llegaban cuando empezó a llover.'], 'Apenas habían llegado cuando empezó a llover.',
     'Apenas + pluscuamperfecto (habían llegado) + cuando + indefinido (empezó) — the standard sequence.'),
    ('Which is a correct formal question with inversion?', ['¿A qué hora llega el tren?', '¿A qué hora el tren llega?', '¿El tren a qué hora llega?'], '¿A qué hora llega el tren?',
     'Questions always use question word + verb + subject order: llega (verb) el tren (subject).'),
    ('Which fronts a manner adverb correctly?', ['Así hablan los que conocen bien el tema.', 'Así los que conocen bien el tema hablan.', 'Así se hablan los que conocen bien el tema.'], 'Así hablan los que conocen bien el tema.',
     'Fronted así + verb (hablan) + subject (los que conocen…) = natural literary inversion.'),
  ]),
  game_desc='Master inversion in Spanish: after direct speech, fronted negatives, and formal emphatic sentences. Reach 100 points to win.',
  items=[
    ('dijo-ella', 'dijo ella (post-speech)', 'she said — verb before subject after direct speech', 'direct speech inversion', '—No lo sabía —<b>dijo ella</b>.', '—No lo sabía — ______ ______ . (she said)', 'dijo ella'),
    ('nunca-habia', 'nunca había', 'never had (fronted)', 'fronted negative', '<b>Nunca había</b> visto un paisaje tan impresionante.', '______ ______ visto un paisaje tan impresionante. (never had)', 'nunca habia'),
    ('apenas-cuando', 'apenas…cuando', 'barely…when', 'sequence of events', '<b>Apenas</b> había terminado <b>cuando</b> llamaron.', '______ había terminado ______ llamaron. (barely…when)', 'apenas cuando'),
    ('aqui-viven', 'aquí viven', 'here live (inverted)', 'place fronting', '<b>Aquí viven</b> los artistas del barrio.', '______ ______ los artistas del barrio. (here live)', 'aqui viven'),
    ('jamas', 'jamás', 'never (emphatic)', 'emphatic negative', '<b>Jamás</b> había escuchado algo tan hermoso.', '______ había escuchado algo tan hermoso. (never — emphatic)', 'jamas'),
    ('ni-siquiera', 'ni siquiera', 'not even', 'fronted emphatic negative', '<b>Ni siquiera</b> avisó antes de salir.', '______ ______ avisó antes de salir. (not even)', 'ni siquiera'),
    ('apenas-habia', 'apenas había terminado cuando', 'barely had finished when', 'pluscuamperfecto sequence', '<b>Apenas había terminado</b> de comer <b>cuando</b> llegaron las visitas.', '______ ______ terminado de comer ______ llegaron las visitas.', 'apenas habia'),
    ('en-el-fondo', 'en el fondo… se esconde', 'deep down/in the depths… hides', 'place inversion', '<b>En el fondo del valle se esconde</b> el pueblo más antiguo de la región.', '______ ______ ______ ______ ______ el pueblo. (in the depths… hides)', 'en el fondo'),
  ],
),

'mixed-conditionals': dict(
  num='G7', short='Mixed Conditionals', title='Mixed Conditionals — Si hubiera estudiado, sabría',
  subtitle='Mixing past hypothesis with present result — and vice versa',
  slides=[
    ('What is a mixed conditional?', None,
     '<p class="slide-explanation">A <b>mixed conditional</b> links conditions and results across different time frames. The two most common types at B2 are:</p>'
     '<ul style="margin:12px 0 0 20px;line-height:1.8">'
     '<li>Past → Present: <b>Si hubiera estudiado más, ahora sabría más.</b> (If I had studied more, I would know more now.)</li>'
     '<li>Present → Past: <b>Si no fuera tan tímida, lo habría dicho ayer.</b> (If she weren\'t so shy, she would have said it yesterday.)</li></ul>'
     '<p style="margin-top:12px">The key: the <b>if</b> clause and the <b>result</b> clause refer to different times.</p>'),
    ('Type 1 mixed: past hypothesis → present result', None,
     '<p class="slide-explanation">Past unreal condition (pluscuamperfecto subjunctive) + present result (condicional simple).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Si + hubiera/hubiese + participio → condicional (sabría/tendría/estaría)</b></p>'
     '<p style="margin-top:8px"><b>Si hubiera ahorrado más, ahora tendría dinero suficiente.</b></p>'
     '<p style="margin-top:8px"><b>Si se hubiera casado entonces, hoy estaría divorciada.</b></p></div>'
     '<p style="margin-top:12px">The result clause often contains <b>ahora, hoy, ya</b> to anchor it in the present.</p>'),
    ('Type 2 mixed: present hypothesis → past result', None,
     '<p class="slide-explanation">Present/habitual unreal condition (imperfecto subjunctive) + past result (condicional perfecto).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Si + imperfecto subjunctive → habría/habría + participio</b></p>'
     '<p style="margin-top:8px"><b>Si no fuera tan impulsivo, no lo habría dicho.</b> (If he weren\'t so impulsive, he wouldn\'t have said it.)</p>'
     '<p style="margin-top:8px"><b>Si tuviera más paciencia, lo habría intentado otra vez.</b></p></div>'),
    ('Recognising the time markers', None,
     '<p class="slide-explanation">Time adverbs signal which part is past and which is present/future.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Past hypothesis:</b> si hubiera nacido en Madrid, si hubiese estudiado</p>'
     '<p style="margin-top:8px"><b>Present result:</b> ahora, hoy, actualmente, ya, todavía</p>'
     '<p style="margin-top:8px"><b>Present hypothesis:</b> si fuera más alto, si tuviera dinero</p>'
     '<p style="margin-top:8px"><b>Past result:</b> habría dicho, habría venido, habría cambiado</p></div>'),
    ('Common mixed conditional patterns', None,
     '<p class="slide-explanation">Fixed patterns to recognise and reproduce:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>1. <b>Si hubiera [hecho X], ahora [sería/tendría/estaría Y].</b></p>'
     '<p style="margin-top:8px">2. <b>Si no hubiera [hecho X], ahora [sería/estaría Y].</b></p>'
     '<p style="margin-top:8px">3. <b>Si [fuera/tuviera X], [habría hecho Y] antes.</b></p>'
     '<p style="margin-top:8px">4. <b>Si no [fuera/tuviera X], [no habría hecho Y].</b></p></div>'),
  ],
  traps=[
    ('Si hubiera venido, habría sido mejor. (mixed?)', 'Si hubiera venido, <strong>habría sido</strong> mejor. — This is a type 3 conditional (past→past), NOT mixed.', 'Both clauses in the past = type 3 conditional, not a mixed conditional. A mixed conditional has clauses in different time frames'),
    ('Si tendría dinero, lo habría comprado.', 'Si <strong>tuviera</strong> dinero, lo habría comprado.', 'The if-clause NEVER takes the conditional (tendría) — use the subjunctive: tuviera'),
    ('Si hubiera estudiado, ahora sabría.', 'Correct! <strong>Si hubiera estudiado</strong> (past subj.) + <strong>sabría</strong> (conditional) — past hypothesis → present result.', 'This is a correct mixed conditional: past subjunctive if-clause + conditional result.'),
    ('Si no era tan tímida, lo habría dicho.', 'Si no <strong>fuera</strong> tan tímida, lo habría dicho.', 'Present/habitual hypothesis uses imperfecto subjunctive (fuera), not the indicative (era)'),
    ('Si hubiera ido allí, ahora habría sabido más.', 'Si hubiera ido allí, ahora <strong>sabría</strong> más.', 'When the result is present, use the condicional simple (sabría), not the condicional perfecto (habría sabido)'),
  ],
  summary=[
    ('Past → Present', 'Si + hubiera/hubiese + pp → condicional simple', 'Si hubiera estudiado, ahora sabría más.'),
    ('Present → Past', 'Si + imperfecto subj. → condicional perfecto', 'Si no fuera tan impulsivo, no lo habría dicho.'),
    ('Time markers (past if)', 'si hubiera nacido, si hubiese trabajado', 'Si hubiera nacido en Madrid…'),
    ('Time markers (present result)', 'ahora, hoy, actualmente, ya', '…ahora viviría allí.'),
    ('Never in if-clause', 'NEVER conditional in if-clause: *si tendría*', 'Always: si tuviera / si hubiera tenido'),
    ('Type 3 vs mixed', 'Type 3 = both past. Mixed = one past + one present/future.', 'Si hubiera ido, lo habría visto (type 3) ≠ Si hubiera ido, lo vería (mixed)'),
  ],
  ex1=('Choose the right verb form', 'Tap the correct mixed conditional form.', [
    ('Si ______ en España, ahora hablaría español perfectamente.', ['hubiera nacido', 'naciera', 'había nacido'], 'hubiera nacido',
     'Past hypothesis → present result: si + pluscuamperfecto subjunctive (hubiera nacido) + condicional (hablaría).'),
    ('Si no ______ tan orgulloso, lo habría pedido ayuda ayer.', ['fuera', 'hubiera sido', 'es'], 'fuera',
     'Present/habitual character trait → past result: si + imperfecto subjunctive (fuera) + condicional perfecto (habría pedido).'),
    ('Si hubiera empezado a ahorrar a los veinte años, ahora ______ mucho dinero.', ['tendría', 'habría tenido', 'tuviera'], 'tendría',
     'Past hypothesis → present result: result clause = condicional simple (tendría), not condicional perfecto.'),
    ('Si ______ más paciente por naturaleza, no lo habría dicho tan bruscamente.', ['fuera', 'hubiera sido', 'sería'], 'fuera',
     'Habitual character (by nature) → past result: si + fuera (imperfecto subj.) + habría dicho (cond. perfecto).'),
    ('Si Juan no ______ enfermado de niño, hoy sería atleta profesional.', ['hubiera', 'fuera', 'había'], 'hubiera',
     'Past event (illness as child) → present result: si + hubiera enfermado + sería.'),
    ('Si no ______ tanto trabajo, lo habría terminado antes.', ['tuviera', 'hubiera tenido', 'tendría'], 'tuviera',
     'Habitual state (has a lot of work generally) → past result: si + tuviera (imperfecto subj.) + habría terminado.'),
  ]),
  ex2=('Complete the mixed conditional', 'Type the missing word — no accents needed.', [
    ('Si ______ estudiado más de joven, ahora tendría mejor trabajo. (I had)', 'hubiera',
     'Si hubiera + participio = past unreal hypothesis. Hubiera estudiado = if I had studied.'),
    ('Si no ______ tan nervioso por naturaleza, no lo habría dicho. (he were)', 'fuera',
     'Present/habitual trait: si + imperfecto subjunctive (fuera) → past result (habría dicho).'),
    ('Si hubiera llegado a tiempo, ahora ______ en casa. (I would be)', 'estaria',
     'Past hypothesis → present result: si hubiera llegado → condicional simple (estaría).'),
    ('Si tuviera más experiencia, lo ______ conseguido antes. (she would have)', 'habria',
     'Present/habitual condition (she lacks experience) → past result: habría conseguido.'),
    ('Si ______ nacido en otro país, mi vida sería muy diferente. (I had)', 'hubiera',
     'Si hubiera nacido = if I had been born — past unreal hypothesis.'),
  ]),
  ex3=('Mixed or not?', 'Identify the correct mixed conditional.', [
    ('Which is a mixed conditional (past hypothesis → present result)?', ['Si hubiera estudiado Medicina, ahora sería médico.', 'Si hubiera estudiado Medicina, habría sido médico.', 'Si estudiara Medicina, sería médico.'], 'Si hubiera estudiado Medicina, ahora sería médico.',
     'Past if-clause (hubiera estudiado) + present result (sería) = mixed. The other is type 3; the last is type 2 (not mixed).'),
    ('Which is a mixed conditional (present trait → past result)?', ['Si no fuera tan tímida, lo habría dicho antes.', 'Si no hubiera sido tan tímida, lo habría dicho antes.', 'Si no fuera tan tímida, lo diría ahora.'], 'Si no fuera tan tímida, lo habría dicho antes.',
     'Present trait (fuera, imperfecto subj.) + past result (habría dicho, cond. perfecto) = mixed. The middle is type 3.'),
    ('Which conditional is formed incorrectly?', ['Si tendría más dinero, lo habría comprado.', 'Si tuviera más dinero, lo habría comprado.', 'Si hubiera tenido más dinero, ahora lo tendría.'], 'Si tendría más dinero, lo habría comprado.',
     'The if-clause NEVER takes the conditional (tendría). Use si tuviera (imperfecto subj.) or si hubiera tenido.'),
    ('Which time marker signals a present result in a mixed conditional?', ['ahora', 'ayer', 'el año pasado'], 'ahora',
     'Ahora, hoy, actualmente anchor the result in the present, making it a mixed conditional.'),
    ('What is the structure of "past hypothesis → present result"?', ['Si + hubiera/hubiese + pp → condicional simple', 'Si + imperfecto subj. → condicional perfecto', 'Si + imperfecto subj. → condicional simple'], 'Si + hubiera/hubiese + pp → condicional simple',
     'Past hypothesis = pluscuamperfecto subjunctive in if-clause; present result = condicional simple.'),
  ]),
  game_desc='Master mixed conditionals in Spanish: past hypothesis with present result, and present traits with past results. Reach 100 points to win.',
  items=[
    ('hubiera-nacido', 'si hubiera nacido', 'if I/she had been born', 'past hypothesis', '<b>Si hubiera nacido</b> en España, hablaría español de niño.', '______ ______ ______ en España, hablaría español de niño.', 'si hubiera nacido'),
    ('ahora-tendria', 'ahora tendría', 'I would now have', 'present result', 'Si hubiera ahorrado, <b>ahora tendría</b> suficiente.', 'Si hubiera ahorrado, ______ ______ suficiente. (I would now have)', 'ahora tendria'),
    ('fuera-habia', 'si fuera… lo habría', 'if she were… she would have', 'present trait → past result', '<b>Si fuera</b> más paciente, <b>lo habría</b> intentado.', '______ ______ más paciente, ______ ______ intentado. (present trait → past result)', 'si fuera'),
    ('no-hubiera', 'si no hubiera', 'if I/she had not', 'negative past hypothesis', '<b>Si no hubiera</b> aceptado ese trabajo, estaría en casa ahora.', '______ ______ ______ aceptado ese trabajo, estaría en casa. (if not had)', 'si no hubiera'),
    ('habria-dicho', 'lo habría dicho', 'she would have said it', 'past result', 'Si no fuera tan tímida, <b>lo habría dicho</b> antes.', 'Si no fuera tan tímida, ______ ______ ______ antes. (she would have said)', 'lo habria dicho'),
    ('ahora-estaria', 'ahora estaría', 'I would be now', 'present result', 'Si hubiera llegado a tiempo, <b>ahora estaría</b> en casa.', 'Si hubiera llegado a tiempo, ______ ______ en casa. (I would be now)', 'ahora estaria'),
    ('si-tuviera-habria', 'si tuviera… habría', 'if she had (trait)… she would have', 'habitual trait → past result', '<b>Si tuviera</b> más confianza, <b>habría</b> pedido el ascenso.', '______ ______ más confianza, ______ pedido el ascenso.', 'si tuviera'),
    ('hoy-seria', 'hoy sería', 'today she/he would be', 'present result', 'Si hubiera seguido entrenando, <b>hoy sería</b> campeona.', 'Si hubiera seguido entrenando, ______ ______ campeona. (today she would be)', 'hoy seria'),
  ],
),

'modals-advanced': dict(
  num='G8', short='Advanced Modals', title='Advanced Modals — Debería haber llegado ya',
  subtitle='Modal verbs in the past: what should have been, could have been, must have been',
  slides=[
    ('Modal perfects: the pattern', None,
     '<p class="slide-explanation">Spanish forms modal perfects by putting the auxiliary in the <b>conditional</b> and adding <b>haber + participle</b>: could have, should have, must have (past).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>debería haber + pp</b> → should have (past): Debería haber llamado. (I should have called.)</p>'
     '<p style="margin-top:8px"><b>podría haber + pp</b> → could have: Podrías haber avisado. (You could have warned us.)</p>'
     '<p style="margin-top:8px"><b>habría podido + inf</b> → could have (alt.): Habría podido ganar. (He could have won.)</p></div>'),
    ('Deber + haber vs deber de + haber', None,
     '<p class="slide-explanation">The preposition <b>de</b> changes meaning: obligation vs deduction.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>debería haber + pp</b> = should have (obligation not fulfilled)</p>'
     '<p style="margin-top:8px"><b>debe de haber + pp</b> = must have (logical deduction about past)</p>'
     '<p style="margin-top:8px"><b>Deberías haber llegado</b> antes. (You should have arrived sooner.)</p>'
     '<p style="margin-top:8px"><b>Debe de haber llegado</b> ya. (He must have already arrived.)</p></div>'),
    ('Could have — two forms', None,
     '<p class="slide-explanation">Two equivalent structures for "could have":</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>podría haber + pp:</b> Podría haber ganado. (He could have won.)</p>'
     '<p style="margin-top:8px"><b>habría podido + inf:</b> Habría podido ganar. (same meaning)</p>'
     '<p style="margin-top:8px">Both forms are equally valid — choose one per sentence.</p></div>'
     '<p style="margin-top:12px">Note: <b>Podría haberlo hecho</b> — the object pronoun goes on haber or the infinitive.</p>'),
    ('Must have (deduction) — past', None,
     '<p class="slide-explanation">For logical deduction about past events, use <b>deber de haber + pp</b> or the more colloquial <b>tener que haber + pp</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Debe de haber salido ya.</b> (He must have left already.)</p>'
     '<p style="margin-top:8px"><b>Tiene que haber sido un error.</b> (It must have been a mistake.)</p>'
     '<p style="margin-top:8px"><b>Han debido de olvidarlo.</b> (They must have forgotten it.) — alternative order</p></div>'),
    ('Common mistakes and register', None,
     '<p class="slide-explanation">Avoid English-influenced errors with modal perfects.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Never: <b>*debería de haber</b> (mixing obligation with deduction marker)</p>'
     '<p style="margin-top:8px">Never: <b>*podría de haber</b> (de does not go with poder)</p>'
     '<p style="margin-top:8px">Colloquial: <b>Tendría que haberlo visto.</b> (You should have seen it!) — surprise/regret</p></div>'),
  ],
  traps=[
    ('Debería de haber llamado. (obligation)', '<strong>Debería haber</strong> llamado. (obligation — no de)', 'Deber + obligation: NO de. Deber de = deduction only: debe de haber llegado'),
    ('Podría de haber ganado.', '<strong>Podría haber</strong> ganado.', 'Poder never takes de in the compound modal: podría haber (not podría de haber)'),
    ('Debe haber llegado. (deduction)', '<strong>Debe de haber</strong> llegado. (deduction)', 'For past deduction, deber DE haber is the standard form (though debe haber is accepted colloquially)'),
    ('Lo podría haber hecho o podría haberlo hecho.', 'Both are correct: <strong>lo podría haber hecho</strong> and <strong>podría haberlo hecho</strong>.', 'Object pronoun can attach to the auxiliary or to the infinitive in compound modals — both positions are correct'),
    ('Habría debido hacer eso.', '<strong>Debería haber</strong> hecho eso.', 'The natural Spanish form for "should have done" is debería haber + pp — habría debido is clunky'),
  ],
  summary=[
    ('Should have', 'debería/deberías/etc. + haber + pp', 'Deberías haber llamado antes.'),
    ('Could have', 'podría haber + pp / habría podido + inf', 'Podría haber ganado fácilmente.'),
    ('Must have (deduction)', 'debe de haber + pp / tiene que haber + pp', 'Debe de haber llegado ya.'),
    ('Should not have', 'no debería haber + pp', 'No deberías haber dicho eso.'),
    ('Could not have', 'no podría haber + pp', 'No podría haberlo hecho sin tu ayuda.'),
    ('Key rule', 'deber = obligation (no de); deber de = deduction', 'debería haber ≠ debe de haber'),
  ],
  ex1=('Choose the right modal perfect', 'Tap the best option.', [
    ('______ haberlo dicho antes. (you should have)', ['Deberías', 'Debes de', 'Podrías'], 'Deberías',
     'Should have = debería/deberías + haber + pp. Deber de is for deduction, not obligation.'),
    ('______ haber ganado el partido si no hubiera llovido. (they could have)', ['Podrían', 'Deberían', 'Deben'], 'Podrían',
     'Could have = podría/podrían + haber + pp — expressing an unfulfilled possibility.'),
    ('Lleva tres horas sin contestar. ______ de haber salido ya. (he must have)', ['Debe', 'Debería', 'Podría'], 'Debe',
     'Past deduction = debe de haber + pp. Debería is obligation; podría is possibility.'),
    ('______ haber esperado un poco más, pero no pudo. (he could have)', ['Podría', 'Debería', 'Debe de'], 'Podría',
     'Podría haber + pp = could have done (unfulfilled ability). Debería = should have.'),
    ('No ______ haber dicho eso — fue muy cruel. (she should not have)', ['debería', 'podría', 'debe de'], 'debería',
     'Should not have = no debería haber + pp (unfulfilled obligation — she did it, but she should not have).'),
    ('______ haber ganado más dinero si hubiera negociado mejor. (she could have)', ['Habría podido', 'Hubiera podido', 'Habría debido'], 'Habría podido',
     'Habría podido + infinitive = could have (alternative to podría haber + pp). Hubiera podido belongs in a si-clause.'),
  ]),
  ex2=('Complete the sentence', 'Type the missing word — no accents needed.', [
    ('______ haber llegado antes — había tiempo. (you should have)', 'deberias',
     'Should have (obligation not met, 2nd person) = deberías haber + pp.'),
    ('Podría ______ ganado el concurso, pero se rindió. (have)', 'haber',
     'Podría haber + participio = could have. The structure is podría + haber + participio.'),
    ('Debe ______ haber salido ya — no está en casa. (deduction particle)', 'de',
     'Past deduction = debe de haber + participio. The de is required for the deduction meaning.'),
    ('No ______ haber invertido todo el dinero en eso. (you should not have)', 'deberias',
     'No deberías haber + pp = you should not have (regret/criticism of past action).'),
    ('______ podido salir antes si no hubiera habido tanto tráfico. (I would have)', 'habria',
     'Habría podido + inf = could have. The condicional of haber: habría.'),
  ]),
  ex3=('Meaning check', 'Choose the sentence with the right meaning.', [
    ('Which expresses "she should have called"?', ['Debería haber llamado.', 'Debe de haber llamado.', 'Podría haber llamado.'], 'Debería haber llamado.',
     'Should have = debería haber + pp (unfulfilled obligation). Debe de = must have (deduction); podría = could have.'),
    ('Which expresses "he must have arrived already"?', ['Debe de haber llegado ya.', 'Debería haber llegado ya.', 'Podría haber llegado ya.'], 'Debe de haber llegado ya.',
     'Past deduction = debe de haber + pp. Debería haber = should have; podría haber = could have.'),
    ('Which expresses "they could have won"?', ['Podrían haber ganado.', 'Deberían haber ganado.', 'Deben de haber ganado.'], 'Podrían haber ganado.',
     'Could have = podrían haber + pp (unfulfilled possibility). Deberían = should have; deben de = must have.'),
    ('Which sentence has an error?', ['Debería de haber llegado. (obligation)', 'Podría haber llegado antes.', 'Debe de haber salido ya.'], 'Debería de haber llegado. (obligation)',
     'Deber + obligation: NO de. Debería haber (not debería DE haber). Deber de = deduction only.'),
    ('Which correctly places the object pronoun?', ['Podría haberlo hecho antes.', 'Podría haber lo hecho antes.', 'Podría haber hecho lo antes.'], 'Podría haberlo hecho antes.',
     'Object pronoun attaches to haber (haberlo) or the auxiliary (lo podría haber hecho) — never separated from haber with a space.'),
  ]),
  game_desc='Master modal perfects in Spanish: should have, could have, and must have. Reach 100 points to win.',
  items=[
    ('deberia-haber', 'debería haber', 'should have', 'obligation not fulfilled', '<b>Deberías haber</b> llegado antes.', '______ ______ llegado antes. (you should have)', 'deberia haber'),
    ('podria-haber', 'podría haber', 'could have', 'unfulfilled possibility', '<b>Podría haber</b> ganado, pero se rindió.', '______ ______ ganado, pero se rindió. (could have)', 'podria haber'),
    ('debe-de-haber', 'debe de haber', 'must have (deduction)', 'past logical deduction', '<b>Debe de haber</b> salido ya — no está en casa.', '______ ______ ______ salido ya. (must have)', 'debe de haber'),
    ('no-deberia', 'no debería haber', 'should not have', 'unfulfilled negative obligation', '<b>No deberías haber</b> dicho eso.', '______ ______ ______ dicho eso. (you should not have)', 'no deberia haber'),
    ('habria-podido', 'habría podido', 'could have (alt.)', 'unfulfilled possibility alternative', '<b>Habría podido</b> terminar antes con tu ayuda.', '______ ______ terminar antes con tu ayuda.', 'habria podido'),
    ('tiene-que-haber', 'tiene que haber', 'must have (colloquial deduction)', 'deduction colloquial', '<b>Tiene que haber</b> sido un error grave.', '______ ______ ______ sido un error grave. (must have been)', 'tiene que haber'),
    ('podria-haberlo', 'podría haberlo', 'could have it (object pronoun)', 'pronoun placement', '<b>Podría haberlo</b> hecho si me lo hubieran pedido.', '______ ______ hecho si me lo hubieran pedido. (could have it)', 'podria haberlo'),
    ('no-podria-haber', 'no podría haber', 'could not have', 'negative possibility', '<b>No podría haber</b> terminado sin tu ayuda.', '______ ______ ______ terminado sin tu ayuda. (could not have)', 'no podria haber'),
  ],
),

'nominalization': dict(
  num='G9', short='Nominalisation', title='Nominalisation — El que llegue primero gana',
  subtitle='Turning verbs and adjectives into noun phrases using el que, lo que, and -ción/-ment-',
  slides=[
    ('What is nominalisation?', None,
     '<p class="slide-explanation">Nominalisation converts a verb or adjective into a noun phrase — a key skill for C-level writing. In Spanish, the main tools are <b>el que / la que / los que / lo que</b> + verb, and suffixes like <b>-ción, -miento, -ura</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El que llegue primero</b> ganará. (Whoever arrives first / The one who arrives first will win.)</p>'
     '<p style="margin-top:8px"><b>Lo que me preocupa</b> es el precio. (What worries me is the price.)</p>'
     '<p style="margin-top:8px"><b>La formación</b> continua es clave. (Ongoing training is key.) — -ción suffix</p></div>'),
    ('El que / La que / Los que + verb', None,
     '<p class="slide-explanation">These noun phrases mean "the one who", "those who", "whoever".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El que quiera venir</b> es bienvenido. (Whoever wants to come is welcome.) — subjunctive: open invitation</p>'
     '<p style="margin-top:8px"><b>Los que llegaron tarde</b> se quedaron sin sitio. (Those who arrived late had no seat.) — indicative: specific people</p>'
     '<p style="margin-top:8px"><b>La que lleva el sombrero</b> es mi hermana. (The one wearing the hat is my sister.)</p></div>'),
    ('Lo que — what / the thing that', None,
     '<p class="slide-explanation"><b>Lo que</b> is a neuter nominaliser — it refers to an abstract idea, not a specific noun.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Lo que más me gusta</b> es su honestidad. (What I like most is her honesty.)</p>'
     '<p style="margin-top:8px"><b>Lo que dijiste</b> fue muy importante. (What you said was very important.)</p>'
     '<p style="margin-top:8px"><b>No entiendo lo que pides.</b> (I don\'t understand what you\'re asking.)</p></div>'),
    ('Verb-to-noun with suffixes', None,
     '<p class="slide-explanation">Many Spanish nouns derive from verbs using common suffixes. Recognising the pattern unlocks advanced vocabulary.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>-ción / -sión:</b> formar → la formación · decidir → la decisión · comunicar → la comunicación</p>'
     '<p style="margin-top:8px"><b>-miento:</b> desarrollar → el desarrollo · conocer → el conocimiento · sentir → el sentimiento</p>'
     '<p style="margin-top:8px"><b>-ura:</b> abrir → la apertura · cerrar → el cierre · calentar → el calentamiento</p></div>'),
    ('The infinitive as a noun', None,
     '<p class="slide-explanation">In Spanish, infinitives can act as nouns — especially as subjects.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El comer bien</b> es importante. (Eating well is important.)</p>'
     '<p style="margin-top:8px"><b>Viajar</b> amplía la mente. (Travelling broadens the mind.) — infinitive as subject</p>'
     '<p style="margin-top:8px"><b>El no saber</b> me angustia. (Not knowing worries me.) — negated infinitive</p></div>'),
  ],
  traps=[
    ('Lo que personas han llegado tarde, salgan.', '<strong>Los que</strong> han llegado tarde, que salgan.', 'Lo que refers to abstract ideas; los que (or las que) refers to people'),
    ('El que dice la verdad siempre gana.', 'El que dice la verdad siempre gana. — correct if referring to a specific person; <strong>el que diga</strong> la verdad… if open/general.', 'Indicative = specific identified person; subjunctive = open/general/whoever'),
    ('La comunicar bien es esencial.', '<strong>La comunicación</strong> bien es esencial. / Comunicar bien es esencial.', 'The nominalised noun is la comunicación (not la comunicar). Infinitives used as nouns usually have no article or take el'),
    ('El saber que no sé nada — Sócrates.', 'Correct: <strong>El saber</strong> que no sé nada. (Knowing that I know nothing.)', 'El + infinitive = the act of (doing) — a correct and common philosophical/formal construction'),
    ('Lo que tú lo dices es importante.', 'Lo que <strong>tú dices</strong> es importante.', 'Lo que + subject + verb: no double object pronoun. Lo que tú dices (not lo que tú lo dices)'),
  ],
  summary=[
    ('Whoever (subj.)', 'El/la que + subjunctive = whoever', 'El que llegue primero ganará.'),
    ('Those who (specific)', 'Los/las que + indicative = those who (specific)', 'Los que llegaron tarde perdieron el tren.'),
    ('What (abstract)', 'Lo que + verb = what (the thing that)', 'Lo que me preocupa es el coste.'),
    ('-ción / -sión', 'verb → formal noun', 'decidir → la decisión · formar → la formación'),
    ('-miento', 'verb → process noun', 'conocer → el conocimiento'),
    ('Infinitive as noun', 'el + infinitive = the act of', 'El viajar amplía la mente.'),
  ],
  ex1=('Choose the right nominaliser', 'Tap the best option for each gap.', [
    ('______ me gusta de tu ciudad es la tranquilidad.', ['Lo que', 'El que', 'Los que'], 'Lo que',
     'Lo que = what (abstract thing) — refers to the abstract quality that is liked. Not a person.'),
    ('______ quieran participar, que levanten la mano.', ['Los que', 'Lo que', 'El que'], 'Los que',
     'Los que + subjunctive (quieran) = whoever (plural) — an open, general invitation.'),
    ('No comprendo ______ me estás pidiendo.', ['lo que', 'el que', 'los que'], 'lo que',
     'I don\'t understand what you are asking = no comprendo lo que (abstract content of request).'),
    ('______ llegaron primero recibieron un premio.', ['Los que', 'Lo que', 'El que'], 'Los que',
     'Specific people who arrived first → los que + indicative (llegaron, past tense).'),
    ('______ más me sorprendió fue su respuesta.', ['Lo que', 'Los que', 'La que'], 'Lo que',
     'What surprised me most (abstract) = lo que. It refers to the abstract thing, not a person.'),
    ('La ______ de nuevos empleados ha aumentado este año. (decision)', ['decisión', 'decidición', 'decidimiento'], 'decisión',
     'Decidir → la decisión. The -ción suffix gives formal nouns from -ir verbs.'),
  ]),
  ex2=('Complete with the right nominaliser or noun form', 'Type the missing word — no accents needed.', [
    ('______ que no entiendan la explicación, que pregunten. (Those who — general)', 'los que',
     'Los que + subjunctive (entiendan) = whoever, those who — general open invitation.'),
    ('______ me pides es imposible. (What you are asking me)', 'lo que',
     'Lo que = what (the thing that) — abstract content of a request.'),
    ('Conocer el mundo lleva a mayor ______. (knowledge — noun from conocer)', 'conocimiento',
     'Conocer → el conocimiento (-miento suffix). Knowledge / understanding.'),
    ('El ______ bien es la base de la salud. (eating — infinitive as noun)', 'comer',
     'El comer bien = the act of eating well. Infinitive used as a noun with the article el.'),
    ('La ______ del nuevo acuerdo tomó semanas. (negotiation — noun from negociar)', 'negociacion',
     'Negociar → la negociación (-ción suffix). The negotiation / process of negotiating.'),
  ]),
  ex3=('Nominalisation choices', 'Choose the most natural option.', [
    ('Which correctly nominalises "those who study hard"?', ['Los que estudian mucho suelen tener éxito.', 'Lo que estudian mucho suelen tener éxito.', 'El que estudian mucho suelen tener éxito.'], 'Los que estudian mucho suelen tener éxito.',
     'Los que (plural, referring to people) + indicative (estudian, habitual truth) = those who study hard.'),
    ('Which correctly uses "what" for an abstract idea?', ['Lo que dices tiene mucho sentido.', 'El que dices tiene mucho sentido.', 'Los que dices tienen mucho sentido.'], 'Lo que dices tiene mucho sentido.',
     'Lo que = what (abstract content of what you say). Lo is the neuter article — no gender agreement.'),
    ('Which correctly nominalises the verb "desarrollar"?', ['el desarrollo', 'el desarrollamiento', 'la desarrollación'], 'el desarrollo',
     'Desarrollar → el desarrollo (irregular: the -llo root, not a regular suffix). Common exception.'),
    ('Which correctly uses an infinitive as a noun?', ['El viajar sola tiene sus ventajas.', 'La viajar sola tiene sus ventajas.', 'El viajando sola tiene sus ventajas.'], 'El viajar sola tiene sus ventajas.',
     'El + infinitive (viajar) = the act of travelling. Feminine article wrong; gerund wrong as noun.'),
    ('Which uses "whoever" with an open meaning?', ['El que quiera aprender, que estudie.', 'El que quiere aprender, que estudie.', 'Los que quieren aprender, que estudien.'], 'El que quiera aprender, que estudie.',
     'El que + subjunctive (quiera) = whoever wants to (open, general). Indicative (quiere) = a specific person.'),
  ]),
  game_desc='Master nominalisation in Spanish: el que / lo que, los que, and noun suffixes. Reach 100 points to win.',
  items=[
    ('lo-que-me-gusta', 'lo que me gusta', 'what I like', 'abstract nominaliser', '<b>Lo que me gusta</b> de este lugar es el silencio.', '______ ______ ______ ______ de este lugar es el silencio. (what I like)', 'lo que me gusta'),
    ('los-que', 'los que + subjunctive', 'whoever, those who (general)', 'open plural nominaliser', '<b>Los que</b> quieran participar, que avisen.', '______ ______ quieran participar, que avisen. (those who)', 'los que'),
    ('el-que-llegue', 'el que llegue', 'whoever arrives', 'open singular nominaliser', '<b>El que llegue</b> primero elige el sitio.', '______ ______ ______ primero elige el sitio. (whoever arrives)', 'el que llegue'),
    ('decision', 'la decisión', 'the decision (-ción)', '-ción nominalisation', 'Tomar una <b>decisión</b> a tiempo es fundamental.', 'Tomar una ______ a tiempo es fundamental. (decision)', 'decision'),
    ('conocimiento', 'el conocimiento', 'knowledge (-miento)', '-miento nominalisation', 'El <b>conocimiento</b> del idioma abre muchas puertas.', 'El ______ del idioma abre muchas puertas. (knowledge)', 'conocimiento'),
    ('el-viajar', 'el viajar', 'the act of travelling', 'infinitive as noun', '<b>El viajar</b> solo tiene sus ventajas e inconvenientes.', '______ ______ solo tiene sus ventajas. (travelling — noun)', 'el viajar'),
    ('lo-que-dijiste', 'lo que dijiste', 'what you said', 'abstract lo que', '<b>Lo que dijiste</b> ayer me hizo pensar mucho.', '______ ______ ______ ayer me hizo pensar mucho. (what you said)', 'lo que dijiste'),
    ('los-que-llegaron', 'los que llegaron', 'those who arrived (specific)', 'specific plural nominaliser', '<b>Los que llegaron</b> tarde tuvieron que esperar fuera.', '______ ______ ______ tarde tuvieron que esperar. (those who arrived)', 'los que llegaron'),
  ],
),

'participle-clauses': dict(
  num='G10', short='Participle Clauses', title='Participle Clauses — Terminada la reunión, salieron',
  subtitle='Reduced relative clauses and absolute constructions with past and present participles',
  slides=[
    ('The past participle as a reduced relative', None,
     '<p class="slide-explanation">A past participle can replace a full relative clause (que + verb) in formal and written Spanish, with the participle agreeing in gender and number.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Full:</b> Los documentos <b>que fueron firmados</b> ayer son válidos.</p>'
     '<p style="margin-top:8px"><b>Reduced:</b> Los documentos <b>firmados</b> ayer son válidos.</p>'
     '<p style="margin-top:8px"><b>Full:</b> La carta <b>que escribiste</b> llegó esta mañana.</p>'
     '<p style="margin-top:8px"><b>Reduced:</b> La carta <b>escrita por ti</b> llegó esta mañana.</p></div>'),
    ('Agreement of the past participle', None,
     '<p class="slide-explanation">When a past participle modifies a noun, it agrees in gender and number — like an adjective.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>el informe publicado</b> (masc. sing.) · <b>los informes publicados</b> (masc. pl.)</p>'
     '<p style="margin-top:8px"><b>la carta enviada</b> (fem. sing.) · <b>las cartas enviadas</b> (fem. pl.)</p>'
     '<p style="margin-top:8px">The participle acts as an adjective: always match the noun.</p></div>'),
    ('Absolute participle clauses', None,
     '<p class="slide-explanation">An <b>absolute</b> participle clause has its own (implied) subject and explains condition, cause, or time. It can come before or after the main clause.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Terminada la reunión, todos salieron.</b> (Once the meeting was over, everyone left.)</p>'
     '<p style="margin-top:8px"><b>Apagadas las luces, empezó la película.</b> (With the lights off, the film began.)</p>'
     '<p style="margin-top:8px"><b>Dicho esto, se marchó.</b> (Having said that, she left.) — fixed expression</p></div>'
     '<p style="margin-top:12px">The participle agrees with the noun that goes with it (la reunión → terminada).</p>'),
    ('Present participle (gerundio) as a reduced clause', None,
     '<p class="slide-explanation">The gerundio can replace a subordinate clause of manner, simultaneous action, or cause.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Simultaneous:</b> Entró silbando. (He came in whistling.) — manner</p>'
     '<p style="margin-top:8px"><b>Cause:</b> Siendo tan tarde, decidimos quedarnos. (Since it was so late, we decided to stay.)</p>'
     '<p style="margin-top:8px"><b>Condition:</b> Estudiando así, aprobarás. (If you study like that, you will pass.)</p></div>'),
    ('Participle clauses in formal writing', None,
     '<p class="slide-explanation">Both participle types appear frequently in journalistic, academic, and legal Spanish.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Una vez firmado el acuerdo, comenzarán las obras.</b> (Once the agreement is signed, works will begin.)</p>'
     '<p style="margin-top:8px"><b>Vistos los resultados, el director tomó medidas.</b> (Having seen the results, the director took action.)</p>'
     '<p style="margin-top:8px">Fixed: <b>Dicho esto · Hecho esto · Teniendo en cuenta que…</b></p></div>'),
  ],
  traps=[
    ('Terminado la reunión, salieron.', '<strong>Terminada</strong> la reunión, salieron.', 'The absolute participle agrees with the noun it belongs to: la reunión (f.) → terminada'),
    ('Los datos publicadas ayer son fiables.', 'Los datos <strong>publicados</strong> ayer son fiables.', 'Los datos (m.pl.) → publicados (m.pl.). The participle must agree with the noun.'),
    ('Siendo muy cansada, me fui a la cama.', 'Estando muy cansada, me fui a la cama. / <strong>Como estaba</strong> muy cansada, me fui.', 'Gerundio of ser (siendo) for a state is unusual — use estar: estando; or use the full clause: como estaba'),
    ('Llegando al aeropuerto, el vuelo ya había salido.', 'Al <strong>llegar</strong> al aeropuerto, el vuelo ya había salido.', 'Gerundio for a prior completed event is wrong — use al + infinitive: al llegar'),
    ('La carta escrita por ti ha llegado.', 'Correct! <strong>La carta escrita por ti</strong> = the letter written by you — the agent is introduced with por.', 'Past participle in reduced relative: agrees (carta→escrita), agent marked with por'),
  ],
  summary=[
    ('Reduced relative', 'Noun + past participle (agreeing)', 'los documentos firmados ayer'),
    ('Agent in reduced relative', 'past participle + por + agent', 'la carta escrita por ella'),
    ('Absolute clause', 'Past participle + noun (agreeing) + comma + main clause', 'Terminada la reunión, salieron.'),
    ('Fixed absolutes', 'Dicho esto · Hecho esto · Visto lo anterior', 'Dicho esto, se marchó.'),
    ('Gerundio: manner', 'Verb + gerundio = how the action was done', 'Entró silbando.'),
    ('Gerundio: cause', 'Gerundio clause + comma + main clause', 'Siendo tarde, decidimos quedarnos.'),
  ],
  ex1=('Choose the right participle form', 'Tap the correct option for each gap.', [
    ('Los contratos ______ ayer entrarán en vigor mañana.', ['firmados', 'firmadas', 'firmado'], 'firmados',
     'Los contratos (m.pl.) → firmados (m.pl.). The participle agrees with the noun it modifies.'),
    ('La propuesta ______ por el comité fue aprobada.', ['presentada', 'presentado', 'presentadas'], 'presentada',
     'La propuesta (f.sing.) → presentada (f.sing.). Feminine singular agreement.'),
    ('______ la reunión, todos se fueron a casa.', ['Terminada', 'Terminado', 'Terminadas'], 'Terminada',
     'La reunión (f.sing.) → terminada (f.sing.). The absolute participle agrees with its noun.'),
    ('______ esto, el ministro abandonó la sala.', ['Dicho', 'Dicha', 'Dichos'], 'Dicho',
     'Dicho esto is a fixed expression — esto (neuter) → dicho (neuter/masculine default form).'),
    ('Entró en la sala ______ una canción. (whistling)', ['silbando', 'silbado', 'silbar'], 'silbando',
     'Manner (how he entered) = gerundio: silbando (whistling). Not participle.'),
    ('______ tan tarde, decidimos quedarnos a dormir.', ['Siendo', 'Teniendo', 'Siendo que'], 'Siendo',
     'Cause with gerundio: Siendo tan tarde (since it was so late). Fixed causal gerundio construction.'),
  ]),
  ex2=('Complete the participle clause', 'Type the missing word — no accents needed.', [
    ('Las cartas ______ esta mañana llegarán mañana. (sent — f.pl.)', 'enviadas',
     'Las cartas (f.pl.) → enviadas (f.pl.). Past participle in reduced relative, feminine plural.'),
    ('______ la cena, los invitados salieron al jardín. (Once… was over — f.)', 'terminada',
     'La cena (f.sing.) → terminada. Absolute participle clause: Terminada la cena,…'),
    ('______ esto, no hay nada más que decir. (having said)', 'dicho',
     'Dicho esto = having said this / that said. Fixed expression, neuter/default form.'),
    ('Llegó ______ por teléfono. (talking)', 'hablando',
     'Manner gerundio: llegó hablando por teléfono = he arrived talking on the phone.'),
    ('Los informes ______ por el auditor muestran un déficit. (reviewed — m.pl.)', 'revisados',
     'Los informes (m.pl.) → revisados (m.pl.). Reduced relative with participle + por + agent.'),
  ]),
  ex3=('Participle clause analysis', 'Choose the best answer.', [
    ('Which correctly reduces "los problemas que han sido detectados"?', ['los problemas detectados', 'los problemas detectado', 'los problemas que detectados'], 'los problemas detectados',
     'Reduced relative: los problemas (m.pl.) + detectados (m.pl.). The que han sido is replaced by the agreeing participle.'),
    ('Which is a correct absolute participle clause?', ['Firmado el contrato, comenzará el proyecto.', 'Firmada el contrato, comenzará el proyecto.', 'Firmando el contrato, comenzará el proyecto.'], 'Firmado el contrato, comenzará el proyecto.',
     'El contrato (m.sing.) → firmado (m.sing.). The participle agrees with el contrato, then the main clause follows.'),
    ('Which gerundio clause expresses reason/cause?', ['Siendo ya las dos de la madrugada, decidimos salir.', 'Llegando a las dos de la madrugada, decidimos salir.', 'Habiendo llegado tarde, decidimos salir.'], 'Siendo ya las dos de la madrugada, decidimos salir.',
     'Being already 2 a.m. (since it was 2 a.m.) = causal gerundio. Siendo sets the circumstance.'),
    ('Which sentence correctly uses por to introduce the agent?', ['La novela escrita por García Márquez es un clásico.', 'La novela escrita de García Márquez es un clásico.', 'La novela que ha escrito García Márquez es clásico.'], 'La novela escrita por García Márquez es un clásico.',
     'Reduced relative + agent with por: la novela escrita por (written by) García Márquez.'),
    ('Which is NOT a correct use of the gerundio?', ['Llegando tarde, perdió el autobús.', 'Estudió escuchando música.', 'Habiéndolo terminado ayer, lo entregó hoy.'], 'Llegando tarde, perdió el autobús.',
     'Gerundio cannot express an action prior to and the direct cause of a completed event — use al llegar tarde or como llegó tarde. The other two are correct uses.'),
  ]),
  game_desc='Master participle clauses in Spanish: reduced relatives, absolute constructions, and gerundio clauses. Reach 100 points to win.',
  items=[
    ('firmados', 'firmados (m.pl.)', 'signed (agreeing participle)', 'reduced relative', 'Los contratos <b>firmados</b> ayer son válidos.', 'Los contratos ______ ayer son válidos. (signed, m.pl.)', 'firmados'),
    ('terminada', 'terminada (f.sing.)', 'over / finished — absolute', 'absolute participle clause', '<b>Terminada</b> la reunión, todos salieron.', '______ la reunión, todos salieron. (once finished, f.sing.)', 'terminada'),
    ('dicho-esto', 'dicho esto', 'having said that', 'fixed absolute', '<b>Dicho esto,</b> se marchó sin más explicaciones.', '______ ______ , se marchó sin más explicaciones. (having said that)', 'dicho esto'),
    ('escrita-por', 'escrita por', 'written by', 'reduced relative with agent', 'La carta <b>escrita por</b> ella llegó esta mañana.', 'La carta ______ ______ ella llegó esta mañana. (written by)', 'escrita por'),
    ('silbando', 'silbando', 'whistling', 'gerundio of manner', 'Entró en la sala <b>silbando</b> una canción.', 'Entró en la sala ______ una canción. (whistling)', 'silbando'),
    ('siendo-tarde', 'siendo tarde', 'since it was late', 'gerundio of cause', '<b>Siendo</b> ya muy tarde, decidimos no salir.', '______ ya muy tarde, decidimos no salir. (since it was late)', 'siendo tarde'),
    ('firmado-el-acuerdo', 'firmado el acuerdo', 'once the agreement is signed', 'absolute (m.)', 'Una vez <b>firmado el acuerdo</b>, empezarán las obras.', 'Una vez ______ ______ ______ , empezarán las obras.', 'firmado el acuerdo'),
    ('visto-esto', 'visto esto', 'having seen this', 'fixed absolute (formal)', '<b>Visto esto,</b> el director tomó medidas inmediatas.', '______ ______ , el director tomó medidas. (having seen this)', 'visto esto'),
  ],
),

}
