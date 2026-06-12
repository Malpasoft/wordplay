# -*- coding: utf-8 -*-
"""espanol-en B1 grammar content — batch 2 (chapters G6-G10)."""

CHAPTERS = {

'countable-uncountable': dict(
  num='G6', short='Quantifiers', title='Quantifiers — mucho, poco, demasiado',
  subtitle='Quantity words that agree (and the ones that refuse to)',
  slides=[
    ('Mucho agrees — much/many is one word', None,
     '<p class="slide-explanation">Where English splits much/many, Spanish has one word — <b>mucho</b> — that <b>agrees</b> with the noun in gender and number.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>mucho tiempo</b> (much time) · <b>mucha gente</b> (many people)</p>'
     '<p style="margin-top:8px"><b>muchos libros</b> (many books) · <b>muchas veces</b> (many times)</p></div>'
     '<p style="margin-top:16px">Four forms: mucho, mucha, muchos, muchas. The same goes for <b>poco</b> (little/few) and <b>demasiado</b> (too much/too many).</p>'),
    ('Poco and demasiado', None,
     '<p class="slide-explanation"><b>Poco</b> = little/few; <b>demasiado</b> = too much/too many. Both agree like mucho.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Tengo poco dinero y pocas vacaciones.</b> (I have little money and few holidays.)</p>'
     '<p style="margin-top:8px"><b>Hay demasiada gente y demasiados coches.</b> (There are too many people and too many cars.)</p></div>'
     '<p style="margin-top:16px">Note gente is singular feminine in Spanish — mucha gente, demasiada gente — even though English "people" is plural.</p>'),
    ('When they refuse to agree: adverbs', None,
     '<p class="slide-explanation">After a verb or before an adjective, mucho/poco/demasiado are <b>adverbs</b> — and adverbs never agree.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Ella trabaja mucho.</b> (She works a lot — never "mucha".)</p>'
     '<p style="margin-top:8px"><b>La sopa está demasiado caliente.</b> (The soup is too hot — demasiado + adjective, invariable.)</p></div>'
     '<p style="margin-top:16px">Test: is there a noun right after? Agree. Is it after a verb or before an adjective? Invariable.</p>'),
    ('Bastante and suficiente — enough', None,
     '<p class="slide-explanation"><b>Bastante</b> means "quite a lot / enough"; <b>suficiente</b> means strictly "sufficient". They only change for number (no gender forms).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hay bastantes sillas.</b> (There are enough/quite a few chairs.)</p>'
     '<p style="margin-top:8px"><b>No tenemos suficiente tiempo.</b> (We don\'t have enough time.)</p>'
     '<p style="margin-top:8px"><b>El examen fue bastante difícil.</b> (The exam was quite hard — adverb, invariable.)</p></div>'
     '<p style="margin-top:16px">Bastante before an adjective = "quite": bastante caro = quite expensive.</p>'),
    ('Algún and ningún — some and none', None,
     '<p class="slide-explanation"><b>Alguno</b> (some) and <b>ninguno</b> (none) drop the -o before a masculine singular noun: <b>algún, ningún</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Tienes algún problema?</b> (Do you have any problem?)</p>'
     '<p style="margin-top:8px"><b>No tengo ningún problema.</b> (I have no problem.)</p>'
     '<p style="margin-top:8px"><b>No queda ninguna entrada.</b> (There are no tickets left.)</p></div>'
     '<p style="margin-top:16px">Like the double negative with nunca: <b>No</b> tengo <b>ningún</b> problema — the two negatives are required, not wrong.</p>'),
  ],
  traps=[
    ('Hay mucho gente en la plaza.', 'Hay <strong>mucha</strong> gente en la plaza.', 'gente is feminine singular — mucha gente, even though English "people" feels plural'),
    ('Ella trabaja mucha.', 'Ella trabaja <strong>mucho</strong>.', 'After a verb, mucho is an adverb and never agrees'),
    ('La sopa está demasiada caliente.', 'La sopa está <strong>demasiado</strong> caliente.', 'Before an adjective, demasiado is an adverb — invariable'),
    ('¿Tienes alguno problema?', '¿Tienes <strong>algún</strong> problema?', 'alguno shortens to algún before a masculine singular noun'),
    ('No tengo ningunos amigos allí.', 'No tengo <strong>ningún</strong> amigo allí.', 'ninguno is almost always singular: ningún amigo, ninguna amiga'),
  ],
  summary=[
    ('Much / many', 'mucho/a/os/as + noun', 'mucha gente · muchos libros'),
    ('Little / few', 'poco/a/os/as + noun', 'poco dinero · pocas veces'),
    ('Too much / many', 'demasiado/a/os/as + noun', 'demasiada gente'),
    ('As adverbs', 'invariable after verbs / before adjectives', 'Trabaja mucho. · demasiado caliente'),
    ('Enough', 'bastante(s) · suficiente(s)', 'bastantes sillas · suficiente tiempo'),
    ('Some / none', 'algún / ningún + masc. sing.', 'algún problema · ningún amigo'),
  ],
  ex1=('Agree or not?', 'Noun → agree; verb or adjective → invariable.', [
    ('Hay ______ gente en el centro hoy.', ['mucha', 'mucho', 'muchas'], 'mucha',
     'gente = feminine singular → MUCHA gente.'),
    ('Mi hermana viaja ______.', ['mucho', 'mucha', 'muchos'], 'mucho',
     'After a verb → adverb, invariable: viaja MUCHO.'),
    ('Este café está ______ caliente.', ['demasiado', 'demasiada', 'demasiados'], 'demasiado',
     'Before an adjective → invariable: DEMASIADO caliente.'),
    ('Tenemos ______ tiempo — ¡corre!', ['poco', 'poca', 'pocos'], 'poco',
     'tiempo = masculine singular → POCO tiempo.'),
    ('¿Hay ______ pregunta antes de empezar?', ['alguna', 'algún', 'alguno'], 'alguna',
     'pregunta = feminine → ALGUNA pregunta.'),
    ('No queda ______ asiento libre.', ['ningún', 'ninguno', 'ninguna'], 'ningún',
     'Before masculine singular noun → NINGÚN asiento.'),
  ]),
  ex2=('Type the right form', 'mucho, poco, demasiado, bastante...', [
    ('There are too many cars. → Hay ______ coches. (demasiado)', 'demasiados',
     'coches = masculine plural → DEMASIADOS.'),
    ('She reads a lot. → Lee ______. (invariable!)', 'mucho',
     'After the verb → adverb MUCHO.'),
    ('many times → ______ veces', 'muchas',
     'veces = feminine plural → MUCHAS veces.'),
    ('I don\'t have any problem. → No tengo ______ problema.', 'ningún',
     'Masculine singular → NINGÚN problema.'),
    ('quite expensive → ______ caro', 'bastante',
     'Before an adjective → invariable BASTANTE caro.'),
  ]),
  ex3=('Find the correct sentence', 'Agreement is everything.', [
    ('Many people came:', ['Vino mucha gente.', 'Vinieron muchos gente.', 'Vino mucho gente.'], 'Vino mucha gente.',
     'gente: feminine singular — MUCHA gente (and singular verb).'),
    ('The film was quite good:', ['La película fue bastante buena.', 'La película fue bastanta buena.', 'La película fue bastantes buena.'], 'La película fue bastante buena.',
     'Bastante before adjective → invariable.'),
    ('We have too much homework:', ['Tenemos demasiados deberes.', 'Tenemos demasiado deberes.', 'Tenemos demasiadas deberes.'], 'Tenemos demasiados deberes.',
     'deberes = masculine plural → DEMASIADOS deberes.'),
    ('Do you have any questions? (plural feel, Spanish singular):', ['¿Tienes alguna pregunta?', '¿Tienes algún pregunta?', '¿Tienes alguno preguntas?'], '¿Tienes alguna pregunta?',
     'pregunta feminine → ALGUNA pregunta.'),
    ('He eats too much:', ['Come demasiado.', 'Come demasiados.', 'Come demasiada.'], 'Come demasiado.',
     'After the verb → invariable DEMASIADO.'),
  ]),
  game_desc='Each quantifier passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('mucha-gente', 'mucha gente', 'many people (gente = fem. singular!)', 'agreement', 'Hay <b>mucha</b> gente en la plaza.', 'Hay ______ gente en la plaza. (many)', 'mucha'),
    ('muchos', 'muchos/as', 'many (agrees in gender + number)', 'much/many', 'Tengo <b>muchos</b> libros.', 'Tengo ______ libros. (many)', 'muchos'),
    ('mucho-adv', 'trabaja mucho', 'a lot (adverb — invariable)', 'after verbs', 'Ella trabaja <b>mucho</b>.', 'Ella trabaja ______. (a lot)', 'mucho'),
    ('poco', 'poco/a/os/as', 'little / few', 'small quantity', 'Tengo <b>poco</b> tiempo.', 'Tengo ______ tiempo. (little)', 'poco'),
    ('demasiado', 'demasiado/a/os/as', 'too much / too many', 'excess', 'Hay <b>demasiada</b> gente.', 'Hay ______ gente. (too many)', 'demasiada'),
    ('demasiado-adv', 'demasiado + adjetivo', 'too (invariable before adjectives)', 'too + adj', 'La sopa está <b>demasiado</b> caliente.', 'La sopa está ______ caliente. (too)', 'demasiado'),
    ('algun', 'algún', 'some/any (short form before masc. sing.)', 'shortening', '¿Tienes <b>algún</b> problema?', '¿Tienes ______ problema? (any)', 'algún'),
    ('ningun', 'ningún', 'no / none (with double negative)', 'negation', 'No tengo <b>ningún</b> problema.', 'No tengo ______ problema. (no)', 'ningún'),
  ],
),

