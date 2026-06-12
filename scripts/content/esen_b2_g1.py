# -*- coding: utf-8 -*-
"""espanol-en B2 grammar content — batch 1 (chapters G1-G5)."""

CHAPTERS = {

'adverbial-clauses': dict(
  num='G1', short='Adverbial Clauses', title='Adverbial Clauses — Cuando vengas, para que sepas',
  subtitle='Time and purpose clauses — and the subjunctive that future time demands',
  slides=[
    ('Cuando + subjunctive for the future', None,
     '<p class="slide-explanation">The headline rule of B2 Spanish: after <b>cuando</b> (and other time links) referring to the <b>future</b>, the verb goes in the <b>subjunctive</b>. English just uses the present — Spanish marks the unreality.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Cuando llegues, llámame.</b> (When you arrive, call me — arrival hasn\'t happened yet.)</p>'
     '<p style="margin-top:8px">Compare habit: <b>Cuando llego a casa, ceno.</b> (When I get home, I have dinner — indicative, routine.)</p></div>'
     '<p style="margin-top:16px">Future reference → <b>llegues</b> (subjunctive). Habit or past → indicative. This contrast is pure B2 exam material.</p>'),
    ('The time-link family', None,
     '<p class="slide-explanation">The same rule covers the whole family of time connectors.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>en cuanto</b> (as soon as) — <b>En cuanto sepa algo, te aviso.</b></p>'
     '<p style="margin-top:8px"><b>hasta que</b> (until) — <b>Espera aquí hasta que vuelva.</b></p>'
     '<p style="margin-top:8px"><b>antes de que</b> (before) — <b>Sal antes de que llueva.</b> (ALWAYS subjunctive)</p>'
     '<p style="margin-top:8px"><b>después de que</b> (after) — <b>Después de que termines, hablamos.</b></p></div>'
     '<p style="margin-top:16px">antes de que is special: it takes the subjunctive even for past events — the "before" event is always unrealised at that point.</p>'),
    ('Para que — purpose needs the subjunctive', None,
     '<p class="slide-explanation">Purpose clauses with <b>para que</b> (so that) always take the subjunctive — the goal is wished, not yet real.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Te lo explico para que lo entiendas.</b> (I\'m explaining so that you understand.)</p>'
     '<p style="margin-top:8px"><b>Habla más alto para que te oigan.</b> (Speak up so they can hear you.)</p></div>'
     '<p style="margin-top:16px">Same subject? Drop que and use the infinitive: Estudio <b>para aprobar</b> (I study to pass) — not "para que yo apruebe".</p>'),
    ('Aunque — two meanings, two moods', None,
     '<p class="slide-explanation"><b>Aunque</b> + indicative states a known fact ("although"); aunque + subjunctive concedes a possibility ("even if").</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Aunque llueve, vamos a salir.</b> (Although it IS raining — I can see it — we\'ll go out.)</p>'
     '<p style="margin-top:8px"><b>Aunque llueva, vamos a salir.</b> (Even if it rains — who knows — we\'ll go out.)</p></div>'
     '<p style="margin-top:16px">One vowel changes the meaning: llueve = fact, llueva = hypothesis. Examiners adore this pair.</p>'),
    ('Mientras, siempre que — conditions in disguise', None,
     '<p class="slide-explanation">Some connectors carry conditions: <b>mientras</b> (as long as) and <b>siempre que</b> (provided that) take the subjunctive when they mean a condition.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Puedes salir siempre que vuelvas antes de las doce.</b> (You can go out provided you\'re back by twelve.)</p>'
     '<p style="margin-top:8px"><b>Mientras vivas en esta casa, seguirás mis reglas.</b> (As long as you live in this house...)</p></div>'
     '<p style="margin-top:16px">Time meaning ("while") → indicative: Mientras yo cocinaba, él ponía la mesa. Condition → subjunctive.</p>'),
  ],
  traps=[
    ('Cuando llegarás, llámame.', 'Cuando <strong>llegues</strong>, llámame.', 'Never the future after cuando — future time takes the present subjunctive: llegues'),
    ('Cuando llegas mañana, llámame.', 'Cuando <strong>llegues</strong> mañana, llámame.', 'Future reference needs the subjunctive, not the present indicative'),
    ('Te lo digo para que lo sabes.', 'Te lo digo para que lo <strong>sepas</strong>.', 'para que always triggers the subjunctive: sepas'),
    ('Estudio para que yo apruebe.', 'Estudio <strong>para aprobar</strong>.', 'Same subject → para + infinitive, no que clause'),
    ('Espera hasta que vuelvo.', 'Espera hasta que <strong>vuelva</strong>.', 'hasta que + future event → subjunctive: vuelva'),
  ],
  summary=[
    ('Future time', 'cuando/en cuanto/hasta que + subjuntivo', 'Cuando llegues, llámame.'),
    ('Habit or past', 'cuando + indicativo', 'Cuando llego a casa, ceno.'),
    ('Before', 'antes de que + subjuntivo (always)', 'Sal antes de que llueva.'),
    ('Purpose', 'para que + subjuntivo', 'Te lo explico para que lo entiendas.'),
    ('Same subject', 'para + infinitivo', 'Estudio para aprobar.'),
    ('Although vs even if', 'aunque + ind. (fact) / subj. (hypothesis)', 'Aunque llueve... / Aunque llueva...'),
  ],
  ex1=('Indicative or subjunctive?', 'Future reference is the key.', [
    ('Cuando ______ a casa, te llamo. (yo, llegar — tonight)', ['llegue', 'llego', 'llegaré'], 'llegue',
     'Future reference after cuando → subjunctive: LLEGUE.'),
    ('Cuando ______ a casa, siempre ceno a las nueve. (yo, llegar — habit)', ['llego', 'llegue', 'llegaré'], 'llego',
     'Habit → indicative: LLEGO.'),
    ('En cuanto ______ algo, te aviso. (yo, saber)', ['sepa', 'sé', 'sabré'], 'sepa',
     'En cuanto + future → subjunctive: SEPA.'),
    ('Te presto el coche para que no ______ tarde. (tú, llegar)', ['llegues', 'llegas', 'llegarás'], 'llegues',
     'para que → subjunctive: LLEGUES.'),
    ('Aunque ______ frío ahora mismo, no pienso ponerme el abrigo. (hacer — I can feel it)', ['hace', 'haga', 'hará'], 'hace',
     'Known fact → indicative: aunque HACE frío.'),
    ('No saldrás hasta que ______ los deberes. (terminar, tú)', ['termines', 'terminas', 'terminarás'], 'termines',
     'hasta que + future event → subjunctive: TERMINES.'),
  ]),
  ex2=('Complete the clause', 'Type the verb in the right mood.', [
    ('Call me when you arrive. → Llámame cuando ______. (llegar, tú)', 'llegues',
     'Future after cuando → subjunctive LLEGUES.'),
    ('Leave before it rains. → Sal antes de que ______. (llover)', 'llueva',
     'antes de que → always subjunctive: LLUEVA.'),
    ('I work to live. (same subject) → Trabajo para ______. (one word)', 'vivir',
     'Same subject → infinitive: para VIVIR.'),
    ('Speak up so they hear you. → Habla alto para que te ______. (oír, ellos)', 'oigan',
     'para que → subjunctive: OIGAN.'),
    ('Even if it costs a lot, I\'ll buy it. → Aunque ______ mucho, lo compraré. (costar)', 'cueste',
     'Hypothesis → subjunctive: CUESTE.'),
  ]),
  ex3=('Fact or hypothesis?', 'Choose the sentence that matches the meaning.', [
    ('"Although it IS expensive (we know), it\'s worth it":', ['Aunque es caro, merece la pena.', 'Aunque sea caro, merece la pena.', 'Aunque será caro, merece la pena.'], 'Aunque es caro, merece la pena.',
     'Known fact → indicative ES.'),
    ('"Even if it\'s expensive (no idea), I\'ll buy it":', ['Aunque sea caro, lo compraré.', 'Aunque es caro, lo compraré.', 'Aunque era caro, lo compraré.'], 'Aunque sea caro, lo compraré.',
     'Concession of a possibility → subjunctive SEA.'),
    ('"As soon as the meeting ends, I\'ll call you":', ['En cuanto termine la reunión, te llamo.', 'En cuanto termina la reunión, te llamo.', 'En cuanto terminará la reunión, te llamo.'], 'En cuanto termine la reunión, te llamo.',
     'Future → subjunctive TERMINE.'),
    ('"You can use my car provided you fill the tank":', ['Puedes usar mi coche siempre que llenes el depósito.', 'Puedes usar mi coche siempre que llenas el depósito.', 'Puedes usar mi coche siempre que llenarás el depósito.'], 'Puedes usar mi coche siempre que llenes el depósito.',
     'Condition → subjunctive LLENES.'),
    ('"While I was cooking, he set the table" (time, past):', ['Mientras yo cocinaba, él ponía la mesa.', 'Mientras yo cocinara, él pusiera la mesa.', 'Mientras yo cocine, él ponga la mesa.'], 'Mientras yo cocinaba, él ponía la mesa.',
     'Pure time in the past → indicative imperfects.'),
  ]),
  game_desc='Each connector passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('cuando-subj', 'cuando + subjuntivo', 'when (future) — subjunctive required', 'future time', '<b>Cuando llegues</b>, llámame.', 'Cuando ______, llámame. (you arrive — subjunctive)', 'llegues'),
    ('en-cuanto', 'en cuanto', 'as soon as', 'time link', '<b>En cuanto</b> sepa algo, te aviso.', 'En ______ sepa algo, te aviso. (as soon as)', 'cuanto'),
    ('hasta-que', 'hasta que + subj.', 'until (future event)', 'until', 'Espera aquí <b>hasta que</b> vuelva.', 'Espera aquí hasta que ______. (I return — subjunctive)', 'vuelva'),
    ('antes-de-que', 'antes de que + subj.', 'before (always subjunctive)', 'before', 'Sal <b>antes de que</b> llueva.', 'Sal antes de que ______. (it rains)', 'llueva'),
    ('para-que', 'para que + subj.', 'so that (purpose)', 'purpose', 'Te lo explico <b>para que</b> lo entiendas.', 'Te lo explico para que lo ______. (you understand)', 'entiendas'),
    ('para-inf', 'para + infinitivo', 'in order to (same subject)', 'infinitive purpose', 'Estudio <b>para aprobar</b>.', 'Estudio para ______. (to pass)', 'aprobar'),
    ('aunque-ind', 'aunque + indicativo', 'although (known fact)', 'fact', '<b>Aunque llueve</b>, vamos a salir.', 'Aunque ______, vamos a salir. (it is raining — fact)', 'llueve'),
    ('aunque-subj', 'aunque + subjuntivo', 'even if (hypothesis)', 'hypothesis', '<b>Aunque llueva</b>, vamos a salir.', 'Aunque ______, vamos a salir. (it rains — even if)', 'llueva'),
  ],
),

