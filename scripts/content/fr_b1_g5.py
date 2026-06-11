# -*- coding: utf-8 -*-
"""fr/ B1 grammaire — lot 5 (5 chapitres, fin du B1)."""

CHAPTERS = {

'past-perfect': dict(
  level='b1', section='grammaire', num='Ch. 3', short='Past Perfect',
  title='Past Perfect — Le plus-que-parfait',
  subtitle='Had + participe : l’action d’avant l’action',
  slides=[
    ('Comme le plus-que-parfait français', None,
     '<p class="slide-explanation">Bonne nouvelle : <b>had + participe passé</b> fonctionne comme notre plus-que-parfait (« j’avais fini »). Il situe une action AVANT une autre action passée.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>When we arrived, the film had started.</b> (Quand nous sommes arrivés, le film avait commencé.)</p>'
     '<p style="margin-top:8px"><b>She had never flown before that day.</b></p></div>'),
    ('Formation', None,
     '<p class="slide-explanation">Had (toutes personnes) + participe passé. Contraction : <b>’d</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’d already eaten.</b> · <b>He hadn’t finished.</b> · <b>Had you met before?</b></p></div>'
     '<p style="margin-top:16px">⚠ ’d peut être had OU would : ’d + participe = had ; ’d + base verbale = would.</p>'),
    ('Le test des deux actions', None,
     '<p class="slide-explanation">Deux actions passées ? La plus ancienne prend had + participe, la plus récente le prétérit.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The train had left when I got to the station.</b> (1. le train part → 2. j’arrive)</p>'
     '<p style="margin-top:8px">Comparez : <b>The train left when I got there.</b> (il est parti à ce moment-là)</p></div>'),
    ('Avec after, before, by the time', None,
     '<p class="slide-explanation">Mots déclencheurs typiques : <b>after, before, by the time, already, just, never... before</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>After she had left, I found her keys.</b></p>'
     '<p style="margin-top:8px"><b>By the time we got there, everything had been eaten.</b></p></div>'),
    ('Au discours indirect et dans les regrets', None,
     '<p class="slide-explanation">Le past perfect est aussi la forme du recul (said + had done) et du regret (wish + had done) — vous l’avez déjà croisé.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>He said he had finished.</b> · <b>I wish I had known!</b></p></div>'),
  ],
  traps=[
    ('When we arrived, the film started. (il avait déjà commencé)', 'When we arrived, the film <strong>had started</strong>.', 'Sans had, on comprend que le film a commencé à notre arrivée.'),
    ('She had went home.', 'She had <strong>gone</strong> home.', 'Had + participe passé (3e colonne) : gone, pas went.'),
    ('I’d like ≠ I’d finished : même ’d ?', '’d + base = <strong>would</strong> ; ’d + participe = <strong>had</strong>', 'I’d like (would) / I’d finished (had) — c’est le mot suivant qui tranche.'),
    ('After she left, I had found her keys. (ordre inversé)', 'After she <strong>had left</strong>, I <strong>found</strong> her keys.', 'C’est l’action la plus ancienne (partir) qui prend had.'),
    ('I never had seen snow before.', 'I had <strong>never seen</strong> snow before.', 'L’adverbe se place entre had et le participe : had never seen.'),
  ],
  summary=[
    ('Formation', 'had + participe passé', 'She had gone.'),
    ('Emploi', 'action avant une action passée', 'The train had left when I arrived.'),
    ('Déclencheurs', 'after, before, by the time, already', 'After she had left...'),
    ('Contraction', '’d + participe', "I'd already eaten."),
    ('Aussi', 'discours indirect, wish', 'He said he had finished.'),
  ],
  ex1=('Choisis la forme correcte', 'Quelle action est la plus ancienne ?', [
    ('When I got home, my family ______ dinner.', ['had finished', 'finished', 'finishes'], 'had finished',
     'Le dîner était déjà fini avant mon arrivée → had finished.'),
    ('She ______ never ______ sushi before she went to Japan.', ['had / eaten', 'has / eaten', 'did / eat'], 'had / eaten',
     'Jamais... avant un moment passé → past perfect : had never eaten.'),
    ('After he ______ his homework, he watched TV.', ['had done', 'did had', 'has done'], 'had done',
     'After + action la plus ancienne → had done.'),
    ('The meeting ______ by the time we arrived.', ['had ended', 'ended', 'has ended'], 'had ended',
     'By the time = quand nous sommes arrivés, c’était déjà fini → had ended.'),
    ('I didn’t laugh because I ______ the joke before.', ['had heard', 'heard', 'have heard'], 'had heard',
     'J’avais déjà entendu la blague (avant de ne pas rire) → had heard.'),
    ('They ______ the house before the price went up.', ['had bought', 'have bought', 'buy'], 'had bought',
     'Achat antérieur à la hausse → had bought.'),
  ]),
  ex2=('Complète au past perfect', 'Écris la forme correcte du verbe.', [
    ('The film ______ already ______ when we sat down. (start)', 'had started',
     'Had + started, avec already entre les deux à l’écrit courant : had already started.'),
    ('She told me she ______ my email. (not / receive → forme négative complète « had not received » ou contractée)', "hadn't received",
     'Discours indirect + antériorité → hadn’t received.'),
    ('By the time the police arrived, the thief ______ . (escape → échapper : escaped)', 'had escaped',
     'Le voleur s’était échappé avant → had escaped.'),
    ('I was tired because I ______ badly. (sleep)', 'had slept',
     'La mauvaise nuit précède la fatigue → had slept (participe : slept).'),
    ('______ you ever ______ abroad before that trip? (live)', 'had lived',
     'Question d’antériorité : Had you ever lived abroad before...?'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Le train était déjà parti quand je suis arrivé. »', ['The train had already left when I arrived.', 'The train already left when I had arrived.', 'The train has already left when I arrived.'], 'The train had already left when I arrived.',
     'Action la plus ancienne (partir) → had left ; arrivée → prétérit.'),
    ('« Elle avait déjà mangé. »', ["She'd already eaten.", "She's already eaten.", 'She already ate had.'], "She'd already eaten.",
     '’d + participe = had : she’d (= she had) already eaten.'),
    ('« Je n’avais jamais vu la mer avant mes vingt ans. »', ['I had never seen the sea before I was twenty.', 'I never saw the sea before I had been twenty.', 'I have never seen the sea before twenty.'], 'I had never seen the sea before I was twenty.',
     'Jamais avant un repère passé → had never seen.'),
    ('« Après qu’il était parti, j’ai trouvé ses clés. »', ['After he had left, I found his keys.', 'After he left, I had found his keys.', 'After he has left, I found his keys.'], 'After he had left, I found his keys.',
     'After + had left (action ancienne) ; found (action suivante).'),
    ('Dans « I’d finished », ’d signifie :', ['had', 'would', 'did'], 'had',
     '’d suivi d’un participe passé (finished) = had.'),
  ]),
  game_desc='Chaque emploi du past perfect passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('had-started', 'had started', 'avait commencé — l’action d’avant', 'antériorité', 'The film <b>had started</b> when we arrived.', 'The film ______ started when we arrived.', 'had'),
    ('had-gone', 'had gone', 'était parti — participe irrégulier gone', 'participe irrégulier', 'She <b>had gone</b> home.', 'She had ______ home. (partie)', 'gone'),
    ('had-never', 'had never + participe', 'n’avait jamais — l’expérience avant un repère passé', 'jamais avant', 'I <b>had never seen</b> snow before.', 'I had ______ seen snow before. (jamais)', 'never'),
    ('after-had', 'after + had done', 'après que + plus-que-parfait', 'avec after', '<b>After she had left</b>, I found her keys.', 'After she ______ left, I found her keys.', 'had'),
    ('by-the-time', 'by the time', 'le temps que... — tout était déjà fait', 'by the time', '<b>By the time</b> we got there, everything had been eaten.', '______ the time we got there, everything had been eaten.', 'by'),
    ('d-had', "'d = had", '’d + participe = had (pas would)', 'contraction', "I<b>'d</b> already eaten. (= I had)", "I'______ already eaten. (= I had)", 'd'),
    ('hadnt', "hadn't + participe", 'n’avait pas — négation', 'négation', 'He <b>hadn’t finished</b>.', 'He ______ finished. (n’avait pas)', "hadn't"),
    ('said-had', 'said + had done', 'le past perfect du discours indirect', 'discours indirect', 'He said he <b>had finished</b>.', 'He said he ______ finished.', 'had'),
  ],
),

