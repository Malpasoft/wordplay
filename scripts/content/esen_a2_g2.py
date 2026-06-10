# -*- coding: utf-8 -*-
"""espanol-en A2 grammar content — batch 2 (5 chapters)."""

CHAPTERS = {

'quantifiers-basic': dict(
  num='G15', short='Quantifiers', title='Quantifiers — Mucho, Poco, Demasiado',
  subtitle='How much and how many: mucho, poco, bastante, demasiado',
  slides=[
    ('Mucho — a lot of', None,
     '<p class="slide-explanation">Before a noun, <b>mucho</b> agrees in gender and number: mucho, mucha, muchos, muchas.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Tengo mucho trabajo.</b> (I have a lot of work.)</p>'
     '<p style="margin-top:8px"><b>Hay mucha gente.</b> (There are a lot of people.)</p>'
     '<p style="margin-top:8px"><b>Tiene muchos amigos / muchas ideas.</b></p></div>'
     '<p style="margin-top:16px">After a verb, mucho never changes: <b>Trabajo mucho.</b> (I work a lot.)</p>'),
    ('Poco — little / few', None,
     '<p class="slide-explanation"><b>Poco</b> also agrees: poco, poca, pocos, pocas. <b>Un poco de</b> means "a bit of" (only with singular nouns).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hay poca leche.</b> (There is little milk.)</p>'
     '<p style="margin-top:8px"><b>Tengo pocos amigos aquí.</b> (I have few friends here.)</p>'
     '<p style="margin-top:8px"><b>¿Quieres un poco de pan?</b> (Do you want a bit of bread?)</p></div>'),
    ('Demasiado — too much / too many', None,
     '<p class="slide-explanation"><b>Demasiado</b> before a noun agrees; before an adjective it never changes.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hay demasiados coches.</b> (There are too many cars.)</p>'
     '<p style="margin-top:8px"><b>El café está demasiado caliente.</b> (The coffee is too hot.) — invariable</p></div>'),
    ('Bastante / Suficiente — enough', None,
     '<p class="slide-explanation"><b>Bastante</b> = quite a lot / enough. <b>Suficiente</b> = sufficient. Both only change for number (bastantes, suficientes), never gender.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Tenemos bastante tiempo.</b> (We have enough/quite a lot of time.)</p>'
     '<p style="margin-top:8px"><b>No hay suficientes sillas.</b> (There are not enough chairs.)</p></div>'),
    ('Algunos / Ninguno — some / none', None,
     '<p class="slide-explanation"><b>Algunos/algunas</b> = some. <b>Ninguno/ninguna</b> = none, used in the singular, and shortened to <b>ningún</b> before a masculine noun.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Algunos estudiantes llegaron tarde.</b> (Some students arrived late.)</p>'
     '<p style="margin-top:8px"><b>No tengo ningún problema.</b> (I have no problem.)</p>'
     '<p style="margin-top:8px"><b>No hay ninguna farmacia cerca.</b> (There is no chemist nearby.)</p></div>'),
  ],
  traps=[
    ('Hay mucho gente.', 'Hay <strong>mucha</strong> gente.', 'Gente is feminine: mucha gente — mucho must agree before nouns'),
    ('Trabajo mucha.', 'Trabajo <strong>mucho</strong>.', 'After a verb, mucho is an adverb and never changes'),
    ('El café está demasiada caliente.', 'El café está <strong>demasiado</strong> caliente.', 'Before an adjective, demasiado is invariable'),
    ('No tengo ningunos problemas.', 'No tengo <strong>ningún problema</strong>.', 'Ninguno is used in the singular: ningún problema'),
    ('un poco de manzanas', '<strong>unas pocas manzanas</strong>', 'Un poco de only works with singular (mass) nouns'),
  ],
  summary=[
    ('A lot of', 'mucho/a/os/as + noun', 'mucha gente, muchos amigos'),
    ('A lot (adverb)', 'verb + mucho (invariable)', 'Trabajo mucho.'),
    ('Little / few', 'poco/a/os/as', 'poca leche, pocos amigos'),
    ('A bit of', 'un poco de + singular', 'un poco de pan'),
    ('Too much/many', 'demasiado/a/os/as + noun', 'demasiados coches'),
    ('Enough', 'bastante(s) / suficiente(s)', 'bastante tiempo'),
  ],
  ex1=('Choose the correct quantifier', 'Tap the best option for each sentence.', [
    ('Hay ______ gente en la plaza.', ['mucha', 'mucho', 'muchos'], 'mucha',
     'Gente is feminine singular (despite meaning "people"), so mucha gente.'),
    ('Tengo ______ libros en casa.', ['muchos', 'mucho', 'mucha'], 'muchos',
     'Libros is masculine plural: muchos libros.'),
    ('Estudio ______ los fines de semana.', ['mucho', 'mucha', 'muchos'], 'mucho',
     'After the verb, mucho is an adverb and never agrees: estudio mucho.'),
    ('Hay ______ coches en el centro. (too many)', ['demasiados', 'demasiado', 'demasiadas'], 'demasiados',
     'Coches is masculine plural: demasiados coches.'),
    ('La sopa está ______ caliente. (too)', ['demasiado', 'demasiada', 'mucha'], 'demasiado',
     'Before an adjective, demasiado never changes — even with a feminine noun.'),
    ('No hay ______ sillas para todos. (enough)', ['suficientes', 'suficiente', 'bastante'], 'suficientes',
     'Sillas is plural, so suficientes. Bastante would also need the plural -s.'),
  ]),
  ex2=('Complete the quantifier', 'Type the missing word — no accents needed.', [
    ('¿Quieres un ______ de agua? (a bit)', 'poco',
     'A bit of = un poco de + singular noun: un poco de agua.'),
    ('Tengo ______ trabajo esta semana. (a lot of, masc. sing.)', 'mucho',
     'Trabajo is masculine singular: mucho trabajo.'),
    ('Hay ______ leche en la nevera. (little, fem. sing.)', 'poca',
     'Leche is feminine: poca leche.'),
    ('No tengo ______ problema con eso. (no, before masc. noun)', 'ningun',
     'Ninguno shortens before a masculine noun: ningún problema (accepted without accent).'),
    ('______ estudiantes llegaron tarde. (some, masc. pl.)', 'algunos',
     'Some + masculine plural noun: algunos estudiantes.'),
  ]),
  ex3=('Usage check', 'Choose the correct option.', [
    ('Which is correct?', ['Hay bastante comida.', 'Hay bastanta comida.', 'Hay bastantes comida.'], 'Hay bastante comida.',
     'Bastante has no feminine form; with a singular noun it stays bastante.'),
    ('"I have no idea" is...', ['No tengo ninguna idea.', 'No tengo ningunas ideas.', 'Tengo ninguna idea.'], 'No tengo ninguna idea.',
     'Ninguna in the singular, and the sentence still needs no before the verb.'),
    ('"Un poco de" can be followed by...', ['pan', 'manzanas', 'coches'], 'pan',
     'Un poco de + singular mass noun: un poco de pan. Plurals need unos pocos / unas pocas.'),
    ('"Duermo poco" means...', ['I sleep little.', 'I sleep a little bit more.', 'I rarely fall asleep.'], 'I sleep little.',
     'Poco after a verb = not much: I sleep little / I do not sleep much.'),
    ('Which is WRONG?', ['demasiada calor', 'demasiado calor', 'demasiados problemas'], 'demasiada calor',
     'Calor is masculine in standard Spanish: demasiado calor.'),
  ]),
  game_desc='Each quantifier passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('mucho', 'mucho / mucha', 'a lot of - agrees with the noun', 'agreeing quantifier', 'Tengo <b>mucho</b> trabajo y <b>mucha</b> suerte.', 'Hay ______ gente en la plaza. (fem.)', 'mucha'),
    ('mucho-adv', 'mucho (adverb)', 'a lot - after a verb, never changes', 'invariable after verb', 'Trabajo <b>mucho</b> los lunes.', 'Estudio ______ los fines de semana.', 'mucho'),
    ('poco', 'poco / poca', 'little or few - agrees with the noun', 'small quantity', 'Hay <b>poca</b> leche en la nevera.', 'Hay ______ leche en la nevera.', 'poca'),
    ('un-poco-de', 'un poco de', 'a bit of - only with singular nouns', 'a bit of', '¿Quieres <b>un poco de</b> pan?', '¿Quieres un ______ de pan?', 'poco'),
    ('demasiado', 'demasiado/a/os/as', 'too much or too many - agrees before nouns', 'excess before noun', 'Hay <b>demasiados</b> coches en el centro.', 'Hay ______ coches en el centro. (masc. pl.)', 'demasiados'),
    ('demasiado-inv', 'demasiado + adjective', 'too - invariable before adjectives', 'excess before adjective', 'El café está <b>demasiado</b> caliente.', 'La sopa está ______ caliente.', 'demasiado'),
    ('bastante', 'bastante', 'enough or quite a lot - no gender form', 'enough', 'Tenemos <b>bastante</b> tiempo.', 'Tenemos ______ tiempo.', 'bastante'),
    ('ningun', 'ningún / ninguna', 'no or none - singular only, ningún before masc. noun', 'zero quantity', 'No tengo <b>ningún</b> problema.', 'No tengo ______ problema.', 'ningun'),
  ],
),

