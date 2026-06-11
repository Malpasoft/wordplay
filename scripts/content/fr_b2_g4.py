# -*- coding: utf-8 -*-
"""fr/ B2 grammaire — lot 4 final (5 chapitres)."""

CHAPTERS = {

'passive': dict(
  level='b2', section='grammaire', num='Ch. 14', short='Passive (Advanced)',
  title='Passive (Advanced) — Le passif niveau supérieur',
  subtitle='It is said that... · have something done · get-passive',
  slides=[
    ('Pourquoi l’anglais adore le passif', None,
     '<p class="slide-explanation">Le français évite le passif avec <b>« on »</b> : « On m’a volé mon vélo. » L’anglais, lui, utilise le passif partout — surtout à l’écrit formel. Au B2, il faut le produire naturellement, pas seulement le reconnaître.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>My bike was stolen.</b> (On m’a volé mon vélo.)</p>'
     '<p style="margin-top:8px"><b>English is spoken here.</b> (Ici, on parle anglais.)</p></div>'
     '<p style="margin-top:16px">Réflexe à prendre : quand vous pensez « on + verbe », envisagez le passif anglais.</p>'),
    ('It is said that... / He is said to...', None,
     '<p class="slide-explanation">Pour rapporter une opinion générale (« on dit que... »), deux structures de registre soutenu :</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>It is said that he is very rich.</b> (On dit qu’il est très riche.)</p>'
     '<p style="margin-top:8px"><b>He is said to be very rich.</b> (Il est réputé très riche.)</p>'
     '<p style="margin-top:8px">Aussi : <b>is believed to, is thought to, is expected to, is reported to</b>.</p></div>'
     '<p style="margin-top:16px">Pour un fait passé : <b>He is said to have left.</b> (On dit qu’il est parti.)</p>'),
    ('Have something done', None,
     '<p class="slide-explanation"><b>have + objet + participe passé</b> = faire faire quelque chose par quelqu’un. Le français dit « faire réparer », l’anglais inverse l’ordre.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I had my car repaired.</b> (J’ai fait réparer ma voiture.)</p>'
     '<p style="margin-top:8px"><b>She’s having her hair cut tomorrow.</b> (Elle se fait couper les cheveux demain.)</p></div>'
     '<p style="margin-top:16px">Attention à l’ordre : have + <b>la chose</b> + participe — jamais « I had repaired my car » (qui est un past perfect !).</p>'),
    ('Le get-passive', None,
     '<p class="slide-explanation">À l’oral, <b>get + participe passé</b> remplace souvent be — surtout pour les événements soudains ou fâcheux.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>He got fired last week.</b> (Il s’est fait virer la semaine dernière.)</p>'
     '<p style="margin-top:8px"><b>My phone got stolen.</b> (Mon téléphone s’est fait voler.)</p></div>'
     '<p style="margin-top:16px">Équivalent du français familier « se faire + infinitif ». Registre : conversation, pas dissertation.</p>'),
    ('Passif + infinitif et gérondif', None,
     '<p class="slide-explanation">Le passif se glisse aussi après les verbes à motifs : <b>to be done</b> (infinitif passif) et <b>being done</b> (gérondif passif).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>She hopes to be promoted.</b> (Elle espère être promue.)</p>'
     '<p style="margin-top:8px"><b>I hate being interrupted.</b> (Je déteste qu’on m’interrompe.)</p>'
     '<p style="margin-top:8px"><b>The report needs to be checked.</b> = <b>The report needs checking.</b></p></div>'),
  ],
  traps=[
    ('They said me that...', '<strong>I was told</strong> that...', '« On m’a dit » → I was told. Say ne prend pas d’objet indirect direct ; tell oui, et son passif est courant.'),
    ('I had repaired my car yesterday.', 'I <strong>had my car repaired</strong> yesterday.', 'L’ordre have + objet + participe est obligatoire pour « faire réparer » ; sinon c’est un past perfect.'),
    ('It is said he to be rich.', '<strong>He is said to be</strong> rich.', 'Soit It is said that he is rich, soit He is said to be rich — pas de mélange.'),
    ('He is believed that he lives abroad.', 'He is believed <strong>to live</strong> abroad.', 'Avec un sujet personnel, la structure est is believed + to + infinitif.'),
    ('I hate to be interrupting.', 'I hate <strong>being interrupted</strong>.', '« Qu’on m’interrompe » = sens passif → being + participe passé.'),
  ],
  summary=[
    ('On dit que...', 'It is said that + proposition', 'It is said that he is rich.'),
    ('Il est réputé...', 'subject + is said to + infinitif', 'He is said to be rich.'),
    ('Faire faire', 'have + objet + participe passé', 'I had my car repaired.'),
    ('Se faire + inf.', 'get + participe passé (oral)', 'He got fired.'),
    ('Infinitif passif', 'to be + participe passé', 'She hopes to be promoted.'),
    ('Gérondif passif', 'being + participe passé', 'I hate being interrupted.'),
  ],
  ex1=('Choisis la forme correcte', 'Structures passives avancées.', [
    ('The suspect ______ to be hiding in France.', ['is believed', 'believes', 'is believing'], 'is believed',
     'On pense qu’il se cache → is believed to be hiding.'),
    ('I’m going to ______ tomorrow.', ['have my eyes tested', 'have tested my eyes', 'test my eyes by someone'], 'have my eyes tested',
     'Faire contrôler sa vue → have + my eyes + tested.'),
    ('She ______ in the accident, but she’s fine now.', ['got injured', 'got injure', 'injured'], 'got injured',
     'Get-passive : got + participe passé — elle s’est blessée / a été blessée.'),
    ('It ______ that the company will close.', ['is reported', 'reports', 'is reporting'], 'is reported',
     'It is reported that... — on rapporte que...'),
    ('Nobody likes ______ in public.', ['being criticised', 'to criticise', 'criticising'], 'being criticised',
     'Être critiqué (sens passif) → being criticised.'),
    ('The ancient city ______ to have been destroyed by an earthquake.', ['is thought', 'thinks', 'is thinking'], 'is thought',
     'Fait passé rapporté : is thought to have been destroyed.'),
  ]),
  ex2=('Complète la structure', 'Écris le mot manquant.', [
    ('We had our kitchen ______ last month. (rénover — participe passé)', 'renovated',
     'Have + objet + participe passé : had our kitchen renovated.'),
    ('He is said ______ be the best player of his generation. (la particule)', 'to',
     'Is said TO be — la structure personnelle du passif de rapport.'),
    ('My wallet ______ stolen on the metro. (se faire voler, à l’oral — prétérit)', 'got',
     'Got stolen — le get-passive des mésaventures.'),
    ('I ______ told that the meeting was cancelled. (be au prétérit)', 'was',
     'On m’a dit → I WAS told.'),
    ('The documents need to ______ signed before Friday. (be)', 'be',
     'Infinitif passif : need to BE signed.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« On dit qu’elle vit au Japon. »', ['She is said to live in Japan.', 'She is said that she lives in Japan.', 'It says she to live in Japan.'], 'She is said to live in Japan.',
     'Structure personnelle : is said to + infinitif.'),
    ('« J’ai fait repeindre la maison. »', ['I had the house repainted.', 'I had repainted the house.', 'I made repaint the house.'], 'I had the house repainted.',
     'Have + objet + participe passé = faire faire.'),
    ('« Il s’est fait renverser par une voiture. »', ['He got knocked down by a car.', 'He knocked down a car.', 'He had knocked down by a car.'], 'He got knocked down by a car.',
     'Get-passive : got knocked down.'),
    ('« On m’a donné de mauvaises informations. »', ['I was given the wrong information.', 'They gave to me wrong information.', 'It was given me wrong information.'], 'I was given the wrong information.',
     'Le passif avec objet indirect : I was given...'),
    ('« Elle déteste qu’on la prenne en photo. »', ['She hates being photographed.', 'She hates to photograph.', 'She hates that one photographs her.'], 'She hates being photographed.',
     'Sens passif après hate → being + participe passé.'),
  ]),
  game_desc='Chaque structure passive avancée passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('is-said-to', 'is said to', 'est réputé / on dit que', 'passif de rapport', 'He <b>is said to</b> be very rich.', 'He is said ______ be very rich.', 'to'),
    ('it-is-believed', 'It is believed that', 'on pense que', 'opinion générale', '<b>It is believed that</b> the suspect left the country.', '______ is believed that the suspect left. (pronom)', 'it'),
    ('have-done', 'have something done', 'faire faire quelque chose', 'causatif passif', 'I <b>had my car repaired</b>.', 'I had my car ______. (réparer — participe)', 'repaired'),
    ('get-passive', 'get + participe', 'se faire + infinitif (oral)', 'get-passive', 'He <b>got fired</b> last week.', 'He ______ fired last week. (get au prétérit)', 'got'),
    ('was-told', 'I was told', 'on m’a dit', 'passif de tell', 'I <b>was told</b> that the meeting was cancelled.', 'I was ______ that the meeting was cancelled. (dire à qqn — participe)', 'told'),
    ('to-be-done', 'to be + participe', 'l’infinitif passif', 'infinitif passif', 'She hopes <b>to be promoted</b>.', 'She hopes to ______ promoted. (be)', 'be'),
    ('being-done', 'being + participe', 'le gérondif passif', 'gérondif passif', 'I hate <b>being interrupted</b>.', 'I hate ______ interrupted. (be en -ing)', 'being'),
    ('is-thought-to', 'is thought to have', 'on pense que (fait passé)', 'rapport au passé', 'He <b>is thought to have</b> left.', 'He is thought to ______ left. (have)', 'have'),
  ],
),