'present-perfect-continuous': dict(
  level='b1', section='grammaire', num='Ch. 4', short='Present Perfect Continuous',
  title='Present Perfect Continuous — Ça dure encore',
  subtitle='Have been + -ing : la durée qui se voit',
  slides=[
    ('« Ça fait deux heures que... »', None,
     '<p class="slide-explanation"><b>Have/has been + -ing</b> traduit nos tournures « ça fait X temps que... » et « depuis » avec insistance sur l’activité.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’ve been waiting for two hours!</b> (Ça fait deux heures que j’attends !)</p>'
     '<p style="margin-top:8px"><b>It has been raining all day.</b> (Il pleut depuis ce matin.)</p></div>'
     '<p style="margin-top:16px">Encore une fois : le français met le présent (« j’attends »), l’anglais non.</p>'),
    ('Le résultat visible', None,
     '<p class="slide-explanation">Aussi pour expliquer un état présent par une activité récente — même terminée.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You’re out of breath. Have you been running?</b> (Tu es essoufflé. Tu as couru ?)</p>'
     '<p style="margin-top:8px"><b>Her eyes are red — she’s been crying.</b></p></div>'),
    ('Simple ou continu ?', None,
     '<p class="slide-explanation">Continu → la durée/l’activité. Simple → le résultat/le bilan chiffré.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’ve been reading this book for a week.</b> (l’activité dure)</p>'
     '<p style="margin-top:8px"><b>I’ve read three books this month.</b> (bilan : 3 livres finis)</p></div>'
     '<p style="margin-top:16px">Un nombre de fois ou de choses accomplies → toujours le simple.</p>'),
    ('How long...?', None,
     '<p class="slide-explanation">La question de la durée en cours : <b>How long have you been + -ing ?</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>How long have you been learning English?</b> (Depuis combien de temps apprends-tu l’anglais ?)</p>'
     '<p style="margin-top:8px">→ <b>I’ve been learning English for three years.</b></p></div>'),
    ('Verbes d’état : toujours pas de -ing', None,
     '<p class="slide-explanation">Know, be, have (posséder), like... restent au present perfect simple, même avec for/since.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’ve known her for ten years.</b> (jamais « been knowing »)</p>'
     '<p style="margin-top:8px"><b>We’ve had this car since 2018.</b></p></div>'),
  ],
  traps=[
    ('I wait for two hours! (ça fait 2 h que j’attends)', 'I <strong>have been waiting</strong> for two hours!', '« Ça fait... que » + présent français → have been + -ing.'),
    ('I’ve been knowing her for years.', 'I’ve <strong>known</strong> her for years.', 'Know est un verbe d’état : perfect simple, même pour une durée.'),
    ('I’ve been reading three books this month.', 'I’ve <strong>read</strong> three books this month.', 'Bilan chiffré (3 livres) → perfect simple.'),
    ('How long do you learn English?', 'How long <strong>have you been learning</strong> English?', 'Durée en cours → present perfect continuous, pas le présent simple.'),
    ('It’s raining since this morning.', 'It <strong>has been raining</strong> since this morning.', '« Il pleut depuis... » → has been raining (le présent continu seul ne suffit pas).'),
  ],
  summary=[
    ('Formation', 'have/has been + -ing', "I've been waiting."),
    ('Ça fait... que', '+ for / since', "I've been waiting for two hours."),
    ('Résultat visible', 'activité récente', "Have you been running?"),
    ('Bilan chiffré', '→ perfect simple', "I've read three books."),
    ('Verbes d’état', '→ perfect simple', "I've known her for years."),
    ('Question', 'How long have you been...?', 'How long have you been learning?'),
  ],
  ex1=('Continu ou simple ?', 'Durée d’activité ou bilan ?', [
    ('She ______ for the exam all week.', ['has been revising', 'has revised', 'revises'], 'has been revising',
     'Activité qui dure toute la semaine → has been revising.'),
    ('I ______ five emails this morning.', ['have written', 'have been writing', 'write'], 'have written',
     'Bilan chiffré (5 e-mails) → perfect simple : have written.'),
    ('How long ______ you ______ here?', ['have / been living', 'do / live', 'are / living'], 'have / been living',
     'Durée en cours → How long have you been living here?'),
    ('You’re covered in paint! What ______ ?', ['have you been doing', 'have you done', 'did you do'], 'have you been doing',
     'Résultat visible d’une activité → have you been doing.'),
    ('We ______ each other since school.', ['have known', 'have been knowing', 'know'], 'have known',
     'Know = état → perfect simple : have known.'),
    ('It ______ all day — the garden is soaked.', ['has been raining', 'has rained twice', 'rains'], 'has been raining',
     'Pluie continue + résultat visible → has been raining.'),
  ]),
  ex2=('Complète la phrase', 'Écris la forme correcte.', [
    ('I’ve ______ waiting for you for an hour! (be)', 'been',
     'Have been + -ing : la brique centrale est been.'),
    ('He’s been ______ since six this morning. (work)', 'working',
     'Has been working : il travaille depuis six heures.'),
    ('They’ve been ______ English for two years. (learn)', 'learning',
     'Have been learning : apprentissage en cours.'),
    ('How long have you ______ learning the guitar? (be)', 'been',
     'How long have you been learning...?'),
    ('We’ve ______ this flat since 2020. (have → posséder, attention !)', 'had',
     'Have (posséder) est un verbe d’état → perfect simple : we’ve had.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Ça fait deux heures que j’attends ! »', ["I've been waiting for two hours!", 'I wait for two hours!', "I'm waiting since two hours!"], "I've been waiting for two hours!",
     '« Ça fait... que » → have been + -ing + for.'),
    ('« Il pleut depuis ce matin. »', ["It's been raining since this morning.", "It rains since this morning.", "It's raining since this morning."], "It's been raining since this morning.",
     'Depuis + durée en cours → has been raining.'),
    ('« Tu as couru ? Tu es tout essoufflé. »', ['Have you been running? You’re out of breath.', 'Did you run? You had run.', 'Are you running? You’re out of breath.'], 'Have you been running? You’re out of breath.',
     'Activité récente au résultat visible → have you been running.'),
    ('« J’ai lu trois livres ce mois-ci. »', ["I've read three books this month.", "I've been reading three books this month.", 'I read three books since this month.'], "I've read three books this month.",
     'Bilan chiffré → perfect simple.'),
    ('« Je la connais depuis dix ans. »', ["I've known her for ten years.", "I've been knowing her for ten years.", 'I know her since ten years.'], "I've known her for ten years.",
     'Verbe d’état + durée → have known + for.'),
  ]),
  game_desc='Chaque emploi passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('been-waiting', 'have been waiting', 'ça fait X temps que j’attends', 'durée en cours', "I<b>'ve been waiting</b> for two hours!", "I've been ______ for two hours! (attendre)", 'waiting'),
    ('been-raining', 'has been raining', 'il pleut depuis...', 'météo qui dure', 'It <b>has been raining</b> all day.', 'It has been ______ all day. (pleuvoir)', 'raining'),
    ('how-long', 'How long have you been...?', 'depuis combien de temps...', 'question de durée', '<b>How long</b> have you been learning English?', '______ ______ have you been learning English? (depuis combien de temps)', 'how long'),
    ('been-running', 'have you been running?', 'résultat visible d’une activité récente', 'résultat visible', 'You’re out of breath — <b>have you been running</b>?', "You're out of breath — have you been ______ ? (courir)", 'running'),
    ('have-read', "I've read three (bilan)", 'le bilan chiffré reste au perfect simple', 'bilan chiffré', "I<b>'ve read</b> three books this month.", "I've ______ three books this month. (ai lu)", 'read'),
    ('have-known', "I've known (état)", 'les verbes d’état refusent le -ing', 'verbe d’état', "I<b>'ve known</b> her for ten years.", "I've ______ her for ten years. (connais)", 'known'),
    ('for-duration', 'for + durée', 'for two hours = depuis deux heures', 'for', "I've been waiting <b>for</b> two hours.", "I've been waiting ______ two hours.", 'for'),
    ('since-point', 'since + repère', 'since six = depuis six heures', 'since', "He's been working <b>since</b> six.", "He's been working ______ six.", 'since'),
  ],
),