'causative-verbs': dict(
  num='G2', short='Causative Verbs', title='Causative Verbs — Hacer, dejar, mandar',
  subtitle='Making, letting and getting things done in Spanish',
  slides=[
    ('Hacer + infinitive — to make someone do', None,
     '<p class="slide-explanation">Spanish causation is beautifully simple: <b>hacer + infinitive</b> = to make someone do something. No extra particles.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Esa película me hizo llorar.</b> (That film made me cry.)</p>'
     '<p style="margin-top:8px"><b>El profesor nos hace repetir los verbos.</b> (The teacher makes us repeat the verbs.)</p></div>'
     '<p style="margin-top:16px">The person affected becomes a pronoun: me hizo llorar, te hará reír, nos hizo esperar.</p>'),
    ('Dejar + infinitive — to let', None,
     '<p class="slide-explanation"><b>Dejar + infinitive</b> = to let/allow. Its negative is the everyday way to say "won\'t let".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Mis padres no me dejan salir entre semana.</b> (My parents don\'t let me go out on weekdays.)</p>'
     '<p style="margin-top:8px"><b>Déjame pensar un momento.</b> (Let me think for a moment.)</p></div>'
     '<p style="margin-top:16px">Alternative with the subjunctive: No dejan que salga. Both correct; the infinitive version is lighter.</p>'),
    ('Mandar and pedir — ordering and asking', None,
     '<p class="slide-explanation"><b>Mandar + infinitive</b> = to order/have someone do. <b>Pedir que + subjunctive</b> = to ask someone to do.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>El médico me mandó descansar.</b> (The doctor told me to rest.)</p>'
     '<p style="margin-top:8px"><b>Le pedí que me ayudara.</b> (I asked him to help me.)</p></div>'
     '<p style="margin-top:16px">English "ask someone TO do" hides a Spanish subjunctive: pedir que + subjuntivo, never "pedir a alguien a hacer".</p>'),
    ('Getting things done: hacerse + infinitive', None,
     '<p class="slide-explanation">English "I had my hair cut" — you didn\'t cut it yourself. Spanish handles this with <b>cortarse el pelo</b> (context implies the hairdresser) or explicitly with hacerse + infinitive.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Me corté el pelo ayer.</b> (I had my hair cut yesterday — everyone understands the hairdresser did it.)</p>'
     '<p style="margin-top:8px"><b>Se hizo construir una casa en la sierra.</b> (He had a house built in the mountains.)</p></div>'
     '<p style="margin-top:16px">Don\'t translate "I had it done" word by word — Spanish either uses the reflexive or hacerse + infinitive.</p>'),
    ('Dejar\'s other lives', None,
     '<p class="slide-explanation">Dejar moonlights in several meanings — learn the family.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>dejar de + inf</b> = to stop: <b>Dejó de fumar.</b></p>'
     '<p style="margin-top:8px"><b>dejar + object</b> = to leave (something): <b>Dejé las llaves en casa.</b></p>'
     '<p style="margin-top:8px"><b>dejar prestado</b> = to lend: <b>¿Me dejas el boli?</b> (everyday "lend")</p></div>'
     '<p style="margin-top:16px">¿Me dejas...? is how Spaniards actually ask to borrow things — far more common than prestar in speech.</p>'),
  ],
  traps=[
    ('La película me hizo a llorar.', 'La película <strong>me hizo llorar</strong>.', 'hacer + infinitive directly — no a in between'),
    ('Mis padres no me dejan que salir.', 'Mis padres no me <strong>dejan salir</strong>.', 'dejar + infinitive (or dejan que + subjunctive) — never que + infinitive'),
    ('Le pedí ayudarme.', 'Le pedí <strong>que me ayudara</strong>.', 'pedir needs que + subjunctive when someone else does the action'),
    ('Hice cortar mi pelo.', '<strong>Me corté el pelo.</strong>', 'Services on yourself use the reflexive — me corté el pelo = I had my hair cut'),
    ('¿Me prestas el boli? (fine, but bookish in Spain)', '¿Me <strong>dejas</strong> el boli?', 'Everyday borrowing uses dejar: ¿me dejas...?'),
  ],
  summary=[
    ('Make', 'hacer + infinitivo', 'Me hizo llorar.'),
    ('Let', 'dejar + infinitivo', 'No me dejan salir.'),
    ('Order', 'mandar + infinitivo', 'El médico me mandó descansar.'),
    ('Ask to', 'pedir que + subjuntivo', 'Le pedí que me ayudara.'),
    ('Have done (self)', 'reflexive', 'Me corté el pelo.'),
    ('Lend (colloquial)', '¿me dejas...?', '¿Me dejas el boli?'),
  ],
  ex1=('Choose the causative', 'hacer, dejar, mandar or pedir?', [
    ('Esa canción siempre me ______ llorar.', ['hace', 'deja', 'pide'], 'hace',
     'To make someone do → HACER: me hace llorar.'),
    ('Mis padres no me ______ ver la tele entre semana.', ['dejan', 'hacen', 'mandan'], 'dejan',
     'To let → DEJAR: no me dejan ver.'),
    ('El médico le ______ guardar cama una semana.', ['mandó', 'dejó', 'pidió a'], 'mandó',
     'Doctor\'s orders → MANDÓ guardar cama.'),
    ('Le ______ que me acompañara al aeropuerto.', ['pedí', 'hice', 'dejé'], 'pedí',
     'To ask someone to → PEDIR que + subjunctive.'),
    ('¿Me ______ tu diccionario un momento?', ['dejas', 'haces', 'mandas'], 'dejas',
     'Everyday lending → ¿me DEJAS...?'),
    ('El humo nos ______ toser a todos.', ['hizo', 'dejó', 'pidió'], 'hizo',
     'Cause → HIZO toser.'),
  ]),
  ex2=('Build the structure', 'Type the missing word.', [
    ('That joke made me laugh. → Ese chiste me hizo ______. (one word)', 'reír',
     'hacer + infinitive: me hizo REÍR.'),
    ('Let me see! → ¡______ ver! (déjame as one word)', 'déjame',
     'dejar + pronoun attached: DÉJAME ver.'),
    ('She stopped smoking. → ______ de fumar. (dejar, indefinido, ella)', 'dejó',
     'dejar de + infinitive: DEJÓ de fumar.'),
    ('I had my hair cut. → Me ______ el pelo. (cortar, indefinido)', 'corté',
     'Reflexive service: me CORTÉ el pelo.'),
    ('I asked her to come. → Le pedí ______ viniera. (one word)', 'que',
     'pedir QUE + subjunctive: le pedí QUE viniera.'),
  ]),
  ex3=('Natural Spanish', 'Pick the version a native would say.', [
    ('"My boss makes us work weekends":', ['Mi jefe nos hace trabajar los fines de semana.', 'Mi jefe nos hace a trabajar los fines de semana.', 'Mi jefe hace que nosotros trabajar.'], 'Mi jefe nos hace trabajar los fines de semana.',
     'hacer + infinitive, person as pronoun: nos hace trabajar.'),
    ('"They won\'t let me park here":', ['No me dejan aparcar aquí.', 'No me dejan que aparcar aquí.', 'No me hacen aparcar aquí.'], 'No me dejan aparcar aquí.',
     'Let → dejar + infinitive.'),
    ('"I\'ll have the documents sent" (formal):', ['Mandaré enviar los documentos.', 'Haré que enviado los documentos.', 'Enviaré hacer los documentos.'], 'Mandaré enviar los documentos.',
     'mandar + infinitive = have something done.'),
    ('"Can I borrow your charger?":', ['¿Me dejas el cargador?', '¿Me haces el cargador?', '¿Puedo prestar tu cargador?'], '¿Me dejas el cargador?',
     'Everyday borrowing → ¿me dejas...?'),
    ('"The teacher had us write an essay":', ['La profesora nos mandó escribir una redacción.', 'La profesora nos escribió hacer una redacción.', 'La profesora hizo que nosotros escribir.'], 'La profesora nos mandó escribir una redacción.',
     'mandar + infinitive: nos mandó escribir.'),
  ]),
  game_desc='Each causative structure passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('hacer-inf', 'hacer + infinitivo', 'to make someone do', 'causation', 'La película me <b>hizo llorar</b>.', 'La película me hizo ______. (cry)', 'llorar'),
    ('dejar-inf', 'dejar + infinitivo', 'to let / allow', 'permission', 'No me <b>dejan salir</b> entre semana.', 'No me dejan ______ entre semana. (go out)', 'salir'),
    ('dejame', '¡Déjame...!', 'let me...!', 'requests', '<b>Déjame</b> pensar un momento.', '______ pensar un momento. (let me)', 'déjame'),
    ('mandar', 'mandar + infinitivo', 'to order / have someone do', 'orders', 'El médico me <b>mandó</b> descansar.', 'El médico me ______ descansar. (ordered)', 'mandó'),
    ('pedir-que', 'pedir que + subjuntivo', 'to ask someone to do', 'requests', 'Le <b>pedí que</b> me ayudara.', 'Le pedí ______ me ayudara. (that)', 'que'),
    ('me-corte', 'me corté el pelo', 'I had my hair cut (reflexive)', 'services', '<b>Me corté</b> el pelo ayer.', 'Me ______ el pelo ayer. (had cut)', 'corté'),
    ('dejar-de', 'dejar de + infinitivo', 'to stop doing', 'stopping', '<b>Dejó de</b> fumar hace un año.', 'Dejó ______ fumar hace un año. (stop marker)', 'de'),
    ('me-dejas', '¿me dejas...?', 'can I borrow...? (colloquial)', 'borrowing', '¿<b>Me dejas</b> el boli?', '¿Me ______ el boli? (will you lend)', 'dejas'),
  ],
),

