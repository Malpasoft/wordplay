# -*- coding: utf-8 -*-
"""fr/ A1 grammaire — lot 1 (chapitres 1-5). Explications en français, anglais cible."""

CHAPTERS = {

'to-be': dict(
  level='a1', section='grammaire', num='Ch. 1', short='Le verbe être',
  title='Le verbe être — I am, you are, he is',
  subtitle='La conjugaison de to be et ses pièges pour les francophones',
  slides=[
    ('To be : le verbe le plus important', None,
     '<p class="slide-explanation">En anglais, le verbe <b>to be</b> (être) est indispensable. Il se conjugue différemment selon le pronom, et les contractions sont très fréquentes à l\'oral et à l\'écrit informel.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I am</b> (I\'m) &nbsp;·&nbsp; <b>You are</b> (You\'re) &nbsp;·&nbsp; <b>He/She/It is</b> (He\'s / She\'s / It\'s)</p>'
     '<p style="margin-top:8px"><b>We are</b> (We\'re) &nbsp;·&nbsp; <b>You are</b> (You\'re) &nbsp;·&nbsp; <b>They are</b> (They\'re)</p></div>'
     '<p style="margin-top:16px">Contrairement au français, l\'anglais <b>ne supprime jamais le pronom</b> : on ne dit pas « am happy », mais toujours <b>I am happy</b>.</p>'),
    ('Les contractions', None,
     '<p class="slide-explanation">Les contractions sont très naturelles en anglais. On les utilise dans la parole et dans tout écrit informel. Elles n\'ont pas d\'équivalent en français.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I am</b> → <b>I\'m</b> &nbsp;&nbsp; <b>you are</b> → <b>you\'re</b> &nbsp;&nbsp; <b>he is</b> → <b>he\'s</b></p>'
     '<p style="margin-top:8px"><b>she is</b> → <b>she\'s</b> &nbsp;&nbsp; <b>it is</b> → <b>it\'s</b> &nbsp;&nbsp; <b>they are</b> → <b>they\'re</b></p></div>'
     '<p style="margin-top:16px">Ne confonds pas <b>it\'s</b> (it is) et <b>its</b> (son/sa — possessif). C\'est une faute très courante !</p>'),
    ('La négation', None,
     '<p class="slide-explanation">Pour mettre to be à la forme négative, il suffit d\'ajouter <b>not</b> après le verbe. Pas besoin de « do » comme pour les autres verbes !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I am not</b> happy. (I\'m not happy.) — Je ne suis pas content.</p>'
     '<p style="margin-top:8px"><b>She is not</b> here. (She\'s not / She isn\'t here.) — Elle n\'est pas là.</p>'
     '<p style="margin-top:8px"><b>They are not</b> ready. (They aren\'t ready.) — Ils ne sont pas prêts.</p></div>'
     '<p style="margin-top:16px">Attention : la seule contraction impossible est <b>am not</b> → il n\'y a pas de « amn\'t ». On dit <b>I\'m not</b>, jamais « I amn\'t ».</p>'),
    ('La question', None,
     '<p class="slide-explanation">Pour poser une question avec to be, on <b>inverse le sujet et le verbe</b>. Pas de « do » ! C\'est très différent du français qui utilise souvent « est-ce que ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Are you</b> happy? — Es-tu content ?</p>'
     '<p style="margin-top:8px"><b>Is she</b> a doctor? — Est-elle médecin ?</p>'
     '<p style="margin-top:8px"><b>Are they</b> ready? — Sont-ils prêts ?</p></div>'
     '<p style="margin-top:16px">Réponses courtes : <b>Yes, I am.</b> / <b>No, I\'m not.</b> · <b>Yes, she is.</b> / <b>No, she isn\'t.</b> — On ne dit jamais juste « Yes, I\'m. »</p>'),
    ('To be pour les professions et nationalités', None,
     '<p class="slide-explanation">On utilise <b>to be</b> pour parler de sa profession, sa nationalité, son état. En anglais, les professions prennent un article (<b>a</b> ou <b>an</b>) — contrairement au français !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« Je suis étudiant. » → <b>I am a student.</b> (avec « a » !)</p>'
     '<p style="margin-top:8px">« Elle est infirmière. » → <b>She is a nurse.</b></p>'
     '<p style="margin-top:8px">« Nous sommes français. » → <b>We are French.</b></p></div>'
     '<p style="margin-top:16px">Les adjectifs de nationalité prennent une <b>majuscule</b> en anglais : <b>French</b>, <b>Spanish</b>, <b>English</b>.</p>'),
  ],
  traps=[
    ('I am a student.', 'I am <strong>a</strong> student.', 'Attention : en anglais, on dit « I am A student » — l\'article est obligatoire avec les professions, contrairement au français (« je suis étudiant »).'),
    ('Are you be tired?', '<strong>Are you</strong> tired?', 'La question avec to be se forme par inversion simple : Are you...? On n\'utilise jamais « do » ni « be » en question.'),
    ('She not is happy.', 'She <strong>is not</strong> happy.', 'La négation se place directement après to be : she IS NOT — pas avant.'),
    ('Yes, I\'m.', 'Yes, I <strong>am</strong>.', 'Les réponses courtes ne se contractent jamais à l\'affirmatif : « Yes, I am. » (et non « Yes, I\'m. »)'),
    ('He is french.', 'He is <strong>French</strong>.', 'Les nationalités et les langues prennent une majuscule en anglais : French, Spanish, English.'),
  ],
  summary=[
    ('Affirmation', 'sujet + am/is/are', 'I am happy. / She is here.'),
    ('Contraction', 'I\'m / you\'re / he\'s...', 'I\'m tired. / They\'re ready.'),
    ('Négation', 'am/is/are + not', 'He isn\'t here. / We aren\'t ready.'),
    ('Question', 'Am/Is/Are + sujet?', 'Are you a teacher?'),
    ('Réponse courte', 'Yes, I am. / No, I\'m not.', 'Yes, she is. / No, they aren\'t.'),
    ('Profession', 'I am A + métier', 'I am a student.'),
  ],
  ex1=('Choisis la bonne forme de to be', 'Sélectionne am, is ou are selon le sujet.', [
    ('She ______ a doctor.', ['is', 'am', 'are'], 'is',
     'Avec he/she/it → is : She IS a doctor.'),
    ('They ______ very tired today.', ['are', 'is', 'am'], 'are',
     'Avec they → are : They ARE very tired.'),
    ('______ you from Paris?', ['Are', 'Is', 'Am'], 'Are',
     'Question avec you → Are you...?'),
    ('I ______ not ready yet.', ['am', 'is', 'are'], 'am',
     'Avec I → am : I AM not ready.'),
    ('My brother ______ a student at university.', ['is', 'are', 'am'], 'is',
     'Avec he (my brother) → is : My brother IS a student.'),
    ('We ______ French and we love English!', ['are', 'is', 'am'], 'are',
     'Avec we → are : We ARE French.'),
  ]),
  ex2=('Complète avec am, is, are ou la contraction', 'Écris la forme correcte du verbe to be.', [
    ('My name ______ Sophie and I ______ fifteen years old. (is / am)', 'is / am',
     'My name IS (he/she/it) et I AM (première personne). Deux formes différentes dans la même phrase.'),
    ('______ your parents at home? No, they ______ not. (are / are)', 'are / are',
     'Are your parents...? → question avec they. They are not → négation avec they.'),
    ('This ______ my friend Lucas. He ______ a great footballer. (is / is)', 'is / is',
     'Avec this et he → is dans les deux cas.'),
    ('We ______ in the same class. ______ you in class 3B? (are / are)', 'are / are',
     'We ARE et Are you → are dans les deux cas.'),
    ('It ______ cold today! The windows ______ very cold too. (is / are)', 'is / are',
     'It IS (impersonnel) mais the windows ARE (pluriel).'),
  ]),
  ex3=('Questions et réponses', 'Choisis la phrase correcte.', [
    ('Comment dit-on « Elle est infirmière » en anglais ?', ['She is a nurse.', 'She is nurse.', 'She am a nurse.'], 'She is a nurse.',
     'She + is + article + profession. L\'article « a » est obligatoire en anglais devant une profession.'),
    ('Comment poser la question « Es-tu anglais ? »', ['Are you English?', 'Do you be English?', 'Is you English?'], 'Are you English?',
     'Question avec to be → inversion : Are you...? Jamais de « do » avec to be.'),
    ('Quelle réponse courte est correcte ?', ['Yes, I am.', 'Yes, I\'m.', 'Yes, am.'], 'Yes, I am.',
     'Les réponses courtes affirmatives ne se contractent pas : Yes, I AM (et non « I\'m »).'),
    ('Comment dire « Nous ne sommes pas prêts » ?', ['We are not ready.', 'We not are ready.', 'We don\'t be ready.'], 'We are not ready.',
     'Négation de to be : sujet + are/is/am + NOT. Jamais de « don\'t ».'),
    ('Laquelle est correcte ?', ['They\'re from Spain.', 'They are from spain.', 'There from Spain.'], 'They\'re from Spain.',
     'They\'re (contraction) + majuscule à Spain (nom de pays). « spain » sans majuscule est faux.'),
  ]),
  game_desc='Chaque forme de to be passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('i-am', 'I am', 'je suis — première personne du singulier', 'I\'m', '<b>I am</b> happy today.', 'I ______ happy today. (je suis)', 'am'),
    ('you-are', 'you are', 'tu es / vous êtes — deuxième personne', 'you\'re', '<b>You are</b> very kind.', 'You ______ very kind. (tu es)', 'are'),
    ('he-is', 'he/she/it is', 'il/elle/c\'est — troisième personne singulier', 'he\'s / she\'s', '<b>She is</b> a nurse.', 'She ______ a nurse. (elle est)', 'is'),
    ('we-are', 'we are', 'nous sommes — première personne pluriel', 'we\'re', '<b>We are</b> from France.', 'We ______ from France. (nous sommes)', 'are'),
    ('are-you', 'Are you...?', 'es-tu... ? — question avec you', 'question', '<b>Are you</b> ready?', '______ you ready? (es-tu)', 'are'),
    ('is-not', 'is not / isn\'t', 'n\'est pas — négation troisième personne', 'isn\'t', 'He <b>is not</b> here today.', 'He ______ not here today. (n\'est pas)', 'is'),
    ('are-not', 'are not / aren\'t', 'ne sont pas — négation pluriel', 'aren\'t', 'They <b>are not</b> ready.', 'They ______ not ready. (ne sont pas)', 'are'),
    ('am-a', 'I am a + profession', 'je suis + article + métier — article obligatoire', 'un/une + métier', '<b>I am a</b> student.', 'I am ______ student. (un étudiant)', 'a'),
  ],
),

