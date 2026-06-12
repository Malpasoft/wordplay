# -*- coding: utf-8 -*-
"""fr/ A1 grammaire — lot 3 (chapitres 11-15). Explications en français, anglais cible."""

CHAPTERS = {

'adjectives-basic': dict(
  level='a1', section='grammaire', num='Ch. 11', short='Les adjectifs',
  title='Les adjectifs — position et invariabilité',
  subtitle='Pourquoi on dit « a red car » et jamais « a car red »',
  slides=[
    ('L\'adjectif se place AVANT le nom', None,
     '<p class="slide-explanation">C\'est la différence numéro un avec le français : en anglais, l\'adjectif se place presque toujours <b>avant</b> le nom qu\'il décrit. En français on dit « une voiture rouge » ; en anglais, c\'est l\'inverse.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>une voiture <b>rouge</b> → a <b>red</b> car</p>'
     '<p style="margin-top:8px">un film <b>intéressant</b> → an <b>interesting</b> film</p>'
     '<p style="margin-top:8px">une maison <b>grande</b> → a <b>big</b> house</p></div>'
     '<p style="margin-top:16px">Règle simple : <b>adjectif + nom</b>, toujours dans cet ordre. « A car red » est une faute typique de francophone.</p>'),
    ('L\'adjectif est INVARIABLE', None,
     '<p class="slide-explanation">Deuxième grande différence : l\'adjectif anglais <b>ne s\'accorde jamais</b>. Pas de féminin, pas de pluriel, pas de -e ni de -s. Une seule forme pour tout.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>a <b>small</b> dog — un petit chien</p>'
     '<p style="margin-top:8px">a <b>small</b> house — une petite maison (pas de féminin !)</p>'
     '<p style="margin-top:8px">two <b>small</b> dogs — deux petits chiens (pas de pluriel !)</p></div>'
     '<p style="margin-top:16px">« The houses are bigs » n\'existe pas. L\'adjectif reste <b>big</b>, même avec un nom pluriel.</p>'),
    ('L\'adjectif après to be', None,
     '<p class="slide-explanation">L\'adjectif peut aussi se placer <b>après le verbe to be</b> (ou après look, seem, feel...). Dans ce cas, il décrit le sujet de la phrase.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>The film is <b>interesting</b>. — Le film est intéressant.</p>'
     '<p style="margin-top:8px">My sisters are <b>tall</b>. — Mes sœurs sont grandes. (pas de -s ni de -es !)</p>'
     '<p style="margin-top:8px">You look <b>tired</b>. — Tu as l\'air fatigué.</p></div>'
     '<p style="margin-top:16px">Même après to be, l\'adjectif reste invariable : <b>they are happy</b>, jamais « happys ».</p>'),
    ('Plusieurs adjectifs ensemble', None,
     '<p class="slide-explanation">Quand on utilise plusieurs adjectifs, ils se placent tous avant le nom, dans un ordre naturel : <b>opinion → taille → âge → couleur</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>a <b>beautiful old</b> house — une belle vieille maison</p>'
     '<p style="margin-top:8px">a <b>big black</b> dog — un gros chien noir</p>'
     '<p style="margin-top:8px">a <b>nice little red</b> car — une jolie petite voiture rouge</p></div>'
     '<p style="margin-top:16px">À ton niveau, retiens surtout : l\'opinion (nice, beautiful) vient en premier, la couleur en dernier, juste avant le nom.</p>'),
    ('Les adjectifs courants à connaître', None,
     '<p class="slide-explanation">Voici les paires d\'adjectifs les plus utiles au niveau A1. Apprends-les par contraires, c\'est plus facile à mémoriser.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>big</b> (grand) ↔ <b>small</b> (petit) &nbsp;·&nbsp; <b>old</b> (vieux) ↔ <b>new</b> (nouveau) / <b>young</b> (jeune)</p>'
     '<p style="margin-top:8px"><b>good</b> (bon) ↔ <b>bad</b> (mauvais) &nbsp;·&nbsp; <b>hot</b> (chaud) ↔ <b>cold</b> (froid)</p>'
     '<p style="margin-top:8px"><b>easy</b> (facile) ↔ <b>difficult</b> (difficile) &nbsp;·&nbsp; <b>happy</b> (content) ↔ <b>sad</b> (triste)</p></div>'
     '<p style="margin-top:16px">Faux ami : <b>large</b> signifie « grand, vaste » — pas « large » (qui se dit <b>wide</b>).</p>'),
  ],
  traps=[
    ('I have a car red.', 'I have a <strong>red car</strong>.', 'L\'adjectif se place AVANT le nom en anglais : red car, et non « car red » comme en français (« voiture rouge »).'),
    ('The houses are bigs.', 'The houses are <strong>big</strong>.', 'L\'adjectif anglais est invariable : jamais de -s au pluriel. Big reste big, même avec un sujet pluriel.'),
    ('She is a girl very beautiful.', 'She is a very <strong>beautiful girl</strong>.', 'L\'adjectif (et son adverbe very) se placent avant le nom : a very beautiful girl.'),
    ('My sister is tall and brune.', 'My sister is tall and <strong>dark-haired</strong>.', 'Pas de mélange français-anglais ! « Brune » se dit dark-haired (cheveux) ; il n\'y a pas de forme féminine.'),
    ('It is a large river? No, a wide one.', 'It is a <strong>wide</strong> river.', 'Faux ami : large = grand/vaste en anglais. Pour « large » (largeur), on dit wide.'),
  ],
  summary=[
    ('Position', 'adjectif + nom', 'a red car / an old house'),
    ('Invariable', 'une seule forme', 'small dog / small house / small dogs'),
    ('Après to be', 'sujet + be + adjectif', 'The film is interesting.'),
    ('Plusieurs adjectifs', 'opinion → taille → âge → couleur', 'a beautiful old house'),
    ('Avec very', 'very + adjectif', 'She is very tall.'),
    ('Faux ami', 'large = grand (pas « large »)', 'a large garden = un grand jardin'),
  ],
  ex1=('Choisis la phrase correcte', 'Attention à la position et à l\'invariabilité de l\'adjectif.', [
    ('Comment dit-on « une voiture rouge » ?', ['a red car', 'a car red', 'a red cars'], 'a red car',
     'Adjectif AVANT le nom : a RED car. « A car red » est un calque du français.'),
    ('They live in a ______ house.', ['beautiful', 'beautifuls', 'beautifully'], 'beautiful',
     'L\'adjectif est invariable : beautiful, sans -s. Beautifully est un adverbe.'),
    ('My brothers are very ______.', ['tall', 'talls', 'tall ones'], 'tall',
     'Après to be, l\'adjectif reste invariable : they are TALL, jamais « talls ».'),
    ('She has two ______ cats.', ['black', 'blacks', 'black ones'], 'black',
     'Two black cats : l\'adjectif ne prend jamais de -s, même avec un nom pluriel.'),
    ('It\'s a ______ day today!', ['beautiful', 'day beautiful', 'beautifuls'], 'beautiful',
     'A beautiful day : adjectif avant le nom, invariable.'),
    ('Comment dit-on « un grand jardin » ?', ['a large garden', 'a wide garden', 'a garden large'], 'a large garden',
     'Large = grand, vaste. C\'est un faux ami : il ne signifie pas « large » (= wide).'),
  ]),
  ex2=('Remets l\'adjectif à la bonne place', 'Écris le groupe nominal correct (article + adjectif + nom).', [
    ('« un film intéressant » → ______ (an / interesting / film)', 'an interesting film',
     'Adjectif avant le nom : an INTERESTING film. L\'article devient « an » devant une voyelle.'),
    ('« des chiens petits » → ______ (small / dogs)', 'small dogs',
     'Small dogs : adjectif invariable avant le nom, pas de -s sur small.'),
    ('« une vieille maison » → ______ (an / old / house)', 'an old house',
     'An old house : adjectif avant le nom ; « an » devant la voyelle de old.'),
    ('« un gros chien noir » → ______ (a / big / black / dog)', 'a big black dog',
     'Taille avant couleur : a BIG BLACK dog.'),
    ('« une belle vieille maison » → ______ (a / beautiful / old / house)', 'a beautiful old house',
     'Opinion avant âge : a BEAUTIFUL OLD house.'),
  ]),
  ex3=('Trouve l\'erreur', 'Choisis la version correcte de chaque phrase.', [
    ('« My parents have a house big. »', ['My parents have a big house.', 'My parents have a house very big.', 'My parents have bigs house.'], 'My parents have a big house.',
     'A big house : l\'adjectif se place avant le nom.'),
    ('« The questions are easies. »', ['The questions are easy.', 'The questions are easys.', 'The questions is easy.'], 'The questions are easy.',
     'Easy est invariable : the questions are EASY. Jamais de pluriel sur l\'adjectif.'),
    ('« She has hairs blonds. »', ['She has blond hair.', 'She has blonds hair.', 'She has hair blond.'], 'She has blond hair.',
     'Blond hair : adjectif avant le nom. Hair est indénombrable (pas de -s) et blond invariable.'),
    ('« It is a very film good. »', ['It is a very good film.', 'It is a film very good.', 'It is very a good film.'], 'It is a very good film.',
     'Very + adjectif + nom : a very good film.'),
    ('« They are happys together. »', ['They are happy together.', 'They are happies together.', 'They is happy together.'], 'They are happy together.',
     'Happy reste invariable après to be : they are HAPPY.'),
  ]),
  game_desc='Chaque règle des adjectifs passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('red-car', 'a red car', 'adjectif AVANT le nom — l\'ordre inverse du français', 'adjectif + nom', 'She drives <b>a red car</b>.', 'She drives a ______ car. (rouge)', 'red'),
    ('invariable', 'small dogs', 'adjectif invariable — jamais de -s au pluriel', 'pas d\'accord', 'I have two <b>small</b> dogs.', 'I have two ______ dogs. (petits)', 'small'),
    ('after-be', 'The film is interesting', 'adjectif après to be — décrit le sujet', 'be + adjectif', 'The film <b>is interesting</b>.', 'The film is ______. (intéressant)', 'interesting'),
    ('very-tall', 'very tall', 'very + adjectif — pour intensifier', 'très', 'My brother is <b>very tall</b>.', 'My brother is very ______. (grand)', 'tall'),
    ('big-black', 'a big black dog', 'taille avant couleur — ordre des adjectifs', 'ordre', 'They have <b>a big black dog</b>.', 'They have a big ______ dog. (noir)', 'black'),
    ('old-house', 'an old house', 'an + adjectif à voyelle — article adapté à l\'adjectif', 'an + voyelle', 'We live in <b>an old house</b>.', 'We live in ______ old house. (article)', 'an'),
    ('large-faux-ami', 'large = grand', 'faux ami — large signifie grand, pas « large »', 'vaste', 'They have a <b>large</b> garden.', 'They have a ______ garden. (grand)', 'large'),
    ('happy-plural', 'they are happy', 'invariable après be — même au pluriel', 'pas de pluriel', 'The children <b>are happy</b>.', 'The children are ______. (contents)', 'happy'),
  ],
),