'future-continuous': dict(
  num='G7', short='Future Continuous', title='Future Continuous — Estaré trabajando',
  subtitle='What you will be doing — and the future that means "probably"',
  slides=[
    ('Estaré + gerundio', None,
     '<p class="slide-explanation">To say what you <b>will be doing</b> at a future moment, combine the future of estar with the gerund — a perfect mirror of English.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Mañana a esta hora estaré volando a Madrid.</b> (Tomorrow at this time I will be flying to Madrid.)</p>'
     '<p style="margin-top:8px"><b>No llames a las tres: estaremos comiendo.</b> (Don\'t call at three: we will be eating.)</p></div>'
     '<p style="margin-top:16px">Future of estar: estaré, estarás, estará, estaremos, estaréis, estarán + -ando/-iendo.</p>'),
    ('The simple future refresher', None,
     '<p class="slide-explanation">The simple future adds <b>-é, -ás, -á, -emos, -éis, -án</b> to the infinitive. The twelve irregular stems (tendr-, har-, dir-, podr-...) apply here too.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El año que viene viajaré más.</b> (Next year I will travel more.)</p>'
     '<p style="margin-top:8px"><b>Tendremos más tiempo en julio.</b> (We will have more time in July.)</p></div>'
     '<p style="margin-top:16px">Remember Spanish also loves <b>ir a + infinitive</b> for plans — the simple future sounds slightly more formal or distant.</p>'),
    ('The future of probability — Spanish\'s secret weapon', None,
     '<p class="slide-explanation">Here is a use English simply doesn\'t have: Spanish uses the <b>future tense to guess about the present</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Dónde estará Juan?</b> (I wonder where Juan is / Where can Juan be?)</p>'
     '<p style="margin-top:8px"><b>Serán las ocho.</b> (It must be about eight o\'clock.)</p>'
     '<p style="margin-top:8px"><b>Estará durmiendo.</b> (He is probably sleeping.)</p></div>'
     '<p style="margin-top:16px">No "probablemente" needed — the future tense alone carries the "probably". This is everywhere in conversation.</p>'),
    ('Guessing about actions in progress', None,
     '<p class="slide-explanation">Combine both ideas: <b>estará + gerundio</b> = "he is probably ...ing right now".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>—¿Por qué no contesta? —<b>Estará conduciendo.</b> (Why isn\'t she answering? — She\'s probably driving.)</p>'
     '<p style="margin-top:8px"><b>Los niños estarán jugando en el parque.</b> (The kids are probably playing in the park.)</p></div>'
     '<p style="margin-top:16px">Context tells you whether estará trabajando means "will be working" (tomorrow) or "is probably working" (right now).</p>'),
    ('Future time markers', None,
     '<p class="slide-explanation">Anchor your futures with the right markers.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>mañana a esta hora</b> · <b>el año que viene</b> (next year) · <b>la semana que viene</b></p>'
     '<p style="margin-top:8px"><b>dentro de dos horas</b> (in two hours) · <b>para entonces</b> (by then)</p>'
     '<p style="margin-top:8px"><b>El lunes que viene a las diez estaré haciendo el examen.</b></p></div>'
     '<p style="margin-top:16px">"Que viene" (literally "that comes") is the everyday way to say next: el mes que viene.</p>'),
  ],
  traps=[
    ('Mañana a las tres seré comiendo.', 'Mañana a las tres <strong>estaré comiendo</strong>.', 'Progressive forms always build on estar, never ser: estaré comiendo'),
    ('Probablemente es las ocho. (clunky)', '<strong>Serán las ocho.</strong>', 'Spanish guesses with the future tense — serán = it must be / probably is'),
    ('¿Dónde está Juan? No sé, quizás... (when guessing)', '¿Dónde <strong>estará</strong> Juan?', 'The wondering question uses the future: ¿dónde estará? = I wonder where he is'),
    ('Estaré volando en el avión a Madrid mañana en esta hora.', 'Mañana <strong>a esta hora</strong> estaré volando a Madrid.', '"At this time" = a esta hora — and time markers sit naturally at the start'),
    ('El próximo año tendreré más tiempo.', 'El año que viene <strong>tendré</strong> más tiempo.', 'tener has the irregular future stem tendr-: tendré'),
  ],
  summary=[
    ('Will be doing', 'estaré + gerundio', 'Estaré volando a Madrid.'),
    ('Simple future', 'infinitive + -é/-ás/-á...', 'Viajaré más el año que viene.'),
    ('Irregular stems', 'tendr- · har- · dir- · podr-', 'Tendremos más tiempo.'),
    ('Probability (present)', 'future = "probably"', 'Serán las ocho. · Estará durmiendo.'),
    ('Wondering', '¿dónde estará...?', '¿Dónde estará Juan?'),
    ('Markers', 'que viene · dentro de · para entonces', 'la semana que viene'),
  ],
  ex1=('Future forms', 'Will do, will be doing, or probably?', [
    ('Mañana a esta hora ______ por Italia. (nosotros, viajar — in progress)', ['estaremos viajando', 'viajamos', 'seremos viajando'], 'estaremos viajando',
     'Will be doing → ESTAR future + gerundio: estaremos viajando.'),
    ('—¿Qué hora es? —No sé, ______ las once. (ser — guess)', ['serán', 'son', 'sean'], 'serán',
     'Probability about now → future: SERÁN las once.'),
    ('—¿Dónde está Ana? —______ en la biblioteca. (estar — probably)', ['Estará', 'Está', 'Esté'], 'Estará',
     'Guess → ESTARÁ en la biblioteca = she\'s probably there.'),
    ('El año que viene ______ a verte. (yo, venir)', ['vendré', 'veniré', 'vengo a'], 'vendré',
     'Irregular stem vendr-: VENDRÉ.'),
    ('No llames a las dos — ______ comiendo. (nosotros)', ['estaremos', 'seremos', 'habremos'], 'estaremos',
     'Progressive → ESTAREMOS comiendo.'),
    ('¿Por qué no contesta? ______ conduciendo. (probably)', ['Estará', 'Estaba', 'Esté'], 'Estará',
     'Guess about an action now → ESTARÁ conduciendo.'),
  ]),
  ex2=('Build the future', 'Type the form.', [
    ('hacer, yo → Mañana ______ la maleta.', 'haré',
     'Irregular stem har-: HARÉ.'),
    ('estar + trabajar, ella → A las diez ______ trabajando.', 'estará',
     'Future of estar: ESTARÁ trabajando.'),
    ('tener, nosotros → ______ más tiempo en verano.', 'tendremos',
     'Irregular stem tendr-: TENDREMOS.'),
    ('ser — guess the time → ______ las nueve, más o menos.', 'serán',
     'Probability: SERÁN las nueve.'),
    ('poder, tú → ¿______ venir a la fiesta?', 'podrás',
     'Irregular stem podr-: PODRÁS.'),
  ]),
  ex3=('Will or probably?', 'Read the context, then choose.', [
    ('"She is probably sleeping" (it\'s 7 am):', ['Estará durmiendo.', 'Estará dormir.', 'Será durmiendo.'], 'Estará durmiendo.',
     'Probability now → estará + gerundio.'),
    ('"This time next week I\'ll be lying on the beach":', ['La semana que viene a esta hora estaré tumbado en la playa.', 'La semana que viene estoy tumbando en la playa.', 'La semana próxima seré tumbado en la playa.'], 'La semana que viene a esta hora estaré tumbado en la playa.',
     'Future moment → estaré + participle/gerund construction with estar.'),
    ('"I wonder who that man is":', ['¿Quién será ese hombre?', '¿Quién es siendo ese hombre?', '¿Quién sea ese hombre?'], '¿Quién será ese hombre?',
     'Wondering → future: ¿quién SERÁ?'),
    ('"It must be expensive":', ['Será caro.', 'Sea caro.', 'Estará siendo caro.'], 'Será caro.',
     'Guess about a quality → SERÁ caro.'),
    ('"We will have finished... no wait — we will be working at 6":', ['A las seis estaremos trabajando.', 'A las seis trabajaremos estando.', 'A las seis somos trabajando.'], 'A las seis estaremos trabajando.',
     'Action in progress at a future time → estaremos trabajando.'),
  ]),
  game_desc='Each future form passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('estare-trabajando', 'estaré trabajando', 'I will be working', 'future progressive', 'A las diez <b>estaré trabajando</b>.', 'A las diez estaré ______. (working)', 'trabajando'),
    ('viajare', 'viajaré', 'I will travel (simple future)', 'futuro simple', 'El año que viene <b>viajaré</b> más.', 'El año que viene ______ más. (I will travel)', 'viajaré'),
    ('tendre', 'tendré', 'I will have (irregular tendr-)', 'tener', '<b>Tendremos</b> más tiempo en julio.', '______ más tiempo en julio. (we will have)', 'tendremos'),
    ('seran-las-ocho', 'serán las ocho', 'it must be eight (probability!)', 'guessing', '<b>Serán</b> las ocho.', '______ las ocho. (it must be)', 'serán'),
    ('estara', 'estará durmiendo', 'he is probably sleeping', 'present guess', '<b>Estará</b> durmiendo.', '______ durmiendo. (he probably is)', 'estará'),
    ('donde-estara', '¿dónde estará...?', 'I wonder where ... is', 'wondering', '¿Dónde <b>estará</b> Juan?', '¿Dónde ______ Juan? (can he be)', 'estará'),
    ('que-viene', 'el año que viene', 'next year', 'time marker', 'Nos vemos <b>el año que viene</b>.', 'Nos vemos el año que ______. (next)', 'viene'),
    ('hare', 'haré', 'I will do/make (irregular har-)', 'hacer', 'Mañana <b>haré</b> la maleta.', 'Mañana ______ la maleta. (I will pack)', 'haré'),
  ],
),

