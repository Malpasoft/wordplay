# -*- coding: utf-8 -*-
"""fr/ A2 grammaire — lot 3 (chapitres 11-15). Explications en français, anglais cible."""

CHAPTERS = {

'too-enough-basic': dict(
  level='a2', section='grammaire', num='Ch. 11', short='Too et enough',
  title='Too et enough — trop et assez',
  subtitle='Deux petits mots, deux positions différentes dans la phrase',
  slides=[
    ('Too + adjectif : trop', None,
     '<p class="slide-explanation"><b>Too</b> signifie « trop » : il exprime un excès, un problème. Il se place <b>devant</b> l\'adjectif, exactement comme en français.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>This coffee is <b>too hot</b>. — Ce café est trop chaud.</p>'
     '<p style="margin-top:8px">The bag is <b>too heavy</b> for me. — Le sac est trop lourd pour moi.</p>'
     '<p style="margin-top:8px">We arrived <b>too late</b>. — Nous sommes arrivés trop tard.</p></div>'
     '<p style="margin-top:16px">Too + adjectif = il y a un problème : c\'est trop, ça ne va pas.</p>'),
    ('Enough APRÈS l\'adjectif', None,
     '<p class="slide-explanation"><b>Enough</b> (assez) a une particularité surprenante : avec un adjectif, il se place <b>après</b> ! C\'est l\'inverse du français « assez grand ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>He is <b>tall enough</b>. — Il est assez grand. (et non « enough tall »)</p>'
     '<p style="margin-top:8px">The water is <b>warm enough</b>. — L\'eau est assez chaude.</p>'
     '<p style="margin-top:8px">Négation : I\'m <b>not old enough</b>. — Je ne suis pas assez âgé.</p></div>'
     '<p style="margin-top:16px">Règle à graver : adjectif + ENOUGH. « Enough tall » est la faute francophone classique.</p>'),
    ('Enough AVANT le nom', None,
     '<p class="slide-explanation">Avec un <b>nom</b>, enough reprend la position française : il se place <b>devant</b>. C\'est sa double vie : après l\'adjectif, avant le nom.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>We have <b>enough money</b>. — Nous avons assez d\'argent.</p>'
     '<p style="margin-top:8px">There aren\'t <b>enough chairs</b>. — Il n\'y a pas assez de chaises.</p>'
     '<p style="margin-top:8px">Do you have <b>enough time</b>? — As-tu assez de temps ?</p></div>'
     '<p style="margin-top:16px">Résumé : tall <b>enough</b> (après l\'adjectif) · <b>enough</b> money (avant le nom).</p>'),
    ('Too... to et enough... to', None,
     '<p class="slide-explanation">Pour dire « trop... pour » ou « assez... pour », on ajoute <b>to + base verbale</b>. Structure très fréquente à l\'oral comme à l\'écrit.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I\'m <b>too tired to go</b> out. — Je suis trop fatigué pour sortir.</p>'
     '<p style="margin-top:8px">She is <b>old enough to drive</b>. — Elle est assez âgée pour conduire.</p>'
     '<p style="margin-top:8px">It\'s <b>too cold to swim</b>. — Il fait trop froid pour nager.</p></div>'
     '<p style="margin-top:16px">« Pour » + infinitif se traduit ici par <b>to</b>, pas par for : too tired TO go.</p>'),
    ('Too ou very ? Ne les confonds pas', None,
     '<p class="slide-explanation"><b>Very</b> (très) est neutre : une simple intensité. <b>Too</b> (trop) signale un <b>problème</b>. Les francophones utilisent parfois too pour dire « très » — erreur de sens !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>This film is <b>very long</b>. — Ce film est très long. (constat, pas de problème)</p>'
     '<p style="margin-top:8px">This film is <b>too long</b>. — Ce film est trop long. (problème : il m\'ennuie !)</p>'
     '<p style="margin-top:8px">She is <b>very nice</b>. — Elle est très gentille. (« too nice » = trop gentille, ça l\'handicape)</p></div>'
     '<p style="margin-top:16px">Si tout va bien, dis very. Réserve too aux situations où ça coince.</p>'),
  ],
  traps=[
    ('He is enough tall to play basketball.', 'He is <strong>tall enough</strong> to play basketball.', 'Enough se place APRÈS l\'adjectif : tall ENOUGH — l\'inverse du français.'),
    ('We don\'t have money enough.', 'We don\'t have <strong>enough money</strong>.', 'Devant un nom, enough se place AVANT : enough MONEY.'),
    ('The film was too good! (compliment)', 'The film was <strong>very good</strong>!', 'Pour un compliment, very : too signale un problème (« trop » = excès négatif).'),
    ('I\'m too tired for go out.', 'I\'m too tired <strong>to go</strong> out.', 'Trop... pour + verbe = too... TO + base verbale : too tired to go.'),
    ('It\'s too much hot today.', 'It\'s <strong>too hot</strong> today.', 'Devant un adjectif, too suffit : too hot. Too much s\'utilise avec un nom (too much sugar).'),
  ],
  summary=[
    ('Trop + adjectif', 'too + adjectif', 'This coffee is too hot.'),
    ('Assez + adjectif', 'adjectif + enough (après !)', 'He is tall enough.'),
    ('Assez de + nom', 'enough + nom (avant)', 'We have enough money.'),
    ('Trop... pour', 'too + adj + to + verbe', 'I\'m too tired to go out.'),
    ('Assez... pour', 'adj + enough + to + verbe', 'She is old enough to drive.'),
    ('Très vs trop', 'very = neutre · too = problème', 'very long / too long'),
  ],
  ex1=('Place too ou enough', 'Avant ou après ? Tout est là.', [
    ('This soup is ______ — I can\'t eat it.', ['too hot', 'very hot enough', 'enough hot'], 'too hot',
     'Excès = problème → TOO hot.'),
    ('He is ______ to reach the shelf.', ['tall enough', 'enough tall', 'too tall enough'], 'tall enough',
     'Enough APRÈS l\'adjectif : tall ENOUGH.'),
    ('We don\'t have ______ for everyone.', ['enough chairs', 'chairs enough', 'too chairs'], 'enough chairs',
     'Enough AVANT le nom : ENOUGH chairs.'),
    ('I\'m too tired ______ out tonight.', ['to go', 'for go', 'for going'], 'to go',
     'Too... TO + base verbale : too tired TO GO.'),
    ('The water is ______ to swim in.', ['warm enough', 'enough warm', 'too warm enough'], 'warm enough',
     'Assez chaude pour → warm ENOUGH to swim.'),
    ('This film is ______ — I love it!', ['very good', 'too good', 'good enough bad'], 'very good',
     'Compliment sans problème → VERY good. Too signalerait un excès.'),
  ]),
  ex2=('Écris le mot manquant', 'too, enough, very ou to ?', [
    ('« Il est assez grand. » → He is tall ______. (un mot)', 'enough',
     'Enough se place après l\'adjectif : tall ENOUGH.'),
    ('« Ce sac est trop lourd. » → This bag is ______ heavy. (un mot)', 'too',
     'Trop = TOO + adjectif.'),
    ('« Assez d\'argent » → ______ money. (un mot)', 'enough',
     'Avant le nom : ENOUGH money.'),
    ('« Trop fatigué pour conduire » → too tired ______ drive. (un mot)', 'to',
     'Too + adjectif + TO + base verbale.'),
    ('« Elle est très gentille. » → She is ______ nice. (un mot)', 'very',
     'Très (neutre, positif) → VERY. Too dirait « trop gentille ».'),
  ]),
  ex3=('Trouve la phrase correcte', 'Position de enough et choix too/very.', [
    ('« Je ne suis pas assez âgé pour voter. »', ['I\'m not old enough to vote.', 'I\'m not enough old to vote.', 'I\'m too old enough to vote.'], 'I\'m not old enough to vote.',
     'Adjectif + ENOUGH + to : old enough to vote.'),
    ('« Il fait trop froid pour nager. »', ['It\'s too cold to swim.', 'It\'s very cold to swim.', 'It\'s too much cold to swim.'], 'It\'s too cold to swim.',
     'TOO cold TO swim — too + adjectif, jamais too much + adjectif.'),
    ('« Nous n\'avons pas assez de temps. »', ['We don\'t have enough time.', 'We don\'t have time enough.', 'We don\'t have too time.'], 'We don\'t have enough time.',
     'ENOUGH + nom : enough time.'),
    ('« Ce restaurant est très bon ! »', ['This restaurant is very good!', 'This restaurant is too good!', 'This restaurant is good too much!'], 'This restaurant is very good!',
     'Compliment → VERY good. Too = excès problématique.'),
    ('« Elle est assez âgée pour conduire. »', ['She is old enough to drive.', 'She is enough old to drive.', 'She is very old to drive.'], 'She is old enough to drive.',
     'Old ENOUGH to drive : enough après l\'adjectif, puis to.'),
  ]),
  game_desc='Chaque emploi de too et enough passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('too-hot', 'too + adjectif', 'trop — un excès qui pose problème', 'trop', 'This coffee is <b>too</b> hot.', 'This coffee is ______ hot. (trop)', 'too'),
    ('tall-enough', 'adjectif + enough', 'assez — APRÈS l\'adjectif', 'assez (après)', 'He is tall <b>enough</b>.', 'He is tall ______. (assez)', 'enough'),
    ('enough-money', 'enough + nom', 'assez de — AVANT le nom', 'assez de (avant)', 'We have <b>enough</b> money.', 'We have ______ money. (assez d\')', 'enough'),
    ('too-to', 'too... to', 'trop... pour — avec to + base verbale', 'trop pour', 'I\'m too tired <b>to</b> go out.', 'I\'m too tired ______ go out. (pour)', 'to'),
    ('enough-to', 'enough... to', 'assez... pour faire quelque chose', 'assez pour', 'She is old enough to <b>drive</b>.', 'She is old enough to ______. (conduire)', 'drive'),
    ('very', 'very', 'très — intensité neutre, sans problème', 'très', 'This film is <b>very</b> long, and I love it.', 'This film is ______ long, and I love it. (très)', 'very'),
    ('not-enough', 'not... enough', 'pas assez — la négation', 'pas assez', 'I\'m <b>not</b> old enough to vote.', 'I\'m ______ old enough to vote. (négation)', 'not'),
    ('too-late', 'too late', 'trop tard — too avec un adverbe', 'trop tard', 'We arrived too <b>late</b>.', 'We arrived too ______. (tard)', 'late'),
  ],
),

