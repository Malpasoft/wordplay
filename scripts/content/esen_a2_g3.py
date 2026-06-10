# -*- coding: utf-8 -*-
"""espanol-en A2 grammar content — batch 3 (final 4 chapters)."""

CHAPTERS = {

'relative-clauses-basic': dict(
  num='G16', short='Relative Clauses', title='Relative Clauses — Que, Donde, Quien',
  subtitle='Join two ideas: the book that I read, the city where I live',
  slides=[
    ('Que — the all-rounder', None,
     '<p class="slide-explanation"><b>Que</b> covers English that, which and who. Unlike English, it can <b>never</b> be left out.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El libro que leí es genial.</b> (The book [that] I read is great.)</p>'
     '<p style="margin-top:8px"><b>La chica que vive aquí es médica.</b> (The girl who lives here is a doctor.)</p></div>'
     '<p style="margin-top:16px">English drops "that" all the time — Spanish never does.</p>'),
    ('Donde — where', None,
     '<p class="slide-explanation"><b>Donde</b> (no accent here) links to a place.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>La ciudad donde vivo es pequeña.</b> (The city where I live is small.)</p>'
     '<p style="margin-top:8px"><b>Ese es el restaurante donde comimos.</b> (That is the restaurant where we ate.)</p></div>'),
    ('Quien — who, after prepositions', None,
     '<p class="slide-explanation"><b>Quien/quienes</b> refers to people, mainly after prepositions (con, a, para...). In everyday speech, que is fine when there is no preposition.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>La amiga con quien viajé es de Cádiz.</b> (The friend with whom I travelled is from Cádiz.)</p>'
     '<p style="margin-top:8px"><b>El chico que conocí ayer...</b> (The boy I met yesterday...) — que, no preposition</p></div>'),
    ('Lo que — what / the thing that', None,
     '<p class="slide-explanation"><b>Lo que</b> means "what" in the sense of "the thing that".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>No entiendo lo que dices.</b> (I do not understand what you are saying.)</p>'
     '<p style="margin-top:8px"><b>Lo que más me gusta es el queso.</b> (What I like most is the cheese.)</p></div>'),
  ],
  traps=[
    ('El libro leí es genial.', 'El libro <strong>que</strong> leí es genial.', 'Spanish never drops the relative pronoun que'),
    ('La ciudad que vivo...', 'La ciudad <strong>donde</strong> vivo...', 'For places where something happens, use donde (or en la que)'),
    ('La persona con que hablé...', 'La persona con <strong>quien</strong> hablé...', 'After a preposition, people take quien (or la que)'),
    ('No entiendo que dices.', 'No entiendo <strong>lo que</strong> dices.', '"What" as "the thing that" = lo que'),
    ('La ciudad dónde vivo (accent)', 'La ciudad <strong>donde</strong> vivo', 'Relative donde has no accent — only the question ¿dónde? does'),
  ],
  summary=[
    ('That / which / who', 'que (never dropped)', 'el libro que leí'),
    ('Where', 'donde (no accent)', 'la ciudad donde vivo'),
    ('With whom etc.', 'preposition + quien', 'la amiga con quien viajé'),
    ('What (= the thing that)', 'lo que', 'No entiendo lo que dices.'),
  ],
  ex1=('Choose the relative', 'Tap the best option for each sentence.', [
    ('La película ______ vimos anoche es francesa.', ['que', 'quien', 'donde'], 'que',
     'A thing (la película) takes que: la película que vimos.'),
    ('El pueblo ______ nació mi madre está en Galicia.', ['donde', 'que', 'quien'], 'donde',
     'A place where something happened takes donde.'),
    ('La profesora con ______ estudio es muy buena.', ['quien', 'que', 'donde'], 'quien',
     'Person after the preposition con → quien: con quien estudio.'),
    ('No me gusta ______ dices.', ['lo que', 'que', 'quien'], 'lo que',
     '"What you say" = the thing that you say = lo que dices.'),
    ('El hombre ______ vive arriba es músico.', ['que', 'quien que', 'donde'], 'que',
     'No preposition, so everyday Spanish uses que even for people.'),
    ('Madrid es la ciudad ______ más me gusta.', ['que', 'donde', 'quien'], 'que',
     'Here the city is the thing liked (direct object), so que: la ciudad que más me gusta.'),
  ]),
  ex2=('Complete the relative', 'Type the missing word(s) — no accents needed.', [
    ('El coche ______ compré es rojo. (that)', 'que',
     'Things take que, and it can never be omitted: el coche que compré.'),
    ('La casa ______ vivimos tiene jardín. (where)', 'donde',
     'Place + action happening there = donde: la casa donde vivimos.'),
    ('El amigo con ______ fui al cine es Pablo. (whom)', 'quien',
     'Preposition + person = quien: con quien fui.'),
    ('______ que necesito es dormir. (what = the thing that)', 'lo',
     'Lo que necesito = what I need.'),
    ('La chica ______ canta es mi prima. (who)', 'que',
     'Subject relative for a person without preposition: que canta.'),
  ]),
  ex3=('Usage check', 'Choose the correct option.', [
    ('"The book I read" must become...', ['el libro que leí', 'el libro leí', 'el libro quien leí'], 'el libro que leí',
     'English drops "that"; Spanish never does — and books take que, not quien.'),
    ('Relative donde vs question dónde:', ['relative has no accent; question does', 'both have accents', 'neither has an accent'], 'relative has no accent; question does',
     'La ciudad donde vivo (no accent) vs ¿Dónde vives? (accent).'),
    ('Which is WRONG?', ['La mujer con que trabajo.', 'La mujer con quien trabajo.', 'La mujer que trabaja aquí.'], 'La mujer con que trabajo.',
     'After con, a person needs quien (or la que): con quien trabajo.'),
    ('"Lo que" means...', ['what (the thing that)', 'where', 'whose'], 'what (the thing that)',
     'Lo que dices = what (the thing that) you say.'),
    ('Pick the natural sentence:', ['Ese es el bar donde conocí a tu padre.', 'Ese es el bar que conocí a tu padre.', 'Ese es el bar quien conocí a tu padre.'], 'Ese es el bar donde conocí a tu padre.',
     'The bar is the place where it happened: donde.'),
  ]),
  game_desc='Each relative passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('que-thing', 'que (things)', 'that or which - for things, never omitted', 'that/which', 'El libro <b>que</b> leí es genial.', 'El libro ______ leí es genial.', 'que'),
    ('que-person', 'que (people)', 'who - for people without a preposition', 'who (no preposition)', 'La chica <b>que</b> vive aquí es médica.', 'La chica ______ vive aquí es médica.', 'que'),
    ('donde', 'donde', 'where - relative of place, no accent', 'where (relative)', 'La ciudad <b>donde</b> vivo es pequeña.', 'La ciudad ______ vivo es pequeña.', 'donde'),
    ('con-quien', 'con quien', 'with whom - preposition + person', 'preposition + person', 'La amiga <b>con quien</b> viajé es de Cádiz.', 'La amiga con ______ viajé es de Cádiz.', 'quien'),
    ('lo-que', 'lo que', 'what - the thing that', 'what = the thing that', 'No entiendo <b>lo que</b> dices.', 'No entiendo ______ ______ dices.', 'lo que'),
    ('never-drop', 'que never dropped', 'unlike English that, que is compulsory', 'compulsory que', 'La película <b>que</b> vimos es buena.', 'La película ______ vimos es buena.', 'que'),
    ('quienes', 'quienes', 'whom plural - quien for several people', 'plural quien', 'Los amigos con <b>quienes</b> ceno...', 'Los amigos con ______ ceno...', 'quienes'),
    ('lo-que-mas', 'lo que más', 'what ... most - common superlative frame', 'what most', '<b>Lo que más</b> me gusta es el queso.', 'Lo que ______ me gusta es el queso.', 'mas'),
  ],
),

