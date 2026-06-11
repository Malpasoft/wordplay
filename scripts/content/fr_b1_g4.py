# -*- coding: utf-8 -*-
"""fr/ B1 grammaire — lot 4 (4 chapitres)."""

CHAPTERS = {

'question-tags': dict(
  level='b1', section='grammaire', num='Ch. 15', short='Question Tags',
  title='Question Tags — N’est-ce pas ?',
  subtitle='You’re French, aren’t you?',
  slides=[
    ('Un « n’est-ce pas » qui se conjugue', None,
     '<p class="slide-explanation">Là où le français se contente de « n’est-ce pas ? » ou « hein ? », l’anglais reprend l’auxiliaire de la phrase et inverse sa polarité.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You’re French, aren’t you?</b> (Tu es français, n’est-ce pas ?)</p>'
     '<p style="margin-top:8px"><b>She doesn’t smoke, does she?</b> (Elle ne fume pas, si ?)</p></div>'
     '<p style="margin-top:16px">Phrase affirmative → tag négatif ; phrase négative → tag affirmatif.</p>'),
    ('Quel auxiliaire reprendre ?', None,
     '<p class="slide-explanation">On reprend l’auxiliaire présent dans la phrase (be, have, will, can...). S’il n’y en a pas, on utilise <b>do/does/did</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>He can swim, can’t he?</b> · <b>You’ve met her, haven’t you?</b></p>'
     '<p style="margin-top:8px"><b>You like jazz, don’t you?</b> · <b>She left early, didn’t she?</b></p></div>'),
    ('Les cas spéciaux', None,
     '<p class="slide-explanation">Trois bizarreries à connaître.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’m late, aren’t I?</b> (et non « amn’t I »)</p>'
     '<p style="margin-top:8px"><b>Let’s go, shall we?</b></p>'
     '<p style="margin-top:8px"><b>Open the door, will you?</b> (après un impératif)</p></div>'),
    ('Intonation : vraie question ou confirmation ?', None,
     '<p class="slide-explanation">Intonation montante = vraie question (je ne sais pas). Descendante = je cherche juste une confirmation.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You’ve seen this film, haven’t you? ↗</b> (Je ne suis pas sûr.)</p>'
     '<p style="margin-top:8px"><b>Lovely day, isn’t it? ↘</b> (Simple bavardage.)</p></div>'),
    ('Y répondre sans se tromper', None,
     '<p class="slide-explanation">On répond à la réalité, pas au tag : si c’est vrai → yes, si c’est faux → no, quel que soit le sens de la question.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>— You don’t eat meat, do you? — <b>No, I don’t.</b> (C’est exact, je n’en mange pas.)</p>'
     '<p style="margin-top:8px">⚠ Le « si » français n’existe pas : on répond <b>Yes, I do.</b></p></div>'),
  ],
  traps=[
    ('You’re French, isn’t it?', 'You’re French, <strong>aren’t you</strong>?', 'Le tag reprend le sujet et l’auxiliaire de la phrase — « isn’t it » universel n’existe pas.'),
    ('She likes tea, doesn’t it?', 'She likes tea, <strong>doesn’t she</strong>?', 'Le pronom du tag reprend le sujet : she → doesn’t she.'),
    ('You can swim, can you? (phrase affirmative)', 'You can swim, <strong>can’t you</strong>?', 'Affirmatif → tag négatif (et inversement).'),
    ('I’m right, amn’t I?', 'I’m right, <strong>aren’t I</strong>?', 'L’exception : I’m... → aren’t I.'),
    ('— Tu ne viens pas ? — Si ! → Yes... si?', '<strong>Yes, I am.</strong>', 'Pas de « si » en anglais : on répond yes + auxiliaire.'),
  ],
  summary=[
    ('Principe', 'polarité inversée', 'You’re French, aren’t you?'),
    ('Sans auxiliaire', 'do/does/did', 'You like jazz, don’t you?'),
    ('I’m...', 'aren’t I?', 'I’m late, aren’t I?'),
    ('Let’s...', 'shall we?', 'Let’s go, shall we?'),
    ('Impératif', 'will you?', 'Open the door, will you?'),
  ],
  ex1=('Choisis le bon tag', 'Auxiliaire + polarité inversée.', [
    ('You’re Belgian, ______ ?', ["aren't you", "isn't it", "are you"], "aren't you",
     'Be affirmatif avec you → aren’t you. « Isn’t it » ne marche qu’avec it + be.'),
    ('She works in Paris, ______ ?', ["doesn't she", "isn't she", "doesn't it"], "doesn't she",
     'Pas d’auxiliaire visible → does ; sujet she → doesn’t she.'),
    ('They didn’t call, ______ ?', ['did they', "didn't they", 'do they'], 'did they',
     'Phrase négative → tag affirmatif : did they.'),
    ('You can drive, ______ ?', ["can't you", 'can you', "don't you"], "can't you",
     'Modal can affirmatif → can’t you.'),
    ('I’m next, ______ ?', ["aren't I", "amn't I", "am I"], "aren't I",
     'L’exception de be avec I → aren’t I.'),
    ('Let’s have a break, ______ ?', ['shall we', 'will we', "don't we"], 'shall we',
     'Let’s → shall we, toujours.'),
  ]),
  ex2=('Écris le tag', 'Complète avec le tag correct (avec l’apostrophe si besoin).', [
    ('You’ve been to London, ______ you?', "haven't",
     'Have affirmatif → haven’t you.'),
    ('He won’t be late, ______ he?', 'will',
     'Négatif (won’t) → tag affirmatif : will he.'),
    ('Your sister speaks Spanish, ______ she?', "doesn't",
     'Présent simple sans auxiliaire → doesn’t she.'),
    ('We met them last year, ______ we?', "didn't",
     'Prétérit → didn’t we.'),
    ('It’s a lovely day, ______ it?', "isn't",
     'It + be → isn’t it (le seul cas où « isn’t it » est juste !).'),
  ]),
  ex3=('Comprendre et répondre', 'Choisis la bonne option.', [
    ('— You don’t eat meat, do you? — (C’est vrai, tu n’en manges pas.)', ["No, I don't.", "Yes, I don't.", 'Si, I do.'], "No, I don't.",
     'On répond à la réalité : je n’en mange pas → No, I don’t.'),
    ('« Tu ne viens pas ? — Si ! » se traduit :', ['Yes, I am.', 'Si, I am.', 'No, I am.'], 'Yes, I am.',
     'Le « si » de contradiction française = Yes + auxiliaire.'),
    ('Intonation descendante sur le tag =', ['simple recherche de confirmation', 'vraie question', 'surprise'], 'simple recherche de confirmation',
     'Descendante = on bavarde ou on confirme ; montante = vraie question.'),
    ('Après un impératif :', ['Open the window, will you?', 'Open the window, do you?', 'Open the window, shall we?'], 'Open the window, will you?',
     'Impératif → will you (shall we est réservé à let’s).'),
    ('Quelle phrase est correcte ?', ["She has finished, hasn't she?", "She has finished, doesn't she?", "She has finished, isn't she?"], "She has finished, hasn't she?",
     'On reprend l’auxiliaire présent : has → hasn’t she.'),
  ]),
  game_desc='Chaque mécanisme des question tags passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('arent-you', "aren't you?", 'n’est-ce pas — après be affirmatif avec you', 'tag de be', "You're French, <b>aren't you</b>?", "You're French, ______ you?", "aren't"),
    ('dont-you', "don't you?", 'tag du présent simple sans auxiliaire', 'tag avec do', 'You like jazz, <b>don’t you</b>?', 'You like jazz, ______ you?', "don't"),
    ('didnt-she', "didn't she?", 'tag du prétérit', 'tag avec did', 'She left early, <b>didn’t she</b>?', 'She left early, ______ she?', "didn't"),
    ('did-they', 'did they?', 'tag affirmatif après une phrase négative', 'polarité inversée', "They didn't call, <b>did they</b>?", "They didn't call, ______ they?", 'did'),
    ('arent-i', "aren't I?", 'l’exception de I am', 'exception', "I'm late, <b>aren't I</b>?", "I'm late, ______ I?", "aren't"),
    ('shall-we', 'shall we?', 'le tag de let’s', 'tag de let’s', "Let's go, <b>shall we</b>?", "Let's go, ______ we?", 'shall'),
    ('will-you', 'will you?', 'le tag de l’impératif', 'tag de l’impératif', 'Open the door, <b>will you</b>?', 'Open the door, ______ you?', 'will'),
    ('yes-i-do', 'Yes, I do.', 'le « si » français — yes + auxiliaire', 'répondre si', "— You don't like it? — <b>Yes, I do!</b>", "— You don't like it? — Yes, I ______ ! (si !)", 'do'),
  ],
),