'relative-clauses-basic': dict(
  level='a2', section='grammaire', num='Ch. 12', short='Les relatives',
  title='Les relatives — who, which, that',
  subtitle='Le bon pronom pour les personnes et pour les choses',
  slides=[
    ('Relier deux idées avec un pronom relatif', None,
     '<p class="slide-explanation">Le pronom relatif relie deux phrases en une : « l\'homme <b>qui</b> habite ici ». En anglais, le choix dépend de la nature de l\'antécédent : <b>personne ou chose ?</b></p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>The man <b>who</b> lives here is a doctor. — L\'homme qui habite ici est médecin.</p>'
     '<p style="margin-top:8px">The book <b>which</b> is on the table is mine. — Le livre qui est sur la table est à moi.</p></div>'
     '<p style="margin-top:16px">Le français dit « qui » dans les deux cas — l\'anglais distingue <b>who</b> (personnes) et <b>which</b> (choses).</p>'),
    ('Who : pour les personnes', None,
     '<p class="slide-explanation"><b>Who</b> s\'utilise uniquement pour les <b>personnes</b>. C\'est le réflexe à acquérir : être humain → who.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>She\'s the teacher <b>who</b> helped me. — C\'est la prof qui m\'a aidé.</p>'
     '<p style="margin-top:8px">I have a friend <b>who</b> speaks four languages. — J\'ai un ami qui parle quatre langues.</p>'
     '<p style="margin-top:8px">The people <b>who</b> live next door are very nice. — Les gens qui habitent à côté sont très gentils.</p></div>'
     '<p style="margin-top:16px">« The man which... » est une vraie faute : which réduirait la personne à une chose !</p>'),
    ('Which : pour les choses et les animaux', None,
     '<p class="slide-explanation"><b>Which</b> s\'utilise pour les <b>choses</b>, les idées et les animaux. Jamais pour les personnes.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>The film <b>which</b> won the prize is French. — Le film qui a gagné le prix est français.</p>'
     '<p style="margin-top:8px">I lost the keys <b>which</b> were on the table. — J\'ai perdu les clés qui étaient sur la table.</p>'
     '<p style="margin-top:8px">The dog <b>which</b> barks all night belongs to my neighbour. — Le chien qui aboie toute la nuit...</p></div>'
     '<p style="margin-top:16px">Astuce : si tu peux remplacer par « it », c\'est which. Si tu remplaces par « he/she », c\'est who.</p>'),
    ('That : le joker des deux familles', None,
     '<p class="slide-explanation"><b>That</b> peut remplacer who ET which dans la plupart des phrases courantes. À l\'oral, c\'est même le plus fréquent.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>The man <b>that</b> lives here is a doctor. (= who)</p>'
     '<p style="margin-top:8px">The book <b>that</b> I\'m reading is great. (= which) — Le livre que je lis est super.</p>'
     '<p style="margin-top:8px">She\'s the singer <b>that</b> everyone loves. — C\'est la chanteuse que tout le monde adore.</p></div>'
     '<p style="margin-top:16px">En cas de doute au niveau A2 : that marche presque toujours. Mais who/which restent plus précis à l\'écrit.</p>'),
    ('Qui ou que ? L\'anglais s\'en moque', None,
     '<p class="slide-explanation">Le français distingue « qui » (sujet) et « que » (objet). L\'anglais utilise les mêmes pronoms — et peut même <b>omettre</b> le pronom objet !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Sujet : The woman <b>who</b> called you is my sister. — La femme QUI t\'a appelé...</p>'
     '<p style="margin-top:8px">Objet : The woman <b>(who)</b> you met is my sister. — La femme QUE tu as rencontrée...</p>'
     '<p style="margin-top:8px">The film <b>(that)</b> we watched was great. — Le film que nous avons regardé était super.</p></div>'
     '<p style="margin-top:16px">Quand le pronom est objet (un autre sujet suit), l\'anglais parlé le supprime souvent : The film we watched...</p>'),
  ],
  traps=[
    ('The man which lives here is a doctor.', 'The man <strong>who</strong> lives here is a doctor.', 'Une personne → who (ou that), jamais which.'),
    ('I have a friend who speak English.', 'I have a friend who <strong>speaks</strong> English.', 'Après who, le verbe s\'accorde avec l\'antécédent : a friend (= he/she) → speakS.'),
    ('The book who is on the table is mine.', 'The book <strong>which</strong> is on the table is mine.', 'Une chose → which (ou that), jamais who.'),
    ('The film what we watched was great.', 'The film <strong>that</strong> we watched was great.', '« What » n\'est pas un pronom relatif ici : on dit the film THAT (ou which) we watched.'),
    ('She\'s the teacher who she helped me.', 'She\'s the teacher who <strong>helped</strong> me.', 'Who est déjà le sujet : pas de deuxième sujet « she » — who helped me.'),
  ],
  summary=[
    ('Personnes', 'who', 'the man who lives here'),
    ('Choses / animaux', 'which', 'the book which is on the table'),
    ('Joker (les deux)', 'that', 'the singer that everyone loves'),
    ('Accord du verbe', 'selon l\'antécédent', 'a friend who speakS'),
    ('Pronom objet', 'souvent omis à l\'oral', 'the film (that) we watched'),
    ('Test rapide', 'he/she → who · it → which', 'who = personne, which = chose'),
  ],
  ex1=('Who, which ou that ?', 'Personne ou chose ? Choisis le pronom.', [
    ('The woman ______ lives next door is a nurse.', ['who', 'which', 'what'], 'who',
     'Une personne → WHO lives next door.'),
    ('I lost the book ______ you gave me.', ['which', 'who', 'what'], 'which',
     'Une chose (the book) → WHICH (ou that).'),
    ('She\'s the singer ______ everyone loves.', ['that', 'which', 'what'], 'that',
     'That fonctionne pour les personnes et les choses : the singer THAT everyone loves.'),
    ('The dog ______ barks all night is my neighbour\'s.', ['which', 'who', 'whose he'], 'which',
     'Un animal → WHICH (ou that), pas who.'),
    ('I have a friend ______ speaks Japanese.', ['who', 'which', 'it'], 'who',
     'Une personne → WHO speaks (avec -s : a friend = he/she).'),
    ('The keys ______ were on the table have disappeared.', ['which', 'who', 'what'], 'which',
     'Des choses (the keys) → WHICH were on the table.'),
  ]),
  ex2=('Écris le pronom relatif', 'who ou which ?', [
    ('« L\'homme qui habite ici » → the man ______ lives here. (un mot)', 'who',
     'Personne → WHO.'),
    ('« Le film qui a gagné » → the film ______ won. (un mot)', 'which',
     'Chose → WHICH.'),
    ('« Les gens qui travaillent ici » → the people ______ work here. (un mot)', 'who',
     'Personnes → WHO work here.'),
    ('« La voiture qui est garée dehors » → the car ______ is parked outside. (un mot)', 'which',
     'Chose → WHICH is parked.'),
    ('« Un ami qui parle anglais » → a friend who ______ English. (un mot)', 'speaks',
     'A friend = he/she → le verbe prend -s : SPEAKS.'),
  ]),
  ex3=('Trouve la phrase correcte', 'Le bon pronom, et pas de double sujet.', [
    ('« La prof qui m\'a aidé est partie. »', ['The teacher who helped me has left.', 'The teacher which helped me has left.', 'The teacher who she helped me has left.'], 'The teacher who helped me has left.',
     'Personne → WHO, et who est déjà sujet : pas de « she » en plus.'),
    ('« Le livre que je lis est génial. »', ['The book that I\'m reading is great.', 'The book who I\'m reading is great.', 'The book what I\'m reading is great.'], 'The book that I\'m reading is great.',
     'Chose → THAT (ou which). What n\'est pas un relatif ici.'),
    ('« J\'ai un chien qui adore nager. »', ['I have a dog which loves swimming.', 'I have a dog who he loves swimming.', 'I have a dog what loves swimming.'], 'I have a dog which loves swimming.',
     'Animal → WHICH (ou that) loves swimming.'),
    ('« Les gens qui habitent ici sont sympas. »', ['The people who live here are nice.', 'The people which live here are nice.', 'The people who lives here is nice.'], 'The people who live here are nice.',
     'Personnes → WHO ; people est pluriel → live (sans -s) et are.'),
    ('« La femme que tu as rencontrée est ma sœur. »', ['The woman you met is my sister.', 'The woman which you met is my sister.', 'The woman who she you met is my sister.'], 'The woman you met is my sister.',
     'Pronom objet : on peut l\'omettre — the woman (who) you met.'),
  ]),
  game_desc='Chaque pronom relatif passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('who', 'who', 'qui — pour les personnes uniquement', 'personnes', 'The man <b>who</b> lives here is a doctor.', 'The man ______ lives here is a doctor. (qui)', 'who'),
    ('which', 'which', 'qui/que — pour les choses et les animaux', 'choses', 'The book <b>which</b> is on the table is mine.', 'The book ______ is on the table is mine. (qui)', 'which'),
    ('that', 'that', 'le joker — remplace who et which', 'joker', 'She\'s the singer <b>that</b> everyone loves.', 'She\'s the singer ______ everyone loves. (que)', 'that'),
    ('who-speaks', 'who + verbe-s', 'accord — le verbe suit l\'antécédent', 'accord', 'I have a friend who <b>speaks</b> four languages.', 'I have a friend who ______ four languages. (parle)', 'speaks'),
    ('which-animal', 'which (animaux)', 'les animaux prennent which, pas who', 'animaux', 'The dog <b>which</b> barks all night is next door.', 'The dog ______ barks all night is next door. (qui)', 'which'),
    ('no-double', 'who (sans double sujet)', 'who est déjà le sujet — pas de he/she en plus', 'sujet unique', 'The teacher who <b>helped</b> me has left.', 'The teacher who ______ me has left. (a aidé)', 'helped'),
    ('omitted', 'pronom objet omis', 'le relatif objet peut disparaître', 'omission', 'The film <b>that</b> we watched was great.', 'The film ______ we watched was great. (que)', 'that'),
    ('people-who', 'the people who', 'people est pluriel — verbe sans -s', 'pluriel', 'The people who <b>live</b> here are nice.', 'The people who ______ here are nice. (habitent)', 'live'),
  ],
),