'future-perfect': dict(
  num='G8', short='Future Perfect', title='Future Perfect — Habré terminado',
  subtitle='What will be done by then — and what has probably happened',
  slides=[
    ('Habré + participio', None,
     '<p class="slide-explanation">The <b>futuro perfecto</b> says what <b>will have happened</b> by a future deadline. Form: future of haber + past participle.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>habré · habrás · habrá · habremos · habréis · habrán</b> + participio</p>'
     '<p style="margin-top:8px"><b>Para el viernes habré terminado el informe.</b> (By Friday I will have finished the report.)</p></div>'
     '<p style="margin-top:16px">Same irregular participles as always: hecho, visto, dicho, escrito, puesto, vuelto...</p>'),
    ('Para — the deadline preposition', None,
     '<p class="slide-explanation">The futuro perfecto loves <b>para</b> + time: "by" a deadline.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Para junio habremos acabado el curso.</b> (By June we will have finished the course.)</p>'
     '<p style="margin-top:8px"><b>Para entonces ya habrán llegado.</b> (By then they will have already arrived.)</p></div>'
     '<p style="margin-top:16px">para el lunes = by Monday · para entonces = by then · para cuando vuelvas = by the time you return.</p>'),
    ('The past-probability superpower', None,
     '<p class="slide-explanation">Like the simple future, the futuro perfecto also guesses — about the <b>recent past</b>. "He must have..." = habrá + participio.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>—Luis no está. —<b>Habrá salido.</b> (Luis isn\'t here. — He must have gone out.)</p>'
     '<p style="margin-top:8px"><b>¿Dónde habré dejado las llaves?</b> (Where can I have left my keys?)</p></div>'
     '<p style="margin-top:16px">This is extremely common speech: se habrá olvidado (he must have forgotten), habrán perdido el tren (they must have missed the train).</p>'),
    ('Future perfect vs simple future', None,
     '<p class="slide-explanation">Choose by asking: finished BEFORE the future moment (perfecto) or happening AT it (simple/continuous)?</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>A las diez habré cenado.</b> (By ten I will have had dinner — done before.)</p>'
     '<p style="margin-top:8px"><b>A las diez estaré cenando.</b> (At ten I will be having dinner — in progress.)</p>'
     '<p style="margin-top:8px"><b>A las diez cenaré.</b> (At ten I will have dinner — starts then.)</p></div>'
     '<p style="margin-top:16px">Three futures, three relationships to the clock. Spanish is precise here — and examiners test it.</p>'),
    ('Putting it together', None,
     '<p class="slide-explanation">A typical B1 paragraph about future plans mixes all the future tools.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El año que viene terminaré el máster. Para septiembre habré encontrado trabajo, y dentro de cinco años estaré dirigiendo mi propio equipo.</b></p>'
     '<p style="margin-top:8px">(Next year I will finish my master\'s. By September I will have found a job, and in five years I will be leading my own team.)</p></div>'
     '<p style="margin-top:16px">terminaré (simple) → habré encontrado (perfect) → estaré dirigiendo (continuous). Use all three in your writing for top marks.</p>'),
  ],
  traps=[
    ('Para el viernes terminaré ya el informe. (deadline meaning)', 'Para el viernes <strong>habré terminado</strong> el informe.', 'Done BY a deadline → futuro perfecto: habré terminado'),
    ('Habré terminado para viernes.', 'Habré terminado <strong>para el viernes</strong>.', 'Days keep their article: para EL viernes'),
    ('Luis no está — debe que salir.', 'Luis no está — <strong>habrá salido</strong>.', 'The natural "he must have gone out" is the futuro perfecto: habrá salido'),
    ('Habré escribido la carta para entonces.', 'Habré <strong>escrito</strong> la carta para entonces.', 'escribir has the irregular participle escrito'),
    ('A las diez habré cenando.', 'A las diez habré <strong>cenado</strong>. / estaré <strong>cenando</strong>.', 'haber takes the participle (cenado); estar takes the gerund (cenando) — don\'t mix'),
  ],
  summary=[
    ('Form', 'habré/habrás... + participio', 'habré terminado'),
    ('Use', 'completed by a future moment', 'Para junio habremos acabado.'),
    ('Deadline', 'para + time = by', 'para el viernes · para entonces'),
    ('Past probability', 'habrá + participio = must have', 'Habrá salido.'),
    ('Wondering', '¿dónde habré...?', '¿Dónde habré dejado las llaves?'),
    ('Contrast', 'habré cenado vs estaré cenando vs cenaré', 'three futures, three timings'),
  ],
  ex1=('Future perfect or not?', 'Look for the deadline or the deduction.', [
    ('Para diciembre ______ de pagar el coche. (nosotros, acabar)', ['habremos acabado', 'acabaremos habiendo', 'estaremos acabado'], 'habremos acabado',
     'By December → futuro perfecto: HABREMOS ACABADO.'),
    ('No contesta al teléfono. Se ______ el móvil en casa. (dejar — deduction)', ['habrá dejado', 'dejará', 'deja'], 'habrá dejado',
     'Must have left → HABRÁ DEJADO.'),
    ('A las once ______ todavía. (ellos, bailar — in progress)', ['estarán bailando', 'habrán bailado', 'bailarán habiendo'], 'estarán bailando',
     'In progress at 11 → ESTARÁN BAILANDO.'),
    ('Para cuando llegues, ya ______ la cena. (yo, hacer)', ['habré hecho', 'haré hecho', 'habré hacido'], 'habré hecho',
     'Done by the time you arrive → HABRÉ HECHO (irregular participle).'),
    ('¿Dónde ______ puesto las gafas? (yo — wondering)', ['habré', 'habría', 'he'], 'habré',
     'Wondering about the recent past → ¿dónde HABRÉ puesto...?'),
    ('El tren llega a las seis; a las siete ya ______ a casa. (nosotros, volver)', ['habremos vuelto', 'volveremos habiendo', 'habremos volvido'], 'habremos vuelto',
     'Completed by seven → HABREMOS VUELTO (vuelto!).'),
  ]),
  ex2=('Build habré + participio', 'Watch the irregular participles.', [
    ('terminar, yo → Para el lunes ______ ______ el proyecto. (two words)', 'habré terminado',
     'HABRÉ TERMINADO para el lunes.'),
    ('ver, ellos → Para entonces ya ______ ______ la película. (two words)', 'habrán visto',
     'Ver → VISTO: habrán visto.'),
    ('salir, él — deduction → No está en casa: ______ ______. (two words)', 'habrá salido',
     'Must have gone out → HABRÁ SALIDO.'),
    ('escribir, ella → Para mayo ______ ______ la tesis. (two words)', 'habrá escrito',
     'Escribir → ESCRITO: habrá escrito.'),
    ('volver, nosotros → Para las diez ______ ______. (two words)', 'habremos vuelto',
     'Volver → VUELTO: habremos vuelto.'),
  ]),
  ex3=('Choose the right future', 'Simple, continuous or perfect?', [
    ('"By Friday I will have sent the email":', ['Para el viernes habré enviado el correo.', 'El viernes enviaré habiendo el correo.', 'Para el viernes estaré enviado el correo.'], 'Para el viernes habré enviado el correo.',
     'Completed by deadline → habré enviado.'),
    ('"They must have missed the bus":', ['Habrán perdido el autobús.', 'Perderán el autobús.', 'Habían perdiendo el autobús.'], 'Habrán perdido el autobús.',
     'Past deduction → habrán perdido.'),
    ('"At eight we will be watching the match":', ['A las ocho estaremos viendo el partido.', 'A las ocho habremos viendo el partido.', 'A las ocho veremos visto el partido.'], 'A las ocho estaremos viendo el partido.',
     'In progress → estaremos viendo.'),
    ('"She must have forgotten":', ['Se habrá olvidado.', 'Se olvidará.', 'Se habría olvidando.'], 'Se habrá olvidado.',
     'Must have forgotten → se habrá olvidado.'),
    ('"By then the film will have started":', ['Para entonces la película ya habrá empezado.', 'Para entonces la película empezará ya habiendo.', 'Para entonces la película está empezada será.'], 'Para entonces la película ya habrá empezado.',
     'Done by then → habrá empezado.'),
  ]),
  game_desc='Each futuro perfecto form passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('habre-terminado', 'habré terminado', 'I will have finished', 'futuro perfecto', 'Para el viernes <b>habré terminado</b>.', 'Para el viernes habré ______. (finished)', 'terminado'),
    ('habra-salido', 'habrá salido', 'he must have gone out (deduction)', 'past probability', 'Luis no está — <b>habrá salido</b>.', 'Luis no está — habrá ______. (gone out)', 'salido'),
    ('para-el-viernes', 'para + fecha', 'by (a deadline)', 'deadline', '<b>Para</b> junio habremos acabado.', '______ junio habremos acabado. (by)', 'para'),
    ('habran-llegado', 'habrán llegado', 'they will have arrived', 'plural form', 'Para entonces ya <b>habrán llegado</b>.', 'Para entonces ya ______ llegado. (they will have)', 'habrán'),
    ('habre-hecho', 'habré hecho', 'I will have done (irregular hecho)', 'hacer', 'Ya <b>habré hecho</b> la cena.', 'Ya habré ______ la cena. (made)', 'hecho'),
    ('habremos-vuelto', 'habremos vuelto', 'we will have returned (vuelto)', 'volver', 'A las diez <b>habremos vuelto</b>.', 'A las diez habremos ______. (returned)', 'vuelto'),
    ('donde-habre', '¿dónde habré...?', 'where can I have...? (wondering)', 'wondering', '¿Dónde <b>habré</b> dejado las llaves?', '¿Dónde ______ dejado las llaves? (can I have)', 'habré'),
    ('para-entonces', 'para entonces', 'by then', 'time marker', '<b>Para entonces</b> ya habrán llegado.', 'Para ______ ya habrán llegado. (then)', 'entonces'),
  ],
),

