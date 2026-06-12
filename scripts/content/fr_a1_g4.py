# -*- coding: utf-8 -*-
"""fr/ A1 grammaire — lot 4 (chapitres 16-20). Explications en français, anglais cible."""

CHAPTERS = {

'imperatives': dict(
  level='a1', section='grammaire', num='Ch. 16', short='L\'impératif',
  title='L\'impératif — Open the door! Don\'t run!',
  subtitle='Donner des ordres, des conseils et des instructions en anglais',
  slides=[
    ('L\'impératif : la base verbale, c\'est tout', None,
     '<p class="slide-explanation">L\'impératif anglais est le temps le plus simple qui existe : on utilise la <b>base verbale</b> (l\'infinitif sans to), sans sujet. Une seule forme pour « tu » et « vous » !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Open</b> the door! — Ouvre la porte ! / Ouvrez la porte !</p>'
     '<p style="margin-top:8px"><b>Listen</b> carefully. — Écoute bien. / Écoutez bien.</p>'
     '<p style="margin-top:8px"><b>Sit</b> down, please. — Assieds-toi / Asseyez-vous, s\'il te/vous plaît.</p></div>'
     '<p style="margin-top:16px">Pas de conjugaison à apprendre : la même forme sert pour une personne ou pour un groupe.</p>'),
    ('La négation : Don\'t + verbe', None,
     '<p class="slide-explanation">Pour interdire ou déconseiller, on place <b>Don\'t</b> (do not) devant la base verbale. C\'est le seul mot à ajouter.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Don\'t run</b> in the corridor! — Ne cours pas dans le couloir !</p>'
     '<p style="margin-top:8px"><b>Don\'t be</b> late. — Ne sois pas en retard.</p>'
     '<p style="margin-top:8px"><b>Don\'t forget</b> your keys. — N\'oublie pas tes clés.</p></div>'
     '<p style="margin-top:16px">Remarque : même avec to be, on utilise don\'t → <b>Don\'t be</b> afraid (n\'aie pas peur).</p>'),
    ('Adoucir avec please', None,
     '<p class="slide-explanation">L\'impératif seul peut paraître sec en anglais. On ajoute <b>please</b> (au début ou à la fin) pour être poli — c\'est presque obligatoire dans les demandes de tous les jours.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Please</b> close the window. — Ferme la fenêtre, s\'il te plaît.</p>'
     '<p style="margin-top:8px">Wait a moment, <b>please</b>. — Attendez un instant, s\'il vous plaît.</p>'
     '<p style="margin-top:8px"><b>Please don\'t</b> touch. — Ne touchez pas, s\'il vous plaît.</p></div>'
     '<p style="margin-top:16px">Les anglophones utilisent please beaucoup plus que les francophones n\'utilisent « s\'il vous plaît ». Sans please, un ordre peut sembler impoli.</p>'),
    ('Let\'s : proposer de faire ensemble', None,
     '<p class="slide-explanation">Pour proposer une activité commune (« allons-y », « faisons... »), on utilise <b>Let\'s</b> + base verbale. La négation est <b>Let\'s not</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Let\'s go</b> to the beach! — Allons à la plage !</p>'
     '<p style="margin-top:8px"><b>Let\'s play</b> football. — Jouons au foot.</p>'
     '<p style="margin-top:8px"><b>Let\'s not</b> stay here. — Ne restons pas ici.</p></div>'
     '<p style="margin-top:16px">Let\'s = let us, mais on utilise presque toujours la contraction.</p>'),
    ('Où rencontre-t-on l\'impératif ?', None,
     '<p class="slide-explanation">L\'impératif est partout dans la vie quotidienne anglophone : panneaux, recettes, modes d\'emploi, consignes de classe. Le reconnaître t\'aide à comprendre ton environnement.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Push.</b> / <b>Pull.</b> — Poussez. / Tirez. (sur les portes)</p>'
     '<p style="margin-top:8px"><b>Mix</b> the eggs and the sugar. — Mélangez les œufs et le sucre. (recette)</p>'
     '<p style="margin-top:8px"><b>Turn left</b> at the bank. — Tournez à gauche à la banque. (itinéraire)</p></div>'
     '<p style="margin-top:16px">Astuce examen : les consignes des exercices Cambridge sont à l\'impératif — Read the text, Answer the questions, Choose the correct word.</p>'),
  ],
  traps=[
    ('You open the door!', '<strong>Open</strong> the door!', 'L\'impératif n\'a pas de sujet : on dit Open the door!, sans « you ».'),
    ('Not run in the corridor!', '<strong>Don\'t run</strong> in the corridor!', 'La négation de l\'impératif utilise don\'t : DON\'T run — jamais « not » seul.'),
    ('Don\'t to forget your keys.', 'Don\'t <strong>forget</strong> your keys.', 'Après don\'t, on utilise la base verbale sans to : don\'t FORGET.'),
    ('Let\'s to go to the cinema.', 'Let\'s <strong>go</strong> to the cinema.', 'Après let\'s, la base verbale sans to : let\'s GO.'),
    ('Close the door. (à un client)', '<strong>Please</strong> close the door.', 'Sans please, l\'impératif peut sembler très sec en anglais. Ajoute toujours please dans une demande polie.'),
  ],
  summary=[
    ('Affirmation', 'base verbale (sans sujet)', 'Open the door! / Sit down.'),
    ('Négation', 'Don\'t + base verbale', 'Don\'t run! / Don\'t be late.'),
    ('Politesse', 'Please + impératif', 'Please close the window.'),
    ('Proposition', 'Let\'s + base verbale', 'Let\'s go to the beach!'),
    ('Proposition négative', 'Let\'s not + base verbale', 'Let\'s not stay here.'),
    ('Usage', 'panneaux · recettes · consignes', 'Push. / Turn left. / Read the text.'),
  ],
  ex1=('Forme l\'impératif correct', 'Affirmatif, négatif ou let\'s ?', [
    ('« Ferme la fenêtre ! » → ______ the window!', ['Close', 'You close', 'To close'], 'Close',
     'Impératif = base verbale sans sujet : CLOSE the window!'),
    ('« Ne parle pas ! » → ______ talk!', ['Don\'t', 'Not', 'No'], 'Don\'t',
     'Négation de l\'impératif : DON\'T + base verbale.'),
    ('« Allons au parc ! » → ______ go to the park!', ['Let\'s', 'We', 'Let'], 'Let\'s',
     'Proposition commune : LET\'S go (= let us go).'),
    ('« Ne sois pas triste. » → ______ sad.', ['Don\'t be', 'Don\'t', 'Not be'], 'Don\'t be',
     'Même avec to be, la négation utilise don\'t : DON\'T BE sad.'),
    ('« Écoutez bien, s\'il vous plaît. » → ______, please.', ['Listen carefully', 'You listen carefully', 'To listen carefully'], 'Listen carefully',
     'Impératif sans sujet + please pour la politesse.'),
    ('« Ne restons pas ici. » → ______ stay here.', ['Let\'s not', 'Don\'t let\'s', 'Not let\'s'], 'Let\'s not',
     'La négation de let\'s est LET\'S NOT + base verbale.'),
  ]),
  ex2=('Écris l\'ordre ou le conseil', 'Utilise l\'impératif (affirmatif ou négatif).', [
    ('« N\'oublie pas tes clés. » → ______ your keys. (deux mots)', 'Don\'t forget',
     'Négation : DON\'T FORGET — don\'t + base verbale sans to.'),
    ('« Assieds-toi. » → ______ down. (un mot)', 'Sit',
     'Impératif simple : SIT down.'),
    ('« Jouons au tennis ! » → ______ tennis! (deux mots)', 'Let\'s play',
     'Proposition : LET\'S PLAY tennis.'),
    ('« Tournez à gauche. » → ______ left. (un mot)', 'Turn',
     'Instruction d\'itinéraire : TURN left.'),
    ('« Ne touche pas ! » → ______! (deux mots)', 'Don\'t touch',
     'Interdiction : DON\'T TOUCH.'),
  ]),
  ex3=('Dans quelle situation ?', 'Choisis la phrase adaptée à chaque situation.', [
    ('Sur une porte de magasin :', ['Push.', 'You push.', 'To push.'], 'Push.',
     'Les panneaux utilisent l\'impératif : Push (poussez) / Pull (tirez).'),
    ('Un professeur donne une consigne :', ['Read the text, please.', 'You read the text.', 'Reading the text.'], 'Read the text, please.',
     'Consigne de classe = impératif + please pour la politesse.'),
    ('Tu proposes une sortie à tes amis :', ['Let\'s go to the cinema!', 'Go to the cinema!', 'You go to the cinema!'], 'Let\'s go to the cinema!',
     'Pour proposer de faire ensemble → LET\'S go.'),
    ('Tu rassures un ami inquiet :', ['Don\'t be afraid.', 'Not be afraid.', 'Don\'t to be afraid.'], 'Don\'t be afraid.',
     'Don\'t + be (base verbale) : DON\'T BE afraid.'),
    ('Une recette de cuisine :', ['Mix the eggs and the sugar.', 'You mix the eggs and the sugar.', 'To mix the eggs and the sugar.'], 'Mix the eggs and the sugar.',
     'Les recettes anglaises sont à l\'impératif : Mix, Add, Cook...'),
  ]),
  game_desc='Chaque forme de l\'impératif passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('open', 'Open the door!', 'impératif affirmatif — base verbale sans sujet', 'ordre', '<b>Open</b> the door, please.', '______ the door, please. (ouvre)', 'open'),
    ('dont-run', 'Don\'t run!', 'impératif négatif — don\'t + base verbale', 'interdiction', '<b>Don\'t run</b> in the corridor!', '______ run in the corridor! (ne... pas)', 'don\'t'),
    ('dont-be', 'Don\'t be late.', 'don\'t + be — même to be utilise don\'t', 'négation de be', '<b>Don\'t be</b> late tomorrow.', 'Don\'t ______ late tomorrow. (sois)', 'be'),
    ('please', 'please', 's\'il te/vous plaît — adoucit l\'ordre', 'politesse', '<b>Please</b> close the window.', '______ close the window. (politesse)', 'please'),
    ('lets-go', 'Let\'s go!', 'allons-y — proposition de faire ensemble', 'proposition', '<b>Let\'s go</b> to the beach!', '______ go to the beach! (allons)', 'let\'s'),
    ('lets-not', 'Let\'s not...', 'ne... pas ensemble — négation de let\'s', 'proposition nég.', '<b>Let\'s not</b> stay here.', 'Let\'s ______ stay here. (négation)', 'not'),
    ('turn-left', 'Turn left.', 'tournez à gauche — itinéraires à l\'impératif', 'itinéraire', '<b>Turn left</b> at the bank.', '______ left at the bank. (tournez)', 'turn'),
    ('sit-down', 'Sit down.', 'assieds-toi — consigne de classe courante', 'consigne', '<b>Sit down</b>, please.', '______ down, please. (assieds-toi)', 'sit'),
  ],
),