'word-order': dict(
  level='a2', section='grammaire', num='Ch. 13', short='L\'ordre des mots',
  title='L\'ordre des mots — sujet, verbe, complément',
  subtitle='Le SVO anglais est strict : jamais « I like very much football »',
  slides=[
    ('SVO : l\'ordre sacré de l\'anglais', None,
     '<p class="slide-explanation">L\'anglais suit un ordre strict : <b>Sujet + Verbe + Objet</b> (SVO). Contrairement au français, on ne peut presque jamais déplacer les blocs.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I</b> (sujet) <b>like</b> (verbe) <b>football</b> (objet). — J\'aime le foot.</p>'
     '<p style="margin-top:8px"><b>She speaks English.</b> — Elle parle anglais.</p>'
     '<p style="margin-top:8px"><b>They bought a house.</b> — Ils ont acheté une maison.</p></div>'
     '<p style="margin-top:16px">Le sujet est obligatoire : « Is raining » est faux — on dit <b>It</b> is raining.</p>'),
    ('Ne sépare JAMAIS le verbe de son objet', None,
     '<p class="slide-explanation">La règle d\'or que les francophones cassent tout le temps : <b>rien ne s\'intercale entre le verbe et son objet</b>. « J\'aime beaucoup le foot » se réorganise en anglais.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>like football very much</b>. — J\'aime beaucoup le foot.</p>'
     '<p style="margin-top:8px;color:var(--muted)">« I like very much football » est LA faute francophone par excellence !</p>'
     '<p style="margin-top:8px">She <b>speaks English well</b>. — Elle parle bien anglais. (et non « speaks well English »)</p></div>'
     '<p style="margin-top:16px">Verbe + objet d\'abord, les adverbes (very much, well, a lot) passent après.</p>'),
    ('La place des compléments : manière, lieu, temps', None,
     '<p class="slide-explanation">Quand plusieurs compléments suivent l\'objet, l\'ordre habituel est : <b>manière → lieu → temps</b>. Le temps peut aussi ouvrir la phrase.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>She sang <b>beautifully</b> (manière) <b>at the concert</b> (lieu) <b>last night</b> (temps).</p>'
     '<p style="margin-top:8px">I went <b>to London</b> (lieu) <b>last week</b> (temps). — Je suis allé à Londres la semaine dernière.</p>'
     '<p style="margin-top:8px"><b>Yesterday</b>, we played tennis. — Hier, nous avons joué au tennis.</p></div>'
     '<p style="margin-top:16px">Jamais le temps entre le verbe et l\'objet : « I saw yesterday Paul » est impossible → I saw Paul yesterday.</p>'),
    ('Les adverbes de fréquence : avant le verbe', None,
     '<p class="slide-explanation">Exception bien réglée : les adverbes de fréquence (<b>always, often, usually, never</b>) se placent <b>avant le verbe</b> principal — mais <b>après be</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I <b>always drink</b> coffee in the morning. — Je bois toujours du café le matin.</p>'
     '<p style="margin-top:8px">She <b>never eats</b> meat. — Elle ne mange jamais de viande.</p>'
     '<p style="margin-top:8px">He <b>is often</b> late. — Il est souvent en retard. (après be !)</p></div>'
     '<p style="margin-top:16px">« I drink always coffee » est un calque du français « je bois toujours » — en anglais, l\'adverbe précède le verbe.</p>'),
    ('L\'adjectif AVANT le nom', None,
     '<p class="slide-explanation">Dernier réflexe d\'ordre : l\'adjectif se place <b>avant</b> le nom, toujours — l\'inverse du français le plus courant.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>a <b>red car</b> — une voiture rouge (et non « a car red »)</p>'
     '<p style="margin-top:8px">an <b>interesting book</b> — un livre intéressant</p>'
     '<p style="margin-top:8px">Plusieurs adjectifs : a <b>beautiful old</b> house — une belle maison ancienne.</p></div>'
     '<p style="margin-top:16px">L\'adjectif est invariable ET antéposé : two red carS (red sans -s, avant le nom).</p>'),
  ],
  traps=[
    ('I like very much football.', 'I like football <strong>very much</strong>.', 'Rien entre le verbe et son objet : like FOOTBALL d\'abord, very much après.'),
    ('She speaks very well English.', 'She speaks English <strong>very well</strong>.', 'Même règle : speaks ENGLISH + very well à la fin.'),
    ('I drink always coffee in the morning.', 'I <strong>always drink</strong> coffee in the morning.', 'L\'adverbe de fréquence se place AVANT le verbe : I ALWAYS drink.'),
    ('I saw yesterday my cousin.', 'I saw my cousin <strong>yesterday</strong>.', 'Le complément de temps ne coupe jamais verbe + objet : I saw my cousin YESTERDAY.'),
    ('She has a car red.', 'She has a <strong>red car</strong>.', 'L\'adjectif se place avant le nom : a RED car.'),
  ],
  summary=[
    ('Ordre de base', 'Sujet + Verbe + Objet', 'I like football.'),
    ('Verbe + objet', 'jamais séparés', 'I like football very much.'),
    ('Compléments', 'manière → lieu → temps', 'She sang beautifully at the concert last night.'),
    ('Fréquence', 'avant le verbe, après be', 'I always drink coffee. / He is often late.'),
    ('Adjectif', 'avant le nom, invariable', 'a red car · two red cars'),
    ('Sujet obligatoire', 'it pour la météo, l\'heure', 'It is raining. / It\'s five o\'clock.'),
  ],
  ex1=('Remets les mots dans l\'ordre', 'SVO strict : choisis la phrase bien construite.', [
    ('« J\'aime beaucoup la musique. »', ['I like music very much.', 'I like very much music.', 'I very much like music very.'], 'I like music very much.',
     'Verbe + objet d\'abord : like MUSIC, puis very much.'),
    ('« Elle parle bien anglais. »', ['She speaks English well.', 'She speaks well English.', 'She well speaks English.'], 'She speaks English well.',
     'Speaks ENGLISH + well à la fin.'),
    ('« Il est souvent en retard. »', ['He is often late.', 'He often is late.', 'He is late often always.'], 'He is often late.',
     'Avec be, l\'adverbe vient APRÈS : he is OFTEN late.'),
    ('« Je bois toujours du thé. »', ['I always drink tea.', 'I drink always tea.', 'Always I drink always tea.'], 'I always drink tea.',
     'Adverbe de fréquence AVANT le verbe : I ALWAYS drink.'),
    ('« Une vieille maison magnifique »', ['a beautiful old house', 'a house old beautiful', 'an old house beautiful'], 'a beautiful old house',
     'Adjectifs avant le nom : beautiful old HOUSE.'),
    ('« Il pleut. »', ['It is raining.', 'Is raining.', 'Raining it is now.'], 'It is raining.',
     'Le sujet est obligatoire : IT is raining.'),
  ]),
  ex2=('Écris le mot à la bonne place', 'Complète la phrase bien ordonnée.', [
    ('« J\'aime beaucoup ce film. » → I like this film very ______. (un mot)', 'much',
     'I like this film VERY MUCH — l\'intensité se place en fin de phrase.'),
    ('« Elle ne mange jamais de viande. » → She ______ eats meat. (un mot)', 'never',
     'NEVER avant le verbe : she never eats.'),
    ('« Une voiture rouge » → a ______ car. (un mot)', 'red',
     'L\'adjectif AVANT le nom : a RED car.'),
    ('« Je suis allé à Londres la semaine dernière. » → I went to London last ______. (un mot)', 'week',
     'Lieu puis temps : to London LAST WEEK.'),
    ('« Il est cinq heures. » → ______ is five o\'clock. (un mot)', 'It',
     'Sujet obligatoire pour l\'heure : IT is five o\'clock.'),
  ]),
  ex3=('Corrige l\'ordre des mots', 'Choisis la version correcte.', [
    ('« I saw yesterday Paul. »', ['I saw Paul yesterday.', 'I yesterday saw Paul.', 'Yesterday I saw yesterday Paul.'], 'I saw Paul yesterday.',
     'Verbe + objet inséparables : saw PAUL, yesterday à la fin.'),
    ('« She has a dress new. »', ['She has a new dress.', 'She has new a dress.', 'She a new dress has.'], 'She has a new dress.',
     'Adjectif avant le nom : a NEW dress.'),
    ('« They play often tennis. »', ['They often play tennis.', 'They play tennis often always.', 'Often they play often tennis.'], 'They often play tennis.',
     'Fréquence avant le verbe : they OFTEN play.'),
    ('« He speaks very well French. »', ['He speaks French very well.', 'He very well speaks French.', 'He speaks very French well.'], 'He speaks French very well.',
     'Speaks FRENCH d\'abord, very well ensuite.'),
    ('« Is cold today. »', ['It is cold today.', 'Today is cold it.', 'Is it cold today is.'], 'It is cold today.',
     'Sujet obligatoire : IT is cold today.'),
  ]),
  game_desc='Chaque règle d\'ordre des mots passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('svo', 'Sujet + Verbe + Objet', 'l\'ordre strict de la phrase anglaise', 'SVO', '<b>I like football</b>.', 'I ______ football. (aime)', 'like'),
    ('very-much', 'very much (à la fin)', 'beaucoup — après l\'objet, jamais avant', 'intensité finale', 'I like football very <b>much</b>.', 'I like football very ______. (beaucoup)', 'much'),
    ('well-end', 'well (après l\'objet)', 'bien — l\'adverbe suit verbe + objet', 'adverbe final', 'She speaks English <b>well</b>.', 'She speaks English ______. (bien)', 'well'),
    ('always-before', 'always + verbe', 'fréquence — avant le verbe principal', 'fréquence', 'I <b>always</b> drink coffee in the morning.', 'I ______ drink coffee in the morning. (toujours)', 'always'),
    ('is-often', 'be + often', 'avec be, l\'adverbe vient après', 'après be', 'He is <b>often</b> late.', 'He is ______ late. (souvent)', 'often'),
    ('red-car', 'adjectif + nom', 'l\'adjectif se place avant le nom', 'adjectif avant', 'She has a <b>red</b> car.', 'She has a ______ car. (rouge)', 'red'),
    ('time-end', 'temps en fin de phrase', 'yesterday, last week — jamais entre verbe et objet', 'temps final', 'I saw my cousin <b>yesterday</b>.', 'I saw my cousin ______. (hier)', 'yesterday'),
    ('it-subject', 'it (sujet obligatoire)', 'météo et heure — il faut un sujet', 'sujet it', '<b>It</b> is raining.', '______ is raining. (sujet)', 'it'),
  ],
),

