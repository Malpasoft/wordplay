# -*- coding: utf-8 -*-
"""espanol-en B1 grammar content — batch 4 (chapters G16-G19)."""

CHAPTERS = {

'present-perfect-advanced': dict(
  num='G16', short='Present Perfect', title='Present Perfect — Perfecto vs indefinido',
  subtitle='he comido vs comí: choosing the right past for the right time frame',
  slides=[
    ('Two pasts, one rule of thumb', None,
     '<p class="slide-explanation">Spanish (in Spain) splits the past by <b>time frame</b>: if the period includes NOW (hoy, esta semana, este año), use the <b>pretérito perfecto</b>; if it is closed (ayer, el lunes, en 2019), use the <b>indefinido</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hoy he desayunado churros.</b> (Today I had churros — today is still running.)</p>'
     '<p style="margin-top:8px"><b>Ayer desayuné tostadas.</b> (Yesterday I had toast — yesterday is closed.)</p></div>'
     '<p style="margin-top:16px">English speakers over-use the indefinido. Listen for the time marker — it decides for you.</p>'),
    ('Form: he, has, ha + participio', None,
     '<p class="slide-explanation">Present of <b>haber</b> + past participle. Same irregular participles as the pluscuamperfecto.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>he · has · ha · hemos · habéis · han</b> + hablado/comido/vivido</p>'
     '<p style="margin-top:8px"><b>¿Has visto mi móvil?</b> (Have you seen my phone?)</p>'
     '<p style="margin-top:8px"><b>Todavía no hemos terminado.</b> (We haven\'t finished yet.)</p></div>'
     '<p style="margin-top:16px">Like English "have done" — but remember nothing can separate haber and the participle.</p>'),
    ('The open-period markers', None,
     '<p class="slide-explanation">These markers call for the perfecto because the period is still open.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>hoy</b> · <b>esta mañana/semana</b> · <b>este mes/año</b> · <b>últimamente</b> (lately)</p>'
     '<p style="margin-top:8px"><b>ya</b> (already) · <b>todavía no</b> (not yet) · <b>alguna vez</b> (ever) · <b>nunca</b></p>'
     '<p style="margin-top:8px"><b>¿Has estado alguna vez en México?</b> (Have you ever been to Mexico?)</p></div>'
     '<p style="margin-top:16px">Experience questions (¿alguna vez...?) always take the perfecto — just like English "have you ever...?".</p>'),
    ('The closed-period markers', None,
     '<p class="slide-explanation">These markers close the period and demand the indefinido.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>ayer</b> · <b>anoche</b> · <b>la semana pasada</b> · <b>el año pasado</b> · <b>en 2015</b> · <b>hace dos días</b></p>'
     '<p style="margin-top:8px"><b>Anoche cené con mis padres.</b> (Last night I had dinner with my parents.)</p>'
     '<p style="margin-top:8px"><b>En 2019 viajamos a Chile.</b> (In 2019 we travelled to Chile.)</p></div>'
     '<p style="margin-top:16px">Unlike British English, Spanish is strict: "hoy" really does force the perfecto, "ayer" really does force the indefinido.</p>'),
    ('A note on Latin America', None,
     '<p class="slide-explanation">In most of Latin America the indefinido covers nearly everything ("Hoy desayuné churros" is normal in Mexico). This course teaches the <b>Castilian</b> distinction — examiners expect it, and you will understand both.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Spain: <b>Hoy he comido</b> paella. &nbsp;·&nbsp; Mexico: <b>Hoy comí</b> tacos.</p>'
     '<p style="margin-top:8px">Both are correct Spanish — but match your register to your exam.</p></div>'
     '<p style="margin-top:16px">Exam tip: in writing, pick one system and stay consistent throughout your text.</p>'),
  ],
  traps=[
    ('Ayer he visitado a mi abuela.', 'Ayer <strong>visité</strong> a mi abuela.', 'ayer closes the period → indefinido, never the perfecto (in Spain)'),
    ('Hoy desayuné churros. (in a Castilian exam)', 'Hoy <strong>he desayunado</strong> churros.', 'hoy keeps the period open → pretérito perfecto in peninsular Spanish'),
    ('¿Has visto la película la semana pasada?', '¿<strong>Viste</strong> la película la semana pasada?', 'la semana pasada is a closed period → indefinido'),
    ('He nunca probado el gazpacho.', '<strong>Nunca he probado</strong> el gazpacho.', 'nunca goes before he — nothing splits haber + participle'),
    ('¿Alguna vez estuviste en México? (experience question)', '¿Alguna vez <strong>has estado</strong> en México?', 'Experience with alguna vez → perfecto: has estado'),
  ],
  summary=[
    ('Open period', 'hoy, esta semana, este año → perfecto', 'Hoy he desayunado churros.'),
    ('Closed period', 'ayer, en 2019, hace dos días → indefinido', 'Ayer desayuné tostadas.'),
    ('Form', 'he/has/ha/hemos/habéis/han + participio', '¿Has visto mi móvil?'),
    ('Experience', '¿alguna vez has...? · nunca he...', '¿Has estado alguna vez en México?'),
    ('Already / yet', 'ya he... · todavía no he...', 'Todavía no hemos terminado.'),
    ('Regional', 'Latin America prefers the indefinido', 'Hoy comí tacos. (Mex.)'),
  ],
  ex1=('Perfecto or indefinido?', 'Let the time marker decide.', [
    ('Esta semana ______ mucho trabajo. (yo, tener)', ['he tenido', 'tuve', 'tenía'], 'he tenido',
     'Esta semana = open period → HE TENIDO.'),
    ('Anoche ______ una película estupenda. (nosotros, ver)', ['vimos', 'hemos visto', 'veíamos'], 'vimos',
     'Anoche = closed → VIMOS.'),
    ('¿______ alguna vez sushi? (tú, probar)', ['Has probado', 'Probaste', 'Probabas'], 'Has probado',
     'Experience question → HAS PROBADO.'),
    ('El año pasado ______ a Argentina. (ellos, viajar)', ['viajaron', 'han viajado', 'viajaban'], 'viajaron',
     'El año pasado = closed → VIAJARON.'),
    ('Todavía no ______ los deberes. (yo, hacer)', ['he hecho', 'hice', 'hacía'], 'he hecho',
     'Todavía no (not yet) → perfecto with irregular participle: HE HECHO.'),
    ('Hace dos años ______ de universidad. (ella, cambiar)', ['cambió', 'ha cambiado', 'cambiaba'], 'cambió',
     'Hace dos años = closed point → CAMBIÓ.'),
  ]),
  ex2=('Type the right past', 'Watch the marker, then conjugate.', [
    ('Hoy ______ tarde al trabajo. (yo, llegar — perfecto, two words)', 'he llegado',
     'Hoy → perfecto: HE LLEGADO tarde.'),
    ('Ayer ______ tarde a clase. (yo, llegar — indefinido, one word)', 'llegué',
     'Ayer → indefinido: LLEGUÉ (g→gu before é).'),
    ('¿Qué has ______ este fin de semana? (hacer — participle)', 'hecho',
     'Hacer → irregular participle HECHO.'),
    ('Nunca ______ escrito una novela. (yo — one word)', 'he',
     'Nunca + HE escrito — nunca before haber.'),
    ('Este mes ______ tres libros. (nosotros, leer — two words)', 'hemos leído',
     'Este mes → perfecto: HEMOS LEÍDO (accent on í).'),
  ]),
  ex3=('Spot the correct sentence', 'Spain rules: open vs closed.', [
    ('Today I have eaten paella:', ['Hoy he comido paella.', 'Hoy comí paella.', 'Hoy comía paella.'], 'Hoy he comido paella.',
     'Hoy → perfecto in Castilian Spanish.'),
    ('Have you ever been to Madrid?', ['¿Has estado alguna vez en Madrid?', '¿Estuviste alguna vez en Madrid?', '¿Estabas alguna vez en Madrid?'], '¿Has estado alguna vez en Madrid?',
     'Experience → perfecto: has estado.'),
    ('Last night we went out for dinner:', ['Anoche salimos a cenar.', 'Anoche hemos salido a cenar.', 'Anoche salíamos a cenar.'], 'Anoche salimos a cenar.',
     'Anoche → indefinido: salimos.'),
    ('I haven\'t finished yet:', ['Todavía no he terminado.', 'Todavía no terminé.', 'No he todavía terminado.'], 'Todavía no he terminado.',
     'Not yet → perfecto, todavía no before he.'),
    ('In 2020 we moved house:', ['En 2020 nos mudamos de casa.', 'En 2020 nos hemos mudado de casa.', 'En 2020 nos mudábamos de casa.'], 'En 2020 nos mudamos de casa.',
     'En 2020 = closed → indefinido: nos mudamos.'),
  ]),
  game_desc='Each past-tense choice passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('he-comido', 'he comido', 'I have eaten (open period)', 'perfecto', 'Hoy <b>he comido</b> paella.', 'Hoy ______ comido paella. (I have)', 'he'),
    ('comi', 'comí', 'I ate (closed period)', 'indefinido', 'Ayer <b>comí</b> con mis padres.', 'Ayer ______ con mis padres. (I ate)', 'comí'),
    ('hoy-perfecto', 'hoy → perfecto', 'today keeps the period open', 'open marker', '<b>Hoy</b> he desayunado churros.', '______ he desayunado churros. (today)', 'hoy'),
    ('ayer-indefinido', 'ayer → indefinido', 'yesterday closes the period', 'closed marker', '<b>Ayer</b> desayuné tostadas.', '______ desayuné tostadas. (yesterday)', 'ayer'),
    ('alguna-vez', '¿alguna vez has...?', 'have you ever...? (experience)', 'experience', '¿Has estado <b>alguna vez</b> en México?', '¿Has estado alguna ______ en México? (ever)', 'vez'),
    ('todavia-no-he', 'todavía no he...', 'I haven\'t ... yet', 'not yet', '<b>Todavía no</b> hemos terminado.', '______ no hemos terminado. (yet/still)', 'todavía'),
    ('ya-he', 'ya he...', 'I have already...', 'already', '<b>Ya</b> he visto esa película.', '______ he visto esa película. (already)', 'ya'),
    ('has-visto', '¿has visto...?', 'have you seen...?', 'question', '¿<b>Has visto</b> mi móvil?', '¿Has ______ mi móvil? (seen)', 'visto'),
  ],
),