'too-enough': dict(
  level='b1', section='grammaire', num='Ch. 19', short='Too & Enough',
  title='Too & Enough — Trop et assez',
  subtitle='Too small, big enough : attention à l’ordre des mots',
  slides=[
    ('Too : trop', None,
     '<p class="slide-explanation"><b>Too + adjectif/adverbe</b> = trop. <b>Too much/too many + nom</b> = trop de.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>This coffee is too hot.</b> · <b>You drive too fast.</b></p>'
     '<p style="margin-top:8px"><b>too much noise</b> (indénombrable) · <b>too many cars</b> (dénombrable)</p></div>'
     '<p style="margin-top:16px">⚠ too ≠ very : very hot = très chaud ; too hot = trop chaud (problème !).</p>'),
    ('Enough : assez — mais où ?', None,
     '<p class="slide-explanation">LE piège : enough se place <b>après</b> l’adjectif mais <b>avant</b> le nom — l’inverse du français des deux côtés.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>big enough</b> (assez grand) — APRÈS l’adjectif</p>'
     '<p style="margin-top:8px"><b>enough money</b> (assez d’argent) — AVANT le nom</p></div>'),
    ('Too... to et enough... to', None,
     '<p class="slide-explanation">Pour dire « trop... pour » et « assez... pour » : + to + infinitif.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>It’s too cold to swim.</b> (Il fait trop froid pour se baigner.)</p>'
     '<p style="margin-top:8px"><b>She’s old enough to vote.</b> (Elle est assez âgée pour voter.)</p></div>'),
    ('Not enough', None,
     '<p class="slide-explanation">« Pas assez » : <b>not + adjectif + enough</b> ou <b>not enough + nom</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The room isn’t big enough.</b> (La chambre n’est pas assez grande.)</p>'
     '<p style="margin-top:8px"><b>There isn’t enough time.</b> (Il n’y a pas assez de temps.)</p></div>'),
    ('Too much en fin de phrase', None,
     '<p class="slide-explanation">Après un verbe, « trop » = too much.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You worry too much.</b> (Tu t’inquiètes trop.)</p>'
     '<p style="margin-top:8px"><b>He talks too much.</b></p></div>'),
  ],
  traps=[
    ('assez grand → enough big', '<strong>big enough</strong>', 'Enough se place APRÈS l’adjectif — l’inverse du français.'),
    ('assez d’argent → money enough', '<strong>enough money</strong>', 'Mais AVANT le nom ! big enough / enough money.'),
    ('It’s too much hot.', "It's <strong>too hot</strong>.", 'Devant un adjectif : too tout seul. Too much s’emploie avec un nom ou après un verbe.'),
    ('Il fait très chaud (very) ≠ too hot', 'very hot = très chaud · <strong>too hot = trop chaud</strong>', 'Too implique un problème ; very est neutre. Ne traduisez pas « très » par too.'),
    ('too cold for swim', 'too cold <strong>to swim</strong>', '« Trop... pour faire » → to + infinitif, pas for + verbe.'),
  ],
  summary=[
    ('Trop + adj', 'too + adjectif', 'too hot, too fast'),
    ('Trop de', 'too much / too many + nom', 'too much noise, too many cars'),
    ('Assez + adj', 'adjectif + enough', 'big enough'),
    ('Assez de', 'enough + nom', 'enough money'),
    ('Trop/assez pour', '+ to + infinitif', 'too cold to swim'),
    ('Trop (après verbe)', 'verb + too much', 'You worry too much.'),
  ],
  ex1=('Choisis la forme correcte', 'Attention à l’ordre des mots.', [
    ('This box is ______ to carry.', ['too heavy', 'too much heavy', 'very heavy enough'], 'too heavy',
     'Too + adjectif directement : too heavy.'),
    ('Is the water warm ______ for swimming?', ['enough', 'too', 'much'], 'enough',
     'Adjectif + enough : warm enough.'),
    ('We don’t have ______ chairs for everyone.', ['enough', 'too many', 'enough of'], 'enough',
     'Enough + nom : enough chairs.'),
    ('There’s ______ traffic in the city centre.', ['too much', 'too many', 'too'], 'too much',
     'Traffic est indénombrable → too much traffic.'),
    ('She’s not old ______ to drive.', ['enough', 'too', 'much'], 'enough',
     'Not + adjectif + enough : not old enough.'),
    ('He eats ______ sweets.', ['too many', 'too much', 'too'], 'too many',
     'Sweets est dénombrable pluriel → too many.'),
  ]),
  ex2=('Complète la phrase', 'Écris le mot manquant.', [
    ('Ce café est trop chaud. → This coffee is ______ hot.', 'too',
     'Trop + adjectif = too hot.'),
    ('La valise n’est pas assez grande. → The suitcase isn’t big ______ .', 'enough',
     'Enough après l’adjectif : big enough.'),
    ('Nous n’avons pas assez de temps. → We don’t have ______ time.', 'enough',
     'Enough avant le nom : enough time.'),
    ('Il fait trop froid pour sortir. → It’s too cold ______ go out.', 'to',
     'Too... to + infinitif : too cold to go out.'),
    ('Tu travailles trop. → You work too ______ .', 'much',
     'Après un verbe : too much. You work too much.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Elle est assez âgée pour voter. »', ["She's old enough to vote.", "She's enough old to vote.", "She's too old to vote."], "She's old enough to vote.",
     'Adjectif + enough + to : old enough to vote.'),
    ('« Il y a trop de monde ici. »', ['There are too many people here.', 'There is too much people here.', 'There are too people here.'], 'There are too many people here.',
     'People est pluriel → too many people.'),
    ('« Ce thé est très bon. » (compliment !)', ['This tea is very good.', 'This tea is too good.', 'This tea is good enough.'], 'This tea is very good.',
     'Compliment neutre → very. Too good suggérerait un problème.'),
    ('« Je suis trop fatigué pour conduire. »', ["I'm too tired to drive.", "I'm very tired for driving.", "I'm too much tired to drive."], "I'm too tired to drive.",
     'Too + adjectif + to + infinitif.'),
    ('« Nous n’avons pas assez de chaises. »', ["We don't have enough chairs.", "We don't have chairs enough.", 'We have too many chairs not.'], "We don't have enough chairs.",
     'Enough avant le nom : enough chairs.'),
  ]),
  game_desc='Chaque structure passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('too-adj', 'too + adjectif', 'trop — implique un problème', 'trop', 'This coffee is <b>too</b> hot.', 'This coffee is ______ hot. (trop)', 'too'),
    ('too-much', 'too much + indénombrable', 'trop de (noise, time, money...)', 'trop de (sing.)', 'There is <b>too much</b> noise.', 'There is too ______ noise.', 'much'),
    ('too-many', 'too many + pluriel', 'trop de (cars, people...)', 'trop de (pluriel)', 'There are <b>too many</b> cars.', 'There are too ______ cars.', 'many'),
    ('adj-enough', 'adjectif + enough', 'assez grand = big enough — ordre inversé', 'assez (après adj.)', 'The room is big <b>enough</b>.', 'The room is big ______ . (assez)', 'enough'),
    ('enough-noun', 'enough + nom', 'assez d’argent = enough money', 'assez de (avant nom)', 'We have <b>enough</b> money.', 'We have ______ money. (assez d’)', 'enough'),
    ('too-to', 'too ... to', 'trop... pour faire', 'trop pour', "It's too cold <b>to</b> swim.", "It's too cold ______ swim. (pour)", 'to'),
    ('enough-to', 'enough ... to', 'assez... pour faire', 'assez pour', "She's old enough <b>to</b> vote.", "She's old enough ______ vote.", 'to'),
    ('verb-too-much', 'verbe + too much', 'tu t’inquiètes trop', 'trop après verbe', 'You worry <b>too much</b>.', 'You worry too ______ .', 'much'),
  ],
),