'present-simple': dict(
  level='a1', section='grammaire', num='Ch. 17', short='Le present simple',
  title='Le present simple — I work, she works',
  subtitle='Le temps des habitudes et des vérités générales, avec do et does',
  slides=[
    ('Le present simple : habitudes et vérités', None,
     '<p class="slide-explanation">Le <b>present simple</b> décrit les habitudes, les goûts et les vérités générales. C\'est l\'équivalent du présent français — mais sa conjugaison est bien plus simple !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>work</b> in Paris. — Je travaille à Paris. (situation habituelle)</p>'
     '<p style="margin-top:8px">She <b>likes</b> chocolate. — Elle aime le chocolat. (goût)</p>'
     '<p style="margin-top:8px">Water <b>boils</b> at 100°C. — L\'eau bout à 100 °C. (vérité générale)</p></div>'
     '<p style="margin-top:16px">Une seule difficulté à retenir : le <b>-s à la troisième personne</b> du singulier.</p>'),
    ('Le -s de la troisième personne', None,
     '<p class="slide-explanation">Avec <b>he, she, it</b>, le verbe prend un <b>-s</b>. C\'est la SEULE terminaison du present simple — mais c\'est la faute la plus fréquente au niveau A1, alors sois vigilant !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I work → he <b>works</b> &nbsp;·&nbsp; I play → she <b>plays</b></p>'
     '<p style="margin-top:8px">I watch → he <b>watches</b> &nbsp;·&nbsp; I study → she <b>studies</b></p>'
     '<p style="margin-top:8px">I go → he <b>goes</b> &nbsp;·&nbsp; I have → she <b>has</b></p></div>'
     '<p style="margin-top:16px">Orthographe : -ch/-sh/-o → <b>-es</b> (watches, goes) ; consonne + y → <b>-ies</b> (studies). Et have devient <b>has</b>.</p>'),
    ('La négation : don\'t / doesn\'t', None,
     '<p class="slide-explanation">Grande différence avec le français : la négation utilise l\'auxiliaire <b>do/does + not</b>. Le verbe principal revient à la base verbale — le -s passe sur l\'auxiliaire !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>don\'t like</b> coffee. — Je n\'aime pas le café.</p>'
     '<p style="margin-top:8px">She <b>doesn\'t work</b> on Sundays. — Elle ne travaille pas le dimanche.</p>'
     '<p style="margin-top:8px;color:var(--muted)">(et non « she doesn\'t workS » — le -s est déjà dans doesn\'t !)</p></div>'
     '<p style="margin-top:16px">Règle d\'or : <b>un seul -s par phrase</b>. Si doesn\'t est là, le verbe reste nu.</p>'),
    ('La question : Do / Does + sujet + verbe', None,
     '<p class="slide-explanation">Pour poser une question, on place <b>Do</b> ou <b>Does</b> devant le sujet. Là encore, le verbe principal reste à la base verbale.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Do you like</b> pizza? — Aimes-tu la pizza ?</p>'
     '<p style="margin-top:8px"><b>Does she speak</b> English? — Parle-t-elle anglais ?</p>'
     '<p style="margin-top:8px">Réponses : <b>Yes, I do.</b> / <b>No, she doesn\'t.</b></p></div>'
     '<p style="margin-top:16px">Le français n\'a pas d\'équivalent de do : ne cherche pas à le traduire, c\'est juste la « machine à questions » de l\'anglais.</p>'),
    ('Les expressions de temps du present simple', None,
     '<p class="slide-explanation">Certaines expressions signalent le present simple : les adverbes de fréquence (chapitre 12) et les expressions d\'habitude.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>every day</b> (tous les jours) &nbsp;·&nbsp; <b>on Mondays</b> (le lundi)</p>'
     '<p style="margin-top:8px"><b>at the weekend</b> (le week-end) &nbsp;·&nbsp; <b>in the morning</b> (le matin)</p>'
     '<p style="margin-top:8px">I play tennis <b>every Saturday</b>. — Je joue au tennis tous les samedis.</p></div>'
     '<p style="margin-top:16px">« On Mondays » avec -s = tous les lundis, l\'habitude. C\'est l\'équivalent du « le lundi » français.</p>'),
  ],
  traps=[
    ('She work in a hospital.', 'She <strong>works</strong> in a hospital.', 'Troisième personne (he/she/it) → -s obligatoire : she workS. C\'est LA faute A1 par excellence.'),
    ('He doesn\'t works here.', 'He doesn\'t <strong>work</strong> here.', 'Un seul -s par phrase : doesn\'t porte déjà la marque, le verbe reste à la base : doesn\'t WORK.'),
    ('You like pizza?', '<strong>Do you like</strong> pizza?', 'La question exige l\'auxiliaire : DO you like...? La simple intonation ne suffit pas en anglais écrit.'),
    ('She no speaks English.', 'She <strong>doesn\'t speak</strong> English.', 'La négation se construit avec doesn\'t, pas avec « no » : she DOESN\'T SPEAK.'),
    ('Does she speaks French?', 'Does she <strong>speak</strong> French?', 'Après does, base verbale : Does she SPEAK? Le -s est déjà sur does.'),
  ],
  summary=[
    ('Affirmation', 'I/you/we/they + verbe · he/she/it + verbe-s', 'I work. / She works.'),
    ('Orthographe du -s', '-ch/-sh/-o → -es · consonne+y → -ies', 'watches / goes / studies'),
    ('Négation', 'don\'t / doesn\'t + base verbale', 'She doesn\'t work on Sundays.'),
    ('Question', 'Do/Does + sujet + base verbale?', 'Does she speak English?'),
    ('Réponse courte', 'Yes, I do. / No, she doesn\'t.', 'Do you like pizza? Yes, I do.'),
    ('Expressions', 'every day · on Mondays · at the weekend', 'I play tennis every Saturday.'),
  ],
  ex1=('Mets le verbe à la bonne forme', 'Attention au -s de la troisième personne !', [
    ('My sister ______ in a bank.', ['works', 'work', 'working'], 'works',
     'My sister = she → -s : she WORKS.'),
    ('I ______ to music every day.', ['listen', 'listens', 'listening'], 'listen',
     'Avec I, pas de -s : I LISTEN.'),
    ('He ______ TV in the evening.', ['watches', 'watchs', 'watch'], 'watches',
     'Watch se termine en -ch → -ES : he watchES.'),
    ('She ______ English and Spanish.', ['studies', 'studys', 'study'], 'studies',
     'Study : consonne + y → -IES : she studIES.'),
    ('My parents ______ in Lyon.', ['live', 'lives', 'living'], 'live',
     'My parents = they → pas de -s : they LIVE.'),
    ('My brother ______ a lot of homework.', ['has', 'haves', 'have'], 'has',
     'Have est irrégulier à la 3e personne : he/she HAS.'),
  ]),
  ex2=('Négation et question', 'Écris la forme demandée avec do/does.', [
    ('« Elle ne mange pas de viande. » → She ______ eat meat. (un mot)', 'doesn\'t',
     'She → DOESN\'T + base verbale : she doesn\'t EAT.'),
    ('« Aimes-tu le café ? » → ______ you like coffee? (un mot)', 'Do',
     'Question avec you → DO you like...?'),
    ('« Parle-t-il français ? » → ______ he speak French? (un mot)', 'Does',
     'Question avec he → DOES he speak...? (verbe sans -s).'),
    ('« Nous ne regardons pas la télé. » → We ______ watch TV. (un mot)', 'don\'t',
     'We → DON\'T + base verbale.'),
    ('« Oui, je l\'aime. » (réponse à Do you like it?) → Yes, I ______. (un mot)', 'do',
     'Réponse courte : Yes, I DO — on reprend l\'auxiliaire, pas le verbe.'),
  ]),
  ex3=('Trouve la phrase correcte', 'Un seul -s par phrase !', [
    ('« Elle travaille à Londres. »', ['She works in London.', 'She work in London.', 'She is work in London.'], 'She works in London.',
     'She + workS : le -s de la 3e personne est obligatoire.'),
    ('« Il ne joue pas au foot. »', ['He doesn\'t play football.', 'He doesn\'t plays football.', 'He don\'t play football.'], 'He doesn\'t play football.',
     'He → doesn\'t + base verbale PLAY (sans -s).'),
    ('« Habites-tu ici ? »', ['Do you live here?', 'Does you live here?', 'You live here?'], 'Do you live here?',
     'You → DO you live...? Does s\'utilise avec he/she/it.'),
    ('« Ma mère ne conduit pas. »', ['My mother doesn\'t drive.', 'My mother don\'t drive.', 'My mother doesn\'t drives.'], 'My mother doesn\'t drive.',
     'My mother = she → DOESN\'T + DRIVE (base verbale).'),
    ('« Est-ce que tes amis aiment le sport ? »', ['Do your friends like sport?', 'Does your friends like sport?', 'Your friends like sport?'], 'Do your friends like sport?',
     'Your friends = they → DO. L\'auxiliaire est obligatoire dans la question.'),
  ]),
  game_desc='Chaque forme du present simple passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('works', 'she works', 'le -s de la 3e personne — he/she/it + verbe-s', '3e personne', 'My sister <b>works</b> in a bank.', 'My sister ______ in a bank. (travaille)', 'works'),
    ('watches', 'he watches', '-es après -ch/-sh/-o — watches, goes', 'orthographe -es', 'He <b>watches</b> TV every evening.', 'He ______ TV every evening. (regarde)', 'watches'),
    ('studies', 'she studies', 'consonne + y → -ies — studies, flies', 'orthographe -ies', 'She <b>studies</b> English at school.', 'She ______ English at school. (étudie)', 'studies'),
    ('has', 'she has', 'have → has — l\'irrégulier de la 3e personne', 'irrégulier', 'My brother <b>has</b> a new bike.', 'My brother ______ a new bike. (a)', 'has'),
    ('dont', 'I don\'t like', 'négation 1re/2e personne — don\'t + base verbale', 'négation', 'I <b>don\'t like</b> coffee.', 'I ______ like coffee. (négation)', 'don\'t'),
    ('doesnt', 'she doesn\'t work', 'négation 3e personne — le -s passe sur doesn\'t', 'négation 3e p.', 'She <b>doesn\'t work</b> on Sundays.', 'She ______ work on Sundays. (négation)', 'doesn\'t'),
    ('do-you', 'Do you...?', 'question 1re/2e personne — do + sujet + verbe', 'question', '<b>Do you</b> like pizza?', '______ you like pizza? (auxiliaire)', 'do'),
    ('does-she', 'Does she...?', 'question 3e personne — does + sujet + base verbale', 'question 3e p.', '<b>Does she</b> speak English?', '______ she speak English? (auxiliaire)', 'does'),
  ],
),

