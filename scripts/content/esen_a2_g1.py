# -*- coding: utf-8 -*-
"""espanol-en A2 grammar content — batch 1 (5 chapters)."""

CHAPTERS = {

'comparatives-basic': dict(
  num='G2', short='Comparatives', title='Comparatives — Comparativos',
  subtitle='Compare people and things: más que, menos que, tan como',
  slides=[
    ('Comparing in Spanish', None,
     '<p class="slide-explanation">To say something is <b>more ... than</b>, Spanish uses <b>más + adjective + que</b>. The adjective still agrees with the noun.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Madrid es más grande que Toledo.</b> (Madrid is bigger than Toledo.)</p>'
     '<p style="margin-top:8px"><b>Esta película es más interesante que el libro.</b> (This film is more interesting than the book.)</p></div>'
     '<p style="margin-top:16px">One pattern covers everything — Spanish never changes the adjective the way English does (big → bigger).</p>'),
    ('Less than — menos ... que', None,
     '<p class="slide-explanation">For <b>less ... than</b>, swap más for <b>menos</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El tren es menos caro que el avión.</b> (The train is less expensive than the plane.)</p>'
     '<p style="margin-top:8px"><b>Tengo menos tiempo que tú.</b> (I have less time than you.)</p></div>'
     '<p style="margin-top:16px">With nouns (tiempo, dinero, amigos) the same structure works: <b>más/menos + noun + que</b>.</p>'),
    ('As ... as — tan ... como', None,
     '<p class="slide-explanation">For equality use <b>tan + adjective + como</b>. With nouns, use <b>tanto/tanta/tantos/tantas + noun + como</b> — it agrees!</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Mi casa es tan bonita como la tuya.</b> (My house is as pretty as yours.)</p>'
     '<p style="margin-top:8px"><b>No tengo tanto dinero como él.</b> (I do not have as much money as him.)</p>'
     '<p style="margin-top:8px"><b>Hay tantas sillas como personas.</b> (There are as many chairs as people.)</p></div>'),
    ('The irregular four', None,
     '<p class="slide-explanation">Four adjectives have special comparative forms — never say "más bueno" for quality.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>bueno → mejor</b> (better): Este café es <b>mejor</b> que el otro.</p>'
     '<p style="margin-top:8px"><b>malo → peor</b> (worse): El tráfico hoy es <b>peor</b> que ayer.</p>'
     '<p style="margin-top:8px"><b>viejo → mayor</b> (older, for people): Mi hermano es <b>mayor</b> que yo.</p>'
     '<p style="margin-top:8px"><b>joven → menor</b> (younger): Ana es <b>menor</b> que Luis.</p></div>'
     '<p style="margin-top:16px">French-style "more good" does not exist in English — and "más bueno" sounds equally wrong in Spanish.</p>'),
    ('The best — superlatives', None,
     '<p class="slide-explanation">To say <b>the most ...</b>, add the article: <b>el/la/los/las + más + adjective</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Es la ciudad más bonita de España.</b> (It is the prettiest city in Spain.)</p>'
     '<p style="margin-top:8px"><b>Carlos es el mejor jugador del equipo.</b> (Carlos is the best player in the team.)</p></div>'
     '<p style="margin-top:16px">Note: after a superlative, English "in" becomes Spanish <b>de</b> — la más alta <b>de</b> la clase.</p>'),
  ],
  traps=[
    ('Madrid es más grande que Toledo? No — "more big"...', 'Madrid es <strong>más grande</strong> que Toledo.', 'Spanish always uses más + adjective — there is no -er ending'),
    ('Este libro es más bueno.', 'Este libro es <strong>mejor</strong>.', 'bueno and malo have irregular comparatives: mejor, peor'),
    ('Soy tan alto que mi padre.', 'Soy tan alto <strong>como</strong> mi padre.', 'Equality uses tan ... como, never tan ... que'),
    ('Tengo tan dinero como tú.', 'Tengo <strong>tanto</strong> dinero como tú.', 'Before a noun use tanto/tanta/tantos/tantas, not tan'),
    ('Es la chica más alta en la clase.', 'Es la chica más alta <strong>de</strong> la clase.', 'After a superlative, use de (not en) for "in"'),
  ],
  summary=[
    ('More than', 'más + adj + que', 'más grande que'),
    ('Less than', 'menos + adj + que', 'menos caro que'),
    ('As ... as', 'tan + adj + como', 'tan bonita como'),
    ('As much/many', 'tanto/a/os/as + noun + como', 'tanto dinero como'),
    ('Irregulars', 'mejor, peor, mayor, menor', 'Es mejor que el otro.'),
    ('Superlative', 'el/la más + adj + de', 'la más alta de la clase'),
  ],
  ex1=('Choose the correct comparative', 'Tap the best option for each sentence.', [
    ('Mi coche es ______ rápido que el tuyo.', ['más', 'tan', 'mucho'], 'más',
     'More ... than = más ... que. Tan needs como, and mucho alone cannot compare.'),
    ('Este restaurante es ______ que el otro. (better)', ['mejor', 'más bueno', 'más bien'], 'mejor',
     'Bueno has the irregular comparative mejor. "Más bueno" is not used for quality, and bien is an adverb.'),
    ('Luisa es tan simpática ______ su madre.', ['como', 'que', 'de'], 'como',
     'Equality is tan ... como. Que belongs with más/menos, and de marks superlatives.'),
    ('Tengo ______ libros como tú.', ['tantos', 'tan', 'tanto'], 'tantos',
     'Before a plural masculine noun (libros) use tantos. Tan goes with adjectives, tanto with singular nouns.'),
    ('Mi hermana es ______ que yo. (younger)', ['menor', 'más joven que', 'menos'], 'menor',
     'Joven has the irregular comparative menor. The option "más joven que" repeats que, and menos alone means less.'),
    ('El examen fue ______ difícil de lo que pensaba.', ['más', 'tan', 'como'], 'más',
     'More difficult than expected = más difícil. Tan and como express equality, not degree.'),
  ]),
  ex2=('Write the comparative', 'Type the missing word(s) — no accents needed in these answers.', [
    ('El avión es mas caro ______ el tren. (than)', 'que',
     'Comparisons with más/menos always close with que: más caro que el tren.'),
    ('Mi habitación es tan grande ______ la tuya. (as)', 'como',
     'Equality: tan + adjective + como. Never tan ... que.'),
    ('Este café es bueno, pero ese es ______. (better)', 'mejor',
     'Irregular comparative of bueno: mejor. No más needed — mejor already means "better".'),
    ('La película es mala, pero el libro es ______. (worse)', 'peor',
     'Irregular comparative of malo: peor — "worse" in one word.'),
    ('No tengo ______ amigos como ella. (as many)', 'tantos',
     'Amigos is masculine plural, so "as many" = tantos. It must agree with the noun.'),
  ]),
  ex3=('Usage and meaning', 'Choose the correct option.', [
    ('Which sentence is correct?', ['Pedro es mayor que Juan.', 'Pedro es más viejo que Juan.', 'Pedro es muy mayor que Juan.'], 'Pedro es mayor que Juan.',
     'For people, "older" is mayor. Más viejo is used for things, and muy cannot combine with que.'),
    ('"Es el restaurante más caro ______ la ciudad."', ['de', 'en', 'que'], 'de',
     'After a superlative, Spanish uses de where English says in: el más caro de la ciudad.'),
    ('How do you say "as much time as"?', ['tanto tiempo como', 'tan tiempo como', 'tanto tiempo que'], 'tanto tiempo como',
     'Tiempo is a singular masculine noun, so tanto tiempo como. Tan is only for adjectives/adverbs; the structure closes with como.'),
    ('Which means "My sister is less tall than me"?', ['Mi hermana es menos alta que yo.', 'Mi hermana es menor alta que yo.', 'Mi hermana es menos alta como yo.'], 'Mi hermana es menos alta que yo.',
     'Less + adjective = menos alta, closed by que. Menor is only the irregular for age, and como belongs to equality.'),
    ('"Hoy hace ______ calor que ayer." (more)', ['más', 'tan', 'tanto'], 'más',
     'More heat than yesterday: más calor que ayer. Tan/tanto would need como and express equality.'),
  ]),
  game_desc='Each comparative structure passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('mas-que', 'más ... que', 'more ... than - the basic comparative', 'comparing upward', 'Madrid es <b>más grande que</b> Toledo.', 'Madrid es ______ grande ______ Toledo.', 'mas que'),
    ('menos-que', 'menos ... que', 'less ... than', 'comparing downward', 'El tren es <b>menos caro que</b> el avión.', 'El tren es ______ caro que el avión.', 'menos'),
    ('tan-como', 'tan ... como', 'as ... as - equality with adjectives', 'equality structure', 'Soy <b>tan alto como</b> mi padre.', 'Soy tan alto ______ mi padre.', 'como'),
    ('tanto-como', 'tanto ... como', 'as much ... as - equality with nouns, agrees with the noun', 'equality with nouns', 'No tengo <b>tanto dinero como</b> él.', 'No tengo ______ dinero como él.', 'tanto'),
    ('mejor', 'mejor', 'better - irregular comparative of bueno', 'irregular of bueno', 'Este café es <b>mejor</b> que el otro.', 'Este café es ______ que el otro.', 'mejor'),
    ('peor', 'peor', 'worse - irregular comparative of malo', 'irregular of malo', 'El tráfico hoy es <b>peor</b> que ayer.', 'El tráfico hoy es ______ que ayer.', 'peor'),
    ('mayor', 'mayor', 'older - irregular comparative for people', 'older (people)', 'Mi hermano es <b>mayor</b> que yo.', 'Mi hermano es ______ que yo.', 'mayor'),
    ('el-mas-de', 'el más ... de', 'the most ... in - superlative, uses de not en', 'superlative structure', 'Es la ciudad <b>más bonita de</b> España.', 'Es la ciudad más bonita ______ España.', 'de'),
  ],
),

