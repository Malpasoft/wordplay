# -*- coding: utf-8 -*-
"""espanol-en B2 grammar content — batch 4 (chapters G16-G18)."""

CHAPTERS = {

'subjunctive-advanced': dict(
  num='G16', short='Subjunctive II', title='Subjunctive II — El imperfecto de subjuntivo',
  subtitle='Past wishes, polite requests and indefinite antecedents',
  slides=[
    ('The imperfect subjunctive in its own right', None,
     '<p class="slide-explanation">You met <b>tuviera/fuera</b> inside conditionals. The imperfect subjunctive also follows any <b>past-tense trigger</b>: quería que, esperaba que, me pidió que.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Quería que vinieras a la fiesta.</b> (I wanted you to come to the party.)</p>'
     '<p style="margin-top:8px"><b>Esperaba que el examen fuera más fácil.</b> (I hoped the exam would be easier.)</p></div>'
     '<p style="margin-top:16px">The rule of pairs: present trigger → present subjunctive (quiero que vengas); past trigger → imperfect subjunctive (quería que vinieras).</p>'),
    ('Formation refresher — and the -se twin', None,
     '<p class="slide-explanation">From the ellos-indefinido minus -ron: hablara, comiera, viviera. Every form has a <b>-se twin</b> with identical meaning.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>dijeron → <b>dijera / dijese</b> · quisieron → <b>quisiera / quisiese</b></p>'
     '<p style="margin-top:8px">fueron → <b>fuera / fuese</b> · hubieron → <b>hubiera / hubiese</b></p></div>'
     '<p style="margin-top:16px">Literature loves -se; conversation prefers -ra. Use -ra, recognise both.</p>'),
    ('Indefinite antecedents: busco a alguien que sepa', None,
     '<p class="slide-explanation">When the person or thing you describe <b>may not exist</b>, the relative clause takes the subjunctive.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Busco un piso que tenga terraza.</b> (I\'m looking for a flat that has a terrace — any such flat, maybe none.)</p>'
     '<p style="margin-top:8px">Compare: <b>Vivo en un piso que tiene terraza.</b> (I live in one — it exists, indicative.)</p>'
     '<p style="margin-top:8px"><b>No hay nadie que lo entienda.</b> (There\'s nobody who understands it.)</p></div>'
     '<p style="margin-top:16px">Known and real → indicative. Hypothetical or denied → subjunctive. This contrast is a B2 exam favourite.</p>'),
    ('Quisiera — the politest verb in Spanish', None,
     '<p class="slide-explanation">The imperfect subjunctive of querer doubles as ultra-polite "I would like": <b>quisiera</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Quisiera hacer una reclamación.</b> (I would like to make a complaint.)</p>'
     '<p style="margin-top:8px"><b>Quisiéramos una mesa junto a la ventana.</b> (We would like a table by the window.)</p></div>'
     '<p style="margin-top:16px">Quisiera outranks querría in formality — perfect for complaints, hotels and officialdom.</p>'),
    ('Ojalá with the past: impossible wishes', None,
     '<p class="slide-explanation">Ojalá\'s meaning shifts with the tense that follows it.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Ojalá venga.</b> (I hope he comes — possible.)</p>'
     '<p style="margin-top:8px"><b>Ojalá viniera.</b> (I wish he would come — unlikely.)</p>'
     '<p style="margin-top:8px"><b>Ojalá hubiera venido.</b> (I wish he had come — impossible now, pure regret.)</p></div>'
     '<p style="margin-top:16px">Three tenses, three degrees of hope: venga (hope) → viniera (wish) → hubiera venido (regret).</p>'),
  ],
  traps=[
    ('Quería que vienes a la fiesta.', 'Quería que <strong>vinieras</strong> a la fiesta.', 'Past trigger → imperfect subjunctive: quería que vinieras'),
    ('Busco un piso que tiene terraza. (still searching)', 'Busco un piso que <strong>tenga</strong> terraza.', 'Indefinite antecedent — the flat may not exist → subjunctive: tenga'),
    ('No hay nadie que lo entiende.', 'No hay nadie que lo <strong>entienda</strong>.', 'Denied existence (no hay nadie) → subjunctive: entienda'),
    ('Quiero hacer una reclamación. (too blunt at a desk)', '<strong>Quisiera</strong> hacer una reclamación.', 'Formal politeness uses quisiera — the imperfect subjunctive of querer'),
    ('Ojalá que viniera ayer y vino.', 'Ojalá <strong>hubiera venido</strong>.', 'Regret about the past → ojalá + pluperfect subjunctive: hubiera venido'),
  ],
  summary=[
    ('Pairing rule', 'past trigger → imperfecto de subjuntivo', 'Quería que vinieras.'),
    ('Formation', 'ellos-indefinido − ron + -ra/-se', 'dijera/dijese · fuera/fuese'),
    ('Indefinite', 'busco ... que + subjuntivo', 'Busco un piso que tenga terraza.'),
    ('Denied', 'no hay nadie que + subjuntivo', 'No hay nadie que lo entienda.'),
    ('Politeness', 'quisiera + infinitivo', 'Quisiera hacer una reclamación.'),
    ('Ojalá scale', 'venga → viniera → hubiera venido', 'hope → wish → regret'),
  ],
  ex1=('Present or imperfect subjunctive?', 'Match the trigger\'s tense.', [
    ('Quiero que me ______ la verdad. (decir, tú)', ['digas', 'dijeras', 'dices'], 'digas',
     'Present trigger → present subjunctive: DIGAS.'),
    ('Quería que me ______ la verdad. (decir, tú)', ['dijeras', 'digas', 'decías'], 'dijeras',
     'Past trigger → imperfect subjunctive: DIJERAS.'),
    ('Busco un trabajo que me ______ viajar. (permitir)', ['permita', 'permite', 'permitiera'], 'permita',
     'Indefinite antecedent, present search → PERMITA.'),
    ('Tengo un trabajo que me ______ viajar. (permitir — it exists!)', ['permite', 'permita', 'permitiera'], 'permite',
     'Real, existing job → indicative: PERMITE.'),
    ('No había nadie que ______ ruso. (hablar)', ['hablara', 'hablaba', 'hable'], 'hablara',
     'Denied existence in the past → HABLARA.'),
    ('Me pidió que le ______ con la mudanza. (ayudar)', ['ayudara', 'ayude', 'ayudaba'], 'ayudara',
     'Past request → imperfect subjunctive: AYUDARA.'),
  ]),
  ex2=('Form the imperfect subjunctive', 'From the ellos-indefinido.', [
    ('venir → Esperaba que ______ a la cena. (tú)', 'vinieras',
     'vinieron → VINIERAS.'),
    ('ser → Ojalá el examen ______ más fácil. (it were)', 'fuera',
     'fueron → FUERA (fuese also correct; type fuera).'),
    ('querer, polite → ______ una habitación doble, por favor. (yo)', 'quisiera',
     'QUISIERA — the politeness form.'),
    ('tener → Buscaba un hotel que ______ piscina.', 'tuviera',
     'tuvieron → TUVIERA.'),
    ('haber, regret → Ojalá ______ estudiado más. (yo)', 'hubiera',
     'Ojalá HUBIERA estudiado — regret about the past.'),
  ]),
  ex3=('Real or hypothetical?', 'Indicative or subjunctive in the relative clause?', [
    ('"I need a colleague who speaks German" (haven\'t found one):', ['Necesito un compañero que hable alemán.', 'Necesito un compañero que habla alemán.', 'Necesito un compañero que hablara alemán.'], 'Necesito un compañero que hable alemán.',
     'May not exist → subjunctive HABLE.'),
    ('"I have a colleague who speaks German":', ['Tengo un compañero que habla alemán.', 'Tengo un compañero que hable alemán.', 'Tengo un compañero que hablase alemán.'], 'Tengo un compañero que habla alemán.',
     'Exists → indicative HABLA.'),
    ('"There is nothing that scares him":', ['No hay nada que le asuste.', 'No hay nada que le asusta.', 'No hay nada que le asustara hoy.'], 'No hay nada que le asuste.',
     'Denied existence → subjunctive ASUSTE.'),
    ('"I wish I were taller" (impossible wish):', ['Ojalá fuera más alto.', 'Ojalá soy más alto.', 'Ojalá seré más alto.'], 'Ojalá fuera más alto.',
     'Unlikely/impossible wish → imperfect subjunctive FUERA.'),
    ('"She asked me to call her":', ['Me pidió que la llamara.', 'Me pidió que la llamo.', 'Me pidió llamarla que.'], 'Me pidió que la llamara.',
     'Past request → que + LLAMARA.'),
  ]),
  game_desc='Each subjunctive pattern passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('queria-que', 'quería que + imperf. subj.', 'I wanted (someone) to...', 'past trigger', '<b>Quería que vinieras</b> a la fiesta.', 'Quería que ______ a la fiesta. (you came)', 'vinieras'),
    ('dijera', 'dijera / dijese', 'imperfect subjunctive of decir', 'formation', 'Me pidió que le <b>dijera</b> la verdad.', 'Me pidió que le ______ la verdad. (I told)', 'dijera'),
    ('que-tenga', 'busco ... que tenga', 'looking for one that has (may not exist)', 'indefinite', 'Busco un piso <b>que tenga</b> terraza.', 'Busco un piso que ______ terraza. (has — subjunctive)', 'tenga'),
    ('nadie-que', 'no hay nadie que + subj.', 'there\'s nobody who...', 'denied existence', 'No hay nadie <b>que lo entienda</b>.', 'No hay nadie que lo ______. (understands)', 'entienda'),
    ('quisiera', 'quisiera', 'I would like (ultra-polite)', 'politeness', '<b>Quisiera</b> hacer una reclamación.', '______ hacer una reclamación. (I would like)', 'quisiera'),
    ('ojala-viniera', 'ojalá + imperf. subj.', 'I wish... (unlikely)', 'wishes', '<b>Ojalá viniera</b> más a menudo.', 'Ojalá ______ más a menudo. (he would come)', 'viniera'),
    ('ojala-hubiera', 'ojalá hubiera + part.', 'I wish ... had (regret)', 'regret', '<b>Ojalá hubiera</b> estudiado más.', 'Ojalá ______ estudiado más. (I had)', 'hubiera'),
    ('esperaba-que', 'esperaba que + imperf. subj.', 'I hoped that...', 'past hope', '<b>Esperaba que</b> el examen <b>fuera</b> fácil.', 'Esperaba que el examen ______ fácil. (would be)', 'fuera'),
  ],
),