'relative-clauses': dict(
  level='b1', section='grammaire', num='Ch. 16', short='Relative Clauses',
  title='Relative Clauses — Who, which, that',
  subtitle='Qui, que, dont, où : relier les phrases',
  slides=[
    ('Qui et que : who, which, that', None,
     '<p class="slide-explanation">Personne → <b>who</b> (ou that). Chose → <b>which</b> (ou that). Pas de distinction qui/que : c’est la fonction qui change tout.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The man who lives next door is a doctor.</b> (L’homme qui habite à côté...)</p>'
     '<p style="margin-top:8px"><b>The film which/that we watched was great.</b> (Le film que nous avons vu...)</p></div>'),
    ('L’anglais adore effacer le relatif', None,
     '<p class="slide-explanation">Quand le relatif est complément (« que »), on peut — et on préfère — le supprimer. Impossible en français, naturel en anglais !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The film we watched was great.</b> (= which we watched)</p>'
     '<p style="margin-top:8px"><b>The girl I met yesterday is Italian.</b> (la fille que j’ai rencontrée)</p></div>'
     '<p style="margin-top:16px">S’il est sujet (« qui »), il reste : The man <b>who</b> lives next door...</p>'),
    ('Whose : dont', None,
     '<p class="slide-explanation"><b>Whose</b> = dont/de qui (possession), suivi directement du nom.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>That’s the woman whose car was stolen.</b> (la femme dont la voiture a été volée)</p></div>'),
    ('Where et when', None,
     '<p class="slide-explanation"><b>Where</b> = où (lieu) ; <b>when</b> = où (temps !). Le français dit « où » dans les deux cas.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The town where I grew up is tiny.</b> (la ville où j’ai grandi)</p>'
     '<p style="margin-top:8px"><b>I remember the day when we met.</b> (le jour où nous nous sommes rencontrés)</p></div>'),
    ('Virgules : deux types de relatives', None,
     '<p class="slide-explanation">Sans virgules : information indispensable. Avec virgules : simple parenthèse — et là, <b>that est interdit</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>My brother who lives in Lyon is a chef.</b> (celui de Lyon — j’en ai plusieurs)</p>'
     '<p style="margin-top:8px"><b>My brother, who lives in Lyon, is a chef.</b> (au passage, il vit à Lyon)</p></div>'),
  ],
  traps=[
    ('The man which lives next door...', 'The man <strong>who</strong> lives next door...', 'Personne → who (ou that), jamais which.'),
    ('The film that we watched it was great.', 'The film that we watched was great.', 'Pas de pronom de rappel : « que nous avons vu », pas « que nous l’avons vu ».'),
    ('The day where we met...', 'The day <strong>when</strong> we met...', 'Le « où » temporel se dit when, pas where.'),
    ('The woman that her car was stolen...', 'The woman <strong>whose</strong> car was stolen...', '« Dont » possessif = whose + nom.'),
    ('My mother, that lives in Nice, ...', 'My mother, <strong>who</strong> lives in Nice, ...', 'Entre virgules, that est interdit : who/which.'),
  ],
  summary=[
    ('Personne (qui/que)', 'who / that', 'the man who lives...'),
    ('Chose (qui/que)', 'which / that', 'the film which we saw'),
    ('« Que » effaçable', '∅ si complément', 'the film we watched'),
    ('Dont', 'whose + nom', 'whose car was stolen'),
    ('Où (lieu/temps)', 'where / when', 'the town where..., the day when...'),
  ],
  ex1=('Choisis le bon relatif', 'Personne, chose, possession, lieu ou temps ?', [
    ('The doctor ______ treated me was very kind.', ['who', 'which', 'whose'], 'who',
     'Personne sujet → who : le médecin qui m’a soigné.'),
    ('The keys ______ were on the table have disappeared.', ['which', 'who', 'whose'], 'which',
     'Chose sujet → which (ou that).'),
    ('That’s the singer ______ album sold millions.', ['whose', 'who', 'which'], 'whose',
     '« Dont l’album » → whose album.'),
    ('The village ______ my grandparents live is beautiful.', ['where', 'which', 'when'], 'where',
     'Lieu où ils vivent → where.'),
    ('I’ll never forget the summer ______ we met.', ['when', 'where', 'which'], 'when',
     '« L’été où » = temps → when.'),
    ('The book ______ you lent me is fascinating.', ['that', 'who', 'whose'], 'that',
     'Chose complément → that/which (ou rien du tout).'),
  ]),
  ex2=('Complète avec le relatif', 'Écris le mot qui manque (ou rien n’est pas proposé ici).', [
    ('The man ______ fixed our roof is retired. (qui)', 'who',
     'Personne sujet → who.'),
    ('The hotel ______ we stayed was right on the beach. (où)', 'where',
     'Lieu → where : l’hôtel où nous avons logé.'),
    ('She’s the friend ______ advice I always trust. (dont les conseils)', 'whose',
     'Possession → whose advice.'),
    ('The day ______ I passed my exam was unforgettable. (où, temporel)', 'when',
     'Jour = temps → when.'),
    ('Everything ______ he said was true. (ce que... → tout ce qu’il a dit)', 'that',
     'Après everything/all, on emploie that : everything that he said.'),
  ]),
  ex3=('Repère la bonne phrase', 'Choisis la version correcte ou la bonne analyse.', [
    ('Quelle phrase est naturelle à l’oral ?', ['The film we watched last night was great.', 'The film what we watched was great.', 'The film who we watched was great.'], 'The film we watched last night was great.',
     'Relatif complément effacé — la tournure la plus naturelle. « What » ne relie jamais deux phrases ainsi.'),
    ('Dans quelle phrase peut-on EFFACER le relatif ?', ['The girl that I met is Italian.', 'The girl that lives here is Italian.', 'The girl whose bag I found...'], 'The girl that I met is Italian.',
     'On efface seulement le relatif complément : the girl I met. Sujet (lives) et whose restent.'),
    ('« Mon frère, qui vit à Lyon, est chef. » (parenthèse)', ['My brother, who lives in Lyon, is a chef.', 'My brother, that lives in Lyon, is a chef.', 'My brother who lives in Lyon is a chef.'], 'My brother, who lives in Lyon, is a chef.',
     'Avec virgules (information accessoire) → who, jamais that.'),
    ('« La ville où je suis né » :', ['the town where I was born', 'the town when I was born', 'the town which I was born'], 'the town where I was born',
     'Lieu → where.'),
    ('Quelle phrase est INCORRECTE ?', ['The car that I bought it last week broke down.', 'The car I bought last week broke down.', 'The car that I bought last week broke down.'], 'The car that I bought it last week broke down.',
     'Pas de pronom de rappel (it) après le relatif.'),
  ]),
  game_desc='Chaque relatif passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('who', 'who', 'qui/que pour une personne', 'relatif personne', 'The man <b>who</b> lives next door is a doctor.', 'The man ______ lives next door is a doctor.', 'who'),
    ('which', 'which', 'qui/que pour une chose', 'relatif chose', 'The film <b>which</b> we watched was great.', 'The film ______ we watched was great.', 'which'),
    ('that-rel', 'that', 'le passe-partout des relatives sans virgules', 'relatif passe-partout', 'The book <b>that</b> you lent me is great.', 'The book ______ you lent me is great.', 'that'),
    ('zero-rel', 'relatif effacé', 'le « que » complément peut disparaître', 'omission', 'The film <b>(that)</b> we watched was great → The film we watched...', 'The girl ______ met yesterday is Italian. (I + relatif effacé)', 'i'),
    ('whose', 'whose', 'dont — possession, suivi du nom', 'dont', "The woman <b>whose</b> car was stolen...", 'The woman ______ car was stolen...', 'whose'),
    ('where-rel', 'where', 'où — pour un lieu', 'où (lieu)', 'The town <b>where</b> I grew up is tiny.', 'The town ______ I grew up is tiny.', 'where'),
    ('when-rel', 'when', 'où — pour un moment (le jour où...)', 'où (temps)', 'I remember the day <b>when</b> we met.', 'I remember the day ______ we met. (où)', 'when'),
    ('no-it', 'pas de pronom de rappel', 'jamais « que je l’ai acheté » : pas de it après le relatif', 'pas de rappel', 'The car that I bought (jamais « bought it ») broke down.', 'The car that I ______ broke down. (ai achetée)', 'bought'),
  ],
),