'modal-must-should': dict(
  num='G9', short='Obligation & Advice', title='Obligation &amp; Advice — Tener que, Deber, Hay que',
  subtitle='Say what you must, need to and should do',
  slides=[
    ('Three ways to say "must"', None,
     '<p class="slide-explanation">Spanish has three everyday structures for obligation. All are followed by an <b>infinitive</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Tengo que estudiar.</b> (I have to study.) — personal, most common</p>'
     '<p style="margin-top:8px"><b>Debo estudiar.</b> (I must study.) — stronger, more formal</p>'
     '<p style="margin-top:8px"><b>Hay que estudiar.</b> (One must study.) — impersonal, general rules</p></div>'),
    ('Tener que + infinitive', None,
     '<p class="slide-explanation"><b>Tener que</b> conjugates tener normally and adds que + infinitive. It is the everyday "have to".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Tengo que trabajar mañana.</b> (I have to work tomorrow.)</p>'
     '<p style="margin-top:8px"><b>Tienes que ver esta película.</b> (You have to see this film.)</p>'
     '<p style="margin-top:8px"><b>Tenemos que salir a las ocho.</b> (We have to leave at eight.)</p></div>'
     '<p style="margin-top:16px">Never drop the <b>que</b>: tengo que ir, not "tengo ir".</p>'),
    ('Deber + infinitive', None,
     '<p class="slide-explanation"><b>Deber</b> goes straight to the infinitive — no que. It sounds like a duty or strong recommendation.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Debes descansar más.</b> (You must rest more.)</p>'
     '<p style="margin-top:8px"><b>Los alumnos deben llegar puntuales.</b> (Pupils must arrive on time.)</p></div>'
     '<p style="margin-top:16px">For advice — English "should" — use the conditional: <b>deberías</b>. <b>Deberías dormir más.</b> (You should sleep more.)</p>'),
    ('Hay que — impersonal', None,
     '<p class="slide-explanation"><b>Hay que + infinitive</b> states a general obligation with no particular subject — like English "you have to / one must".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hay que reservar con antelación.</b> (You have to book in advance.)</p>'
     '<p style="margin-top:8px"><b>En España hay que cenar tarde.</b> (In Spain one has to dine late.)</p></div>'
     '<p style="margin-top:16px">It never changes form — hay que works for everyone in general.</p>'),
    ('No tener que = no need', None,
     '<p class="slide-explanation">Careful with negatives: <b>no tengo que</b> means "I do not have to" (no obligation), while <b>no debes</b> means "you must not" (prohibition-ish advice).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>No tienes que venir.</b> (You do not have to come — optional.)</p>'
     '<p style="margin-top:8px"><b>No debes fumar aquí.</b> (You must not smoke here.)</p></div>'),
  ],
  traps=[
    ('Tengo ir al médico.', 'Tengo <strong>que</strong> ir al médico.', 'Tener que always keeps que before the infinitive'),
    ('Debo que estudiar.', '<strong>Debo estudiar.</strong>', 'Deber takes the infinitive directly — no que'),
    ('Hay que tú estudias.', 'Hay que <strong>estudiar</strong>.', 'Hay que is impersonal and is always followed by an infinitive'),
    ('Tú deberías a dormir más.', 'Deberías <strong>dormir</strong> más.', 'No preposition before the infinitive after deberías'),
    ('No debo ir = I don\'t have to go?', '<strong>No tengo que ir</strong> = I don\'t have to go.', 'No deber sounds like "must not"; for absence of obligation use no tener que'),
  ],
  summary=[
    ('Have to', 'tener que + inf', 'Tengo que trabajar.'),
    ('Must', 'deber + inf', 'Debes descansar.'),
    ('Should', 'debería + inf', 'Deberías dormir más.'),
    ('One must', 'hay que + inf', 'Hay que reservar.'),
    ("Don't have to", 'no tener que + inf', 'No tienes que venir.'),
  ],
  ex1=('Choose the correct form', 'Tap the best option for each sentence.', [
    ('Mañana yo ______ que madrugar.', ['tengo', 'debo', 'hay'], 'tengo',
     'With que after it, the verb must be tener: tengo que madrugar. Debo never takes que, and hay que has no personal subject.'),
    ('______ que llevar pasaporte para viajar.', ['Hay', 'Tiene', 'Debe'], 'Hay',
     'A general rule with no subject = hay que. Tiene/debe would need a person as subject.'),
    ('Estás cansado. ______ descansar.', ['Deberías', 'Tienes', 'Hay que'], 'Deberías',
     'Advice ("you should") = deberías + infinitive. Tienes would need que, and hay que is impersonal.'),
    ('Los estudiantes ______ llegar puntuales.', ['deben', 'tienen', 'hay que'], 'deben',
     'Deber + infinitive directly: deben llegar. Tienen would need que; hay que cannot follow a subject.'),
    ('No ______ que pagar — es gratis.', ['tienes', 'debes', 'deberías'], 'tienes',
     'Absence of obligation = no tener que: no tienes que pagar. No debes would mean "you must not".'),
    ('______ que cenar tarde en España.', ['Hay', 'Tengo', 'Debes'], 'Hay',
     'A general cultural rule: hay que cenar tarde. The others would make it personal.'),
  ]),
  ex2=('Complete the obligation', 'Type the missing word — no accents needed.', [
    ('Tengo ______ estudiar esta noche. (have to)', 'que',
     'Tener que + infinitive: the que is obligatory — tengo que estudiar.'),
    ('______ que reciclar el plástico. (one must)', 'hay',
     'Impersonal obligation: hay que reciclar. Hay never changes form.'),
    ('Ella ______ ahorrar más dinero. (must, from deber)', 'debe',
     'Deber conjugated for ella is debe, followed directly by the infinitive.'),
    ('Nosotros tenemos ______ limpiar la casa. (have to)', 'que',
     'Whatever the form of tener, the que stays: tenemos que limpiar.'),
    ('No tienes ______ venir si no quieres. (do not have to)', 'que',
     'No tener que = no obligation, and the que still appears: no tienes que venir.'),
  ]),
  ex3=('Meaning check', 'Choose the correct option.', [
    ('"No tienes que pagar" means...', ["You don't have to pay.", 'You must not pay.', 'You should pay.'], "You don't have to pay.",
     'No tener que removes the obligation. Prohibition would be no debes pagar.'),
    ('Which is the impersonal structure?', ['hay que', 'tener que', 'deber'], 'hay que',
     'Hay que has no subject — it states what one must do in general.'),
    ('Which sentence gives advice?', ['Deberías comer mejor.', 'Tienes que comer.', 'Hay que comer.'], 'Deberías comer mejor.',
     'The conditional deberías softens deber into advice — English "you should".'),
    ('Complete: "Para aprobar, ______ estudiar cada día."', ['hay que', 'tengo', 'debes que'], 'hay que',
     'A general recipe for passing: hay que estudiar. Tengo lacks que; "debes que" is never correct.'),
    ('Which is WRONG?', ['Debo que trabajar.', 'Tengo que trabajar.', 'Hay que trabajar.'], 'Debo que trabajar.',
     'Deber never takes que. The correct form is debo trabajar.'),
  ]),
  game_desc='Each obligation structure passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('tengo-que', 'tengo que', 'I have to - everyday personal obligation', 'tener que, yo form', '<b>Tengo que</b> estudiar esta noche.', '______ ______ estudiar esta noche. (I have to)', 'tengo que'),
    ('tienes-que', 'tienes que', 'you have to - tener que for tu', 'tener que, tu form', '<b>Tienes que</b> ver esta película.', '______ que ver esta película. (you)', 'tienes'),
    ('hay-que', 'hay que', 'one must - impersonal general obligation', 'impersonal obligation', '<b>Hay que</b> reservar con antelación.', '______ ______ reservar con antelación.', 'hay que'),
    ('debo', 'debo', 'I must - stronger or more formal duty', 'deber, yo form', '<b>Debo</b> terminar el informe hoy.', '______ terminar el informe hoy. (I must)', 'debo'),
    ('deberias', 'deberías', 'you should - advice with the conditional of deber', 'advice form', '<b>Deberías</b> dormir más.', '______ dormir más. (you should)', 'deberias'),
    ('no-tengo-que', 'no tengo que', 'I do not have to - absence of obligation', 'no obligation', '<b>No tengo que</b> trabajar mañana.', 'No ______ que trabajar mañana.', 'tengo'),
    ('debemos', 'debemos', 'we must - deber for nosotros', 'deber, nosotros form', '<b>Debemos</b> llegar puntuales.', '______ llegar puntuales. (we must)', 'debemos'),
    ('tenemos-que', 'tenemos que', 'we have to - tener que for nosotros', 'tener que, nosotros form', '<b>Tenemos que</b> salir a las ocho.', '______ que salir a las ocho. (we)', 'tenemos'),
  ],
),

