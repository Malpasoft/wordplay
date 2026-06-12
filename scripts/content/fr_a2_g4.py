# -*- coding: utf-8 -*-
"""fr/ A2 grammaire — lot 4 (chapitres 16-19). Explications en français, anglais cible."""

CHAPTERS = {

'conjunctions': dict(
  level='a2', section='grammaire', num='Ch. 16', short='Les conjonctions',
  title='Les conjonctions — and, but, so, because',
  subtitle='Relier ses idées : la différence entre la cause et la conséquence',
  slides=[
    ('Les quatre conjonctions de base', None,
     '<p class="slide-explanation">Pour relier deux idées dans une phrase, l\'anglais utilise des <b>conjonctions</b>. Les quatre premières sont transparentes pour un francophone.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>and</b> (et) — I like tea <b>and</b> coffee.</p>'
     '<p style="margin-top:8px"><b>but</b> (mais) — He is rich <b>but</b> unhappy.</p>'
     '<p style="margin-top:8px"><b>or</b> (ou) — Do you want tea <b>or</b> coffee?</p>'
     '<p style="margin-top:8px"><b>so</b> (donc, alors) — It was late, <b>so</b> I went home.</p></div>'
     '<p style="margin-top:16px">La ponctuation est plus légère qu\'en français : pas de virgule obligatoire avant and/but dans les phrases courtes.</p>'),
    ('Because et so : cause ou conséquence ?', None,
     '<p class="slide-explanation">Le piège classique : <b>because</b> introduit la <b>cause</b>, <b>so</b> introduit la <b>conséquence</b>. Les deux relient les mêmes idées, mais dans des sens opposés.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I stayed at home <b>because</b> it was raining. — ... parce qu\'il pleuvait. (cause)</p>'
     '<p style="margin-top:8px">It was raining, <b>so</b> I stayed at home. — ... donc je suis resté. (conséquence)</p></div>'
     '<p style="margin-top:16px">Test rapide : si tu peux dire « parce que » → because. Si tu peux dire « donc » → so. Ne les utilise jamais ensemble dans la même phrase !</p>'),
    ('When : quand deux actions se rencontrent', None,
     '<p class="slide-explanation"><b>When</b> (quand) relie deux actions dans le temps. À retenir : après when, on utilise le <b>présent</b> pour parler du futur — jamais will !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>When</b> I arrived, everyone was sleeping. — Quand je suis arrivé, tout le monde dormait.</p>'
     '<p style="margin-top:8px">I\'ll call you <b>when</b> I <b>get</b> home. — Je t\'appellerai quand j\'arriverai. (présent get, pas will get !)</p></div>'
     '<p style="margin-top:16px">Le français dit « quand j\'arriverai » (futur) ; l\'anglais dit when I GET home (présent). C\'est une faute d\'interférence très fréquente.</p>'),
    ('If : la condition', None,
     '<p class="slide-explanation"><b>If</b> (si) introduit une condition. Comme avec when : après if, le <b>présent</b> suffit, même si la phrase parle du futur.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>If</b> it rains, we\'ll stay at home. — S\'il pleut, nous resterons à la maison.</p>'
     '<p style="margin-top:8px"><b>If</b> you\'re tired, go to bed. — Si tu es fatigué, va te coucher.</p></div>'
     '<p style="margin-top:16px">Structure : If + présent, will + verbe. Jamais « If it will rain » — le will reste dans l\'autre moitié de la phrase.</p>'),
    ('Enchaîner un récit : then, after that, finally', None,
     '<p class="slide-explanation">Pour raconter une suite d\'événements (très utile en rédaction), ajoute ces mots de liaison en début de phrase.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>First</b>, we visited the castle. — D\'abord...</p>'
     '<p style="margin-top:8px"><b>Then</b> we had lunch by the river. — Ensuite...</p>'
     '<p style="margin-top:8px"><b>After that</b>, we went shopping. <b>Finally</b>, we took the train home. — Après cela... Enfin...</p></div>'
     '<p style="margin-top:16px">Quatre jalons (first, then, after that, finally) suffisent pour structurer n\'importe quel récit A2.</p>'),
  ],
  traps=[
    ('I stayed at home because it was raining, so I stayed.', 'It was raining, <strong>so</strong> I stayed at home.', 'Because OU so — jamais les deux pour la même relation cause-conséquence.'),
    ('I\'ll call you when I will arrive.', 'I\'ll call you when I <strong>arrive</strong>.', 'Après when (sens futur), le présent : when I ARRIVE. Le français utilise le futur, pas l\'anglais.'),
    ('If it will rain, we will stay at home.', '<strong>If it rains</strong>, we will stay at home.', 'Après if, le présent : if it RAINS. Le will reste dans la proposition principale.'),
    ('He is rich but he is not happy but he smiles.', 'He is rich <strong>but</strong> not happy.', 'Un seul but par phrase — sinon le contraste se perd. Allège : rich but not happy.'),
    ('I like coffee and I don\'t like tea.', 'I like coffee <strong>but</strong> I don\'t like tea.', 'Deux idées opposées → but, pas and : I like coffee BUT I don\'t like tea.'),
  ],
  summary=[
    ('Addition', 'and = et', 'I like tea and coffee.'),
    ('Contraste', 'but = mais', 'He is rich but unhappy.'),
    ('Cause', 'because = parce que', 'I stayed in because it was raining.'),
    ('Conséquence', 'so = donc', 'It was raining, so I stayed in.'),
    ('Temps/condition', 'when / if + PRÉSENT (jamais will)', 'When I get home... / If it rains...'),
    ('Récit', 'first · then · after that · finally', 'First we visited... Finally we left.'),
  ],
  ex1=('Choisis la bonne conjonction', 'Cause, conséquence, contraste ou addition ?', [
    ('I was tired, ______ I went to bed early.', ['so', 'because', 'but'], 'so',
     'Conséquence (donc) → SO : j\'étais fatigué, DONC je me suis couché.'),
    ('I went to bed early ______ I was tired.', ['because', 'so', 'and'], 'because',
     'Cause (parce que) → BECAUSE : ... PARCE QUE j\'étais fatigué.'),
    ('She likes music ______ she can\'t sing.', ['but', 'and', 'so'], 'but',
     'Contraste → BUT : elle aime la musique MAIS ne sait pas chanter.'),
    ('Do you want pasta ______ rice?', ['or', 'and', 'but'], 'or',
     'Choix → OR : des pâtes OU du riz ?'),
    ('I bought bread, milk ______ eggs.', ['and', 'or', 'so'], 'and',
     'Énumération → AND : du pain, du lait ET des œufs.'),
    ('______ it rains tomorrow, we\'ll stay at home.', ['If', 'So', 'But'], 'If',
     'Condition → IF : S\'IL pleut demain.'),
  ]),
  ex2=('Complète la phrase', 'Écris la conjonction ou la forme verbale qui manque.', [
    ('It was cold, ______ I took my coat. (donc)', 'so',
     'Conséquence → SO.'),
    ('I love this song ______ the lyrics are beautiful. (parce que)', 'because',
     'Cause → BECAUSE.'),
    ('I\'ll call you when I ______ home. (arriver — attention au temps !)', 'get',
     'Après when, présent : when I GET home — jamais will get.'),
    ('If it ______ sunny, we\'ll go to the beach. (être — attention au temps !)', 'is',
     'Après if, présent : if it IS sunny.'),
    ('______ we visited the museum. Then we had lunch. (d\'abord)', 'First',
     'Le récit commence par FIRST, puis then, after that, finally.'),
  ]),
  ex3=('Corrige les fautes de liaison', 'Choisis la version correcte.', [
    ('« If it will rain, we will cancel the picnic. »', ['If it rains, we will cancel the picnic.', 'If it rain, we will cancel the picnic.', 'If it would rain, we cancel the picnic.'], 'If it rains, we will cancel the picnic.',
     'If + présent (rains), will dans la principale.'),
    ('« I\'ll text you when I will arrive at the station. »', ['I\'ll text you when I arrive at the station.', 'I\'ll text you when I arrived at the station.', 'I text you when I will arrive.'], 'I\'ll text you when I arrive at the station.',
     'When + présent pour le futur : when I ARRIVE.'),
    ('« He was hungry, because he made a sandwich. »', ['He was hungry, so he made a sandwich.', 'He was hungry, and so because he made a sandwich.', 'He was hungry but he made a sandwich.'], 'He was hungry, so he made a sandwich.',
     'La faim est la cause, le sandwich la conséquence → SO.'),
    ('« I like swimming and I hate running. »', ['I like swimming but I hate running.', 'I like swimming or I hate running.', 'I like swimming so I hate running.'], 'I like swimming but I hate running.',
     'Opposition aimer/détester → BUT.'),
    ('« Finally, we visited the castle. Then we arrived. First we left. » (ordre !)', ['First we arrived. Then we visited the castle. Finally, we left.', 'Then we arrived. First we visited. Finally we left.', 'Finally we arrived. First we visited. Then we left.'], 'First we arrived. Then we visited the castle. Finally, we left.',
     'L\'ordre logique du récit : first → then → finally.'),
  ]),
  game_desc='Chaque conjonction passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('and', 'and', 'et — pour ajouter une idée', 'addition', 'I like tea <b>and</b> coffee.', 'I like tea ______ coffee. (et)', 'and'),
    ('but', 'but', 'mais — pour opposer deux idées', 'contraste', 'He is rich <b>but</b> unhappy.', 'He is rich ______ unhappy. (mais)', 'but'),
    ('or', 'or', 'ou — pour proposer un choix', 'choix', 'Do you want tea <b>or</b> coffee?', 'Do you want tea ______ coffee? (ou)', 'or'),
    ('because', 'because', 'parce que — introduit la cause', 'cause', 'I stayed in <b>because</b> it was raining.', 'I stayed in ______ it was raining. (parce que)', 'because'),
    ('so', 'so', 'donc — introduit la conséquence', 'conséquence', 'It was raining, <b>so</b> I stayed in.', 'It was raining, ______ I stayed in. (donc)', 'so'),
    ('when-present', 'when I get home', 'quand + présent — jamais will après when', 'temps', 'I\'ll call you when I <b>get</b> home.', 'I\'ll call you when I ______ home. (arrive, au présent)', 'get'),
    ('if', 'if it rains', 'si + présent — la condition', 'condition', '<b>If</b> it rains, we\'ll stay at home.', '______ it rains, we\'ll stay at home. (si)', 'if'),
    ('finally', 'finally', 'enfin — le dernier jalon du récit', 'récit', '<b>Finally</b>, we took the train home.', '______, we took the train home. (enfin)', 'finally'),
  ],
),