'present-continuous': dict(
  level='a1', section='grammaire', num='Ch. 18', short='Le present continuous',
  title='Le present continuous — I am working',
  subtitle='Le temps de l\'action en cours, qui n\'existe pas en français',
  slides=[
    ('Un temps que le français n\'a pas', None,
     '<p class="slide-explanation">Le <b>present continuous</b> décrit une action <b>en train de se passer maintenant</b>. Le français utilise le présent simple ou « être en train de » — l\'anglais a un temps dédié.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>am working</b>. — Je travaille (en ce moment) / Je suis en train de travailler.</p>'
     '<p style="margin-top:8px">She <b>is sleeping</b>. — Elle dort (là, maintenant).</p>'
     '<p style="margin-top:8px">They <b>are playing</b> football. — Ils jouent au foot (en ce moment).</p></div>'
     '<p style="margin-top:16px">Formation : <b>be (am/is/are) + verbe-ing</b>. Les deux morceaux sont obligatoires !</p>'),
    ('La formation : be + verbe-ing', None,
     '<p class="slide-explanation">Le present continuous a toujours deux parties : l\'auxiliaire <b>be</b> conjugué (am/is/are) et le verbe principal en <b>-ing</b>. Oublier l\'une des deux est une faute classique.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>am eating</b> &nbsp;·&nbsp; you <b>are eating</b> &nbsp;·&nbsp; he/she <b>is eating</b></p>'
     '<p style="margin-top:8px">we <b>are eating</b> &nbsp;·&nbsp; they <b>are eating</b></p></div>'
     '<p style="margin-top:16px">Orthographe du -ing : make → <b>making</b> (le e tombe) ; run → <b>running</b> (consonne doublée) ; study → <b>studying</b> (le y reste).</p>'),
    ('Négation et question', None,
     '<p class="slide-explanation">Bonne nouvelle : comme l\'auxiliaire be est déjà là, la négation et la question suivent les règles de to be — pas besoin de do !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>She <b>isn\'t sleeping</b>. — Elle ne dort pas.</p>'
     '<p style="margin-top:8px"><b>Are you listening</b> to me? — Tu m\'écoutes ?</p>'
     '<p style="margin-top:8px"><b>What are you doing</b>? — Qu\'est-ce que tu fais ?</p></div>'
     '<p style="margin-top:16px">« What are you doing? » est probablement la question la plus fréquente de l\'anglais parlé — apprends-la en bloc.</p>'),
    ('Present simple ou present continuous ?', None,
     '<p class="slide-explanation">C\'est LE choix difficile pour un francophone, car le français dit « je travaille » dans les deux cas. Pose-toi la question : <b>habitude ou maintenant ?</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>work</b> in a bank. — Je travaille dans une banque. (mon métier, habitude)</p>'
     '<p style="margin-top:8px">I <b>am working</b> right now. — Je travaille là, maintenant. (action en cours)</p>'
     '<p style="margin-top:8px">She <b>speaks</b> English. (elle sait) / She <b>is speaking</b> English. (en ce moment)</p></div>'
     '<p style="margin-top:16px">Indices : <b>now, right now, at the moment, look!, listen!</b> → continuous. <b>every day, always, on Mondays</b> → simple.</p>'),
    ('Les verbes qui refusent le -ing', None,
     '<p class="slide-explanation">Certains verbes d\'état (goûts, opinions, possession) ne s\'utilisent presque jamais au continuous, même pour parler de maintenant.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>like, love, hate</b> — I <b>love</b> this song! (et non « I am loving »)</p>'
     '<p style="margin-top:8px"><b>want, need</b> — I <b>want</b> a coffee. (et non « I am wanting »)</p>'
     '<p style="margin-top:8px"><b>know, understand, have</b> (= posséder) — I <b>know</b> the answer.</p></div>'
     '<p style="margin-top:16px">Au niveau A1, retiens : like, love, want, need, know → toujours au present simple.</p>'),
  ],
  traps=[
    ('I working now.', 'I <strong>am working</strong> now.', 'Le present continuous a DEUX parties : be + -ing. Sans am/is/are, la phrase est incorrecte.'),
    ('She is work at the moment.', 'She is <strong>working</strong> at the moment.', 'Après is, le verbe prend -ing : she is workING.'),
    ('I am loving this song!', 'I <strong>love</strong> this song!', 'Love est un verbe d\'état : il reste au present simple, même pour maintenant.'),
    ('Do you watching TV?', '<strong>Are you watching</strong> TV?', 'La question du continuous utilise be, pas do : ARE you watching?'),
    ('He is runing in the park.', 'He is <strong>running</strong> in the park.', 'Run double sa consonne : runNING. (make → making, le e tombe ; run → running, le n double.)'),
  ],
  summary=[
    ('Formation', 'am/is/are + verbe-ing', 'I am working. / They are playing.'),
    ('Orthographe -ing', 'make → making · run → running · study → studying', 'making / running / studying'),
    ('Négation', 'am/is/are + not + verbe-ing', 'She isn\'t sleeping.'),
    ('Question', 'Am/Is/Are + sujet + verbe-ing?', 'Are you listening?'),
    ('Simple vs continuous', 'habitude → simple · maintenant → continuous', 'I work in a bank. / I am working now.'),
    ('Verbes d\'état', 'like, love, want, need, know → jamais -ing', 'I love this song!'),
  ],
  ex1=('Forme le present continuous', 'be + verbe-ing : les deux parties comptent.', [
    ('Look! It ______ ! (rain)', ['is raining', 'rains', 'raining'], 'is raining',
     '« Look! » signale une action en cours → present continuous : it IS RAINING.'),
    ('I ______ my homework right now. (do)', ['am doing', 'do', 'doing'], 'am doing',
     'Right now → continuous : I AM DOING.'),
    ('They ______ football in the park. (play)', ['are playing', 'is playing', 'play now'], 'are playing',
     'They → ARE + playING.'),
    ('She ______ a cake at the moment. (make)', ['is making', 'is makeing', 'makes now'], 'is making',
     'Make perd son e devant -ing : makING.'),
    ('The children ______ in the garden. (run)', ['are running', 'are runing', 'is running'], 'are running',
     'Run double le n : runNING. The children = they → are.'),
    ('He ______ to music. (listen)', ['is listening', 'is listen', 'listening'], 'is listening',
     'Be + -ing obligatoires : he IS LISTENING.'),
  ]),
  ex2=('Simple ou continuous ?', 'Choisis le bon temps et écris le verbe.', [
    ('I usually ______ tea, but today I ______ coffee. (drink / drink)', 'drink / am drinking',
     'Usually → simple (I drink) ; today → continuous (I am drinking).'),
    ('She ______ in a hospital. C\'est son métier. (work)', 'works',
     'Métier = habitude → present simple : she WORKS.'),
    ('Be quiet! The baby ______. (sleep)', 'is sleeping',
     'Action en cours (maintenant) → continuous : the baby IS SLEEPING.'),
    ('I ______ this song! (love)', 'love',
     'Love est un verbe d\'état → toujours simple : I LOVE this song.'),
    ('What ______ you ______ right now? (do)', 'are / doing',
     'Right now → continuous : What ARE you DOING?'),
  ]),
  ex3=('Corrige les fautes', 'Choisis la version correcte.', [
    ('« I watching TV. »', ['I am watching TV.', 'I watching TV now.', 'I am watch TV.'], 'I am watching TV.',
     'Les deux parties sont obligatoires : AM + watchING.'),
    ('« She is cook dinner. »', ['She is cooking dinner.', 'She is cooks dinner.', 'She cooking dinner.'], 'She is cooking dinner.',
     'Après is, le verbe prend -ing : cookING.'),
    ('« I am wanting a pizza. »', ['I want a pizza.', 'I am want a pizza.', 'I wanting a pizza.'], 'I want a pizza.',
     'Want est un verbe d\'état → present simple : I WANT.'),
    ('« Do they playing tennis? »', ['Are they playing tennis?', 'Do they play tennis now?', 'Does they playing tennis?'], 'Are they playing tennis?',
     'Question du continuous avec be : ARE they playing?'),
    ('« He is studying every day. » (habitude !)', ['He studies every day.', 'He is study every day.', 'He studying every day.'], 'He studies every day.',
     'Every day = habitude → present simple : he STUDIES.'),
  ]),
  game_desc='Chaque forme du present continuous passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('am-working', 'I am working', 'action en cours — be + verbe-ing', 'maintenant', 'I <b>am working</b> right now.', 'I am ______ right now. (en train de travailler)', 'working'),
    ('is-sleeping', 'she is sleeping', '3e personne — is + verbe-ing', 'is + -ing', 'The baby <b>is sleeping</b>.', 'The baby is ______. (en train de dormir)', 'sleeping'),
    ('are-playing', 'they are playing', 'pluriel — are + verbe-ing', 'are + -ing', 'They <b>are playing</b> football.', 'They are ______ football. (en train de jouer)', 'playing'),
    ('making', 'making', 'le e tombe — make → making', 'orthographe', 'She is <b>making</b> a cake.', 'She is ______ a cake. (make + ing)', 'making'),
    ('running', 'running', 'consonne doublée — run → running', 'orthographe', 'He is <b>running</b> in the park.', 'He is ______ in the park. (run + ing)', 'running'),
    ('isnt-sleeping', 'she isn\'t sleeping', 'négation — be + not + verbe-ing', 'négation', 'She <b>isn\'t sleeping</b> now.', 'She ______ sleeping now. (négation)', 'isn\'t'),
    ('are-you-doing', 'What are you doing?', 'la question du continuous — avec be, sans do', 'question', 'What <b>are</b> you <b>doing</b>?', 'What ______ you doing? (auxiliaire)', 'are'),
    ('state-verbs', 'I love (jamais loving)', 'verbes d\'état — like, love, want, need restent au simple', 'verbe d\'état', 'I <b>love</b> this song!', 'I ______ this song! (et non « am loving »)', 'love'),
  ],
),

