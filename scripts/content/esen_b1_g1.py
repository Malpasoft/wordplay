# -*- coding: utf-8 -*-
"""espanol-en B1 grammar content — batch 1 (chapters G1-G5)."""

CHAPTERS = {

'adverbs-frequency': dict(
  num='G1', short='Adverbs of Frequency', title='Adverbs of Frequency — Adverbios de Frecuencia',
  subtitle='Say how often: siempre, a menudo, a veces, casi nunca, nunca',
  slides=[
    ('The frequency scale', None,
     '<p class="slide-explanation">Five adverbs cover the whole scale from always to never: <b>siempre</b>, <b>a menudo</b>, <b>a veces</b>, <b>casi nunca</b>, <b>nunca</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Siempre</b> desayuno a las ocho. (I always have breakfast at eight.)</p>'
     '<p style="margin-top:8px">Veo a mis primos <b>a menudo</b>. (I see my cousins often.)</p>'
     '<p style="margin-top:8px"><b>A veces</b> vamos al cine. (Sometimes we go to the cinema.)</p></div>'
     '<p style="margin-top:16px">Learn them as a ladder: siempre → casi siempre → a menudo → a veces → casi nunca → nunca.</p>'),
    ('Position is flexible', None,
     '<p class="slide-explanation">English locks frequency adverbs into mid-position (I <b>always</b> get up early). Spanish is more relaxed: before the verb, after the verb, or at the start or end of the sentence.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Siempre llego pronto.</b> = <b>Llego pronto siempre.</b> (I always arrive early.)</p>'
     '<p style="margin-top:8px"><b>A veces como fuera.</b> = <b>Como fuera a veces.</b> (Sometimes I eat out.)</p></div>'
     '<p style="margin-top:16px">The phrase adverbs <b>a menudo</b> and <b>a veces</b> sound most natural at the start or the end.</p>'),
    ('Nunca and the double negative', None,
     '<p class="slide-explanation">Here is the rule English speakers resist: when <b>nunca</b> comes after the verb, Spanish <b>requires</b> a double negative with <b>no</b>. It is not sloppy — it is compulsory.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>No voy nunca al teatro.</b> (I never go to the theatre.) — no + verb + nunca</p>'
     '<p style="margin-top:8px"><b>Nunca voy al teatro.</b> (Same meaning.) — nunca before the verb, no extra no</p></div>'
     '<p style="margin-top:16px">Two negatives do not cancel out in Spanish. "No voy nunca" is the only correct way to say it with nunca after the verb.</p>'),
    ('Casi — almost', None,
     '<p class="slide-explanation"><b>Casi</b> (almost) glues onto siempre and nunca to soften them: <b>casi siempre</b> (almost always), <b>casi nunca</b> (hardly ever).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Casi siempre</b> ceno en casa. (I almost always have dinner at home.)</p>'
     '<p style="margin-top:8px"><b>Casi nunca</b> como carne. (I hardly ever eat meat.)</p>'
     '<p style="margin-top:8px">No veo la tele <b>casi nunca</b>. (I hardly ever watch TV.) — double negative again</p></div>'),
    ('Asking how often', None,
     '<p class="slide-explanation">The question is <b>¿Con qué frecuencia...?</b> (How often...?). Typical answers use <b>vez/veces</b> (time/times).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Con qué frecuencia vas al gimnasio?</b> (How often do you go to the gym?)</p>'
     '<p style="margin-top:8px"><b>Una vez a la semana.</b> (Once a week.)</p>'
     '<p style="margin-top:8px"><b>Dos veces al mes.</b> (Twice a month.)</p></div>'
     '<p style="margin-top:16px">Note the pattern: una vez / dos veces + <b>a la</b> semana, <b>al</b> mes, <b>al</b> año.</p>'),
  ],
  traps=[
    ('Voy nunca al gimnasio.', '<strong>No</strong> voy <strong>nunca</strong> al gimnasio.', 'When nunca follows the verb, the no before the verb is compulsory'),
    ('Nunca no voy al cine.', '<strong>Nunca voy</strong> al cine.', 'When nunca comes first, it works alone — no extra no'),
    ('Siempre no llego tarde.', '<strong>Nunca llego</strong> tarde.', 'To say never, use nunca — "siempre no" is not how Spanish negates'),
    ('Casi yo nunca bebo café.', 'Yo <strong>casi nunca</strong> bebo café.', 'Casi sticks directly to nunca: casi nunca is one unit'),
    ('¿Qué frecuencia vas al gimnasio?', '¿<strong>Con qué frecuencia</strong> vas al gimnasio?', 'The how-often question needs con: con qué frecuencia'),
  ],
  summary=[
    ('Always', 'siempre', 'Siempre desayuno a las ocho.'),
    ('Often', 'a menudo', 'Veo a mis primos a menudo.'),
    ('Sometimes', 'a veces', 'A veces vamos al cine.'),
    ('Hardly ever', 'casi nunca', 'Casi nunca como carne.'),
    ('Never (before verb)', 'nunca + verb', 'Nunca llego tarde.'),
    ('Never (after verb)', 'no + verb + nunca', 'No voy nunca al teatro.'),
  ],
  ex1=('Choose the correct adverb', 'Tap the best option for each sentence.', [
    ('No como carne ______. (never)', ['nunca', 'siempre', 'a veces'], 'nunca',
     'With the adverb after the verb, Spanish demands the double negative: no como nunca. The other options clash with the no.'),
    ('______ voy al gimnasio — no me gusta nada. (never, before the verb)', ['Nunca', 'No nunca', 'Nunca no'], 'Nunca',
     'Before the verb, nunca stands alone: Nunca voy. Adding no before or after it is wrong in this position.'),
    ('Vemos a los abuelos muy ______. (often)', ['a menudo', 'a veces', 'casi nunca'], 'a menudo',
     'Often = a menudo. A veces is only sometimes, and casi nunca is hardly ever.'),
    ('______ nunca llego tarde — solo una o dos veces al año. (almost)', ['Casi', 'Muy', 'No'], 'Casi',
     'Once or twice a year = hardly ever = casi nunca. Muy never combines with nunca, and No would need the verb first.'),
    ('¿______ qué frecuencia estudias español?', ['Con', 'De', 'En'], 'Con',
     'The fixed question is ¿Con qué frecuencia...? — only con works here.'),
    ('Voy a la piscina dos ______ a la semana. (twice a week)', ['veces', 'vez', 'tiempos'], 'veces',
     'Two times = dos veces (plural of vez). Tiempo means time as a concept, not an occasion.'),
  ]),
  ex2=('Write the frequency word', 'Type the missing word — no accents needed in these answers.', [
    ('No voy ______ al teatro. (never — after the verb)', 'nunca',
     'After the verb, never = nunca, and the no before the verb stays: no voy nunca.'),
    ('______ desayuno a las ocho. (always)', 'siempre',
     'Always = siempre. Before the verb is its most common home.'),
    ('Vamos al cine a ______. (sometimes: a ...)', 'veces',
     'Sometimes = a veces — literally "at times".'),
    ('Veo a mis primos muy a ______. (often: a ...)', 'menudo',
     'Often = a menudo. It is a two-word phrase, like a veces.'),
    ('______ nunca como pescado. (almost never)', 'casi',
     'Hardly ever = casi nunca — casi (almost) softens nunca.'),
  ]),
  ex3=('Usage and meaning', 'Choose the correct option.', [
    ('Which is correct?', ['No voy nunca al teatro.', 'Voy nunca al teatro.', 'No voy siempre nunca al teatro.'], 'No voy nunca al teatro.',
     'Nunca after the verb requires no before it. Without the no it is wrong, and siempre cannot join in.'),
    ('Which is WRONG?', ['Nunca no como pescado.', 'Nunca como pescado.', 'No como nunca pescado.'], 'Nunca no como pescado.',
     'When nunca opens the sentence it replaces the no — you never use both in that order.'),
    ('"Casi nunca" means...', ['almost never', 'almost always', 'sometimes'], 'almost never',
     'Casi = almost, nunca = never: casi nunca = almost never / hardly ever.'),
    ('Where can "a veces" go?', ['at the start or the end of the sentence', 'only between subject and verb', 'only at the very end'], 'at the start or the end of the sentence',
     'Spanish frequency phrases are flexible — a veces sounds natural at either end of the sentence.'),
    ('¿Vas mucho al cine? — The natural "hardly ever" reply is...', ['No, casi nunca.', 'No, casi siempre.', 'Sí, nunca.'], 'No, casi nunca.',
     'Hardly ever = casi nunca. Casi siempre means almost always, and sí + nunca contradicts itself.'),
  ]),
  game_desc='Each frequency adverb passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('siempre', 'siempre', 'always', 'every single time', '<b>Siempre</b> desayuno a las ocho.', '______ desayuno a las ocho. (always)', 'siempre'),
    ('a-menudo', 'a menudo', 'often', 'frequently', 'Veo a mis primos <b>a menudo</b>.', 'Veo a mis primos a ______. (often)', 'menudo'),
    ('a-veces', 'a veces', 'sometimes', 'occasionally', '<b>A veces</b> vamos al cine.', 'A ______ vamos al cine. (sometimes)', 'veces'),
    ('casi-nunca', 'casi nunca', 'hardly ever - almost plus never', 'almost never', '<b>Casi nunca</b> como carne.', '______ nunca como carne. (almost)', 'casi'),
    ('nunca', 'nunca', 'never - stands alone before the verb', 'never, before the verb', '<b>Nunca</b> llego tarde.', '______ llego tarde. (never)', 'nunca'),
    ('no-nunca', 'no ... nunca', 'never - the compulsory double negative after the verb', 'double negative', '<b>No</b> voy <b>nunca</b> al teatro.', '______ voy nunca al teatro. (the compulsory first negative)', 'no'),
    ('casi-siempre', 'casi siempre', 'almost always', 'nearly always', '<b>Casi siempre</b> ceno en casa.', '______ ______ ceno en casa. (almost always)', 'casi siempre'),
    ('una-vez', 'una vez a la semana', 'once a week - a typical frequency answer', 'weekly', 'Voy al gimnasio <b>una vez a la semana</b>.', 'Voy al gimnasio una ______ a la semana. (once: one ...)', 'vez'),
  ],
),