'imperatives': dict(
  num='G9', short='Imperatives', title='Imperatives — ¡Dímelo! ¡No me lo digas!',
  subtitle='Commands for tú, vosotros and usted — and where the pronouns go',
  slides=[
    ('Affirmative tú: the easy one', None,
     '<p class="slide-explanation">The affirmative tú command is just the <b>él/ella form</b> of the present: habla, come, escribe.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¡Habla más despacio!</b> (Speak more slowly!)</p>'
     '<p style="margin-top:8px"><b>¡Abre la ventana!</b> (Open the window!)</p></div>'
     '<p style="margin-top:16px">Eight irregulars to memorise: <b>pon</b> (poner), <b>ven</b> (venir), <b>haz</b> (hacer), <b>di</b> (decir), <b>sal</b> (salir), <b>ten</b> (tener), <b>ve</b> (ir), <b>sé</b> (ser).</p>'),
    ('Vosotros and usted', None,
     '<p class="slide-explanation">Vosotros commands swap the infinitive\'s -r for <b>-d</b>. Usted commands use the <b>subjunctive</b> form.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Vosotros: hablar → <b>¡Hablad!</b> · comer → <b>¡Comed!</b> · venir → <b>¡Venid!</b></p>'
     '<p style="margin-top:8px">Usted: <b>¡Hable!</b> · <b>¡Coma!</b> · <b>¡Venga!</b> (polite commands = subjunctive)</p></div>'
     '<p style="margin-top:16px">In a restaurant you\'ll hear usted commands constantly: pase (come in), siéntese (sit down), diga (hello? on the phone).</p>'),
    ('Negative commands: NO + subjunctive', None,
     '<p class="slide-explanation">ALL negative commands — tú included — use <b>no + present subjunctive</b>. The affirmative tú form disappears.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¡Habla!</b> → <b>¡No hables!</b> (Don\'t speak!)</p>'
     '<p style="margin-top:8px"><b>¡Ven!</b> → <b>¡No vengas!</b> (Don\'t come!)</p>'
     '<p style="margin-top:8px"><b>¡Hazlo!</b> → <b>¡No lo hagas!</b> (Don\'t do it!)</p></div>'
     '<p style="margin-top:16px">This is why the subjunctive (G18) matters so early — half of all commands need it.</p>'),
    ('Pronoun attachment: the dance', None,
     '<p class="slide-explanation">Pronouns <b>attach to the end</b> of affirmative commands but go <b>before</b> negative ones. Watch the accent appear to keep the stress.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¡Dímelo!</b> (Tell it to me!) — di + me + lo, accent added</p>'
     '<p style="margin-top:8px"><b>¡No me lo digas!</b> (Don\'t tell me!) — pronouns float free before the verb</p>'
     '<p style="margin-top:8px"><b>¡Levántate!</b> / <b>¡No te levantes!</b> (Get up! / Don\'t get up!)</p></div>'
     '<p style="margin-top:16px">Order stays me/te/se before lo/la: dímelo, dáselo — never "dilome".</p>'),
    ('Softening commands', None,
     '<p class="slide-explanation">Bare imperatives can sound brusque. Spanish softens with these tools:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Puedes cerrar la puerta?</b> (Can you close the door?)</p>'
     '<p style="margin-top:8px"><b>¿Me pasas la sal, por favor?</b> (Pass me the salt? — present as polite request)</p>'
     '<p style="margin-top:8px"><b>Cierra la puerta, anda.</b> (Close the door, go on — softener words: anda, venga, hombre)</p></div>'
     '<p style="margin-top:16px">Spaniards actually use imperatives more freely than English speakers — with por favor or a softener, they\'re perfectly polite.</p>'),
  ],
  traps=[
    ('¡No habla tan rápido!', '¡No <strong>hables</strong> tan rápido!', 'Negative commands need the subjunctive: no hables'),
    ('¡Dime lo!', '¡<strong>Dímelo</strong>!', 'Pronouns attach to affirmative commands as one word — with a written accent'),
    ('¡No dímelo!', '¡No <strong>me lo digas</strong>!', 'In negative commands the pronouns move BEFORE the verb: no me lo digas'),
    ('¡Pone la mesa!', '¡<strong>Pon</strong> la mesa!', 'poner has the irregular tú command pon'),
    ('¡Levanta te temprano!', '¡<strong>Levántate</strong> temprano!', 'Reflexive pronouns attach too: levántate (one word, accented)'),
  ],
  summary=[
    ('Tú +', 'él/ella form', '¡Habla! · ¡Come! · ¡Abre!'),
    ('Tú irregulars', 'pon · ven · haz · di · sal · ten · ve · sé', '¡Haz los deberes!'),
    ('Vosotros +', 'infinitive -r → -d', '¡Hablad! · ¡Venid!'),
    ('Usted', 'subjunctive form', '¡Pase! · ¡Siéntese!'),
    ('Negative', 'no + subjunctive (all persons)', '¡No hables! · ¡No vengas!'),
    ('Pronouns', 'attached after + / before no', '¡Dímelo! · ¡No me lo digas!'),
  ],
  ex1=('Give the command', 'Affirmative or negative, tú, vosotros or usted.', [
    ('(tú, hablar) ¡______ más alto, no te oigo!', ['Habla', 'Hables', 'Hablas'], 'Habla',
     'Affirmative tú = él/ella form: HABLA.'),
    ('(tú, no llegar) ¡______ tarde otra vez!', ['No llegues', 'No llega', 'No llegas'], 'No llegues',
     'Negative → no + subjunctive: NO LLEGUES.'),
    ('(tú, hacer) ¡______ los deberes ahora!', ['Haz', 'Hace', 'Haga'], 'Haz',
     'Irregular tú command: HAZ.'),
    ('(usted, pasar) ¡______, por favor!', ['Pase', 'Pasa', 'Pasad'], 'Pase',
     'Usted command = subjunctive: PASE.'),
    ('(vosotros, venir) ¡______ aquí ahora mismo!', ['Venid', 'Vened', 'Vengan'], 'Venid',
     'Vosotros: -r → -d: VENID.'),
    ('(tú, no preocuparse) ¡______!', ['No te preocupes', 'No preocúpate', 'No te preocupas'], 'No te preocupes',
     'Negative reflexive: pronoun before + subjunctive: no te PREOCUPES.'),
  ]),
  ex2=('Attach the pronouns', 'One word or pronouns first?', [
    ('Tell it to me! (decir + me + lo) → ¡______! (one word)', 'dímelo',
     'Affirmative → attached: DÍMELO (with accent).'),
    ('Don\'t tell it to me! → ¡No ______ ______ digas! (two pronouns)', 'me lo',
     'Negative → pronouns before: no ME LO digas.'),
    ('Get up! (levantarse, tú) → ¡______! (one word)', 'levántate',
     'Reflexive attached: LEVÁNTATE.'),
    ('Put it (la mesa... lo) on! → ¡Pon______! (attach lo)', 'lo',
     'PONLO — irregular pon + attached lo.'),
    ('Give it to him! (dar + se + lo) → ¡______! (one word)', 'dáselo',
     'DÁSELO — se before lo, accent added.'),
  ]),
  ex3=('Polite or brusque?', 'Choose the natural option.', [
    ('At the doctor\'s: "Sit down, please" (usted):', ['Siéntese, por favor.', 'Siéntate, por favor.', 'Sentaos, por favor.'], 'Siéntese, por favor.',
     'Usted reflexive command: SIÉNTESE.'),
    ('"Don\'t worry!" (tú):', ['¡No te preocupes!', '¡No preocúpate!', '¡No te preocupas!'], '¡No te preocupes!',
     'Negative → pronoun first + subjunctive: no te preocupes.'),
    ('"Come here!" (tú):', ['¡Ven aquí!', '¡Viene aquí!', '¡Venga tú aquí venid!'], '¡Ven aquí!',
     'Irregular tú command: VEN.'),
    ('Softened request for the salt:', ['¿Me pasas la sal, por favor?', '¡Pásame la sal ya!', '¡La sal!'], '¿Me pasas la sal, por favor?',
     'The present-as-request is the gentlest: ¿me pasas...?'),
    ('"Kids, eat your dinner!" (vosotros):', ['¡Comed la cena!', '¡Comer la cena!', '¡Coméis la cena!'], '¡Comed la cena!',
     'Vosotros command: -r → -d: COMED. (The infinitive is common in speech but wrong in exams.)'),
  ]),
  game_desc='Each command form passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('habla', '¡Habla!', 'speak! (tú = él/ella form)', 'affirmative tú', '¡<b>Habla</b> más despacio!', '¡______ más despacio! (speak)', 'habla'),
    ('haz', '¡Haz!', 'do/make! (irregular)', 'hacer → haz', '¡<b>Haz</b> los deberes!', '¡______ los deberes! (do)', 'haz'),
    ('no-hables', '¡No hables!', 'don\'t speak! (no + subjunctive)', 'negative', '¡<b>No hables</b> tan rápido!', '¡No ______ tan rápido! (speak — subjunctive)', 'hables'),
    ('dimelo', '¡Dímelo!', 'tell it to me! (pronouns attached)', 'attachment', '¡<b>Dímelo</b> ahora!', '¡______ ahora! (tell-me-it, one word)', 'dímelo'),
    ('no-me-lo-digas', '¡No me lo digas!', 'don\'t tell me! (pronouns first)', 'negative + pronouns', '¡<b>No me lo digas</b>!', '¡No me lo ______! (tell — subjunctive)', 'digas'),
    ('levantate', '¡Levántate!', 'get up! (reflexive attached)', 'reflexive', '¡<b>Levántate</b>, que es tarde!', '¡______, que es tarde! (get up)', 'levántate'),
    ('pase', '¡Pase!', 'come in! (usted = subjunctive)', 'usted', '¡<b>Pase</b>, por favor!', '¡______, por favor! (come in — usted)', 'pase'),
    ('hablad', '¡Hablad!', 'speak! (vosotros: -r → -d)', 'vosotros', '¡<b>Hablad</b> en español!', '¡______ en español! (speak — vosotros)', 'hablad'),
  ],
),

