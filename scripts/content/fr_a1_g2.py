# -*- coding: utf-8 -*-
"""fr/ A1 grammaire — lot 2 (chapitres 6-10). Explications en français, anglais cible."""

CHAPTERS = {

'demonstratives': dict(
  level='a1', section='grammaire', num='Ch. 6', short='Les démonstratifs',
  title='Les démonstratifs — this, that, these, those',
  subtitle='Près ou loin : la distinction que le français ne fait pas',
  slides=[
    ('Ce/cet/cette/ces → four mots en anglais', None,
     '<p class="slide-explanation">Le français a <b>ce/cet/cette/ces</b> pour les démonstratifs. L\'anglais distingue en plus la <b>distance</b> : ce qui est <b>près</b> (this/these) et ce qui est <b>loin</b> (that/those).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>This</b> (singulier, près) &nbsp;·&nbsp; <b>These</b> (pluriel, près)</p>'
     '<p style="margin-top:8px"><b>That</b> (singulier, loin) &nbsp;·&nbsp; <b>Those</b> (pluriel, loin)</p></div>'
     '<p style="margin-top:16px">En français, on peut dire « ce livre-ci » ou « ce livre-là » pour insister — en anglais, la distinction est <b>obligatoire</b> dans tous les cas.</p>'),
    ('This et these : près de moi', None,
     '<p class="slide-explanation"><b>This</b> (singulier) et <b>these</b> (pluriel) indiquent quelque chose ou quelqu\'un de <b>proche</b> — physiquement ou dans le temps.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>This book</b> is mine. (ce livre-ci — dans mes mains)</p>'
     '<p style="margin-top:8px"><b>These shoes</b> are very comfortable. (ces chaussures-ci — que je montre)</p>'
     '<p style="margin-top:8px">Présentations : <b>This is</b> my friend Sophie. (C\'est mon amie Sophie.)</p></div>'
     '<p style="margin-top:16px">Au téléphone : <b>This is</b> Tom. — Je suis Tom. (pour se présenter)</p>'),
    ('That et those : loin de moi', None,
     '<p class="slide-explanation"><b>That</b> (singulier) et <b>those</b> (pluriel) indiquent quelque chose de <b>plus éloigné</b> — physiquement ou dans le temps.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>That house</b> over there is beautiful. (cette maison-là — au loin)</p>'
     '<p style="margin-top:8px"><b>Those people</b> are my neighbours. (ces gens-là — en face)</p>'
     '<p style="margin-top:8px"><b>That was</b> a great film! (c\'était — dans le passé récent)</p></div>'
     '<p style="margin-top:16px"><b>That</b> s\'utilise aussi pour parler d\'un événement passé récent ou de quelque chose qu\'on vient de vivre.</p>'),
    ('This/that comme pronoms', None,
     '<p class="slide-explanation"><b>This</b>, <b>that</b>, <b>these</b> et <b>those</b> peuvent s\'utiliser seuls (sans nom) comme pronoms.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>— What is <b>this</b>? — <b>This is</b> a telescope. (Qu\'est-ce que c\'est ?)</p>'
     '<p style="margin-top:8px">— Are <b>these</b> your keys? — No, <b>those</b> are mine, not <b>these</b>.</p></div>'
     '<p style="margin-top:16px">On peut pointer vers une chose sans répéter son nom : « I like <b>those</b>. » (J\'aime ceux-là.)</p>'),
    ('Résumé du système', None,
     '<p class="slide-explanation">Un tableau simple pour retenir les quatre formes.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Singulier</b>&nbsp;&nbsp;&nbsp;&nbsp;<b>Pluriel</b></p>'
     '<p style="margin-top:8px"><b>Près :</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;this&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;these</p>'
     '<p style="margin-top:8px"><b>Loin :</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;that&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;those</p></div>'
     '<p style="margin-top:16px">Astuce mnémotechnique : <b>this/these</b> contiennent un « s » pour « sur moi » (proche). <b>that/those</b> contiennent « a » pour « au loin ».</p>'),
  ],
  traps=[
    ('These is my books.', '<strong>These are</strong> my books.', '« These » est pluriel → verbe au pluriel : « these ARE ». Ces démonstratifs s\'accordent en nombre.'),
    ('This are my friends. (présentation)', '<strong>These are</strong> my friends.', 'Pour présenter plusieurs personnes → these are my friends. « This are » est incorrect.'),
    ('That shoes are nice.', '<strong>Those shoes</strong> are nice.', '« Shoes » est pluriel → démonstratif pluriel : « those shoes », pas « that shoes ».'),
    ('Ce sont mes amis → This is my friends.', 'This is my friend. / <strong>These are</strong> my friends.', 'Pour un groupe d\'amis, le pluriel s\'impose : These are my friends.'),
    ('This is a nice day (parlant d\'hier)', '<strong>That was</strong> a nice day.', '« That » s\'utilise pour quelque chose dans le passé ou d\'éloigné dans le temps. « This is » = maintenant.'),
  ],
  summary=[
    ('Singulier proche', 'this', 'This book is great.'),
    ('Pluriel proche', 'these', 'These shoes are mine.'),
    ('Singulier éloigné', 'that', 'That house is beautiful.'),
    ('Pluriel éloigné', 'those', 'Those people are kind.'),
    ('Présentation', 'This is...', 'This is my friend Tom.'),
    ('Plusieurs personnes', 'These are...', 'These are my classmates.'),
  ],
  ex1=('This, that, these ou those ?', 'Singulier ou pluriel, près ou loin ?', [
    ('______ is my brother. (il est à côté de moi)', ['This', 'That', 'These'], 'This',
     'Une personne, proche → This is my brother.'),
    ('Can you pass me ______ book over there?', ['that', 'this', 'those'], 'that',
     'Singulier et éloigné (over there) → that book.'),
    ('______ are my friends Maria and Leo.', ['These', 'Those', 'This'], 'These',
     'Plusieurs personnes proches qu\'on présente → These are my friends.'),
    ('Look at ______ clouds — they\'re so dark!', ['those', 'these', 'that'], 'those',
     'Nuages au ciel (loin) au pluriel → those clouds.'),
    ('______ was a fantastic concert! (qu\'on vient de finir)', ['That', 'This', 'Those'], 'That',
     'Événement passé/récent → That was a fantastic concert!'),
    ('______ are my books here on my desk.', ['These', 'Those', 'That'], 'These',
     'Livres sur le bureau (proche), pluriel → These are my books.'),
  ]),
  ex2=('Complète avec le bon démonstratif', 'Écris this, that, these ou those.', [
    ('______ shoes are too small. Can I try ______ ones over there? (these / those)', 'these / those',
     'Chaussures proches (pluriel) → these ; celles qui sont loin → those.'),
    ('— What is ______ ? — ______ is a guitar. (that / that)', 'that / that',
     'Objet éloigné, singulier → that dans les deux cas.'),
    ('______ is my teacher, Mr Davis. (présentation, proche)', 'this',
     'Présentation d\'une personne proche → This is my teacher.'),
    ('______ flowers over there are beautiful. (pluriel, loin)', 'those',
     'Fleurs éloignées, pluriel → those flowers.'),
    ('— Is ______ your bag? — No, ______ is mine over here. (that / this)', 'that / this',
     'Sac loin → that ; sac proche → this.'),
  ]),
  ex3=('Choisis la phrase correcte', 'Quelle traduction est juste ?', [
    ('« Ce sont mes cahiers. » (sur la table devant moi)', ['These are my notebooks.', 'Those are my notebooks.', 'This are my notebooks.'], 'These are my notebooks.',
     'Pluriel, proche → These are. « This are » est incorrect car this est singulier.'),
    ('« Tu vois cette maison là-bas ? »', ['Do you see that house over there?', 'Do you see this house over there?', 'Do you see those house over there?'], 'Do you see that house over there?',
     'Singulier, loin (over there) → that house.'),
    ('« C\'était un bon repas ! »', ['That was a good meal!', 'This is a good meal!', 'These were a good meal!'], 'That was a good meal!',
     'Repas terminé, passé → That was. « This is » = moment présent.'),
    ('« Ces gens sont très sympa. » (au loin)', ['Those people are very nice.', 'These people are very nice.', 'That people are very nice.'], 'Those people are very nice.',
     'Pluriel, éloigné → Those people. « That people » est incorrect car that est singulier.'),
    ('« Bonjour, c\'est Sophie. » (au téléphone)', ['Hi, this is Sophie.', 'Hi, that is Sophie.', 'Hi, I am Sophie.'], 'Hi, this is Sophie.',
     'Pour se présenter au téléphone en anglais → This is + prénom.'),
  ]),
  game_desc='Chaque démonstratif passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('this', 'this', 'ce/cet/cette — singulier, proche', 'singulier proche', '<b>This</b> book is mine.', '______ book is mine. (ce livre-ci)', 'this'),
    ('that', 'that', 'ce/cet/cette — singulier, loin', 'singulier loin', '<b>That</b> house is beautiful.', '______ house is beautiful. (cette maison-là)', 'that'),
    ('these', 'these', 'ces — pluriel, proche', 'pluriel proche', '<b>These</b> are my shoes.', '______ are my shoes. (ces chaussures-ci)', 'these'),
    ('those', 'those', 'ces — pluriel, loin', 'pluriel loin', '<b>Those</b> people are friendly.', '______ people are friendly. (ces gens-là)', 'those'),
    ('this-is', 'This is...', 'c\'est — présentation, singulier', 'présentation', '<b>This is</b> my friend Kate.', '______ ______ my friend Kate. (c\'est)', 'this is'),
    ('these-are', 'These are...', 'ce sont — présentation, pluriel', 'présentation pluriel', '<b>These are</b> my classmates.', '______ ______ my classmates. (ce sont)', 'these are'),
    ('that-was', 'That was...', 'c\'était — événement passé', 'passé récent', '<b>That was</b> a great film!', '______ ______ a great film! (c\'était)', 'that was'),
    ('those-over-there', 'those over there', 'ceux-là / celles-là — loin', 'démonstratif loin plur.', 'I love <b>those</b> over there.', 'I love ______ over there. (ceux-là)', 'those'),
  ],
),