'relative-clauses': dict(
  level='b2', section='grammaire', num='Ch. 15', short='Relative Clauses',
  title='Relative Clauses — Relatives avancées',
  subtitle='Virgules, whose, prépositions et relatives réduites',
  slides=[
    ('Définissante ou non ? La virgule décide', None,
     '<p class="slide-explanation">Une relative <b>définissante</b> identifie de qui on parle — pas de virgule. Une relative <b>non-définissante</b> ajoute une parenthèse — virgules obligatoires, et <b>that est interdit</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The students who passed got a certificate.</b> (seulement ceux qui ont réussi)</p>'
     '<p style="margin-top:8px"><b>My brother, who lives in Lyon, is a chef.</b> (parenthèse — j’ai un seul frère)</p></div>'
     '<p style="margin-top:16px">En français, la virgule joue le même rôle — mais à l’écrit anglais, l’erreur coûte des points au Cambridge.</p>'),
    ('Dont = whose (et ses pièges)', None,
     '<p class="slide-explanation">Le français « dont » se traduit le plus souvent par <b>whose</b> (possession), valable pour les personnes ET les choses.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>That’s the author whose book won the prize.</b> (l’auteur dont le livre...)</p>'
     '<p style="margin-top:8px"><b>A city whose streets are always crowded.</b></p></div>'
     '<p style="margin-top:16px">Mais « dont » ≠ toujours whose : « le film dont je parle » = the film <b>(that) I’m talking about</b> — c’est la préposition qui compte.</p>'),
    ('La préposition : à la fin ou devant which/whom', None,
     '<p class="slide-explanation">Deux registres : préposition rejetée à la fin (courant) ou devant <b>which/whom</b> (soutenu).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The people I work with are great.</b> (courant)</p>'
     '<p style="margin-top:8px"><b>The people with whom I work are great.</b> (soutenu)</p></div>'
     '<p style="margin-top:16px">Jamais « with who » ni « with that » : après une préposition, c’est <b>whom</b> ou <b>which</b>.</p>'),
    ('Which qui reprend toute la phrase', None,
     '<p class="slide-explanation">Après une virgule, <b>which</b> peut reprendre toute l’idée précédente — le français dit « ce qui ».</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>He arrived on time, which surprised everyone.</b></p>'
     '<p style="margin-top:8px">(Il est arrivé à l’heure, ce qui a surpris tout le monde.)</p></div>'
     '<p style="margin-top:16px">Erreur classique de francophone : « what surprised everyone ». What n’est jamais relatif après une virgule.</p>'),
    ('Relatives réduites', None,
     '<p class="slide-explanation">L’anglais raccourcit : <b>-ing</b> pour le sens actif, <b>participe passé</b> pour le sens passif.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>The man standing by the door is my uncle.</b> (= who is standing)</p>'
     '<p style="margin-top:8px"><b>The products sold here are organic.</b> (= that are sold)</p></div>'),
  ],
  traps=[
    ('My mother, that lives in Nice, is retired.', 'My mother, <strong>who</strong> lives in Nice, is retired.', 'Après une virgule (relative non-définissante), that est interdit — who/which seulement.'),
    ('The film about which I told you... (à l’oral)', 'The film <strong>I told you about</strong>...', 'Correct mais trop soutenu pour l’oral : on rejette la préposition à la fin.'),
    ('He was late, what annoyed me.', 'He was late, <strong>which</strong> annoyed me.', '« Ce qui » après une virgule = which, jamais what.'),
    ('The girl which won is my cousin.', 'The girl <strong>who</strong> won is my cousin.', 'Personne → who (ou that en définissante) ; which est réservé aux choses.'),
    ('That’s the man who’s car was stolen.', 'That’s the man <strong>whose</strong> car was stolen.', 'Whose = dont (possession) ; who’s = who is.'),
  ],
  summary=[
    ('Définissante', 'pas de virgule · that possible', 'The students who/that passed...'),
    ('Non-définissante', 'virgules · jamais that', 'My brother, who lives in Lyon,...'),
    ('Dont (possession)', 'whose + nom', 'the author whose book won'),
    ('Préposition', 'à la fin / with whom (soutenu)', 'the people I work with'),
    ('Ce qui', ', which + verbe', 'He came, which surprised us.'),
    ('Réduite', '-ing (actif) / participe (passif)', 'the man standing there'),
  ],
  ex1=('Choisis la forme correcte', 'Relatives avancées.', [
    ('My sister, ______ works in Paris, is visiting us.', ['who', 'that', 'which'], 'who',
     'Non-définissante (virgules) + personne → who ; that est interdit.'),
    ('That’s the woman ______ son won the competition.', ['whose', 'who’s', 'which'], 'whose',
     'Dont le fils → whose + nom.'),
    ('The hotel ______ we stayed was right on the beach.', ['where', 'which', 'what'], 'where',
     'Lieu + « nous y avons séjourné » → where (= in which).'),
    ('She passed her exam, ______ made her parents proud.', ['which', 'what', 'that'], 'which',
     'Reprise de toute la phrase après virgule → which.'),
    ('The colleagues ______ I have lunch are very friendly.', ['with whom', 'with who', 'with that'], 'with whom',
     'Après une préposition : whom (personnes) — jamais who ni that.'),
    ('Anyone ______ a ticket can enter the draw.', ['buying', 'bought', 'who buying'], 'buying',
     'Relative réduite active : anyone buying = anyone who buys.'),
  ]),
  ex2=('Complète la relative', 'Écris le mot manquant.', [
    ('The keys ______ on the table are mine. (relative réduite passive de leave)', 'left',
     'The keys left on the table = that were left.'),
    ('He’s the artist ______ paintings sell for millions. (dont)', 'whose',
     'Dont les tableaux → whose paintings.'),
    ('It rained all week, ______ ruined our holiday. (ce qui)', 'which',
     'Reprise de phrase : , which ruined...'),
    ('The town ______ I grew up has changed a lot. (où)', 'where',
     'Le lieu où j’ai grandi → where.'),
    ('To ______ should I address the letter? (à qui — soutenu)', 'whom',
     'Après préposition, registre soutenu : to whom.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Le professeur dont je t’ai parlé prend sa retraite. »', ['The teacher I told you about is retiring.', 'The teacher whose I told you is retiring.', 'The teacher about that I told you is retiring.'], 'The teacher I told you about is retiring.',
     '« Dont je parle » = préposition about, pas whose : the teacher I told you about.'),
    ('« Mon père, qui a 70 ans, fait encore du vélo. »', ['My father, who is 70, still cycles.', 'My father that is 70 still cycles.', 'My father, which is 70, still cycles.'], 'My father, who is 70, still cycles.',
     'Non-définissante : virgules + who.'),
    ('« Elle a refusé l’offre, ce qui m’a étonné. »', ['She refused the offer, which surprised me.', 'She refused the offer, what surprised me.', 'She refused the offer, that surprised me.'], 'She refused the offer, which surprised me.',
     '« Ce qui » = , which.'),
    ('« Les personnes invitées à la réunion sont arrivées. »', ['The people invited to the meeting have arrived.', 'The people inviting to the meeting have arrived.', 'The people who invited to the meeting arrived.'], 'The people invited to the meeting have arrived.',
     'Sens passif (invitées) → participe passé : invited.'),
    ('Quelle phrase est en registre SOUTENU ?', ['The candidate with whom we spoke was excellent.', 'The candidate we spoke with was excellent.', 'The candidate who we spoke with was excellent.'], 'The candidate with whom we spoke was excellent.',
     'Préposition + whom = registre soutenu des écrits formels.'),
  ]),
  game_desc='Chaque structure relative passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('whose', 'whose', 'dont (possession)', 'possession', 'The author <b>whose</b> book won the prize.', 'The author ______ book won the prize. (dont)', 'whose'),
    ('non-defining-who', ', who ...', 'relative non-définissante (personne)', 'parenthèse', 'My brother, <b>who</b> lives in Lyon, is a chef.', 'My brother, ______ lives in Lyon, is a chef.', 'who'),
    ('sentence-which', ', which', 'ce qui (reprend la phrase)', 'reprise', 'He arrived on time, <b>which</b> surprised everyone.', 'He arrived on time, ______ surprised everyone.', 'which'),
    ('with-whom', 'with whom', 'avec qui (soutenu)', 'préposition', 'The people <b>with whom</b> I work.', 'The people with ______ I work. (soutenu)', 'whom'),
    ('where', 'where', 'où (lieu)', 'lieu', 'The town <b>where</b> I grew up.', 'The town ______ I grew up. (où)', 'where'),
    ('reduced-ing', 'relative réduite en -ing', 'sens actif raccourci', 'réduction active', 'The man <b>standing</b> by the door.', 'The man ______ by the door is my uncle. (stand en -ing)', 'standing'),
    ('reduced-pp', 'relative réduite (participe)', 'sens passif raccourci', 'réduction passive', 'The products <b>sold</b> here are organic.', 'The products ______ here are organic. (vendre — participe)', 'sold'),
    ('that-defining', 'that (définissante)', 'qui/que sans virgule', 'définissante', 'The students <b>that</b> passed got a certificate.', 'The students ______ passed got a certificate. (sans virgule, mot en t)', 'that'),
  ],
),