'indirect-speech': dict(
  num='G10', short='Indirect Speech', title='Indirect Speech — Dijo que...',
  subtitle='Reporting words: when dice stays put and dijo shifts everything back',
  slides=[
    ('Dice que — reporting with no shift', None,
     '<p class="slide-explanation">When the reporting verb is in the <b>present</b> (dice que...), nothing changes — just bolt the sentence on.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>«Estoy cansada.» → <b>Dice que está cansada.</b> (She says she is tired.)</p>'
     '<p style="margin-top:8px">«Vivo en Cádiz.» → <b>Dice que vive en Cádiz.</b></p></div>'
     '<p style="margin-top:16px">Only the person changes (estoy → está). Easy. The fun starts with dijo.</p>'),
    ('Dijo que — the backshift', None,
     '<p class="slide-explanation">With a past reporting verb (<b>dijo que</b>...), tenses shift one step back — just like English.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>presente → imperfecto: «Estoy cansada» → Dijo que <b>estaba</b> cansada.</p>'
     '<p style="margin-top:8px">indefinido → pluscuamperfecto: «Compré pan» → Dijo que <b>había comprado</b> pan.</p>'
     '<p style="margin-top:8px">futuro → condicional: «Iré mañana» → Dijo que <b>iría</b> al día siguiente.</p></div>'
     '<p style="margin-top:16px">Three conversions cover almost everything: estaba, había comprado, iría.</p>'),
    ('Reporting questions', None,
     '<p class="slide-explanation">Questions report with <b>preguntó</b>: wh-questions keep their question word; yes/no questions use <b>si</b> (if/whether).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>«¿Dónde vives?» → <b>Me preguntó dónde vivía.</b></p>'
     '<p style="margin-top:8px">«¿Tienes hambre?» → <b>Me preguntó si tenía hambre.</b></p></div>'
     '<p style="margin-top:16px">Word order goes back to normal (no inversion), and the accent stays on dónde, qué, cuándo in reported questions.</p>'),
    ('Time and place words shift too', None,
     '<p class="slide-explanation">When the moment of speaking moves, so do the pointers.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>hoy → ese día</b> · <b>ayer → el día anterior</b> · <b>mañana → al día siguiente</b></p>'
     '<p style="margin-top:8px"><b>aquí → allí</b> · <b>este → ese</b> · <b>ahora → entonces</b></p>'
     '<p style="margin-top:8px">«Te veo mañana aquí» → Dijo que me vería <b>al día siguiente allí</b>.</p></div>'
     '<p style="margin-top:16px">Same logic as English (today → that day) — the words just need learning.</p>'),
    ('Reporting commands: que + subjunctive', None,
     '<p class="slide-explanation">Commands report with <b>pedir/decir que + subjunctive</b> (imperfect subjunctive after a past verb — recognise it for now).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>«¡Ven pronto!» → <b>Me pidió que viniera pronto.</b> (She asked me to come early.)</p>'
     '<p style="margin-top:8px">«¡No llegues tarde!» → <b>Me dijo que no llegara tarde.</b></p></div>'
     '<p style="margin-top:16px">Pattern to recognise: pidió que + -ara/-iera forms. Production of these forms is a B2 goal — recognition is enough at B1.</p>'),
  ],
  traps=[
    ('Dijo que está cansada. (about yesterday)', 'Dijo que <strong>estaba</strong> cansada.', 'After dijo, the present shifts back to the imperfect: estaba'),
    ('Me preguntó que dónde vivo yo ahora.', 'Me preguntó dónde <strong>vivía</strong>.', 'Reported question: no que before dónde, and the tense shifts: vivía'),
    ('Me preguntó si tengo hambre. (yesterday)', 'Me preguntó si <strong>tenía</strong> hambre.', 'Yes/no questions report with si + backshifted tense'),
    ('Dijo que compró pan. (reporting «compré pan»)', 'Dijo que <strong>había comprado</strong> pan.', 'The indefinido steps back to the pluscuamperfecto: había comprado'),
    ('Dijo que vendrá mañana. (said yesterday)', 'Dijo que <strong>vendría al día siguiente</strong>.', 'Future → conditional, and mañana → al día siguiente'),
  ],
  summary=[
    ('No shift', 'dice que + same tense', 'Dice que está cansada.'),
    ('Present →', 'imperfecto', '«Estoy» → dijo que estaba'),
    ('Indefinido →', 'pluscuamperfecto', '«Compré» → dijo que había comprado'),
    ('Future →', 'condicional', '«Iré» → dijo que iría'),
    ('Questions', 'preguntó + dónde/si + backshift', 'Me preguntó si tenía hambre.'),
    ('Time words', 'hoy→ese día · mañana→al día siguiente', 'aquí→allí · ahora→entonces'),
  ],
  ex1=('Shift the tense', 'What did they say?', [
    ('«Estoy enfermo.» → Dijo que ______ enfermo.', ['estaba', 'está', 'estuvo'], 'estaba',
     'Present → imperfecto: ESTABA.'),
    ('«Compré las entradas.» → Dijo que ______ las entradas.', ['había comprado', 'compró', 'compraba'], 'había comprado',
     'Indefinido → pluscuamperfecto: HABÍA COMPRADO.'),
    ('«Llegaré a las ocho.» → Dijo que ______ a las ocho.', ['llegaría', 'llegará', 'llegaba'], 'llegaría',
     'Future → conditional: LLEGARÍA.'),
    ('«¿Dónde trabajas?» → Me preguntó dónde ______.', ['trabajaba', 'trabajo', 'trabajé'], 'trabajaba',
     'Reported question + backshift: TRABAJABA.'),
    ('«¿Tienes coche?» → Me preguntó ______ tenía coche.', ['si', 'que', 'cuándo'], 'si',
     'Yes/no question → SI tenía coche.'),
    ('«Te veo mañana.» → Dijo que me vería ______.', ['al día siguiente', 'mañana', 'ayer'], 'al día siguiente',
     'mañana shifts to AL DÍA SIGUIENTE.'),
  ]),
  ex2=('Report it', 'Type the shifted form.', [
    ('«Vivo en Málaga.» → Dijo que ______ en Málaga. (vivir)', 'vivía',
     'Present → imperfect: VIVÍA.'),
    ('«Vi la película.» → Dijo que ______ visto la película. (one word)', 'había',
     'Indefinido → pluscuamperfecto: HABÍA visto.'),
    ('«Iré al médico.» → Dijo que ______ al médico. (ir)', 'iría',
     'Future → conditional: IRÍA.'),
    ('«¿Estás bien?» → Me preguntó ______ estaba bien. (one word)', 'si',
     'Yes/no → SI estaba bien.'),
    ('«Hoy no puedo.» → Dijo que ______ día no podía. (two→one word: ese)', 'ese',
     'hoy → ESE día.'),
  ]),
  ex3=('Full report', 'Choose the correctly reported sentence.', [
    ('«Estoy muy contenta aquí» (said last week):', ['Dijo que estaba muy contenta allí.', 'Dijo que está muy contenta aquí.', 'Dijo que estuvo muy contenta aquí.'], 'Dijo que estaba muy contenta allí.',
     'estoy → estaba; aquí → allí.'),
    ('«¿Cuándo llega el tren?»:', ['Me preguntó cuándo llegaba el tren.', 'Me preguntó que cuándo llega el tren.', 'Me preguntó si cuándo llegaba el tren.'], 'Me preguntó cuándo llegaba el tren.',
     'Question word kept, tense shifted: cuándo llegaba.'),
    ('«Terminé el informe ayer»:', ['Dijo que había terminado el informe el día anterior.', 'Dijo que terminó el informe ayer.', 'Dijo que terminaba el informe ayer mismo.'], 'Dijo que había terminado el informe el día anterior.',
     'Indefinido → pluscuamperfecto; ayer → el día anterior.'),
    ('«¡Ven pronto!» (request):', ['Me pidió que viniera pronto.', 'Me pidió venir pronto que sí.', 'Me pidió que vengo pronto.'], 'Me pidió que viniera pronto.',
     'Reported command → pidió que + imperfect subjunctive: viniera.'),
    ('«Os llamaré mañana»:', ['Dijo que nos llamaría al día siguiente.', 'Dijo que os llamará mañana.', 'Dijo que nos llamaba mañana siguiente.'], 'Dijo que nos llamaría al día siguiente.',
     'Future → conditional (llamaría); mañana → al día siguiente; os → nos.'),
  ]),
  game_desc='Each reporting pattern passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('dice-que', 'dice que + presente', 'says that... (no shift)', 'present reporting', '<b>Dice que</b> está cansada.', '______ que está cansada. (she says)', 'dice'),
    ('estaba', 'presente → imperfecto', '"estoy" becomes estaba after dijo', 'backshift 1', 'Dijo que <b>estaba</b> cansada.', 'Dijo que ______ cansada. (she was)', 'estaba'),
    ('habia-comprado', 'indefinido → pluscuamperfecto', '"compré" becomes había comprado', 'backshift 2', 'Dijo que <b>había comprado</b> pan.', 'Dijo que ______ comprado pan. (had)', 'había'),
    ('iria', 'futuro → condicional', '"iré" becomes iría', 'backshift 3', 'Dijo que <b>iría</b> al día siguiente.', 'Dijo que ______ al día siguiente. (would go)', 'iría'),
    ('pregunto-si', 'preguntó si...', 'asked whether... (yes/no questions)', 'questions', 'Me preguntó <b>si</b> tenía hambre.', 'Me preguntó ______ tenía hambre. (whether)', 'si'),
    ('donde-vivia', 'preguntó dónde...', 'asked where... (wh-questions)', 'wh-questions', 'Me preguntó <b>dónde</b> vivía.', 'Me preguntó ______ vivía. (where)', 'dónde'),
    ('al-dia-siguiente', 'mañana → al día siguiente', 'tomorrow → the next day', 'time shift', 'Dijo que vendría <b>al día siguiente</b>.', 'Dijo que vendría al día ______. (next)', 'siguiente'),
    ('pidio-que', 'pidió que + subjuntivo', 'asked (someone) to... (commands)', 'reported commands', 'Me <b>pidió que</b> viniera pronto.', 'Me ______ que viniera pronto. (asked)', 'pidió'),
  ],
),

}