'relative-clauses-advanced': dict(
  num='G17', short='Relative Clauses', title='Relative Clauses — que, quien, cuyo',
  subtitle='the people who, the book that, whose: joining sentences like a native',
  slides=[
    ('Que — the universal relative', None,
     '<p class="slide-explanation">Spanish <b>que</b> covers English who, which AND that — for people and things alike. It can never be left out, unlike English "that".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>La chica que vive arriba es médica.</b> (The girl who lives upstairs is a doctor.)</p>'
     '<p style="margin-top:8px"><b>El libro que compré es buenísimo.</b> (The book [that] I bought is great.)</p></div>'
     '<p style="margin-top:16px">English drops "that" (the book I bought); Spanish never drops <b>que</b>. El libro que compré — always.</p>'),
    ('Quien and quienes — after prepositions', None,
     '<p class="slide-explanation">For people after a preposition, use <b>quien/quienes</b> (or el que/la que). Bare que alone won\'t do after con, para, de...</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El amigo con quien viajé...</b> (The friend with whom I travelled / the friend I travelled with...)</p>'
     '<p style="margin-top:8px"><b>La profesora de quien te hablé...</b> (The teacher I told you about...)</p></div>'
     '<p style="margin-top:16px">English hides the preposition at the end (the friend I travelled WITH); Spanish puts it FIRST: con quien, de quien, para quien.</p>'),
    ('El que, la que, los que, las que', None,
     '<p class="slide-explanation">After prepositions — and for "the one who/which" — Spanish uses <b>el/la/los/las que</b>, agreeing with the noun.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>La empresa para la que trabajo es alemana.</b> (The company I work for is German.)</p>'
     '<p style="margin-top:8px"><b>Los que llegaron tarde no entraron.</b> (The ones who arrived late didn\'t get in.)</p></div>'
     '<p style="margin-top:16px">Pick the article that matches: el barrio en el que vivo · la casa en la que nací.</p>'),
    ('Lo que — "what" as a connector', None,
     '<p class="slide-explanation"><b>Lo que</b> = "what" in the sense of "the thing that". A hugely common connector.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>No entiendo lo que dices.</b> (I don\'t understand what you are saying.)</p>'
     '<p style="margin-top:8px"><b>Lo que más me gusta es la playa.</b> (What I like most is the beach.)</p></div>'
     '<p style="margin-top:16px">Trap: never use qué (with accent) here — question word ≠ connector. No entiendo lo que dices.</p>'),
    ('Cuyo — whose (formal but exam-loved)', None,
     '<p class="slide-explanation"><b>Cuyo/cuya/cuyos/cuyas</b> = whose. It agrees with the thing POSSESSED, not the possessor.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El escritor cuya novela ganó el premio...</b> (The writer whose novel won the prize... — cuya agrees with novela.)</p>'
     '<p style="margin-top:8px"><b>Una ciudad cuyos parques son famosos...</b> (A city whose parks are famous...)</p></div>'
     '<p style="margin-top:16px">In speech people often rephrase, but cuyo earns marks in writing. Remember: agreement follows what comes AFTER cuyo.</p>'),
  ],
  traps=[
    ('El libro compré es muy bueno.', 'El libro <strong>que</strong> compré es muy bueno.', 'Spanish never omits que — English "the book I bought" still needs que'),
    ('La persona que hablé con...', 'La persona <strong>con quien</strong> hablé...', 'The preposition goes BEFORE the relative: con quien, never stranded at the end'),
    ('No entiendo qué dices. (statement, not question)', 'No entiendo <strong>lo que</strong> dices.', 'The connector "what" is lo que — qué with an accent is only for questions'),
    ('El autor cuyo novela me encanta...', 'El autor <strong>cuya</strong> novela me encanta...', 'cuyo agrees with the possessed noun (novela, feminine) — not with the possessor'),
    ('La empresa que trabajo para...', 'La empresa <strong>para la que</strong> trabajo...', 'Preposition first + article + que: para la que trabajo'),
  ],
  summary=[
    ('Universal', 'que (people and things, never omitted)', 'El libro que compré.'),
    ('After preposition (people)', 'con/de/para + quien(es)', 'El amigo con quien viajé.'),
    ('After preposition (things)', 'en/para + el/la/los/las que', 'La empresa para la que trabajo.'),
    ('The ones who', 'los que / las que', 'Los que llegaron tarde no entraron.'),
    ('What (connector)', 'lo que', 'No entiendo lo que dices.'),
    ('Whose', 'cuyo/a/os/as (agrees with possessed)', 'El escritor cuya novela ganó.'),
  ],
  ex1=('Choose the relative', 'que, quien, lo que or cuyo?', [
    ('La película ______ vimos anoche era larguísima.', ['que', 'quien', 'cuya'], 'que',
     'Things → QUE: la película que vimos.'),
    ('El compañero con ______ comparto piso es muy ordenado.', ['quien', 'que cual', 'cuyo'], 'quien',
     'Person after preposition → con QUIEN.'),
    ('No entiendo ______ quieres decir.', ['lo que', 'que', 'cuyo'], 'lo que',
     '"What you mean" → LO QUE quieres decir.'),
    ('La autora ______ libros leo siempre gana premios.', ['cuyos', 'cuya', 'que'], 'cuyos',
     'Whose + libros (masc. plural) → CUYOS libros.'),
    ('______ estudian más, aprueban. (the ones who)', ['Los que', 'Quien que', 'Cuyos'], 'Los que',
     '"The ones who" → LOS QUE estudian.'),
    ('El pueblo en ______ nací está en la montaña.', ['el que', 'quien', 'lo que'], 'el que',
     'Place after preposition → en EL QUE (el pueblo, masculine).'),
  ]),
  ex2=('Complete with the right relative', 'Type the missing word(s).', [
    ('The friend I travelled with → el amigo con ______ viajé (one word)', 'quien',
     'Person after con → QUIEN.'),
    ('What I like most → ______ que más me gusta (one word)', 'lo',
     '"What" connector → LO que.'),
    ('The writer whose novel won → el escritor ______ novela ganó (one word)', 'cuya',
     'Cuyo agrees with novela → CUYA.'),
    ('The book I bought → el libro ______ compré (one word)', 'que',
     'Never omit que: el libro QUE compré.'),
    ('The company I work for → la empresa para ______ ______ trabajo (two words)', 'la que',
     'Preposition + article + que → para LA QUE trabajo.'),
  ]),
  ex3=('Join the sentences', 'Pick the natural combined sentence.', [
    ('Tengo una amiga. Su hermano es actor.', ['Tengo una amiga cuyo hermano es actor.', 'Tengo una amiga que su hermano es actor.', 'Tengo una amiga quien hermano es actor.'], 'Tengo una amiga cuyo hermano es actor.',
     'Whose → cuyo (agrees with hermano): cuya amiga... no — cuyo HERMANO.'),
    ('Vivo en un barrio. El barrio tiene muchos parques.', ['Vivo en un barrio que tiene muchos parques.', 'Vivo en un barrio quien tiene parques.', 'Vivo en un barrio cuyo tiene parques.'], 'Vivo en un barrio que tiene muchos parques.',
     'Subject relative for things → QUE tiene.'),
    ('Hablé con una señora. La señora era la directora.', ['La señora con quien hablé era la directora.', 'La señora que hablé con era la directora.', 'La señora con que cual hablé era la directora.'], 'La señora con quien hablé era la directora.',
     'Person + preposition → CON QUIEN hablé.'),
    ('"I don\'t know what to do":', ['No sé qué hacer.', 'No sé lo que hacer que.', 'No sé cuyo hacer.'], 'No sé qué hacer.',
     'Before an infinitive, the indirect question uses qué: no sé qué hacer.'),
    ('"The ones who finish early can leave":', ['Los que terminen pronto pueden irse.', 'Cuyos terminan pronto pueden irse.', 'Quien que terminan pronto pueden irse.'], 'Los que terminen pronto pueden irse.',
     '"The ones who" → LOS QUE (+ subjunctive for an open group).'),
  ]),
  game_desc='Each relative passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('que', 'que', 'who / which / that — never omitted', 'universal relative', 'El libro <b>que</b> compré es buenísimo.', 'El libro ______ compré es buenísimo. (that)', 'que'),
    ('con-quien', 'con quien', 'with whom (person + preposition)', 'preposition first', 'El amigo <b>con quien</b> viajé.', 'El amigo con ______ viajé. (whom)', 'quien'),
    ('el-que', 'el/la que', 'which (after a preposition)', 'agreeing article', 'La empresa para <b>la que</b> trabajo.', 'La empresa para la ______ trabajo. (which)', 'que'),
    ('los-que', 'los que', 'the ones who', 'group', '<b>Los que</b> llegaron tarde no entraron.', '______ que llegaron tarde no entraron. (the ones)', 'los'),
    ('lo-que', 'lo que', 'what (the thing that)', 'connector', 'No entiendo <b>lo que</b> dices.', 'No entiendo ______ que dices. (what)', 'lo'),
    ('cuyo', 'cuyo/cuya', 'whose (agrees with the possessed)', 'possession', 'El escritor <b>cuya</b> novela ganó el premio.', 'El escritor ______ novela ganó el premio. (whose)', 'cuya'),
    ('en-el-que', 'en el que', 'in which / where', 'place', 'El pueblo <b>en el que</b> nací.', 'El pueblo en el ______ nací. (which)', 'que'),
    ('de-quien', 'de quien', 'about whom', 'person + de', 'La profesora <b>de quien</b> te hablé.', 'La profesora de ______ te hablé. (whom)', 'quien'),
  ],
),