'adverbs-frequency': dict(
  level='a1', section='grammaire', num='Ch. 12', short='Adverbes de fréquence',
  title='Les adverbes de fréquence — always, often, never',
  subtitle='Dire à quelle fréquence on fait les choses, et où placer l\'adverbe',
  slides=[
    ('L\'échelle de fréquence', None,
     '<p class="slide-explanation">Les adverbes de fréquence indiquent <b>à quelle fréquence</b> une action se produit. Mémorise-les comme une échelle, de 100 % à 0 %.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>always</b> (toujours, 100%) &nbsp;·&nbsp; <b>usually</b> (d\'habitude, 90%)</p>'
     '<p style="margin-top:8px"><b>often</b> (souvent, 70%) &nbsp;·&nbsp; <b>sometimes</b> (parfois, 50%)</p>'
     '<p style="margin-top:8px"><b>rarely</b> (rarement, 10%) &nbsp;·&nbsp; <b>never</b> (jamais, 0%)</p></div>'
     '<p style="margin-top:16px">Ces adverbes s\'utilisent surtout avec le <b>present simple</b>, pour parler d\'habitudes.</p>'),
    ('Position : AVANT le verbe principal', None,
     '<p class="slide-explanation">La règle d\'or : l\'adverbe de fréquence se place <b>avant le verbe principal</b>. En français, il se place après (« je mange souvent ») — en anglais, c\'est l\'inverse !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>often</b> eat pasta. — Je mange souvent des pâtes.</p>'
     '<p style="margin-top:8px">She <b>always</b> gets up at 7. — Elle se lève toujours à 7 h.</p>'
     '<p style="margin-top:8px">They <b>never</b> watch TV. — Ils ne regardent jamais la télé.</p></div>'
     '<p style="margin-top:16px">« I eat often pasta » est une faute typique de francophone. L\'adverbe vient AVANT eat.</p>'),
    ('Position : APRÈS to be', None,
     '<p class="slide-explanation">Exception importante : avec le verbe <b>to be</b>, l\'adverbe de fréquence se place <b>après</b> le verbe, pas avant.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>He <b>is always</b> late. — Il est toujours en retard.</p>'
     '<p style="margin-top:8px">I <b>am never</b> tired in the morning. — Je ne suis jamais fatigué le matin.</p>'
     '<p style="margin-top:8px">They <b>are usually</b> at home on Sundays. — Ils sont d\'habitude chez eux le dimanche.</p></div>'
     '<p style="margin-top:16px">Retiens : <b>avant</b> les verbes ordinaires, <b>après</b> to be.</p>'),
    ('Never : jamais de double négation', None,
     '<p class="slide-explanation">En français, « jamais » s\'accompagne de « ne ». En anglais, <b>never est déjà négatif</b> : le verbe reste à la forme affirmative. Pas de don\'t avec never !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Je ne bois jamais de café. → I <b>never drink</b> coffee.</p>'
     '<p style="margin-top:8px">Il ne pleut jamais ici. → It <b>never rains</b> here.</p>'
     '<p style="margin-top:8px;color:var(--muted)">(et non « I don\'t never drink coffee »)</p></div>'
     '<p style="margin-top:16px">Une seule négation par phrase en anglais : never suffit, le « do not » disparaît.</p>'),
    ('Poser la question : How often...?', None,
     '<p class="slide-explanation">Pour demander la fréquence, on utilise <b>How often...?</b> (« à quelle fréquence, tous les combien »). On peut répondre avec un adverbe ou une expression.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>How often</b> do you play football? — Tu joues au foot tous les combien ?</p>'
     '<p style="margin-top:8px">I play <b>twice a week</b>. — J\'y joue deux fois par semaine.</p>'
     '<p style="margin-top:8px"><b>Sometimes.</b> / <b>Every day.</b> — Parfois. / Tous les jours.</p></div>'
     '<p style="margin-top:16px">Expressions utiles : <b>once a week</b> (une fois par semaine), <b>twice a month</b> (deux fois par mois), <b>every day</b> (tous les jours).</p>'),
  ],
  traps=[
    ('I eat often pasta.', 'I <strong>often eat</strong> pasta.', 'L\'adverbe de fréquence se place AVANT le verbe principal : I often eat. En français il vient après le verbe, d\'où l\'erreur.'),
    ('He always is late.', 'He <strong>is always</strong> late.', 'Avec to be, l\'adverbe vient APRÈS le verbe : he is always late.'),
    ('I don\'t drink never coffee.', 'I <strong>never drink</strong> coffee.', 'Never est déjà négatif : pas de double négation. Le verbe reste affirmatif : I never drink.'),
    ('She watches sometimes TV.', 'She <strong>sometimes watches</strong> TV.', 'L\'adverbe se place avant le verbe : she sometimes watches TV (sometimes peut aussi commencer la phrase).'),
    ('How many do you play tennis?', '<strong>How often</strong> do you play tennis?', 'Pour la fréquence, c\'est How often...? — How many sert à compter des objets.'),
  ],
  summary=[
    ('Échelle', 'always → usually → often → sometimes → rarely → never', '100% → 0%'),
    ('Verbe ordinaire', 'sujet + adverbe + verbe', 'I often eat pasta.'),
    ('Avec to be', 'sujet + be + adverbe', 'He is always late.'),
    ('Never', 'never + verbe affirmatif', 'I never drink coffee.'),
    ('Question', 'How often + do/does + sujet + verbe?', 'How often do you play?'),
    ('Expressions', 'once/twice a week · every day', 'I play twice a week.'),
  ],
  ex1=('Place l\'adverbe correctement', 'Choisis la phrase où l\'adverbe est à la bonne place.', [
    ('« Je bois souvent du thé. »', ['I often drink tea.', 'I drink often tea.', 'Often I drink tea always.'], 'I often drink tea.',
     'Adverbe AVANT le verbe principal : I OFTEN drink tea.'),
    ('« Il est toujours content. »', ['He is always happy.', 'He always is happy.', 'Always he is happy.'], 'He is always happy.',
     'Avec to be, l\'adverbe vient APRÈS : he is ALWAYS happy.'),
    ('« Nous ne regardons jamais la télé. »', ['We never watch TV.', 'We don\'t never watch TV.', 'We watch never TV.'], 'We never watch TV.',
     'Never + verbe affirmatif : pas de double négation en anglais.'),
    ('« Elle se lève d\'habitude à 7 h. »', ['She usually gets up at 7.', 'She gets usually up at 7.', 'Usually she gets up always at 7.'], 'She usually gets up at 7.',
     'Adverbe avant le verbe : she USUALLY gets up.'),
    ('« Ils sont rarement en retard. »', ['They are rarely late.', 'They rarely are late.', 'They are late rarely.'], 'They are rarely late.',
     'Avec to be : they are RARELY late.'),
    ('« Tu joues au tennis tous les combien ? »', ['How often do you play tennis?', 'How many do you play tennis?', 'How much you play tennis?'], 'How often do you play tennis?',
     'La fréquence se demande avec How often + do + sujet + verbe.'),
  ]),
  ex2=('Traduis avec le bon adverbe', 'Écris l\'adverbe de fréquence qui correspond.', [
    ('« toujours » (100%) → I ______ have breakfast at 8.', 'always',
     'Always = toujours, fréquence maximale. I ALWAYS have breakfast.'),
    ('« jamais » (0%) → She ______ eats meat.', 'never',
     'Never = jamais. Le verbe reste affirmatif : she never EATS (pas de doesn\'t).'),
    ('« parfois » (50%) → We ______ go to the cinema.', 'sometimes',
     'Sometimes = parfois, environ la moitié du temps.'),
    ('« souvent » (70%) → They ______ play video games.', 'often',
     'Often = souvent. Position : avant le verbe play.'),
    ('« d\'habitude » (90%) → He ______ walks to school.', 'usually',
     'Usually = d\'habitude, presque toujours.'),
  ]),
  ex3=('Corrige les fautes de francophone', 'Choisis la version correcte.', [
    ('« I go sometimes to the pool. »', ['I sometimes go to the pool.', 'I go to the pool sometimes never.', 'Sometimes I go never to the pool.'], 'I sometimes go to the pool.',
     'L\'adverbe se place avant le verbe : I SOMETIMES go.'),
    ('« She is late never. »', ['She is never late.', 'She never is late.', 'Never she is late.'], 'She is never late.',
     'Avec to be, l\'adverbe vient juste après : she is NEVER late.'),
    ('« They don\'t go never to bed early. »', ['They never go to bed early.', 'They don\'t never go to bed early.', 'They go never to bed early.'], 'They never go to bed early.',
     'Never remplace la négation : they NEVER go (sans don\'t).'),
    ('« Often he is tired. » (phrase maladroite)', ['He is often tired.', 'He often is tired.', 'He is tired often always.'], 'He is often tired.',
     'La place naturelle avec to be : he is OFTEN tired.'),
    ('« How much often do you swim? »', ['How often do you swim?', 'How much do you swim often?', 'How many often you swim?'], 'How often do you swim?',
     'How often suffit pour demander la fréquence — sans much ni many.'),
  ]),
  game_desc='Chaque adverbe de fréquence passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('always', 'always', 'toujours — fréquence 100 %', '100%', 'I <b>always</b> have breakfast at 8.', 'I ______ have breakfast at 8. (toujours)', 'always'),
    ('usually', 'usually', 'd\'habitude — fréquence environ 90 %', 'normalement', 'He <b>usually</b> walks to school.', 'He ______ walks to school. (d\'habitude)', 'usually'),
    ('often', 'often', 'souvent — fréquence environ 70 %', 'fréquemment', 'They <b>often</b> play video games.', 'They ______ play video games. (souvent)', 'often'),
    ('sometimes', 'sometimes', 'parfois — fréquence environ 50 %', 'de temps en temps', 'We <b>sometimes</b> go to the cinema.', 'We ______ go to the cinema. (parfois)', 'sometimes'),
    ('never', 'never', 'jamais — déjà négatif, verbe affirmatif', '0%', 'She <b>never</b> eats meat.', 'She ______ eats meat. (jamais)', 'never'),
    ('after-be', 'is always', 'après to be — l\'adverbe suit le verbe être', 'be + adverbe', 'He <b>is always</b> late.', 'He is ______ late. (toujours)', 'always'),
    ('how-often', 'How often...?', 'à quelle fréquence ? — la question de fréquence', 'tous les combien', '<b>How often</b> do you play tennis?', 'How ______ do you play tennis? (à quelle fréquence)', 'often'),
    ('twice-a-week', 'twice a week', 'deux fois par semaine — expression de fréquence', '2x / semaine', 'I swim <b>twice a week</b>.', 'I swim ______ a week. (deux fois)', 'twice'),
  ],
),