'so-neither': dict(
  level='b1', section='grammaire', num='Ch. 20', short='So & Neither',
  title='So & Neither — Moi aussi, moi non plus',
  subtitle='So do I, neither can she : l’accord en écho',
  slides=[
    ('Moi aussi : so + auxiliaire + sujet', None,
     '<p class="slide-explanation">Pour dire « moi aussi », l’anglais reprend l’auxiliaire en écho, inversé : <b>So do I, so am I, so can I...</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>— I love jazz. — <b>So do I.</b> (Moi aussi.)</p>'
     '<p style="margin-top:8px">— I’m tired. — <b>So am I.</b></p>'
     '<p style="margin-top:8px">— She can swim. — <b>So can he.</b> (Lui aussi.)</p></div>'),
    ('Moi non plus : neither + auxiliaire + sujet', None,
     '<p class="slide-explanation">Après une phrase négative : <b>Neither do I / Neither am I...</b> (ou Nor do I).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>— I don’t smoke. — <b>Neither do I.</b> (Moi non plus.)</p>'
     '<p style="margin-top:8px">— I can’t drive. — <b>Neither can I.</b></p></div>'
     '<p style="margin-top:16px">⚠ L’auxiliaire reste affirmatif après neither : « neither don’t I » est impossible.</p>'),
    ('Quel auxiliaire choisir ?', None,
     '<p class="slide-explanation">Le même que la phrase de départ : be → be, modal → modal, sinon do/does/did.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>— I went to the concert. — <b>So did we.</b></p>'
     '<p style="margin-top:8px">— She’s been to Japan. — <b>So have I.</b></p></div>'),
    ('La version détendue : me too, me neither', None,
     '<p class="slide-explanation">À l’oral familier : <b>Me too</b> (moi aussi) et <b>Me neither</b> (moi non plus).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>— I love this song. — <b>Me too.</b></p>'
     '<p style="margin-top:8px">— I don’t like horror films. — <b>Me neither.</b></p></div>'),
    ('Pas d’accord ? I do / I don’t', None,
     '<p class="slide-explanation">Pour marquer la différence : <b>I do / I don’t / I am / I can’t</b>...</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>— I love opera. — <b>I don’t.</b> (Pas moi.)</p>'
     '<p style="margin-top:8px">— I can’t cook. — <b>I can!</b> (Moi si !)</p></div>'),
  ],
  traps=[
    ('— I love jazz. — So I do.', '— <strong>So do I.</strong>', 'L’ordre est inversé : so + auxiliaire + sujet.'),
    ('— I don’t smoke. — So do I. (moi non plus)', '— <strong>Neither do I.</strong>', 'Après une négative : neither, pas so.'),
    ('— I can’t drive. — Neither can’t I.', '— Neither <strong>can</strong> I.', 'Neither porte déjà la négation : l’auxiliaire reste affirmatif.'),
    ('— I went out. — So did I went.', '— So did I<strong>.</strong>', 'L’écho s’arrête à l’auxiliaire : so did I, sans répéter le verbe.'),
    ('— I’m hungry. — So do I.', '— So <strong>am</strong> I.', 'On reprend le même auxiliaire : be → so am I.'),
  ],
  summary=[
    ('Moi aussi', 'So + auxiliaire + sujet', 'So do I. / So am I.'),
    ('Moi non plus', 'Neither + auxiliaire + sujet', 'Neither do I.'),
    ('Familier', 'Me too / Me neither', '— I love it. — Me too.'),
    ('Désaccord', 'I do / I don’t...', '— I love opera. — I don’t.'),
    ('Règle', 'même auxiliaire, ordre inversé', 'been → So have I.'),
  ],
  ex1=('Choisis le bon écho', 'So, neither, et le bon auxiliaire.', [
    ('— I love Italian food. — ______', ['So do I.', 'So am I.', 'So I do.'], 'So do I.',
     'Love (présent simple) → do : So do I.'),
    ('— I’m exhausted. — ______', ['So am I.', 'So do I.', 'Neither am I.'], 'So am I.',
     'Be → be : So am I.'),
    ('— I don’t eat meat. — ______', ['Neither do I.', 'So do I.', "Neither don't I."], 'Neither do I.',
     'Phrase négative → neither + auxiliaire affirmatif.'),
    ('— She can speak Arabic. — ______ her brother.', ['So can', 'So does', 'Neither can'], 'So can',
     'Modal can → So can her brother.'),
    ('— We went to Spain last year. — ______', ['So did we.', 'So went we.', 'So we did.'], 'So did we.',
     'Prétérit → did : So did we.'),
    ('— I’ve never tried sushi. — ______', ['Neither have I.', 'So have I.', 'Neither I have.'], 'Neither have I.',
     'Négatif (never) + perfect → Neither have I.'),
  ]),
  ex2=('Complète l’écho', 'Écris le mot manquant.', [
    ('— I’m French. — So ______ I. (moi aussi)', 'am',
     'Be → So am I.'),
    ('— I don’t like mushrooms. — ______ do I. (moi non plus)', 'neither',
     'Après une négative : Neither do I.'),
    ('— I can swim. — So ______ I.', 'can',
     'On reprend le modal : So can I.'),
    ('— They have finished. — So ______ we.', 'have',
     'Perfect → have : So have we.'),
    ('— I love this song. — Me ______ . (familier)', 'too',
     'La version détendue : Me too.'),
  ]),
  ex3=('Choisis la bonne réaction', 'Accord, désaccord ou écho familier ?', [
    ('— I don’t like horror films. — (familier, moi non plus)', ['Me neither.', 'Me too.', 'So do I.'], 'Me neither.',
     'Après une négative, la version familière est Me neither.'),
    ('— I love opera. — (pas moi !)', ["I don't.", 'Neither do I.', 'So do I.'], "I don't.",
     'Désaccord avec une affirmative → I don’t.'),
    ('— I can’t cook at all. — (moi si !)', ['I can!', 'So can I!', 'Neither can I!'], 'I can!',
     'Contredire une négative → auxiliaire affirmatif : I can!'),
    ('— He works from home. — (elle aussi)', ['So does she.', 'So is she.', 'So she does.'], 'So does she.',
     'Présent simple, 3e personne → does : So does she.'),
    ('Quelle réponse est INCORRECTE ?', ["— I'm tired. — So do I.", "— I'm tired. — So am I.", "— I'm tired. — Me too."], "— I'm tired. — So do I.",
     'Be ne se reprend jamais avec do : So am I.'),
  ]),
  game_desc='Chaque écho passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('so-do-i', 'So do I', 'moi aussi — après un présent simple', 'moi aussi (do)', '— I love jazz. — <b>So do I.</b>', '— I love jazz. — So ______ I.', 'do'),
    ('so-am-i', 'So am I', 'moi aussi — après be', 'moi aussi (be)', "— I'm tired. — <b>So am I.</b>", "— I'm tired. — So ______ I.", 'am'),
    ('so-did', 'So did I', 'moi aussi — après un prétérit', 'moi aussi (passé)', '— I went out. — <b>So did I.</b>', '— I went out. — So ______ I.', 'did'),
    ('neither-do', 'Neither do I', 'moi non plus — auxiliaire affirmatif', 'moi non plus', "— I don't smoke. — <b>Neither do I.</b>", "— I don't smoke. — ______ do I.", 'neither'),
    ('neither-can', 'Neither can I', 'moi non plus — avec un modal', 'non plus (modal)', "— I can't drive. — <b>Neither can I.</b>", "— I can't drive. — Neither ______ I.", 'can'),
    ('me-too', 'Me too', 'moi aussi — familier', 'familier positif', '— I love this song. — <b>Me too.</b>', '— I love this song. — Me ______ .', 'too'),
    ('me-neither', 'Me neither', 'moi non plus — familier', 'familier négatif', "— I don't like it. — <b>Me neither.</b>", "— I don't like it. — Me ______ .", 'neither'),
    ('i-dont', "I don't (désaccord)", 'pas moi — marquer la différence', 'désaccord', '— I love opera. — <b>I don’t.</b>', "— I love opera. — I ______ . (pas moi)", "don't"),
  ],
),