'conjunctions': dict(
  num='G3', short='Conjunctions', title='Conjunctions — Pero, Porque, Aunque',
  subtitle='Join ideas: and, or, but, because, although',
  slides=[
    ('Y / O — and / or', None,
     '<p class="slide-explanation"><b>Y</b> = and, <b>o</b> = or. They change before certain sounds: <b>y → e</b> before i-/hi-, and <b>o → u</b> before o-/ho-.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Carmen y Pedro</b> · <b>padres e hijos</b> (y → e before hi-)</p>'
     '<p style="margin-top:8px"><b>¿Té o café?</b> · <b>¿siete u ocho?</b> (o → u before o-)</p></div>'),
    ('Pero / Sino — but', None,
     '<p class="slide-explanation"><b>Pero</b> = but (adds a contrast). <b>Sino</b> = but rather, only after a negative, correcting it.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Quiero ir, pero no puedo.</b> (I want to go, but I cannot.)</p>'
     '<p style="margin-top:8px"><b>No es lunes, sino martes.</b> (It is not Monday but Tuesday.)</p></div>'),
    ('Porque — because', None,
     '<p class="slide-explanation"><b>Porque</b> answers ¿por qué? Note the difference: <b>¿Por qué?</b> (why, two words) vs <b>porque</b> (because, one word).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Por qué estudias español? — Porque me gusta.</b></p>'
     '<p style="margin-top:8px"><b>No salgo porque llueve.</b> (I am not going out because it is raining.)</p></div>'),
    ('Aunque — although', None,
     '<p class="slide-explanation"><b>Aunque</b> = although / even though. At A2, use it with the indicative for facts.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Aunque llueve, vamos a salir.</b> (Although it is raining, we are going out.)</p>'
     '<p style="margin-top:8px"><b>Me gusta el piso aunque es pequeño.</b> (I like the flat although it is small.)</p></div>'),
    ('Así que / Cuando — so / when', None,
     '<p class="slide-explanation"><b>Así que</b> = so (consequence). <b>Cuando</b> = when (time).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Estaba cansado, así que me fui a casa.</b> (I was tired, so I went home.)</p>'
     '<p style="margin-top:8px"><b>Cuando llego a casa, ceno.</b> (When I get home, I have dinner.)</p></div>'),
  ],
  traps=[
    ('María y Isabel', 'María <strong>e</strong> Isabel', 'Y becomes e before words starting with i- or hi-'),
    ('¿Siete o ocho?', '¿Siete <strong>u</strong> ocho?', 'O becomes u before words starting with o- or ho-'),
    ('No es lunes, pero martes.', 'No es lunes, <strong>sino</strong> martes.', 'Correcting a negative uses sino, not pero'),
    ('No salgo por que llueve.', 'No salgo <strong>porque</strong> llueve.', 'Because is one word: porque. ¿Por qué? (two words) is the question'),
    ('Estaba cansado, aunque me fui a casa.', 'Estaba cansado, <strong>así que</strong> me fui a casa.', 'Consequence = así que; aunque is concession (although)'),
  ],
  summary=[
    ('And', 'y (→ e before i-/hi-)', 'padres e hijos'),
    ('Or', 'o (→ u before o-/ho-)', 'siete u ocho'),
    ('But', 'pero', 'Quiero ir, pero no puedo.'),
    ('But rather', 'sino (after a negative)', 'No es lunes, sino martes.'),
    ('Because', 'porque', 'No salgo porque llueve.'),
    ('Although / So', 'aunque / así que', 'Aunque llueve, salimos.'),
  ],
  ex1=('Choose the conjunction', 'Tap the best option for each sentence.', [
    ('Madres ______ hijas comieron juntas.', ['e', 'y', 'u'], 'e',
     'Hijas starts with i sound (hi-), so y becomes e: madres e hijas.'),
    ('¿Quieres siete ______ ocho?', ['u', 'o', 'y'], 'u',
     'Ocho starts with o-, so o becomes u: siete u ocho.'),
    ('Me gusta el café, ______ prefiero el té.', ['pero', 'sino', 'porque'], 'pero',
     'A simple contrast after a positive clause = pero.'),
    ('No quiero té, ______ café.', ['sino', 'pero', 'aunque'], 'sino',
     'After a negative, the correction "but rather" is sino: no té, sino café.'),
    ('No voy a la fiesta ______ estoy enfermo.', ['porque', 'así que', 'sino'], 'porque',
     'The reason for not going = porque (because) I am ill.'),
    ('Estoy cansado, ______ me voy a dormir.', ['así que', 'aunque', 'sino'], 'así que',
     'Consequence: I am tired, so (así que) I am going to sleep.'),
  ]),
  ex2=('Complete the conjunction', 'Type the missing word — no accents needed.', [
    ('Carmen ______ Ignacio son hermanos. (and, before I-)', 'e',
     'Before Ignacio (i-), y becomes e: Carmen e Ignacio.'),
    ('No estudio frances, ______ aleman. (but rather)', 'sino',
     'Correcting a negative: no francés, sino alemán.'),
    ('Estudio español ______ me encanta. (because)', 'porque',
     'Because is one word: porque me encanta.'),
    ('______ llueve, vamos a salir. (although)', 'aunque',
     'Although it rains, we will go out: aunque llueve.'),
    ('______ llego a casa, ceno. (when)', 'cuando',
     'Time clause: cuando llego a casa, ceno.'),
  ]),
  ex3=('Meaning check', 'Choose the correct option.', [
    ('"¿Por qué?" vs "porque":', ['¿Por qué? asks why; porque answers because', 'Both mean because', 'Both ask why'], '¿Por qué? asks why; porque answers because',
     'Two words with accent = the question why; one word = the answer because.'),
    ('Which needs "sino"?', ['No es caro, ____ barato.', 'Es caro, ____ bueno.', 'Es caro ____ lo compro.'], 'No es caro, ____ barato.',
     'Sino corrects a negative: no es caro, sino barato. The others take pero.'),
    ('"Aunque es pequeño, me gusta" means...', ['Although it is small, I like it.', 'Because it is small, I like it.', 'It is small, so I like it.'], 'Although it is small, I like it.',
     'Aunque introduces a concession — although/even though.'),
    ('Pick the correct change:', ['mujeres u hombres', 'mujeres o hombres', 'mujeres y hombres → e hombres'], 'mujeres u hombres',
     'Before hombres (ho-), o becomes u: mujeres u hombres.'),
    ('"Estaba lloviendo, así que cogí el paraguas" — así que means...', ['so', 'although', 'because'], 'so',
     'Así que introduces the consequence: it was raining, so I took the umbrella.'),
  ]),
  game_desc='Each conjunction passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('y-e', 'y → e', 'and - becomes e before i- or hi- words', 'and, with sound change', 'Carmen <b>e</b> Ignacio son hermanos.', 'Carmen ______ Ignacio son hermanos.', 'e'),
    ('o-u', 'o → u', 'or - becomes u before o- or ho- words', 'or, with sound change', '¿Siete <b>u</b> ocho personas?', '¿Siete ______ ocho personas?', 'u'),
    ('pero', 'pero', 'but - simple contrast', 'plain contrast', 'Quiero ir, <b>pero</b> no puedo.', 'Quiero ir, ______ no puedo.', 'pero'),
    ('sino', 'sino', 'but rather - corrects a negative', 'correcting negative', 'No es lunes, <b>sino</b> martes.', 'No es lunes, ______ martes.', 'sino'),
    ('porque', 'porque', 'because - one word, answers por que', 'reason', 'No salgo <b>porque</b> llueve.', 'No salgo ______ llueve.', 'porque'),
    ('aunque', 'aunque', 'although - concession, indicative at A2', 'concession', '<b>Aunque</b> llueve, vamos a salir.', '______ llueve, vamos a salir.', 'aunque'),
    ('asi-que', 'así que', 'so - introduces a consequence', 'consequence', 'Estaba cansado, <b>así que</b> me fui.', 'Estaba cansado, ______ ______ me fui.', 'asi que'),
    ('cuando', 'cuando', 'when - time clause', 'time link', '<b>Cuando</b> llego a casa, ceno.', '______ llego a casa, ceno.', 'cuando'),
  ],
),