'reported-speech': dict(
  level='b2', section='grammaire', num='Ch. 16', short='Reported Speech (Advanced)',
  title='Reported Speech (Advanced) — Les verbes de rapport',
  subtitle='suggest, admit, deny, accuse of : au-delà de say et tell',
  slides=[
    ('Au-delà de say et tell', None,
     '<p class="slide-explanation">Au B2, rapporter avec <b>said that</b> partout fait perdre des points. Les verbes de rapport (<b>suggest, admit, deny, promise, refuse, warn...</b>) résument l’intention en un mot — mais chacun impose sa structure.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« I’m sorry I was late. » → <b>He apologised for being late.</b></p>'
     '<p style="margin-top:8px">« I didn’t take it! » → <b>She denied taking it.</b></p></div>'),
    ('Verbe + gérondif', None,
     '<p class="slide-explanation"><b>admit, deny, suggest, recommend, apologise for, insist on, accuse sb of</b> + -ing.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>He admitted cheating.</b> (Il a avoué avoir triché.)</p>'
     '<p style="margin-top:8px"><b>She suggested going early.</b> (Elle a proposé de partir tôt.)</p>'
     '<p style="margin-top:8px"><b>They accused him of lying.</b></p></div>'
     '<p style="margin-top:16px">Piège n° 1 du francophone : « suggérer DE faire » → jamais « suggest to do ». C’est <b>suggest doing</b> ou <b>suggest (that) we do</b>.</p>'),
    ('Verbe + (objet) + to + infinitif', None,
     '<p class="slide-explanation"><b>promise, refuse, offer, agree, threaten</b> + to do · <b>advise, warn, remind, persuade, encourage, order + quelqu’un</b> + to do.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>She refused to answer.</b> (Elle a refusé de répondre.)</p>'
     '<p style="margin-top:8px"><b>He reminded me to lock the door.</b> (Il m’a rappelé de fermer.)</p>'
     '<p style="margin-top:8px"><b>They warned us not to go.</b> (négation : not to)</p></div>'),
    ('Rapporter les questions', None,
     '<p class="slide-explanation">Question rapportée = ordre affirmatif (sujet + verbe), pas d’inversion, pas de point d’interrogation. Yes/no → <b>if/whether</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>« Where do you live? » → <b>He asked me where I lived.</b></p>'
     '<p style="margin-top:8px">« Are you ready? » → <b>She asked if I was ready.</b></p></div>'
     '<p style="margin-top:16px">Jamais « He asked me where did I live » — l’inversion disparaît.</p>'),
    ('Quand ne PAS reculer les temps', None,
     '<p class="slide-explanation">Pas de backshift si le fait est toujours vrai, ou si le verbe de rapport est au présent.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>She said the Earth goes round the Sun.</b> (vérité générale)</p>'
     '<p style="margin-top:8px"><b>He says he’s coming.</b> (rapport au présent → rien ne bouge)</p></div>'),
  ],
  traps=[
    ('She suggested to go early.', 'She suggested <strong>going</strong> early.', 'Suggest + -ing (ou suggest that we go) — jamais suggest to do, malgré « suggérer de ».'),
    ('He asked me where did I live.', 'He asked me where <strong>I lived</strong>.', 'Question rapportée : ordre affirmatif, pas d’inversion.'),
    ('They accused him to steal the money.', 'They accused him <strong>of stealing</strong> the money.', 'Accuse somebody OF + -ing.'),
    ('She warned us to not go out.', 'She warned us <strong>not to</strong> go out.', 'La négation de l’infinitif : not to go — not avant to.'),
    ('He said me that he was tired.', 'He <strong>told me</strong> that he was tired.', 'Say + that (sans objet) ; tell + quelqu’un + that. « Said me » n’existe pas.'),
  ],
  summary=[
    ('Avouer / nier', 'admit, deny + -ing', 'He denied taking it.'),
    ('Proposer', 'suggest + -ing / that...', 'She suggested going early.'),
    ('Accuser', 'accuse sb of + -ing', 'They accused him of lying.'),
    ('Refuser / promettre', 'refuse, promise + to do', 'She refused to answer.'),
    ('Conseiller / rappeler', 'advise, remind sb + to do', 'He reminded me to lock up.'),
    ('Question rapportée', 'asked + if/wh- + sujet + verbe', 'He asked where I lived.'),
  ],
  ex1=('Choisis la forme correcte', 'Verbes de rapport et leurs structures.', [
    ('She suggested ______ a taxi.', ['taking', 'to take', 'take'], 'taking',
     'Suggest + -ing : suggested taking.'),
    ('He denied ______ the window.', ['breaking', 'to break', 'break'], 'breaking',
     'Deny + -ing : il a nié avoir cassé.'),
    ('They persuaded us ______ another night.', ['to stay', 'staying', 'stay'], 'to stay',
     'Persuade + objet + to + infinitif.'),
    ('She asked me ______ I had seen her keys.', ['if', 'that', 'did'], 'if',
     'Question yes/no rapportée → if/whether.'),
    ('The police accused him ______ the documents.', ['of stealing', 'to steal', 'for stealing'], 'of stealing',
     'Accuse sb OF + -ing.'),
    ('He reminded me ______ forget my passport.', ['not to', 'to not', 'don’t'], 'not to',
     'Négation de l’infinitif : not to forget.'),
  ]),
  ex2=('Complète le rapport', 'Écris le mot manquant.', [
    ('« I’ll help you. » → He offered ______ help me. (la particule)', 'to',
     'Offer + TO + infinitif : he offered to help.'),
    ('« I’m sorry I shouted. » → She apologised ______ shouting. (la préposition)', 'for',
     'Apologise FOR + -ing.'),
    ('« Don’t touch it! » → He warned me not ______ touch it. (la particule)', 'to',
     'Warn sb not TO do.'),
    ('« Are you French? » → She asked me ______ I was French. (si)', 'if',
     'Question yes/no → if (ou whether).'),
    ('« It was me. » → He admitted ______ it. (do en -ing)', 'doing',
     'Admit + -ing : admitted doing it.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Elle a proposé d’aller au cinéma. »', ['She suggested going to the cinema.', 'She suggested to go to the cinema.', 'She suggested go to the cinema.'], 'She suggested going to the cinema.',
     'Suggérer de faire → suggest + -ing.'),
    ('« Il m’a demandé où j’habitais. »', ['He asked me where I lived.', 'He asked me where did I live.', 'He asked me where do you live.'], 'He asked me where I lived.',
     'Pas d’inversion dans la question rapportée.'),
    ('« Ils l’ont accusée d’avoir menti. »', ['They accused her of lying.', 'They accused her to lie.', 'They accused her for lying.'], 'They accused her of lying.',
     'Accuse sb of + -ing.'),
    ('« Il a refusé de signer le contrat. »', ['He refused to sign the contract.', 'He refused signing the contract.', 'He denied to sign the contract.'], 'He refused to sign the contract.',
     'Refuse + to + infinitif.'),
    ('« Elle m’a rappelé d’acheter du pain. »', ['She reminded me to buy some bread.', 'She remembered me to buy some bread.', 'She reminded me buying some bread.'], 'She reminded me to buy some bread.',
     'Remind sb to do — remember = se souvenir, remind = rappeler à quelqu’un.'),
  ]),
  game_desc='Chaque verbe de rapport passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('suggest-ing', 'suggest + -ing', 'proposer de faire', 'proposition', 'She <b>suggested going</b> early.', 'She suggested ______ early. (go en -ing)', 'going'),
    ('deny-ing', 'deny + -ing', 'nier avoir fait', 'négation', 'He <b>denied taking</b> the money.', 'He denied ______ the money. (take en -ing)', 'taking'),
    ('accuse-of', 'accuse sb of', 'accuser quelqu’un de', 'accusation', 'They <b>accused him of</b> lying.', 'They accused him ______ lying. (préposition)', 'of'),
    ('refuse-to', 'refuse to', 'refuser de faire', 'refus', 'She <b>refused to</b> answer.', 'She refused ______ answer. (particule)', 'to'),
    ('remind-to', 'remind sb to', 'rappeler à quelqu’un de', 'rappel', 'He <b>reminded me to</b> lock the door.', 'He ______ me to lock the door. (rappeler — prétérit)', 'reminded'),
    ('asked-if', 'asked if', 'a demandé si', 'question rapportée', 'She <b>asked if</b> I was ready.', 'She asked ______ I was ready. (si)', 'if'),
    ('apologise-for', 'apologise for', 's’excuser de', 'excuse', 'He <b>apologised for</b> being late.', 'He apologised ______ being late. (préposition)', 'for'),
    ('warn-not-to', 'warn sb not to', 'avertir de ne pas', 'avertissement', 'They <b>warned us not to</b> go.', 'They warned us ______ to go. (négation)', 'not'),
  ],
),