'short-answers': dict(
  num='G17', short='Short Answers', title='Short Answers — Sí, claro / Creo que no',
  subtitle='Answer naturally without repeating everything',
  slides=[
    ('Sí / No + verb', None,
     '<p class="slide-explanation">Spanish has no "do" — so no "Yes, I do". The natural short answer repeats the <b>verb</b> (or just says sí/no).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>—¿Hablas inglés? —<b>Sí, hablo un poco.</b> / —<b>Sí.</b></p>'
     '<p style="margin-top:8px">—¿Tienes hambre? —<b>No, no tengo.</b></p></div>'
     '<p style="margin-top:16px">Note the double no: the first answers, the second negates the verb.</p>'),
    ('Creo que sí / creo que no', None,
     '<p class="slide-explanation">"I think so / I don\'t think so" = <b>creo que sí / creo que no</b>. The same frame works with espero (hope), supongo (suppose), me parece (it seems).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>—¿Viene Marta? —<b>Creo que sí.</b> (I think so.)</p>'
     '<p style="margin-top:8px">—¿Hay clase mañana? —<b>Espero que no.</b> (I hope not.)</p></div>'),
    ('Claro / Por supuesto', None,
     '<p class="slide-explanation">To agree warmly: <b>claro</b> (of course), <b>claro que sí</b>, <b>por supuesto</b> (certainly).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>—¿Me ayudas? —<b>¡Claro que sí!</b></p>'
     '<p style="margin-top:8px">—¿Puedo pasar? —<b>Por supuesto.</b></p></div>'),
    ('Yo también / yo tampoco', None,
     '<p class="slide-explanation">Agreeing with someone: <b>yo también</b> (me too) after a positive, <b>yo tampoco</b> (me neither) after a negative.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>—Me encanta el cine. —<b>A mí también.</b> (Me too — with gustar-type verbs it is a mí.)</p>'
     '<p style="margin-top:8px">—No como carne. —<b>Yo tampoco.</b> (Me neither.)</p></div>'),
    ('Disagreeing politely', None,
     '<p class="slide-explanation">To disagree with the previous speaker: <b>yo sí</b> (I do) after their negative, <b>yo no</b> (I don\'t) after their positive.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>—No me gusta el fútbol. —<b>A mí sí.</b> (I like it.)</p>'
     '<p style="margin-top:8px">—Yo vivo en el centro. —<b>Yo no.</b> (I don\'t.)</p></div>'),
  ],
  traps=[
    ('—¿Hablas inglés? —Sí, hago.', '—Sí, <strong>hablo</strong>.', 'There is no do in Spanish — repeat the real verb'),
    ('Creo que yes.', 'Creo que <strong>sí</strong>.', 'The frame is creo que sí / creo que no'),
    ('—No como carne. —Yo también.', '—Yo <strong>tampoco</strong>.', 'After a negative, me neither = yo tampoco'),
    ('—Me gusta el cine. —Yo también.', '—<strong>A mí</strong> también.', 'With gustar, agreement uses a mí también, not yo'),
    ('—¿Tienes hambre? —No, tengo.', '—No, <strong>no</strong> tengo.', 'The verb keeps its own no: no, no tengo'),
  ],
  summary=[
    ('Yes, I do', 'Sí, + verb', 'Sí, hablo un poco.'),
    ('No, I don\'t', 'No, no + verb', 'No, no tengo.'),
    ('I think so / not', 'creo que sí / no', 'Creo que sí.'),
    ('Of course', 'claro (que sí), por supuesto', '¡Claro que sí!'),
    ('Me too / neither', '(a mí) también / tampoco', 'Yo tampoco. A mí también.'),
    ('I do / I don\'t (contrast)', 'yo sí / yo no', 'A mí sí.'),
  ],
  ex1=('Choose the natural answer', 'Tap the best option for each exchange.', [
    ('—¿Hablas francés? —______', ['Sí, un poco.', 'Sí, hago.', 'Sí, soy.'], 'Sí, un poco.',
     'No auxiliary do exists: answer with sí + real information (or repeat hablo).'),
    ('—¿Viene Pedro a la cena? —______ (I think so)', ['Creo que sí.', 'Creo que yes.', 'Pienso sí.'], 'Creo que sí.',
     'The fixed frame is creo que sí.'),
    ('—No me gusta el café. —______ (me neither)', ['A mí tampoco.', 'A mí también.', 'Yo sí no.'], 'A mí tampoco.',
     'Gustar-type verb → a mí, and after a negative → tampoco.'),
    ('—¿Me ayudas con la maleta? —______ (of course!)', ['¡Claro que sí!', '¡Claro que no!', 'Creo que no.'], '¡Claro que sí!',
     'Warm agreement: claro que sí.'),
    ('—Yo vivo en el centro. —______ (I don\'t)', ['Yo no.', 'Yo tampoco.', 'A mí no.'], 'Yo no.',
     'Contrasting with a positive statement: yo no. Tampoco only follows negatives.'),
    ('—¿Tienes coche? —______', ['No, no tengo.', 'No, tengo.', 'No, no hago.'], 'No, no tengo.',
     'First no answers; second no negates the verb: no, no tengo.'),
  ]),
  ex2=('Complete the short answer', 'Type the missing word — no accents needed.', [
    ('—¿Hay examen mañana? —Espero que ______ . (I hope not)', 'no',
     'Espero que no = I hope not. The same frame as creo que sí/no.'),
    ('—Me encanta viajar. —A mí ______ . (me too)', 'tambien',
     'With encantar/gustar: a mí también.'),
    ('—No tengo dinero. —Yo ______ . (me neither)', 'tampoco',
     'After a negative statement: yo tampoco.'),
    ('—¿Puedo abrir la ventana? —Por ______ . (certainly)', 'supuesto',
     'Por supuesto = of course / certainly.'),
    ('—¿Vienes a la fiesta? —Creo que ______ , pero no estoy seguro. (I think so)', 'si',
     'Creo que sí — answered with sí (accent optional when you type).'),
  ]),
  ex3=('Pick the right reply', 'Choose the correct option.', [
    ('"Yes, I do" after ¿Fumas? is...', ['Sí, fumo.', 'Sí, hago.', 'Sí, estoy.'], 'Sí, fumo.',
     'Repeat the actual verb: sí, fumo. Hacer is not an auxiliary.'),
    ('Tampoco is used...', ['to agree with a negative', 'to agree with a positive', 'to disagree always'], 'to agree with a negative',
     'También agrees with positives; tampoco agrees with negatives.'),
    ('"—No me gusta el fútbol. —A mí sí." means...', ['I DO like it.', 'Me neither.', 'I agree.'], 'I DO like it.',
     'A mí sí contrasts: unlike you, I do like it.'),
    ('The warmest yes is...', ['¡Claro que sí!', 'Creo que sí.', 'Supongo que sí.'], '¡Claro que sí!',
     'Claro que sí is enthusiastic; the others sound hesitant.'),
    ('Which is WRONG?', ['—¿Estudias? —Sí, estudio que sí.', '—¿Estudias? —Sí.', '—¿Estudias? —Sí, estudio.'], '—¿Estudias? —Sí, estudio que sí.',
     '"Estudio que sí" mixes two patterns. Either sí alone or sí + verb.'),
  ]),
  game_desc='Each short-answer pattern passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('si-verbo', 'Sí, + verb', 'yes I do - repeat the verb, no auxiliary', 'affirmative answer', '—¿Hablas inglés? —<b>Sí, hablo</b> un poco.', '—¿Hablas inglés? —Sí, ______ un poco.', 'hablo'),
    ('no-no-verbo', 'No, no + verb', 'no I do not - double no is correct', 'negative answer', '—¿Tienes hambre? —<b>No, no tengo</b>.', '—¿Tienes hambre? —No, ______ tengo.', 'no'),
    ('creo-que-si', 'creo que sí', 'I think so', 'I think so', '—¿Viene Marta? —<b>Creo que sí</b>.', '—¿Viene Marta? —Creo que ______ .', 'si'),
    ('espero-que-no', 'espero que no', 'I hope not', 'I hope not', '—¿Hay clase? —<b>Espero que no</b>.', '—¿Hay clase? —Espero que ______ .', 'no'),
    ('claro-que-si', 'claro que sí', 'of course - warm agreement', 'of course', '—¿Me ayudas? —¡<b>Claro que sí</b>!', '—¿Me ayudas? —¡Claro que ______ !', 'si'),
    ('tambien', '(a mí) también', 'me too - agree with a positive', 'me too', '—Me encanta el cine. —A mí <b>también</b>.', '—Me encanta el cine. —A mí ______ .', 'tambien'),
    ('tampoco', '(yo) tampoco', 'me neither - agree with a negative', 'me neither', '—No como carne. —Yo <b>tampoco</b>.', '—No como carne. —Yo ______ .', 'tampoco'),
    ('a-mi-si', 'a mí sí', 'I do - contrast after their negative', 'polite contrast', '—No me gusta el fútbol. —<b>A mí sí</b>.', '—No me gusta el fútbol. —A mí ______ .', 'si'),
  ],
),