'comparatives-superlatives': dict(
  level='b1', section='grammaire', num='Ch. 21', short='Comparatives & Superlatives',
  title='Comparatives & Superlatives — Plus, moins, le plus',
  subtitle='Bigger, more interesting, the best',
  slides=[
    ('Deux systèmes selon la longueur', None,
     '<p class="slide-explanation">Adjectif court (1 syllabe) → <b>-er / -est</b>. Adjectif long (2+ syllabes) → <b>more / the most</b>. Le français, lui, dit toujours « plus » !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>tall → taller → the tallest</b></p>'
     '<p style="margin-top:8px"><b>interesting → more interesting → the most interesting</b></p></div>'),
    ('Orthographe des courts', None,
     '<p class="slide-explanation">big → bigger (doublement), nice → nicer (e muet), happy → happier (-y → -ier). Les adjectifs en -y de 2 syllabes comptent comme courts.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>hot → hotter · easy → easier · early → earlier</b></p></div>'),
    ('Than et the', None,
     '<p class="slide-explanation">« Que » de comparaison = <b>than</b> (pas that !). Le superlatif prend <b>the</b> et se complète avec <b>in</b> pour un lieu/groupe.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>She’s taller than me.</b></p>'
     '<p style="margin-top:8px"><b>It’s the tallest building in the city.</b> (de la ville → in !)</p></div>'),
    ('Les irréguliers', None,
     '<p class="slide-explanation">good → better → the best · bad → worse → the worst · far → further → the furthest.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>This film is better than the book.</b></p>'
     '<p style="margin-top:8px"><b>It was the worst day of my life.</b></p></div>'),
    ('Égalité et écarts', None,
     '<p class="slide-explanation"><b>as ... as</b> (aussi... que), <b>not as ... as</b> (pas aussi... que), <b>much/a bit + comparatif</b> pour doser.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>He’s as tall as his father.</b></p>'
     '<p style="margin-top:8px"><b>The train is much faster than the bus.</b> (bien plus rapide)</p></div>'),
  ],
  traps=[
    ('more big, more easy', '<strong>bigger, easier</strong>', 'Adjectifs courts → -er. More est réservé aux longs.'),
    ('She is taller that me.', 'She is taller <strong>than</strong> me.', '« Que » comparatif = than, jamais that.'),
    ('the most tall building of the city', 'the <strong>tallest</strong> building <strong>in</strong> the city', 'Court → -est, et « de la ville » → in the city.'),
    ('This film is more better.', 'This film is <strong>better</strong>.', 'Better est déjà un comparatif : jamais more devant.'),
    ('He is so tall as his father. (aussi grand que)', 'He is <strong>as</strong> tall <strong>as</strong> his father.', 'Égalité = as... as (so... as seulement à la négative).'),
  ],
  summary=[
    ('Courts', '-er / the -est', 'taller, the tallest'),
    ('Longs', 'more / the most', 'more interesting'),
    ('Que', 'than', 'taller than me'),
    ('Irréguliers', 'better/best, worse/worst', 'better than the book'),
    ('Aussi... que', 'as ... as', 'as tall as his father'),
    ('De la ville/du monde', 'in the city / in the world', 'the best in the world'),
  ],
  ex1=('Choisis la forme correcte', 'Court, long ou irrégulier ?', [
    ('My new flat is ______ than the old one.', ['bigger', 'more big', 'biggest'], 'bigger',
     'Big est court → bigger (avec doublement du g).'),
    ('This book is ______ than the film.', ['more interesting', 'interestinger', 'most interesting'], 'more interesting',
     'Interesting est long → more interesting.'),
    ('It’s ______ restaurant in town.', ['the best', 'the better', 'best'], 'the best',
     'Superlatif irrégulier de good → the best.'),
    ('Today is ______ than yesterday.', ['hotter', 'more hot', 'hottest'], 'hotter',
     'Hot → hotter (doublement du t).'),
    ('She’s not as tall ______ her sister.', ['as', 'than', 'that'], 'as',
     'Égalité (même à la négative) : as... as.'),
    ('The exam was ______ than I expected.', ['easier', 'more easy', 'easyer'], 'easier',
     'Easy (2 syllabes en -y) → easier.'),
  ]),
  ex2=('Écris la forme demandée', 'Comparatif ou superlatif du mot entre parenthèses.', [
    ('My brother is ______ than me. (old)', 'older',
     'Court → older.'),
    ('This is ______ day of the year. (hot, superlatif avec the)', 'the hottest',
     'The + hottest (doublement) : le jour le plus chaud.'),
    ('The weather today is ______ than yesterday. (bad)', 'worse',
     'Irrégulier : bad → worse.'),
    ('This is ______ film I’ve ever seen. (good, superlatif avec the)', 'the best',
     'Good → the best : le meilleur film que j’aie jamais vu.'),
    ('Trains are ______ than planes for short trips. (practical, comparatif)', 'more practical',
     'Practical est long → more practical.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Elle est plus grande que moi. »', ['She is taller than me.', 'She is more tall than me.', 'She is taller that me.'], 'She is taller than me.',
     'Court → taller, et que → than.'),
    ('« C’est le plus haut bâtiment de la ville. »', ["It's the tallest building in the city.", "It's the most tall building of the city.", "It's the taller building in the city."], "It's the tallest building in the city.",
     'Superlatif -est + in the city.'),
    ('« Ce film est bien meilleur que le livre. »', ['This film is much better than the book.', 'This film is much more better than the book.', 'This film is very better than the book.'], 'This film is much better than the book.',
     '« Bien meilleur » = much better — jamais more better.'),
    ('« Il est aussi rapide que son frère. »', ["He's as fast as his brother.", "He's so fast as his brother.", "He's as fast than his brother."], "He's as fast as his brother.",
     'Égalité : as fast as.'),
    ('« C’était la pire journée de ma vie. »', ['It was the worst day of my life.', 'It was the most bad day of my life.', 'It was the worse day of my life.'], 'It was the worst day of my life.',
     'Superlatif irrégulier de bad → the worst.'),
  ]),
  game_desc='Chaque structure de comparaison passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('taller', 'taller (court + -er)', 'plus grand — adjectif court', 'comparatif court', 'She is <b>taller</b> than me.', 'She is ______ than me. (plus grande)', 'taller'),
    ('more-interesting', 'more + adjectif long', 'plus intéressant — adjectif long', 'comparatif long', 'This book is <b>more</b> interesting.', 'This book is ______ interesting. (plus)', 'more'),
    ('than', 'than', 'que — jamais that', 'que comparatif', 'She is taller <b>than</b> me.', 'She is taller ______ me. (que)', 'than'),
    ('the-tallest', 'the + -est', 'le plus grand — superlatif court', 'superlatif court', "It's <b>the tallest</b> building in the city.", "It's the ______ building in the city. (le plus haut)", 'tallest'),
    ('better', 'better', 'meilleur — irrégulier de good', 'irrégulier good', 'This film is <b>better</b> than the book.', 'This film is ______ than the book. (meilleur)', 'better'),
    ('worst', 'the worst', 'le pire — irrégulier de bad', 'irrégulier bad', 'It was <b>the worst</b> day of my life.', 'It was the ______ day of my life. (pire)', 'worst'),
    ('as-as', 'as ... as', 'aussi... que', 'égalité', "He's <b>as</b> tall <b>as</b> his father.", "He's ______ tall as his father. (aussi)", 'as'),
    ('in-the-city', 'superlatif + in', 'le plus... DE la ville = in the city', 'in après superlatif', 'The best restaurant <b>in</b> town.', 'The best restaurant ______ town. (de la ville)', 'in'),
  ],
),
}