'modal-could-might': dict(
  num='G8', short='Possibility', title='Possibility — Poder, Quizás, A lo mejor',
  subtitle='Say what could or might happen',
  slides=[
    ('Could — poder in the conditional', None,
     '<p class="slide-explanation">To say something <b>could</b> happen, use <b>podría</b> (conditional of poder) + infinitive.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Podríamos ir al cine.</b> (We could go to the cinema.)</p>'
     '<p style="margin-top:8px"><b>¿Podrías ayudarme?</b> (Could you help me?) — polite request</p></div>'
     '<p style="margin-top:16px">Forms: podría, podrías, podría, podríamos, podríais, podrían.</p>'),
    ('Puede — maybe it happens', None,
     '<p class="slide-explanation"><b>Puede</b> (present of poder) + infinitive expresses ability or real possibility.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Puede llover esta tarde.</b> (It may rain this afternoon.)</p>'
     '<p style="margin-top:8px"><b>Puedo llegar a las seis.</b> (I can arrive at six.)</p></div>'),
    ('Quizás / Tal vez — perhaps', None,
     '<p class="slide-explanation"><b>Quizás</b> and <b>tal vez</b> both mean "perhaps / maybe". At A2, use them with the normal indicative.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Quizás voy mañana.</b> (Maybe I will go tomorrow.)</p>'
     '<p style="margin-top:8px"><b>Tal vez está en casa.</b> (Perhaps he is at home.)</p></div>'
     '<p style="margin-top:16px">You will later meet these with the subjunctive (quizás vaya) — both are heard in Spain.</p>'),
    ('A lo mejor — the everyday "maybe"', None,
     '<p class="slide-explanation"><b>A lo mejor</b> is the most colloquial option — and good news: it always takes the plain indicative.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>A lo mejor vamos a la playa.</b> (Maybe we will go to the beach.)</p>'
     '<p style="margin-top:8px"><b>A lo mejor es verdad.</b> (Maybe it is true.)</p></div>'),
    ('Es posible que — a first taste', None,
     '<p class="slide-explanation">You will also hear <b>es posible que</b> + subjunctive. Recognise it at A2; you do not need to produce it yet.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Es posible que llueva.</b> (It is possible that it will rain.)</p></div>'),
  ],
  traps=[
    ('Podría a venir mañana.', 'Podría <strong>venir</strong> mañana.', 'No preposition between podría and the infinitive'),
    ('Puedo que llegar tarde.', '<strong>Puedo llegar</strong> tarde.', 'Poder never takes que — straight to the infinitive'),
    ('A lo mejor que viene.', '<strong>A lo mejor viene.</strong>', 'A lo mejor takes no que — just add the normal verb'),
    ('Quizás to rain tomorrow...', 'Quizás <strong>llueve</strong> mañana.', 'Quizás needs a conjugated verb, not an infinitive'),
  ],
  summary=[
    ('Could', 'podría + inf', 'Podríamos ir al cine.'),
    ('Polite request', '¿Podrías + inf?', '¿Podrías ayudarme?'),
    ('May / can', 'puede + inf', 'Puede llover esta tarde.'),
    ('Perhaps', 'quizás / tal vez + verb', 'Quizás voy mañana.'),
    ('Maybe (colloquial)', 'a lo mejor + indicative', 'A lo mejor vamos a la playa.'),
  ],
  ex1=('Choose the correct option', 'Tap the best option for each sentence.', [
    ('______ ir al cine esta noche. (we could)', ['Podríamos', 'Podemos que', 'Podríamos a'], 'Podríamos',
     'Conditional of poder + infinitive directly: podríamos ir. No que, no a.'),
    ('¿______ ayudarme con esto? (could you, polite)', ['Podrías', 'Puedes que', 'Podría yo'], 'Podrías',
     'Polite request to tú: ¿Podrías ayudarme? Poder never takes que.'),
    ('______ llueve mañana. (perhaps)', ['Quizás', 'Podría', 'Puede'], 'Quizás',
     'Perhaps + normal verb: quizás llueve. Podría/puede would need an infinitive after them.'),
    ('A lo mejor ______ a la playa el domingo.', ['vamos', 'ir', 'vayamos'], 'vamos',
     'A lo mejor always takes the plain indicative: a lo mejor vamos. Never an infinitive.'),
    ('______ llover esta tarde — lleva paraguas.', ['Puede', 'Quizás', 'A lo mejor'], 'Puede',
     'Followed directly by the infinitive llover, only puede works: puede llover.'),
    ('Es posible que ______ tarde. (a first taste of subjunctive)', ['llegue', 'llega', 'llegar'], 'llegue',
     'Es posible que triggers the subjunctive: llegue. You only need to recognise this at A2.'),
  ]),
  ex2=('Complete the sentence', 'Type the missing word — no accents needed in these answers.', [
    ('¿Podrias ______ la ventana, por favor? (close → cerrar)', 'cerrar',
     'After podrías comes the infinitive unchanged: cerrar la ventana.'),
    ('A lo ______ viene Juan esta tarde. (maybe)', 'mejor',
     'The fixed phrase is a lo mejor — literally "at the best", meaning maybe.'),
    ('Tal ______ está en casa. (perhaps)', 'vez',
     'Tal vez = perhaps. Like quizás, it can take the normal indicative at A2.'),
    ('Nosotros ______ ir en tren o en coche. (could → podriamos)', 'podriamos',
     'Conditional nosotros form: podríamos (accepted here without the accent).'),
    ('Puede ______ esta noche. (rain → llover)', 'llover',
     'Puede + infinitive: puede llover — it may rain.'),
  ]),
  ex3=('Meaning check', 'Choose the correct option.', [
    ('"¿Podrías abrir la ventana?" is...', ['a polite request', 'an obligation', 'a prohibition'], 'a polite request',
     'The conditional podrías softens the question — exactly like English "could you...?".'),
    ('Which expression NEVER takes the subjunctive?', ['a lo mejor', 'es posible que', 'quizás'], 'a lo mejor',
     'A lo mejor always uses the indicative. Es posible que requires subjunctive; quizás can take either.'),
    ('"Puede llover" means...', ['It may rain.', 'It must rain.', 'It rained.'], 'It may rain.',
     'Puede + infinitive expresses possibility: it may/can rain.'),
    ('Which is WRONG?', ['Podría que venir.', 'Podría venir.', 'A lo mejor viene.'], 'Podría que venir.',
     'Poder never takes que before the infinitive — podría venir is the correct form.'),
    ('The most colloquial "maybe" is...', ['a lo mejor', 'tal vez', 'es posible que'], 'a lo mejor',
     'A lo mejor is the everyday spoken option; tal vez and es posible que are more formal.'),
  ]),
  game_desc='Each possibility structure passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('podria', 'podría', 'could - conditional of poder for I or he/she', 'conditional of poder', '<b>Podría</b> venir mañana.', '______ venir mañana. (could)', 'podria'),
    ('podrias', 'podrías', 'could you - polite request form', 'polite request', '¿<b>Podrías</b> ayudarme?', '¿______ ayudarme? (could you)', 'podrias'),
    ('podriamos', 'podríamos', 'we could - conditional of poder for nosotros', 'we could', '<b>Podríamos</b> ir al cine.', '______ ir al cine. (we could)', 'podriamos'),
    ('puede', 'puede', 'may or can - present of poder plus infinitive', 'real possibility', '<b>Puede</b> llover esta tarde.', '______ llover esta tarde.', 'puede'),
    ('quizas', 'quizás', 'perhaps - with a normal indicative verb at A2', 'perhaps', '<b>Quizás</b> voy mañana.', '______ voy mañana. (perhaps)', 'quizas'),
    ('tal-vez', 'tal vez', 'perhaps - synonym of quizas', 'synonym of quizas', '<b>Tal vez</b> está en casa.', '______ ______ está en casa.', 'tal vez'),
    ('a-lo-mejor', 'a lo mejor', 'maybe - colloquial, always indicative', 'colloquial maybe', '<b>A lo mejor</b> vamos a la playa.', 'A lo ______ vamos a la playa.', 'mejor'),
    ('es-posible-que', 'es posible que', 'it is possible that - triggers subjunctive, recognise only', 'possibility + subjunctive', '<b>Es posible que</b> llueva.', 'Es ______ que llueva.', 'posible'),
  ],
),