'ing-form': dict(
  level='b1', section='grammaire', num='Ch. 17', short='The -ing Form',
  title='The -ing Form — Le gérondif anglais',
  subtitle='Swimming is fun : quand le verbe devient nom',
  slides=[
    ('Un verbe qui sert de nom', None,
     '<p class="slide-explanation">La forme en -ing permet d’utiliser un verbe comme un nom — là où le français emploie l’infinitif.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Swimming is good for you.</b> (Nager est bon pour la santé.)</p>'
     '<p style="margin-top:8px"><b>I love reading.</b> (J’adore lire.)</p></div>'
     '<p style="margin-top:16px">Réflexe : un verbe français à l’infinitif en position de nom → -ing en anglais.</p>'),
    ('Après les prépositions : toujours -ing', None,
     '<p class="slide-explanation">Règle d’or : après une préposition (in, for, of, about, without, after, before...), le verbe est TOUJOURS en -ing.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’m interested in learning Japanese.</b></p>'
     '<p style="margin-top:8px"><b>She left without saying goodbye.</b> (sans dire au revoir)</p>'
     '<p style="margin-top:8px"><b>Thanks for coming!</b></p></div>'),
    ('Les verbes suivis de -ing', None,
     '<p class="slide-explanation">Certains verbes appellent -ing : <b>enjoy, finish, avoid, suggest, mind, keep, practise</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I enjoy cooking.</b> (jamais « enjoy to cook »)</p>'
     '<p style="margin-top:8px"><b>He kept talking.</b> (Il a continué à parler.)</p>'
     '<p style="margin-top:8px"><b>Would you mind opening the window?</b></p></div>'),
    ('Le piège to + -ing', None,
     '<p class="slide-explanation">Dans <b>look forward to, be used to, object to</b>, le to est une préposition → -ing derrière !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I look forward to hearing from you.</b> (Dans l’attente de votre réponse — la formule des e-mails !)</p>'
     '<p style="margin-top:8px"><b>I’m used to getting up early.</b> (J’ai l’habitude de me lever tôt.)</p></div>'),
    ('Orthographe du -ing', None,
     '<p class="slide-explanation">Trois règles : e muet tombe (make → making), consonne finale doublée après voyelle brève accentuée (run → running), -ie → -ying (lie → lying).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>write → writing · swim → swimming · die → dying</b></p></div>'),
  ],
  traps=[
    ('Smoke is bad for you. (fumer)', '<strong>Smoking</strong> is bad for you.', 'Le verbe-sujet prend -ing : fumer = smoking, pas smoke.'),
    ('I enjoy to cook.', 'I enjoy <strong>cooking</strong>.', 'Enjoy fait partie des verbes toujours suivis de -ing.'),
    ('She left without to say goodbye.', 'She left without <strong>saying</strong> goodbye.', 'Après une préposition, toujours -ing.'),
    ('I look forward to hear from you.', 'I look forward to <strong>hearing</strong> from you.', 'Ici to est une préposition → hearing. La formule à mémoriser pour les e-mails.'),
    ('run → runing', 'run → <strong>running</strong>', 'Voyelle brève + consonne finale → on double : running, swimming, stopping.'),
  ],
  summary=[
    ('Verbe-nom', '-ing en sujet/complément', 'Swimming is fun.'),
    ('Après préposition', 'toujours -ing', 'without saying goodbye'),
    ('Verbes + -ing', 'enjoy, finish, avoid, mind, keep', 'I enjoy cooking.'),
    ('to préposition', 'look forward to + -ing', 'looking forward to hearing'),
    ('Orthographe', 'making, running, dying', 'write→writing, run→running'),
  ],
  ex1=('Choisis la forme correcte', '-ing ou infinitif ?', [
    ('______ is my favourite hobby.', ['Cooking', 'Cook', 'To cooking'], 'Cooking',
     'Verbe en position de sujet → -ing : Cooking is...'),
    ('I’m thinking about ______ jobs.', ['changing', 'to change', 'change'], 'changing',
     'Après la préposition about → -ing.'),
    ('She avoided ______ my question.', ['answering', 'to answer', 'answer'], 'answering',
     'Avoid + -ing : elle a évité de répondre.'),
    ('Thanks for ______ me!', ['helping', 'to help', 'help'], 'helping',
     'For est une préposition → helping.'),
    ('I look forward to ______ you soon.', ['seeing', 'see', 'will see'], 'seeing',
     'Look forward to + -ing — le to est une préposition.'),
    ('He left the room without ______ a word.', ['saying', 'to say', 'said'], 'saying',
     'Without + -ing : sans dire un mot.'),
  ]),
  ex2=('Écris la forme en -ing', 'Attention à l’orthographe.', [
    ('make → ______ (fabriquer)', 'making',
     'Le e muet tombe : making.'),
    ('swim → ______ (nager)', 'swimming',
     'Voyelle brève + consonne : on double le m : swimming.'),
    ('lie → ______ (mentir / être allongé)', 'lying',
     '-ie devient -ying : lying.'),
    ('I’m used to ______ up early. (get)', 'getting',
     'Be used to + -ing, et get double son t : getting.'),
    ('Would you mind ______ the door? (close)', 'closing',
     'Mind + -ing, e muet tombe : closing.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Fumer est mauvais pour la santé. »', ['Smoking is bad for your health.', 'Smoke is bad for your health.', 'To smoking is bad for your health.'], 'Smoking is bad for your health.',
     'Infinitif français sujet → -ing anglais.'),
    ('« Elle est partie sans payer. »', ['She left without paying.', 'She left without to pay.', 'She left without pay.'], 'She left without paying.',
     'Préposition without → paying.'),
    ('« J’ai l’habitude de travailler le soir. »', ["I'm used to working in the evening.", "I'm used to work in the evening.", 'I used to working in the evening.'], "I'm used to working in the evening.",
     'Be used to + -ing = avoir l’habitude de. (Used to + base = autrefois !)'),
    ('« Dans l’attente de votre réponse... » (e-mail)', ['I look forward to hearing from you.', 'I look forward to hear from you.', 'I look forward hearing you.'], 'I look forward to hearing from you.',
     'La formule de clôture professionnelle — to + hearing.'),
    ('« Continue à pratiquer ! »', ['Keep practising!', 'Keep to practise!', 'Continue practise!'], 'Keep practising!',
     'Keep + -ing = continuer à.'),
  ]),
  game_desc='Chaque emploi du -ing passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('ing-subject', '-ing sujet', 'le verbe-nom en début de phrase — « nager est... »', 'verbe comme sujet', '<b>Swimming</b> is good for you.', '______ is good for you. (nager)', 'swimming'),
    ('prep-ing', 'préposition + -ing', 'après in/for/about/without : toujours -ing', 'après préposition', 'She left without <b>saying</b> goodbye.', 'She left without ______ goodbye. (dire)', 'saying'),
    ('enjoy-ing', 'enjoy + -ing', 'enjoy refuse l’infinitif', 'verbe + -ing', 'I enjoy <b>cooking</b>.', 'I enjoy ______ . (cuisiner)', 'cooking'),
    ('keep-ing', 'keep + -ing', 'continuer à faire', 'continuer à', 'He kept <b>talking</b>.', 'He kept ______ . (à parler)', 'talking'),
    ('mind-ing', 'mind + -ing', 'would you mind — demande polie', 'demande polie', 'Would you mind <b>opening</b> the window?', 'Would you mind ______ the window? (ouvrir)', 'opening'),
    ('look-forward', 'look forward to + -ing', 'dans l’attente de — to est une préposition', 'formule d’e-mail', 'I look forward to <b>hearing</b> from you.', 'I look forward to ______ from you.', 'hearing'),
    ('used-to-ing', 'be used to + -ing', 'avoir l’habitude de', 'habitude', "I'm used to <b>getting</b> up early.", "I'm used to ______ up early.", 'getting'),
    ('double-cons', 'running (orthographe)', 'consonne doublée après voyelle brève', 'orthographe', 'run → <b>running</b>, swim → swimming', 'run → ______', 'running'),
  ],
),