'too-enough-basic': dict(
  num='G18', short='Too & Enough', title='Too &amp; Enough — Demasiado y Suficiente',
  subtitle='Excess and sufficiency: too big, enough time',
  slides=[
    ('Demasiado + adjective — too', None,
     '<p class="slide-explanation">Before an adjective or adverb, <b>demasiado</b> means "too" and never changes.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Este piso es demasiado caro.</b> (This flat is too expensive.)</p>'
     '<p style="margin-top:8px"><b>Hablas demasiado rápido.</b> (You speak too fast.)</p></div>'),
    ('Demasiado + noun — too much / too many', None,
     '<p class="slide-explanation">Before a noun it agrees: demasiado, demasiada, demasiados, demasiadas.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hay demasiado ruido.</b> (There is too much noise.)</p>'
     '<p style="margin-top:8px"><b>Tengo demasiadas cosas que hacer.</b> (I have too many things to do.)</p></div>'),
    ('Suficiente — enough', None,
     '<p class="slide-explanation"><b>Suficiente(s)</b> = enough. It usually goes <b>before</b> the noun and only changes for number.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>No tengo suficiente dinero.</b> (I do not have enough money.)</p>'
     '<p style="margin-top:8px"><b>¿Hay suficientes sillas?</b> (Are there enough chairs?)</p></div>'),
    ('Lo suficientemente + adjective', None,
     '<p class="slide-explanation">"Adjective + enough" (big enough) = <b>lo suficientemente + adjective</b>. Spanish flips the English order.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>No es lo suficientemente grande.</b> (It is not big enough.)</p>'
     '<p style="margin-top:8px"><b>Eres lo suficientemente mayor para entenderlo.</b> (You are old enough to understand it.)</p></div>'
     '<p style="margin-top:16px">A simpler everyday alternative: <b>bastante</b> — Es bastante grande. (It is big enough / quite big.)</p>'),
    ('Demasiado as adverb after a verb', None,
     '<p class="slide-explanation">After a verb, demasiado = "too much" and never changes.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Trabajas demasiado.</b> (You work too much.)</p>'
     '<p style="margin-top:8px"><b>Comí demasiado.</b> (I ate too much.)</p></div>'),
  ],
  traps=[
    ('La maleta es demasiada pesada.', 'La maleta es <strong>demasiado</strong> pesada.', 'Before an adjective, demasiado is invariable'),
    ('Hay demasiado personas.', 'Hay <strong>demasiadas</strong> personas.', 'Before a noun it agrees: demasiadas personas'),
    ('No es grande suficiente.', 'No es <strong>lo suficientemente grande</strong>.', 'Spanish flips English "big enough": lo suficientemente + adjective'),
    ('Trabajo demasiados.', 'Trabajo <strong>demasiado</strong>.', 'After a verb, demasiado never agrees'),
    ('suficienta comida', '<strong>suficiente</strong> comida', 'Suficiente has no feminine form — only a plural'),
  ],
  summary=[
    ('Too + adjective', 'demasiado + adj (invariable)', 'demasiado caro'),
    ('Too much/many + noun', 'demasiado/a/os/as + noun', 'demasiadas cosas'),
    ('Too much (after verb)', 'verb + demasiado', 'Trabajas demasiado.'),
    ('Enough + noun', 'suficiente(s) + noun', 'suficiente dinero'),
    ('Adjective + enough', 'lo suficientemente + adj', 'lo suficientemente grande'),
  ],
  ex1=('Choose the correct form', 'Tap the best option for each sentence.', [
    ('El café está ______ caliente. (too)', ['demasiado', 'demasiada', 'demasiados'], 'demasiado',
     'Before the adjective caliente, demasiado is invariable.'),
    ('Hay ______ gente en el concierto. (too many)', ['demasiada', 'demasiado', 'demasiados'], 'demasiada',
     'Gente is feminine singular: demasiada gente.'),
    ('No tenemos ______ tiempo. (enough)', ['suficiente', 'suficientes', 'demasiado'], 'suficiente',
     'Tiempo is singular: suficiente tiempo.'),
    ('¿Hay ______ sillas para todos? (enough)', ['suficientes', 'suficiente', 'demasiada'], 'suficientes',
     'Sillas is plural, so suficientes.'),
    ('Este barrio no es ______ tranquilo. (quiet enough)', ['lo suficientemente', 'suficiente', 'demasiado'], 'lo suficientemente',
     'Adjective + enough flips to lo suficientemente + adjective.'),
    ('Mi jefe trabaja ______ . (too much)', ['demasiado', 'demasiados', 'demasiada'], 'demasiado',
     'After a verb, demasiado is an invariable adverb.'),
  ]),
  ex2=('Complete the sentence', 'Type the missing word — no accents needed.', [
    ('Comí ______ en la cena. (too much)', 'demasiado',
     'After the verb: comí demasiado — invariable.'),
    ('Hay ______ coches en esta calle. (too many, masc. pl.)', 'demasiados',
     'Coches is masculine plural: demasiados coches.'),
    ('No tengo ______ dinero para el viaje. (enough)', 'suficiente',
     'Dinero is singular: suficiente dinero.'),
    ('La caja no es lo ______ grande. (enough, the -mente word)', 'suficientemente',
     'Lo suficientemente grande = big enough.'),
    ('Tengo ______ trabajo esta semana. (too much, masc. sing.)', 'demasiado',
     'Trabajo (noun) is masculine singular: demasiado trabajo.'),
  ]),
  ex3=('Meaning check', 'Choose the correct option.', [
    ('"Trabajas demasiado" means...', ['You work too much.', 'You work enough.', 'You work too many.'], 'You work too much.',
     'Verb + demasiado = too much.'),
    ('"It is not big enough" is...', ['No es lo suficientemente grande.', 'No es grande suficiente.', 'No es demasiado grande.'], 'No es lo suficientemente grande.',
     'The Spanish order flips English: lo suficientemente + adjective.'),
    ('Which is WRONG?', ['demasiada calor', 'demasiado calor', 'demasiado frío'], 'demasiada calor',
     'Calor is masculine: demasiado calor.'),
    ('"Bastante grande" can mean...', ['big enough / quite big', 'too big', 'never big'], 'big enough / quite big',
     'Bastante is the everyday way to say "enough/quite" before adjectives.'),
    ('"¿Hay suficientes entradas?" asks if there are...', ['enough tickets', 'too many tickets', 'few tickets'], 'enough tickets',
     'Suficientes + plural noun = enough tickets.'),
  ]),
  game_desc='Each structure passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('demasiado-adj', 'demasiado + adjective', 'too - invariable before adjectives', 'too + adjective', 'Este piso es <b>demasiado</b> caro.', 'Este piso es ______ caro.', 'demasiado'),
    ('demasiado-noun', 'demasiado/a + noun', 'too much - agrees with the noun', 'too much + noun', 'Hay <b>demasiado</b> ruido aquí.', 'Hay ______ ruido aquí. (masc.)', 'demasiado'),
    ('demasiadas', 'demasiadas + noun', 'too many - feminine plural agreement', 'too many fem.', 'Tengo <b>demasiadas</b> cosas que hacer.', 'Tengo ______ cosas que hacer.', 'demasiadas'),
    ('verbo-demasiado', 'verb + demasiado', 'too much after a verb - invariable', 'adverbial too much', 'Trabajas <b>demasiado</b>.', 'Trabajas ______ .', 'demasiado'),
    ('suficiente', 'suficiente + noun', 'enough - changes only for number', 'enough + noun', 'No tengo <b>suficiente</b> dinero.', 'No tengo ______ dinero.', 'suficiente'),
    ('suficientes', 'suficientes + plural', 'enough with plural nouns', 'enough plural', '¿Hay <b>suficientes</b> sillas?', '¿Hay ______ sillas?', 'suficientes'),
    ('lo-suficientemente', 'lo suficientemente + adj', 'adjective + enough - flipped order', 'big enough pattern', 'No es <b>lo suficientemente</b> grande.', 'No es lo ______ grande.', 'suficientemente'),
    ('bastante', 'bastante + adjective', 'quite or enough - everyday alternative', 'everyday enough', 'Es <b>bastante</b> grande.', 'Es ______ grande.', 'bastante'),
  ],
),