'adverbs-manner': dict(
  num='G1', short='Adverbs of Manner', title='Adverbs of Manner — -mente',
  subtitle='Say how things happen: rápidamente, bien, despacio',
  slides=[
    ('Building -mente adverbs', None,
     '<p class="slide-explanation">Take the <b>feminine</b> form of the adjective and add <b>-mente</b> — like English -ly.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>rápido → rápida → <b>rápidamente</b> (quickly)</p>'
     '<p style="margin-top:8px">lento → lenta → <b>lentamente</b> (slowly)</p>'
     '<p style="margin-top:8px">fácil → <b>fácilmente</b> (easily) — no separate feminine, just add -mente</p></div>'
     '<p style="margin-top:16px">If the adjective has an accent, the adverb keeps it: rápidamente, fácilmente.</p>'),
    ('Bien and mal', None,
     '<p class="slide-explanation">The two most common manner adverbs are irregular: <b>bien</b> (well) and <b>mal</b> (badly). Never "buenamente" for this meaning.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Cocinas muy bien.</b> (You cook very well.)</p>'
     '<p style="margin-top:8px"><b>Dormí mal anoche.</b> (I slept badly last night.)</p></div>'
     '<p style="margin-top:16px">Watch out: bueno/malo are adjectives (describe nouns); bien/mal are adverbs (describe verbs).</p>'),
    ('Despacio and friends', None,
     '<p class="slide-explanation">Some everyday manner adverbs are single words with no -mente.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>despacio</b> (slowly): Habla más despacio, por favor.</p>'
     '<p style="margin-top:8px"><b>deprisa</b> (quickly), <b>alto</b> (loudly), <b>bajo</b> (quietly), <b>claro</b> (clearly)</p></div>'),
    ('Two -mente in a row', None,
     '<p class="slide-explanation">When two -mente adverbs are joined by y/o, only the <b>last</b> one keeps -mente.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Habla lenta y claramente.</b> (He speaks slowly and clearly.)</p></div>'),
    ('Position', None,
     '<p class="slide-explanation">Manner adverbs usually follow the verb (or the whole verb phrase).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Conduce con cuidado / cuidadosamente.</b> (He drives carefully.)</p>'
     '<p style="margin-top:8px"><b>Explicó el problema claramente.</b> (She explained the problem clearly.)</p></div>'),
  ],
  traps=[
    ('rápidomente', '<strong>rápidamente</strong>', 'Use the feminine form of the adjective: rápida + mente'),
    ('Canta muy bueno.', 'Canta muy <strong>bien</strong>.', 'Verbs take the adverb bien, not the adjective bueno'),
    ('Habla lentamente y claramente.', 'Habla <strong>lenta y claramente</strong>.', 'With two adverbs, only the last keeps -mente'),
    ('facilmente (no accent)', '<strong>fácilmente</strong>', 'The adverb keeps the accent of the original adjective'),
    ('Conduce despacio... ¿despaciamente?', '<strong>despacio</strong> is already an adverb', 'Despacio, deprisa, alto, bajo need no -mente'),
  ],
  summary=[
    ('Formation', 'feminine adjective + -mente', 'rápida → rápidamente'),
    ('Well / badly', 'bien / mal (irregular)', 'Cocinas bien. Dormí mal.'),
    ('No -mente needed', 'despacio, deprisa, alto, bajo', 'Habla más despacio.'),
    ('Two in a row', 'first loses -mente', 'lenta y claramente'),
    ('Accent', 'kept from the adjective', 'fácil → fácilmente'),
  ],
  ex1=('Choose the correct adverb', 'Tap the best option for each sentence.', [
    ('El tren pasó ______ . (quickly)', ['rápidamente', 'rápidomente', 'rápidamento'], 'rápidamente',
     'Feminine rápida + mente = rápidamente.'),
    ('Mi abuela cocina muy ______ .', ['bien', 'buena', 'bueno'], 'bien',
     'Cooking is a verb — it needs the adverb bien, not the adjective bueno/buena.'),
    ('Habla más ______ , por favor — no entiendo.', ['despacio', 'despaciamente', 'lentamenta'], 'despacio',
     'Despacio is already an adverb; it never takes -mente.'),
    ('Explicó todo lenta y ______ .', ['claramente', 'clara', 'claramenta'], 'claramente',
     'With two linked adverbs, only the last keeps -mente: lenta y claramente.'),
    ('Anoche dormí ______ . (badly)', ['mal', 'malo', 'mala'], 'mal',
     'Sleeping badly = the adverb mal. Malo is an adjective for nouns.'),
    ('Resolvió el problema ______ . (easily)', ['fácilmente', 'facilamente', 'fácilamente'], 'fácilmente',
     'Fácil has one form; just add -mente and keep the accent: fácilmente.'),
  ]),
  ex2=('Build the adverb', 'Type the -mente adverb formed from the adjective — accents optional here.', [
    ('lento → ______ (slowly)', 'lentamente',
     'Feminine lenta + mente = lentamente.'),
    ('tranquilo → ______ (calmly)', 'tranquilamente',
     'Tranquila + mente = tranquilamente.'),
    ('perfecto → ______ (perfectly)', 'perfectamente',
     'Perfecta + mente = perfectamente.'),
    ('normal → ______ (normally)', 'normalmente',
     'Adjectives in -l have one form: normal + mente.'),
    ('claro → ______ (clearly)', 'claramente',
     'Clara + mente = claramente.'),
  ]),
  ex3=('Usage check', 'Choose the correct option.', [
    ('Bien vs bueno:', ['bien modifies verbs; bueno modifies nouns', 'they are interchangeable', 'bueno modifies verbs'], 'bien modifies verbs; bueno modifies nouns',
     'Canta bien (verb) vs un buen cantante (noun).'),
    ('Which is WRONG?', ['Habla altamente.', 'Habla alto.', 'Habla claramente.'], 'Habla altamente.',
     'For volume, Spanish uses alto as an adverb. Altamente exists but means "highly" (altamente recomendable).'),
    ('"Conduce con cuidado" could also be...', ['cuidadosamente', 'cuidadomente', 'cuidadamenta'], 'cuidadosamente',
     'Cuidadoso → cuidadosa + mente = cuidadosamente.'),
    ('Pick the correct pair:', ['rápida y eficazmente', 'rápidamente y eficazmente', 'rápida y eficaz'], 'rápida y eficazmente',
     'Only the final adverb keeps -mente when two are joined.'),
    ('"Lo hizo mal" means...', ['He did it badly.', 'He did something bad.', 'He is bad.'], 'He did it badly.',
     'Mal is the adverb describing how he did it.'),
  ]),
  game_desc='Each adverb passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('rapidamente', 'rápidamente', 'quickly - from feminine rapida + mente', 'quickly', 'El tren pasó <b>rápidamente</b>.', 'El tren pasó ______ . (quickly)', 'rapidamente'),
    ('lentamente', 'lentamente', 'slowly - from lenta + mente', 'slowly', 'Camina <b>lentamente</b> por el parque.', 'Camina ______ por el parque. (slowly)', 'lentamente'),
    ('bien', 'bien', 'well - irregular adverb of manner', 'well', 'Mi abuela cocina muy <b>bien</b>.', 'Mi abuela cocina muy ______ .', 'bien'),
    ('mal', 'mal', 'badly - irregular adverb of manner', 'badly', 'Anoche dormí <b>mal</b>.', 'Anoche dormí ______ .', 'mal'),
    ('despacio', 'despacio', 'slowly - single-word adverb, no -mente', 'slowly (one word)', 'Habla más <b>despacio</b>, por favor.', 'Habla más ______ , por favor.', 'despacio'),
    ('facilmente', 'fácilmente', 'easily - keeps the accent of facil', 'easily', 'Resolvió el problema <b>fácilmente</b>.', 'Resolvió el problema ______ . (easily)', 'facilmente'),
    ('claramente', 'claramente', 'clearly - from clara + mente', 'clearly', 'Explicó todo <b>claramente</b>.', 'Explicó todo ______ . (clearly)', 'claramente'),
    ('lenta-y', 'lenta y claramente', 'slowly and clearly - first adverb drops -mente', 'paired adverbs', 'Habla <b>lenta y claramente</b>.', 'Habla ______ y claramente. (slowly)', 'lenta'),
  ],
),