'pronouns': dict(
  level='a1', section='grammaire', num='Ch. 2', short='Les pronoms sujets',
  title='Les pronoms sujets — I, you, he, she, it, we, they',
  subtitle='Le système des pronoms anglais et ses différences avec le français',
  slides=[
    ('Les pronoms sujets en anglais', None,
     '<p class="slide-explanation">En anglais, le <b>pronom sujet est obligatoire</b> — on ne peut jamais l\'omettre comme en espagnol. Les pronoms anglais sont différents du français sur plusieurs points importants.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I</b> (je) &nbsp;·&nbsp; <b>you</b> (tu / vous) &nbsp;·&nbsp; <b>he</b> (il, masc.) &nbsp;·&nbsp; <b>she</b> (elle, fém.)</p>'
     '<p style="margin-top:8px"><b>it</b> (il/elle — pour les choses) &nbsp;·&nbsp; <b>we</b> (nous) &nbsp;·&nbsp; <b>they</b> (ils/elles)</p></div>'
     '<p style="margin-top:16px"><b>I</b> s\'écrit toujours avec une majuscule, même en milieu de phrase.</p>'),
    ('You : un seul mot pour tu et vous', None,
     '<p class="slide-explanation">L\'anglais n\'a pas de distinction entre <b>tu</b> et <b>vous</b>. Le mot <b>you</b> est utilisé dans toutes les situations — avec un ami, un professeur, un supérieur.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« Tu es mon ami. » → <b>You are</b> my friend.</p>'
     '<p style="margin-top:8px">« Vous êtes professeur. » (formel) → <b>You are</b> a teacher.</p>'
     '<p style="margin-top:8px">« Vous êtes prêts ? » (pluriel) → <b>Are you</b> ready?</p></div>'
     '<p style="margin-top:16px">Le contexte indique si « you » est singulier ou pluriel. Pour insister sur le pluriel, on peut dire <b>you all</b> ou <b>all of you</b>.</p>'),
    ('He, she, it — la distinction choses/personnes', None,
     '<p class="slide-explanation">En français, tous les noms ont un genre (le livre / la table). En anglais, <b>he</b> et <b>she</b> sont réservés aux personnes (et aux animaux familiers). Pour les choses et les animaux inconnus, on utilise <b>it</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Mon livre : « <b>It</b> is very interesting. » — pas « he » ni « he is »</p>'
     '<p style="margin-top:8px">La table : « <b>It</b> is in the kitchen. » — pas « she »</p>'
     '<p style="margin-top:8px">Mon chat (familier) : « <b>He</b> is very funny. » (possible)</p></div>'
     '<p style="margin-top:16px">Le genre grammatical français (<i>le</i>/<i>la</i>) ne détermine <b>pas</b> le choix de he/she/it en anglais.</p>'),
    ('They : ils et elles', None,
     '<p class="slide-explanation">En anglais, <b>they</b> s\'utilise pour les personnes (masculin et féminin confondus) et pour les choses au pluriel. Il n\'y a pas de distinction entre « ils » et « elles ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>They are</b> my friends. (Ils/Elles sont mes amis.)</p>'
     '<p style="margin-top:8px"><b>The books? They are</b> on the table. (Les livres ? Ils sont sur la table.)</p></div>'
     '<p style="margin-top:16px">En anglais moderne, <b>they</b> est aussi utilisé pour une personne dont le genre est inconnu ou non-binaire : « Someone called — <b>they</b> left a message. »</p>'),
    ('Pas de pronoms toniques séparés', None,
     '<p class="slide-explanation">En français, on distingue les pronoms sujets (je, tu) et les pronoms toniques (moi, toi). En anglais A1, il n\'y a qu\'un seul pronom sujet. Les pronoms compléments (me, you, him...) sont différents mais s\'apprennent plus tard.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« C\'est moi. » → <b>It\'s me.</b> (en anglais courant)</p>'
     '<p style="margin-top:8px">« Lui et moi, nous... » → <b>He and I...</b> (sujet) / <b>Him and me...</b> (complément)</p></div>'
     '<p style="margin-top:16px">À noter : avec to be, la langue formelle dit « It is <b>I</b> » mais en pratique courante on dit toujours « It\'s <b>me</b>. »</p>'),
  ],
  traps=[
    ('My book, he is interesting.', 'My book, <strong>it</strong> is interesting.', '« He » et « she » sont réservés aux personnes. Pour les choses, même si le mot français est masculin ou féminin, on utilise « it ».'),
    ('i am happy.', '<strong>I</strong> am happy.', 'Le pronom « I » s\'écrit toujours avec une majuscule en anglais, même au milieu d\'une phrase.'),
    ('You are student.', 'You are <strong>a</strong> student.', 'Les professions demandent un article en anglais : « a student », « a teacher ». Ne pas oublier « a/an ».'),
    ('She and me are friends.', '<strong>She and I</strong> are friends.', 'Comme sujet du verbe, on utilise « I » (et non « me »). « Me » est un pronom complément.'),
    ('They is from Paris.', 'They <strong>are</strong> from Paris.', 'Avec « they », le verbe to be est toujours « are » — jamais « is ».'),
  ],
  summary=[
    ('Singulier', 'I / you / he / she / it', 'I am, you are, he is...'),
    ('Pluriel', 'we / you / they', 'We are, you are, they are...'),
    ('Choses', 'it (pas he ni she)', 'It is a book.'),
    ('Tu et vous', 'you (un seul mot)', 'You are welcome.'),
    ('I majuscule', 'toujours I, jamais i', 'My friend and I are here.'),
    ('Ils et elles', 'they (sans distinction)', 'They are ready.'),
  ],
  ex1=('Choisis le bon pronom sujet', 'Quel pronom remplace le groupe nominal ?', [
    ('Marie is a student. ______ is 18.', ['She', 'He', 'It'], 'She',
     'Marie est une personne féminine → she.'),
    ('The book is great. ______ is very funny.', ['It', 'He', 'She'], 'It',
     'Un livre est une chose → it. Même si le mot français « livre » est masculin, on utilise it en anglais.'),
    ('Tom and Alice are here. ______ are my friends.', ['They', 'It', 'We'], 'They',
     'Deux personnes (Tom et Alice) → they.'),
    ('My sister and ______ are from Lyon.', ['I', 'me', 'we'], 'I',
     'En position de sujet, on utilise « I » (et non « me »). Règle : placer « I » en dernier dans la liste.'),
    ('______ are students in the same class.', ['We', 'Us', 'They'], 'We',
     'Nous = we en position sujet.'),
    ('The chairs? ______ are in the living room.', ['They', 'It', 'She'], 'They',
     'Des choses au pluriel (les chaises) → they.'),
  ]),
  ex2=('Complète avec le bon pronom', 'Écris I, you, he, she, it, we ou they.', [
    ('My brother is 15. ______ is in secondary school.', 'he',
     'Mon frère est masculin → he.'),
    ('Anna and I go to school together. ______ are in the same class.', 'we',
     'Anna et moi (deux personnes incluant moi) → we.'),
    ('Where is my phone? ______ is on the table.', 'it',
     'Un téléphone est une chose → it.'),
    ('My parents are at work. ______ come home at 6.', 'they',
     'Deux personnes au pluriel → they.'),
    ('______ speak French very well, Mrs Brown!', 'you',
     'S\'adresser à quelqu\'un (tu ou vous) → you.'),
  ]),
  ex3=('Choisis la traduction correcte', 'Quelle phrase anglaise correspond à la phrase française ?', [
    ('« Mon vélo est rouge. Il est dans le garage. »', ['My bike is red. It is in the garage.', 'My bike is red. He is in the garage.', 'My bike is red. She is in the garage.'], 'My bike is red. It is in the garage.',
     'Un vélo est une chose → it, même si « vélo » est masculin en français.'),
    ('« Vous êtes prêts ? » (à un groupe)', ['Are you ready?', 'Is you ready?', 'Are they ready?'], 'Are you ready?',
     'Qu\'il s\'agisse d\'une personne ou d\'un groupe, on utilise toujours « you » en anglais.'),
    ('« Sophie et moi sommes amies. »', ['Sophie and I are friends.', 'Sophie and me are friends.', 'Sophie and I is friends.'], 'Sophie and I are friends.',
     '« Sophie et moi » comme sujet → « Sophie and I » + are (pluriel).'),
    ('« Ils sont dans la salle. » (les livres)', ['They are in the room.', 'It are in the room.', 'He is in the room.'], 'They are in the room.',
     'Des choses au pluriel (les livres) → they are.'),
    ('« Tu es très gentil. »', ['You are very kind.', 'He is very kind.', 'I am very kind.'], 'You are very kind.',
     'S\'adresser à quelqu\'un → you are. En anglais il n\'y a pas de distinction tu/vous.'),
  ]),
  game_desc='Chaque pronom sujet passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('i', 'I', 'je — toujours avec majuscule', 'première personne sing.', '<b>I</b> am from France.', '______ am from France. (je)', 'i'),
    ('you', 'you', 'tu / vous — singulier et pluriel', 'deuxième personne', '<b>You</b> are very kind.', '______ are very kind. (tu es)', 'you'),
    ('he', 'he', 'il — pour une personne masculine', 'troisième personne masc.', '<b>He</b> is my brother.', '______ is my brother. (il est)', 'he'),
    ('she', 'she', 'elle — pour une personne féminine', 'troisième personne fém.', '<b>She</b> is a teacher.', '______ is a teacher. (elle est)', 'she'),
    ('it', 'it', 'il/elle — pour une chose ou un animal', 'chose ou animal', '<b>It</b> is a big house.', '______ is a big house. (elle est — pour une maison)', 'it'),
    ('we', 'we', 'nous — première personne pluriel', 'première personne plur.', '<b>We</b> are students.', '______ are students. (nous sommes)', 'we'),
    ('they', 'they', 'ils/elles — personnes et choses au pluriel', 'troisième personne plur.', '<b>They</b> are my friends.', '______ are my friends. (ils sont)', 'they'),
    ('it-thing', 'it (pour les choses)', 'remplace une chose — pas he ni she', 'chose — it', 'The book? <b>It</b> is on the table.', 'The book? ______ is on the table.', 'it'),
  ],
),