'adverbs-manner': dict(
  num='G2', short='Adverbs of Manner', title='Adverbs of Manner — Adverbios de Modo',
  subtitle='Say how things are done: lentamente, bien, mal',
  slides=[
    ('Building -mente adverbs', None,
     '<p class="slide-explanation">English adds <b>-ly</b>; Spanish adds <b>-mente</b> — but always to the <b>feminine</b> form of the adjective.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>lento → lenta → lentamente</b> (slowly)</p>'
     '<p style="margin-top:8px"><b>tranquilo → tranquila → tranquilamente</b> (calmly)</p>'
     '<p style="margin-top:8px"><b>fácil → fácilmente</b> (easily) — adjectives without a separate feminine just add -mente</p></div>'),
    ('The accent survives', None,
     '<p class="slide-explanation">If the adjective has a written accent, the adverb <b>keeps it</b> in the same place — -mente never steals the accent.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>rápido → rápida → rápidamente</b> (quickly)</p>'
     '<p style="margin-top:8px"><b>fácil → fácilmente</b> (easily)</p>'
     '<p style="margin-top:8px"><b>Ella conduce rápidamente.</b> (She drives quickly.)</p></div>'
     '<p style="margin-top:16px">Result: -mente adverbs are the rare Spanish words with two stressed syllables — RÁ-pida-MEN-te.</p>'),
    ('Bien and mal — the irregulars', None,
     '<p class="slide-explanation">Bueno and malo do not take -mente. Their adverbs are <b>bien</b> (well) and <b>mal</b> (badly) — exactly like English good → well.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Mi hermana cocina muy bien.</b> (My sister cooks very well.)</p>'
     '<p style="margin-top:8px"><b>Hoy he dormido mal.</b> (I slept badly today.)</p></div>'
     '<p style="margin-top:16px">Never say "canta bueno" — just as you would never say "she sings good" in careful English.</p>'),
    ('Two -mente adverbs in a row', None,
     '<p class="slide-explanation">When two manner adverbs are joined by <b>y</b>, only the <b>last</b> one takes -mente. The first stays in its feminine adjective form.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Habla lenta y claramente.</b> (He speaks slowly and clearly.)</p>'
     '<p style="margin-top:8px"><b>Trabaja rápida y eficazmente.</b> (She works quickly and efficiently.)</p></div>'
     '<p style="margin-top:16px">English repeats -ly on both words; Spanish trims the first one. It is elegant once you expect it.</p>'),
    ('Adjective or adverb?', None,
     '<p class="slide-explanation">Adjectives describe nouns and <b>agree</b> with them. Adverbs describe verbs and <b>never change</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Ella es una conductora rápida.</b> (She is a fast driver.) — adjective, agrees</p>'
     '<p style="margin-top:8px"><b>Ella conduce rápidamente.</b> (She drives quickly.) — adverb, invariable</p></div>'
     '<p style="margin-top:16px">If the word answers "how is it done?", you want the adverb.</p>'),
  ],
  traps=[
    ('Habla lentomente.', 'Habla <strong>lentamente</strong>.', '-mente attaches to the feminine form: lenta + mente'),
    ('Canta muy bueno.', 'Canta muy <strong>bien</strong>.', 'Bueno is the adjective; the adverb of manner is bien'),
    ('Cocina muy malo.', 'Cocina muy <strong>mal</strong>.', 'Malo is the adjective; with a verb you need mal'),
    ('Habla lentamente y claramente.', 'Habla <strong>lenta y claramente</strong>.', 'With two adverbs joined by y, only the last keeps -mente'),
    ('Ella conduce rapidamente.', 'Ella conduce <strong>rápidamente</strong>.', 'The adjective keeps its written accent: rápida → rápidamente'),
  ],
  summary=[
    ('Formation', 'feminine adjective + mente', 'lenta → lentamente'),
    ('Accent kept', 'rápida → rápidamente', 'Conduce rápidamente.'),
    ('Well', 'bien (never "buenamente")', 'Cocina muy bien.'),
    ('Badly', 'mal', 'He dormido mal.'),
    ('Two in a row', 'adj. fem. + y + adverb-mente', 'lenta y claramente'),
    ('Adj vs adverb', 'adjective agrees; adverb never changes', 'conductora rápida / conduce rápidamente'),
  ],
  ex1=('Choose the correct form', 'Tap the best option for each sentence.', [
    ('Habla muy ______. (slowly)', ['lentamente', 'lentomente', 'lentamenta'], 'lentamente',
     'The base is the feminine lenta + mente = lentamente. -mente never attaches to the masculine lento.'),
    ('Mi hermana cocina muy ______. (well)', ['bien', 'buena', 'buenamente'], 'bien',
     'The adverb of bueno is the irregular bien. Buena is an adjective and "buenamente" is not used for skill.'),
    ('fácil → ______', ['fácilmente', 'facilamente', 'fácilamente'], 'fácilmente',
     'Fácil has no separate feminine, so just add -mente — and keep the accent: fácilmente.'),
    ('Explica las cosas lenta y ______. (clearly)', ['claramente', 'clara', 'claro'], 'claramente',
     'With two adverbs joined by y, the last one carries the -mente: lenta y claramente.'),
    ('El equipo jugó muy ______. (badly)', ['mal', 'malo', 'mala'], 'mal',
     'How they played = adverb mal. Malo/mala are adjectives and would need a noun to describe.'),
    ('rápido → ______', ['rápidamente', 'rapidomente', 'rápidomente'], 'rápidamente',
     'Feminine first (rápida), then -mente, keeping the accent: rápidamente.'),
  ]),
  ex2=('Build the adverb', 'Type the missing word — no accents needed in these answers.', [
    ('lenta → ______ (form the adverb)', 'lentamente',
     'Feminine adjective + mente: lenta + mente = lentamente.'),
    ('Mi abuela cocina muy ______. (well)', 'bien',
     'Bueno has the irregular adverb bien — never "buenamente" for skill.'),
    ('Hoy he dormido ______. (badly)', 'mal',
     'Malo has the irregular adverb mal — one short word.'),
    ('tranquila → ______ (form the adverb)', 'tranquilamente',
     'Tranquila + mente = tranquilamente (calmly).'),
    ('Habla lenta y ______. (clearly — from clara)', 'claramente',
     'Only the last adverb in the pair takes -mente: lenta y claramente.'),
  ]),
  ex3=('Usage and meaning', 'Choose the correct option.', [
    ('Which is correct?', ['Habla lenta y claramente.', 'Habla lentamente y claramente.', 'Habla lento y claramente.'], 'Habla lenta y claramente.',
     'In a pair, the first adverb drops -mente but stays feminine: lenta y claramente.'),
    ('"She sings well" is...', ['Canta bien.', 'Canta buena.', 'Canta bueno.'], 'Canta bien.',
     'A verb needs the adverb bien. Buena/bueno are adjectives — they describe nouns, not singing.'),
    ('The adverb from "fácil" is...', ['fácilmente', 'fácilamente', 'facilmente'], 'fácilmente',
     'Fácil simply adds -mente and keeps its written accent: fácilmente.'),
    ('Which is WRONG?', ['Ella es una conductora rápidamente.', 'Ella conduce rápidamente.', 'Ella es una conductora rápida.'], 'Ella es una conductora rápidamente.',
     'An adverb cannot describe a noun. A driver is rápida (adjective); driving is done rápidamente (adverb).'),
    ('-mente attaches to...', ['the feminine form of the adjective', 'the masculine form of the adjective', 'the plural form of the adjective'], 'the feminine form of the adjective',
     'Always the feminine: lenta + mente, rápida + mente. Adjectives with one form for both genders just add -mente.'),
  ]),
  game_desc='Each manner adverb passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('lentamente', 'lentamente', 'slowly - from lenta + mente', 'slow manner', 'Habla <b>lentamente</b>.', 'Habla ______. (slowly)', 'lentamente'),
    ('rapidamente', 'rápidamente', 'quickly - the accent of rápida survives', 'fast manner', 'Ella conduce <b>rápidamente</b>.', 'Ella conduce ______. (quickly)', 'rápidamente'),
    ('facilmente', 'fácilmente', 'easily - fácil just adds -mente', 'easy manner', 'Aprende idiomas <b>fácilmente</b>.', 'Aprende idiomas ______. (easily)', 'fácilmente'),
    ('bien', 'bien', 'well - the irregular adverb of bueno', 'irregular: good → well', 'Mi hermana cocina muy <b>bien</b>.', 'Mi hermana cocina muy ______. (well)', 'bien'),
    ('mal', 'mal', 'badly - the irregular adverb of malo', 'irregular: bad → badly', 'Hoy he dormido <b>mal</b>.', 'Hoy he dormido ______. (badly)', 'mal'),
    ('claramente', 'claramente', 'clearly - from clara + mente', 'clear manner', 'Explica todo <b>claramente</b>.', 'Explica todo ______. (clearly)', 'claramente'),
    ('tranquilamente', 'tranquilamente', 'calmly - from tranquila + mente', 'calm manner', 'Desayuno <b>tranquilamente</b> los domingos.', 'Desayuno ______ los domingos. (calmly)', 'tranquilamente'),
    ('lenta-y-claramente', 'lenta y claramente', 'slowly and clearly - only the last adverb takes -mente', 'two adverbs in a row', 'Habla <b>lenta y claramente</b>.', 'Habla ______ y claramente. (slowly — feminine form, no -mente)', 'lenta'),
  ],
),