'prepositions-of-place': dict(
  level='a1', section='grammaire', num='Ch. 13', short='Prépositions de lieu',
  title='Les prépositions de lieu — in, on, under, next to',
  subtitle='Dire où se trouvent les choses : la position dans l\'espace',
  slides=[
    ('In, on, under : les trois de base', None,
     '<p class="slide-explanation">Pour dire où se trouve un objet, l\'anglais utilise des prépositions de lieu. Commençons par les trois plus fréquentes.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>in</b> = dans — The keys are <b>in</b> the bag. (dans le sac)</p>'
     '<p style="margin-top:8px"><b>on</b> = sur — The book is <b>on</b> the table. (sur la table)</p>'
     '<p style="margin-top:8px"><b>under</b> = sous — The cat is <b>under</b> the bed. (sous le lit)</p></div>'
     '<p style="margin-top:16px">Ces trois-là correspondent bien au français : dans / sur / sous. Les pièges arrivent avec les suivantes !</p>'),
    ('Next to, behind, in front of, between', None,
     '<p class="slide-explanation">Quatre prépositions pour situer par rapport à d\'autres objets. Attention : <b>in front of</b> s\'écrit en trois mots.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>next to</b> = à côté de — The school is <b>next to</b> the park.</p>'
     '<p style="margin-top:8px"><b>behind</b> = derrière — The garden is <b>behind</b> the house.</p>'
     '<p style="margin-top:8px"><b>in front of</b> = devant — The car is <b>in front of</b> the door.</p>'
     '<p style="margin-top:8px"><b>between</b> = entre — The bank is <b>between</b> the shop and the café.</p></div>'
     '<p style="margin-top:16px">Piège : « devant » = <b>in front of</b> — ne traduis pas par « in face of », qui n\'existe pas.</p>'),
    ('Le piège in / on / at', None,
     '<p class="slide-explanation">Certains emplois ne correspondent pas au français. C\'est là que les francophones font le plus d\'erreurs — apprends ces cas par cœur.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>in</b> the picture (SUR la photo !) &nbsp;·&nbsp; <b>in</b> the street (dans la rue)</p>'
     '<p style="margin-top:8px"><b>on</b> the wall (au mur) &nbsp;·&nbsp; <b>on</b> the bus (dans le bus !)</p>'
     '<p style="margin-top:8px"><b>at</b> the door (à la porte) &nbsp;·&nbsp; <b>at</b> the top (en haut)</p></div>'
     '<p style="margin-top:16px">Le plus surprenant : on dit <b>in the picture</b> (et non « on the picture ») et <b>on the bus</b> (et non « in the bus »).</p>'),
    ('Où est... ? Where is...?', None,
     '<p class="slide-explanation">Pour demander où se trouve quelque chose, on utilise <b>Where is...?</b> (singulier) ou <b>Where are...?</b> (pluriel). La réponse utilise une préposition de lieu.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Where is</b> my phone? — It\'s <b>on</b> the sofa.</p>'
     '<p style="margin-top:8px"><b>Where are</b> my keys? — They\'re <b>in</b> your pocket.</p>'
     '<p style="margin-top:8px"><b>Where is</b> the station? — It\'s <b>next to</b> the supermarket.</p></div>'
     '<p style="margin-top:16px">N\'oublie pas l\'accord : Where IS (singulier) / Where ARE (pluriel) — comme « où est / où sont ».</p>'),
    ('Décrire une pièce', None,
     '<p class="slide-explanation">Avec les prépositions de lieu et <b>there is / there are</b> (chapitre suivant), tu peux décrire n\'importe quelle pièce ou image. C\'est une question classique d\'examen A1.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>The sofa is <b>next to</b> the window. — Le canapé est à côté de la fenêtre.</p>'
     '<p style="margin-top:8px">There is a lamp <b>on</b> the desk. — Il y a une lampe sur le bureau.</p>'
     '<p style="margin-top:8px">The shoes are <b>under</b> the chair. — Les chaussures sont sous la chaise.</p></div>'
     '<p style="margin-top:16px">Astuce examen : commence par les grands meubles, puis situe les petits objets par rapport à eux.</p>'),
  ],
  traps=[
    ('The photo is on the picture.', 'She is <strong>in</strong> the picture.', 'En anglais, on est IN the picture (dans la photo) — jamais « on the picture », même si le français dit « sur la photo ».'),
    ('I am in the bus.', 'I am <strong>on</strong> the bus.', 'Pour les transports publics (bus, train, plane), l\'anglais utilise ON : on the bus, on the train.'),
    ('The car is in face of the house.', 'The car is <strong>in front of</strong> the house.', '« Devant » = in front of (trois mots). « In face of » n\'existe pas en anglais.'),
    ('The poster is in the wall.', 'The poster is <strong>on</strong> the wall.', 'Une affiche est ON the wall (en contact avec la surface) — pas « in » (à l\'intérieur).'),
    ('Where is my keys?', 'Where <strong>are</strong> my keys?', 'Keys est pluriel : Where ARE my keys? — l\'accord du verbe est obligatoire.'),
  ],
  summary=[
    ('Base', 'in = dans · on = sur · under = sous', 'in the bag / on the table / under the bed'),
    ('Voisinage', 'next to = à côté de · between = entre', 'next to the park / between A and B'),
    ('Avant/arrière', 'in front of = devant · behind = derrière', 'in front of the door / behind the house'),
    ('Pièges', 'in the picture · on the bus · on the wall', 'She is in the picture.'),
    ('Question', 'Where is/are + nom?', 'Where are my keys?'),
    ('Réponse', 'It\'s/They\'re + préposition + lieu', 'They\'re in your pocket.'),
  ],
  ex1=('Choisis la bonne préposition', 'In, on, under, next to, behind, in front of ou between ?', [
    ('The book is ______ the table. (sur)', ['on', 'in', 'under'], 'on',
     'Sur la table = ON the table : contact avec la surface.'),
    ('The keys are ______ the bag. (dans)', ['in', 'on', 'at'], 'in',
     'Dans le sac = IN the bag : à l\'intérieur.'),
    ('The cat is ______ the bed. (sous)', ['under', 'on', 'behind'], 'under',
     'Sous le lit = UNDER the bed.'),
    ('The bank is ______ the shop and the café. (entre)', ['between', 'next to', 'behind'], 'between',
     'Entre deux choses = BETWEEN... and...'),
    ('The garden is ______ the house. (derrière)', ['behind', 'in front of', 'under'], 'behind',
     'Derrière = BEHIND. Devant = in front of.'),
    ('The bus stop is ______ the school. (devant)', ['in front of', 'in face of', 'on front of'], 'in front of',
     'Devant = IN FRONT OF (trois mots). « In face of » n\'existe pas.'),
  ]),
  ex2=('Traduis la préposition', 'Écris la préposition anglaise qui manque.', [
    ('« Elle est sur la photo. » → She is ______ the picture.', 'in',
     'Piège classique : IN the picture, même si le français dit « sur » la photo.'),
    ('« Je suis dans le bus. » → I am ______ the bus.', 'on',
     'Transports publics : ON the bus, on the train, on the plane.'),
    ('« L\'affiche est au mur. » → The poster is ______ the wall.', 'on',
     'En contact avec une surface verticale : ON the wall.'),
    ('« Le chien est à côté de la porte. » → The dog is ______ the door. (deux mots)', 'next to',
     'À côté de = NEXT TO (deux mots).'),
    ('« Mes chaussures sont sous la chaise. » → My shoes are ______ the chair.', 'under',
     'Sous = UNDER.'),
  ]),
  ex3=('Où est-ce ? Questions et réponses', 'Choisis la phrase correcte.', [
    ('Comment demander « Où sont mes clés ? »', ['Where are my keys?', 'Where is my keys?', 'Where my keys are?'], 'Where are my keys?',
     'Keys est pluriel → Where ARE. Et l\'ordre est Where + are + sujet.'),
    ('« Le téléphone est sur le canapé. »', ['The phone is on the sofa.', 'The phone is in the sofa.', 'The phone is at the sofa.'], 'The phone is on the sofa.',
     'Sur le canapé (surface) = ON the sofa.'),
    ('« Il y a une lampe sur le bureau. »', ['There is a lamp on the desk.', 'There is a lamp in the desk.', 'It has a lamp on the desk.'], 'There is a lamp on the desk.',
     'Sur le bureau = ON the desk. Et « il y a » = there is.'),
    ('« La gare est à côté du supermarché. »', ['The station is next to the supermarket.', 'The station is next the supermarket.', 'The station is at side of the supermarket.'], 'The station is next to the supermarket.',
     'Next TO : ne pas oublier le « to ».'),
    ('« Elle est sur la photo de classe. »', ['She is in the class photo.', 'She is on the class photo.', 'She is at the class photo.'], 'She is in the class photo.',
     'IN the photo : l\'anglais considère qu\'on est « dans » l\'image.'),
  ]),
  game_desc='Chaque préposition de lieu passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('in', 'in', 'dans — à l\'intérieur de quelque chose', 'dans', 'The keys are <b>in</b> the bag.', 'The keys are ______ the bag. (dans)', 'in'),
    ('on', 'on', 'sur — en contact avec une surface', 'sur', 'The book is <b>on</b> the table.', 'The book is ______ the table. (sur)', 'on'),
    ('under', 'under', 'sous — en dessous de quelque chose', 'sous', 'The cat is <b>under</b> the bed.', 'The cat is ______ the bed. (sous)', 'under'),
    ('next-to', 'next to', 'à côté de — juste à proximité', 'à côté', 'The school is <b>next to</b> the park.', 'The school is ______ to the park. (à côté)', 'next'),
    ('behind', 'behind', 'derrière — à l\'arrière de', 'derrière', 'The garden is <b>behind</b> the house.', 'The garden is ______ the house. (derrière)', 'behind'),
    ('in-front-of', 'in front of', 'devant — à l\'avant de (trois mots)', 'devant', 'The car is <b>in front of</b> the door.', 'The car is in ______ of the door. (devant)', 'front'),
    ('between', 'between', 'entre — au milieu de deux choses', 'entre', 'The bank is <b>between</b> the shop and the café.', 'The bank is ______ the shop and the café. (entre)', 'between'),
    ('on-the-bus', 'on the bus', 'dans le bus — ON pour les transports publics', 'transports', 'I am <b>on the bus</b>.', 'I am ______ the bus. (dans le bus)', 'on'),
  ],
),