'tense-consistency': dict(
  num='G17', short='Tense Consistency', title='Tense Consistency — La concordancia de tiempos',
  subtitle='Keeping every clause in the right time zone',
  slides=[
    ('The pairing table', None,
     '<p class="slide-explanation">Spanish clauses agree across the <b>que</b> boundary. Main-verb tense decides the subordinate tense — learn the pairs as a table.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Quiero que <b>vengas</b>. → Quería que <b>vinieras</b>.</p>'
     '<p style="margin-top:8px">Creo que <b>viene</b>. → Creía que <b>venía</b>.</p>'
     '<p style="margin-top:8px">Dice que <b>vendrá</b>. → Dijo que <b>vendría</b>.</p></div>'
     '<p style="margin-top:16px">Shift the main verb to the past and every dependent verb steps back with it: presente→imperfecto, futuro→condicional, subjuntivo presente→subjuntivo imperfecto.</p>'),
    ('Narration: the imperfecto-indefinido dance', None,
     '<p class="slide-explanation">Stories alternate two pasts with strict roles: <b>imperfecto</b> sets scenes, <b>indefinido</b> moves the plot.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Llovía</b> (scene), las calles <b>estaban</b> vacías (scene), cuando de repente <b>sonó</b> el teléfono (event) y todo <b>cambió</b> (event).</p></div>'
     '<p style="margin-top:16px">Switching roles mid-story is the classic B2 composition error. Scene → imperfecto. Action → indefinido. Earlier past → pluscuamperfecto.</p>'),
    ('Mientras and cuando in the past', None,
     '<p class="slide-explanation">Two patterns to automate.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Interrupted action: <b>Mientras cocinaba, llegó mi hermano.</b> (imperfecto + indefinido)</p>'
     '<p style="margin-top:8px">Parallel actions: <b>Mientras yo cocinaba, él ponía la mesa.</b> (imperfecto + imperfecto)</p>'
     '<p style="margin-top:8px">Sequence: <b>Cuando terminé, me fui.</b> (indefinido + indefinido)</p></div>'
     '<p style="margin-top:16px">Ask: was one action a backdrop (imperfecto) or did both simply happen one after the other (indefinido)?</p>'),
    ('Future and conditional pairs', None,
     '<p class="slide-explanation">Time clauses about the future keep their subjunctive even when the main verb is conditional.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Te llamaré cuando llegue.</b> (future + present subjunctive)</p>'
     '<p style="margin-top:8px"><b>Dijo que me llamaría cuando llegara.</b> (conditional + imperfect subjunctive)</p></div>'
     '<p style="margin-top:16px">The whole sentence moves back as a block: llamaré→llamaría, llegue→llegara. Consistency is the skill.</p>'),
    ('Proofreading your own writing', None,
     '<p class="slide-explanation">A B2 self-check routine for any composition:</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>1. Circle every main verb — is the anchor tense consistent?</p>'
     '<p style="margin-top:8px">2. Check every que-clause against the pairing table.</p>'
     '<p style="margin-top:8px">3. In narration, justify each imperfecto (scene?) and each indefinido (event?).</p></div>'
     '<p style="margin-top:16px">Examiners penalise tense drift more than any single wrong form — consistency earns the band.</p>'),
  ],
  traps=[
    ('Quería que vengas conmigo.', 'Quería que <strong>vinieras</strong> conmigo.', 'Past main verb → imperfect subjunctive in the que-clause'),
    ('Creía que viene mañana.', 'Creía que <strong>venía / vendría</strong> mañana.', 'creía (past) cannot govern a present — step it back: venía or vendría'),
    ('Ayer llovía, sonaba el teléfono y cambiaba todo. (all imperfecto)', 'Ayer llovía, <strong>sonó</strong> el teléfono y todo <strong>cambió</strong>.', 'Plot events take the indefinido; only the backdrop stays imperfecto'),
    ('Dijo que me llamaría cuando llegue.', 'Dijo que me llamaría cuando <strong>llegara</strong>.', 'Conditional main verb → imperfect subjunctive in the time clause: llegara'),
    ('Mientras cocinaba, mi hermano llegaba. (one event!)', 'Mientras cocinaba, mi hermano <strong>llegó</strong>.', 'An interrupting event takes the indefinido: llegó'),
  ],
  summary=[
    ('Pairs', 'presente→imperfecto · futuro→condicional', 'Dice que vendrá. → Dijo que vendría.'),
    ('Subjunctive pair', 'venga → viniera', 'Quiero que vengas. → Quería que vinieras.'),
    ('Scene', 'imperfecto', 'Llovía y las calles estaban vacías.'),
    ('Event', 'indefinido', 'De repente sonó el teléfono.'),
    ('Interruption', 'mientras + imperfecto, indefinido', 'Mientras cocinaba, llegó mi hermano.'),
    ('Future block', 'llamaré cuando llegue → llamaría cuando llegara', 'shift the whole sentence together'),
  ],
  ex1=('Keep the tenses consistent', 'Step everything back together.', [
    ('Dijo que ______ al día siguiente. (venir)', ['vendría', 'vendrá', 'venga'], 'vendría',
     'dijo → future becomes conditional: VENDRÍA.'),
    ('Quería que le ______ con el informe. (ayudar, yo)', ['ayudara', 'ayude', 'ayudaba'], 'ayudara',
     'Past trigger → imperfect subjunctive: AYUDARA.'),
    ('Mientras ______ por el parque, empezó a llover. (pasear, nosotros)', ['paseábamos', 'paseamos', 'paseáramos'], 'paseábamos',
     'Backdrop → imperfecto: PASEÁBAMOS; the rain is the event.'),
    ('Cuando ______ el ruido, todos se levantaron. (oír, ellos)', ['oyeron', 'oían', 'oigan'], 'oyeron',
     'Sequence of events → indefinido: OYERON.'),
    ('Creía que la tienda ______ abierta. (estar)', ['estaba', 'está', 'estuviera'], 'estaba',
     'creía → present steps back to imperfecto: ESTABA.'),
    ('Prometió que me escribiría cuando ______ a Lima. (llegar)', ['llegara', 'llegue', 'llegaría'], 'llegara',
     'Conditional block → imperfect subjunctive: LLEGARA.'),
  ]),
  ex2=('Step it back', 'Rewrite in the past — type the shifted verb.', [
    ('Dice que viene. → Dijo que ______.', 'venía',
     'Present → imperfecto: VENÍA.'),
    ('Quiero que vengas. → Quería que ______.', 'vinieras',
     'Present subjunctive → imperfect subjunctive: VINIERAS.'),
    ('Te llamo cuando llegue. → Dijo que me llamaría cuando ______.', 'llegara',
     'Present subjunctive → imperfect subjunctive: LLEGARA.'),
    ('Cree que lloverá. → Creía que ______.', 'llovería',
     'Future → conditional: LLOVERÍA.'),
    ('Espero que haya llegado. → Esperaba que ______ llegado. (one word)', 'hubiera',
     'Perfect subjunctive → pluperfect subjunctive: HUBIERA llegado.'),
  ]),
  ex3=('Fix the narration', 'Scene or event?', [
    ('Choose the correct story opening:', ['Era de noche y llovía. De repente, alguien llamó a la puerta.', 'Fue de noche y llovió. De repente, alguien llamaba a la puerta.', 'Era de noche y llovió siempre. Alguien llamaba de repente.'], 'Era de noche y llovía. De repente, alguien llamó a la puerta.',
     'Scene = imperfecto (era, llovía); event = indefinido (llamó).'),
    ('"While I was studying, the lights went out":', ['Mientras estudiaba, se fue la luz.', 'Mientras estudié, se iba la luz.', 'Mientras estudiara, se fue la luz.'], 'Mientras estudiaba, se fue la luz.',
     'Backdrop imperfecto + event indefinido.'),
    ('"She said she would write to me":', ['Dijo que me escribiría.', 'Dijo que me escribirá.', 'Dijo que me escriba.'], 'Dijo que me escribiría.',
     'dijo + conditional: escribiría.'),
    ('"I didn\'t know you were coming":', ['No sabía que venías.', 'No sabía que vienes.', 'No supe que vengas.'], 'No sabía que venías.',
     'Past knowledge → imperfecto pair: sabía + venías.'),
    ('"He promised he would call when he arrived":', ['Prometió que llamaría cuando llegara.', 'Prometió que llamará cuando llegue.', 'Prometió que llamaría cuando llegue.'], 'Prometió que llamaría cuando llegara.',
     'Whole block in the past: llamaría + llegara.'),
  ]),
  game_desc='Each tense pair passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('dijo-vendria', 'dijo que vendría', 'said he would come (futuro→condicional)', 'backshift', 'Dijo que <b>vendría</b> al día siguiente.', 'Dijo que ______ al día siguiente. (he would come)', 'vendría'),
    ('queria-vinieras', 'quería que vinieras', 'wanted you to come (subjunctive pair)', 'subjunctive shift', 'Quería que <b>vinieras</b>.', 'Quería que ______. (you came)', 'vinieras'),
    ('llovia', 'llovía (scene)', 'it was raining — backdrop imperfecto', 'scene-setting', '<b>Llovía</b> y las calles estaban vacías.', '______ y las calles estaban vacías. (it was raining)', 'llovía'),
    ('sono', 'sonó (event)', 'it rang — plot indefinido', 'events', 'De repente <b>sonó</b> el teléfono.', 'De repente ______ el teléfono. (it rang)', 'sonó'),
    ('mientras-imperfecto', 'mientras + imperfecto', 'while I was ...ing (backdrop)', 'interruption', '<b>Mientras cocinaba</b>, llegó mi hermano.', 'Mientras ______, llegó mi hermano. (I was cooking)', 'cocinaba'),
    ('creia-que', 'creía que + imperfecto', 'I thought (that)...', 'belief shift', '<b>Creía que</b> la tienda <b>estaba</b> abierta.', 'Creía que la tienda ______ abierta. (was)', 'estaba'),
    ('cuando-llegara', 'llamaría cuando llegara', 'would call when he arrived', 'block shift', 'Dijo que llamaría cuando <b>llegara</b>.', 'Dijo que llamaría cuando ______. (he arrived)', 'llegara'),
    ('no-sabia', 'no sabía que + imperfecto', 'I didn\'t know (that)...', 'past knowledge', '<b>No sabía que venías.</b>', 'No sabía que ______. (you were coming)', 'venías'),
  ],
),