'have-got': dict(
  level='a1', section='grammaire', num='Ch. 3', short='Have got',
  title='Have got — j\'ai, tu as, il a...',
  subtitle='Exprimer la possession en anglais et « quel âge as-tu ? »',
  slides=[
    ('Have got : exprimer la possession', None,
     '<p class="slide-explanation"><b>Have got</b> est la façon la plus courante d\'exprimer la possession en anglais britannique A1. Il signifie la même chose que <b>have</b> seul, mais have got est plus fréquent à l\'oral.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I have got</b> (I\'ve got) a dog. — J\'ai un chien.</p>'
     '<p style="margin-top:8px"><b>She has got</b> (She\'s got) a bike. — Elle a un vélo.</p>'
     '<p style="margin-top:8px"><b>They have got</b> (They\'ve got) a big house. — Ils ont une grande maison.</p></div>'
     '<p style="margin-top:16px">Avec <b>he/she/it</b>, on utilise <b>has got</b> (et non « have got »).</p>'),
    ('La conjugaison complète', None,
     '<p class="slide-explanation">Have got change selon le pronom. Attention à la troisième personne du singulier !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I\'ve got</b> &nbsp;·&nbsp; <b>You\'ve got</b> &nbsp;·&nbsp; <b>He\'s/She\'s/It\'s got</b></p>'
     '<p style="margin-top:8px"><b>We\'ve got</b> &nbsp;·&nbsp; <b>You\'ve got</b> &nbsp;·&nbsp; <b>They\'ve got</b></p></div>'
     '<p style="margin-top:16px">La forme longue : <b>I have got</b>, <b>she has got</b>. Les contractions sont plus fréquentes dans la conversation.</p>'),
    ('La négation et la question', None,
     '<p class="slide-explanation">Pour la négation, on ajoute <b>not</b> entre have/has et got. Pour la question, on inverse.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Négation : <b>I haven\'t got</b> a car. / <b>She hasn\'t got</b> a sister.</p>'
     '<p style="margin-top:8px">Question : <b>Have you got</b> a pen? / <b>Has she got</b> a brother?</p>'
     '<p style="margin-top:8px">Réponse : <b>Yes, I have.</b> / <b>No, I haven\'t.</b> — sans « got » dans la réponse courte !</p></div>'),
    ('L\'âge en anglais', None,
     '<p class="slide-explanation">En français on dit « j\'<b>ai</b> 15 ans » (avoir). En anglais, on utilise <b>to be</b> (être) pour l\'âge : <b>I am 15 years old</b> ou simplement <b>I am 15</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« Quel âge as-tu ? » → <b>How old are you?</b></p>'
     '<p style="margin-top:8px">« J\'ai 16 ans. » → <b>I am 16 (years old).</b></p>'
     '<p style="margin-top:8px">« Il a 30 ans. » → <b>He is 30.</b></p></div>'
     '<p style="margin-top:16px">C\'est l\'une des erreurs les plus fréquentes des francophones : <b>ne jamais dire « I have 16 years »</b>.</p>'),
    ('Have got vs have', None,
     '<p class="slide-explanation">En anglais britannique A1, <b>have got</b> et <b>have</b> sont tous les deux corrects pour la possession. L\'américain préfère <b>have</b> seul. À votre niveau, les deux sont acceptés.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Britannique : <b>I\'ve got a car.</b> = Américain : <b>I have a car.</b></p>'
     '<p style="margin-top:8px">Question britannique : <b>Have you got a pen?</b></p>'
     '<p style="margin-top:8px">Question américaine : <b>Do you have a pen?</b></p></div>'
     '<p style="margin-top:16px">Important : avec <b>have</b> seul, la question utilise <b>do/does</b>, pas l\'inversion directe.</p>'),
  ],
  traps=[
    ('I have got a dog (she).', '<strong>She has got</strong> a dog.', 'Avec he/she/it, c\'est « HAS got » — pas « have got ». L\'erreur est très courante.'),
    ('I have 16 years.', 'I <strong>am</strong> 16 years old.', 'L\'âge en anglais utilise TO BE, pas have : « I am 16 ». Jamais « I have 16 years ».'),
    ('Has you got a pen?', '<strong>Have</strong> you got a pen?', 'La question avec « you » utilise « HAVE » (pas has) : Have you got...?'),
    ('Yes, I have got.', 'Yes, I <strong>have</strong>.', 'Dans les réponses courtes, on n\'utilise pas « got » : Yes, I have. / No, I haven\'t.'),
    ('I haven\'t got no friends.', 'I <strong>haven\'t got</strong> any friends.', 'En anglais, on n\'utilise pas deux négations ensemble. « Any » remplace « no » après une négation.'),
  ],
  summary=[
    ('Possession (aff.)', 'have got / has got', 'I\'ve got a cat. She\'s got a car.'),
    ('Possession (nég.)', 'haven\'t got / hasn\'t got', 'He hasn\'t got a bike.'),
    ('Question', 'Have/Has + sujet + got?', 'Have you got a pen?'),
    ('Réponse courte', 'Yes, I have. / No, I haven\'t.', '(pas de « got » dans la réponse)'),
    ('L\'âge', 'I am + nombre (+ years old)', 'I am 15. / How old are you?'),
    ('He/she/it', 'has got (pas have got)', 'She has got / She\'s got'),
  ],
  ex1=('Choisis la bonne forme', 'Have got ou has got ? Fais attention à la personne.', [
    ('My sister ______ a new phone.', ['has got', 'have got', 'is got'], 'has got',
     'My sister = she → HAS got (troisième personne singulier).'),
    ('______ you got a pen I can borrow?', ['Have', 'Has', 'Do'], 'Have',
     'Question avec you → Have you got...?'),
    ('We ______ a lot of homework tonight.', ['have got', 'has got', 'got'], 'have got',
     'We → have got.'),
    ('He ______ any brothers or sisters.', ['hasn\'t got', 'haven\'t got', 'don\'t got'], 'hasn\'t got',
     'He → hasn\'t got (négation troisième personne singulier).'),
    ('How old ______ you?', ['are', 'have', 'is'], 'are',
     'L\'âge utilise to be en anglais : How old ARE you?'),
    ('I ______ two tickets for the concert!', ['have got', 'has got', 'am got'], 'have got',
     'I → have got.'),
  ]),
  ex2=('Complète les phrases', 'Écris la forme correcte de have got ou to be pour l\'âge.', [
    ('My dog ______ big brown eyes. (has got)', 'has got',
     'My dog = it → has got.'),
    ('______ your brother got a car? Yes, he ______ . (have / has)', 'have / has',
     'Question avec your brother → Has your brother got...? Réponse courte → Yes, he HAS.'),
    ('How old ______ your teacher? She ______ about 35. (is / is)', 'is / is',
     'L\'âge → to be. How old IS she? She IS about 35.'),
    ('We ______ any milk. Can you buy some? (haven\'t got)', 'haven\'t got',
     'Négation avec we → haven\'t got.'),
    ('My parents ______ a beautiful garden. (have got)', 'have got',
     'My parents = they → have got.'),
  ]),
  ex3=('Comment traduire ces phrases ?', 'Choisis la meilleure traduction anglaise.', [
    ('« J\'ai un frère et une sœur. »', ['I\'ve got a brother and a sister.', 'I have a brother and a sister. (les deux sont corrects)', 'I\'ve got a brother and a sister. (les deux sont corrects)'], 'I\'ve got a brother and a sister. (les deux sont corrects)',
     'Have got et have sont tous les deux corrects pour la possession en anglais.'),
    ('« Quel âge a-t-il ? »', ['How old is he?', 'How old has he?', 'How many years has he?'], 'How old is he?',
     'L\'âge utilise to be en anglais : How old IS he?'),
    ('« Elle n\'a pas de voiture. »', ['She hasn\'t got a car.', 'She haven\'t got a car.', 'She isn\'t got a car.'], 'She hasn\'t got a car.',
     'She (troisième pers. sing.) → hasn\'t got.'),
    ('« As-tu un animal de compagnie ? »', ['Have you got a pet?', 'Has you got a pet?', 'Do you got a pet?'], 'Have you got a pet?',
     'Question avec you → Have you got...?'),
    ('« J\'ai 14 ans. »', ['I am 14 years old.', 'I have 14 years.', 'I have got 14 years.'], 'I am 14 years old.',
     'L\'âge = to be en anglais. « I have 14 years » est l\'erreur classique des francophones.'),
  ]),
  game_desc='Chaque structure de have got passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('ive-got', 'I\'ve got', 'j\'ai — possession, première personne', 'I have', '<b>I\'ve got</b> a new book.', 'I\'ve ______ a new book. (j\'ai)', 'got'),
    ('shes-got', 'she\'s got', 'elle a — troisième personne féminine', 'she has', '<b>She\'s got</b> two cats.', 'She\'s ______ two cats. (elle a)', 'got'),
    ('havent-got', 'haven\'t got', 'je n\'ai pas — négation avec I/you/we/they', 'have not got', 'I <b>haven\'t got</b> a bike.', 'I ______ got a bike. (je n\'ai pas)', "haven't"),
    ('hasnt-got', 'hasn\'t got', 'il/elle n\'a pas — négation troisième personne', 'has not got', 'He <b>hasn\'t got</b> a sister.', 'He ______ got a sister. (il n\'a pas)', "hasn't"),
    ('have-you-got', 'Have you got?', 'as-tu... ? — question possession', 'Do you have?', '<b>Have you got</b> a pen?', '______ you got a pen? (as-tu)', 'have'),
    ('how-old', 'How old are you?', 'quel âge as-tu ? — to be pour l\'âge', 'age question', '<b>How old are you?</b> I\'m 15.', 'How old ______ you? (quel âge)', 'are'),
    ('i-am-15', 'I am 15', 'j\'ai 15 ans — to be pour l\'âge, jamais have', 'j\'ai X ans = I am X', 'I <b>am</b> 15 years old.', 'I ______ 15 years old. (j\'ai 15 ans)', 'am'),
    ('yes-i-have', 'Yes, I have.', 'oui — réponse courte sans got', 'réponse courte', 'Have you got a pet? Yes, I <b>have</b>.', 'Have you got a pet? Yes, I ______ . (oui)', 'have'),
  ],
),