'possessive-adjectives': dict(
  level='a1', section='grammaire', num='Ch. 7', short='Les adjectifs possessifs',
  title='Les adjectifs possessifs — my, your, his, her...',
  subtitle='His et her : le possessif s\'accorde avec le possesseur, pas l\'objet possédé',
  slides=[
    ('Les adjectifs possessifs en anglais', None,
     '<p class="slide-explanation">Les adjectifs possessifs indiquent à qui appartient quelque chose. En anglais, ils ne changent pas selon le nom qui suit — contrairement au français où on dit « mon/ma », « son/sa ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>my</b> (mon/ma/mes) &nbsp;·&nbsp; <b>your</b> (ton/ta/tes ; votre/vos)</p>'
     '<p style="margin-top:8px"><b>his</b> (son/sa/ses — pour un homme) &nbsp;·&nbsp; <b>her</b> (son/sa/ses — pour une femme)</p>'
     '<p style="margin-top:8px"><b>its</b> (son/sa — pour une chose) &nbsp;·&nbsp; <b>our</b> (notre/nos) &nbsp;·&nbsp; <b>their</b> (leur/leurs)</p></div>'),
    ('Le piège classique : his ou her ?', None,
     '<p class="slide-explanation">En français, « son livre » peut appartenir à un homme ou à une femme — le genre de l\'adjectif possessif s\'accorde avec <b>l\'objet possédé</b> (livre = masculin → son). En anglais, c\'est l\'inverse : <b>his</b> ou <b>her</b> s\'accordent avec le <b>possesseur</b> !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>John</b> loves <b>his</b> dog. (son chien — John est masculin → his)</p>'
     '<p style="margin-top:8px"><b>Sophie</b> loves <b>her</b> dog. (son chien — Sophie est féminin → her)</p>'
     '<p style="margin-top:8px">Le mot « dog » ne change rien : c\'est le possesseur qui compte.</p></div>'
     '<p style="margin-top:16px">En français : « Son vélo est rouge. » (on ne sait pas si c\'est un homme ou une femme). En anglais : <b>His bike</b> is red. (homme) / <b>Her bike</b> is red. (femme).</p>'),
    ('Its pour les choses et les animaux', None,
     '<p class="slide-explanation"><b>Its</b> est le possessif pour les choses et les animaux (quand le sexe est inconnu). Attention : <b>its</b> (possessif) ≠ <b>it\'s</b> (= it is).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>The dog wags <b>its</b> tail. (Le chien remue sa queue.)</p>'
     '<p style="margin-top:8px">Paris is famous for <b>its</b> museums. (Paris est célèbre pour ses musées.)</p>'
     '<p style="margin-top:8px">Attention : <b>it\'s</b> cold = it IS cold (contraction !)</p></div>'),
    ('Our, your, their : le pluriel', None,
     '<p class="slide-explanation"><b>Our</b>, <b>your</b> et <b>their</b> sont les possessifs pluriels. Ils ne changent pas selon le nom qui suit — pas de distinction notre/nos, leur/leurs.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Our</b> house is big. (notre maison) / <b>Our</b> books are here. (nos livres)</p>'
     '<p style="margin-top:8px"><b>Their</b> cat is black. (leur chat) / <b>Their</b> parents are nice. (leurs parents)</p></div>'
     '<p style="margin-top:16px">En anglais, « notre/nos » = toujours <b>our</b> ; « leur/leurs » = toujours <b>their</b>.</p>'),
    ('Les adjectifs possessifs ne prennent pas d\'article', None,
     '<p class="slide-explanation">Important : on n\'utilise <b>jamais</b> l\'article défini « the » avant un adjectif possessif. En français, on dit « ma maison » ou « la maison de Paul ». En anglais, l\'un ou l\'autre — jamais les deux ensemble.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Correct : <b>my house</b>, <b>his car</b>, <b>their dog</b></p>'
     '<p style="margin-top:8px">Incorrect : ~~the my house~~, ~~the his car~~</p></div>'
     '<p style="margin-top:16px">Rappel : les parties du corps utilisent souvent l\'adjectif possessif en anglais là où le français emploie l\'article défini : « She broke <b>her</b> arm. » = Elle s\'est cassé <b>le</b> bras.</p>'),
  ],
  traps=[
    ('Sophie and her book. → Son livre (livre est masc. en fr.)', 'Sophie and <strong>her</strong> book.', '« Her » car Sophie est une femme — le genre de l\'objet (livre) n\'a aucune importance en anglais.'),
    ('It\'s tail is long. (pour le chien)', '<strong>Its</strong> tail is long.', '« Its » (sans apostrophe) = possessif. « It\'s » = it is. Ne pas confondre !'),
    ('The my friend is nice.', '<strong>My</strong> friend is nice.', 'Jamais d\'article before un possessif : « the my » est impossible en anglais.'),
    ('Mark lost her keys.', 'Mark lost <strong>his</strong> keys.', 'Mark est masculin → his. Le genre du possesseur détermine his/her.'),
    ('Our parents, they house is big.', '<strong>Their</strong> house is big.', '« Their » = leur/leurs. « They » est un pronom sujet, pas un possessif.'),
  ],
  summary=[
    ('Singulier (1re/2e pers.)', 'my / your', 'my book, your pen'),
    ('Masculin (3e pers. sing.)', 'his', 'his car, his friend'),
    ('Féminin (3e pers. sing.)', 'her', 'her bag, her sister'),
    ('Chose/animal (3e pers.)', 'its', 'its name, its tail'),
    ('Pluriel (1re/2e/3e)', 'our / your / their', 'our house, their friends'),
    ('Pas d\'article + possessif', 'jamais « the my »', 'my friend (pas the my friend)'),
  ],
  ex1=('Choisis l\'adjectif possessif correct', 'His, her, its, their... ?', [
    ('Tom is reading ______ book.', ['his', 'her', 'its'], 'his',
     'Tom est masculin → his book.'),
    ('Emma loves ______ cat — ______ name is Biscuit.', ['her / its', 'his / its', 'her / her'], 'her / its',
     'Emma → her cat. Le chat (chose) → its name.'),
    ('We forgot ______ umbrellas at home.', ['our', 'their', 'your'], 'our',
     'Nous (we) → our umbrellas.'),
    ('The students left ______ bags in the classroom.', ['their', 'our', 'its'], 'their',
     'Les élèves (they) → their bags.'),
    ('The dog wags ______ tail when it sees me.', ['its', 'his', 'their'], 'its',
     'Chose/animal → its tail.'),
    ('My sister forgot ______ phone at home.', ['her', 'his', 'its'], 'her',
     'Ma sœur est féminine → her phone.'),
  ]),
  ex2=('Complète avec le bon possessif', 'Écris my, your, his, her, its, our ou their.', [
    ('Is this ______ pen, or is it mine? (yours / ton)', 'your',
     'S\'adresser à quelqu\'un → your pen.'),
    ('Paul and Marie love ______ dog. ______ name is Rex. (their / its)', 'their / its',
     'Paul et Marie (they) → their dog. Le chien (chose) → its name.'),
    ('I can\'t find ______ keys. Have you seen them? (my)', 'my',
     'Mes clés → my keys.'),
    ('Sophie broke ______ arm last week. (her)', 'her',
     'Sophie est féminine → her arm. Les parties du corps prennent le possessif en anglais.'),
    ('The school is proud of ______ students. (its)', 'its',
     'The school (institution = chose) → its students.'),
  ]),
  ex3=('Choisis la traduction correcte', 'Quelle phrase anglaise est juste ?', [
    ('« Marc a oublié son manteau. »', ['Marc forgot his coat.', 'Marc forgot her coat.', 'Marc forgot its coat.'], 'Marc forgot his coat.',
     'Marc est masculin → his coat. Le genre de « manteau » (masc. en fr.) n\'a aucun rôle.'),
    ('« Marie a oublié son manteau. »', ['Marie forgot her coat.', 'Marie forgot his coat.', 'Marie forgot its coat.'], 'Marie forgot her coat.',
     'Marie est féminine → her coat. Même objet (manteau), mais possesseur différent → her.'),
    ('« La ville est connue pour ses musées. »', ['The city is known for its museums.', 'The city is known for their museums.', 'The city is known for her museums.'], 'The city is known for its museums.',
     'Une ville est une chose → its museums.'),
    ('« Nos parents sont très sympas. »', ['Our parents are very nice.', 'Their parents are very nice.', 'We parents are very nice.'], 'Our parents are very nice.',
     'Nous (we) → our parents.'),
    ('Laquelle est correcte ?', ['Her name is Anna.', 'The her name is Anna.', 'She name is Anna.'], 'Her name is Anna.',
     'Adjectif possessif sans article : Her name (pas « the her name »). « She » est un pronom, pas un possessif.'),
  ]),
  game_desc='Chaque adjectif possessif passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('my', 'my', 'mon/ma/mes — première personne singulier', 'mon/ma', 'I love <b>my</b> dog.', 'I love ______ dog. (mon)', 'my'),
    ('your', 'your', 'ton/ta/tes ou votre/vos', 'ton/votre', 'Is this <b>your</b> pen?', 'Is this ______ pen? (ton)', 'your'),
    ('his', 'his', 'son/sa/ses — possesseur masculin', 'possesseur masc.', '<b>His</b> car is red.', '______ car is red. (sa voiture — à lui)', 'his'),
    ('her', 'her', 'son/sa/ses — possesseur féminin', 'possesseur fém.', '<b>Her</b> bag is blue.', '______ bag is blue. (son sac — à elle)', 'her'),
    ('its', 'its', 'son/sa — chose ou animal', 'chose/animal', 'The cat drinks <b>its</b> milk.', 'The cat drinks ______ milk. (son lait — du chat)', 'its'),
    ('our', 'our', 'notre/nos — première personne pluriel', 'notre/nos', '<b>Our</b> house is near the park.', '______ house is near the park. (notre)', 'our'),
    ('their', 'their', 'leur/leurs — troisième personne pluriel', 'leur/leurs', '<b>Their</b> parents are teachers.', '______ parents are teachers. (leurs)', 'their'),
    ('his-her-contrast', 'his vs her', 's\'accorde avec le possesseur, pas l\'objet', 'possesseur = clé', 'Tom has <b>his</b> book. / Anna has <b>her</b> book.', 'Tom has ______ book. Anna has ______ book. (son — à lui / elle)', 'his'),
  ],
),