'object-pronouns': dict(
  level='a2', section='grammaire', num='Ch. 14', short='Les pronoms compléments',
  title='Les pronoms compléments — me, him, her, them',
  subtitle='« Je le vois » devient I see HIM : le pronom passe après le verbe',
  slides=[
    ('La famille des pronoms compléments', None,
     '<p class="slide-explanation">Chaque pronom sujet a son pronom <b>complément</b> (objet). Apprends les paires par cœur : c\'est du vocabulaire de base.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>I → <b>me</b> · you → <b>you</b> · he → <b>him</b> · she → <b>her</b></p>'
     '<p style="margin-top:8px">it → <b>it</b> · we → <b>us</b> · they → <b>them</b></p>'
     '<p style="margin-top:8px">She knows <b>me</b>. — Elle me connaît. · I called <b>them</b>. — Je les ai appelés.</p></div>'
     '<p style="margin-top:16px">You et it ne changent pas de forme — les autres si !</p>'),
    ('LA grande différence : la position', None,
     '<p class="slide-explanation">En français, le pronom se place <b>avant</b> le verbe : « je <b>le</b> vois ». En anglais, il reste <b>après</b>, à la place normale de l\'objet : I see <b>him</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« Je le vois. » → I see <b>him</b>. (et non « I him see »)</p>'
     '<p style="margin-top:8px">« Elle m\'aime. » → She loves <b>me</b>.</p>'
     '<p style="margin-top:8px">« Nous les invitons. » → We invite <b>them</b>.</p></div>'
     '<p style="margin-top:16px">L\'ordre SVO ne bouge jamais : sujet, verbe, puis le pronom complément.</p>'),
    ('Him ou her ? It ou them ?', None,
     '<p class="slide-explanation">Le choix suit le genre et le nombre : <b>him</b> pour un homme, <b>her</b> pour une femme, <b>it</b> pour une chose, <b>them</b> pour un pluriel (personnes ou choses).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Where\'s Paul? I can\'t see <b>him</b>. — Où est Paul ? Je ne le vois pas.</p>'
     '<p style="margin-top:8px">Do you know Marie? Yes, I know <b>her</b>. — Oui, je la connais.</p>'
     '<p style="margin-top:8px">I love these songs — I listen to <b>them</b> every day. — Je les écoute tous les jours.</p></div>'
     '<p style="margin-top:16px">Attention : une voiture, un livre = <b>it</b> (pas de genre grammatical pour les objets en anglais).</p>'),
    ('Après une préposition : forme complément', None,
     '<p class="slide-explanation">Après une préposition (<b>with, for, to, at...</b>), on utilise toujours la forme complément — comme « avec moi », « pour eux » en français.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Come with <b>me</b>. — Viens avec moi.</p>'
     '<p style="margin-top:8px">This present is for <b>her</b>. — Ce cadeau est pour elle.</p>'
     '<p style="margin-top:8px">Look at <b>them</b>! — Regarde-les !</p></div>'
     '<p style="margin-top:16px">Jamais de pronom sujet après une préposition : « with I » et « for he » n\'existent pas.</p>'),
    ('Donner quelque chose à quelqu\'un', None,
     '<p class="slide-explanation">Avec les verbes comme <b>give, send, show, tell</b>, deux ordres sont possibles — mais le pronom reste toujours après le verbe.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Give <b>me</b> the book. = Give the book <b>to me</b>. — Donne-moi le livre.</p>'
     '<p style="margin-top:8px">I sent <b>her</b> a message. — Je lui ai envoyé un message.</p>'
     '<p style="margin-top:8px">Show <b>us</b> your photos! — Montre-nous tes photos !</p></div>'
     '<p style="margin-top:16px">« Lui » peut être him ou her selon la personne : I told HIM (à lui) / I told HER (à elle).</p>'),
  ],
  traps=[
    ('I him see every day.', 'I see <strong>him</strong> every day.', 'Le pronom complément reste APRÈS le verbe en anglais : I see HIM — jamais avant comme « je le vois ».'),
    ('She loves I.', 'She loves <strong>me</strong>.', 'Après un verbe, forme complément : loves ME, pas I.'),
    ('Come with I.', 'Come with <strong>me</strong>.', 'Après une préposition, forme complément : with ME.'),
    ('Do you know Marie? Yes, I know him.', 'Yes, I know <strong>her</strong>.', 'Marie est une femme → HER. Him est réservé aux hommes.'),
    ('I love this song — I listen to it every day. / these songs → I listen to its.', 'I listen to <strong>them</strong> every day.', 'Le pluriel des choses est THEM : I listen to them. « Its » est un possessif, pas un pronom pluriel.'),
  ],
  summary=[
    ('Les paires', 'I→me · he→him · she→her', 'She knows me. / I see him.'),
    ('Pluriel', 'we→us · they→them', 'They invited us.'),
    ('Position', 'toujours après le verbe', 'I see him. (≠ je le vois)'),
    ('Après préposition', 'with me · for her · at them', 'Come with me.'),
    ('Choses', 'it (singulier) · them (pluriel)', 'I like it. / I like them.'),
    ('Donner à', 'give me / give it to me', 'Give me the book.'),
  ],
  ex1=('Choisis le bon pronom', 'Genre, nombre, et toujours après le verbe.', [
    ('Where\'s Paul? I can\'t see ______.', ['him', 'he', 'her'], 'him',
     'Paul = homme, après le verbe → HIM.'),
    ('Do you know Marie? Yes, I know ______.', ['her', 'him', 'she'], 'her',
     'Marie = femme → HER.'),
    ('These photos are great — look at ______!', ['them', 'its', 'they'], 'them',
     'Pluriel → THEM, même pour des choses.'),
    ('Come to the cinema with ______.', ['us', 'we', 'our'], 'us',
     'Après une préposition → forme complément : with US.'),
    ('I bought a new phone. I love ______!', ['it', 'him', 'them'], 'it',
     'Une chose singulière → IT.'),
    ('She called ______ last night.', ['me', 'I', 'my'], 'me',
     'Après le verbe → ME : she called me.'),
  ]),
  ex2=('Traduis le pronom', 'Écris le pronom complément.', [
    ('« Je le vois. » → I see ______. (un mot)', 'him',
     'Le (masculin) → HIM, après le verbe.'),
    ('« Elle m\'aime. » → She loves ______. (un mot)', 'me',
     'M\' → ME : she loves me.'),
    ('« Nous les connaissons. » → We know ______. (un mot)', 'them',
     'Les → THEM.'),
    ('« Viens avec moi. » → Come with ______. (un mot)', 'me',
     'Avec moi → with ME.'),
    ('« Je la regarde. » (la télé) → I watch ______. (un mot)', 'it',
     'La télé est une chose → IT : I watch it.'),
  ]),
  ex3=('Trouve la phrase correcte', 'Le pronom reste après le verbe !', [
    ('« Je l\'appelle ce soir. » (Paul)', ['I\'ll call him tonight.', 'I\'ll him call tonight.', 'I\'ll call he tonight.'], 'I\'ll call him tonight.',
     'Après le verbe, forme complément : call HIM.'),
    ('« Donne-moi le sel, s\'il te plaît. »', ['Give me the salt, please.', 'Give I the salt, please.', 'Me give the salt, please.'], 'Give me the salt, please.',
     'Give ME the salt — le pronom suit le verbe.'),
    ('« Ce cadeau est pour elle. »', ['This present is for her.', 'This present is for she.', 'This present is for hers her.'], 'This present is for her.',
     'Après for → forme complément : for HER.'),
    ('« Tu nous as vus ? »', ['Did you see us?', 'Did you see we?', 'Did you us see?'], 'Did you see us?',
     'See US : forme complément après le verbe.'),
    ('« J\'adore ces chansons, je les écoute tous les jours. »', ['I love these songs — I listen to them every day.', 'I love these songs — I listen to its every day.', 'I love these songs — I them listen every day.'], 'I love these songs — I listen to them every day.',
     'Pluriel de choses → THEM, après la préposition to.'),
  ]),
  game_desc='Chaque pronom complément passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('me', 'me', 'me / moi — complément de I', 'me, moi', 'She loves <b>me</b>.', 'She loves ______. (m\')', 'me'),
    ('him', 'him', 'le / lui — pour un homme', 'le, lui', 'I see <b>him</b> every day.', 'I see ______ every day. (le)', 'him'),
    ('her', 'her', 'la / elle — pour une femme', 'la, elle', 'Do you know Marie? I know <b>her</b>.', 'Do you know Marie? I know ______. (la)', 'her'),
    ('it', 'it', 'le / la — pour une chose', 'chose', 'I bought a phone and I love <b>it</b>.', 'I bought a phone and I love ______. (l\')', 'it'),
    ('us', 'us', 'nous — complément de we', 'nous', 'They invited <b>us</b> to the party.', 'They invited ______ to the party. (nous)', 'us'),
    ('them', 'them', 'les / eux — pluriel, personnes ou choses', 'les, eux', 'I called <b>them</b> yesterday.', 'I called ______ yesterday. (les)', 'them'),
    ('with-me', 'préposition + complément', 'après with, for, to — jamais de pronom sujet', 'après préposition', 'Come with <b>me</b>.', 'Come with ______. (moi)', 'me'),
    ('give-me', 'give me', 'donne-moi — le pronom suit le verbe', 'donner à', 'Give <b>me</b> the book, please.', 'Give ______ the book, please. (moi)', 'me'),
  ],
),