'verb-infinitive-patterns': dict(
  level='b1', section='grammaire', num='Ch. 18', short='Verb Patterns',
  title='Verb Patterns — Infinitif ou -ing ?',
  subtitle='Want to do, enjoy doing : quel verbe appelle quoi ?',
  slides=[
    ('Le problème', None,
     '<p class="slide-explanation">Le français enchaîne deux verbes sans se poser de questions (« je veux partir », « j’aime partir »). L’anglais impose un choix : <b>to + infinitif</b> ou <b>-ing</b>, selon le premier verbe.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I want to leave.</b> · <b>I enjoy leaving early.</b></p></div>'),
    ('Famille « to + infinitif »', None,
     '<p class="slide-explanation"><b>want, decide, hope, plan, promise, learn, offer, refuse, agree, need</b> + to...</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>We decided to move.</b> · <b>She hopes to find a job soon.</b></p>'
     '<p style="margin-top:8px"><b>He promised to help us.</b></p></div>'),
    ('Famille « -ing »', None,
     '<p class="slide-explanation"><b>enjoy, finish, avoid, suggest, mind, keep, practise, imagine, miss</b> + -ing...</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Have you finished eating?</b> · <b>I suggest taking the train.</b></p>'
     '<p style="margin-top:8px"><b>I miss living by the sea.</b> (Ça me manque de vivre près de la mer.)</p></div>'),
    ('Les deux, sans grand changement', None,
     '<p class="slide-explanation"><b>like, love, hate, prefer, start, begin, continue</b> acceptent les deux formes au sens quasi identique.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I love reading. = I love to read.</b></p>'
     '<p style="margin-top:8px">Avec would : toujours to → <b>I’d like to book a table.</b> (jamais « I’d like booking »)</p></div>'),
    ('Les deux, mais le sens change !', None,
     '<p class="slide-explanation"><b>stop, remember, forget, try</b> changent de sens selon la forme.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>He stopped smoking.</b> (Il a arrêté de fumer.) · <b>He stopped to smoke.</b> (Il s’est arrêté pour fumer.)</p>'
     '<p style="margin-top:8px"><b>Remember to lock the door.</b> (Pense à fermer !) · <b>I remember locking it.</b> (Je me souviens de l’avoir fermée.)</p></div>'),
  ],
  traps=[
    ('I want that you come.', 'I want <strong>you to come</strong>.', '« Je veux que tu viennes » → want + personne + to : I want you to come.'),
    ('I enjoy to travel.', 'I enjoy <strong>travelling</strong>.', 'Enjoy appartient à la famille -ing.'),
    ('She decided buying a flat.', 'She decided <strong>to buy</strong> a flat.', 'Decide appartient à la famille to + infinitif.'),
    ('I’d like ordering now.', "I'd like <strong>to order</strong> now.", 'Would like + to + infinitif, toujours.'),
    ('Il a arrêté de fumer → He stopped to smoke.', 'He stopped <strong>smoking</strong>.', 'Stop + -ing = arrêter de ; stop + to = s’arrêter pour.'),
  ],
  summary=[
    ('+ to', 'want, decide, hope, promise...', 'We decided to move.'),
    ('+ -ing', 'enjoy, finish, avoid, suggest...', 'Have you finished eating?'),
    ('Les deux (≈)', 'like, love, start, continue', 'I love reading / to read.'),
    ('would + to', "I'd like to...", "I'd like to book a table."),
    ('Sens change', 'stop, remember, forget, try', 'stopped smoking ≠ stopped to smoke'),
    ('Vouloir que qqn', 'want + personne + to', 'I want you to come.'),
  ],
  ex1=('To ou -ing ?', 'Choisis la forme correcte après chaque verbe.', [
    ('She decided ______ her job.', ['to quit', 'quitting', 'quit'], 'to quit',
     'Decide + to + infinitif.'),
    ('Do you enjoy ______ in the rain?', ['walking', 'to walk', 'walk'], 'walking',
     'Enjoy + -ing.'),
    ('He promised ______ on time.', ['to be', 'being', 'be'], 'to be',
     'Promise + to + infinitif.'),
    ('I suggest ______ a taxi.', ['taking', 'to take', 'take'], 'taking',
     'Suggest + -ing : je suggère de prendre un taxi.'),
    ('Would you like ______ with us?', ['to come', 'coming', 'come'], 'to come',
     'Would like + to, sans exception.'),
    ('Please stop ______ so much noise!', ['making', 'to make', 'make'], 'making',
     'Arrêter de faire → stop + -ing.'),
  ]),
  ex2=('Complète la phrase', 'Écris le verbe entre parenthèses à la bonne forme.', [
    ('I hope ______ you again soon. (see)', 'to see',
     'Hope + to + infinitif : to see.'),
    ('Have you finished ______ ? (eat)', 'eating',
     'Finish + -ing : eating.'),
    ('I want you ______ me the truth. (tell)', 'to tell',
     '« Je veux que tu me dises » → want you to tell.'),
    ('Remember ______ the lights before you leave. (turn off)', 'to turn off',
     'Pense à éteindre → remember + to (l’action est à faire).'),
    ('We should avoid ______ during rush hour. (drive)', 'driving',
     'Avoid + -ing : éviter de conduire.'),
  ]),
  ex3=('Le sens change-t-il ?', 'Choisis la phrase qui correspond au sens demandé.', [
    ('« Il a arrêté de fumer. »', ['He stopped smoking.', 'He stopped to smoke.', 'He stopped the smoke.'], 'He stopped smoking.',
     'Stop + -ing = arrêter une habitude.'),
    ('« Pense à poster la lettre ! »', ['Remember to post the letter!', 'Remember posting the letter!', 'Remind to post the letter!'], 'Remember to post the letter!',
     'Action encore à faire → remember + to.'),
    ('« Je me souviens d’avoir fermé la porte. »', ['I remember locking the door.', 'I remember to lock the door.', 'I remind locking the door.'], 'I remember locking the door.',
     'Souvenir d’une action passée → remember + -ing.'),
    ('« Je veux que tu m’aides. »', ['I want you to help me.', 'I want that you help me.', 'I want you helping me.'], 'I want you to help me.',
     'Pas de « that » après want : want + personne + to.'),
    ('« Ça me manque de vivre à Paris. »', ['I miss living in Paris.', 'I miss to live in Paris.', 'Living in Paris misses me.'], 'I miss living in Paris.',
     'Miss + -ing, et c’est moi le sujet — contrairement à « ça me manque ».'),
  ]),
  game_desc='Chaque construction passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('want-to', 'want to', 'vouloir faire — famille to + infinitif', 'famille to', 'I <b>want to</b> leave early.', 'I ______ to leave early. (veux)', 'want'),
    ('want-you-to', 'want someone to', 'vouloir QUE quelqu’un fasse — pas de that', 'vouloir que', 'I want <b>you to</b> come.', 'I want you ______ come. (que tu viennes)', 'to'),
    ('decide-to', 'decide to', 'décider de faire', 'décider de', 'We <b>decided to</b> move.', 'We decided ______ move.', 'to'),
    ('enjoy-doing', 'enjoy + -ing', 'aimer faire — famille -ing', 'famille -ing', 'I enjoy <b>cooking</b>.', 'I enjoy ______ . (cuisiner)', 'cooking'),
    ('suggest-ing', 'suggest + -ing', 'suggérer de faire', 'suggérer de', 'I suggest <b>taking</b> the train.', 'I suggest ______ the train. (prendre)', 'taking'),
    ('would-like-to', "'d like to", 'aimerais faire — toujours to après would like', 'would like', "I'd like <b>to book</b> a table.", "I'd like ______ book a table.", 'to'),
    ('stop-smoking', 'stop + -ing', 'arrêter de faire (≠ stop to = s’arrêter pour)', 'arrêter de', 'He <b>stopped smoking</b> last year.', 'He stopped ______ last year. (de fumer)', 'smoking'),
    ('remember-to', 'remember to', 'penser à faire (action à venir)', 'penser à', '<b>Remember to</b> lock the door!', '______ to lock the door! (pense à)', 'remember'),
  ],
),
}