'adverbs-manner': dict(
  level='a2', section='grammaire', num='Ch. 17', short='Adverbes de manière',
  title='Les adverbes de manière — slowly, well, hard',
  subtitle='Adjectif + -ly : dire comment on fait les choses',
  slides=[
    ('Adjectif + -ly = adverbe', None,
     '<p class="slide-explanation">Pour dire <b>comment</b> on fait une action, l\'anglais transforme l\'adjectif en adverbe avec <b>-ly</b> — l\'équivalent du « -ment » français.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>slow (lent) → <b>slowly</b> (lentement) — He drives <b>slowly</b>.</p>'
     '<p style="margin-top:8px">quiet (silencieux) → <b>quietly</b> — She speaks <b>quietly</b>.</p>'
     '<p style="margin-top:8px">careful (prudent) → <b>carefully</b> — Read the question <b>carefully</b>.</p></div>'
     '<p style="margin-top:16px">L\'adverbe se place généralement <b>après le verbe</b> (ou après le complément) : he drives slowly.</p>'),
    ('Adjectif ou adverbe ? Le test du verbe', None,
     '<p class="slide-explanation">L\'erreur du francophone : utiliser l\'adjectif à la place de l\'adverbe. Le test : si le mot décrit un <b>verbe</b> (comment ?), il faut l\'adverbe en -ly.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>She is a <b>slow</b> driver. (adjectif — décrit driver, un nom)</p>'
     '<p style="margin-top:8px">She drives <b>slowly</b>. (adverbe — décrit drives, un verbe)</p>'
     '<p style="margin-top:8px;color:var(--muted)">(« She drives slow » est incorrect à l\'écrit)</p></div>'
     '<p style="margin-top:16px">Demande-toi : est-ce que je décris une chose (adjectif) ou une action (adverbe) ?</p>'),
    ('Good → well : l\'irrégulier à connaître', None,
     '<p class="slide-explanation">L\'adverbe de <b>good</b> n\'est pas « goodly » mais <b>well</b>. C\'est LA faute la plus fréquente du chapitre.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>She is a <b>good</b> singer. — C\'est une bonne chanteuse. (adjectif)</p>'
     '<p style="margin-top:8px">She sings <b>well</b>. — Elle chante bien. (adverbe)</p>'
     '<p style="margin-top:8px;color:var(--muted)">(jamais « she sings good » ni « she sings very good »)</p></div>'
     '<p style="margin-top:16px">Attention : How are you? — I\'m <b>well</b> (je vais bien). Well sert aussi d\'adjectif de santé.</p>'),
    ('Hard, fast, late : pas de -ly !', None,
     '<p class="slide-explanation">Quelques adverbes gardent la <b>même forme que l\'adjectif</b> : hard, fast, late, early. Ajouter -ly change le sens ou crée une faute.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>She works <b>hard</b>. — Elle travaille dur. (hardly = à peine — un autre mot !)</p>'
     '<p style="margin-top:8px">He runs <b>fast</b>. — Il court vite. (« fastly » n\'existe pas)</p>'
     '<p style="margin-top:8px">The train arrived <b>late</b>. — Le train est arrivé en retard. (lately = ces derniers temps !)</p></div>'
     '<p style="margin-top:16px">Piège majeur : <b>hardly</b> ne veut PAS dire « durement » mais « à peine » : I hardly know him = je le connais à peine.</p>'),
    ('L\'orthographe du -ly', None,
     '<p class="slide-explanation">Quelques ajustements en ajoutant -ly, faciles à retenir.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>consonne + y → -ily : happy → <b>happily</b> · easy → <b>easily</b></p>'
     '<p style="margin-top:8px">-le → -ly : terrible → <b>terribly</b> · comfortable → <b>comfortably</b></p>'
     '<p style="margin-top:8px">-ic → -ically : automatic → <b>automatically</b></p></div>'
     '<p style="margin-top:16px">Et certains mots en -ly sont des <b>adjectifs</b>, pas des adverbes : friendly, lovely, lonely. « She smiled friendly » est faux — on dit in a friendly way.</p>'),
  ],
  traps=[
    ('She sings very good.', 'She sings very <strong>well</strong>.', 'L\'adverbe de good est well : she sings WELL. Good est l\'adjectif (a good singer).'),
    ('He drives very fastly.', 'He drives very <strong>fast</strong>.', 'Fast est identique en adjectif et adverbe : « fastly » n\'existe pas.'),
    ('They work hardly every day.', 'They work <strong>hard</strong> every day.', 'Hard = dur (adverbe identique à l\'adjectif). Hardly = à peine — un sens complètement différent !'),
    ('Please listen careful.', 'Please listen <strong>carefully</strong>.', 'Listen est un verbe → adverbe en -ly : listen CAREFULLY.'),
    ('She speaks English very easy.', 'She speaks English very <strong>easily</strong>.', 'Easy → easily (consonne + y → -ily) : elle parle FACILEMENT.'),
  ],
  summary=[
    ('Formation', 'adjectif + -ly', 'slow → slowly · quiet → quietly'),
    ('Position', 'après le verbe (+ complément)', 'He drives slowly.'),
    ('Irrégulier', 'good → well', 'She sings well.'),
    ('Sans -ly', 'hard · fast · late · early', 'She works hard. / He runs fast.'),
    ('Pièges de sens', 'hardly = à peine · lately = récemment', 'I hardly know him.'),
    ('Orthographe', 'happy → happily · terrible → terribly', 'easily / automatically'),
  ],
  ex1=('Adjectif ou adverbe ?', 'Décide si le mot décrit un nom ou un verbe.', [
    ('She is a ______ driver.', ['careful', 'carefully', 'carefuly'], 'careful',
     'Driver est un nom → adjectif : a CAREFUL driver.'),
    ('She drives ______.', ['carefully', 'careful', 'carefulness'], 'carefully',
     'Drives est un verbe → adverbe : drives CAREFULLY.'),
    ('He speaks English very ______.', ['well', 'good', 'goodly'], 'well',
     'L\'adverbe de good est WELL : he speaks English well.'),
    ('My grandfather walks very ______.', ['slowly', 'slow', 'slowness'], 'slowly',
     'Walks est un verbe → SLOWLY.'),
    ('She passed the exam ______.', ['easily', 'easy', 'easyly'], 'easily',
     'Easy → EASILY (y → -ily).'),
    ('Be ______! The floor is wet.', ['careful', 'carefully', 'carefulness'], 'careful',
     'Après be → adjectif : be CAREFUL.'),
  ]),
  ex2=('Forme l\'adverbe', 'Écris l\'adverbe correspondant à l\'adjectif.', [
    ('quiet → Please close the door ______.', 'quietly',
     'Quiet + ly = QUIETLY.'),
    ('good → She plays the piano very ______. (irrégulier !)', 'well',
     'Good → WELL, l\'irrégulier à connaître absolument.'),
    ('happy → The children played ______ in the garden.', 'happily',
     'Happy → HAPPILY (consonne + y → -ily).'),
    ('fast → He runs very ______. (attention, pas de -ly !)', 'fast',
     'Fast ne change pas : he runs FAST.'),
    ('hard → They worked ______ all week. (attention, pas de -ly !)', 'hard',
     'Hard ne change pas. Hardly voudrait dire « à peine » !'),
  ]),
  ex3=('Trouve la phrase correcte', 'Attention aux faux adverbes !', [
    ('« Elle chante très bien. »', ['She sings very well.', 'She sings very good.', 'She sings very goodly.'], 'She sings very well.',
     'L\'adverbe de good est WELL.'),
    ('« Il travaille dur. »', ['He works hard.', 'He works hardly.', 'He hardly works.'], 'He works hard.',
     'Hard = dur. He hardly works = il travaille à peine — le contraire !'),
    ('« Parle plus lentement, s\'il te plaît. »', ['Please speak more slowly.', 'Please speak more slow.', 'Please speak slowlier.'], 'Please speak more slowly.',
     'Speak est un verbe → adverbe SLOWLY, comparatif avec more.'),
    ('« Le train est arrivé en retard. »', ['The train arrived late.', 'The train arrived lately.', 'The train lately arrived.'], 'The train arrived late.',
     'Late = en retard. Lately = ces derniers temps !'),
    ('« Elle m\'a souri gentiment. »', ['She smiled at me in a friendly way.', 'She smiled at me friendly.', 'She smiled at me friendlyly.'], 'She smiled at me in a friendly way.',
     'Friendly est un ADJECTIF : pour l\'adverbe, on dit in a friendly way.'),
  ]),
  game_desc='Chaque adverbe de manière passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('slowly', 'slowly', 'lentement — adjectif + -ly', '-ly', 'He drives <b>slowly</b>.', 'He drives ______. (lentement)', 'slowly'),
    ('carefully', 'carefully', 'prudemment / attentivement — careful + -ly', 'attention', 'Read the question <b>carefully</b>.', 'Read the question ______. (attentivement)', 'carefully'),
    ('well', 'well', 'bien — l\'adverbe irrégulier de good', 'good → well', 'She sings very <b>well</b>.', 'She sings very ______. (bien)', 'well'),
    ('hard', 'hard', 'dur — même forme que l\'adjectif, jamais hardly', 'sans -ly', 'They work <b>hard</b> every day.', 'They work ______ every day. (dur)', 'hard'),
    ('fast', 'fast', 'vite — « fastly » n\'existe pas', 'sans -ly', 'He runs very <b>fast</b>.', 'He runs very ______. (vite)', 'fast'),
    ('late', 'late', 'en retard — lately veut dire « récemment »', 'sans -ly', 'The train arrived <b>late</b>.', 'The train arrived ______. (en retard)', 'late'),
    ('easily', 'easily', 'facilement — easy → easily (y → i)', 'orthographe', 'She passed the exam <b>easily</b>.', 'She passed the exam ______. (facilement)', 'easily'),
    ('happily', 'happily', 'joyeusement — happy → happily', 'orthographe', 'The children played <b>happily</b>.', 'The children played ______. (joyeusement)', 'happily'),
  ],
),