'articles-basic': dict(
  level='a1', section='grammaire', num='Ch. 4', short='A/an et the',
  title='A/an et the — les articles anglais',
  subtitle='Un/une et le/la/les : comment fonctionnent les articles en anglais',
  slides=[
    ('A et an : l\'article indéfini', None,
     '<p class="slide-explanation"><b>A</b> et <b>an</b> correspondent à « un » et « une » en français. On les utilise devant un nom singulier <b>non spécifique</b> : quelque chose qu\'on mentionne pour la première fois ou quelque chose de général.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>A</b> + consonne : <b>a book</b>, <b>a car</b>, <b>a dog</b></p>'
     '<p style="margin-top:8px"><b>An</b> + voyelle (a, e, i, o, u) : <b>an apple</b>, <b>an egg</b>, <b>an orange</b></p>'
     '<p style="margin-top:8px"><b>An</b> + h muet : <b>an hour</b>, <b>an honest person</b></p></div>'
     '<p style="margin-top:16px">C\'est le <b>son</b> qui compte, pas la lettre : « a university » (car le u se prononce « you »), « an hour » (le h est muet).</p>'),
    ('The : l\'article défini', None,
     '<p class="slide-explanation"><b>The</b> correspond à « le », « la », « les ». On l\'utilise quand on parle de quelque chose de <b>spécifique</b> ou de <b>déjà connu</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Première mention : <b>I have a cat.</b> Deuxième mention : <b>The cat is black.</b></p>'
     '<p style="margin-top:8px">Unique : <b>the sun</b>, <b>the moon</b>, <b>the Eiffel Tower</b></p>'
     '<p style="margin-top:8px">Connu : <b>Pass me the salt, please.</b> (le sel qui est sur la table)</p></div>'
     '<p style="margin-top:16px"><b>The</b> ne change pas selon le genre ou le nombre — toujours <b>the</b>, que le nom soit masculin, féminin, singulier ou pluriel.</p>'),
    ('Quand utiliser a/an ou the ?', None,
     '<p class="slide-explanation">La règle fondamentale : <b>a/an</b> = nouveauté ou généralité ; <b>the</b> = élément déjà identifié ou unique.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« J\'ai vu <b>un film</b>. <b>Le film</b> était super. » → I saw <b>a</b> film. <b>The</b> film was great.</p>'
     '<p style="margin-top:8px">« <b>Le</b> soleil brille. » → <b>The</b> sun is shining. (unique)</p>'
     '<p style="margin-top:8px">« C\'est <b>un</b> médecin. » → She is <b>a</b> doctor. (profession = généralité)</p></div>'),
    ('L\'absence d\'article (Ø)', None,
     '<p class="slide-explanation">En anglais, certains noms ne prennent <b>pas d\'article</b> du tout — ce qu\'on appelle l\'article zéro (Ø). En français, on utilise souvent « du/de la/des » là où l\'anglais n\'a rien.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Noms indénombrables en général : I like <b>Ø music</b>. (J\'aime la musique.)</p>'
     '<p style="margin-top:8px">Noms pluriels en général : <b>Ø Dogs</b> are friendly. (Les chiens sont sympathiques.)</p>'
     '<p style="margin-top:8px">Repas : I have <b>Ø breakfast</b> at 7. / She eats <b>Ø lunch</b> at 12.</p></div>'
     '<p style="margin-top:16px">Attention : « I like <b>the</b> music » = j\'aime cette musique précise (celle qui joue maintenant). « I like <b>Ø</b> music » = j\'aime la musique en général.</p>'),
    ('Articles avec les professions et les lieux', None,
     '<p class="slide-explanation">Règles pratiques pour les professions et les lieux fréquents à l\'A1.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Professions : toujours <b>a/an</b> → <b>a teacher</b>, <b>an engineer</b></p>'
     '<p style="margin-top:8px">Lieux uniques : <b>the</b> → <b>the cinema</b>, <b>the station</b></p>'
     '<p style="margin-top:8px">Pas d\'article : <b>at school</b>, <b>at home</b>, <b>in bed</b>, <b>at work</b></p></div>'
     '<p style="margin-top:16px">« She is at <b>Ø</b> school » (à l\'école, en train d\'étudier) vs « She is at <b>the</b> school » (dans le bâtiment précis).'),
  ],
  traps=[
    ('She is teacher.', 'She is <strong>a</strong> teacher.', 'Les professions prennent toujours l\'article indéfini en anglais : a teacher, an engineer. Le français n\'en a pas besoin.'),
    ('I like the music. (en général)', 'I like <strong>Ø</strong> music.', '« The music » désigne une musique précise. Pour un goût général, pas d\'article en anglais.'),
    ('I have a umbrella.', 'I have <strong>an</strong> umbrella.', '« Umbrella » commence par une voyelle → an umbrella. C\'est le son qui détermine a ou an.'),
    ('The dogs are friendly. (en général)', '<strong>Ø</strong> Dogs are friendly.', 'Une généralité sur les chiens au pluriel → pas d\'article. « The dogs » désignerait des chiens précis.'),
    ('I go to the school every day. (élève)', 'I go to <strong>Ø</strong> school every day.', '« At school / to school » sans article = activité scolaire. « The school » = le bâtiment physique précis.'),
  ],
  summary=[
    ('Indéfini + consonne', 'a + nom', 'a book, a car, a dog'),
    ('Indéfini + voyelle', 'an + nom', 'an apple, an hour, an egg'),
    ('Défini', 'the + nom (sing. ou plur.)', 'the sun, the books'),
    ('Généralité (plur.)', 'Ø (pas d\'article)', 'Dogs are friendly.'),
    ('Goût général', 'Ø (pas d\'article)', 'I like music.'),
    ('Professions', 'a/an obligatoire', 'She is a nurse.'),
  ],
  ex1=('A, an, the ou Ø ?', 'Choisis le bon article pour chaque phrase.', [
    ('She is ______ engineer.', ['an', 'a', 'the'], 'an',
     '« Engineer » commence par une voyelle → an engineer. Et les professions prennent l\'article indéfini.'),
    ('I love ______ chocolate!', ['Ø', 'the', 'a'], 'Ø',
     'Goût général pour quelque chose d\'indénombrable → pas d\'article.'),
    ('Look at ______ moon tonight — it\'s beautiful.', ['the', 'a', 'Ø'], 'the',
     'La lune est unique → the moon.'),
    ('I saw ______ good film yesterday. ______ film was very exciting.', ['a / the', 'the / a', 'a / a'], 'a / the',
     'Première mention → a film ; deuxième mention (déjà identifié) → the film.'),
    ('______ children love playing outside.', ['Ø', 'The', 'A'], 'Ø',
     'Généralité sur les enfants au pluriel → pas d\'article.'),
    ('Can you pass me ______ salt, please?', ['the', 'a', 'Ø'], 'the',
     'Le sel qui est sur la table — spécifique et connu des deux interlocuteurs → the salt.'),
  ]),
  ex2=('Complète avec a, an, the ou rien (Ø)', 'Écris l\'article qui convient ou laisse vide si aucun article n\'est nécessaire.', [
    ('My dad is ______ architect. He loves ______ architecture. (an / Ø)', 'an / Ø',
     'Profession → an architect (a devant voyelle). Goût général → Ø architecture.'),
    ('I go to ______ bed at 10 pm. (Ø)', 'Ø',
     '« Go to bed » → pas d\'article. Expression figée.'),
    ('______ sun rises in the east. (the)', 'the',
     'Le soleil est unique → the sun.'),
    ('Is there ______ supermarket near here? (a)', 'a',
     'Première mention, singulier, non spécifique → a supermarket.'),
    ('I love ______ animals, especially ______ dog we saw at the park. (Ø / the)', 'Ø / the',
     'Goût général → Ø animals. Chien précis (vu au parc, déjà identifié) → the dog.'),
  ]),
  ex3=('Choisis la phrase correcte', 'Quelle phrase utilise l\'article correctement ?', [
    ('Profession : elle est médecin', ['She is a doctor.', 'She is doctor.', 'She is the doctor.'], 'She is a doctor.',
     'Les professions prennent l\'article indéfini : a doctor, a teacher, an engineer.'),
    ('Goût général : j\'aime les chats', ['I like Ø cats.', 'I like the cats.', 'I like a cats.'], 'I like Ø cats.',
     'Goût général avec nom pluriel → pas d\'article. « I like the cats » désignerait des chats précis.'),
    ('Première mention : j\'ai vu un chien', ['I saw a dog.', 'I saw the dog.', 'I saw dog.'], 'I saw a dog.',
     'Première mention, non spécifique → a dog.'),
    ('Unique : le soleil', ['The sun is very bright today.', 'A sun is very bright today.', 'Sun is very bright today.'], 'The sun is very bright today.',
     'Objet unique dans le monde → the sun.'),
    ('Repas : je prends le petit-déjeuner à 7h', ['I have Ø breakfast at 7.', 'I have the breakfast at 7.', 'I have a breakfast at 7.'], 'I have Ø breakfast at 7.',
     'Les repas en anglais ne prennent pas d\'article dans l\'expression ordinaire : have breakfast, eat lunch, have dinner.'),
  ]),
  game_desc='Chaque usage des articles passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('a-consonant', 'a + consonne', 'article indéfini devant consonne — un/une', 'un/une', 'I have <b>a</b> book.', 'I have ______ book. (un)', 'a'),
    ('an-vowel', 'an + voyelle', 'article indéfini devant voyelle ou h muet', 'un/une (+ voyelle)', 'She ate <b>an</b> apple.', 'She ate ______ apple. (une)', 'an'),
    ('the-specific', 'the', 'article défini — élément connu ou unique', 'le/la/les', '<b>The</b> sun is shining.', '______ sun is shining. (le)', 'the'),
    ('a-profession', 'a/an + profession', 'article obligatoire avec les métiers', 'a teacher, an engineer', 'He is <b>a</b> doctor.', 'He is ______ doctor. (un)', 'a'),
    ('zero-general', 'Ø (pluriel général)', 'pas d\'article pour une généralité au pluriel', 'généralité', '<b>Ø</b> Dogs are friendly.', '______ Dogs are friendly. (les chiens en général)', ''),
    ('zero-taste', 'Ø (goût général)', 'pas d\'article avec les indénombrables en général', 'goût général', 'I love <b>Ø</b> music.', 'I love ______ music. (la musique en général)', ''),
    ('first-mention', 'a (première mention)', 'un objet mentionné pour la première fois → a', 'nouveauté', 'I saw <b>a</b> film. The film was great.', 'I saw ______ film. The film was great.', 'a'),
    ('the-unique', 'the (unique)', 'the pour un élément unique au monde', 'le/la (unique)', 'Look at <b>the</b> moon!', 'Look at ______ moon! (la lune)', 'the'),
  ],
),