'possessives': dict(
  level='a1', section='grammaire', num='Ch. 8', short='Le génitif saxon',
  title='Le génitif saxon — \'s et of',
  subtitle='John\'s car ou the car of John : comment exprimer la possession en anglais',
  slides=[
    ('Le génitif saxon : \'s', None,
     '<p class="slide-explanation">En anglais, pour dire que quelque chose appartient à quelqu\'un, on ajoute <b>\'s</b> (apostrophe + s) après le possesseur. C\'est l\'équivalent de « de » en français, mais l\'ordre est inversé.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« La voiture de Jean » → <b>Jean\'s car</b> (Jean + \'s + objet possédé)</p>'
     '<p style="margin-top:8px">« La chambre de Sophie » → <b>Sophie\'s room</b></p>'
     '<p style="margin-top:8px">« Le chien de mes parents » → <b>my parents\'</b> dog</p></div>'
     '<p style="margin-top:16px">Règle d\'or : en anglais, le <b>possesseur passe en premier</b>, puis l\'objet. En français, c\'est l\'inverse.</p>'),
    ('\'s pour les singuliers', None,
     '<p class="slide-explanation">Pour un possesseur singulier, on ajoute toujours <b>\'s</b> (apostrophe + s) après le nom.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Tom\'s</b> bike is new. (Le vélo de Tom est neuf.)</p>'
     '<p style="margin-top:8px"><b>My sister\'s</b> room is upstairs. (La chambre de ma sœur est en haut.)</p>'
     '<p style="margin-top:8px"><b>The dog\'s</b> name is Rex. (Le nom du chien est Rex.)</p></div>'
     '<p style="margin-top:16px">Même si le nom se termine déjà par s : <b>James\'s</b> book ou <b>James\'</b> book (les deux sont acceptés).</p>'),
    ('L\'apostrophe seule pour les pluriels en -s', None,
     '<p class="slide-explanation">Quand le possesseur est au pluriel et se termine par <b>-s</b>, on ajoute <b>seulement l\'apostrophe</b> (pas de -s supplémentaire).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Singulier : <b>my friend\'s</b> house (la maison de mon ami)</p>'
     '<p style="margin-top:8px">Pluriel : <b>my friends\'</b> house (la maison de mes amis)</p>'
     '<p style="margin-top:8px"><b>the students\'</b> work (le travail des étudiants)</p></div>'
     '<p style="margin-top:16px">Pour les pluriels irréguliers (qui ne finissent pas par -s), on remet <b>\'s</b> : <b>the children\'s</b> room.</p>'),
    ('Of pour les choses', None,
     '<p class="slide-explanation">Pour les <b>choses</b> (pas des personnes), on utilise plus souvent <b>of</b> que le génitif \'s. Les deux peuvent exister, mais « of » est plus naturel avec les objets inanimés.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Le titre du livre → <b>the title of the book</b> (plus naturel que « the book\'s title »)</p>'
     '<p style="margin-top:8px">La fin du film → <b>the end of the film</b></p>'
     '<p style="margin-top:8px">La capitale de la France → <b>the capital of France</b></p></div>'
     '<p style="margin-top:16px">Cependant, pour les pays, organisations ou institutions, le \'s est souvent possible : <b>France\'s capital</b>, <b>the company\'s name</b>.</p>'),
    ('\'s vs it\'s : ne pas confondre', None,
     '<p class="slide-explanation">Attention à la confusion fréquente entre <b>\'s</b> de possession et <b>\'s</b> de contraction (= is ou has).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Tom\'s</b> car is red. → Tom\'s = appartient à Tom (possession)</p>'
     '<p style="margin-top:8px"><b>Tom\'s</b> very happy. → Tom\'s = Tom is (contraction)</p>'
     '<p style="margin-top:8px">Le contexte permet toujours de distinguer : nom après → possession ; adjectif/verbe après → contraction.</p></div>'),
  ],
  traps=[
    ('The car of John.', '<strong>John\'s car.</strong>', 'Pour les personnes, le génitif \'s est bien plus naturel en anglais : John\'s car. « The car of John » est grammaticalement possible mais très rare et formel.'),
    ('The book\'s title. (chose)', 'The <strong>title of the book</strong>.', 'Pour les objets inanimés, « of » est préférable : the title of the book, the end of the film.'),
    ('The students\'s work.', 'The <strong>students\'</strong> work.', 'Pour un pluriel en -s, on ajoute seulement l\'apostrophe : students\' (pas d\'autre -s).'),
    ('Sophie\'s is my friend.', 'Sophie <strong>is</strong> my friend.', '\'s ne s\'utilise que pour la possession devant un nom. « Sophie\'s is my friend » est incorrect — on ne peut pas l\'utiliser seul.'),
    ('My sister room is big.', 'My <strong>sister\'s</strong> room is big.', 'Pour exprimer la possession, il faut l\'apostrophe : sister\'s room. Sans \'s, la phrase n\'a pas de sens.'),
  ],
  summary=[
    ('Possession (personne sing.)', 'possesseur + \'s + objet', 'Tom\'s car / my sister\'s room'),
    ('Possession (pluriel en -s)', 'possesseur + \' + objet', 'my friends\' house'),
    ('Pluriel irrégulier', 'possesseur + \'s + objet', 'the children\'s toys'),
    ('Possession (chose)', 'the + objet + of + chose', 'the end of the film'),
    ('Order (ordre)', 'possesseur → objet', 'Paul\'s bike (pas « the bike of Paul »)'),
    ('\'s = is aussi !', 'Tom\'s = Tom is (contraction)', 'Tom\'s very happy. (= Tom is)'),
  ],
  ex1=('Choisis la forme possessive correcte', 'Génitif ou of ?', [
    ('The ______ name is Bella. (chien)', ['dog\'s', 'dog of', 'of dog'], 'dog\'s',
     'On peut utiliser \'s pour les animaux : the dog\'s name.'),
    ('I love ______ films. (Spielberg — personne)', ['Spielberg\'s', 'the films of Spielberg', 'Spielbergs'], 'Spielberg\'s',
     'Pour une personne → génitif \'s : Spielberg\'s films.'),
    ('What is ______ ? (fin du chapitre — chose)', ['the end of the chapter', 'the chapter\'s end', 'the end the chapter'], 'the end of the chapter',
     'Pour une chose abstraite/objet → of est plus naturel : the end of the chapter.'),
    ('That is ______ bag. (Anna — sing.)', ['Anna\'s', 'Annas\'', 'of Anna'], 'Anna\'s',
     'Personne singulière → Anna\'s bag.'),
    ('Where is ______ room? (les enfants — plur. irrég.)', ['the children\'s', 'the childrens\'', 'the children of'], 'the children\'s',
     'Children est un pluriel irrégulier (pas de -s) → children\'s room.'),
    ('______ work is excellent. (les étudiants — plur.)', ['The students\'', 'The student\'s', 'The students\'s'], 'The students\'',
     'Pluriel régulier (students) → apostrophe seule : students\'.'),
  ]),
  ex2=('Réécris en utilisant le génitif \'s', 'Transforme la phrase selon le modèle.', [
    ('The room of my brother → ______', 'my brother\'s room',
     'Personne singulière → my brother\'s room. L\'ordre s\'inverse par rapport au français.'),
    ('The toys of the children → ______', 'the children\'s toys',
     'Pluriel irrégulier (children) → the children\'s toys.'),
    ('The car of my parents → ______', 'my parents\' car',
     'Pluriel régulier (parents) → apostrophe seule : my parents\' car.'),
    ('The name of the teacher → ______', 'the teacher\'s name',
     'Pour une personne, \'s est plus naturel que « of ».'),
    ('The cat of Sophie → ______', 'Sophie\'s cat',
     'Personne singulière → Sophie\'s cat.'),
  ]),
  ex3=('Repère l\'erreur ou choisis la bonne phrase', 'Quelle option est correcte ?', [
    ('Possession d\'une personne singulière', ['Paul\'s book', 'the book of Paul', 'Pauls book'], 'Paul\'s book',
     'Pour une personne, le génitif \'s est naturel et courant : Paul\'s book.'),
    ('Laquelle est correcte pour « la fin du film » ?', ['the end of the film', 'the film\'s end', 'the end the film'], 'the end of the film',
     'Pour un objet inanimé → « of » est préférable : the end of the film.'),
    ('Laquelle est correcte pour les amis au pluriel ?', ['my friends\' house', 'my friends\'s house', 'my friends house'], 'my friends\' house',
     'Pluriel en -s → apostrophe seule : friends\'.'),
    ('Quelle phrase exprime « le livre de Sophie » ?', ['Sophie\'s book', 'Sophie\'s is a book', 'the Sophie book'], 'Sophie\'s book',
     'Sophie\'s + objet possédé = possessif standard.'),
    ('Quelle phrase signifie « Tom is happy » ?', ['Tom\'s happy.', 'Tom\'s book is here.', 'Tom is happy.'], 'Tom\'s happy.',
     'Tom\'s (suivi d\'un adjectif) = Tom is. Tom\'s book (suivi d\'un nom) = appartient à Tom.'),
  ]),
  game_desc='Chaque structure possessive passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('genitive-s', '\'s (singulier)', 'génitif saxon — possesseur singulier', 'la voiture de + \'s', '<b>Tom\'s</b> bike is fast.', '______ bike is fast. (le vélo de Tom)', "tom's"),
    ('plural-apost', '\' (pluriel en -s)', 'pluriel → apostrophe seule', 'les livres de + \'', 'Those are <b>my friends\'</b> books.', 'Those are my friends______ books. (apostrophe)', "'"),
    ('irregular-plural-s', '\'s (pluriel irrégulier)', 'pluriels sans -s reprennent \'s', 'enfants, hommes...', 'I love <b>the children\'s</b> drawings.', 'I love the children______ drawings.', "'s"),
    ('of-things', 'of (pour les choses)', 'la fin de / le titre de — objets inanimés', 'of + chose', 'I love <b>the end of</b> the film.', 'I love the end ______ the film. (de)', 'of'),
    ('order', 'possesseur + objet', 'l\'ordre s\'inverse par rapport au français', 'ordre inversé', '<b>Sophie\'s room</b> is upstairs.', '______ room is upstairs. (la chambre de Sophie)', "sophie's"),
    ('its-possession', 'its (chose)', 'possession d\'une chose — apostrophe interdite', 'its pas it\'s', 'The dog wags <b>its</b> tail.', 'The dog wags ______ tail. (sa queue)', 'its'),
    ('contraction-vs-possession', '\'s = is ou possession', 'contexte détermine le sens', 'contraction vs possession', '<b>Tom\'s</b> happy today.', 'Tom______ happy today. (= Tom is)', "'s"),
    ('of-capital', 'the capital of France', 'structure of pour les pays/lieux', 'capitale de', '<b>The capital of</b> France is Paris.', 'The capital ______ France is Paris. (de)', 'of'),
  ],
),