'cleft-sentences': dict(
  num='G3', short='Emphasis', title='Emphasis — Lo que necesito es...',
  subtitle='Cleft sentences and fronting: putting the spotlight where you want it',
  slides=[
    ('Lo que ... es — the workhorse cleft', None,
     '<p class="slide-explanation">To emphasise WHAT, wrap it in <b>lo que ... es</b> — exactly like English "what I need is...".</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Lo que necesito es dormir.</b> (What I need is sleep.)</p>'
     '<p style="margin-top:8px"><b>Lo que más me molesta es el ruido.</b> (What annoys me most is the noise.)</p></div>'
     '<p style="margin-top:16px">Pattern: Lo que + clause + es + the highlighted element. Instantly upgrades your spoken and written Spanish.</p>'),
    ('Fue ... quien — emphasising the person', None,
     '<p class="slide-explanation">To emphasise WHO, use <b>ser ... quien/el que</b>. The tense of ser matches the action.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Fue María quien encontró las llaves.</b> (It was María who found the keys.)</p>'
     '<p style="margin-top:8px"><b>Es mi hermano el que cocina en casa.</b> (It\'s my brother who cooks at home.)</p></div>'
     '<p style="margin-top:16px">Fue ... quien for past events, es ... el que/quien for present habits. The verb after quien agrees normally.</p>'),
    ('Fronting: Eso no lo sé', None,
     '<p class="slide-explanation">Spanish loves moving the object to the front for emphasis — but when you do, you must <b>repeat it as a pronoun</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Eso no lo sé.</b> (THAT I don\'t know — eso fronted, lo repeats it.)</p>'
     '<p style="margin-top:8px"><b>A Juan no lo he visto hoy.</b> (Juan I haven\'t seen today.)</p>'
     '<p style="margin-top:8px"><b>El postre lo traigo yo.</b> (The dessert, I\'m bringing.)</p></div>'
     '<p style="margin-top:16px">The duplicate pronoun (lo, la, los, las) is obligatory — "Eso no sé" sounds broken.</p>'),
    ('Es ... lo que / donde / cuando', None,
     '<p class="slide-explanation">The cleft family extends to places, times and things.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Es aquí donde nos conocimos.</b> (It\'s here that we met.)</p>'
     '<p style="margin-top:8px"><b>Fue entonces cuando lo entendí.</b> (It was then that I understood.)</p>'
     '<p style="margin-top:8px"><b>Es el precio lo que no me convence.</b> (It\'s the price that doesn\'t convince me.)</p></div>'
     '<p style="margin-top:16px">Match the connector to the element: place → donde, time → cuando, thing → lo que. Never plain "que" here.</p>'),
    ('Everyday emphasis tools', None,
     '<p class="slide-explanation">Two more native-sounding intensifiers for conversation.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Sí que</b>: <b>Esta paella sí que está buena.</b> (This paella really IS good.)</p>'
     '<p style="margin-top:8px"><b>Lo + adjective + que</b>: <b>No sabes lo cansada que estoy.</b> (You don\'t know HOW tired I am.)</p></div>'
     '<p style="margin-top:16px">lo cansada que estoy — the adjective agrees (cansadA, speaker is female) even after neutral lo.</p>'),
  ],
  traps=[
    ('Qué necesito es dormir.', '<strong>Lo que</strong> necesito es dormir.', 'The cleft "what" is lo que — qué is only for questions'),
    ('Eso no sé.', 'Eso no <strong>lo</strong> sé.', 'A fronted object must be doubled with a pronoun: eso no LO sé'),
    ('Fue María que encontró las llaves.', 'Fue María <strong>quien</strong> encontró las llaves.', 'Cleft persons take quien (or la que) — not bare que'),
    ('Es aquí que nos conocimos.', 'Es aquí <strong>donde</strong> nos conocimos.', 'Place clefts use donde — "es aquí que" is a French calque'),
    ('No sabes lo cansado que estoy. (female speaker)', 'No sabes lo <strong>cansada</strong> que estoy.', 'In lo + adjective + que, the adjective still agrees with the speaker'),
  ],
  summary=[
    ('What-cleft', 'lo que ... es ...', 'Lo que necesito es dormir.'),
    ('Who-cleft', 'fue/es ... quien ...', 'Fue María quien encontró las llaves.'),
    ('Fronting', 'object first + duplicate pronoun', 'Eso no lo sé. · El postre lo traigo yo.'),
    ('Place / time', 'es ... donde / fue ... cuando', 'Es aquí donde nos conocimos.'),
    ('Really is', 'sí que + verb', 'Esta paella sí que está buena.'),
    ('How + adj', 'lo + adjetivo + que', 'No sabes lo cansada que estoy.'),
  ],
  ex1=('Build the emphasis', 'Cleft it the Spanish way.', [
    ('______ más me gusta de Madrid es la vida nocturna.', ['Lo que', 'Qué', 'Que'], 'Lo que',
     'What-cleft → LO QUE más me gusta...'),
    ('Fue mi abuela ______ me enseñó a cocinar.', ['quien', 'que cual', 'cuya'], 'quien',
     'Person cleft → QUIEN me enseñó.'),
    ('Es en Sevilla ______ se come el mejor gazpacho.', ['donde', 'que', 'cuando'], 'donde',
     'Place cleft → DONDE.'),
    ('El vino ______ traigo yo, tú trae el postre.', ['lo', 'le', 'él'], 'lo',
     'Fronted object needs its duplicate: el vino LO traigo yo.'),
    ('Fue en 2015 ______ nos mudamos aquí.', ['cuando', 'donde', 'que'], 'cuando',
     'Time cleft → CUANDO.'),
    ('Este restaurante ______ que es caro.', ['sí', 'si', 'más'], 'sí',
     'Emphatic really → SÍ QUE es caro.'),
  ]),
  ex2=('Type the missing piece', 'Clefts and fronting.', [
    ('What I want is peace. → ______ ______ quiero es tranquilidad. (two words)', 'lo que',
     'What-cleft → LO QUE quiero es...'),
    ('THAT I don\'t understand. → Eso no ______ entiendo. (one word)', 'lo',
     'Fronting needs the duplicate pronoun LO.'),
    ('It was Juan who called. → Fue Juan ______ llamó. (one word)', 'quien',
     'Person cleft → QUIEN llamó.'),
    ('It\'s here that I live. → Es aquí ______ vivo. (one word)', 'donde',
     'Place cleft → DONDE vivo.'),
    ('You don\'t know HOW expensive it is. → No sabes ______ caro que es. (one word)', 'lo',
     'lo + adjective + que: LO caro que es.'),
  ]),
  ex3=('Most natural version', 'Which sentence sounds Spanish?', [
    ('Emphasising the dessert:', ['El postre lo traigo yo.', 'El postre traigo yo.', 'Traigo el postre lo yo.'], 'El postre lo traigo yo.',
     'Fronted object + duplicate LO.'),
    ('"It was then that everything changed":', ['Fue entonces cuando todo cambió.', 'Fue entonces que todo cambió.', 'Era entonces donde todo cambió.'], 'Fue entonces cuando todo cambió.',
     'Time cleft → fue entonces CUANDO.'),
    ('"What worries me is the exam":', ['Lo que me preocupa es el examen.', 'Qué me preocupa es el examen.', 'Que me preocupa está el examen.'], 'Lo que me preocupa es el examen.',
     'LO QUE me preocupa es...'),
    ('"This film really is good":', ['Esta película sí que es buena.', 'Esta película sí es que buena.', 'Esta película que sí es buena.'], 'Esta película sí que es buena.',
     'SÍ QUE + verb.'),
    ('"Juan I haven\'t seen today":', ['A Juan no lo he visto hoy.', 'Juan no he visto hoy.', 'A Juan no he visto lo hoy.'], 'A Juan no lo he visto hoy.',
     'Personal a + fronting + duplicate LO.'),
  ]),
  game_desc='Each emphasis structure passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('lo-que-es', 'lo que ... es', 'what ... is (cleft)', 'what-cleft', '<b>Lo que</b> necesito <b>es</b> dormir.', '______ que necesito es dormir. (what)', 'lo'),
    ('fue-quien', 'fue ... quien', 'it was ... who', 'who-cleft', '<b>Fue</b> María <b>quien</b> encontró las llaves.', 'Fue María ______ encontró las llaves. (who)', 'quien'),
    ('eso-no-lo-se', 'Eso no lo sé', 'THAT I don\'t know (fronting + pronoun)', 'fronting', '<b>Eso no lo sé.</b>', 'Eso no ______ sé. (duplicate pronoun)', 'lo'),
    ('es-donde', 'es ... donde', 'it\'s ... where (place cleft)', 'place', 'Es aquí <b>donde</b> nos conocimos.', 'Es aquí ______ nos conocimos. (where)', 'donde'),
    ('fue-cuando', 'fue ... cuando', 'it was ... when (time cleft)', 'time', 'Fue entonces <b>cuando</b> lo entendí.', 'Fue entonces ______ lo entendí. (when)', 'cuando'),
    ('si-que', 'sí que', 'really / certainly (emphasis)', 'intensifier', 'Esta paella <b>sí que</b> está buena.', 'Esta paella ______ que está buena. (really)', 'sí'),
    ('lo-adj-que', 'lo + adjetivo + que', 'how + adjective (exclamation)', 'how-cleft', 'No sabes <b>lo cansada que</b> estoy.', 'No sabes lo ______ que estoy. (tired — fem.)', 'cansada'),
    ('el-postre-lo', 'el postre lo traigo yo', 'fronted object + duplicate', 'duplication', '<b>El postre lo traigo</b> yo.', 'El postre ______ traigo yo. (it)', 'lo'),
  ],
),