'there-is-there-are': dict(
  level='a1', section='grammaire', num='Ch. 14', short='There is / There are',
  title='There is / There are — il y a',
  subtitle='Le « il y a » anglais change selon le singulier et le pluriel',
  slides=[
    ('Il y a : deux formes en anglais', None,
     '<p class="slide-explanation">En français, « il y a » est invariable. En anglais, il faut choisir : <b>there is</b> + singulier, <b>there are</b> + pluriel. C\'est LE point à maîtriser dans ce chapitre.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>There is</b> a book on the table. — Il y a un livre sur la table.</p>'
     '<p style="margin-top:8px"><b>There are</b> two books on the table. — Il y a deux livres sur la table.</p></div>'
     '<p style="margin-top:16px">Surtout, ne traduis jamais « il y a » par « it has » ou « it is » — c\'est toujours <b>there is/are</b>.</p>'),
    ('There is + singulier', None,
     '<p class="slide-explanation"><b>There is</b> (contraction : <b>there\'s</b>) s\'utilise avec un nom singulier ou un indénombrable.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>There is</b> a cat in the garden. — Il y a un chat dans le jardin.</p>'
     '<p style="margin-top:8px"><b>There\'s</b> a problem. — Il y a un problème.</p>'
     '<p style="margin-top:8px"><b>There is</b> some milk in the fridge. — Il y a du lait dans le frigo.</p></div>'
     '<p style="margin-top:16px">Avec les indénombrables (milk, water, money), on utilise toujours <b>there is</b>, même si la quantité semble grande.</p>'),
    ('There are + pluriel', None,
     '<p class="slide-explanation"><b>There are</b> s\'utilise avec un nom pluriel. C\'est ici que les francophones oublient le changement, puisque « il y a » ne change pas en français.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>There are</b> three chairs in the room. — Il y a trois chaises dans la pièce.</p>'
     '<p style="margin-top:8px"><b>There are</b> some apples in the kitchen. — Il y a des pommes dans la cuisine.</p>'
     '<p style="margin-top:8px"><b>There are</b> a lot of people here. — Il y a beaucoup de monde ici.</p></div>'
     '<p style="margin-top:16px">Réflexe à prendre : compte le nom qui suit. Un seul → there is. Plusieurs → there are.</p>'),
    ('Négation : there isn\'t / there aren\'t', None,
     '<p class="slide-explanation">Pour dire « il n\'y a pas », on ajoute <b>not</b> : there is not (there isn\'t) / there are not (there aren\'t). Au négatif, on utilise souvent <b>any</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>There isn\'t</b> a swimming pool. — Il n\'y a pas de piscine.</p>'
     '<p style="margin-top:8px"><b>There aren\'t any</b> shops near here. — Il n\'y a pas de magasins près d\'ici.</p>'
     '<p style="margin-top:8px"><b>There isn\'t any</b> milk left. — Il ne reste plus de lait.</p></div>'
     '<p style="margin-top:16px">« Pas de » + pluriel → there aren\'t ANY + pluriel. Le any remplace le « de » français.</p>'),
    ('Question : Is there...? / Are there...?', None,
     '<p class="slide-explanation">Pour demander « Y a-t-il...? », on inverse : <b>Is there...?</b> / <b>Are there...?</b> Les réponses courtes reprennent there.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Is there</b> a bank near here? — <b>Yes, there is.</b> / <b>No, there isn\'t.</b></p>'
     '<p style="margin-top:8px"><b>Are there</b> any restaurants? — <b>Yes, there are.</b> / <b>No, there aren\'t.</b></p></div>'
     '<p style="margin-top:16px">Dans les questions au pluriel, on utilise aussi <b>any</b> : Are there ANY restaurants?</p>'),
  ],
  traps=[
    ('It has a book on the table.', '<strong>There is</strong> a book on the table.', '« Il y a » ne se traduit JAMAIS par « it has ». La structure anglaise est there is / there are.'),
    ('There is three chairs.', '<strong>There are</strong> three chairs.', 'Three chairs est pluriel → there ARE. En français « il y a » est invariable, pas en anglais !'),
    ('There are a problem.', '<strong>There is</strong> a problem.', 'A problem est singulier → there IS a problem.'),
    ('There aren\'t shops near here.', 'There aren\'t <strong>any</strong> shops near here.', 'Au négatif pluriel, on ajoute any : there aren\'t ANY shops (= pas de magasins).'),
    ('Has there a bank near here?', '<strong>Is there</strong> a bank near here?', 'La question se forme par inversion de there is → Is there...? Jamais avec « has ».'),
  ],
  summary=[
    ('Singulier', 'There is + nom singulier', 'There is a cat in the garden.'),
    ('Pluriel', 'There are + nom pluriel', 'There are three chairs.'),
    ('Indénombrable', 'There is + some + indénombrable', 'There is some milk.'),
    ('Négation', 'There isn\'t a... / There aren\'t any...', 'There aren\'t any shops.'),
    ('Question', 'Is there...? / Are there any...?', 'Is there a bank near here?'),
    ('Réponse courte', 'Yes, there is/are. · No, there isn\'t/aren\'t.', 'Yes, there is.'),
  ],
  ex1=('There is ou there are ?', 'Regarde bien si le nom qui suit est singulier ou pluriel.', [
    ('______ a supermarket in my street.', ['There is', 'There are', 'It has'], 'There is',
     'A supermarket = singulier → THERE IS.'),
    ('______ two windows in my bedroom.', ['There are', 'There is', 'It has'], 'There are',
     'Two windows = pluriel → THERE ARE.'),
    ('______ some water in the bottle.', ['There is', 'There are', 'They are'], 'There is',
     'Water est indénombrable → THERE IS some water.'),
    ('______ a lot of students in the class.', ['There are', 'There is', 'It is'], 'There are',
     'A lot of students = pluriel → THERE ARE.'),
    ('______ any good films on TV tonight?', ['Are there', 'Is there', 'Have there'], 'Are there',
     'Films = pluriel, question → ARE THERE any...?'),
    ('______ a problem with my computer.', ['There is', 'There are', 'It has'], 'There is',
     'A problem = singulier → THERE IS a problem. Jamais « it has ».'),
  ]),
  ex2=('Traduis « il y a »', 'Écris there is, there are, there isn\'t ou there aren\'t.', [
    ('« Il y a un chat dans le jardin. » → ______ a cat in the garden.', 'There is',
     'Un chat = singulier → THERE IS a cat.'),
    ('« Il y a des pommes dans la cuisine. » → ______ some apples in the kitchen.', 'There are',
     'Des pommes = pluriel → THERE ARE some apples.'),
    ('« Il n\'y a pas de piscine. » → ______ a swimming pool.', 'There isn\'t',
     'Négation singulier → THERE ISN\'T a swimming pool.'),
    ('« Il n\'y a pas de magasins. » → ______ any shops.', 'There aren\'t',
     'Négation pluriel → THERE AREN\'T any shops.'),
    ('« Il y a du lait dans le frigo. » → ______ some milk in the fridge.', 'There is',
     'Milk est indénombrable → THERE IS some milk.'),
  ]),
  ex3=('Questions et réponses courtes', 'Choisis la forme correcte.', [
    ('« Y a-t-il une banque près d\'ici ? »', ['Is there a bank near here?', 'Has there a bank near here?', 'There is a bank near here?'], 'Is there a bank near here?',
     'Question = inversion : IS THERE a bank...?'),
    ('« Y a-t-il des restaurants ? »', ['Are there any restaurants?', 'Is there any restaurants?', 'Are there a restaurants?'], 'Are there any restaurants?',
     'Pluriel → ARE THERE ANY restaurants?'),
    ('Réponse affirmative à « Is there a pool? »', ['Yes, there is.', 'Yes, it is.', 'Yes, there\'s.'], 'Yes, there is.',
     'Réponse courte : Yes, THERE IS (jamais contracté à l\'affirmatif).'),
    ('Réponse négative à « Are there any shops? »', ['No, there aren\'t.', 'No, there isn\'t.', 'No, they aren\'t.'], 'No, there aren\'t.',
     'Pluriel → No, there AREN\'T.'),
    ('Comment dire « Il y a beaucoup de monde » ?', ['There are a lot of people.', 'There is a lot of people.', 'It has a lot of people.'], 'There are a lot of people.',
     'People est pluriel en anglais → THERE ARE a lot of people.'),
  ]),
  game_desc='Chaque forme de there is / there are passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('there-is', 'there is', 'il y a + singulier — un seul objet ou personne', 'there\'s', '<b>There is</b> a cat in the garden.', 'There ______ a cat in the garden. (il y a)', 'is'),
    ('there-are', 'there are', 'il y a + pluriel — plusieurs objets ou personnes', 'pluriel', '<b>There are</b> three chairs in the room.', 'There ______ three chairs in the room. (il y a)', 'are'),
    ('there-is-some', 'there is some + indénombrable', 'il y a du/de la — avec milk, water, money...', 'indénombrable', '<b>There is some</b> milk in the fridge.', 'There is ______ milk in the fridge. (du)', 'some'),
    ('there-isnt', 'there isn\'t', 'il n\'y a pas + singulier', 'négation sing.', '<b>There isn\'t</b> a swimming pool.', 'There ______ a swimming pool. (il n\'y a pas)', 'isn\'t'),
    ('there-arent-any', 'there aren\'t any', 'il n\'y a pas de + pluriel — avec any', 'négation plur.', '<b>There aren\'t any</b> shops near here.', 'There aren\'t ______ shops near here. (pas de)', 'any'),
    ('is-there', 'Is there...?', 'y a-t-il + singulier ? — question par inversion', 'question sing.', '<b>Is there</b> a bank near here?', '______ there a bank near here? (y a-t-il)', 'is'),
    ('are-there', 'Are there any...?', 'y a-t-il des... ? — question au pluriel', 'question plur.', '<b>Are there any</b> restaurants?', '______ there any restaurants? (y a-t-il)', 'are'),
    ('short-answer', 'Yes, there is.', 'réponse courte — on reprend there + is/are', 'réponse', 'Is there a pool? <b>Yes, there is.</b>', 'Is there a pool? Yes, there ______. (réponse courte)', 'is'),
  ],
),