'subjunctive-intro': dict(
  num='G18', short='Subjunctive Intro', title='Subjunctive — El presente de subjuntivo',
  subtitle='quiero que vengas: the mood English almost lost, alive and essential in Spanish',
  slides=[
    ('What the subjunctive is for', None,
     '<p class="slide-explanation">The subjunctive is not a tense but a <b>mood</b>: it marks what is wished, doubted, or felt — rather than stated as fact. English has traces ("I suggest he <b>be</b> on time"); Spanish uses it constantly.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Fact: <b>Sé que vienes.</b> (I know you are coming — indicative.)</p>'
     '<p style="margin-top:8px">Wish: <b>Quiero que vengas.</b> (I want you to come — subjunctive!)</p></div>'
     '<p style="margin-top:16px">Notice the English: "I want YOU TO COME" — Spanish says "I want THAT you come", with the verb in the subjunctive.</p>'),
    ('Forming it: swap the vowel', None,
     '<p class="slide-explanation">Start from the yo form of the present, drop -o, add the <b>opposite vowel</b> endings: -ar verbs take -e endings, -er/-ir verbs take -a endings.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>hablar → hable, hables, hable, hablemos, habléis, hablen</b></p>'
     '<p style="margin-top:8px"><b>comer → coma, comas, coma, comamos, comáis, coman</b></p>'
     '<p style="margin-top:8px"><b>vivir → viva, vivas, viva, vivamos, viváis, vivan</b></p></div>'
     '<p style="margin-top:16px">Starting from the yo form keeps the irregularities: tengo → <b>tenga</b>, hago → <b>haga</b>, conozco → <b>conozca</b>.</p>'),
    ('The big irregulars', None,
     '<p class="slide-explanation">Six verbs don\'t follow the yo-form trick — memorise them with the classic acronym-friendly list.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>ser → sea</b> · <b>estar → esté</b> · <b>ir → vaya</b></p>'
     '<p style="margin-top:8px"><b>saber → sepa</b> · <b>dar → dé</b> · <b>haber → haya</b></p>'
     '<p style="margin-top:8px"><b>Espero que sea fácil.</b> (I hope it is easy.) · <b>¡Que te vaya bien!</b> (Hope it goes well!)</p></div>'
     '<p style="margin-top:16px">These six appear in every exam. Sea, esté, vaya, sepa, dé, haya — chant them.</p>'),
    ('The triggers: wishes, emotions, requests', None,
     '<p class="slide-explanation">The subjunctive appears after a trigger + <b>que</b> + change of subject. The B1 trigger families:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Wish/request: <b>quiero que / espero que / pido que</b> + subj.</p>'
     '<p style="margin-top:8px">Emotion: <b>me alegro de que / siento que / me molesta que</b> + subj.</p>'
     '<p style="margin-top:8px">Impersonal: <b>es importante que / es necesario que / es mejor que</b> + subj.</p></div>'
     '<p style="margin-top:16px">Same subject → infinitive: Quiero <b>ir</b>. Different subjects → que + subjunctive: Quiero que <b>vayas</b>.</p>'),
    ('Ojalá and other one-word triggers', None,
     '<p class="slide-explanation">Some triggers are single words. The loveliest is <b>ojalá</b> (from Arabic "law šā\' Allāh" — God willing): hope itself, always + subjunctive.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Ojalá llueva café.</b> (I hope it rains coffee — as the song goes.)</p>'
     '<p style="margin-top:8px"><b>Ojalá apruebes el examen.</b> (I hope you pass the exam.)</p>'
     '<p style="margin-top:8px"><b>Que tengas buen viaje.</b> (Have a good trip! — a wish, so subjunctive.)</p></div>'
     '<p style="margin-top:16px">Good-wish formulas all hide a subjunctive: que aproveche, que te mejores, que cumplas muchos más.</p>'),
  ],
  traps=[
    ('Quiero que vienes a la fiesta.', 'Quiero que <strong>vengas</strong> a la fiesta.', 'After quiero que (wish + new subject) the verb must be subjunctive: vengas'),
    ('Quiero que ir al cine. (same subject)', 'Quiero <strong>ir</strong> al cine.', 'Same subject → plain infinitive, no que: quiero ir'),
    ('Espero que el examen es fácil.', 'Espero que el examen <strong>sea</strong> fácil.', 'esperar que triggers the subjunctive — and ser is irregular: sea'),
    ('Es importante que estudias cada día.', 'Es importante que <strong>estudies</strong> cada día.', 'Impersonal judgements (es importante que) take the subjunctive: estudies'),
    ('Ojalá que llueve mañana no.', 'Ojalá <strong>no llueva</strong> mañana.', 'ojalá always takes the subjunctive: llueva'),
  ],
  summary=[
    ('Concept', 'mood of wishes, doubts, emotions', 'Quiero que vengas.'),
    ('-ar verbs', 'opposite vowel: -e endings', 'hable · hables · hablen'),
    ('-er/-ir verbs', '-a endings (from the yo form)', 'coma · viva · tenga · haga'),
    ('Irregular six', 'sea · esté · vaya · sepa · dé · haya', 'Espero que sea fácil.'),
    ('Triggers', 'querer/esperar/es importante + que', 'Es mejor que vengas pronto.'),
    ('Ojalá', 'ojalá + subjunctive', 'Ojalá apruebes el examen.'),
  ],
  ex1=('Subjunctive or indicative?', 'Look for the trigger and the subject change.', [
    ('Quiero que ______ conmigo al concierto. (tú, venir)', ['vengas', 'vienes', 'venir'], 'vengas',
     'Wish + new subject → subjunctive: VENGAS.'),
    ('Sé que ______ mucho. (tú, estudiar — fact!)', ['estudias', 'estudies', 'estudiar'], 'estudias',
     'Saber que states a fact → indicative: ESTUDIAS.'),
    ('Es necesario que ______ antes de las diez. (vosotros, llegar)', ['lleguéis', 'llegáis', 'llegar'], 'lleguéis',
     'Es necesario que → subjunctive: LLEGUÉIS (gu spelling).'),
    ('Espero que la película ______ buena. (ser)', ['sea', 'es', 'será'], 'sea',
     'Esperar que → subjunctive, irregular: SEA.'),
    ('Me alegro de que ______ aquí. (tú, estar)', ['estés', 'estás', 'estar'], 'estés',
     'Emotion trigger → subjunctive: ESTÉS.'),
    ('Quiero ______ temprano mañana. (yo, salir — same subject!)', ['salir', 'salga', 'salgo'], 'salir',
     'Same subject → infinitive: quiero SALIR.'),
  ]),
  ex2=('Form the present subjunctive', 'Start from the yo form.', [
    ('hacer (él) → Es mejor que lo ______ él mismo.', 'haga',
     'hago → HAGA: the yo form keeps the g.'),
    ('tener (tú) → Espero que ______ suerte.', 'tengas',
     'tengo → TENGAS.'),
    ('ir (nosotros) → Quiere que ______ juntos.', 'vayamos',
     'Ir is irregular: VAYAMOS.'),
    ('saber (ellos) → Ojalá ______ la respuesta.', 'sepan',
     'Saber is irregular: SEPAN.'),
    ('hablar (yo) → Quieren que ______ en la reunión.', 'hable',
     '-ar → -e endings: HABLE.'),
  ]),
  ex3=('Wishes and reactions', 'Choose the correct sentence.', [
    ('I want you to help me:', ['Quiero que me ayudes.', 'Quiero que me ayudas.', 'Quiero ayudarte que.'], 'Quiero que me ayudes.',
     'Wish + new subject → subjunctive AYUDES.'),
    ('I hope it doesn\'t rain:', ['Espero que no llueva.', 'Espero que no llueve.', 'Espero no que lloverá.'], 'Espero que no llueva.',
     'Esperar que → subjunctive LLUEVA.'),
    ('Have a good weekend! (wish):', ['¡Que tengas buen fin de semana!', '¡Que tienes buen fin de semana!', '¡Tengas que buen fin de semana!'], '¡Que tengas buen fin de semana!',
     'Good wishes = que + subjunctive: que TENGAS.'),
    ('It\'s important that everyone participates:', ['Es importante que todos participen.', 'Es importante que todos participan.', 'Es importante todos participar que.'], 'Es importante que todos participen.',
     'Impersonal judgement → subjunctive PARTICIPEN.'),
    ('I know she lives here (fact):', ['Sé que vive aquí.', 'Sé que viva aquí.', 'Sé que viviera aquí.'], 'Sé que vive aquí.',
     'Fact → indicative VIVE. No trigger, no subjunctive.'),
  ]),
  game_desc='Each subjunctive trigger passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('quiero-que', 'quiero que + subj.', 'I want (someone) to...', 'wish trigger', '<b>Quiero que vengas</b> a la fiesta.', 'Quiero que ______ a la fiesta. (you come)', 'vengas'),
    ('espero-que', 'espero que + subj.', 'I hope (that)...', 'hope trigger', 'Espero que <b>sea</b> fácil.', 'Espero que ______ fácil. (it is — subjunctive of ser)', 'sea'),
    ('es-importante', 'es importante que + subj.', 'it is important that...', 'impersonal', 'Es importante que <b>estudies</b> cada día.', 'Es importante que ______ cada día. (you study)', 'estudies'),
    ('ojala', 'ojalá + subj.', 'I hope / let\'s hope (from Arabic)', 'one-word trigger', '<b>Ojalá</b> apruebes el examen.', '______ apruebes el examen. (hopefully)', 'ojalá'),
    ('vaya', 'vaya', 'irregular subjunctive of ir', 'ir → vaya', '¡Que te <b>vaya</b> bien!', '¡Que te ______ bien! (may it go)', 'vaya'),
    ('tenga', 'tenga', 'subjunctive of tener (from tengo)', 'yo-form trick', 'Espero que <b>tengas</b> suerte.', 'Espero que ______ suerte. (you have)', 'tengas'),
    ('haga', 'haga', 'subjunctive of hacer (from hago)', 'yo-form trick', 'Es mejor que lo <b>haga</b> él.', 'Es mejor que lo ______ él. (he does)', 'haga'),
    ('mismo-sujeto', 'quiero + infinitive', 'same subject → no que, no subjunctive', 'infinitive rule', 'Quiero <b>ir</b> al cine.', 'Quiero ______ al cine. (to go — same subject)', 'ir'),
  ],
),