'used-to': dict(
  level='b2', section='grammaire', num='Ch. 17', short='Used To and Would',
  title='Used To and Would — Les habitudes du passé',
  subtitle='used to · would · be used to : trois structures, trois sens',
  slides=[
    ('Used to : l’imparfait d’habitude', None,
     '<p class="slide-explanation"><b>used to + infinitif</b> = une habitude ou un état du passé qui n’existe plus. C’est souvent la meilleure traduction de l’imparfait français.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I used to smoke.</b> (Je fumais — avant, plus maintenant.)</p>'
     '<p style="margin-top:8px"><b>There used to be a cinema here.</b> (Il y avait un cinéma ici.)</p></div>'
     '<p style="margin-top:16px">Négation et question : <b>didn’t use to</b> / <b>Did you use to...?</b> — sans le d final.</p>'),
    ('Would : les actions répétées seulement', None,
     '<p class="slide-explanation"><b>would + infinitif</b> raconte aussi les habitudes passées — mais uniquement les <b>actions répétées</b>, jamais les états.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Every summer, we would swim in the lake.</b> ✓ (action)</p>'
     '<p style="margin-top:8px">We <s>would have</s> a small house. ✗ → We <b>used to have</b> a small house. (état)</p></div>'
     '<p style="margin-top:16px">Règle simple : live, have, be, like, know (états) → used to seulement.</p>'),
    ('Be used to : être habitué à', None,
     '<p class="slide-explanation">Tout autre sens ! <b>be used to + -ing/nom</b> = être habitué à. Le « to » est une préposition → -ing derrière.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I’m used to getting up early.</b> (J’ai l’habitude de me lever tôt.)</p>'
     '<p style="margin-top:8px"><b>She isn’t used to the cold.</b> (Elle n’est pas habituée au froid.)</p></div>'),
    ('Get used to : s’habituer à', None,
     '<p class="slide-explanation"><b>get used to + -ing/nom</b> = le processus de s’habituer.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>You’ll get used to the noise.</b> (Tu t’habitueras au bruit.)</p>'
     '<p style="margin-top:8px"><b>I’m getting used to driving on the left.</b> (Je m’habitue à conduire à gauche.)</p></div>'),
    ('Les trois côte à côte', None,
     '<p class="slide-explanation">Le test du B2 adore les mélanger :</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I used to live in Spain.</b> (Avant, j’habitais en Espagne.)</p>'
     '<p style="margin-top:8px"><b>I’m used to living alone.</b> (J’ai l’habitude de vivre seul.)</p>'
     '<p style="margin-top:8px"><b>I’m getting used to living here.</b> (Je m’habitue à vivre ici.)</p></div>'
     '<p style="margin-top:16px">used to + <b>infinitif</b> · be/get used to + <b>-ing</b> — c’est la terminaison qui trahit le sens.</p>'),
  ],
  traps=[
    ('I use to play tennis when I was young.', 'I <strong>used to</strong> play tennis...', 'À l’affirmatif passé, c’est used to avec d. « Use to » seul n’existe qu’après did/didn’t.'),
    ('Did you used to live here?', 'Did you <strong>use to</strong> live here?', 'Après did, l’infinitif sans d : did you use to.'),
    ('We would have a big garden.', 'We <strong>used to have</strong> a big garden.', 'Have (état) ne va pas avec would ; les états exigent used to.'),
    ('I’m used to get up early.', 'I’m used to <strong>getting</strong> up early.', 'Dans be used to, to est une préposition → -ing.'),
    ('I can’t get used to live here.', 'I can’t get used to <strong>living</strong> here.', 'Get used to + -ing : s’habituer à vivre ici.'),
  ],
  summary=[
    ('Habitude passée', 'used to + infinitif', 'I used to smoke.'),
    ('Négation / question', 'didn’t use to / did... use to?', 'Did you use to live here?'),
    ('Actions répétées', 'would + infinitif (pas d’états)', 'We would swim every summer.'),
    ('Être habitué', 'be used to + -ing/nom', 'I’m used to getting up early.'),
    ('S’habituer', 'get used to + -ing/nom', 'You’ll get used to it.'),
  ],
  ex1=('Choisis la forme correcte', 'used to, would, be/get used to.', [
    ('I ______ in London, but I moved to Lyon in 2020.', ['used to live', 'would live', 'am used to living'], 'used to live',
     'Live est un état → used to live (would est impossible).'),
    ('Every Sunday, my grandfather ______ us stories.', ['would tell', 'was used to tell', 'use to tell'], 'would tell',
     'Action répétée du passé → would tell fonctionne (used to told n’existe pas, use to manque le d).'),
    ('She’s a nurse, so she ______ night shifts.', ['is used to working', 'used to work', 'gets used to work'], 'is used to working',
     'Elle a l’habitude (présent) → is used to + -ing.'),
    ('Don’t worry, you’ll soon ______ the new system.', ['get used to', 'used to', 'use to'], 'get used to',
     'S’habituer (processus futur) → get used to.'),
    ('______ you use to wear glasses?', ['Did', 'Would', 'Were'], 'Did',
     'Question d’habitude passée : Did you use to...?'),
    ('He ______ like coffee, but now he drinks it every day.', ['didn’t use to', 'didn’t used to', 'wouldn’t'], 'didn’t use to',
     'Négation : didn’t use to (sans d) ; like est un état, donc would est exclu.'),
  ]),
  ex2=('Complète la structure', 'Écris le mot manquant.', [
    ('There ______ to be a bakery on this corner. (le verbe d’habitude passée)', 'used',
     'There used to be — il y avait (mais plus maintenant).'),
    ('I’m not used to ______ up so early. (get en -ing)', 'getting',
     'Be used to + -ing : not used to getting up.'),
    ('Every winter, we ______ go skiing in the Alps. (le modal des actions répétées)', 'would',
     'Action répétée → would go.'),
    ('Did you use ______ play an instrument? (la particule)', 'to',
     'Did you use TO play...?'),
    ('She slowly ______ used to the British weather. (get au prétérit)', 'got',
     'Elle s’y est habituée → got used to.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Avant, je jouais au foot tous les samedis. »', ['I used to play football every Saturday.', 'I am used to playing football every Saturday.', 'I use to play football every Saturday.'], 'I used to play football every Saturday.',
     'Habitude passée révolue → used to play.'),
    ('« J’ai l’habitude de travailler sous pression. »', ['I’m used to working under pressure.', 'I used to work under pressure.', 'I would work under pressure.'], 'I’m used to working under pressure.',
     'Habitude actuelle → be used to + -ing.'),
    ('« Tu t’habitueras vite à la nourriture anglaise. »', ['You’ll soon get used to English food.', 'You’ll soon be use to English food.', 'You soon used to English food.'], 'You’ll soon get used to English food.',
     'Processus → get used to.'),
    ('« Il y avait une église ici. »', ['There used to be a church here.', 'There would be a church here.', 'It used to have a church here.'], 'There used to be a church here.',
     'État passé → there used to be (would + be d’état est exclu).'),
    ('Quelle phrase est INCORRECTE ?', ['We would live in a small flat.', 'We used to live in a small flat.', 'We lived in a small flat.'], 'We would live in a small flat.',
     'Live est un état : would est impossible — used to ou prétérit simple.'),
  ]),
  game_desc='Chaque structure d’habitude passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('used-to', 'used to + infinitif', 'habitude/état passé révolu', 'imparfait', 'I <b>used to</b> smoke.', 'I ______ to smoke, but I quit. (us...)', 'used'),
    ('didnt-use-to', 'didn’t use to', 'la négation (sans d)', 'négation', 'He <b>didn’t use to</b> like coffee.', 'He didn’t ______ to like coffee. (sans d)', 'use'),
    ('would-habit', 'would + action', 'action répétée du passé', 'répétition', 'We <b>would swim</b> in the lake every summer.', 'Every summer we ______ swim in the lake. (modal)', 'would'),
    ('be-used-to', 'be used to + -ing', 'être habitué à', 'habitude actuelle', 'I’m <b>used to getting</b> up early.', 'I’m used to ______ up early. (get en -ing)', 'getting'),
    ('get-used-to', 'get used to', 's’habituer à', 'processus', 'You’ll <b>get used to</b> the noise.', 'You’ll ______ used to the noise. (get)', 'get'),
    ('there-used-to', 'There used to be', 'il y avait (avant)', 'état passé', '<b>There used to be</b> a cinema here.', '______ used to be a cinema here. (mot d’existence)', 'there'),
    ('states-rule', 'états → used to seulement', 'live, have, be : jamais would', 'règle des états', 'We <b>used to have</b> a big garden.', 'We ______ to have a big garden. (pas would !)', 'used'),
    ('did-use-to', 'Did you use to...?', 'la question d’habitude', 'question', '<b>Did</b> you <b>use to</b> wear glasses?', '______ you use to wear glasses? (auxiliaire)', 'did'),
  ],
),