'can-basic': dict(
  level='a1', section='grammaire', num='Ch. 9', short='Can : capacité',
  title='Can — la capacité et l\'autorisation',
  subtitle='Je peux, tu peux, il peut... Can est invariable en anglais',
  slides=[
    ('Can : le modal de base', None,
     '<p class="slide-explanation"><b>Can</b> est un <b>modal</b> — un verbe auxiliaire spécial qui exprime la capacité ou l\'autorisation. Il ne se conjugue pas : même forme pour toutes les personnes, et jamais de -s à la troisième personne.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I can</b> swim. / <b>You can</b> swim. / <b>She can</b> swim. (jamais « she cans »)</p>'
     '<p style="margin-top:8px"><b>We can</b> swim. / <b>They can</b> swim.</p></div>'
     '<p style="margin-top:16px">Comparaison avec le français : « je peux, tu peux, il peut, nous pouvons... » — en anglais, <b>can</b> ne change jamais de forme.</p>'),
    ('Can + infinitif sans to', None,
     '<p class="slide-explanation">Après <b>can</b>, le verbe qui suit est à l\'infinitif <b>sans to</b>. C\'est une règle absolue des modaux.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I can speak</b> French. (Je parle français.) — pas « I can to speak »</p>'
     '<p style="margin-top:8px"><b>She can play</b> the guitar. — jamais « she can plays »</p>'
     '<p style="margin-top:8px"><b>They can come</b> tomorrow. — jamais « they can to come »</p></div>'
     '<p style="margin-top:16px">Règle : modal → base verbale (pas d\'infinitif avec to, pas de conjugaison).</p>'),
    ('La négation : cannot / can\'t', None,
     '<p class="slide-explanation">La négation de can est <b>cannot</b> (forme longue) ou <b>can\'t</b> (contraction). Pas de « do » nécessaire !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I can\'t</b> drive. (Je ne sais pas conduire.)</p>'
     '<p style="margin-top:8px"><b>She can\'t</b> come tonight. (Elle ne peut pas venir ce soir.)</p>'
     '<p style="margin-top:8px"><b>We cannot</b> enter without a ticket. (Nous ne pouvons pas entrer sans billet.)</p></div>'
     '<p style="margin-top:16px">Cannot s\'écrit en un seul mot — jamais « can not » avec un espace, sauf pour insister.</p>'),
    ('La question : Can + sujet ?', None,
     '<p class="slide-explanation">Pour poser une question avec can, on inverse simplement can et le sujet. Pas de « do » !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Can you</b> swim? — Sais-tu nager ?</p>'
     '<p style="margin-top:8px"><b>Can she</b> play the piano? — Sait-elle jouer du piano ?</p>'
     '<p style="margin-top:8px">Réponse courte : <b>Yes, I can.</b> / <b>No, I can\'t.</b></p></div>'
     '<p style="margin-top:16px">La question avec can est aussi utilisée pour des demandes polies : <b>Can you help me, please?</b></p>'),
    ('Can pour l\'autorisation', None,
     '<p class="slide-explanation"><b>Can</b> peut aussi exprimer l\'autorisation (permission) — similaire à « avoir le droit de » en français.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You can use</b> my pen. (Tu peux utiliser mon stylo. / Tu as le droit.)</p>'
     '<p style="margin-top:8px"><b>Can I sit</b> here? (Est-ce que je peux m\'asseoir ici ?)</p>'
     '<p style="margin-top:8px"><b>You can\'t park</b> here. (Vous ne pouvez pas garer ici.)</p></div>'
     '<p style="margin-top:16px">Plus poli : <b>Could I...?</b> (Pourrais-je... ?) — mais à l\'A1, can suffit pour l\'autorisation.</p>'),
  ],
  traps=[
    ('She cans speak English.', 'She <strong>can</strong> speak English.', 'Can est un modal : jamais de -s à la troisième personne singulier. Toujours « can », pas « cans ».'),
    ('I can to swim.', 'I can <strong>swim</strong>.', 'Après can, l\'infinitif est sans « to » : I can swim (jamais « can to swim »).'),
    ('Do you can help me?', '<strong>Can</strong> you help me?', 'Avec les modaux, pas de « do » pour la question : on inverse directement can et le sujet.'),
    ('Can not (deux mots)', '<strong>Cannot</strong> (un mot) ou <strong>can\'t</strong> (contraction)', '« Cannot » s\'écrit toujours en un seul mot. « Can not » (séparé) n\'est utilisé que pour un contraste très fort.'),
    ('I can swimming.', 'I can <strong>swim</strong>.', 'Après can → base verbale (infinitif court). Jamais de -ing.'),
  ],
  summary=[
    ('Capacité', 'can + base verbale', 'I can swim. / She can drive.'),
    ('Autorisation', 'can + base verbale', 'You can go now.'),
    ('Négation', 'cannot / can\'t + base verbale', 'I can\'t come. / We cannot enter.'),
    ('Question', 'Can + sujet + base verbale?', 'Can you help me?'),
    ('Réponse courte', 'Yes, I can. / No, I can\'t.', '(sans répéter le verbe)'),
    ('Invariable !', 'jamais de -s ni de to', 'She can (pas cans) / can swim (pas to swim)'),
  ],
  ex1=('Choisis la forme correcte avec can', 'Attention à l\'infinitif sans to et à l\'absence de -s.', [
    ('My brother ______ play the guitar very well.', ['can', 'cans', 'can to'], 'can',
     'Can est invariable : jamais de -s, même à la troisième personne.'),
    ('______ you speak Spanish?', ['Can', 'Do can', 'Are'], 'Can',
     'Question avec can → Can + sujet (inversion directe, pas de do).'),
    ('I ______ find my keys — have you seen them?', ['can\'t', 'don\'t can', 'cannot to'], 'can\'t',
     'Négation de can → can\'t (ou cannot). Jamais de « don\'t can ».'),
    ('She ______ very well in the dark.', ['can see', 'can sees', 'can to see'], 'can see',
     'Can + base verbale (sans to, sans -s) : can see.'),
    ('______ I borrow your pen, please?', ['Can', 'Do', 'Am'], 'Can',
     'Demande de permission → Can I...? (poli à l\'A1)'),
    ('They ______ here — it\'s a no-parking zone.', ['can\'t park', 'don\'t can park', 'can\'t to park'], "can't park",
     'Négation → can\'t + base verbale : can\'t park.'),
  ]),
  ex2=('Complète avec can ou can\'t', 'Écris can ou can\'t selon le sens.', [
    ('I ______ ride a bike — I never learned. (ne sais pas)', "can't",
     'Ne sais pas faire → can\'t ride.'),
    ('______ your sister cook? Yes, she ______ make amazing pasta. (can / can)', 'can / can',
     'Question → Can your sister...? Réponse → Yes, she can.'),
    ('Sorry, I ______ come tonight — I have too much homework. (ne peut pas)', "can't",
     'Impossibilité → can\'t come.'),
    ('______ you open the window, please? It\'s so hot! (peut-tu)', 'Can',
     'Demande polie → Can you...?'),
    ('He ______ speak three languages — French, English and Spanish! (sait)', 'can',
     'Capacité → can speak.'),
  ]),
  ex3=('Choisis la traduction correcte', 'Quelle phrase anglaise correspond ?', [
    ('« Elle sait nager. »', ['She can swim.', 'She cans swim.', 'She can to swim.'], 'She can swim.',
     'Can invariable + base verbale sans to : She can swim.'),
    ('« Peux-tu m\'aider ? »', ['Can you help me?', 'Do you can help me?', 'You can help me?'], 'Can you help me?',
     'Question → Can + sujet. Pas de do avec les modaux.'),
    ('« Je ne sais pas conduire. »', ["I can't drive.", "I don't can drive.", "I can't to drive."], "I can't drive.",
     'Négation → can\'t + base verbale (pas de to, pas de do).'),
    ('« Tu peux utiliser mon stylo. »', ['You can use my pen.', 'You can to use my pen.', 'You cans use my pen.'], 'You can use my pen.',
     'Autorisation → can + base verbale. Invariable, pas de to.'),
    ('« Sait-il jouer de la guitare ? Oui. »', ['Can he play the guitar? Yes, he can.', 'Does he can play guitar? Yes, he does.', 'Can he plays guitar? Yes, he can.'], 'Can he play the guitar? Yes, he can.',
     'Question → Can he play (base verbale, pas de -s). Réponse courte → Yes, he can.'),
  ]),
  game_desc='Chaque usage de can passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('can-ability', 'can (capacité)', 'pouvoir / savoir faire — capacité', 'je sais', 'I <b>can</b> swim very well.', 'I ______ swim very well. (je sais)', 'can'),
    ('can-permission', 'can (autorisation)', 'avoir le droit de — permission', 'autorisation', 'You <b>can</b> use my pen.', 'You ______ use my pen. (tu peux)', 'can'),
    ('cannot', 'cannot / can\'t', 'ne pas pouvoir — négation', 'impossibilité', 'She <b>can\'t</b> come today.', 'She ______ come today. (ne peut pas)', "can't"),
    ('can-question', 'Can you...?', 'peux-tu...? — question avec can', 'question modale', '<b>Can you</b> speak French?', '______ you speak French? (peux-tu)', 'can'),
    ('no-s', 'she can (pas cans)', 'invariable — jamais de -s à la 3e personne', 'modal invariable', 'She <b>can</b> play the piano.', 'She ______ play the piano. (sait — sans s)', 'can'),
    ('no-to', 'can + base (sans to)', 'jamais de to après can', 'modal sans to', 'I can <b>drive</b>.', 'I can ______ . (conduire — sans to)', 'drive'),
    ('yes-i-can', 'Yes, I can.', 'oui — réponse courte affirmative', 'réponse courte', 'Can you swim? Yes, I <b>can</b>.', 'Can you swim? Yes, I ______ . (oui)', 'can'),
    ('can-request', 'Can I...?', 'puis-je...? — demande de permission', 'demande polie', '<b>Can I</b> sit here?', '______ I sit here? (puis-je)', 'can'),
  ],
),