'short-answers': dict(
  level='a2', section='grammaire', num='Ch. 15', short='Les réponses courtes',
  title='Les réponses courtes — Yes, I do. No, she isn\'t.',
  subtitle='Répondre comme un anglophone : on reprend l\'auxiliaire',
  slides=[
    ('Yes et no tout seuls : trop secs !', None,
     '<p class="slide-explanation">En anglais, répondre juste « yes » ou « no » paraît sec, voire impoli. La réponse naturelle reprend <b>l\'auxiliaire de la question</b> : c\'est la <b>réponse courte</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Do you like</b> tea? — <b>Yes, I do.</b> / <b>No, I don\'t.</b></p>'
     '<p style="margin-top:8px"><b>Is she</b> French? — <b>Yes, she is.</b> / <b>No, she isn\'t.</b></p>'
     '<p style="margin-top:8px"><b>Can you</b> swim? — <b>Yes, I can.</b> / <b>No, I can\'t.</b></p></div>'
     '<p style="margin-top:16px">La recette : Yes/No + pronom + auxiliaire (positif ou négatif). Jamais le verbe principal !</p>'),
    ('Avec do et does', None,
     '<p class="slide-explanation">Question au present simple → l\'auxiliaire est <b>do/does</b>. La réponse courte reprend do ou does, jamais le verbe.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Do you speak English? — Yes, I <b>do</b>. (et non « Yes, I speak »)</p>'
     '<p style="margin-top:8px">Does he work here? — Yes, he <b>does</b>. / No, he <b>doesn\'t</b>.</p>'
     '<p style="margin-top:8px">Did they come? — Yes, they <b>did</b>. / No, they <b>didn\'t</b>.</p></div>'
     '<p style="margin-top:16px">Au passé, c\'est <b>did</b> pour tout le monde : Yes, I did. / No, she didn\'t.</p>'),
    ('Avec be : is, are, was, were', None,
     '<p class="slide-explanation">Question avec <b>be</b> → on reprend la forme de be. Attention à l\'accord : la réponse s\'accorde avec le <b>pronom de la réponse</b>, pas celui de la question !</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Is she French? — Yes, she <b>is</b>. / No, she <b>isn\'t</b>.</p>'
     '<p style="margin-top:8px">Are you ready? — Yes, I <b>am</b>. / No, I\'<b>m not</b>.</p>'
     '<p style="margin-top:8px">Were they at home? — Yes, they <b>were</b>. / No, they <b>weren\'t</b>.</p></div>'
     '<p style="margin-top:16px">Piège : « Are you...? » se répond avec I — Yes, I AM (pas « yes, you are » !).</p>'),
    ('Avec les modaux et have', None,
     '<p class="slide-explanation">Même principe avec <b>can, will, could, should</b> et le present perfect (<b>have/has</b>) : on renvoie l\'auxiliaire de la question.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Can you drive? — Yes, I <b>can</b>. / No, I <b>can\'t</b>.</p>'
     '<p style="margin-top:8px">Will she come? — Yes, she <b>will</b>. / No, she <b>won\'t</b>.</p>'
     '<p style="margin-top:8px">Have you finished? — Yes, I <b>have</b>. / No, I <b>haven\'t</b>.</p></div>'
     '<p style="margin-top:16px">L\'auxiliaire qui ouvre la question est celui qui ferme la réponse — un vrai jeu de miroir.</p>'),
    ('Pas de contraction au positif !', None,
     '<p class="slide-explanation">Détail important : à la réponse <b>positive</b>, pas de contraction. À la négative, la contraction est normale.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Yes, I <b>am</b>. (et non « Yes, I\'m. ») · Yes, she <b>is</b>. (et non « Yes, she\'s. »)</p>'
     '<p style="margin-top:8px">No, I\'<b>m not</b>. · No, she <b>isn\'t</b>. · No, they <b>don\'t</b>. — contractions normales.</p>'
     '<p style="margin-top:8px">Yes, we <b>have</b>. / No, we <b>haven\'t</b>.</p></div>'
     '<p style="margin-top:16px">La forme pleine au positif donne du poids à la réponse : Yes, I AM.</p>'),
  ],
  traps=[
    ('Do you like tea? — Yes, I like.', 'Yes, I <strong>do</strong>.', 'La réponse courte reprend l\'auxiliaire, pas le verbe : Yes, I DO.'),
    ('Is she French? — Yes, she\'s.', 'Yes, she <strong>is</strong>.', 'Pas de contraction à la réponse positive : Yes, she IS.'),
    ('Are you ready? — Yes, you are.', 'Yes, <strong>I am</strong>.', 'On répond pour soi : Are YOU...? → Yes, I am.'),
    ('Can you swim? — Yes, I do.', 'Yes, I <strong>can</strong>.', 'On renvoie le MÊME auxiliaire que la question : Can...? → Yes, I CAN.'),
    ('Did you see the film? — No, I didn\'t saw.', 'No, I <strong>didn\'t</strong>.', 'La réponse courte s\'arrête à l\'auxiliaire : No, I didn\'t — sans répéter le verbe.'),
  ],
  summary=[
    ('Recette', 'Yes/No + pronom + auxiliaire', 'Yes, I do. / No, she isn\'t.'),
    ('Present simple', 'do / does / don\'t / doesn\'t', 'Does he work? — Yes, he does.'),
    ('Past simple', 'did / didn\'t', 'Did they come? — No, they didn\'t.'),
    ('Be', 'am / is / are / was / were', 'Are you ready? — Yes, I am.'),
    ('Modaux et have', 'can · will · have...', 'Can you drive? — Yes, I can.'),
    ('Au positif', 'forme pleine, sans contraction', 'Yes, she is. (jamais « Yes, she\'s »)'),
  ],
  ex1=('Choisis la réponse courte', 'Reprends l\'auxiliaire de la question.', [
    ('Do you like coffee? — Yes, I ______.', ['do', 'like', 'am'], 'do',
     'Question avec do → réponse avec DO : Yes, I do.'),
    ('Is your brother a student? — Yes, he ______.', ['is', 'does', 'student'], 'is',
     'Question avec is → Yes, he IS.'),
    ('Can she drive? — No, she ______.', ['can\'t', 'doesn\'t', 'isn\'t'], 'can\'t',
     'Question avec can → No, she CAN\'T.'),
    ('Did they win the match? — Yes, they ______.', ['did', 'won', 'do'], 'did',
     'Question avec did → Yes, they DID — sans répéter le verbe.'),
    ('Have you finished? — No, I ______.', ['haven\'t', 'didn\'t', 'don\'t'], 'haven\'t',
     'Question avec have → No, I HAVEN\'T.'),
    ('Are you French? — Yes, I ______.', ['am', 'are', 'is'], 'am',
     'Are YOU...? → on répond pour soi : Yes, I AM.'),
  ]),
  ex2=('Écris la réponse courte', 'Auxiliaire seulement !', [
    ('Does she work here? — Yes, she ______. (un mot)', 'does',
     'Does dans la question → DOES dans la réponse.'),
    ('Were they at the party? — No, they ______. (un mot)', 'weren\'t',
     'Were + négation → WEREN\'T.'),
    ('Will he come tomorrow? — No, he ______. (un mot)', 'won\'t',
     'Will + négation → WON\'T.'),
    ('Do you speak Spanish? — No, I ______. (un mot)', 'don\'t',
     'Do + négation → DON\'T.'),
    ('Is it raining? — Yes, it ______. (un mot)', 'is',
     'Is → Yes, it IS (forme pleine au positif).'),
  ]),
  ex3=('La bonne réponse à chaque question', 'Le miroir de l\'auxiliaire.', [
    ('« Did you call her? » — réponse négative :', ['No, I didn\'t.', 'No, I didn\'t call.', 'No, I don\'t.'], 'No, I didn\'t.',
     'Réponse courte : auxiliaire seul — No, I DIDN\'T.'),
    ('« Are you tired? » — réponse positive :', ['Yes, I am.', 'Yes, you are.', 'Yes, I\'m.'], 'Yes, I am.',
     'On répond pour soi (I), forme pleine au positif : Yes, I AM.'),
    ('« Can your sister swim? » — réponse positive :', ['Yes, she can.', 'Yes, she does.', 'Yes, she swims.'], 'Yes, she can.',
     'Can dans la question → CAN dans la réponse.'),
    ('« Does he play football? » — réponse négative :', ['No, he doesn\'t.', 'No, he don\'t.', 'No, he doesn\'t play.'], 'No, he doesn\'t.',
     'He → DOESN\'T, et on s\'arrête à l\'auxiliaire.'),
    ('« Have they arrived? » — réponse positive :', ['Yes, they have.', 'Yes, they did.', 'Yes, they\'ve.'], 'Yes, they have.',
     'Have dans la question → Yes, they HAVE (forme pleine).'),
  ]),
  game_desc='Chaque réponse courte passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('yes-i-do', 'Yes, I do.', 'réponse à Do you...? — on reprend do', 'avec do', 'Do you like tea? — Yes, I <b>do</b>.', 'Do you like tea? — Yes, I ______. (auxiliaire)', 'do'),
    ('no-i-dont', 'No, I don\'t.', 'réponse négative avec don\'t', 'négatif do', 'Do you smoke? — No, I <b>don\'t</b>.', 'Do you smoke? — No, I ______. (négation)', 'don\'t'),
    ('yes-she-is', 'Yes, she is.', 'réponse avec be — forme pleine au positif', 'avec be', 'Is she French? — Yes, she <b>is</b>.', 'Is she French? — Yes, she ______. (auxiliaire)', 'is'),
    ('yes-i-am', 'Yes, I am.', 'Are you...? → on répond avec I am', 'are → am', 'Are you ready? — Yes, I <b>am</b>.', 'Are you ready? — Yes, I ______. (auxiliaire)', 'am'),
    ('yes-i-can', 'Yes, I can.', 'réponse avec un modal — le même qu\'en question', 'avec can', 'Can you swim? — Yes, I <b>can</b>.', 'Can you swim? — Yes, I ______. (auxiliaire)', 'can'),
    ('no-she-didnt', 'No, she didn\'t.', 'réponse au passé avec didn\'t', 'avec did', 'Did she come? — No, she <b>didn\'t</b>.', 'Did she come? — No, she ______. (négation)', 'didn\'t'),
    ('yes-i-have', 'Yes, I have.', 'réponse au present perfect avec have', 'avec have', 'Have you finished? — Yes, I <b>have</b>.', 'Have you finished? — Yes, I ______. (auxiliaire)', 'have'),
    ('no-he-wont', 'No, he won\'t.', 'réponse au futur avec won\'t', 'avec will', 'Will he come? — No, he <b>won\'t</b>.', 'Will he come? — No, he ______. (négation)', 'won\'t'),
  ],
),

}