'verb-forms': dict(
  num='G19', short='Verb Forms', title='Verb Forms — Infinitivo, gerundio, participio',
  subtitle='ir a + inf, seguir + gerundio, acabar de: the periphrases that power fluent Spanish',
  slides=[
    ('The three non-personal forms', None,
     '<p class="slide-explanation">Every Spanish verb has three non-personal forms — and each plugs into different structures.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Infinitivo</b>: hablar, comer, vivir — the dictionary form</p>'
     '<p style="margin-top:8px"><b>Gerundio</b>: hablando, comiendo, viviendo — the -ing form</p>'
     '<p style="margin-top:8px"><b>Participio</b>: hablado, comido, vivido — the -ed/-en form</p></div>'
     '<p style="margin-top:16px">Combined with helper verbs, they form <b>perífrasis verbales</b> — the secret to natural-sounding Spanish.</p>'),
    ('Ir a + infinitive, acabar de + infinitive', None,
     '<p class="slide-explanation">Two infinitive periphrases bracket the present: what is about to happen and what just happened.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Voy a llamarte esta noche.</b> (I am going to call you tonight.)</p>'
     '<p style="margin-top:8px"><b>Acabo de llegar.</b> (I have JUST arrived.)</p></div>'
     '<p style="margin-top:16px">Acabar de is a gem: English needs "just" + perfect; Spanish needs only acabo de + infinitive. Acabo de comer = I\'ve just eaten.</p>'),
    ('Seguir + gerundio, llevar + gerundio', None,
     '<p class="slide-explanation">Two gerund periphrases express continuation — where English says "still" or "have been ...ing".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Sigo estudiando español.</b> (I am STILL studying Spanish.)</p>'
     '<p style="margin-top:8px"><b>Llevo dos años viviendo aquí.</b> (I have been living here for two years.)</p></div>'
     '<p style="margin-top:16px">Llevar + time + gerundio replaces a whole English perfect-continuous clause. Learn it as a pattern: llevo + duración + -ndo.</p>'),
    ('Volver a + infinitive, dejar de + infinitive', None,
     '<p class="slide-explanation">Repetition and stopping — two more high-frequency periphrases.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>He vuelto a ver esa serie.</b> (I have watched that series AGAIN.)</p>'
     '<p style="margin-top:8px"><b>Dejé de fumar hace un año.</b> (I STOPPED smoking a year ago.)</p></div>'
     '<p style="margin-top:16px">volver a + inf = to do again · dejar de + inf = to stop doing. Both beat clumsy literal translations (otra vez, parar...).</p>'),
    ('When English -ing is a Spanish infinitive', None,
     '<p class="slide-explanation">The biggest English-speaker trap: after prepositions and as a subject, English uses -ing but Spanish uses the <b>infinitive</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Antes de salir, cierra las ventanas.</b> (Before leavING...)</p>'
     '<p style="margin-top:8px"><b>Nadar es bueno para la espalda.</b> (SwimmING is good for your back.)</p>'
     '<p style="margin-top:8px"><b>Gracias por venir.</b> (Thanks for comING.)</p></div>'
     '<p style="margin-top:16px">Rule: preposition + infinitive, subject = infinitive. "Nadando es bueno" is the give-away error of an English speaker.</p>'),
  ],
  traps=[
    ('Nadando es bueno para la salud.', '<strong>Nadar</strong> es bueno para la salud.', 'A verb as subject is the infinitive in Spanish — English -ing does not transfer'),
    ('Gracias por viniendo.', 'Gracias por <strong>venir</strong>.', 'After a preposition Spanish always uses the infinitive: por venir'),
    ('Acabo de comiendo.', 'Acabo de <strong>comer</strong>.', 'acabar de + INFINITIVE: acabo de comer = I have just eaten'),
    ('Estoy aquí desde dos años viviendo.', '<strong>Llevo dos años viviendo</strong> aquí.', 'The natural pattern is llevar + time + gerundio: llevo dos años viviendo'),
    ('Paré de fumar. (understandable but unnatural)', '<strong>Dejé de</strong> fumar.', 'The idiomatic "stop doing" is dejar de + infinitive'),
  ],
  summary=[
    ('Going to', 'ir a + infinitivo', 'Voy a llamarte esta noche.'),
    ('Just did', 'acabar de + infinitivo', 'Acabo de llegar.'),
    ('Still doing', 'seguir + gerundio', 'Sigo estudiando español.'),
    ('Have been doing', 'llevar + tiempo + gerundio', 'Llevo dos años viviendo aquí.'),
    ('Again / stop', 'volver a + inf · dejar de + inf', 'Volví a llamar. / Dejé de fumar.'),
    ('Preposition rule', 'preposición + infinitivo', 'Antes de salir... · Gracias por venir.'),
  ],
  ex1=('Pick the periphrasis', 'Which structure fits the meaning?', [
    ('He acabado... no: I have JUST eaten → ______ comer.', ['Acabo de', 'Voy a', 'Sigo'], 'Acabo de',
     'Just done → ACABO DE + infinitive.'),
    ('I am still working there → ______ trabajando allí.', ['Sigo', 'Acabo de', 'Dejo de'], 'Sigo',
     'Still doing → SIGO + gerundio.'),
    ('I have been studying for three hours → ______ tres horas estudiando.', ['Llevo', 'Tengo', 'Hago'], 'Llevo',
     'Duration + continuing → LLEVO + time + gerundio.'),
    ('She stopped eating meat → ______ comer carne.', ['Dejó de', 'Volvió a', 'Acabó'], 'Dejó de',
     'Stop doing → DEJAR DE + infinitive.'),
    ('We are going to travel in July → ______ viajar en julio.', ['Vamos a', 'Llevamos', 'Seguimos'], 'Vamos a',
     'Future plan → IR A + infinitive.'),
    ('He called again → ______ llamar.', ['Volvió a', 'Dejó de', 'Siguió a'], 'Volvió a',
     'Do again → VOLVER A + infinitive.'),
  ]),
  ex2=('Infinitive, gerund or participle?', 'Type the right form of the verb.', [
    ('Antes de ______, apaga la luz. (salir — after a preposition)', 'salir',
     'Preposition + INFINITIVE: antes de SALIR.'),
    ('Llevo una hora ______ el autobús. (esperar — gerundio)', 'esperando',
     'Llevar + gerundio: ESPERANDO.'),
    ('______ es bueno para el corazón. (correr — as subject)', 'correr',
     'Verb as subject → infinitive: CORRER es bueno.'),
    ('Acabo de ______ las noticias. (ver)', 'ver',
     'Acabar de + infinitive: acabo de VER.'),
    ('Sigue ______ en la misma empresa. (trabajar — gerundio)', 'trabajando',
     'Seguir + gerundio: TRABAJANDO.'),
  ]),
  ex3=('Translate the idea', 'Choose the natural Spanish.', [
    ('"I have just seen Marta":', ['Acabo de ver a Marta.', 'Justo he visto a Marta acabando.', 'Acabé viendo a Marta.'], 'Acabo de ver a Marta.',
     'Just seen → ACABO DE VER.'),
    ('"Thanks for helping me":', ['Gracias por ayudarme.', 'Gracias por ayudándome.', 'Gracias para ayudarme.'], 'Gracias por ayudarme.',
     'Preposition + infinitive, and thanks takes POR: gracias por AYUDARME.'),
    ('"I have been waiting for an hour":', ['Llevo una hora esperando.', 'Estoy esperando desde una hora.', 'He esperado por una hora llevando.'], 'Llevo una hora esperando.',
     'LLEVO + time + gerundio — the natural pattern.'),
    ('"Smoking is bad for you":', ['Fumar es malo para la salud.', 'Fumando es malo para la salud.', 'El fumando es malo.'], 'Fumar es malo para la salud.',
     'Verb as subject → infinitive FUMAR.'),
    ('"She is still living in Madrid":', ['Sigue viviendo en Madrid.', 'Todavía vive viviendo en Madrid.', 'Sigue a vivir en Madrid.'], 'Sigue viviendo en Madrid.',
     'SEGUIR + gerundio: sigue viviendo.'),
  ]),
  game_desc='Each verb periphrasis passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('ir-a', 'ir a + infinitivo', 'to be going to (future plan)', 'future', '<b>Voy a</b> llamarte esta noche.', '______ a llamarte esta noche. (I am going)', 'voy'),
    ('acabar-de', 'acabar de + infinitivo', 'to have just done', 'recent past', '<b>Acabo de</b> llegar.', 'Acabo ______ llegar. (just)', 'de'),
    ('seguir', 'seguir + gerundio', 'to still be doing', 'continuation', '<b>Sigo estudiando</b> español.', 'Sigo ______ español. (studying)', 'estudiando'),
    ('llevar', 'llevar + tiempo + gerundio', 'to have been doing for...', 'duration', '<b>Llevo</b> dos años viviendo aquí.', '______ dos años viviendo aquí. (I have been)', 'llevo'),
    ('volver-a', 'volver a + infinitivo', 'to do again', 'repetition', 'He <b>vuelto a</b> ver esa serie.', 'He vuelto ______ ver esa serie. (again marker)', 'a'),
    ('dejar-de', 'dejar de + infinitivo', 'to stop doing', 'stopping', '<b>Dejé de</b> fumar hace un año.', 'Dejé ______ fumar hace un año. (stop marker)', 'de'),
    ('prep-inf', 'preposición + infinitivo', 'after prepositions: infinitive, not -ing', 'preposition rule', 'Gracias por <b>venir</b>.', 'Gracias por ______. (coming)', 'venir'),
    ('inf-subject', 'infinitivo como sujeto', 'verb as subject = infinitive', 'subject rule', '<b>Nadar</b> es bueno para la espalda.', '______ es bueno para la espalda. (swimming)', 'nadar'),
  ],
),

}