'voice-and-register': dict(
  num='G18', short='Register', title='Register — Tú, usted and the formal voice',
  subtitle='Choosing the right Spanish for the room: colloquial, neutral, formal',
  slides=[
    ('The address system', None,
     '<p class="slide-explanation">Spanish encodes formality in its pronouns. Spain uses four: <b>tú/vosotros</b> (informal), <b>usted/ustedes</b> (formal). Latin America drops vosotros entirely — ustedes serves everyone.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Tienes hora?</b> (informal, to a friend)</p>'
     '<p style="margin-top:8px"><b>¿Tiene usted hora?</b> (formal, to a stranger/elder)</p></div>'
     '<p style="margin-top:16px">usted takes <b>third-person</b> verb forms — grammatically you talk ABOUT the person you\'re talking TO. Spain today defaults to tú faster than you\'d expect; usted survives in officialdom, with the elderly, and in service contexts.</p>'),
    ('Formal written Spanish: the se voice', None,
     '<p class="slide-explanation">Formal documents avoid "you" altogether with the impersonal <b>se</b> — instructions, notices and signs live in this voice.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Se ruega silencio.</b> (Silence is requested.)</p>'
     '<p style="margin-top:8px"><b>No se admiten devoluciones.</b> (No returns accepted.)</p>'
     '<p style="margin-top:8px"><b>Se recomienda reservar.</b> (Booking is recommended.)</p></div>'
     '<p style="margin-top:16px">se ruega, se recomienda, se prohíbe, no se admite — the four pillars of Spanish signage.</p>'),
    ('Colloquial markers', None,
     '<p class="slide-explanation">Spoken Spanish runs on small words that never appear in formal writing — recognise them, use them with friends only.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>vale</b> (OK) · <b>venga</b> (come on / OK then) · <b>bueno</b> (well...) · <b>pues</b> (well/so)</p>'
     '<p style="margin-top:8px"><b>¿sabes?</b> (you know?) · <b>o sea</b> (I mean) · <b>en plan</b> (like — youth slang)</p></div>'
     '<p style="margin-top:16px">A B2 speaker who drops a natural "pues nada, venga, hasta luego" sounds years ahead of the textbook.</p>'),
    ('Formal vocabulary upgrades', None,
     '<p class="slide-explanation">Formal register swaps everyday verbs for their Latinate cousins — essential for formal letters and reports.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>empezar → <b>comenzar/iniciar</b> · acabar → <b>finalizar</b> · pedir → <b>solicitar</b></p>'
     '<p style="margin-top:8px">dar → <b>proporcionar/facilitar</b> · decir → <b>comunicar/informar de</b> · arreglar → <b>subsanar</b></p>'
     '<p style="margin-top:8px"><b>Le ruego que me facilite la información solicitada.</b> (Please provide the requested information.)</p></div>'
     '<p style="margin-top:16px">Same trick as English (ask→request, start→commence) — Spanish formality is largely vocabulary choice.</p>'),
    ('Softening and hedging', None,
     '<p class="slide-explanation">Politeness also lives in verb tenses: the imperfect and conditional soften any request or opinion.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Quería pedirte un favor.</b> (I wanted to ask you a favour — imperfect softener.)</p>'
     '<p style="margin-top:8px"><b>¿No sería mejor esperar?</b> (Wouldn\'t it be better to wait?)</p>'
     '<p style="margin-top:8px"><b>Yo diría que es un error.</b> (I\'d say it\'s a mistake.)</p></div>'
     '<p style="margin-top:16px">quería, querría, quisiera — three rungs of the same politeness ladder. Climb according to the formality of the room.</p>'),
  ],
  traps=[
    ('¿Tienes usted hora?', '¿<strong>Tiene</strong> usted hora?', 'usted takes third-person verbs: tiene, not tienes'),
    ('Se ruegan silencio.', '<strong>Se ruega</strong> silencio.', 'Impersonal se agrees with the subject (silencio, singular): se ruega'),
    ('Estimado señor: te escribo para...', 'Estimado señor: <strong>le</strong> escribo para...', 'Formal letters stay in usted — le escribo, never te'),
    ('Quiero pedirte un favor. (a bit blunt)', '<strong>Quería</strong> pedirte un favor.', 'The imperfect quería softens requests — the polite past'),
    ('Vale, venga, hasta luego. (in a formal letter!)', '<strong>Atentamente,</strong>', 'Colloquial markers (vale, venga) never enter formal writing'),
  ],
  summary=[
    ('Informal', 'tú / vosotros + second person', '¿Tienes hora? · ¿Venís a cenar?'),
    ('Formal', 'usted / ustedes + third person', '¿Tiene usted hora?'),
    ('Signs', 'se ruega / se prohíbe / no se admite', 'Se ruega silencio.'),
    ('Colloquial', 'vale · venga · pues · o sea', 'Pues nada, venga, hasta luego.'),
    ('Formal verbs', 'solicitar · facilitar · comunicar', 'Le ruego que me facilite...'),
    ('Softeners', 'quería · sería · diría', 'Quería pedirte un favor.'),
  ],
  ex1=('Choose the register', 'Who are you talking to?', [
    ('To an elderly stranger: ¿______ decirme dónde está el banco?', ['Podría', 'Puedes', 'Podéis'], 'Podría',
     'Formal + softened → PODRÍA usted.'),
    ('On a sign: ______ fumar en todo el edificio.', ['Se prohíbe', 'Te prohíbo', 'Prohibimos a ti'], 'Se prohíbe',
     'Notices use impersonal se: SE PROHÍBE.'),
    ('To your friends (Spain): ¿______ al cine esta tarde?', ['Venís', 'Vienen ustedes', 'Viene'], 'Venís',
     'Group of friends in Spain → vosotros: VENÍS.'),
    ('Formal letter: Le escribo para ______ información sobre el curso.', ['solicitar', 'pedir un poco de', 'preguntar por ahí'], 'solicitar',
     'Formal verb → SOLICITAR (= request).'),
    ('Chatting: ______, nada, nos vemos mañana entonces.', ['Pues', 'Atentamente', 'Estimado'], 'Pues',
     'Colloquial filler → PUES nada.'),
    ('Hotel desk, very polite: ______ una habitación con vistas.', ['Quisiera', 'Quiero', 'Dame'], 'Quisiera',
     'Top politeness → QUISIERA.'),
  ]),
  ex2=('Upgrade the register', 'Type the formal equivalent.', [
    ('pedir → Le escribo para ______ una beca. (formal verb)', 'solicitar',
     'pedir → SOLICITAR in formal writing.'),
    ('empezar → El acto ______ a las ocho. (formal, future: comenzará/empezará — type the comenzar form)', 'comenzará',
     'empezar → COMENZAR: comenzará.'),
    ('Sign: "Booking recommended" → ______ recomienda reservar. (one word)', 'se',
     'Impersonal SE recomienda.'),
    ('Formal "you have": ¿______ usted alguna pregunta? (tener)', 'tiene',
     'usted → third person: TIENE.'),
    ('Soft request: ______ pedirte un favor. (querer, imperfecto, yo)', 'quería',
     'Imperfect softener: QUERÍA pedirte un favor.'),
  ]),
  ex3=('Match the voice to the room', 'Choose the appropriate version.', [
    ('Ending a formal email:', ['Atentamente, Laura Gómez', 'Venga, chao, Laura', 'Un beso enorme, Lau'], 'Atentamente, Laura Gómez',
     'Formal close → Atentamente.'),
    ('Asking your friend for the time:', ['¿Qué hora es, tío?', '¿Tendría usted la amabilidad de decirme la hora?', 'Se ruega comunicar la hora.'], '¿Qué hora es, tío?',
     'Friends → informal (tío is colloquial Spain).'),
    ('A notice in a museum:', ['No se permite hacer fotos.', 'No hagas fotos, ¿vale?', 'Os prohibimos las fotos, chicos.'], 'No se permite hacer fotos.',
     'Notices → impersonal se.'),
    ('Complaining politely at a hotel:', ['Quisiera hacer una reclamación: la habitación no está limpia.', '¡Oye, la habitación está hecha un asco!', 'Se ruega limpiar mi habitación ya.'], 'Quisiera hacer una reclamación: la habitación no está limpia.',
     'Formal complaint → quisiera + neutral description.'),
    ('Talking to your friend\'s grandmother (Spain, polite):', ['¿Quiere usted un poco más de café?', '¿Quieres más café, abuela tú?', '¿Queréis usted más café?'], '¿Quiere usted un poco más de café?',
     'Elder → usted + third person: quiere usted.'),
  ]),
  game_desc='Each register tool passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('usted-tiene', 'usted + 3rd person', 'formal you takes he/she verb forms', 'formal address', '¿<b>Tiene</b> usted hora?', '¿______ usted hora? (do you have — formal)', 'tiene'),
    ('vosotros', 'vosotros', 'informal plural you (Spain)', 'Spain plural', '¿<b>Venís</b> al cine esta tarde?', '¿______ al cine esta tarde? (are you all coming)', 'venís'),
    ('se-ruega', 'se ruega', 'is requested (signs)', 'impersonal se', '<b>Se ruega</b> silencio.', 'Se ______ silencio. (is requested)', 'ruega'),
    ('se-prohibe', 'se prohíbe', 'is forbidden (signs)', 'prohibition', '<b>Se prohíbe</b> fumar.', 'Se ______ fumar. (is forbidden)', 'prohíbe'),
    ('solicitar', 'solicitar', 'to request (formal for pedir)', 'formal verb', 'Le escribo para <b>solicitar</b> información.', 'Le escribo para ______ información. (request)', 'solicitar'),
    ('queria-softener', 'quería + infinitivo', 'I wanted to... (polite softener)', 'softening', '<b>Quería</b> pedirte un favor.', '______ pedirte un favor. (I wanted — softener)', 'quería'),
    ('vale', 'vale', 'OK (colloquial Spain)', 'colloquial', '—¿Quedamos a las ocho? —<b>Vale.</b>', '—¿Quedamos a las ocho? —______. (OK)', 'vale'),
    ('atentamente', 'Atentamente', 'Yours sincerely (formal close)', 'formal letters', '<b>Atentamente</b>, Laura Gómez.', '______, Laura Gómez. (formal close)', 'atentamente'),
  ],
),

}