'going-to-future': dict(
  level='a1', section='grammaire', num='Ch. 19', short='Le futur avec going to',
  title='Going to — le futur des projets',
  subtitle='Parler de ses projets et intentions, comme le futur proche français',
  slides=[
    ('Going to : le cousin du futur proche', None,
     '<p class="slide-explanation">Bonne nouvelle pour les francophones : <b>be going to + verbe</b> fonctionne presque exactement comme « aller + infinitif » en français. « Je vais voyager » → I am going to travel.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>am going to visit</b> London. — Je vais visiter Londres.</p>'
     '<p style="margin-top:8px">She <b>is going to study</b> medicine. — Elle va étudier la médecine.</p>'
     '<p style="margin-top:8px">We <b>are going to watch</b> a film tonight. — On va regarder un film ce soir.</p></div>'
     '<p style="margin-top:16px">Formation : <b>be (am/is/are) + going to + base verbale</b>. Trois morceaux, toujours dans cet ordre.</p>'),
    ('Quand utiliser going to ?', None,
     '<p class="slide-explanation">On utilise going to pour les <b>projets et intentions</b> (décidés avant de parler) et pour les <b>prédictions évidentes</b> (on voit que ça va arriver).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Projet :</b> I\'m going to learn the guitar this year. — Je vais apprendre la guitare cette année.</p>'
     '<p style="margin-top:8px"><b>Prédiction évidente :</b> Look at those clouds! It\'s going to rain. — Regarde ces nuages ! Il va pleuvoir.</p></div>'
     '<p style="margin-top:16px">Comme en français : « il va pleuvoir » quand les nuages sont déjà là. Le parallèle avec le futur proche marche presque toujours.</p>'),
    ('Négation et question', None,
     '<p class="slide-explanation">Comme pour le present continuous, l\'auxiliaire be fait tout le travail : négation avec not, question par inversion.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I\'m <b>not going to watch</b> TV tonight. — Je ne vais pas regarder la télé ce soir.</p>'
     '<p style="margin-top:8px"><b>Are you going to come</b> to the party? — Tu vas venir à la fête ?</p>'
     '<p style="margin-top:8px"><b>What are you going to do</b>? — Qu\'est-ce que tu vas faire ?</p></div>'
     '<p style="margin-top:16px">Réponses courtes avec be : Yes, I am. / No, I\'m not. — comme toujours avec l\'auxiliaire be.</p>'),
    ('Les expressions de temps du futur', None,
     '<p class="slide-explanation">Going to s\'accompagne d\'expressions qui situent le projet dans le futur. Les voici, des plus proches aux plus lointaines.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>tonight</b> (ce soir) &nbsp;·&nbsp; <b>tomorrow</b> (demain) &nbsp;·&nbsp; <b>next week</b> (la semaine prochaine)</p>'
     '<p style="margin-top:8px"><b>next month</b> (le mois prochain) &nbsp;·&nbsp; <b>next year</b> (l\'année prochaine) &nbsp;·&nbsp; <b>soon</b> (bientôt)</p></div>'
     '<p style="margin-top:16px">Piège : « la semaine prochaine » = next week, <b>sans article</b> — pas « the next week ».</p>'),
    ('Going to + go : le cas particulier', None,
     '<p class="slide-explanation">« Je vais aller... » donne en théorie « I am going to go... » — c\'est correct, mais les anglophones raccourcissent souvent en <b>I am going to + lieu</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I\'m <b>going to go</b> to the beach. = I\'m <b>going to</b> the beach (tomorrow).</p>'
     '<p style="margin-top:8px">She\'s <b>going to</b> Spain next summer. — Elle va en Espagne l\'été prochain.</p></div>'
     '<p style="margin-top:16px">Les deux formes sont justes. Retiens simplement que « going to the beach » peut déjà exprimer le futur avec une expression de temps.</p>'),
  ],
  traps=[
    ('I going to visit London.', 'I <strong>am going to</strong> visit London.', 'Be est obligatoire : I AM going to visit. Sans am/is/are, la structure s\'effondre.'),
    ('She is going to studies medicine.', 'She is going to <strong>study</strong> medicine.', 'Après going to, la base verbale sans -s ni -ing : going to STUDY.'),
    ('It will rain, look at the clouds!', 'It <strong>is going to</strong> rain, look at the clouds!', 'Prédiction évidente (les nuages sont là) → going to, comme le français « il va pleuvoir ».'),
    ('We are going to the next week party.', 'We are going to the party <strong>next week</strong>.', 'L\'expression de temps se place en fin de phrase : ...the party NEXT WEEK (sans the).'),
    ('Do you going to come?', '<strong>Are you going to</strong> come?', 'La question utilise be : ARE you going to come? Jamais do avec going to.'),
  ],
  summary=[
    ('Formation', 'am/is/are + going to + base verbale', 'I am going to travel.'),
    ('Projet', 'intention décidée avant de parler', 'I\'m going to learn the guitar.'),
    ('Prédiction', 'évidence visible', 'Look! It\'s going to rain.'),
    ('Négation', 'be + not + going to + verbe', 'I\'m not going to watch TV.'),
    ('Question', 'Am/Is/Are + sujet + going to + verbe?', 'Are you going to come?'),
    ('Temps du futur', 'tonight · tomorrow · next week · soon', 'We\'re leaving next week.'),
  ],
  ex1=('Forme le futur avec going to', 'be + going to + base verbale.', [
    ('I ______ visit my grandparents tomorrow.', ['am going to', 'going to', 'am going'], 'am going to',
     'Les trois morceaux : AM + GOING TO + visit.'),
    ('She ______ study medicine next year.', ['is going to', 'are going to', 'going to'], 'is going to',
     'She → IS going to study.'),
    ('Look at those clouds! It ______ rain.', ['is going to', 'is going', 'will going to'], 'is going to',
     'Prédiction évidente → it IS GOING TO rain.'),
    ('We ______ watch a film tonight.', ['are going to', 'is going to', 'am going to'], 'are going to',
     'We → ARE going to watch.'),
    ('They ______ buy a new car.', ['are going to', 'is going to', 'going to are'], 'are going to',
     'They → ARE going to buy.'),
    ('After going to, le verbe est à la base : She is going to ______ tonight.', ['cook', 'cooks', 'cooking'], 'cook',
     'Going to + base verbale : going to COOK (jamais cooks ni cooking).'),
  ]),
  ex2=('Traduis le futur proche', 'Écris la forme manquante de be going to.', [
    ('« Je vais voyager en Italie. » → I ______ travel to Italy. (trois mots)', 'am going to',
     '« Je vais » + infinitif = I AM GOING TO + base verbale.'),
    ('« Il va pleuvoir. » → It ______ rain. (trois mots)', 'is going to',
     'It → IS GOING TO rain.'),
    ('« Nous n\'allons pas sortir. » → We ______ going to go out. (deux mots)', 'are not',
     'Négation : we ARE NOT (aren\'t) going to go out.'),
    ('« Vas-tu venir à la fête ? » → ______ you going to come to the party? (un mot)', 'Are',
     'Question par inversion de be : ARE you going to come?'),
    ('« Elle va acheter une robe demain. » → She is going to ______ a dress tomorrow. (un mot)', 'buy',
     'Après going to → base verbale : BUY.'),
  ]),
  ex3=('Projets et prédictions', 'Choisis la phrase correcte.', [
    ('« Qu\'est-ce que tu vas faire ce week-end ? »', ['What are you going to do this weekend?', 'What do you going to do this weekend?', 'What you are going to do this weekend?'], 'What are you going to do this weekend?',
     'Question : What + ARE + sujet + going to + verbe.'),
    ('« Je ne vais pas regarder ce film. »', ['I\'m not going to watch this film.', 'I don\'t going to watch this film.', 'I\'m going to not watch this film.'], 'I\'m not going to watch this film.',
     'Négation : be + NOT + going to : I\'m NOT going to watch.'),
    ('« Attention ! Tu vas tomber ! »', ['Careful! You\'re going to fall!', 'Careful! You will to fall!', 'Careful! You go to fall!'], 'Careful! You\'re going to fall!',
     'Prédiction évidente (on le voit venir) → going to : you\'re GOING TO fall.'),
    ('« Ils vont se marier l\'année prochaine. »', ['They\'re going to get married next year.', 'They going to get married the next year.', 'They\'re going to get married the next year.'], 'They\'re going to get married next year.',
     'Next year SANS article : pas de « the next year ».'),
    ('Réponse courte à « Are you going to come? »', ['Yes, I am.', 'Yes, I going.', 'Yes, I do.'], 'Yes, I am.',
     'L\'auxiliaire est be → Yes, I AM (pas do).'),
  ]),
  game_desc='Chaque forme de going to passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('am-going-to', 'I am going to + verbe', 'je vais + infinitif — le futur des projets', 'futur proche', 'I <b>am going to</b> visit London.', 'I am ______ to visit London. (vais)', 'going'),
    ('is-going-to', 'she is going to', '3e personne — is + going to + base verbale', 'is going to', 'She <b>is going to</b> study medicine.', 'She ______ going to study medicine. (auxiliaire)', 'is'),
    ('base-verbale', 'going to + base verbale', 'après going to — verbe nu, sans -s ni -ing', 'verbe nu', 'She is going to <b>buy</b> a dress.', 'She is going to ______ a dress. (acheter)', 'buy'),
    ('prediction', 'It\'s going to rain', 'prédiction évidente — on voit que ça arrive', 'évidence', 'Look at those clouds! It\'s going to <b>rain</b>.', 'Look at those clouds! It\'s going to ______. (pleuvoir)', 'rain'),
    ('not-going-to', 'I\'m not going to', 'négation — be + not + going to', 'négation', 'I\'m <b>not</b> going to watch TV.', 'I\'m ______ going to watch TV. (négation)', 'not'),
    ('are-you-going', 'Are you going to...?', 'question — inversion de be', 'question', '<b>Are</b> you going to come to the party?', '______ you going to come? (auxiliaire)', 'are'),
    ('tomorrow', 'tomorrow', 'demain — expression de temps du futur', 'demain', 'I\'m going to see her <b>tomorrow</b>.', 'I\'m going to see her ______. (demain)', 'tomorrow'),
    ('next-week', 'next week', 'la semaine prochaine — sans article the', 'sans article', 'We\'re going to leave <b>next week</b>.', 'We\'re going to leave ______ week. (prochaine)', 'next'),
  ],
),