'conditional-advanced': dict(
  num='G4', short='Conditionals', title='Conditionals — Si tuviera, si hubiera sabido',
  subtitle='Unreal present and past: the imperfect subjunctive earns its keep',
  slides=[
    ('The second conditional: si + imperfect subjunctive', None,
     '<p class="slide-explanation">Unreal present/future conditions: <b>si + imperfecto de subjuntivo, condicional</b>. You met the chunks at B1 — now own the full pattern.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Si tuviera más tiempo, aprendería a tocar el piano.</b> (If I had more time, I would learn the piano.)</p>'
     '<p style="margin-top:8px"><b>Si fueras más amable, tendrías más amigos.</b> (If you were kinder, you\'d have more friends.)</p></div>'
     '<p style="margin-top:16px">Never the conditional in the si-clause: si tendría is the error that screams "English speaker".</p>'),
    ('Forming the imperfect subjunctive', None,
     '<p class="slide-explanation">Take the <b>ellos form of the indefinido</b>, drop -ron, add <b>-ra endings</b>. All the indefinido\'s irregularity comes along free.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>hablaron → <b>hablara, hablaras, hablara, habláramos, hablarais, hablaran</b></p>'
     '<p style="margin-top:8px">tuvieron → <b>tuviera</b> · fueron → <b>fuera</b> · hicieron → <b>hiciera</b> · pudieron → <b>pudiera</b></p></div>'
     '<p style="margin-top:16px">There is also a -se form (hablase, tuviese) — same meaning. Recognise both, produce the -ra form.</p>'),
    ('The third conditional: regrets', None,
     '<p class="slide-explanation">Unreal PAST: <b>si + hubiera + participio, habría + participio</b>. The grammar of regret and relief.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Si hubiera sabido, no habría venido.</b> (If I had known, I wouldn\'t have come.)</p>'
     '<p style="margin-top:8px"><b>Si hubieras estudiado, habrías aprobado.</b> (If you had studied, you would have passed.)</p></div>'
     '<p style="margin-top:16px">Spanish also accepts hubiera in BOTH halves: si hubiera sabido, no hubiera venido — common in speech.</p>'),
    ('Como si — as if', None,
     '<p class="slide-explanation"><b>Como si</b> (as if) always takes the imperfect (or pluperfect) subjunctive — the comparison is unreal by definition.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Habla como si lo supiera todo.</b> (He talks as if he knew everything.)</p>'
     '<p style="margin-top:8px"><b>Me miró como si no me hubiera visto nunca.</b> (She looked at me as if she had never seen me.)</p></div>'
     '<p style="margin-top:16px">como si + supiera (imperfect subj.) for present unreality, + hubiera visto (pluperfect subj.) for past unreality.</p>'),
    ('Softer conditions: de + infinitive, yo que tú', None,
     '<p class="slide-explanation">Two elegant alternatives for advanced writing and speech.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>De haberlo sabido, habría venido antes.</b> (Had I known, I\'d have come earlier — de + compound infinitive.)</p>'
     '<p style="margin-top:8px"><b>Yo que tú, aceptaría la oferta.</b> (If I were you, I\'d accept the offer.)</p></div>'
     '<p style="margin-top:16px">De haberlo sabido is formal/written; yo que tú is everyday advice. Both replace a full si-clause.</p>'),
  ],
  traps=[
    ('Si tendría dinero, viajaría.', 'Si <strong>tuviera</strong> dinero, viajaría.', 'The si-clause never takes the conditional — imperfect subjunctive: tuviera'),
    ('Si hubiera sabido, no vendría. (past regret)', 'Si hubiera sabido, no <strong>habría venido</strong>.', 'Past condition → past result: habría venido (or hubiera venido)'),
    ('Habla como si sabe todo.', 'Habla como si lo <strong>supiera</strong> todo.', 'como si demands the imperfect subjunctive: supiera'),
    ('Si yo era tú, aceptaría.', '<strong>Yo que tú</strong>, aceptaría. / Si yo <strong>fuera</strong> tú...', '"If I were you" needs fuera (subjunctive) — or the idiom yo que tú'),
    ('Si habría estudiado, habría aprobado.', 'Si <strong>hubiera</strong> estudiado, habría aprobado.', 'Third conditional si-clause: hubiera + participle, never habría'),
  ],
  summary=[
    ('Unreal present', 'si + imperf. subj., condicional', 'Si tuviera tiempo, viajaría.'),
    ('Imperf. subj.', 'ellos indefinido − ron + -ra', 'tuvieron → tuviera · fueron → fuera'),
    ('Unreal past', 'si + hubiera + part., habría + part.', 'Si hubiera sabido, no habría venido.'),
    ('As if', 'como si + imperf./plusc. subj.', 'Habla como si lo supiera todo.'),
    ('Formal alternative', 'de + (haber +) infinitivo', 'De haberlo sabido, habría venido.'),
    ('If I were you', 'yo que tú + condicional', 'Yo que tú, aceptaría la oferta.'),
  ],
  ex1=('Complete the conditional', 'Which form goes in each slot?', [
    ('Si ______ rico, me compraría una isla. (ser)', ['fuera', 'sería', 'era'], 'fuera',
     'Si-clause → imperfect subjunctive: FUERA.'),
    ('Si tuviera tu edad, ______ el mundo. (recorrer)', ['recorrería', 'recorriera', 'recorro'], 'recorrería',
     'Main clause → conditional: RECORRERÍA.'),
    ('Si ______ sabido la verdad, te lo habría dicho. (haber)', ['hubiera', 'habría', 'había'], 'hubiera',
     'Third conditional si-clause → HUBIERA sabido.'),
    ('Si hubieras venido, te ______ encantado. (haber)', ['habría', 'hubieras', 'habías'], 'habría',
     'Result clause → HABRÍA encantado.'),
    ('Gasta dinero como si ______ millonario. (ser)', ['fuera', 'es', 'sería'], 'fuera',
     'como si → imperfect subjunctive: FUERA.'),
    ('Yo que tú, no ______ ese contrato. (firmar)', ['firmaría', 'firmara', 'firmo'], 'firmaría',
     'Yo que tú + conditional: FIRMARÍA.'),
  ]),
  ex2=('Form the subjunctive', 'From the ellos-indefinido.', [
    ('tener → Si ______ más tiempo, leería más. (yo)', 'tuviera',
     'tuvieron → TUVIERA.'),
    ('poder → Si ______ ayudarte, lo haría. (yo)', 'pudiera',
     'pudieron → PUDIERA.'),
    ('hacer → Si ______ mejor tiempo, saldríamos. (hacer, 3rd sing.)', 'hiciera',
     'hicieron → HICIERA.'),
    ('saber → De haberlo ______, habría venido. (participle)', 'sabido',
     'de haber + participle: SABIDO.'),
    ('estudiar → Si hubieras ______, habrías aprobado. (participle)', 'estudiado',
     'hubiera + participle: ESTUDIADO.'),
  ]),
  ex3=('Regrets and hypotheses', 'Choose the correct sentence.', [
    ('"If I won the lottery, I\'d quit my job":', ['Si me tocara la lotería, dejaría el trabajo.', 'Si me tocaría la lotería, dejara el trabajo.', 'Si me toca la lotería, dejaría dejara el trabajo.'], 'Si me tocara la lotería, dejaría el trabajo.',
     'Unreal present: tocara (subj.) + dejaría (cond.).'),
    ('"If you had told me, I would have helped you":', ['Si me lo hubieras dicho, te habría ayudado.', 'Si me lo habrías dicho, te hubiera ayudado mal.', 'Si me lo dijeras ayer, te ayudaría.'], 'Si me lo hubieras dicho, te habría ayudado.',
     'Past unreal: hubieras dicho + habría ayudado.'),
    ('"She treats me as if I were a child":', ['Me trata como si fuera un niño.', 'Me trata como si soy un niño.', 'Me trata como si sería un niño.'], 'Me trata como si fuera un niño.',
     'como si + FUERA.'),
    ('"Had I known..." (formal):', ['De haberlo sabido...', 'De lo saber...', 'De haberlo sabiendo...'], 'De haberlo sabido...',
     'de + haber + participle: de haberlo sabido.'),
    ('"If I were you, I\'d see a doctor":', ['Yo que tú, iría al médico.', 'Yo que tú, fuera al médico.', 'Si yo sería tú, iría al médico.'], 'Yo que tú, iría al médico.',
     'Yo que tú + conditional: iría.'),
  ]),
  game_desc='Each conditional pattern passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('si-tuviera', 'si tuviera..., ...ría', 'if I had..., I would...', '2nd conditional', '<b>Si tuviera</b> tiempo, viajaría más.', 'Si ______ tiempo, viajaría más. (I had)', 'tuviera'),
    ('fuera', 'fuera', 'were (imperf. subj. of ser)', 'ser → fuera', 'Si <b>fuera</b> rico, me compraría una isla.', 'Si ______ rico, me compraría una isla. (I were)', 'fuera'),
    ('hubiera-sabido', 'si hubiera sabido', 'if I had known', '3rd conditional', '<b>Si hubiera sabido</b>, no habría venido.', 'Si ______ sabido, no habría venido. (I had)', 'hubiera'),
    ('habria-venido', 'habría venido', 'I would have come', 'past result', 'No <b>habría venido</b>.', 'No ______ venido. (I would have)', 'habría'),
    ('como-si', 'como si + subj.', 'as if (always subjunctive)', 'unreal comparison', 'Habla <b>como si</b> lo supiera todo.', 'Habla como ______ lo supiera todo. (if)', 'si'),
    ('supiera', 'supiera', 'knew (imperf. subj. of saber)', 'saber → supiera', 'Como si lo <b>supiera</b> todo.', 'Como si lo ______ todo. (he knew)', 'supiera'),
    ('de-haberlo', 'de haberlo sabido', 'had I known (formal)', 'de + infinitive', '<b>De haberlo sabido</b>, habría venido antes.', 'De ______ sabido, habría venido antes. (having it)', 'haberlo'),
    ('yo-que-tu', 'yo que tú', 'if I were you', 'advice idiom', '<b>Yo que tú</b>, aceptaría la oferta.', 'Yo que ______, aceptaría la oferta. (you)', 'tú'),
  ],
),