'prepositions-movement': dict(
  level='a2', section='grammaire', num='Ch. 18', short='Prépositions de mouvement',
  title='Les prépositions de mouvement — to, into, through, across',
  subtitle='Décrire les déplacements : d\'où l\'on vient, où l\'on va, par où l\'on passe',
  slides=[
    ('To et from : la destination et l\'origine', None,
     '<p class="slide-explanation">Les deux piliers du mouvement : <b>to</b> (vers, à — la destination) et <b>from</b> (de, depuis — l\'origine).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>We walked <b>to</b> the station. — Nous avons marché jusqu\'à la gare.</p>'
     '<p style="margin-top:8px">She comes <b>from</b> Italy. — Elle vient d\'Italie.</p>'
     '<p style="margin-top:8px">The train goes <b>from</b> Paris <b>to</b> London. — Le train va de Paris à Londres.</p></div>'
     '<p style="margin-top:16px">Rappel A1 : go home, sans to ! Et arrive ne prend jamais to : on dit arrive AT (un endroit) ou arrive IN (une ville).</p>'),
    ('Into et out of : entrer et sortir', None,
     '<p class="slide-explanation"><b>Into</b> = mouvement vers l\'intérieur ; <b>out of</b> = mouvement vers l\'extérieur. Ils remplacent in/out quand il y a déplacement.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>She walked <b>into</b> the room. — Elle est entrée dans la pièce.</p>'
     '<p style="margin-top:8px">He ran <b>out of</b> the house. — Il est sorti de la maison en courant.</p>'
     '<p style="margin-top:8px">Get <b>into</b> the car! — Monte dans la voiture !</p></div>'
     '<p style="margin-top:16px">Remarque le génie de l\'anglais : le verbe donne la manière (walk, run), la préposition donne la direction. « Entrer en courant » = run into.</p>'),
    ('Through, across, along : par où on passe', None,
     '<p class="slide-explanation">Trois prépositions de trajet, à bien distinguer.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>through</b> = à travers (un volume) — We drove <b>through</b> the tunnel.</p>'
     '<p style="margin-top:8px"><b>across</b> = d\'un côté à l\'autre (une surface) — She swam <b>across</b> the river.</p>'
     '<p style="margin-top:8px"><b>along</b> = le long de — They walked <b>along</b> the beach.</p></div>'
     '<p style="margin-top:16px">Through pour un tunnel, une forêt, une foule (3D) ; across pour une rue, une rivière, un pont (2D).</p>'),
    ('Up, down, over, under : les directions', None,
     '<p class="slide-explanation">Les directions verticales et le passage au-dessus / en dessous.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>up</b> = vers le haut — We climbed <b>up</b> the hill.</p>'
     '<p style="margin-top:8px"><b>down</b> = vers le bas — She ran <b>down</b> the stairs.</p>'
     '<p style="margin-top:8px"><b>over</b> = par-dessus — The cat jumped <b>over</b> the wall.</p>'
     '<p style="margin-top:8px"><b>past</b> = devant (en passant) — We walked <b>past</b> the bakery.</p></div>'
     '<p style="margin-top:16px">Walk past the bakery = passer devant la boulangerie (sans s\'arrêter) — très utile pour les itinéraires.</p>'),
    ('Donner un itinéraire', None,
     '<p class="slide-explanation">Avec ces prépositions et l\'impératif (chapitre A1), tu peux donner et comprendre un itinéraire complet — exercice classique d\'examen A2.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Go along</b> this street and <b>turn left</b> at the bank.</p>'
     '<p style="margin-top:8px"><b>Go across</b> the bridge and <b>through</b> the park.</p>'
     '<p style="margin-top:8px">Walk <b>past</b> the church — the museum is <b>on your right</b>.</p></div>'
     '<p style="margin-top:16px">Boîte à outils itinéraire : go along, turn left/right, go past, go across, it\'s on your left/right.</p>'),
  ],
  traps=[
    ('We arrived to the station at 6.', 'We arrived <strong>at</strong> the station at 6.', 'Arrive ne prend jamais to : arrive AT + lieu, arrive IN + ville.'),
    ('She entered into the room.', 'She <strong>entered</strong> the room. / She walked <strong>into</strong> the room.', 'Enter se construit sans préposition (enter the room) ; ou bien walk/go INTO.'),
    ('We crossed across the street.', 'We <strong>crossed</strong> the street. / We went <strong>across</strong> the street.', 'Cross contient déjà l\'idée de traversée : cross the street, sans across.'),
    ('He went at London last week.', 'He went <strong>to</strong> London last week.', 'Go + destination → TO : go TO London.'),
    ('Walk among the tunnel.', 'Walk <strong>through</strong> the tunnel.', 'À travers un volume (tunnel, forêt) → THROUGH. Among = parmi (des personnes/objets).'),
  ],
  summary=[
    ('Destination', 'to = vers · from = depuis', 'from Paris to London'),
    ('Entrer/sortir', 'into = vers l\'intérieur · out of = hors de', 'She walked into the room.'),
    ('Trajet', 'through (3D) · across (2D) · along', 'through the tunnel / across the river'),
    ('Vertical', 'up = monter · down = descendre', 'up the hill / down the stairs'),
    ('Passage', 'over = par-dessus · past = devant', 'over the wall / past the bakery'),
    ('Arrive', 'arrive AT + lieu / IN + ville (jamais to !)', 'We arrived at the station.'),
  ],
  ex1=('Choisis la préposition de mouvement', 'Direction, trajet ou passage ?', [
    ('We walked ______ the station.', ['to', 'at', 'into'], 'to',
     'Destination → TO the station.'),
    ('She ran ______ the stairs to the second floor.', ['up', 'over', 'across'], 'up',
     'Vers le haut → UP the stairs.'),
    ('The train went ______ a long tunnel.', ['through', 'across', 'along'], 'through',
     'À travers un volume → THROUGH the tunnel.'),
    ('We walked ______ the bridge to the other side.', ['across', 'through', 'out of'], 'across',
     'D\'un côté à l\'autre d\'une surface → ACROSS the bridge.'),
    ('He jumped ______ the wall and escaped.', ['over', 'under', 'into'], 'over',
     'Par-dessus → OVER the wall.'),
    ('She got ______ the car and drove away.', ['into', 'to', 'at'], 'into',
     'Mouvement vers l\'intérieur → INTO the car.'),
  ]),
  ex2=('Complète l\'itinéraire', 'Écris la préposition qui manque.', [
    ('Go ______ this street until the traffic lights. (le long de)', 'along',
     'Le long de la rue → ALONG this street.'),
    ('Walk ______ the church — the museum is behind it. (devant, en passant)', 'past',
     'Passer devant → PAST the church.'),
    ('He ran ______ of the house. (hors de, deux mots — écris le premier)', 'out',
     'Sortir → OUT of the house.'),
    ('She comes ______ Spain. (origine)', 'from',
     'L\'origine → FROM Spain.'),
    ('We arrived ______ the airport two hours early. (attention, pas to !)', 'at',
     'Arrive AT + lieu : arrived AT the airport.'),
  ]),
  ex3=('Trouve la phrase correcte', 'Attention aux verbes qui n\'aiment pas les prépositions !', [
    ('« Nous sommes arrivés à Londres. »', ['We arrived in London.', 'We arrived to London.', 'We arrived at London.'], 'We arrived in London.',
     'Arrive IN + ville : arrived IN London. (At pour les lieux précis.)'),
    ('« Elle est entrée dans la salle. »', ['She entered the room.', 'She entered into the room.', 'She entered to the room.'], 'She entered the room.',
     'Enter sans préposition : enter THE ROOM directement.'),
    ('« Nous avons traversé la rue. »', ['We crossed the street.', 'We crossed across the street.', 'We acrossed the street.'], 'We crossed the street.',
     'Cross + complément direct : cross the street.'),
    ('« Ils ont marché le long de la plage. »', ['They walked along the beach.', 'They walked through the beach.', 'They walked among the beach.'], 'They walked along the beach.',
     'Le long de → ALONG the beach.'),
    ('« Monte dans le bus ! »', ['Get on the bus!', 'Get into the bus!', 'Go in bus!'], 'Get on the bus!',
     'Transports publics : get ON the bus (mais get INTO the car !).'),
  ]),
  game_desc='Chaque préposition de mouvement passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('to', 'to', 'vers / à — la destination du mouvement', 'destination', 'We walked <b>to</b> the station.', 'We walked ______ the station. (vers)', 'to'),
    ('from', 'from', 'de / depuis — l\'origine du mouvement', 'origine', 'She comes <b>from</b> Italy.', 'She comes ______ Italy. (de)', 'from'),
    ('into', 'into', 'dans (avec mouvement) — entrer à l\'intérieur', 'entrer', 'She walked <b>into</b> the room.', 'She walked ______ the room. (dans)', 'into'),
    ('out-of', 'out of', 'hors de — sortir de l\'intérieur', 'sortir', 'He ran <b>out of</b> the house.', 'He ran ______ of the house. (hors)', 'out'),
    ('through', 'through', 'à travers — un volume : tunnel, forêt', 'à travers', 'We drove <b>through</b> the tunnel.', 'We drove ______ the tunnel. (à travers)', 'through'),
    ('across', 'across', 'd\'un côté à l\'autre — une surface : rue, pont', 'traverser', 'She swam <b>across</b> the river.', 'She swam ______ the river. (à travers)', 'across'),
    ('along', 'along', 'le long de — suivre une ligne', 'longer', 'They walked <b>along</b> the beach.', 'They walked ______ the beach. (le long de)', 'along'),
    ('past', 'past', 'devant (en passant) — sans s\'arrêter', 'passer devant', 'Walk <b>past</b> the church.', 'Walk ______ the church. (devant)', 'past'),
  ],
),