'word-order': dict(
  num='G19', short='Word Order', title='Word Order — El Orden de las Palabras',
  subtitle='Build natural Spanish sentences',
  slides=[
    ('Basic order: like English, but flexible', None,
     '<p class="slide-explanation">Neutral Spanish order is Subject–Verb–Object, like English — but the subject is often dropped because the verb ending shows it.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>(Yo) compro pan los sábados.</b> (I buy bread on Saturdays.)</p>'
     '<p style="margin-top:8px"><b>María lee el periódico.</b> (María reads the newspaper.)</p></div>'),
    ('Adjectives go after the noun', None,
     '<p class="slide-explanation">Unlike English, descriptive adjectives normally <b>follow</b> the noun.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>un coche rojo</b> (a red car) · <b>una ciudad antigua</b> (an old city)</p>'
     '<p style="margin-top:8px">Exceptions before the noun: numbers and quantity words — <b>dos coches, muchos libros, buen día</b>.</p></div>'),
    ('Negation: no before the verb', None,
     '<p class="slide-explanation">Negation is simple: put <b>no</b> directly before the verb (and before any object pronoun).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>No tengo hambre.</b> (I am not hungry.)</p>'
     '<p style="margin-top:8px"><b>No lo conozco.</b> (I do not know him.)</p></div>'),
    ('Questions: just flip or just ask', None,
     '<p class="slide-explanation">Spanish questions need no auxiliary "do". Either invert verb and subject, or keep the order and use intonation — plus the opening ¿.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Habla usted inglés?</b> (Do you speak English?)</p>'
     '<p style="margin-top:8px"><b>¿Tú vienes mañana?</b> (Are you coming tomorrow?) — same order, rising tone</p>'
     '<p style="margin-top:8px"><b>¿Dónde vive Juan?</b> (Where does Juan live?) — question word first</p></div>'),
    ('Frequency words', None,
     '<p class="slide-explanation">Adverbs like siempre, nunca, a veces usually go before the verb or at the start.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Siempre desayuno a las ocho.</b> (I always have breakfast at eight.)</p>'
     '<p style="margin-top:8px"><b>Nunca como carne.</b> = <b>No como carne nunca.</b> (I never eat meat.)</p></div>'),
  ],
  traps=[
    ('un rojo coche', 'un coche <strong>rojo</strong>', 'Descriptive adjectives follow the noun in Spanish'),
    ('¿Do tú hablas español?', '¿<strong>Hablas</strong> español?', 'Spanish has no auxiliary do — the verb asks the question alone'),
    ('Tengo no hambre.', '<strong>No tengo</strong> hambre.', 'No goes immediately before the verb'),
    ('¿Dónde Juan vive?', '¿Dónde <strong>vive Juan</strong>?', 'After a question word, the verb comes before the subject'),
    ('Como nunca carne.', '<strong>Nunca como</strong> carne.', 'Nunca goes before the verb (or no...nunca around it)'),
  ],
  summary=[
    ('Neutral order', 'Subject–Verb–Object (subject often dropped)', 'María lee el periódico.'),
    ('Adjectives', 'after the noun', 'un coche rojo'),
    ('Negation', 'no + (pronoun) + verb', 'No lo conozco.'),
    ('Yes/no questions', 'verb first or intonation', '¿Hablas inglés?'),
    ('Wh- questions', '¿Question word + verb + subject?', '¿Dónde vive Juan?'),
    ('Frequency', 'before the verb', 'Siempre desayuno a las ocho.'),
  ],
  ex1=('Choose the correct order', 'Tap the option with natural Spanish word order.', [
    ('A red car is...', ['un coche rojo', 'un rojo coche', 'rojo un coche'], 'un coche rojo',
     'Descriptive adjectives follow the noun: un coche rojo.'),
    ('"I do not know him" is...', ['No lo conozco.', 'Lo no conozco.', 'Conozco no lo.'], 'No lo conozco.',
     'No + object pronoun + verb: no lo conozco.'),
    ('"Where does María work?" is...', ['¿Dónde trabaja María?', '¿Dónde María trabaja?', '¿María dónde trabaja?'], '¿Dónde trabaja María?',
     'After the question word, verb before subject: ¿Dónde trabaja María?'),
    ('"I never drink coffee" is...', ['Nunca bebo café.', 'Bebo nunca café.', 'Bebo café no nunca.'], 'Nunca bebo café.',
     'Nunca precedes the verb (or no bebo café nunca).'),
    ('"Do you speak English?" is...', ['¿Hablas inglés?', '¿Haces hablar inglés?', '¿Do hablas inglés?'], '¿Hablas inglés?',
     'No auxiliary needed: the conjugated verb alone asks the question.'),
    ('"Many books" is...', ['muchos libros', 'libros muchos', 'mucho libros'], 'muchos libros',
     'Quantity words go before the noun and agree: muchos libros.'),
  ]),
  ex2=('Put it in order', 'Type the correct word for the gap — no accents needed.', [
    ('______ tengo tiempo hoy. (not)', 'no',
     'Negation goes first: No tengo tiempo.'),
    ('Es una ciudad ______ . (beautiful → bonita, after the noun)', 'bonita',
     'The adjective follows: una ciudad bonita.'),
    ('¿______ vives? (where)', 'donde',
     'Question word first: ¿Dónde vives? (accent optional in your answer).'),
    ('______ desayuno a las ocho. (always)', 'siempre',
     'Frequency adverb before the verb: Siempre desayuno.'),
    ('¿Hablas ______ ? (Spanish — language after verb)', 'espanol',
     'Verb + object: ¿Hablas español?'),
  ]),
  ex3=('Spot the correct sentence', 'Choose the correct option.', [
    ('Pick the natural sentence:', ['María compró un vestido nuevo.', 'María un vestido nuevo compró.', 'Compró María un nuevo vestido a.'], 'María compró un vestido nuevo.',
     'Subject–verb–object with the adjective after the noun.'),
    ('Why can Spanish drop "yo" in "Compro pan"?', ['the verb ending already shows the subject', 'subjects are optional everywhere in any language', 'pan is the subject'], 'the verb ending already shows the subject',
     'Compro can only be yo — the ending -o carries the subject.'),
    ('Which question is WRONG?', ['¿Qué tú quieres decir do?', '¿Qué quieres decir?', '¿Tú qué quieres decir?'], '¿Qué tú quieres decir do?',
     'There is no do in Spanish questions; the other two orders are both heard.'),
    ('"No como carne nunca" is...', ['correct — double negative is fine', 'wrong — two negatives cancel', 'only correct in writing'], 'correct — double negative is fine',
     'Spanish allows (and often requires) double negation: no...nunca.'),
    ('"Un buen día" shows that...', ['some short adjectives can precede the noun', 'all adjectives precede the noun', 'buen is a noun'], 'some short adjectives can precede the noun',
     'Bueno shortens to buen before a masculine noun and may precede it.'),
  ]),
  game_desc='Each word-order rule passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('adj-after', 'noun + adjective', 'descriptive adjectives follow the noun', 'adjective position', 'Tiene un coche <b>rojo</b>.', 'Tiene un coche ______ . (red)', 'rojo'),
    ('no-verb', 'no + verb', 'negation goes right before the verb', 'negation order', '<b>No tengo</b> hambre.', '______ tengo hambre. (not)', 'no'),
    ('no-pronoun', 'no + pronoun + verb', 'no precedes object pronouns too', 'negation with pronoun', '<b>No lo</b> conozco.', '______ lo conozco. (not)', 'no'),
    ('q-no-do', 'verb-first question', 'questions need no auxiliary do', 'question formation', '¿<b>Hablas</b> inglés?', '¿______ inglés? (do you speak)', 'hablas'),
    ('q-word', 'question word + verb + subject', 'wh-questions invert verb and subject', 'wh-question order', '¿Dónde <b>vive Juan</b>?', '¿Dónde ______ Juan? (lives)', 'vive'),
    ('drop-subject', 'dropped subject', 'verb endings make subject pronouns optional', 'null subject', '<b>Compro</b> pan los sábados.', '______ pan los sábados. (I buy)', 'compro'),
    ('siempre', 'siempre + verb', 'frequency adverbs precede the verb', 'frequency position', '<b>Siempre</b> desayuno a las ocho.', '______ desayuno a las ocho. (always)', 'siempre'),
    ('doble-neg', 'no ... nunca', 'double negation is correct Spanish', 'double negative', '<b>No</b> como carne <b>nunca</b>.', 'No como carne ______ . (never)', 'nunca'),
  ],
),