'can-cant': dict(
  level='a1', section='grammaire', num='Ch. 10', short='Can/can\'t',
  title='Can/can\'t — permissions et refus',
  subtitle='Exprimer ce qu\'on a le droit de faire ou pas',
  slides=[
    ('Can pour demander la permission', None,
     '<p class="slide-explanation">En anglais A1, <b>can</b> est l\'outil standard pour demander ou accorder une permission. On l\'utilise autant à l\'école, à la maison qu\'entre amis.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Can I go</b> to the toilet, please? (Puis-je aller aux toilettes ?)</p>'
     '<p style="margin-top:8px"><b>Can we leave</b> early today? (Pouvons-nous partir tôt ?)</p>'
     '<p style="margin-top:8px"><b>Can I have</b> a glass of water? (Puis-je avoir un verre d\'eau ?)</p></div>'
     '<p style="margin-top:16px">Réponses possibles : <b>Yes, you can.</b> / <b>No, you can\'t.</b> / <b>Of course!</b> / <b>Sorry, you can\'t.</b></p>'),
    ('Can pour accorder ou refuser', None,
     '<p class="slide-explanation">Un adulte, un règlement ou un signe peut accorder ou refuser la permission avec <b>can</b> (accorder) ou <b>can\'t</b> (refuser).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You can use</b> your phone during the break. (Tu peux utiliser ton téléphone.)</p>'
     '<p style="margin-top:8px"><b>You can\'t eat</b> in the classroom. (Tu ne peux pas manger en classe.)</p>'
     '<p style="margin-top:8px"><b>You can\'t park</b> here. (Stationnement interdit.)</p></div>'),
    ('Can\'t pour les interdictions', None,
     '<p class="slide-explanation"><b>Can\'t</b> (cannot) exprime une interdiction ou une impossibilité. Il est plus fort que « you don\'t » — il indique que c\'est une règle, pas juste une habitude.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You can\'t smoke</b> in here. (Il est interdit de fumer ici.)</p>'
     '<p style="margin-top:8px"><b>Students can\'t use</b> calculators in the test. (Les élèves ne peuvent pas utiliser de calculatrices.)</p>'
     '<p style="margin-top:8px"><b>We can\'t go</b> out — it\'s raining. (Nous ne pouvons pas sortir.)</p></div>'
     '<p style="margin-top:16px"><b>Cannot</b> (un seul mot) est la forme écrite formelle. <b>Can\'t</b> est la forme parlée courante.</p>'),
    ('Structures utiles avec can', None,
     '<p class="slide-explanation">Voici les structures les plus utiles à l\'A1 pour utiliser can au quotidien.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Can I have...?</b> — Puis-je avoir... ? (commander, demander)</p>'
     '<p style="margin-top:8px"><b>Can you...?</b> — Peux-tu... ? (demande d\'aide)</p>'
     '<p style="margin-top:8px"><b>Can we...?</b> — Pouvons-nous... ?</p>'
     '<p style="margin-top:8px"><b>You can / can\'t...</b> — Tu as / n\'as pas le droit de...</p></div>'),
    ('Can vs must pour les règles', None,
     '<p class="slide-explanation">À l\'A1, il est utile de distinguer <b>can\'t</b> (interdit) et <b>must</b> (obligatoire). Ces deux modaux servent à exprimer des règles.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You can\'t run</b> in the corridor. (C\'est interdit.)</p>'
     '<p style="margin-top:8px"><b>You must wear</b> a helmet. (C\'est obligatoire.)</p>'
     '<p style="margin-top:8px"><b>You can leave</b> now. (C\'est autorisé.)</p></div>'
     '<p style="margin-top:16px"><b>Must</b> sera étudié plus tard — pour l\'instant, retenons que can/can\'t couvre la permission et l\'interdiction.</p>'),
  ],
  traps=[
    ('Can I to go out?', '<strong>Can I go</strong> out?', 'Après can → infinitif sans to. Jamais « can I to go ».'),
    ('You can\'t to smoke here.', 'You <strong>can\'t smoke</strong> here.', 'Can\'t + base verbale (sans to) : can\'t smoke.'),
    ('Do you can come?', '<strong>Can you</strong> come?', 'Avec les modaux, la question se forme par inversion : Can you (pas Do you can).'),
    ('Can I have some water, it is possible?', '<strong>Can I have</strong> some water, please?', '« Can I have...? » est la forme standard pour demander quelque chose. Pas besoin de « it is possible ».'),
    ('You cannot to enter.', 'You <strong>cannot enter</strong>.', 'Cannot + base verbale (sans to) : cannot enter.'),
  ],
  summary=[
    ('Demander permission', 'Can I/we + base verbale?', 'Can I go out? Can we leave?'),
    ('Accorder permission', 'You can + base verbale.', 'You can use my pen.'),
    ('Refuser / interdire', 'You can\'t + base verbale.', 'You can\'t eat here.'),
    ('Règle formelle', 'cannot + base verbale', 'You cannot enter without a ticket.'),
    ('Réponse positive', 'Yes, you can. / Of course!', 'Yes, you can go.'),
    ('Réponse négative', 'No, you can\'t. / Sorry, no.', 'No, you can\'t park here.'),
  ],
  ex1=('Can ou can\'t ?', 'Permission ou interdiction ? Complète avec can ou can\'t.', [
    ('______ I use your phone for a second?', ['Can', 'Can\'t', 'Do'], 'Can',
     'Demande de permission → Can I...?'),
    ('Sorry, you ______ eat in the library.', ['can\'t', 'can', 'cannot to'], "can't",
     'Interdiction → you can\'t eat.'),
    ('______ we leave the class five minutes early today?', ['Can', 'Can\'t', 'Do we'], 'Can',
     'Demande de permission pour un groupe → Can we...?'),
    ('You ______ park here — look at the sign!', ['can\'t', 'can', 'couldn\'t to'], "can't",
     'Interdiction → can\'t park.'),
    ('Of course you ______ sit here — the seat is free!', ['can', 'can\'t', 'can to'], 'can',
     'Autorisation → you can sit.'),
    ('Students ______ use their phones during the exam.', ['can\'t', 'can', 'don\'t can'], "can't",
     'Règle scolaire = interdiction → can\'t use.'),
  ]),
  ex2=('Complète les mini-dialogues', 'Écris la réponse logique.', [
    ('Can I open the window? — Yes, you ______ .', 'can',
     'Réponse affirmative courte → Yes, you CAN.'),
    ('Can we eat in here? — Sorry, you ______ — it\'s a library.', "can't",
     'Réponse négative → Sorry, you CAN\'T.'),
    ('______ I have a menu, please? (au restaurant)', 'Can',
     'Demande polie au restaurant → Can I have...?'),
    ('You ______ talk during the test — it\'s a rule.', "can't",
     'Règle du test → can\'t talk.'),
    ('______ you help me with this exercise? I don\'t understand.', 'Can',
     'Demande d\'aide → Can you help me?'),
  ]),
  ex3=('Choisis la bonne phrase', 'Laquelle exprime correctement l\'idée ?', [
    ('Demander si on peut sortir', ['Can I go out?', 'I can to go out?', 'Do I can go out?'], 'Can I go out?',
     'Demande de permission → Can I + base verbale (sans to).'),
    ('Dire qu\'il est interdit de courir', ['You can\'t run here.', 'You don\'t run here.', 'You can\'t to run here.'], "You can't run here.",
     'Interdiction → can\'t + base verbale (sans to).'),
    ('Accorder la permission de partir', ['You can go now.', 'You can to go now.', 'You cans go now.'], 'You can go now.',
     'Autorisation → can + base verbale. Can invariable, pas de to.'),
    ('Répondre non à « Can I sit here? »', ['No, you can\'t.', 'No, you cannot to.', 'No, you don\'t can.'], "No, you can't.",
     'Refus → No, you can\'t. Réponse courte standard.'),
    ('Dire qu\'une règle interdit quelque chose', ['Students cannot use phones in class.', 'Students can\'t to use phones in class.', 'Students don\'t can use phones in class.'], 'Students cannot use phones in class.',
     'Interdiction formelle → cannot + base verbale (un seul mot, sans to).'),
  ]),
  game_desc='Chaque usage de can/can\'t passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('can-i', 'Can I...?', 'puis-je...? — demande de permission', 'demande de permission', '<b>Can I</b> go to the toilet?', '______ I go to the toilet? (puis-je)', 'can'),
    ('can-you-request', 'Can you...?', 'peux-tu...? — demande d\'aide', 'demande d\'aide', '<b>Can you</b> help me, please?', '______ you help me? (peux-tu)', 'can'),
    ('you-can', 'You can...', 'tu peux — autorisation', 'permission accordée', 'You <b>can</b> use my pen.', 'You ______ use my pen. (tu peux)', 'can'),
    ('you-cant', 'You can\'t...', 'tu ne peux pas — interdiction', 'permission refusée', 'You <b>can\'t</b> eat in the library.', 'You ______ eat in the library. (interdit)', "can't"),
    ('cannot', 'cannot', 'ne peut pas — interdiction formelle écrite', 'interdiction formelle', 'You <b>cannot</b> enter without a ticket.', 'You ______ enter without a ticket. (interdit formellement)', 'cannot'),
    ('yes-you-can', 'Yes, you can.', 'oui, tu peux — réponse positive', 'réponse positive', 'Can I sit here? Yes, you <b>can</b>.', 'Can I sit here? Yes, you ______ . (oui)', 'can'),
    ('no-you-cant', 'No, you can\'t.', 'non, tu ne peux pas — réponse négative', 'réponse négative', 'Can I smoke? No, you <b>can\'t</b>.', 'Can I smoke? No, you ______ . (non)', "can't"),
    ('can-have', 'Can I have...?', 'puis-je avoir...? — commander ou demander', 'demande formelle', '<b>Can I have</b> a coffee, please?', '______ I have a coffee, please? (puis-je avoir)', 'can'),
  ],
),

}