'indirect-questions': dict(
  level='a2', section='grammaire', num='Ch. 19', short='Questions indirectes',
  title='Les questions indirectes — Can you tell me where the station is?',
  subtitle='Poser une question poliment : l\'inversion disparaît',
  slides=[
    ('La question indirecte : plus polie', None,
     '<p class="slide-explanation">Pour demander quelque chose poliment (à un inconnu, dans la rue, dans un magasin), l\'anglais enveloppe la question dans une formule : <b>Can you tell me...?</b> / <b>Do you know...?</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Direct : <b>Where is the station?</b></p>'
     '<p style="margin-top:8px">Indirect : <b>Can you tell me where the station is?</b></p>'
     '<p style="margin-top:8px">Indirect : <b>Do you know where the station is?</b></p></div>'
     '<p style="margin-top:16px">C\'est l\'équivalent du « Pourriez-vous me dire où... » français — incontournable à l\'oral comme aux examens.</p>'),
    ('LA règle : plus d\'inversion !', None,
     '<p class="slide-explanation">Dans la question indirecte, l\'ordre des mots redevient celui d\'une <b>phrase normale</b> : sujet + verbe. L\'inversion et le do/does/did disparaissent !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Where <b>is the station</b>? → Can you tell me where <b>the station is</b>?</p>'
     '<p style="margin-top:8px">What time <b>does the shop open</b>? → Do you know what time <b>the shop opens</b>?</p>'
     '<p style="margin-top:8px;color:var(--muted)">(le does disparaît, et le verbe récupère son -s !)</p></div>'
     '<p style="margin-top:16px">Mémo : après where/what/when..., remets les mots dans l\'ordre d\'une affirmation.</p>'),
    ('Avec do/does/did : l\'auxiliaire s\'efface', None,
     '<p class="slide-explanation">Quand la question directe utilise do/does/did, l\'indirecte les <b>supprime</b> et reconjugue le verbe.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Where <b>does she live</b>? → Do you know where she <b>lives</b>?</p>'
     '<p style="margin-top:8px">When <b>did they arrive</b>? → Can you tell me when they <b>arrived</b>?</p>'
     '<p style="margin-top:8px">What <b>do you want</b>? → Tell me what you <b>want</b>.</p></div>'
     '<p style="margin-top:16px">Le temps ne change pas : does she live → she liveS (présent) ; did they arrive → they arrivED (passé).</p>'),
    ('Les questions oui/non : if ou whether', None,
     '<p class="slide-explanation">Quand la question directe n\'a pas de mot interrogatif (réponse oui/non), la question indirecte commence par <b>if</b> (= si).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Is there a bank near here? → Do you know <b>if there is</b> a bank near here?</p>'
     '<p style="margin-top:8px">Does this bus go to the centre? → Can you tell me <b>if this bus goes</b> to the centre?</p></div>'
     '<p style="margin-top:16px">C\'est exactement le « si » français : « Savez-vous S\'IL y a une banque... ». Whether est un synonyme plus formel de if.</p>'),
    ('Les formules d\'introduction', None,
     '<p class="slide-explanation">Varie tes ouvertures selon la situation — toutes suivent la même règle d\'ordre des mots.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Can/Could you tell me</b> where the station is? (demande polie)</p>'
     '<p style="margin-top:8px"><b>Do you know</b> what time it opens? (à un inconnu)</p>'
     '<p style="margin-top:8px"><b>I\'d like to know</b> how much it costs. (au guichet)</p>'
     '<p style="margin-top:8px"><b>I wonder</b> if she is at home. (pour soi-même : je me demande si...)</p></div>'
     '<p style="margin-top:16px">Could you tell me... est encore plus poli que Can you tell me... — parfait pour l\'examen oral.</p>'),
  ],
  traps=[
    ('Can you tell me where is the station?', 'Can you tell me where <strong>the station is</strong>?', 'Pas d\'inversion dans la question indirecte : where THE STATION IS (ordre normal).'),
    ('Do you know what time does the shop open?', 'Do you know what time <strong>the shop opens</strong>?', 'Le does disparaît et le verbe reprend son -s : the shop OPENS.'),
    ('I wonder where did they go.', 'I wonder where <strong>they went</strong>.', 'Le did disparaît et le verbe passe au past simple : they WENT.'),
    ('Do you know if is there a bank?', 'Do you know if <strong>there is</strong> a bank?', 'Après if, ordre normal : if THERE IS a bank.'),
    ('Could you tell me how much costs it?', 'Could you tell me how much <strong>it costs</strong>?', 'Sujet avant verbe : how much IT COSTS.'),
  ],
  summary=[
    ('Principe', 'formule + question SANS inversion', 'Can you tell me where the station is?'),
    ('Avec be', 'where is X? → where X is', 'Do you know where the station is?'),
    ('Avec do/does', 'l\'auxiliaire disparaît, le -s revient', 'Do you know where she lives?'),
    ('Avec did', 'did disparaît, verbe au passé', 'Can you tell me when they arrived?'),
    ('Oui/non', 'if (= si)', 'Do you know if there is a bank?'),
    ('Formules', 'Can/Could you tell me · Do you know · I wonder', 'Could you tell me...? (le plus poli)'),
  ],
  ex1=('Choisis la question indirecte correcte', 'Pas d\'inversion, pas de do/does/did !', [
    ('« Where is the museum? » poliment :', ['Can you tell me where the museum is?', 'Can you tell me where is the museum?', 'Can you tell me where does the museum is?'], 'Can you tell me where the museum is?',
     'Ordre normal après where : the museum IS.'),
    ('« What time does the film start? » poliment :', ['Do you know what time the film starts?', 'Do you know what time does the film start?', 'Do you know what time the film start?'], 'Do you know what time the film starts?',
     'Does disparaît, le -s revient sur le verbe : the film STARTS.'),
    ('« Is there a pharmacy near here? » poliment :', ['Do you know if there is a pharmacy near here?', 'Do you know is there a pharmacy near here?', 'Do you know if is there a pharmacy near here?'], 'Do you know if there is a pharmacy near here?',
     'Question oui/non → IF + ordre normal : if THERE IS.'),
    ('« Where did she go? » poliment :', ['Can you tell me where she went?', 'Can you tell me where did she go?', 'Can you tell me where she did go?'], 'Can you tell me where she went?',
     'Did disparaît, verbe au passé : she WENT.'),
    ('« How much is this T-shirt? » poliment :', ['Could you tell me how much this T-shirt is?', 'Could you tell me how much is this T-shirt?', 'Could you tell me how much does this T-shirt?'], 'Could you tell me how much this T-shirt is?',
     'Ordre normal : how much THIS T-SHIRT IS.'),
    ('« Je me demande où ils habitent. »', ['I wonder where they live.', 'I wonder where do they live.', 'I wonder where they do live.'], 'I wonder where they live.',
     'I wonder + ordre normal : where THEY LIVE.'),
  ]),
  ex2=('Transforme en question indirecte', 'Écris le ou les mots qui manquent.', [
    ('Where is the station? → Can you tell me where the station ______?', 'is',
     'L\'inversion disparaît : where the station IS.'),
    ('Where does she work? → Do you know where she ______? (le -s revient !)', 'works',
     'Does disparaît → she WORKS.'),
    ('Is this seat free? → Do you know ______ this seat is free? (si)', 'if',
     'Question oui/non → IF this seat is free.'),
    ('When did the train leave? → Can you tell me when the train ______? (au passé)', 'left',
     'Did disparaît → past simple : the train LEFT.'),
    ('What time do the shops close? → I\'d like to know what time the shops ______.', 'close',
     'Do disparaît, le verbe reste à la base (they) : the shops CLOSE.'),
  ]),
  ex3=('Dans la rue, à l\'hôtel, au magasin', 'Choisis la demande polie correcte.', [
    ('Tu cherches la gare :', ['Excuse me, could you tell me where the station is?', 'Excuse me, where is station, tell me?', 'Hey! Station where?'], 'Excuse me, could you tell me where the station is?',
     'Excuse me + could you tell me + ordre normal : la politesse complète.'),
    ('Tu veux savoir si le bus va au centre :', ['Do you know if this bus goes to the centre?', 'Do you know does this bus go to the centre?', 'This bus go centre, yes?'], 'Do you know if this bus goes to the centre?',
     'IF + this bus GOES (le -s sur le verbe, sans does).'),
    ('Tu veux connaître le prix :', ['Could you tell me how much it costs?', 'Could you tell me how much does it cost?', 'How much costs it, please?'], 'Could you tell me how much it costs?',
     'Ordre normal : how much IT COSTS.'),
    ('Tu veux savoir l\'heure d\'ouverture :', ['Do you know what time the museum opens?', 'Do you know what time opens the museum?', 'What time the museum does open?'], 'Do you know what time the museum opens?',
     'Sujet avant verbe : the museum OPENS.'),
    ('Tu te demandes si elle viendra :', ['I wonder if she will come.', 'I wonder will she come.', 'I wonder if will she come.'], 'I wonder if she will come.',
     'I wonder IF + ordre normal : she will come.'),
  ]),
  game_desc='Chaque structure de question indirecte passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('can-you-tell-me', 'Can you tell me...?', 'pourriez-vous me dire... — la formule polie', 'formule', '<b>Can you tell me</b> where the station is?', 'Can you ______ me where the station is? (dire)', 'tell'),
    ('no-inversion', 'where the station is', 'ordre normal — l\'inversion disparaît', 'ordre des mots', 'Can you tell me where <b>the station is</b>?', 'Can you tell me where the station ______? (verbe à la fin)', 'is'),
    ('does-disparait', 'where she lives', 'does disparaît — le -s revient sur le verbe', 'sans does', 'Do you know where she <b>lives</b>?', 'Do you know where she ______? (habite)', 'lives'),
    ('did-disparait', 'when they arrived', 'did disparaît — le verbe passe au passé', 'sans did', 'Can you tell me when they <b>arrived</b>?', 'Can you tell me when they ______? (sont arrivés)', 'arrived'),
    ('if', 'if', 'si — pour les questions oui/non', 'oui/non', 'Do you know <b>if</b> there is a bank near here?', 'Do you know ______ there is a bank near here? (si)', 'if'),
    ('do-you-know', 'Do you know...?', 'savez-vous... — pour demander à un inconnu', 'formule', '<b>Do you know</b> what time it opens?', 'Do you ______ what time it opens? (savez)', 'know'),
    ('i-wonder', 'I wonder...', 'je me demande... — la question pour soi-même', 'se demander', '<b>I wonder</b> if she is at home.', 'I ______ if she is at home. (me demande)', 'wonder'),
    ('could-you', 'Could you tell me...?', 'pourriez-vous — encore plus poli que can', 'politesse', '<b>Could</b> you tell me how much it costs?', '______ you tell me how much it costs? (pourriez)', 'could'),
  ],
),

}