'some-any': dict(
  level='a1', section='grammaire', num='Ch. 20', short='Some et any',
  title='Some et any — du, de la, des',
  subtitle='Exprimer une quantité indéfinie : affirmatif, négatif, question',
  slides=[
    ('Some : la quantité indéfinie à l\'affirmatif', None,
     '<p class="slide-explanation"><b>Some</b> correspond au « du / de la / des » français : une quantité non précisée. Il s\'utilise dans les <b>phrases affirmatives</b>, avec les pluriels et les indénombrables.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I have <b>some</b> friends in London. — J\'ai des amis à Londres.</p>'
     '<p style="margin-top:8px">There is <b>some</b> milk in the fridge. — Il y a du lait dans le frigo.</p>'
     '<p style="margin-top:8px">She wants <b>some</b> water. — Elle veut de l\'eau.</p></div>'
     '<p style="margin-top:16px">Some + pluriel (some friends) ou some + indénombrable (some milk) — les deux marchent.</p>'),
    ('Any : dans les négations', None,
     '<p class="slide-explanation">Dans une phrase <b>négative</b>, some devient <b>any</b>. C\'est l\'équivalent du « pas de » français.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I don\'t have <b>any</b> money. — Je n\'ai pas d\'argent.</p>'
     '<p style="margin-top:8px">There aren\'t <b>any</b> apples left. — Il ne reste pas de pommes.</p>'
     '<p style="margin-top:8px">She doesn\'t want <b>any</b> help. — Elle ne veut pas d\'aide.</p></div>'
     '<p style="margin-top:16px">« I don\'t have some money » est une faute : au négatif, c\'est toujours <b>any</b>.</p>'),
    ('Any : dans les questions', None,
     '<p class="slide-explanation">Dans les <b>questions</b>, on utilise aussi <b>any</b> : on ne sait pas si la chose existe, donc la quantité est totalement ouverte.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Do you have <b>any</b> brothers or sisters? — As-tu des frères et sœurs ?</p>'
     '<p style="margin-top:8px">Is there <b>any</b> milk left? — Reste-t-il du lait ?</p>'
     '<p style="margin-top:8px">Are there <b>any</b> questions? — Y a-t-il des questions ?</p></div>'
     '<p style="margin-top:16px">Règle simple A1 : affirmatif → some · négatif et question → any.</p>'),
    ('L\'exception polie : some dans les offres', None,
     '<p class="slide-explanation">Une exception agréable : quand on <b>offre</b> ou qu\'on <b>demande poliment</b> quelque chose (et qu\'on attend un oui), on garde <b>some</b> dans la question.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Would you like <b>some</b> tea? — Veux-tu du thé ? (offre)</p>'
     '<p style="margin-top:8px">Can I have <b>some</b> water, please? — Puis-je avoir de l\'eau, s\'il vous plaît ? (demande polie)</p></div>'
     '<p style="margin-top:16px">L\'idée : si tu espères une réponse positive (offrir du thé, demander de l\'eau), some est plus naturel que any.</p>'),
    ('Some, any et les dénombrables', None,
     '<p class="slide-explanation">Rappel : some et any s\'utilisent avec les <b>pluriels</b> et les <b>indénombrables</b>. Avec un singulier dénombrable, on utilise a/an.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>a book (un livre) → <b>some books</b> (des livres) → not... <b>any books</b> (pas de livres)</p>'
     '<p style="margin-top:8px">— <b>some bread</b> (du pain) → not... <b>any bread</b> (pas de pain)</p>'
     '<p style="margin-top:8px;color:var(--muted)">(bread est indénombrable : jamais « a bread » !)</p></div>'
     '<p style="margin-top:16px">Indénombrables fréquents : water, milk, bread, money, time, music, homework.</p>'),
  ],
  traps=[
    ('I don\'t have some money.', 'I don\'t have <strong>any</strong> money.', 'Au négatif, some devient any : I don\'t have ANY money.'),
    ('Do you have some brothers?', 'Do you have <strong>any</strong> brothers?', 'Dans une question ordinaire, on utilise any : Do you have ANY brothers?'),
    ('There is any milk in the fridge.', 'There is <strong>some</strong> milk in the fridge.', 'À l\'affirmatif, c\'est some : there is SOME milk. Any est réservé au négatif et aux questions.'),
    ('Would you like any tea?', 'Would you like <strong>some</strong> tea?', 'Dans une offre polie (on espère un oui), on garde some : Would you like SOME tea?'),
    ('Can I have a bread?', 'Can I have <strong>some</strong> bread?', 'Bread est indénombrable : pas de « a bread ». On dit some bread (du pain).'),
  ],
  summary=[
    ('Affirmatif', 'some + pluriel / indénombrable', 'I have some friends. / some milk'),
    ('Négatif', 'not... any', 'I don\'t have any money.'),
    ('Question', 'any', 'Do you have any brothers?'),
    ('Offre polie', 'Would you like some...?', 'Would you like some tea?'),
    ('Singulier', 'a/an (jamais some)', 'a book → some books'),
    ('Indénombrables', 'water, bread, money, time...', 'some bread (jamais « a bread »)'),
  ],
  ex1=('Some ou any ?', 'Regarde si la phrase est affirmative, négative ou interrogative.', [
    ('I have ______ good friends at school.', ['some', 'any', 'a'], 'some',
     'Phrase affirmative → SOME : I have some friends.'),
    ('We don\'t have ______ milk.', ['any', 'some', 'a'], 'any',
     'Phrase négative → ANY : we don\'t have any milk.'),
    ('Do you have ______ questions?', ['any', 'some', 'a'], 'any',
     'Question ordinaire → ANY : do you have any questions?'),
    ('There are ______ apples on the table.', ['some', 'any', 'an'], 'some',
     'Affirmatif pluriel → SOME apples.'),
    ('Would you like ______ coffee?', ['some', 'any', 'a'], 'some',
     'Offre polie → SOME : would you like some coffee?'),
    ('There isn\'t ______ bread left.', ['any', 'some', 'a'], 'any',
     'Négatif → ANY : there isn\'t any bread.'),
  ]),
  ex2=('Traduis la quantité', 'Écris some, any, a ou an.', [
    ('« J\'ai des cousins en Espagne. » → I have ______ cousins in Spain.', 'some',
     'Des = quantité indéfinie à l\'affirmatif → SOME.'),
    ('« Je n\'ai pas d\'argent. » → I don\'t have ______ money.', 'any',
     'Pas de + négatif → ANY.'),
    ('« Reste-t-il du lait ? » → Is there ______ milk left?', 'any',
     'Question → ANY.'),
    ('« Veux-tu du thé ? » (offre) → Would you like ______ tea?', 'some',
     'Offre polie → SOME, même dans une question.'),
    ('« Il y a du pain sur la table. » → There is ______ bread on the table.', 'some',
     'Affirmatif + indénombrable → SOME bread.'),
  ]),
  ex3=('Trouve la phrase correcte', 'Attention aux indénombrables et au choix some/any.', [
    ('« Je n\'ai pas de devoirs ce soir. »', ['I don\'t have any homework tonight.', 'I don\'t have some homework tonight.', 'I don\'t have a homework tonight.'], 'I don\'t have any homework tonight.',
     'Négatif → ANY. Homework est indénombrable (jamais « a homework »).'),
    ('« As-tu des animaux ? »', ['Do you have any pets?', 'Do you have some pets?', 'Have you any pet?'], 'Do you have any pets?',
     'Question → ANY + pluriel : any pets.'),
    ('« Il y a des magasins dans ma rue. »', ['There are some shops in my street.', 'There are any shops in my street.', 'There is some shops in my street.'], 'There are some shops in my street.',
     'Affirmatif pluriel → THERE ARE SOME shops.'),
    ('« Puis-je avoir de l\'eau, s\'il vous plaît ? »', ['Can I have some water, please?', 'Can I have any water, please?', 'Can I have a water, please?'], 'Can I have some water, please?',
     'Demande polie → SOME. Water est indénombrable (pas de « a water »).'),
    ('« Nous n\'avons pas de questions. »', ['We don\'t have any questions.', 'We don\'t have some questions.', 'We no have any questions.'], 'We don\'t have any questions.',
     'Négation avec don\'t + ANY : we don\'t have any questions.'),
  ]),
  game_desc='Chaque emploi de some et any passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('some-plural', 'some + pluriel', 'des — quantité indéfinie à l\'affirmatif', 'des', 'I have <b>some</b> friends in London.', 'I have ______ friends in London. (des)', 'some'),
    ('some-uncount', 'some + indénombrable', 'du / de la — avec milk, water, bread...', 'du / de la', 'There is <b>some</b> milk in the fridge.', 'There is ______ milk in the fridge. (du)', 'some'),
    ('not-any', 'not... any', 'pas de — any dans les négations', 'pas de', 'I don\'t have <b>any</b> money.', 'I don\'t have ______ money. (pas d\')', 'any'),
    ('question-any', 'any dans les questions', 'des... ? — any dans les questions ordinaires', 'question', 'Do you have <b>any</b> brothers?', 'Do you have ______ brothers? (des)', 'any'),
    ('would-some', 'Would you like some...?', 'offre polie — some reste dans les offres', 'offre', 'Would you like <b>some</b> tea?', 'Would you like ______ tea? (du)', 'some'),
    ('arent-any', 'there aren\'t any', 'il n\'y a pas de — négation de there are', 'il n\'y a pas', 'There aren\'t <b>any</b> apples left.', 'There aren\'t ______ apples left. (pas de)', 'any'),
    ('a-vs-some', 'a book → some books', 'singulier a/an — some pour le pluriel', 'a/an vs some', 'I need <b>a</b> pen and <b>some</b> paper.', 'I need a pen and ______ paper. (du)', 'some'),
    ('uncountable', 'bread, money, water', 'indénombrables — jamais a/an devant', 'indénombrable', 'Can I have some <b>bread</b>, please?', 'Can I have some ______, please? (pain)', 'bread'),
  ],
),

}