'continuous-forms': dict(
  num='G5', short='Continuous Forms', title='Continuous Forms — Ir, andar, seguir + gerundio',
  subtitle='Beyond estar: the gerund periphrases that add colour and precision',
  slides=[
    ('Ir + gerundio — gradual progress', None,
     '<p class="slide-explanation"><b>Ir + gerundio</b> paints an action unfolding <b>little by little</b> — a nuance English needs adverbs for.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Voy entendiendo la gramática.</b> (I\'m gradually getting the grammar.)</p>'
     '<p style="margin-top:8px"><b>El cielo se va oscureciendo.</b> (The sky is slowly darkening.)</p>'
     '<p style="margin-top:8px"><b>Ve preparando la cena, ahora llego.</b> (Start getting dinner ready, I\'m on my way.)</p></div>'
     '<p style="margin-top:16px">Ir + gerundio = progressive build-up. The imperative ve preparando = "start ...ing (in the meantime)".</p>'),
    ('Andar + gerundio — going around doing', None,
     '<p class="slide-explanation"><b>Andar + gerundio</b> adds a flavour of "going around doing something" — often with a hint of disapproval.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Anda diciendo que fue idea suya.</b> (He\'s going around saying it was his idea.)</p>'
     '<p style="margin-top:8px"><b>¿Qué andas buscando?</b> (What are you after / poking around for?)</p></div>'
     '<p style="margin-top:16px">Colloquial and very Spanish — recognise it in speech, deploy it carefully.</p>'),
    ('Llevar + gerundio vs llevar sin', None,
     '<p class="slide-explanation">You know <b>llevar + time + gerundio</b> (have been doing). Its negative twin is <b>llevar + time + sin + infinitive</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Llevo tres años estudiando español.</b> (I\'ve been studying Spanish for three years.)</p>'
     '<p style="margin-top:8px"><b>Llevo dos meses sin fumar.</b> (I haven\'t smoked for two months.)</p></div>'
     '<p style="margin-top:16px">"I haven\'t done X for [time]" → llevo + tiempo + sin + infinitive. No perfect tense needed.</p>'),
    ('Seguir and quedarse', None,
     '<p class="slide-explanation">Continuation and lingering: <b>seguir + gerundio</b> (still doing) and <b>quedarse + gerundio</b> (stay doing).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Sigue lloviendo.</b> (It\'s still raining.)</p>'
     '<p style="margin-top:8px"><b>Me quedé estudiando hasta las dos.</b> (I stayed up studying until two.)</p></div>'
     '<p style="margin-top:16px">Negative of seguir: <b>ya no</b> + verb — Ya no llueve (it\'s not raining any more), or sigue sin llover (it still hasn\'t rained).</p>'),
    ('When NOT to use the gerund', None,
     '<p class="slide-explanation">English -ing spreads everywhere; the Spanish gerund doesn\'t. Three no-go zones:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Subject: <b>Fumar</b> es malo. (not "fumando")</p>'
     '<p style="margin-top:8px">After prepositions: antes de <b>salir</b> (not "saliendo")</p>'
     '<p style="margin-top:8px">As adjective: agua <b>corriente</b>, una historia <b>fascinante</b> (not gerunds!)</p></div>'
     '<p style="margin-top:16px">"The man reading the paper" → el hombre <b>que lee</b> el periódico. Spanish prefers a relative clause.</p>'),
  ],
  traps=[
    ('Estoy aprendiendo poco a poco... (fine, but flat)', '<strong>Voy aprendiendo</strong> poco a poco.', 'Gradual progress sounds native with ir + gerundio: voy aprendiendo'),
    ('No fumo desde hace dos meses. (fine) / He estado sin fumar...', '<strong>Llevo dos meses sin fumar.</strong>', 'The idiomatic "haven\'t done for X time" is llevar + tiempo + sin + infinitive'),
    ('El hombre leyendo el periódico es mi tío.', 'El hombre <strong>que lee</strong> el periódico es mi tío.', 'Spanish gerunds can\'t modify nouns — use a relative clause'),
    ('Todavía llueve... (fine) but "still raining" emphatic:', '<strong>Sigue lloviendo.</strong>', 'seguir + gerundio is the natural "still ...ing"'),
    ('Quedé estudiando hasta las dos.', '<strong>Me quedé</strong> estudiando hasta las dos.', 'quedarse (reflexive) = to stay; quedar alone means to arrange to meet'),
  ],
  summary=[
    ('Gradual', 'ir + gerundio', 'Voy entendiendo la gramática.'),
    ('Going around', 'andar + gerundio', 'Anda diciendo que fue idea suya.'),
    ('Have been doing', 'llevar + tiempo + gerundio', 'Llevo tres años estudiando.'),
    ('Haven\'t done for', 'llevar + tiempo + sin + inf.', 'Llevo dos meses sin fumar.'),
    ('Still / stay', 'seguir + ger. · quedarse + ger.', 'Sigue lloviendo. · Me quedé estudiando.'),
    ('No gerund', 'subject, after prepositions, as adjective', 'Fumar es malo. · antes de salir'),
  ],
  ex1=('Pick the periphrasis', 'Which nuance does the sentence need?', [
    ('Poco a poco ______ mejorando mi pronunciación.', ['voy', 'ando', 'quedo'], 'voy',
     'Gradual progress → VOY mejorando.'),
    ('______ tres semanas sin ver a mis padres.', ['Llevo', 'Sigo', 'Voy'], 'Llevo',
     'Haven\'t for + time → LLEVO tres semanas SIN ver.'),
    ('¿Todavía trabajas allí? Sí, ______ trabajando en la misma oficina.', ['sigo', 'ando', 'voy'], 'sigo',
     'Still doing → SIGO trabajando.'),
    ('Mi vecino ______ contando a todos que le ha tocado la lotería.', ['anda', 'lleva', 'queda'], 'anda',
     'Going around saying → ANDA contando.'),
    ('Anoche me ______ leyendo hasta las tres.', ['quedé', 'fui', 'anduve'], 'quedé',
     'Stayed doing → ME QUEDÉ leyendo.'),
    ('______ es malo para la salud. (smoking, as subject)', ['Fumar', 'Fumando', 'El fumando'], 'Fumar',
     'Subject → infinitive: FUMAR es malo.'),
  ]),
  ex2=('Build the form', 'Type the missing piece.', [
    ('I\'ve been waiting for an hour. → ______ una hora esperando. (one word)', 'llevo',
     'LLEVO una hora esperando.'),
    ('I haven\'t seen her for months. → Llevo meses ______ verla. (one word)', 'sin',
     'llevar + SIN + infinitive.'),
    ('It\'s still snowing. → ______ nevando. (seguir, 3rd sing.)', 'sigue',
     'SIGUE nevando.'),
    ('I\'m gradually understanding. → ______ entendiendo. (ir, yo)', 'voy',
     'VOY entendiendo.'),
    ('Start setting the table (meanwhile). → Ve ______ la mesa. (poner, gerundio)', 'poniendo',
     'Ve PONIENDO la mesa — imperative ir + gerundio.'),
  ]),
  ex3=('Choose the native version', 'Gerund or not?', [
    ('"The woman talking to Juan is my boss":', ['La mujer que habla con Juan es mi jefa.', 'La mujer hablando con Juan es mi jefa.', 'La mujer hablante con Juan es mi jefa.'], 'La mujer que habla con Juan es mi jefa.',
     'No adjectival gerunds → relative clause: que habla.'),
    ('"After eating, we went for a walk":', ['Después de comer, dimos un paseo.', 'Después de comiendo, dimos un paseo.', 'Después comer, dimos un paseo.'], 'Después de comer, dimos un paseo.',
     'Preposition + infinitive: después de COMER.'),
    ('"He still hasn\'t called":', ['Sigue sin llamar.', 'Sigue no llamando.', 'Anda sin llamada.'], 'Sigue sin llamar.',
     'Still not done → seguir SIN + infinitive.'),
    ('"Prices keep going up":', ['Los precios van subiendo.', 'Los precios suben yendo.', 'Los precios están en subiendo.'], 'Los precios van subiendo.',
     'Gradual continuing rise → van subiendo.'),
    ('"We stayed chatting until late":', ['Nos quedamos charlando hasta tarde.', 'Quedamos charlando hasta tarde.', 'Nos fuimos charlando hasta tarde.'], 'Nos quedamos charlando hasta tarde.',
     'Stay doing → NOS QUEDAMOS charlando.'),
  ]),
  game_desc='Each gerund periphrasis passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('ir-gerundio', 'ir + gerundio', 'to be gradually doing', 'gradual', '<b>Voy entendiendo</b> la gramática.', '______ entendiendo la gramática. (I am gradually)', 'voy'),
    ('andar-gerundio', 'andar + gerundio', 'to go around doing', 'colloquial', '<b>Anda diciendo</b> que fue idea suya.', '______ diciendo que fue idea suya. (he goes around)', 'anda'),
    ('llevar-gerundio', 'llevar + tiempo + gerundio', 'to have been doing for', 'duration', '<b>Llevo</b> tres años estudiando español.', '______ tres años estudiando español. (I have been)', 'llevo'),
    ('llevar-sin', 'llevar + tiempo + sin + inf.', 'to not have done for', 'negative duration', 'Llevo dos meses <b>sin</b> fumar.', 'Llevo dos meses ______ fumar. (without)', 'sin'),
    ('seguir-gerundio', 'seguir + gerundio', 'to still be doing', 'continuation', '<b>Sigue lloviendo.</b>', '______ lloviendo. (it is still)', 'sigue'),
    ('quedarse-gerundio', 'quedarse + gerundio', 'to stay doing', 'lingering', '<b>Me quedé</b> estudiando hasta las dos.', 'Me ______ estudiando hasta las dos. (I stayed)', 'quedé'),
    ('seguir-sin', 'seguir sin + infinitivo', 'to still not have done', 'still not', '<b>Sigue sin</b> llamar.', 'Sigue ______ llamar. (without)', 'sin'),
    ('no-adj-gerund', 'que + verbo (no gerund!)', 'the man READING = que lee', 'relative clause', 'El hombre <b>que lee</b> el periódico.', 'El hombre ______ lee el periódico. (who)', 'que'),
  ],
),

}