'nouns-plural': dict(
  level='a1', section='grammaire', num='Ch. 5', short='Le pluriel des noms',
  title='Le pluriel — -s, -es et les irréguliers',
  subtitle='Former le pluriel des noms en anglais : règles et exceptions',
  slides=[
    ('Le pluriel régulier : ajouter -s', None,
     '<p class="slide-explanation">En anglais, la règle de base pour le pluriel est simple : on ajoute <b>-s</b> à la fin du nom. C\'est identique au français pour la majorité des mots.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>book</b> → <b>books</b> &nbsp;·&nbsp; <b>cat</b> → <b>cats</b> &nbsp;·&nbsp; <b>table</b> → <b>tables</b></p>'
     '<p style="margin-top:8px"><b>phone</b> → <b>phones</b> &nbsp;·&nbsp; <b>student</b> → <b>students</b></p></div>'
     '<p style="margin-top:16px">Important : en anglais, le pluriel ne change <b>pas</b> les adjectifs. On dit « big dogs » et non « bigs dogs ». Les adjectifs sont invariables !</p>'),
    ('Le pluriel en -es', None,
     '<p class="slide-explanation">Les noms qui se terminent par <b>-s, -ss, -sh, -ch, -x, -z</b> prennent <b>-es</b> au pluriel. On ajoute une syllabe pour faciliter la prononciation.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>box</b> → <b>boxes</b> &nbsp;·&nbsp; <b>bus</b> → <b>buses</b> &nbsp;·&nbsp; <b>class</b> → <b>classes</b></p>'
     '<p style="margin-top:8px"><b>beach</b> → <b>beaches</b> &nbsp;·&nbsp; <b>dish</b> → <b>dishes</b></p></div>'
     '<p style="margin-top:16px">Astuce : si tu dois prononcer deux consonnes difficiles ensemble, il faut probablement ajouter <b>-es</b>.</p>'),
    ('Le pluriel en -ies', None,
     '<p class="slide-explanation">Les noms qui se terminent par <b>consonne + y</b> changent le <b>y</b> en <b>i</b> et ajoutent <b>-es</b>. Mais si la lettre avant le y est une voyelle, on ajoute juste <b>-s</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Consonne + y → -ies : <b>city</b> → <b>cities</b>, <b>country</b> → <b>countries</b>, <b>baby</b> → <b>babies</b></p>'
     '<p style="margin-top:8px">Voyelle + y → -ys : <b>day</b> → <b>days</b>, <b>boy</b> → <b>boys</b>, <b>key</b> → <b>keys</b></p></div>'),
    ('Les pluriels irréguliers', None,
     '<p class="slide-explanation">Certains noms très courants ont un pluriel totalement irrégulier — il faut les mémoriser !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>man</b> → <b>men</b> &nbsp;·&nbsp; <b>woman</b> → <b>women</b> &nbsp;·&nbsp; <b>child</b> → <b>children</b></p>'
     '<p style="margin-top:8px"><b>tooth</b> → <b>teeth</b> &nbsp;·&nbsp; <b>foot</b> → <b>feet</b> &nbsp;·&nbsp; <b>mouse</b> → <b>mice</b></p>'
     '<p style="margin-top:8px"><b>person</b> → <b>people</b> &nbsp;·&nbsp; <b>fish</b> → <b>fish</b> (invariable) &nbsp;·&nbsp; <b>sheep</b> → <b>sheep</b></p></div>'),
    ('Noms toujours au pluriel ou toujours singulier', None,
     '<p class="slide-explanation">Certains noms sont toujours au pluriel en anglais (et prennent un verbe pluriel), d\'autres sont toujours singuliers (indénombrables).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Toujours pluriel : <b>trousers</b> (pantalon), <b>glasses</b> (lunettes), <b>scissors</b> (ciseaux)</p>'
     '<p style="margin-top:8px">→ « My trousers <b>are</b> blue. » (pas is)</p>'
     '<p style="margin-top:8px">Indénombrables (jamais de pluriel) : <b>water</b>, <b>music</b>, <b>information</b>, <b>advice</b></p>'
     '<p style="margin-top:8px">→ « <b>Information is</b> important. » (pas « informations are »)</p></div>'),
  ],
  traps=[
    ('childs, mans, womans', '<strong>children, men, women</strong>', 'Ces pluriels sont totalement irréguliers : child → children, man → men, woman → women. Jamais de -s.'),
    ('citys, countrys', '<strong>cities, countries</strong>', 'Consonne + y → changer y en i + es : city → cities, country → countries.'),
    ('My trousers is new.', 'My trousers <strong>are</strong> new.', '« Trousers » est toujours pluriel en anglais → verbe au pluriel : are.'),
    ('informations', '<strong>information</strong> (indénombrable)', '« Information » est indénombrable en anglais — jamais de pluriel. On dit « a piece of information » pour individualiser.'),
    ('two sheeps / two fishs', 'two <strong>sheep</strong> / two <strong>fish</strong>', 'Sheep et fish ont le même forme au singulier et au pluriel : one sheep, two sheep. Pas de -s.'),
  ],
  summary=[
    ('Règle générale', '+ -s', 'books, cats, students'),
    ('-s/-ss/-sh/-ch/-x + es', '+ -es', 'boxes, classes, dishes'),
    ('Consonne + y', 'y → -ies', 'city → cities, baby → babies'),
    ('Voyelle + y', '+ -s', 'day → days, key → keys'),
    ('Irréguliers clés', 'formes à mémoriser', 'men, women, children, teeth, feet'),
    ('Invariables', 'même forme sing./plur.', 'fish, sheep'),
  ],
  ex1=('Choisis le bon pluriel', 'Quelle est la forme plurielle correcte ?', [
    ('box', ['boxes', 'boxs', 'boxies'], 'boxes',
     'Box se termine par -x → pluriel en -es : boxes.'),
    ('child', ['children', 'childs', 'childes'], 'children',
     'Child est un pluriel irrégulier : children. Jamais « childs ».'),
    ('city', ['cities', 'citys', 'cityes'], 'cities',
     'City se termine par consonne + y → on change y en i et on ajoute -es : cities.'),
    ('tooth', ['teeth', 'tooths', 'toothes'], 'teeth',
     'Tooth est un pluriel irrégulier : teeth.'),
    ('day', ['days', 'daies', 'dayes'], 'days',
     'Day se termine par voyelle + y → on ajoute juste -s : days.'),
    ('woman', ['women', 'womans', 'womens'], 'women',
     'Woman est un pluriel irrégulier : women. Ne pas ajouter -s !'),
  ]),
  ex2=('Écris le pluriel', 'Mets le nom entre parenthèses au pluriel.', [
    ('There are three ______ in the room. (man)', 'men',
     'Man → irrégulier : men.'),
    ('I love big ______ . (city)', 'cities',
     'City → consonne + y → cities.'),
    ('Put your ______ in the box, please. (book)', 'books',
     'Book → pluriel régulier : books.'),
    ('The ______ are playing in the park. (child)', 'children',
     'Child → irrégulier : children.'),
    ('She washed all the ______ after dinner. (dish)', 'dishes',
     'Dish se termine par -sh → pluriel en -es : dishes.'),
  ]),
  ex3=('Trouve l\'erreur', 'Quelle phrase est correcte ?', [
    ('Quel est le pluriel correct de « country » ?', ['countries', 'countrys', 'countres'], 'countries',
     'Country → consonne + y → on change y en i et on ajoute -es : countries.'),
    ('Quelle phrase est correcte ?', ['My glasses are on the table.', 'My glasses is on the table.', 'My glass are on the table.'], 'My glasses are on the table.',
     '« Glasses » (lunettes) est toujours pluriel en anglais → ARE.'),
    ('Comment dit-on « deux poissons » ?', ['two fish', 'two fishs', 'two fishes'], 'two fish',
     'Fish est invariable : one fish, two fish. Pas de -s au pluriel.'),
    ('Quel pluriel est correct ?', ['people', 'persons', 'peoples'], 'people',
     'Person → pluriel irrégulier : people. « Persons » est utilisé dans des contextes très formels/juridiques uniquement.'),
    ('Quelle phrase est correcte ?', ['I need some information.', 'I need some informations.', 'I need an information.'], 'I need some information.',
     '« Information » est indénombrable en anglais : pas de pluriel, pas d\'article « a ». On dit « some information » ou « a piece of information ».'),
  ]),
  game_desc='Chaque règle de pluriel passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('plural-s', '+ -s (règle générale)', 'pluriel régulier — ajouter s', 'règle générale', 'I have three <b>books</b>.', 'I have three book______ . (ajoute le pluriel)', 's'),
    ('plural-es', '+ -es (-s/-sh/-ch/-x)', 'pluriel des mots terminant par s, sh, ch, x', '+ -es', 'I see two <b>boxes</b>.', 'I see two box______ . (pluriel)', 'es'),
    ('plural-ies', 'y → -ies', 'consonne + y → changer en -ies', 'cities, babies', 'There are many <b>cities</b> in France.', 'There are many cit______ in France. (pluriel)', 'ies'),
    ('irregular-men', 'man → men', 'pluriel irrégulier — sans s', 'irrégulier', 'The <b>men</b> are in the office.', 'The ______ are in the office. (hommes, pluriel)', 'men'),
    ('irregular-children', 'child → children', 'pluriel irrégulier très courant', 'irrégulier', 'The <b>children</b> are playing.', 'The ______ are playing. (enfants, pluriel)', 'children'),
    ('irregular-teeth', 'tooth → teeth', 'pluriel irrégulier — dents', 'irrégulier', 'Brush your <b>teeth</b> every day.', 'Brush your ______ every day. (dents)', 'teeth'),
    ('invariable-fish', 'fish → fish', 'invariable — même forme sing. et plur.', 'invariable', 'I caught three <b>fish</b> today.', 'I caught three ______ today. (poissons)', 'fish'),
    ('uncountable-info', 'information (Ø pluriel)', 'indénombrable — jamais de pluriel', 'indénombrable', 'The <b>information</b> is very useful.', 'The ______ is very useful. (l\'information)', 'information'),
  ],
),

}