'indirect-questions': dict(
  num='G7', short='Indirect Questions', title='Indirect Questions — ¿Sabes dónde...?',
  subtitle='Ask politely inside another sentence',
  slides=[
    ('What is an indirect question?', None,
     '<p class="slide-explanation">Wrap a question inside a polite frame: ¿Sabes...? (Do you know...?), Me pregunto... (I wonder...), No sé... (I do not know...).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Direct: <b>¿Dónde está el banco?</b></p>'
     '<p style="margin-top:8px">Indirect: <b>¿Sabes dónde está el banco?</b> (Do you know where the bank is?)</p></div>'
     '<p style="margin-top:16px">Good news: the word order inside does not change, and question words keep their accents.</p>'),
    ('With question words', None,
     '<p class="slide-explanation">Dónde, cuándo, qué, quién, cómo, cuánto keep their <b>accents</b> in indirect questions.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>No sé cuándo llega el tren.</b> (I do not know when the train arrives.)</p>'
     '<p style="margin-top:8px"><b>Me pregunto qué hora es.</b> (I wonder what time it is.)</p>'
     '<p style="margin-top:8px"><b>¿Puedes decirme cómo funciona?</b> (Can you tell me how it works?)</p></div>'),
    ('Yes/no questions: si', None,
     '<p class="slide-explanation">When there is no question word, use <b>si</b> (if/whether) — without accent.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Direct: <b>¿Viene Juan?</b> → Indirect: <b>No sé si viene Juan.</b> (I do not know if Juan is coming.)</p>'
     '<p style="margin-top:8px"><b>Me pregunto si está abierto.</b> (I wonder whether it is open.)</p></div>'),
    ('Polite frames', None,
     '<p class="slide-explanation">The most useful openers for sounding polite in shops, stations and offices:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Sabes/Sabe usted...?</b> · <b>¿Puedes/Puede decirme...?</b> · <b>¿Podrías decirme...?</b></p>'
     '<p style="margin-top:8px"><b>¿Podría decirme dónde está la salida?</b> (Could you tell me where the exit is?)</p></div>'),
    ('Statements inside: que', None,
     '<p class="slide-explanation">Do not confuse indirect questions with reported statements, which use <b>que</b>: Dice que viene. (He says he is coming.)</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Pregunta si vienes.</b> (He asks if you are coming.) — question → si</p>'
     '<p style="margin-top:8px"><b>Dice que vienes.</b> (He says you are coming.) — statement → que</p></div>'),
  ],
  traps=[
    ('No sé donde está. (no accent)', 'No sé <strong>dónde</strong> está.', 'Question words keep their accent in indirect questions'),
    ('Me pregunto que hora es.', 'Me pregunto <strong>qué</strong> hora es.', 'Qué keeps its accent when it asks something'),
    ('No sé si que viene.', 'No sé <strong>si</strong> viene.', 'Use si alone for yes/no indirect questions — never si que'),
    ('¿Sabes dónde está el banco? → ...where is the bank? order', '¿Sabes dónde <strong>está el banco</strong>?', 'Spanish keeps the same order; do not copy English "where the bank is" puzzles'),
    ('Dice si viene mañana. (statement)', 'Dice <strong>que</strong> viene mañana.', 'Statements use que; si is only for asking whether'),
  ],
  summary=[
    ('Frame + question word', '¿Sabes dónde/cuándo/qué...?', '¿Sabes dónde está el banco?'),
    ('Accents', 'kept on question words', 'No sé cuándo llega.'),
    ('Yes/no', 'si (no accent)', 'No sé si viene Juan.'),
    ('Polite ask', '¿Podría decirme...?', '¿Podría decirme dónde está la salida?'),
    ('Statement vs question', 'que vs si', 'Dice que viene. / Pregunta si viene.'),
  ],
  ex1=('Choose the correct option', 'Tap the best option for each sentence.', [
    ('¿Sabes ______ está la estación?', ['dónde', 'donde', 'si'], 'dónde',
     'The question word keeps its accent inside: ¿Sabes dónde está...?'),
    ('No sé ______ viene a la fiesta. (if)', ['si', 'sí', 'que'], 'si',
     'Yes/no indirect questions use si without accent. Sí with accent means yes.'),
    ('Me pregunto ______ hora es.', ['qué', 'que', 'cuál'], 'qué',
     'Asking what time = qué with accent: me pregunto qué hora es.'),
    ('¿Puedes decirme ______ funciona esta máquina?', ['cómo', 'como', 'si cómo'], 'cómo',
     'How = cómo with accent, directly after the polite frame.'),
    ('No sé ______ cuesta el billete.', ['cuánto', 'cuanto', 'que'], 'cuánto',
     'How much = cuánto, accent kept: no sé cuánto cuesta.'),
    ('Dice ______ llega mañana. (a statement)', ['que', 'si', 'qué'], 'que',
     'Reported statement → que: dice que llega mañana.'),
  ]),
  ex2=('Make it indirect', 'Type the missing connector — accents optional in your answers.', [
    ('¿Viene Ana? → No sé ______ viene Ana.', 'si',
     'A yes/no question becomes si (whether): no sé si viene Ana.'),
    ('¿Dónde está el baño? → ¿Puede decirme ______ está el baño?', 'donde',
     'The question word transfers directly: dónde (accent kept in writing).'),
    ('¿Cuándo sale el tren? → Me pregunto ______ sale el tren.', 'cuando',
     'Me pregunto cuándo sale el tren — accent on cuándo in proper writing.'),
    ('¿Quién es ese hombre? → No sé ______ es ese hombre.', 'quien',
     'No sé quién es — quién keeps its accent as a question word.'),
    ('¿Está abierta la tienda? → Me pregunto ______ está abierta.', 'si',
     'No question word → si: me pregunto si está abierta.'),
  ]),
  ex3=('Meaning check', 'Choose the correct option.', [
    ('"¿Sabes si hay un banco cerca?" asks...', ['whether there is a bank nearby', 'where the bank is', 'when the bank opens'], 'whether there is a bank nearby',
     'Si introduces a yes/no question: whether there is a bank nearby.'),
    ('Which is more polite?', ['¿Podría decirme dónde está la salida?', '¿Dónde está la salida?', 'Dime dónde está la salida.'], '¿Podría decirme dónde está la salida?',
     'The conditional podría + decirme is the politest frame.'),
    ('Que or si: "He asks ___ you are coming."', ['si', 'que', 'qué'], 'si',
     'Asking whether = si: pregunta si vienes.'),
    ('Why does dónde keep the accent in "No sé dónde está"?', ['it is still a question word', 'all words keep accents', 'sé requires it'], 'it is still a question word',
     'Indirect questions keep the interrogative force, so the accent stays.'),
    ('Which is WRONG?', ['No sé si que viene.', 'No sé si viene.', 'No sé cuándo viene.'], 'No sé si que viene.',
     'Si and que never combine — si alone introduces the indirect yes/no question.'),
  ]),
  game_desc='Each indirect-question pattern passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('sabes-donde', '¿Sabes dónde...?', 'do you know where - polite location question', 'polite where', '¿<b>Sabes dónde</b> está el banco?', '¿Sabes ______ está el banco?', 'donde'),
    ('no-se-si', 'no sé si', 'I do not know whether - yes/no indirect', 'whether clause', '<b>No sé si</b> viene Juan.', 'No sé ______ viene Juan.', 'si'),
    ('me-pregunto', 'me pregunto', 'I wonder - reflective frame', 'I wonder', '<b>Me pregunto</b> qué hora es.', 'Me ______ qué hora es. (I wonder)', 'pregunto'),
    ('puede-decirme', '¿Puede decirme...?', 'can you tell me - polite request frame', 'polite frame', '¿<b>Puede decirme</b> cómo funciona?', '¿Puede ______ cómo funciona? (tell me)', 'decirme'),
    ('cuando-acc', 'cuándo', 'when - keeps its accent in indirect questions', 'when, accented', 'No sé <b>cuándo</b> llega el tren.', 'No sé ______ llega el tren. (when)', 'cuando'),
    ('cuanto-acc', 'cuánto', 'how much - keeps its accent', 'how much', 'No sé <b>cuánto</b> cuesta.', 'No sé ______ cuesta. (how much)', 'cuanto'),
    ('que-statement', 'dice que', 'says that - statements take que, not si', 'reported statement', '<b>Dice que</b> viene mañana.', 'Dice ______ viene mañana. (that)', 'que'),
    ('podria-decirme', '¿Podría decirme...?', 'could you tell me - the politest frame', 'politest frame', '¿<b>Podría decirme</b> dónde está la salida?', '¿______ decirme dónde está la salida? (could you)', 'podria'),
  ],
),
}