'countable-uncountable-basic': dict(
  num='G4', short='Countable & Uncountable', title='Countable &amp; Uncountable — ¿Cuánto o Cuántos?',
  subtitle='Mass vs countable nouns and their question words',
  slides=[
    ('Two kinds of nouns', None,
     '<p class="slide-explanation">Like English, Spanish distinguishes countable nouns (un libro, dos libros) from mass nouns (agua, dinero, tiempo). The quantifier must match.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Countable: <b>tres manzanas, muchos coches</b></p>'
     '<p style="margin-top:8px">Uncountable: <b>mucha agua, poco dinero</b> — no plural, no numbers</p></div>'),
    ('¿Cuánto? agrees four ways', None,
     '<p class="slide-explanation">How much / how many = <b>cuánto, cuánta, cuántos, cuántas</b> — agreeing with the noun.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Cuánto dinero tienes?</b> (How much money...?)</p>'
     '<p style="margin-top:8px"><b>¿Cuánta leche queda?</b> (How much milk...?)</p>'
     '<p style="margin-top:8px"><b>¿Cuántos hermanos tienes?</b> (How many brothers...?)</p>'
     '<p style="margin-top:8px"><b>¿Cuántas horas trabajas?</b> (How many hours...?)</p></div>'),
    ('Mucho / poco with both kinds', None,
     '<p class="slide-explanation">With mass nouns use the singular (mucho dinero, poca agua); with countables use the plural (muchos libros, pocas sillas).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hay mucho tráfico.</b> (much traffic — mass)</p>'
     '<p style="margin-top:8px"><b>Hay muchos coches.</b> (many cars — countable)</p></div>'),
    ('Un poco de / unos pocos', None,
     '<p class="slide-explanation"><b>Un poco de</b> + mass noun = a bit of. For countables, use <b>unos pocos / unas pocas</b> or simply <b>algunos/as</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>un poco de pan</b> (a bit of bread)</p>'
     '<p style="margin-top:8px"><b>unas pocas monedas / algunas monedas</b> (a few coins)</p></div>'),
    ('Containers make mass nouns countable', None,
     '<p class="slide-explanation">To count a mass noun, add a container or unit: un vaso de agua, dos tazas de café, un kilo de arroz.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Me pones un vaso de agua?</b> (a glass of water)</p>'
     '<p style="margin-top:8px"><b>Compra dos barras de pan.</b> (two loaves of bread)</p></div>'),
  ],
  traps=[
    ('¿Cuántos dinero tienes?', '¿<strong>Cuánto</strong> dinero tienes?', 'Dinero is a mass noun — singular cuánto'),
    ('Hay muchas tráfico.', 'Hay <strong>mucho</strong> tráfico.', 'Tráfico is mass and masculine: mucho tráfico'),
    ('dos aguas, tres panes... (counting mass nouns)', 'dos <strong>vasos de</strong> agua, tres <strong>barras de</strong> pan', 'Count the container or unit, not the mass noun'),
    ('un poco de monedas', '<strong>unas pocas</strong> monedas', 'Un poco de only takes mass nouns; countables take unos pocos/as'),
    ('¿Cuánta años tienes?', '¿<strong>Cuántos</strong> años tienes?', 'Años is masculine plural: cuántos años'),
  ],
  summary=[
    ('How much (masc.)', 'cuánto + mass noun', '¿Cuánto dinero?'),
    ('How much (fem.)', 'cuánta + mass noun', '¿Cuánta leche?'),
    ('How many', 'cuántos/cuántas + plural', '¿Cuántos hermanos?'),
    ('Much / many', 'mucho/a + mass, muchos/as + plural', 'mucho tráfico, muchos coches'),
    ('A bit of', 'un poco de + mass', 'un poco de pan'),
    ('Counting mass', 'unit + de + mass noun', 'un vaso de agua'),
  ],
  ex1=('Cuánto, cuánta, cuántos or cuántas?', 'Tap the best option for each question.', [
    ('¿______ dinero necesitas?', ['Cuánto', 'Cuántos', 'Cuánta'], 'Cuánto',
     'Dinero is a masculine mass noun: cuánto dinero.'),
    ('¿______ leche compro?', ['Cuánta', 'Cuánto', 'Cuántas'], 'Cuánta',
     'Leche is a feminine mass noun: cuánta leche.'),
    ('¿______ años tienes?', ['Cuántos', 'Cuánto', 'Cuántas'], 'Cuántos',
     'Años is masculine plural: cuántos años.'),
    ('¿______ horas duermes?', ['Cuántas', 'Cuántos', 'Cuánta'], 'Cuántas',
     'Horas is feminine plural: cuántas horas.'),
    ('Hay ______ tráfico en el centro.', ['mucho', 'muchos', 'muchas'], 'mucho',
     'Tráfico is mass and masculine: mucho tráfico.'),
    ('Quedan ______ entradas para el concierto.', ['pocas', 'poca', 'poco'], 'pocas',
     'Entradas is feminine plural: pocas entradas.'),
  ]),
  ex2=('Complete the quantity', 'Type the missing word — no accents needed.', [
    ('¿Quieres un poco ______ queso? (of)', 'de',
     'A bit of = un poco de + mass noun.'),
    ('Compra un ______ de agua, por favor. (a bottle → botella... type the container word "litro" or "vaso"? Use: vaso)', 'vaso',
     'Mass nouns are counted through units: un vaso de agua.'),
    ('No tengo ______ tiempo. (much, masc. sing.)', 'mucho',
     'Tiempo is mass: mucho tiempo.'),
    ('Hay ______ personas en la cola. (many, fem. pl.)', 'muchas',
     'Personas is feminine plural: muchas personas.'),
    ('Quedan ______ pocas monedas. (a few, fem.)', 'unas',
     'A few coins = unas pocas monedas.'),
  ]),
  ex3=('Usage check', 'Choose the correct option.', [
    ('Which noun is uncountable?', ['dinero', 'moneda', 'billete'], 'dinero',
     'Dinero is mass; monedas and billetes are the countable pieces.'),
    ('"Two waters" in a café is really...', ['dos botellas de agua', 'dos aguas grandes de', 'dos aguar'], 'dos botellas de agua',
     'Count the container: dos botellas (or dos vasos) de agua.'),
    ('Which is WRONG?', ['¿Cuántas dinero tienes?', '¿Cuánto dinero tienes?', '¿Cuántas monedas tienes?'], '¿Cuántas dinero tienes?',
     'Dinero is masculine mass — cuánto. Cuántas only fits feminine plurals.'),
    ('"Un poco de" works with...', ['arroz', 'sillas', 'coches'], 'arroz',
     'Un poco de + mass noun: un poco de arroz. Countables need unos pocos/algunos.'),
    ('"Hay poca gente" means...', ['There are few people.', 'There is a little person.', 'There are too many people.'], 'There are few people.',
     'Gente is a feminine mass noun; poca gente = few people / not many people.'),
  ]),
  game_desc='Each quantity pattern passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('cuanto', 'cuánto + mass', 'how much - masculine mass nouns', 'how much masc.', '¿<b>Cuánto</b> dinero tienes?', '¿______ dinero tienes?', 'cuanto'),
    ('cuanta', 'cuánta + mass', 'how much - feminine mass nouns', 'how much fem.', '¿<b>Cuánta</b> leche queda?', '¿______ leche queda?', 'cuanta'),
    ('cuantos', 'cuántos + plural', 'how many - masculine plurals', 'how many masc.', '¿<b>Cuántos</b> años tienes?', '¿______ años tienes?', 'cuantos'),
    ('cuantas', 'cuántas + plural', 'how many - feminine plurals', 'how many fem.', '¿<b>Cuántas</b> horas trabajas?', '¿______ horas trabajas?', 'cuantas'),
    ('mucho-mass', 'mucho + mass noun', 'much - singular with mass nouns', 'much + mass', 'Hay <b>mucho</b> tráfico hoy.', 'Hay ______ tráfico hoy.', 'mucho'),
    ('un-poco-de', 'un poco de', 'a bit of - mass nouns only', 'a bit of', '¿Quieres <b>un poco de</b> pan?', '¿Quieres un poco ______ pan?', 'de'),
    ('vaso-de', 'un vaso de agua', 'a glass of water - count the unit', 'counting unit', 'Ponme <b>un vaso de</b> agua, por favor.', 'Ponme un ______ de agua, por favor.', 'vaso'),
    ('unas-pocas', 'unas pocas + plural', 'a few - countable version of un poco', 'a few', 'Solo quedan <b>unas pocas</b> entradas.', 'Solo quedan unas ______ entradas.', 'pocas'),
  ],
),
}