'verb-patterns': dict(
  level='b2', section='grammaire', num='Ch. 18', short='Verb Patterns',
  title='Verb Patterns — Verbe + objet + infinitif',
  subtitle='want sb to do · make/let · allow, encourage, expect',
  slides=[
    ('Want somebody to do', None,
     '<p class="slide-explanation">Le piège n° 1 du francophone : « je veux QUE tu viennes ». L’anglais ne dit jamais « want that » — c’est <b>want + objet + to + infinitif</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>I want you to come.</b> (Je veux que tu viennes.)</p>'
     '<p style="margin-top:8px"><b>She’d like us to wait.</b> (Elle aimerait que nous attendions.)</p></div>'
     '<p style="margin-top:16px">Même structure : <b>would like, expect, need, ask, tell</b> + objet + to do.</p>'),
    ('Make et let : sans to', None,
     '<p class="slide-explanation"><b>make sb do</b> (forcer) et <b>let sb do</b> (laisser) prennent l’infinitif <b>sans to</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>My parents made me tidy my room.</b> (m’ont obligé à ranger)</p>'
     '<p style="margin-top:8px"><b>They let me stay up late.</b> (m’ont laissé veiller)</p></div>'
     '<p style="margin-top:16px">Au passif, make récupère son to : <b>I was made to wait.</b> (Let n’a pas de passif — on dit was allowed to.)</p>'),
    ('Allow, encourage, persuade, teach', None,
     '<p class="slide-explanation">La grande famille du <b>verbe + objet + to + infinitif</b> : <b>allow, encourage, persuade, teach, advise, invite, remind, warn, order, force</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>They allowed us to leave early.</b></p>'
     '<p style="margin-top:8px"><b>She taught me to drive.</b></p>'
     '<p style="margin-top:8px"><b>He encouraged her to apply.</b></p></div>'),
    ('Help et les sens : deux cas souples', None,
     '<p class="slide-explanation"><b>help</b> accepte les deux : help sb (to) do. Les verbes de perception (<b>see, hear, watch, feel</b>) : infinitif sans to (action complète) ou -ing (action en cours).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>She helped me (to) carry the boxes.</b></p>'
     '<p style="margin-top:8px"><b>I saw him leave.</b> (je l’ai vu partir — tout)</p>'
     '<p style="margin-top:8px"><b>I saw him leaving.</b> (en train de partir)</p></div>'),
    ('Suggest : l’exception qui résiste', None,
     '<p class="slide-explanation"><b>Suggest n’entre jamais dans ce moule</b> : pas de « suggest me to do ». Trois options correctes :</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>She suggested taking a break.</b></p>'
     '<p style="margin-top:8px"><b>She suggested (that) we take a break.</b></p>'
     '<p style="margin-top:8px"><b>She suggested a break.</b></p></div>'
     '<p style="margin-top:16px">Même logique pour <b>explain</b> : explain something TO somebody — jamais « explain me ».</p>'),
  ],
  traps=[
    ('I want that you come with me.', 'I want <strong>you to come</strong> with me.', 'Want + objet + to + infinitif — jamais want that.'),
    ('She made me to apologise.', 'She made me <strong>apologise</strong>.', 'Make sb do — infinitif sans to à l’actif.'),
    ('My parents don’t let me to go out.', 'My parents don’t let me <strong>go</strong> out.', 'Let sb do — sans to, toujours.'),
    ('He suggested me to try again.', 'He suggested <strong>trying</strong> again. / He suggested <strong>that I try</strong> again.', 'Suggest refuse le moule objet + to do.'),
    ('Can you explain me the rule?', 'Can you explain <strong>the rule to me</strong>?', 'Explain something TO somebody — l’objet de la chose d’abord.'),
  ],
  summary=[
    ('Vouloir que', 'want/expect sb to do', 'I want you to come.'),
    ('Forcer', 'make sb do (sans to)', 'She made me apologise.'),
    ('Laisser', 'let sb do (sans to)', 'They let me stay.'),
    ('Permettre', 'allow sb to do', 'They allowed us to leave.'),
    ('Perception', 'see/hear sb do / doing', 'I saw him leave / leaving.'),
    ('Exceptions', 'suggest + -ing · explain sth to sb', 'She suggested taking a break.'),
  ],
  ex1=('Choisis la forme correcte', 'Verbe + objet + infinitif (avec ou sans to).', [
    ('My boss wants ______ the report today.', ['me to finish', 'that I finish', 'me finishing'], 'me to finish',
     'Want + objet + to + infinitif : wants me to finish.'),
    ('The teacher made us ______ the exercise again.', ['do', 'to do', 'doing'], 'do',
     'Make sb do — sans to.'),
    ('Her parents won’t let her ______ to the party.', ['go', 'to go', 'going'], 'go',
     'Let sb do — sans to.'),
    ('The school allows students ______ their phones at lunch.', ['to use', 'use', 'using'], 'to use',
     'Allow + objet + to + infinitif.'),
    ('I heard someone ______ my name.', ['call', 'to call', 'that called'], 'call',
     'Verbe de perception + infinitif sans to : heard someone call.'),
    ('He was made ______ for an hour.', ['to wait', 'wait', 'waiting'], 'to wait',
     'Au passif, make récupère son to : was made to wait.'),
  ]),
  ex2=('Complète le motif', 'Écris le mot manquant.', [
    ('I’d like you ______ meet my parents. (la particule)', 'to',
     'Would like + objet + TO + infinitif.'),
    ('She taught her brother ______ swim. (la particule)', 'to',
     'Teach sb TO do.'),
    ('They didn’t ______ us take photos inside. (laisser)', 'let',
     'Let sb do : ne nous ont pas laissés photographier.'),
    ('The film ______ me cry. (faire — prétérit)', 'made',
     'Make sb do : the film made me cry.'),
    ('I expect everyone ______ be on time. (la particule)', 'to',
     'Expect + objet + TO be.'),
  ]),
  ex3=('Traduis le sens', 'Choisis la phrase anglaise qui correspond.', [
    ('« Je veux que tu m’écoutes. »', ['I want you to listen to me.', 'I want that you listen to me.', 'I want you listen me.'], 'I want you to listen to me.',
     'Want + objet + to + infinitif.'),
    ('« Mes parents m’ont obligé à rester. »', ['My parents made me stay.', 'My parents made me to stay.', 'My parents let me stay.'], 'My parents made me stay.',
     'Obliger = make sb do, sans to.'),
    ('« Elle m’a laissé conduire sa voiture. »', ['She let me drive her car.', 'She let me to drive her car.', 'She allowed me drive her car.'], 'She let me drive her car.',
     'Let sb do, sans to (allow exigerait to drive).'),
    ('« Il m’a appris à cuisiner. »', ['He taught me to cook.', 'He learned me to cook.', 'He taught me cooking to.'], 'He taught me to cook.',
     'Teach sb to do — learn = apprendre soi-même.'),
    ('« Je l’ai vue partir. »', ['I saw her leave.', 'I saw her to leave.', 'I saw that she leaves.'], 'I saw her leave.',
     'Perception + infinitif sans to : saw her leave.'),
  ]),
  game_desc='Chaque motif verbal passe par trois types de questions : sens, contexte et production. Atteins 100 points pour gagner.',
  items=[
    ('want-sb-to', 'want sb to do', 'vouloir que quelqu’un fasse', 'volonté', 'I <b>want you to</b> come.', 'I want you ______ come. (particule)', 'to'),
    ('make-sb-do', 'make sb do', 'obliger (sans to)', 'contrainte', 'She <b>made me apologise</b>.', 'She made me ______. (s’excuser — base verbale)', 'apologise'),
    ('let-sb-do', 'let sb do', 'laisser (sans to)', 'permission', 'They <b>let me stay</b> up late.', 'They let me ______ up late. (rester — base verbale)', 'stay'),
    ('allow-sb-to', 'allow sb to do', 'permettre (avec to)', 'autorisation', 'They <b>allowed us to</b> leave early.', 'They allowed us ______ leave early. (particule)', 'to'),
    ('teach-sb-to', 'teach sb to do', 'apprendre à quelqu’un', 'enseignement', 'She <b>taught me to</b> drive.', 'She ______ me to drive. (enseigner — prétérit)', 'taught'),
    ('see-sb-do', 'see sb do', 'voir quelqu’un faire (complet)', 'perception', 'I <b>saw him leave</b>.', 'I saw him ______. (partir — base verbale)', 'leave'),
    ('was-made-to', 'was made to', 'le passif de make (avec to)', 'passif', 'I <b>was made to</b> wait.', 'I was made ______ wait. (particule)', 'to'),
    ('explain-to', 'explain sth to sb', 'expliquer quelque chose à', 'exception', 'Can you <b>explain</b> the rule <b>to</b> me?', 'Can you explain the rule ______ me? (préposition)', 'to'),
  ],
),

}