'question-words': dict(
  level='a1', section='grammaire', num='Ch. 15', short='Les mots interrogatifs',
  title='Les mots interrogatifs — who, what, where, when, why, how',
  subtitle='Poser toutes les questions essentielles en anglais',
  slides=[
    ('Les six mots interrogatifs de base', None,
     '<p class="slide-explanation">Les <b>question words</b> (ou « wh-words ») permettent de poser des questions ouvertes. Apprends d\'abord ces six-là, ils couvrent presque tout.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Who</b> = qui &nbsp;·&nbsp; <b>What</b> = quoi/que &nbsp;·&nbsp; <b>Where</b> = où</p>'
     '<p style="margin-top:8px"><b>When</b> = quand &nbsp;·&nbsp; <b>Why</b> = pourquoi &nbsp;·&nbsp; <b>How</b> = comment</p></div>'
     '<p style="margin-top:16px">Attention à ne pas confondre <b>where</b> (où) et <b>who</b> (qui) — les francophones les mélangent souvent à cause de la ressemblance sonore.</p>'),
    ('L\'ordre des mots dans la question', None,
     '<p class="slide-explanation">La structure est toujours la même : <b>mot interrogatif + auxiliaire + sujet + verbe</b>. Avec le present simple, l\'auxiliaire est do/does.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Where do</b> you live? — Où habites-tu ?</p>'
     '<p style="margin-top:8px"><b>What does</b> she do? — Que fait-elle ?</p>'
     '<p style="margin-top:8px"><b>Why do</b> they study English? — Pourquoi étudient-ils l\'anglais ?</p></div>'
     '<p style="margin-top:16px">« Where you live? » sans do est LA faute de francophone. N\'oublie jamais l\'auxiliaire !</p>'),
    ('Questions avec to be : pas d\'auxiliaire', None,
     '<p class="slide-explanation">Quand le verbe est <b>to be</b>, pas besoin de do/does : on inverse simplement le sujet et le verbe.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Where is</b> the station? — Où est la gare ?</p>'
     '<p style="margin-top:8px"><b>How are</b> you? — Comment vas-tu ?</p>'
     '<p style="margin-top:8px"><b>Who is</b> that man? — Qui est cet homme ?</p></div>'
     '<p style="margin-top:16px">Compare : Where IS the station? (to be → inversion) / Where DO you live? (verbe ordinaire → do).</p>'),
    ('How + adjectif : how old, how much, how many', None,
     '<p class="slide-explanation"><b>How</b> se combine avec d\'autres mots pour former des questions précises. La plus importante : <b>How old are you?</b> (l\'âge se demande avec to be, pas avec have !).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>How old</b> are you? — Quel âge as-tu ? (littéralement « comme vieux es-tu »)</p>'
     '<p style="margin-top:8px"><b>How many</b> brothers do you have? — Combien de frères as-tu ? (dénombrable)</p>'
     '<p style="margin-top:8px"><b>How much</b> is it? — Combien ça coûte ? (indénombrable/prix)</p></div>'
     '<p style="margin-top:16px"><b>How many</b> + pluriel dénombrable · <b>How much</b> + indénombrable. On y reviendra avec some/any.</p>'),
    ('Which et whose', None,
     '<p class="slide-explanation">Deux mots interrogatifs supplémentaires utiles : <b>which</b> (lequel, pour un choix limité) et <b>whose</b> (à qui, pour la possession).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Which</b> colour do you prefer, red or blue? — Quelle couleur préfères-tu, rouge ou bleu ?</p>'
     '<p style="margin-top:8px"><b>Whose</b> bag is this? — À qui est ce sac ?</p>'
     '<p style="margin-top:8px;color:var(--muted)">(Whose ≠ who\'s ! Who\'s = who is.)</p></div>'
     '<p style="margin-top:16px"><b>What</b> = choix ouvert (What music do you like?) · <b>Which</b> = choix limité (Which one, this or that?).</p>'),
  ],
  traps=[
    ('Where you live?', 'Where <strong>do you</strong> live?', 'Avec un verbe ordinaire, l\'auxiliaire do/does est obligatoire : Where DO you live?'),
    ('How old have you?', 'How old <strong>are</strong> you?', 'L\'âge se demande avec to be : How old ARE you? — jamais avec have (interférence de « quel âge as-tu »).'),
    ('What does she does?', 'What does she <strong>do</strong>?', 'Après does, le verbe revient à la base verbale : What does she DO? (un seul -es, sur l\'auxiliaire).'),
    ('How many money do you have?', 'How <strong>much</strong> money do you have?', 'Money est indénombrable → how MUCH money. How many s\'utilise avec un pluriel dénombrable.'),
    ('Who\'s bag is this?', '<strong>Whose</strong> bag is this?', 'La possession se demande avec whose. Who\'s = who is — c\'est une autre question !'),
  ],
  summary=[
    ('Les six de base', 'who · what · where · when · why · how', 'Who is that? / Where do you live?'),
    ('Verbe ordinaire', 'Mot interrogatif + do/does + sujet + verbe', 'Where do you live?'),
    ('Avec to be', 'Mot interrogatif + am/is/are + sujet', 'Where is the station?'),
    ('Âge', 'How old + be', 'How old are you?'),
    ('Quantité', 'How many + pluriel · How much + indénombrable', 'How many brothers? / How much is it?'),
    ('Choix et possession', 'which = lequel · whose = à qui', 'Which one? / Whose bag is this?'),
  ],
  ex1=('Choisis le bon mot interrogatif', 'Qui, quoi, où, quand, pourquoi ou comment ?', [
    ('______ do you live? — In Lyon.', ['Where', 'When', 'Who'], 'Where',
     'La réponse est un lieu → WHERE (où).'),
    ('______ is your birthday? — In May.', ['When', 'Where', 'What'], 'When',
     'La réponse est une date → WHEN (quand).'),
    ('______ is that woman? — She\'s my teacher.', ['Who', 'Where', 'Which'], 'Who',
     'La réponse est une personne → WHO (qui).'),
    ('______ are you learning English? — Because I love it!', ['Why', 'How', 'What'], 'Why',
     'La réponse commence par because → WHY (pourquoi).'),
    ('______ do you go to school? — By bus.', ['How', 'Why', 'Where'], 'How',
     'La réponse est un moyen → HOW (comment).'),
    ('______ is your favourite colour? — Blue.', ['What', 'Which', 'Who'], 'What',
     'Choix ouvert parmi toutes les couleurs → WHAT.'),
  ]),
  ex2=('Complète la question', 'Écris le mot qui manque (auxiliaire ou mot interrogatif).', [
    ('Where ______ you live? (auxiliaire)', 'do',
     'Verbe ordinaire → auxiliaire DO obligatoire : Where DO you live?'),
    ('How old ______ you? (verbe)', 'are',
     'L\'âge se demande avec to be : How old ARE you?'),
    ('What ______ she do at the weekend? (auxiliaire)', 'does',
     'Avec she → DOES : What DOES she do?'),
    ('How ______ brothers do you have? (combien, dénombrable)', 'many',
     'Brothers est dénombrable pluriel → how MANY brothers.'),
    ('______ bag is this? It\'s Marie\'s. (à qui)', 'Whose',
     'La possession → WHOSE bag is this? (≠ who\'s = who is).'),
  ]),
  ex3=('Corrige les questions fausses', 'Choisis la version correcte.', [
    ('« Where you go on holiday? »', ['Where do you go on holiday?', 'Where you do go on holiday?', 'Where go you on holiday?'], 'Where do you go on holiday?',
     'Mot interrogatif + DO + sujet + verbe : Where DO you go...?'),
    ('« How old have you? »', ['How old are you?', 'How old do you have?', 'How many years have you?'], 'How old are you?',
     'L\'âge avec to be : How old ARE you? L\'interférence du français fait utiliser have — à éviter.'),
    ('« What time it is? »', ['What time is it?', 'What time it is?', 'What is time it?'], 'What time is it?',
     'Inversion obligatoire : What time IS IT?'),
    ('« How much books do you have? »', ['How many books do you have?', 'How much books you have?', 'How many books have you?'], 'How many books do you have?',
     'Books est dénombrable pluriel → how MANY books + do you have.'),
    ('« Why you are late? »', ['Why are you late?', 'Why you are late?', 'Why do you be late?'], 'Why are you late?',
     'Avec to be → inversion : Why ARE YOU late? Pas de do avec be.'),
  ]),
  game_desc='Chaque mot interrogatif passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('who', 'who', 'qui — pour demander une personne', 'qui ?', '<b>Who</b> is that man?', '______ is that man? (qui)', 'who'),
    ('what', 'what', 'quoi / que / quel — choix ouvert', 'quoi ?', '<b>What</b> is your favourite colour?', '______ is your favourite colour? (quel)', 'what'),
    ('where', 'where', 'où — pour demander un lieu', 'où ?', '<b>Where</b> do you live?', '______ do you live? (où)', 'where'),
    ('when', 'when', 'quand — pour demander un moment', 'quand ?', '<b>When</b> is your birthday?', '______ is your birthday? (quand)', 'when'),
    ('why', 'why', 'pourquoi — la réponse commence par because', 'pourquoi ?', '<b>Why</b> are you learning English?', '______ are you learning English? (pourquoi)', 'why'),
    ('how', 'how', 'comment — la manière ou le moyen', 'comment ?', '<b>How</b> do you go to school?', '______ do you go to school? (comment)', 'how'),
    ('how-old', 'How old are you?', 'quel âge as-tu ? — avec to be, jamais have', 'l\'âge', '<b>How old are</b> you?', 'How old ______ you? (verbe)', 'are'),
    ('how-many', 'how many', 'combien de + dénombrable pluriel', 'combien ?', '<b>How many</b> brothers do you have?', 'How ______ brothers do you have? (combien)', 'many'),
  ],
),

}