'comparatives-superlatives': dict(
  num='G3', short='Comparatives & Superlatives', title='Comparatives &amp; Superlatives — Comparativos y Superlativos',
  subtitle='Better, the best, extremely good and more and more',
  slides=[
    ('Quick review: más, menos, tan', None,
     '<p class="slide-explanation">You know the core from A2: <b>más ... que</b> (more than), <b>menos ... que</b> (less than), <b>tan ... como</b> (as ... as).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Este hotel es más caro que el otro.</b> (This hotel is more expensive than the other.)</p>'
     '<p style="margin-top:8px"><b>Madrid no es tan tranquila como Toledo.</b> (Madrid is not as quiet as Toledo.)</p></div>'
     '<p style="margin-top:16px">At B1 we add three upgrades: the irregulars, -ísimo, and cada vez más.</p>'),
    ('The irregular four', None,
     '<p class="slide-explanation">Four comparatives never use más: <b>mejor</b> (better), <b>peor</b> (worse), <b>mayor</b> (older), <b>menor</b> (younger).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Este restaurante es mejor que el otro.</b> (This restaurant is better than the other one.)</p>'
     '<p style="margin-top:8px"><b>Mi abuelo es mayor que mi padre.</b> (My grandfather is older than my father.)</p></div>'
     '<p style="margin-top:16px">"Más mejor" is as wrong in Spanish as "more better" is in English — mejor already contains the more.</p>'),
    ('-ísimo: extremely', None,
     '<p class="slide-explanation">Drop the final vowel and add <b>-ísimo/a/os/as</b> to mean <b>extremely</b>. It agrees like a normal adjective.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>bueno → buenísimo</b>: El concierto fue <b>buenísimo</b>. (The concert was amazing.)</p>'
     '<p style="margin-top:8px"><b>fácil → facilísimo</b>: El examen fue <b>facilísimo</b>. — the original accent disappears</p>'
     '<p style="margin-top:8px"><b>mucho → muchísimo</b>: Me gusta <b>muchísimo</b>. (I like it very much.)</p></div>'),
    ('The most ... in', None,
     '<p class="slide-explanation">The relative superlative is <b>el/la/los/las + más + adjective</b>. Watch the ending: after a superlative, English "in" becomes Spanish <b>de</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Es el chico más alto de la clase.</b> (He is the tallest boy in the class.)</p>'
     '<p style="margin-top:8px"><b>Es el mejor restaurante de la ciudad.</b> (It is the best restaurant in town.)</p></div>'
     '<p style="margin-top:16px">Never "en la clase" after a superlative — always <b>de</b>.</p>'),
    ('Cada vez más — more and more', None,
     '<p class="slide-explanation">English repeats the comparative (more and more, colder and colder). Spanish uses one fixed phrase: <b>cada vez más</b> (literally "each time more") — or <b>cada vez menos</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Cada vez más gente trabaja desde casa.</b> (More and more people work from home.)</p>'
     '<p style="margin-top:8px"><b>Cada vez hace más calor.</b> (It is getting hotter and hotter.)</p>'
     '<p style="margin-top:8px"><b>Tengo cada vez menos tiempo.</b> (I have less and less time.)</p></div>'),
  ],
  traps=[
    ('Es más mejor que el otro.', 'Es <strong>mejor</strong> que el otro.', 'Mejor already means better — adding más is like saying "more better"'),
    ('Este café es muy muy bueno.', 'Este café es <strong>buenísimo</strong>.', 'Spanish packs "really, really" into one ending: -ísimo'),
    ('Es el restaurante más caro en la ciudad.', 'Es el restaurante más caro <strong>de</strong> la ciudad.', 'After a superlative, "in" is de — never en'),
    ('La gente trabaja más y más desde casa.', 'La gente trabaja <strong>cada vez más</strong> desde casa.', 'English "more and more" translates as the fixed phrase cada vez más'),
    ('El examen fue fácilísimo.', 'El examen fue <strong>facilísimo</strong>.', 'With -ísimo the original accent disappears — the stress moves to -ísimo'),
  ],
  summary=[
    ('More than', 'más + adjective + que', 'más caro que'),
    ('Irregulars', 'mejor, peor, mayor, menor', 'Es mejor que el otro.'),
    ('Extremely', 'adjective (no final vowel) + ísimo', 'bueno → buenísimo'),
    ('Very much', 'muchísimo', 'Me gusta muchísimo.'),
    ('The most ... in', 'el/la más + adjective + de', 'el más alto de la clase'),
    ('More and more', 'cada vez más / menos', 'Cada vez hace más calor.'),
  ],
  ex1=('Choose the correct form', 'Tap the best option for each sentence.', [
    ('Este hotel es ______ que el otro. (better)', ['mejor', 'más bueno', 'más bien'], 'mejor',
     'Bueno has the irregular comparative mejor. "Más bueno" is not used for quality, and bien is an adverb.'),
    ('La paella estaba ______. (really, really good)', ['buenísima', 'muy buenísima', 'más buena'], 'buenísima',
     '-ísimo agrees: paella is feminine, so buenísima. Muy never combines with -ísimo — the ending already means very.'),
    ('Es la ciudad más bonita ______ España.', ['de', 'en', 'que'], 'de',
     'After a superlative, Spanish uses de where English says in: la más bonita de España.'),
    ('______ gente compra por internet. (more and more)', ['Cada vez más', 'Más y más', 'Siempre más'], 'Cada vez más',
     'The fixed phrase is cada vez más. "Más y más" is a word-for-word calque from English.'),
    ('Mi abuela es ______ que mi madre. (older)', ['mayor', 'más mayor', 'más vieja de'], 'mayor',
     'For people, older = mayor — no más needed, and the comparison closes with que.'),
    ('El examen fue ______ — aprobé sin estudiar. (extremely easy)', ['facilísimo', 'fácilísimo', 'muy facilísimo'], 'facilísimo',
     'Fácil + ísimo = facilísimo: the original accent on fácil disappears, and muy cannot be added.'),
  ]),
  ex2=('Write the comparative', 'Type the missing word — no accents needed in these answers.', [
    ('Este libro es bueno, pero ese es ______. (better)', 'mejor',
     'Irregular comparative of bueno: mejor — better in one word.'),
    ('La película es mala, pero la serie es ______. (worse)', 'peor',
     'Irregular comparative of malo: peor — worse in one word.'),
    ('Mi abuelo es ______ que mi padre. (older)', 'mayor',
     'For people, older = mayor, the irregular comparative of viejo.'),
    ('Es el chico más alto ______ la clase. (in)', 'de',
     'After a superlative, English in becomes Spanish de: el más alto de la clase.'),
    ('Mi hermana es ______ que yo. (younger)', 'menor',
     'Younger = menor, the irregular comparative of joven.'),
  ]),
  ex3=('Usage and meaning', 'Choose the correct option.', [
    ('"Buenísimo" means...', ['extremely good', 'a little good', 'better'], 'extremely good',
     'The -ísimo ending is the absolute superlative: extremely / really, really good.'),
    ('Which is WRONG?', ['Es más mejor que el otro.', 'Es mejor que el otro.', 'Es el mejor de todos.'], 'Es más mejor que el otro.',
     'Mejor never takes más — it already means "more good".'),
    ('"Cada vez más caro" means...', ['more and more expensive', 'as expensive as', 'the most expensive'], 'more and more expensive',
     'Cada vez más + adjective = increasingly / more and more.'),
    ('The -ísimo form of "fácil" is...', ['facilísimo', 'fácilísimo', 'facilisimo'], 'facilísimo',
     'The accent moves to -ísimo, so fácil loses its own: facilísimo.'),
    ('"The best restaurant in town" is...', ['el mejor restaurante de la ciudad', 'el mejor restaurante en la ciudad', 'el más mejor restaurante de la ciudad'], 'el mejor restaurante de la ciudad',
     'Mejor needs no más, and the superlative closes with de, not en.'),
  ]),
  game_desc='Each comparative form passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('mejor', 'mejor', 'better - irregular comparative of bueno', 'irregular of bueno', 'Este hotel es <b>mejor</b> que el otro.', 'Este hotel es ______ que el otro. (better)', 'mejor'),
    ('peor', 'peor', 'worse - irregular comparative of malo', 'irregular of malo', 'La película es <b>peor</b> que el libro.', 'La película es ______ que el libro. (worse)', 'peor'),
    ('mayor', 'mayor', 'older - irregular comparative for people', 'older (people)', 'Mi abuelo es <b>mayor</b> que mi padre.', 'Mi abuelo es ______ que mi padre. (older)', 'mayor'),
    ('menor', 'menor', 'younger - irregular comparative for people', 'younger (people)', 'Mi hermana es <b>menor</b> que yo.', 'Mi hermana es ______ que yo. (younger)', 'menor'),
    ('buenisimo', 'buenísimo', 'extremely good - absolute superlative of bueno', 'really, really good', 'El concierto fue <b>buenísimo</b>.', 'El concierto fue ______. (extremely good)', 'buenísimo'),
    ('muchisimo', 'muchísimo', 'very much - absolute superlative of mucho', 'very much indeed', 'Me gusta <b>muchísimo</b> este libro.', 'Me gusta ______ este libro. (very much)', 'muchísimo'),
    ('el-mas-de', 'el más ... de', 'the most ... in - the superlative closes with de', 'relative superlative', 'Es el chico más alto <b>de</b> la clase.', 'Es el chico más alto ______ la clase. (in)', 'de'),
    ('cada-vez-mas', 'cada vez más', 'more and more - growing degree', 'increasingly', '<b>Cada vez más</b> gente trabaja desde casa.', 'Cada ______ más gente trabaja desde casa. (time, occasion)', 'vez'),
  ],
),