'object-pronouns': dict(
  num='G10', short='Object Pronouns', title='Object Pronouns — Lo, La, Le',
  subtitle='Replace nouns: I see it, I give her, I buy them',
  slides=[
    ('Direct object pronouns', None,
     '<p class="slide-explanation">Direct object pronouns replace the thing or person receiving the action: <b>me, te, lo, la, nos, os, los, las</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>¿El libro? <b>Lo</b> leo. (The book? I read it.)</p>'
     '<p style="margin-top:8px">¿La película? <b>La</b> vi anoche. (The film? I saw it last night.)</p>'
     '<p style="margin-top:8px">¿Las llaves? <b>Las</b> tengo yo. (The keys? I have them.)</p></div>'),
    ('Position: before the verb', None,
     '<p class="slide-explanation">Unlike English, the pronoun goes <b>before</b> the conjugated verb.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Lo compro.</b> (I buy it — literally "it I-buy".)</p>'
     '<p style="margin-top:8px"><b>No la conozco.</b> (I do not know her.) — no goes first</p></div>'),
    ('Indirect object pronouns', None,
     '<p class="slide-explanation">Indirect pronouns mark <b>to/for whom</b>: <b>me, te, le, nos, os, les</b>. Note le/les for him, her, them.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Le doy el libro.</b> (I give him/her the book.)</p>'
     '<p style="margin-top:8px"><b>Les escribo un correo.</b> (I write them an email.)</p>'
     '<p style="margin-top:8px"><b>¿Me prestas tu boli?</b> (Will you lend me your pen?)</p></div>'),
    ('With infinitives: two options', None,
     '<p class="slide-explanation">With ir a + infinitive, querer + infinitive etc., the pronoun can go before the first verb <b>or</b> attach to the infinitive. Both are correct.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Lo voy a comprar.</b> = <b>Voy a comprarlo.</b> (I am going to buy it.)</p>'
     '<p style="margin-top:8px"><b>Te quiero ver.</b> = <b>Quiero verte.</b> (I want to see you.)</p></div>'),
    ('Two pronouns together', None,
     '<p class="slide-explanation">When both appear, the indirect comes first: <b>me lo, te la, nos los</b>... And <b>le/les + lo/la</b> becomes <b>se lo / se la</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>¿El regalo? <b>Te lo</b> doy mañana. (I will give it to you tomorrow.)</p>'
     '<p style="margin-top:8px">¿El libro a Juan? <b>Se lo</b> presto. (I lend it to him.)</p></div>'),
  ],
  traps=[
    ('Veo lo.', '<strong>Lo veo.</strong>', 'Pronouns go before the conjugated verb, not after'),
    ('La no conozco.', '<strong>No la conozco.</strong>', 'No comes before the pronoun: no + pronoun + verb'),
    ('Le veo. (I see him)', '<strong>Lo veo.</strong>', 'Seeing someone is a direct object: lo/la, not le'),
    ('Doy el libro a él → Doy le el libro.', '<strong>Le doy</strong> el libro.', 'The indirect pronoun also goes before the verb'),
    ('Le lo doy.', '<strong>Se lo</strong> doy.', 'le + lo is impossible — it always becomes se lo'),
  ],
  summary=[
    ('Direct', 'me, te, lo, la, nos, os, los, las', '¿El libro? Lo leo.'),
    ('Indirect', 'me, te, le, nos, os, les', 'Le doy el libro.'),
    ('Position', 'before the conjugated verb', 'No la conozco.'),
    ('With infinitive', 'before or attached', 'Lo voy a comprar / Voy a comprarlo.'),
    ('Two together', 'indirect + direct; le+lo → se lo', 'Te lo doy. Se lo presto.'),
  ],
  ex1=('Choose the correct pronoun', 'Tap the best option for each sentence.', [
    ('¿La televisión? No ______ veo mucho.', ['la', 'lo', 'le'], 'la',
     'Televisión is feminine singular, so the direct pronoun is la.'),
    ('¿Los deberes? ______ hago después de cenar.', ['Los', 'Las', 'Les'], 'Los',
     'Deberes is masculine plural → los. Les is only for indirect objects.'),
    ('______ doy las llaves a mi madre.', ['Le', 'La', 'Lo'], 'Le',
     'Giving to my mother = indirect object → le. The thing given (las llaves) stays as a noun here.'),
    ('¿Me prestas el boli? — Sí, te ______ presto.', ['lo', 'le', 'la'], 'lo',
     'El boli is masculine singular → lo, after the indirect te: te lo presto.'),
    ('¿El regalo para Juan? ______ lo doy mañana.', ['Se', 'Le', 'La'], 'Se',
     'Le + lo is impossible; le changes to se: se lo doy.'),
    ('¿A tus padres? ______ escribo cada semana.', ['Les', 'Los', 'Se'], 'Les',
     'Writing to them = indirect plural → les escribo.'),
  ]),
  ex2=('Rewrite with a pronoun', 'Type the missing pronoun — no accents needed.', [
    ('¿El periódico? ______ leo por la mañana. (it, masc.)', 'lo',
     'Periódico is masculine singular: lo leo.'),
    ('¿Las fotos? ______ subo a internet esta noche. (them, fem.)', 'las',
     'Fotos is feminine plural: las subo.'),
    ('A María ______ regalo flores. (to her)', 'le',
     'Indirect object for ella: le regalo flores.'),
    ('¿La verdad? Voy a decir______ . (attach "it" to the infinitive)', 'la',
     'Attached to the infinitive: decirla — la verdad is feminine.'),
    ('¿El coche a tu hermano? ______ lo vendo. (to him + it)', 'se',
     'Le + lo becomes se lo: se lo vendo.'),
  ]),
  ex3=('Position and usage', 'Choose the correct option.', [
    ('Which is correct?', ['Lo voy a comprar.', 'Voy a lo comprar.', 'Lo voy a comprarlo.'], 'Lo voy a comprar.',
     'Before the first verb or attached to the infinitive (voy a comprarlo) — never in the middle, never twice.'),
    ('"I do not know her" is...', ['No la conozco.', 'La no conozco.', 'No le conozco a ella.'], 'No la conozco.',
     'No + pronoun + verb. Knowing someone takes a direct pronoun: la.'),
    ('"Quiero verte" means...', ['I want to see you.', 'I want you to see.', 'You want to see me.'], 'I want to see you.',
     'Te is attached to the infinitive ver: I want to see you.'),
    ('Replace both: "Doy el libro a Ana" →', ['Se lo doy.', 'Le lo doy.', 'Lo le doy.'], 'Se lo doy.',
     'Indirect first, and le + lo must become se lo.'),
    ('"¿Me ayudas?" means...', ['Will you help me?', 'Do I help you?', 'Help yourself.'], 'Will you help me?',
     'Me is the object of ayudas (you help): will you help me?'),
  ]),
  game_desc='Each pronoun passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('lo', 'lo', 'it or him - direct object, masculine singular', 'direct object masc.', '¿El libro? <b>Lo</b> leo esta noche.', '¿El libro? ______ leo esta noche.', 'lo'),
    ('la', 'la', 'it or her - direct object, feminine singular', 'direct object fem.', '¿La película? <b>La</b> vi anoche.', '¿La película? ______ vi anoche.', 'la'),
    ('los', 'los', 'them - direct object, masculine plural', 'direct object masc. pl.', '¿Los deberes? <b>Los</b> hago ahora.', '¿Los deberes? ______ hago ahora.', 'los'),
    ('las', 'las', 'them - direct object, feminine plural', 'direct object fem. pl.', '¿Las llaves? <b>Las</b> tengo yo.', '¿Las llaves? ______ tengo yo.', 'las'),
    ('le', 'le', 'to him or to her - indirect object singular', 'indirect object sing.', '<b>Le</b> doy el libro a María.', '______ doy el libro a María.', 'le'),
    ('les', 'les', 'to them - indirect object plural', 'indirect object pl.', '<b>Les</b> escribo un correo a mis padres.', '______ escribo un correo a mis padres.', 'les'),
    ('me', 'me', 'me or to me - first person object', 'first person object', '¿<b>Me</b> prestas tu boli?', '¿______ prestas tu boli?', 'me'),
    ('se-lo', 'se lo', 'it to him/her/them - le+lo always becomes se lo', 'combined pronouns', '¿El regalo? <b>Se lo</b> doy mañana.', '¿El regalo? ______ ______ doy mañana.', 'se lo'),
  ],
),