'conditional-clauses': dict(
  num='G4', short='Conditional Clauses', title='Conditional Clauses — Oraciones con Si',
  subtitle='Si llueve, no salimos — and a first look at si tuviera',
  slides=[
    ('Real conditions: si + present', None,
     '<p class="slide-explanation">For real, likely conditions, Spanish works like English: <b>si + present tense</b>, then present or future for the result.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Si llueve, no salimos.</b> (If it rains, we do not go out.)</p>'
     '<p style="margin-top:8px"><b>Si estudias, aprobarás el examen.</b> (If you study, you will pass the exam.)</p></div>'
     '<p style="margin-top:16px">Note: <b>si</b> (if) has no accent. <b>Sí</b> with an accent means yes.</p>'),
    ('Order is flexible', None,
     '<p class="slide-explanation">The si-clause can come first or second. When it comes first, add a comma.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Si hace sol, vamos a la playa.</b> (If it is sunny, we go to the beach.)</p>'
     '<p style="margin-top:8px"><b>Vamos a la playa si hace sol.</b> (Same meaning, no comma.)</p></div>'),
    ('The golden rule: never si + conditional', None,
     '<p class="slide-explanation">Whatever happens, the verb right after <b>si</b> is never the future and never the conditional. English speakers usually get this right by instinct — until they translate "would" word for word.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Wrong: Si <b>tendría</b> dinero... / Si <b>lloverá</b> mañana...</p>'
     '<p style="margin-top:8px">Right: <b>Si tengo</b> dinero... / <b>Si llueve</b> mañana...</p></div>'
     '<p style="margin-top:16px">The conditional lives in the result half of the sentence, never after si.</p>'),
    ('Unreal conditions: si tuviera..., viajaría', None,
     '<p class="slide-explanation">For imaginary situations, Spanish uses <b>si + imperfect subjunctive</b>, then the <b>conditional</b>: like English "If I had time, I would travel".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Si tuviera tiempo, viajaría más.</b> (If I had time, I would travel more.)</p>'
     '<p style="margin-top:8px"><b>Si fuera rico, compraría una casa en la playa.</b> (If I were rich, I would buy a house on the beach.)</p>'
     '<p style="margin-top:8px"><b>Si pudiera, te ayudaría.</b> (If I could, I would help you.)</p></div>'),
    ('Spotting the -ra forms', None,
     '<p class="slide-explanation">The imperfect subjunctive comes from the <b>ellos</b> form of the preterite: drop <b>-ron</b>, add <b>-ra</b>. At B1, recognise the big four.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>tuvieron → tuviera</b> (tener: had)</p>'
     '<p style="margin-top:8px"><b>fueron → fuera</b> (ser: were)</p>'
     '<p style="margin-top:8px"><b>pudieron → pudiera</b> (poder: could)</p>'
     '<p style="margin-top:8px"><b>hicieron → hiciera</b> (hacer: did/made)</p></div>'),
  ],
  traps=[
    ('Si tendría dinero, compraría un coche.', 'Si <strong>tuviera</strong> dinero, compraría un coche.', 'Never the conditional after si — the if-clause takes the imperfect subjunctive'),
    ('Si lloverá mañana, no saldremos.', 'Si <strong>llueve</strong> mañana, no saldremos.', 'Even about the future, si takes the present tense'),
    ('Sí llueve, no salimos.', '<strong>Si</strong> llueve, no salimos.', 'If = si with no accent; sí with an accent means yes'),
    ('Si tuviera tiempo, viajaba más.', 'Si tuviera tiempo, <strong>viajaría</strong> más.', 'The result of an unreal condition uses the conditional, not the imperfect'),
    ('Si era tú, no lo haría.', 'Si <strong>fuera</strong> tú, no lo haría.', '"If I were you" needs the subjunctive fuera, not the imperfect era'),
  ],
  summary=[
    ('Real condition', 'si + presente, + presente', 'Si llueve, no salimos.'),
    ('Future result', 'si + presente, + futuro', 'Si estudias, aprobarás.'),
    ('Unreal condition', 'si + imperf. subjuntivo, + condicional', 'Si tuviera tiempo, viajaría.'),
    ('Key -ra forms', 'tuviera, fuera, pudiera, hiciera', 'Si pudiera, te ayudaría.'),
    ('Banned after si', 'never futuro or condicional', 'Si tengo (not "si tendré") tiempo...'),
    ('Si vs sí', 'si = if; sí = yes', 'Si llueve... / Sí, claro.'),
  ],
  ex1=('Choose the correct verb', 'Tap the best option for each sentence.', [
    ('Si ______ mañana, no salimos. (it rains)', ['llueve', 'lloverá', 'llovería'], 'llueve',
     'After si, even for tomorrow, Spanish uses the present: si llueve. Future and conditional are banned after si.'),
    ('Si estudias, ______ el examen. (you will pass)', ['aprobarás', 'aprobarías', 'hubieras aprobado'], 'aprobarás',
     'Real condition: si + present, then future for the result — aprobarás.'),
    ('Si ______ rico, compraría una casa enorme. (I were)', ['fuera', 'sería', 'era'], 'fuera',
     'Unreal condition: si + imperfect subjunctive fuera. Sería is conditional (banned after si) and era is plain imperfect.'),
    ('Si tuviera más tiempo, ______ más. (I would read)', ['leería', 'leeré', 'leo'], 'leería',
     'The result of si + tuviera is the conditional: leería. The future or present would break the unreal pattern.'),
    ('______ hace sol, vamos a la playa. (if)', ['Si', 'Sí', 'Se'], 'Si',
     'If = si without an accent. Sí means yes, and se is a pronoun.'),
    ('Si ______ ayudarte, lo haría. (I could)', ['pudiera', 'podría', 'puedo'], 'pudiera',
     'After si in an unreal sentence: imperfect subjunctive pudiera. Podría is conditional — it belongs in the other half.'),
  ]),
  ex2=('Complete the condition', 'Type the missing word — no accents needed in these answers.', [
    ('______ llueve, no salimos. (if)', 'si',
     'If = si, written without an accent — sí with an accent means yes.'),
    ('Si ______ tiempo, viajaría más. (I had — imperfect subjunctive of tener)', 'tuviera',
     'Tuvieron minus -ron plus -ra: tuviera. The conditional tendría is banned after si.'),
    ('Si estudias, ______ el examen. (you pass — present tense of aprobar, tú)', 'apruebas',
     'Real condition with a present result: si estudias, apruebas. Aprobar is o→ue: apruebas.'),
    ('Si ______ rico, compraría una casa en la playa. (I were — imperfect subjunctive of ser)', 'fuera',
     'Fueron minus -ron plus -ra: fuera — "if I were".'),
    ('Si hace sol mañana, ______ a la playa. (we go — present tense of ir)', 'vamos',
     'Real condition: si + present, present result — vamos a la playa.'),
  ]),
  ex3=('Meaning check', 'Choose the correct option.', [
    ('Which is WRONG?', ['Si tendría dinero, viajaría.', 'Si tuviera dinero, viajaría.', 'Si tengo dinero, viajo.'], 'Si tendría dinero, viajaría.',
     'The conditional never follows si. The unreal pattern is si tuviera..., viajaría.'),
    ('"Si tuviera tiempo, viajaría" means...', ['If I had time, I would travel.', 'If I have time, I will travel.', 'When I had time, I travelled.'], 'If I had time, I would travel.',
     'Si + imperfect subjunctive + conditional = an unreal, imagined situation.'),
    ('The -ra form of poder is...', ['pudiera', 'podiera', 'pudría'], 'pudiera',
     'From the preterite pudieron: drop -ron, add -ra — pudiera.'),
    ('"If it rains, we will stay at home" is...', ['Si llueve, nos quedaremos en casa.', 'Si lloverá, nos quedaremos en casa.', 'Si llovería, nos quedamos en casa.'], 'Si llueve, nos quedaremos en casa.',
     'Si + present (llueve), future result (nos quedaremos). Future and conditional cannot follow si.'),
    ('"Si fuera tú..." means...', ['If I were you...', 'If I went outside...', 'Yes, it was you...'], 'If I were you...',
     'Fuera is the imperfect subjunctive of ser here: if I were you. Si has no accent, so it cannot mean yes.'),
  ]),
  game_desc='Each conditional pattern passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('si', 'si', 'if - no accent, unlike sí meaning yes', 'condition marker', '<b>Si</b> llueve, no salimos.', '______ llueve, no salimos. (if)', 'si'),
    ('si-llueve', 'si llueve', 'if it rains - real condition with the present tense', 'real condition', '<b>Si llueve</b>, nos quedamos en casa.', 'Si ______, nos quedamos en casa. (it rains)', 'llueve'),
    ('aprobaras', 'aprobarás', 'you will pass - the future result of a real condition', 'future result', 'Si estudias, <b>aprobarás</b>.', 'Si estudias, ______. (you will pass)', 'aprobarás'),
    ('tuviera', 'tuviera', 'had - imperfect subjunctive of tener', 'unreal "had"', 'Si <b>tuviera</b> tiempo, viajaría más.', 'Si ______ tiempo, viajaría más. (I had)', 'tuviera'),
    ('fuera', 'fuera', 'were - imperfect subjunctive of ser', 'unreal "were"', 'Si <b>fuera</b> rico, compraría una casa.', 'Si ______ rico, compraría una casa. (I were)', 'fuera'),
    ('pudiera', 'pudiera', 'could - imperfect subjunctive of poder', 'unreal "could"', 'Si <b>pudiera</b>, te ayudaría.', 'Si ______, te ayudaría. (I could)', 'pudiera'),
    ('hiciera', 'hiciera', 'did or made - imperfect subjunctive of hacer', 'unreal "did"', 'Si <b>hiciera</b> sol, iríamos a la playa.', 'Si ______ sol, iríamos a la playa. (it were sunny)', 'hiciera'),
    ('viajaria', 'viajaría', 'I would travel - the conditional result of an unreal condition', 'conditional result', 'Si tuviera dinero, <b>viajaría</b> por todo el mundo.', 'Si tuviera dinero, ______ por todo el mundo. (I would travel)', 'viajaría'),
  ],
),