'prepositions-movement': dict(
  num='G13', short='Prepositions of Movement', title='Prepositions of Movement — A, De, Hacia, Hasta',
  subtitle='Say where you are going, coming from and how far',
  slides=[
    ('A — to', None,
     '<p class="slide-explanation"><b>A</b> marks the destination. Remember the contraction: <b>a + el = al</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Voy a Madrid.</b> (I am going to Madrid.)</p>'
     '<p style="margin-top:8px"><b>Vamos al cine.</b> (We are going to the cinema.) — a + el = al</p></div>'),
    ('De / Desde — from', None,
     '<p class="slide-explanation"><b>De</b> = from (origin). <b>Desde</b> = from, emphasising the starting point. Contraction: <b>de + el = del</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Vengo de la oficina.</b> (I am coming from the office.)</p>'
     '<p style="margin-top:8px"><b>Salgo del trabajo a las seis.</b> (I leave work at six.) — de + el = del</p>'
     '<p style="margin-top:8px"><b>Desde mi casa hasta la estación hay un kilómetro.</b> (From my house to the station it is one kilometre.)</p></div>'),
    ('Hacia / Hasta — towards / as far as', None,
     '<p class="slide-explanation"><b>Hacia</b> = towards (direction, you may not arrive). <b>Hasta</b> = up to / as far as (the limit).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Caminamos hacia el centro.</b> (We walk towards the centre.)</p>'
     '<p style="margin-top:8px"><b>Este autobús va hasta la playa.</b> (This bus goes as far as the beach.)</p></div>'),
    ('Por — through / along', None,
     '<p class="slide-explanation"><b>Por</b> covers movement through or along a place.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Paseamos por el parque.</b> (We stroll through the park.)</p>'
     '<p style="margin-top:8px"><b>El tren pasa por Toledo.</b> (The train passes through Toledo.)</p></div>'),
    ('En — transport', None,
     '<p class="slide-explanation">For means of transport, Spanish uses <b>en</b>: en coche, en tren, en avión. Exception: <b>a pie</b> (on foot) and <b>a caballo</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Viajamos en tren.</b> (We travel by train.)</p>'
     '<p style="margin-top:8px"><b>Voy al trabajo a pie.</b> (I walk to work.)</p></div>'),
  ],
  traps=[
    ('Voy a el cine.', 'Voy <strong>al</strong> cine.', 'a + el always contracts to al'),
    ('Vengo de el trabajo.', 'Vengo <strong>del</strong> trabajo.', 'de + el always contracts to del'),
    ('Viajo por tren.', 'Viajo <strong>en</strong> tren.', 'Transport takes en: en tren, en coche — except a pie'),
    ('Voy en pie.', 'Voy <strong>a pie</strong>.', 'On foot is the exception: a pie, never en pie'),
    ('El bus va hacia la playa (and stops there).', 'El bus va <strong>hasta</strong> la playa.', 'If it reaches the end point, use hasta; hacia is only direction'),
  ],
  summary=[
    ('To', 'a (a+el = al)', 'Vamos al cine.'),
    ('From', 'de (de+el = del) / desde', 'Vengo del trabajo.'),
    ('Towards', 'hacia', 'Caminamos hacia el centro.'),
    ('As far as', 'hasta', 'El bus va hasta la playa.'),
    ('Through / along', 'por', 'Paseamos por el parque.'),
    ('Transport', 'en + transport / a pie', 'Viajamos en tren. Voy a pie.'),
  ],
  ex1=('Choose the correct preposition', 'Tap the best option for each sentence.', [
    ('Esta tarde vamos ______ cine.', ['al', 'a el', 'en el'], 'al',
     'A + el contracts to al — always. "A el" is never written.'),
    ('Vengo ______ supermercado.', ['del', 'de el', 'al'], 'del',
     'De + el contracts to del: vengo del supermercado.'),
    ('Caminamos ______ la estación, pero paramos antes.', ['hacia', 'hasta', 'de'], 'hacia',
     '"But we stop before" tells you it is direction only → hacia. Hasta would mean reaching it.'),
    ('El autobús llega ______ la última parada.', ['hasta', 'hacia', 'por'], 'hasta',
     'It reaches the final stop — the limit — so hasta.'),
    ('Me gusta pasear ______ la playa.', ['por', 'a', 'hasta'], 'por',
     'Strolling along/through a place = por la playa.'),
    ('Siempre viajo ______ tren.', ['en', 'por', 'a'], 'en',
     'Means of transport take en: en tren. Only a pie / a caballo use a.'),
  ]),
  ex2=('Complete with the preposition', 'Type the missing word — no accents needed.', [
    ('Voy ______ trabajo a pie. (to the, contracted)', 'al',
     'A + el trabajo = al trabajo. The contraction is compulsory.'),
    ('Salimos ______ hotel a las nueve. (from the, contracted)', 'del',
     'De + el hotel = del hotel.'),
    ('______ mi casa hasta el centro hay dos kilometros. (from, emphasising start)', 'desde',
     'Desde ... hasta marks the full stretch: desde mi casa hasta el centro.'),
    ('El tren pasa ______ Toledo. (through)', 'por',
     'Passing through a place is por: pasa por Toledo.'),
    ('Prefiero ir ______ pie. (on foot)', 'a',
     'The fixed exception: a pie — on foot.'),
  ]),
  ex3=('Meaning check', 'Choose the correct option.', [
    ('"El bus va hasta la playa" means the bus...', ['goes as far as the beach', 'goes towards the beach', 'goes through the beach'], 'goes as far as the beach',
     'Hasta marks the end point — the bus reaches the beach.'),
    ('Which is WRONG?', ['Voy a el parque.', 'Voy al parque.', 'Vengo del parque.'], 'Voy a el parque.',
     'A + el must contract: al parque.'),
    ('"By car" is...', ['en coche', 'por coche', 'a coche'], 'en coche',
     'Transport uses en. Por would suggest movement through something.'),
    ('"Caminamos hacia el rio" means we...', ['walk towards the river', 'walk as far as the river', 'walk along the river'], 'walk towards the river',
     'Hacia is direction only — we may or may not arrive. Along would be por.'),
    ('"From Monday to Friday" uses the same pair as movement:', ['desde ... hasta', 'de ... a el', 'por ... en'], 'desde ... hasta',
     'Desde ... hasta works for space and time: desde el lunes hasta el viernes.'),
  ]),
  game_desc='Each preposition passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('al', 'al', 'to the - compulsory contraction of a + el', 'a + el', 'Vamos <b>al</b> cine esta tarde.', 'Vamos ______ cine esta tarde.', 'al'),
    ('del', 'del', 'from the - compulsory contraction of de + el', 'de + el', 'Vengo <b>del</b> trabajo.', 'Vengo ______ trabajo.', 'del'),
    ('a', 'a', 'to - marks the destination', 'destination marker', 'Voy <b>a</b> Madrid mañana.', 'Voy ______ Madrid mañana.', 'a'),
    ('desde', 'desde', 'from - emphasises the starting point', 'starting point', '<b>Desde</b> mi casa hasta la estación hay un kilómetro.', '______ mi casa hasta la estación hay un kilómetro.', 'desde'),
    ('hacia', 'hacia', 'towards - direction without necessarily arriving', 'direction only', 'Caminamos <b>hacia</b> el centro.', 'Caminamos ______ el centro.', 'hacia'),
    ('hasta', 'hasta', 'up to or as far as - the limit of the movement', 'end point', 'Este autobús va <b>hasta</b> la playa.', 'Este autobús va ______ la playa.', 'hasta'),
    ('por', 'por', 'through or along a place', 'through/along', 'Paseamos <b>por</b> el parque.', 'Paseamos ______ el parque.', 'por'),
    ('en-tren', 'en tren', 'by train - transport takes en', 'transport preposition', 'Viajamos <b>en tren</b> a Sevilla.', 'Viajamos ______ ______ a Sevilla.', 'en tren'),
  ],
),
}