'conjunctions-advanced': dict(
  num='G5', short='Advanced Conjunctions', title='Advanced Conjunctions — Conectores Avanzados',
  subtitle='Link ideas: sin embargo, por eso, aunque, mientras, ya que',
  slides=[
    ('Sin embargo — however', None,
     '<p class="slide-explanation"><b>Sin embargo</b> (however) sets two sentences against each other. It usually follows a full stop or semicolon and is wrapped in commas.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El piso es caro; sin embargo, lo vamos a comprar.</b> (The flat is expensive; however, we are going to buy it.)</p>'
     '<p style="margin-top:8px"><b>No me gusta el fútbol. Sin embargo, veo todos los partidos de mi hijo.</b></p></div>'
     '<p style="margin-top:16px">Despite appearances, it has nothing to do with embargoes — treat it as one fixed unit.</p>'),
    ('Por eso and ya que — effect and cause', None,
     '<p class="slide-explanation"><b>Por eso</b> (that is why) introduces a consequence. <b>Ya que</b> (since, given that) introduces a cause that is already known.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Llueve; por eso no salimos.</b> (It is raining; that is why we are not going out.)</p>'
     '<p style="margin-top:8px"><b>Ya que estás aquí, ayúdame con esto.</b> (Since you are here, help me with this.)</p></div>'
     '<p style="margin-top:16px">Careful: ya que has nothing to do with "already" here — it is a cause connector.</p>'),
    ('En cambio and mientras (que)', None,
     '<p class="slide-explanation"><b>En cambio</b> (on the other hand) contrasts two people or things. <b>Mientras</b> alone = while (time); <b>mientras que</b> = whereas (contrast).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Yo trabajo; en cambio, mi hermano descansa.</b> (I work; my brother, on the other hand, rests.)</p>'
     '<p style="margin-top:8px"><b>Mientras ceno, veo la tele.</b> (While I have dinner, I watch TV.) — time</p>'
     '<p style="margin-top:8px"><b>Yo ahorro, mientras que tú lo gastas todo.</b> (I save, whereas you spend everything.) — contrast</p></div>'),
    ('Aunque + indicative — although (a fact)', None,
     '<p class="slide-explanation"><b>Aunque</b> with the normal indicative concedes a <b>real fact</b>: although, even though. Note that aunque already contains que — never add another.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Aunque llueve, vamos a salir.</b> (Although it is raining, we are going to go out.)</p>'
     '<p style="margin-top:8px"><b>Aunque es caro, lo voy a comprar.</b> (Although it is expensive, I am going to buy it.)</p></div>'),
    ('Aunque + subjunctive — even if', None,
     '<p class="slide-explanation">With the <b>subjunctive</b>, aunque shifts from fact to hypothesis: <b>even if</b>. At B1, learn to recognise the difference.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Aunque llueve, salimos.</b> (Although it IS raining — a fact.)</p>'
     '<p style="margin-top:8px"><b>Aunque llueva, saldremos.</b> (Even if it rains — we do not know yet.)</p></div>'
     '<p style="margin-top:16px">One vowel changes the meaning: llueve (fact) vs llueva (possibility).</p>'),
  ],
  traps=[
    ('Sin embargo de la lluvia, salimos.', '<strong>A pesar de</strong> la lluvia, salimos.', 'Sin embargo never takes a noun — before a noun, despite = a pesar de'),
    ('Por eso que llegué tarde.', '<strong>Por eso</strong> llegué tarde.', 'Por eso connects directly — no que after it'),
    ('Aunque que es caro, lo compro.', '<strong>Aunque</strong> es caro, lo compro.', 'Aunque already contains que — never double it'),
    ('Mientras que ceno, veo la tele.', '<strong>Mientras</strong> ceno, veo la tele.', 'For "while" (time), use plain mientras; mientras que means whereas'),
    ('Está lloviendo; en otra mano, ayer hizo sol.', 'Está lloviendo; <strong>en cambio</strong>, ayer hizo sol.', '"On the other hand" is en cambio — never a word-for-word "en otra mano"'),
  ],
  summary=[
    ('However', 'sin embargo', 'Es caro; sin embargo, lo compro.'),
    ('That is why', 'por eso', 'Llueve; por eso no salimos.'),
    ('Since', 'ya que', 'Ya que estás aquí, ayúdame.'),
    ('Whereas', 'en cambio / mientras que', 'Yo trabajo; en cambio, él descansa.'),
    ('Although (fact)', 'aunque + indicativo', 'Aunque llueve, salimos.'),
    ('Even if', 'aunque + subjuntivo', 'Aunque llueva, saldremos.'),
  ],
  ex1=('Choose the connector', 'Tap the best option for each sentence.', [
    ('El piso es caro; ______, lo vamos a comprar. (however)', ['sin embargo', 'por eso', 'ya que'], 'sin embargo',
     'A contrast between the two halves = sin embargo. Por eso would give a consequence, ya que a cause.'),
    ('Estaba enfermo; ______ no fui a clase. (that is why)', ['por eso', 'en cambio', 'aunque'], 'por eso',
     'Being ill caused the absence: por eso = that is why.'),
    ('______ estás aquí, ayúdame con esto. (since)', ['Ya que', 'Sin embargo', 'Por eso'], 'Ya que',
     'A known cause introduces the request: ya que = since / given that.'),
    ('A mí me encanta el café; mi hermano, ______, prefiere el té.', ['en cambio', 'por eso', 'ya que'], 'en cambio',
     'Two people contrasted = en cambio (on the other hand).'),
    ('______ llueve, vamos a salir. (although — it is raining right now)', ['Aunque', 'Sin embargo', 'Mientras'], 'Aunque',
     'Conceding a real fact inside one sentence = aunque + indicative. Sin embargo needs two separate sentences.'),
    ('Aunque ______ mucho dinero, no lo compraría. (even if I had)', ['tuviera', 'tengo', 'tendría'], 'tuviera',
     'Even if = aunque + subjunctive: tuviera. Tengo would make it a fact, and the conditional cannot follow aunque here.'),
  ]),
  ex2=('Complete the connector', 'Type the missing word — no accents needed in these answers.', [
    ('Es caro; sin ______, lo voy a comprar. (however)', 'embargo',
     'However = sin embargo — a fixed two-word unit.'),
    ('Llueve; por ______ no salimos. (that is why)', 'eso',
     'That is why = por eso — eso points back at the cause.'),
    ('______ es caro, lo voy a comprar. (although)', 'aunque',
     'Although = aunque, one word that already includes que.'),
    ('Yo trabajo mucho; en ______, mi hermano descansa. (on the other hand)', 'cambio',
     'On the other hand = en cambio — literally "in exchange".'),
    ('______ ceno, veo la tele. (while)', 'mientras',
     'While (two actions at the same time) = mientras, without que.'),
  ]),
  ex3=('Meaning check', 'Choose the correct option.', [
    ('"Sin embargo" means...', ['however', 'therefore', 'meanwhile'], 'however',
     'Sin embargo contrasts two statements — however / nevertheless.'),
    ('Which is WRONG?', ['Aunque que llueve, salimos.', 'Aunque llueve, salimos.', 'Aunque llueva, saldremos.'], 'Aunque que llueve, salimos.',
     'Aunque never takes an extra que. Both other versions are correct — fact and hypothesis.'),
    ('"Aunque llueva, saldremos" (subjunctive llueva) means...', ['Even if it rains, we will go out.', 'Although it is raining now, we go out.', 'Because it rains, we will go out.'], 'Even if it rains, we will go out.',
     'The subjunctive llueva makes it hypothetical: even if. The indicative llueve would state a fact.'),
    ('"Mientras que" usually expresses...', ['contrast - whereas', 'time - while', 'cause - because'], 'contrast - whereas',
     'Mientras que = whereas. Plain mientras (no que) covers "while" in time.'),
    ('Before a noun, "despite" is...', ['a pesar de', 'sin embargo de', 'aunque de'], 'a pesar de',
     'Only a pesar de can take a noun: a pesar de la lluvia. Sin embargo and aunque introduce clauses.'),
  ]),
  game_desc='Each connector passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('sin-embargo', 'sin embargo', 'however - contrast between two sentences', 'contrast linker', 'Es caro; <b>sin embargo</b>, lo compro.', 'Es caro; sin ______, lo compro. (however)', 'embargo'),
    ('por-eso', 'por eso', 'that is why - introduces a consequence', 'consequence linker', 'Llueve; <b>por eso</b> no salimos.', 'Llueve; por ______ no salimos. (that is why)', 'eso'),
    ('ya-que', 'ya que', 'since / given that - a known cause', 'cause linker', '<b>Ya que</b> estás aquí, ayúdame.', '______ que estás aquí, ayúdame. (since: ... que)', 'ya'),
    ('en-cambio', 'en cambio', 'on the other hand - contrasts two people or things', 'contrast of two sides', 'Yo trabajo; <b>en cambio</b>, él descansa.', 'Yo trabajo; en ______, él descansa. (on the other hand)', 'cambio'),
    ('aunque', 'aunque', 'although - concedes a fact, already contains que', 'concession', '<b>Aunque</b> es caro, lo compro.', '______ es caro, lo compro. (although)', 'aunque'),
    ('aunque-llueva', 'aunque llueva', 'even if it rains - aunque + subjunctive for hypothesis', 'even if + subjunctive', '<b>Aunque llueva</b>, saldremos.', 'Aunque ______, saldremos. (it might rain — subjunctive)', 'llueva'),
    ('mientras', 'mientras', 'while - two actions at the same time', 'time linker', '<b>Mientras</b> ceno, veo la tele.', '______ ceno, veo la tele. (while)', 'mientras'),
    ('a-pesar-de', 'a pesar de', 'despite - the connector that works before a noun', 'despite + noun', '<b>A pesar de</b> la lluvia, salimos.', 'A ______ de la lluvia, salimos. (despite)', 'pesar'),
  ],
),
}
