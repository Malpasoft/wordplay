# -*- coding: utf-8 -*-
"""espanol-en A2 writing content — 3 chapters."""

CHAPTERS = {

'postcard': dict(
  num='W3', short='A Postcard', title='Writing a Postcard — Una Postal',
  subtitle='Greetings, describing your holiday, signing off',
  slides=[
    ('The shape of a postcard', None,
     '<p class="slide-explanation">A Spanish postcard has four short parts: a greeting, where you are, what you are doing / what it is like, and a sign-off.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¡Hola, Marta!</b> (greeting)</p>'
     '<p style="margin-top:8px"><b>Estoy en Valencia con mi familia.</b> (where)</p>'
     '<p style="margin-top:8px"><b>Hace sol y la playa es preciosa.</b> (what it is like)</p>'
     '<p style="margin-top:8px"><b>¡Hasta pronto! Un beso, Ana.</b> (sign-off)</p></div>'),
    ('Greetings and sign-offs', None,
     '<p class="slide-explanation">Postcards are informal — use warm openings and closings.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>Open: <b>¡Hola, + name! · Querido Juan / Querida Ana</b> (Dear...)</p>'
     '<p style="margin-top:8px">Close: <b>Un beso · Un abrazo · Hasta pronto · Saludos desde Valencia</b></p></div>'
     '<p style="margin-top:16px">Querido agrees: quer<b>ido</b> Juan, quer<b>ida</b> Ana.</p>'),
    ('Saying where you are', None,
     '<p class="slide-explanation">Location and feelings use <b>estar</b>; descriptions of the place use <b>ser</b>.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Estoy en Sevilla.</b> (I am in Seville.) — location → estar</p>'
     '<p style="margin-top:8px"><b>La ciudad es preciosa.</b> (The city is beautiful.) — description → ser</p>'
     '<p style="margin-top:8px"><b>Estamos muy contentos.</b> (We are very happy.) — feeling → estar</p></div>'),
    ('Weather and activities', None,
     '<p class="slide-explanation">Weather uses <b>hace</b>; current activities use <b>estar + gerundio</b> or the simple present.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hace sol / calor / buen tiempo.</b> (It is sunny / hot / nice weather.)</p>'
     '<p style="margin-top:8px"><b>Estamos visitando la catedral.</b> (We are visiting the cathedral.)</p>'
     '<p style="margin-top:8px"><b>Mañana vamos a la playa.</b> (Tomorrow we are going to the beach.)</p></div>'),
    ('What you have done', None,
     '<p class="slide-explanation">Use the pretérito perfecto for what you have done so far on the trip.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Hemos visitado el museo.</b> (We have visited the museum.)</p>'
     '<p style="margin-top:8px"><b>He comido una paella riquísima.</b> (I have eaten a delicious paella.)</p></div>'),
  ],
  traps=[
    ('Querido Ana,', '<strong>Querida</strong> Ana,', 'Querido agrees with the person: querida for a woman'),
    ('Soy en Valencia.', '<strong>Estoy</strong> en Valencia.', 'Location always takes estar, never ser'),
    ('Es sol y calor.', '<strong>Hace</strong> sol y calor.', 'Weather uses hace: hace sol, hace calor'),
    ('Un beso, ¡hasta pronto! (as the opening)', 'Open with <strong>¡Hola!</strong> / <strong>Querida...</strong>', 'Besos and abrazos close a postcard — they never open it'),
    ('La playa está preciosa cada año.', 'La playa <strong>es</strong> preciosa.', 'A permanent description of the place takes ser'),
  ],
  summary=[
    ('Greeting', '¡Hola...! / Querido/a + name', '¡Hola, Marta!'),
    ('Where', 'Estoy/Estamos en + place', 'Estoy en Valencia.'),
    ('Weather', 'Hace + sol/calor/frío', 'Hace muy buen tiempo.'),
    ('Activities', 'estar + gerundio / ir a + inf', 'Estamos visitando la catedral.'),
    ('Done so far', 'pretérito perfecto', 'Hemos visitado el museo.'),
    ('Sign-off', 'Un beso / Un abrazo / Hasta pronto', 'Un abrazo, Ana.'),
  ],
  ex1=('Choose the right phrase', 'Tap the best option for each gap in the postcard.', [
    ('______ Marta: ¿qué tal todo?', ['Querida', 'Querido', 'Un beso'], 'Querida',
     'Marta is a woman → querida. Un beso is a closing, not an opening.'),
    ('______ en Granada con mis padres.', ['Estoy', 'Soy', 'Hay'], 'Estoy',
     'Location takes estar: estoy en Granada.'),
    ('______ mucho calor todos los días.', ['Hace', 'Es', 'Está'], 'Hace',
     'Weather expressions use hacer: hace calor.'),
    ('La ciudad ______ preciosa.', ['es', 'está', 'hace'], 'es',
     'A general description of the city takes ser: es preciosa.'),
    ('Hoy ______ visitando la Alhambra.', ['estamos', 'somos', 'hacemos'], 'estamos',
     'Ongoing activity: estar + gerundio — estamos visitando.'),
    ('¡Hasta pronto! ______ , Ana.', ['Un abrazo', 'Querida', 'Estoy'], 'Un abrazo',
     'The closing formula: un abrazo (or un beso) + your name.'),
  ]),
  ex2=('Complete the postcard', 'Type the missing word — no accents needed.', [
    ('¡______ , Pablo! ¿Cómo estás? (informal greeting)', 'hola',
     'The simplest warm opening: ¡Hola, Pablo!'),
    ('Estamos ______ Mallorca desde el lunes. (in)', 'en',
     'Estar en + place: estamos en Mallorca.'),
    ('______ sol y la playa es preciosa. (weather word)', 'hace',
     'Hace sol — weather uses hacer.'),
    ('Hemos ______ el castillo y el mercado. (visited)', 'visitado',
     'Pretérito perfecto: hemos visitado — regular -ar participle.'),
    ('Un ______ muy fuerte, Carmen. (hug)', 'abrazo',
     'Un abrazo = a hug, the classic sign-off.'),
  ]),
  ex3=('Order and usage', 'Choose the correct option.', [
    ('The natural order of a postcard is...', ['greeting → place → activities → sign-off', 'sign-off → place → greeting', 'activities → greeting → place'], 'greeting → place → activities → sign-off',
     'Open, say where you are and what it is like, then close warmly.'),
    ('"Saludos desde Sevilla" means...', ['Greetings from Seville', 'Goodbye to Seville', 'I arrived in Seville'], 'Greetings from Seville',
     'Desde marks the origin: greetings from Seville.'),
    ('Which closing is for a postcard to a close friend?', ['Un beso', 'Atentamente', 'Estimado señor'], 'Un beso',
     'Un beso is warm and informal; the other two are formal-letter language.'),
    ('"Lo estamos pasando genial" means...', ['We are having a great time.', 'We are passing by.', 'It is genial weather.'], 'We are having a great time.',
     'Pasarlo genial/bien = to have a great/good time.'),
    ('Which sentence belongs in a postcard?', ['Mañana vamos a la playa.', 'Adjunto mi currículum.', 'Le escribo para quejarme.'], 'Mañana vamos a la playa.',
     'Holiday plans fit a postcard; the others belong to formal letters.'),
  ]),
  game_desc='Each postcard phrase passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('querida', 'Querido / Querida', 'Dear - agrees with the person', 'warm opening', '<b>Querida</b> Marta: ¿qué tal todo?', '______ Marta: ¿qué tal todo? (Dear, fem.)', 'querida'),
    ('estoy-en', 'estoy en', 'I am in - location with estar', 'location phrase', '<b>Estoy en</b> Valencia con mi familia.', '______ ______ Valencia con mi familia. (I am in)', 'estoy en'),
    ('hace-sol', 'hace sol', 'it is sunny - weather with hacer', 'weather phrase', '<b>Hace sol</b> y la playa es preciosa.', '______ sol y la playa es preciosa.', 'hace'),
    ('lo-pasamos', 'pasarlo genial', 'to have a great time', 'enjoyment phrase', 'Lo estamos <b>pasando genial</b>.', 'Lo estamos ______ genial. (having)', 'pasando'),
    ('hemos-visitado', 'hemos visitado', 'we have visited - perfect tense for the trip so far', 'trip so far', '<b>Hemos visitado</b> el museo.', '______ visitado el museo. (we have)', 'hemos'),
    ('manana-vamos', 'mañana vamos a', 'tomorrow we are going to - plans', 'future plan', 'Mañana <b>vamos a</b> la playa.', 'Mañana ______ a la playa. (we go)', 'vamos'),
    ('un-abrazo', 'un abrazo', 'a hug - warm sign-off', 'sign-off', '¡Hasta pronto! <b>Un abrazo</b>, Ana.', '¡Hasta pronto! Un ______ , Ana.', 'abrazo'),
    ('saludos-desde', 'saludos desde', 'greetings from - classic postcard line', 'greetings line', '<b>Saludos desde</b> Sevilla.', '______ desde Sevilla. (greetings)', 'saludos'),
  ],
  ref_rows=[
    ('Open', '¡Hola, + name! · Querido Juan / Querida Ana'),
    ('Where you are', 'Estoy/Estamos en… · desde el lunes'),
    ('Weather', 'Hace sol / calor / buen tiempo · Llueve un poco'),
    ('Activities', 'Estamos visitando… · Mañana vamos a… · Hemos visitado…'),
    ('Feelings', 'Lo estamos pasando genial · Estamos muy contentos'),
    ('Close', 'Un beso · Un abrazo · Hasta pronto · Saludos desde…'),
  ],
  task='Write a holiday postcard in Spanish (35–45 words) to a friend: greet them, say where you are and who with, describe the weather, mention one thing you have done and one plan for tomorrow, then sign off warmly.',
  model='¡Hola, Marta! Estoy en Valencia con mi familia. Hace sol y mucho calor. Hemos visitado la Ciudad de las Artes y he comido una paella riquísima. Mañana vamos a la playa. ¡Lo estamos pasando genial! Un beso, Ana.',
),

'informal-email': dict(
  num='W2', short='An Informal Email', title='Writing an Informal Email — Un Correo Informal',
  subtitle='Openings, asking about news, making plans, closing',
  slides=[
    ('The shape of an informal email', None,
     '<p class="slide-explanation">Greeting → thanks / reaction to their news → your news → a question or plan → closing.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¡Hola, Leo! ¿Qué tal?</b></p>'
     '<p style="margin-top:8px"><b>Gracias por tu correo. ¡Qué buena noticia!</b></p>'
     '<p style="margin-top:8px"><b>Yo estoy muy liado con los exámenes...</b></p>'
     '<p style="margin-top:8px"><b>¿Por qué no quedamos el sábado?</b></p>'
     '<p style="margin-top:8px"><b>¡Escríbeme pronto! Un abrazo, Dani.</b></p></div>'),
    ('Openings', None,
     '<p class="slide-explanation">Informal Spanish emails open with hola and a how-are-you.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¡Hola, Leo! ¿Qué tal? · ¿Cómo estás? · ¿Cómo te va?</b></p>'
     '<p style="margin-top:8px"><b>Gracias por tu correo / tu mensaje.</b> (Thanks for your email.)</p>'
     '<p style="margin-top:8px"><b>Perdona por tardar en contestar.</b> (Sorry for taking so long to reply.)</p></div>'),
    ('Reacting to news', None,
     '<p class="slide-explanation">React before giving your own news — it keeps the email friendly.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¡Qué buena noticia!</b> (What great news!) · <b>¡Enhorabuena!</b> (Congratulations!)</p>'
     '<p style="margin-top:8px"><b>¡Qué pena!</b> (What a shame!) · <b>¡No me lo puedo creer!</b> (I can\'t believe it!)</p></div>'),
    ('Making plans', None,
     '<p class="slide-explanation">Suggest meeting with <b>quedar</b> (to arrange to meet) — a key verb English speakers miss.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¿Por qué no quedamos el sábado?</b> (Why don\'t we meet on Saturday?)</p>'
     '<p style="margin-top:8px"><b>¿Te apetece ir al cine?</b> (Do you fancy going to the cinema?)</p>'
     '<p style="margin-top:8px"><b>Si quieres, puedo pasar por tu casa.</b> (If you like, I can come by your place.)</p></div>'),
    ('Closings', None,
     '<p class="slide-explanation">Ask them to write back, then sign off informally.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>¡Escríbeme pronto!</b> (Write soon!) · <b>Cuéntame cosas.</b> (Tell me your news.)</p>'
     '<p style="margin-top:8px"><b>Un abrazo · Un beso · Nos vemos · Hasta pronto</b></p></div>'),
  ],
  traps=[
    ('Estimado Leo: (to a friend)', '<strong>¡Hola, Leo!</strong>', 'Estimado is formal-letter language — friends get ¡Hola!'),
    ('Gracias para tu correo.', 'Gracias <strong>por</strong> tu correo.', 'Thanks for = gracias por, never para'),
    ('¿Quieres meet el sábado?', '¿Por qué no <strong>quedamos</strong> el sábado?', 'Arranging to meet = quedar — a verb English speakers forget'),
    ('Atentamente, Dani (to a friend)', '<strong>Un abrazo,</strong> Dani', 'Atentamente closes formal letters; friends get un abrazo/beso'),
    ('Escríbeme prontamente.', '¡Escríbeme <strong>pronto</strong>!', 'Pronto is already the adverb — no -mente needed'),
  ],
  summary=[
    ('Open', '¡Hola...! ¿Qué tal?', '¡Hola, Leo! ¿Qué tal?'),
    ('Thank / apologise', 'Gracias por tu correo · Perdona por tardar', 'Gracias por tu mensaje.'),
    ('React', '¡Qué buena noticia! · ¡Qué pena!', '¡Enhorabuena!'),
    ('Suggest', '¿Por qué no quedamos...? · ¿Te apetece...?', '¿Te apetece ir al cine?'),
    ('Close', '¡Escríbeme pronto! + Un abrazo', 'Un abrazo, Dani.'),
  ],
  ex1=('Choose the right phrase', 'Tap the best option for each gap.', [
    ('¡Hola, Marta! ¿______ tal?', ['Qué', 'Cómo', 'Cuál'], 'Qué',
     'The fixed greeting is ¿Qué tal? — how are things?'),
    ('Gracias ______ tu correo.', ['por', 'para', 'de'], 'por',
     'Thanks for something received = gracias por.'),
    ('¡______ ! Me alegro mucho por ti. (Congratulations)', ['Enhorabuena', 'Qué pena', 'Perdona'], 'Enhorabuena',
     'Enhorabuena congratulates; qué pena commiserates.'),
    ('¿Por qué no ______ el viernes por la tarde?', ['quedamos', 'encontramos a', 'reunimos que'], 'quedamos',
     'Quedar = to arrange to meet: ¿por qué no quedamos?'),
    ('¿Te ______ ir al cine esta noche?', ['apetece', 'apeteces', 'gusta a'], 'apetece',
     'Apetecer works like gustar: ¿te apetece + infinitive?'),
    ('¡Escríbeme ______ ! Un abrazo.', ['pronto', 'prontamente', 'rápida'], 'pronto',
     'Pronto is the adverb: write soon. No -mente form is needed.'),
  ]),
  ex2=('Complete the email', 'Type the missing word — no accents needed.', [
    ('______ por tardar en contestar. (sorry)', 'perdona',
     'Perdona por + infinitive = sorry for (doing something).'),
    ('¡Qué buena ______ ! (news)', 'noticia',
     '¡Qué buena noticia! = what great news!'),
    ('Si quieres, ______ pasar por tu casa. (I can)', 'puedo',
     'Offering: puedo pasar por tu casa — I can come by.'),
    ('______ cosas — quiero saberlo todo. (tell me)', 'cuentame',
     'Cuéntame cosas = tell me your news (accent optional when typing).'),
    ('Nos ______ el sábado entonces. (we see each other)', 'vemos',
     'Nos vemos = see you — also a closing formula.'),
  ]),
  ex3=('Register check', 'Choose the correct option.', [
    ('Which opening fits an email to a friend?', ['¡Hola, Juan! ¿Cómo te va?', 'Estimado Sr. García:', 'Muy señor mío:'], '¡Hola, Juan! ¿Cómo te va?',
     'The other two are formal-letter openings.'),
    ('"¿Te apetece...?" is used to...', ['suggest something appealing', 'apologise', 'complain'], 'suggest something appealing',
     'Apetecer = to fancy / feel like: do you fancy...?'),
    ('Which closing is WRONG for a friend?', ['Atentamente', 'Un beso', 'Nos vemos'], 'Atentamente',
     'Atentamente = yours faithfully — formal only.'),
    ('"Quedamos a las ocho" means...', ['We are meeting at eight.', 'We stayed at eight.', 'There are eight left.'], 'We are meeting at eight.',
     'Quedar (to arrange to meet): quedamos a las ocho.'),
    ('The friendly order is...', ['react to their news, then give yours', 'give your news only', 'close, then open'], 'react to their news, then give yours',
     'Reacting first (¡qué buena noticia!) keeps the email warm and connected.'),
  ]),
  game_desc='Each email phrase passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('que-tal', '¿Qué tal?', 'how are things - the universal informal greeting', 'informal greeting', '¡Hola, Leo! ¿<b>Qué tal</b>?', '¡Hola, Leo! ¿______ tal?', 'que'),
    ('gracias-por', 'gracias por', 'thanks for - always por, never para', 'thanking', '<b>Gracias por</b> tu correo.', '______ ______ tu correo. (thanks for)', 'gracias por'),
    ('perdona-por', 'perdona por tardar', 'sorry for taking so long - apology opener', 'apologising', '<b>Perdona por tardar</b> en contestar.', '______ por tardar en contestar. (sorry)', 'perdona'),
    ('enhorabuena', '¡Enhorabuena!', 'congratulations - reacting to good news', 'congratulating', '¡<b>Enhorabuena</b> por el trabajo nuevo!', '¡______ por el trabajo nuevo!', 'enhorabuena'),
    ('que-pena', '¡Qué pena!', 'what a shame - reacting to bad news', 'commiserating', '¡<b>Qué pena</b> lo de tu viaje!', '¡Qué ______ lo de tu viaje!', 'pena'),
    ('quedamos', '¿Por qué no quedamos?', 'why do we not meet up - making plans with quedar', 'arranging to meet', '¿Por qué no <b>quedamos</b> el sábado?', '¿Por qué no ______ el sábado?', 'quedamos'),
    ('te-apetece', '¿Te apetece...?', 'do you fancy - suggesting, works like gustar', 'suggesting', '¿<b>Te apetece</b> ir al cine?', '¿Te ______ ir al cine?', 'apetece'),
    ('escribeme', '¡Escríbeme pronto!', 'write to me soon - classic closing', 'closing line', '¡<b>Escríbeme pronto</b>! Un abrazo.', '¡______ pronto! Un abrazo. (write to me)', 'escribeme'),
  ],
  ref_rows=[
    ('Open', '¡Hola, + name! ¿Qué tal? · ¿Cómo te va?'),
    ('Thank / apologise', 'Gracias por tu correo · Perdona por tardar en contestar'),
    ('React', '¡Qué buena noticia! · ¡Enhorabuena! · ¡Qué pena!'),
    ('Your news', 'Estoy muy liado/a con… · ¿Sabes qué? …'),
    ('Plans', '¿Por qué no quedamos…? · ¿Te apetece…? · Si quieres…'),
    ('Close', '¡Escríbeme pronto! · Cuéntame cosas · Un abrazo / Un beso'),
  ],
  task='Write an informal email in Spanish (40–50 words) replying to a friend who has just got a new job: greet them, react to their news, give one piece of your own news, suggest meeting up at the weekend, and close asking them to write back.',
  model='¡Hola, Leo! ¿Qué tal? ¡Enhorabuena por el trabajo nuevo, qué buena noticia! Yo estoy muy liado con los exámenes, pero termino el viernes. ¿Por qué no quedamos el sábado para celebrarlo? ¡Escríbeme pronto y cuéntame cosas! Un abrazo, Dani.',
),

'description': dict(
  num='W1', short='A Description', title='Writing a Description — Una Descripción',
  subtitle='Describe people and places with ser, estar, tener and hay',
  slides=[
    ('Describing people: ser + tener', None,
     '<p class="slide-explanation">Use <b>ser</b> for character and appearance, <b>tener</b> for features and age.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Mi hermana es alta y simpática.</b> (My sister is tall and friendly.)</p>'
     '<p style="margin-top:8px"><b>Tiene el pelo largo y los ojos verdes.</b> (She has long hair and green eyes.)</p>'
     '<p style="margin-top:8px"><b>Tiene veinte años.</b> (She is twenty.) — age uses tener!</p></div>'),
    ('Adjective agreement', None,
     '<p class="slide-explanation">Every adjective agrees with the noun in gender and number — the trap English speakers fall into most.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>un chico alto → una chica alta → unos chicos altos</b></p>'
     '<p style="margin-top:8px"><b>El piso es pequeño pero las habitaciones son luminosas.</b></p></div>'),
    ('Describing places: hay + estar', None,
     '<p class="slide-explanation"><b>Hay</b> = there is/are (what exists). <b>Estar</b> = where things are located.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>En mi barrio hay un parque y dos cafeterías.</b> (In my neighbourhood there is a park and two cafés.)</p>'
     '<p style="margin-top:8px"><b>El parque está cerca de mi casa.</b> (The park is near my house.)</p></div>'),
    ('Useful structure for a description', None,
     '<p class="slide-explanation">Move from general to specific: introduce → describe → say what you like.</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p>1. <b>Mi mejor amiga se llama Carla.</b> (introduce)</p>'
     '<p style="margin-top:8px">2. <b>Es baja y muy graciosa. Tiene el pelo rizado.</b> (describe)</p>'
     '<p style="margin-top:8px">3. <b>Lo que más me gusta de ella es su sentido del humor.</b> (what you like)</p></div>'),
    ('Connectors for richer sentences', None,
     '<p class="slide-explanation">Join short sentences with y, pero, también, además (besides), aunque (although).</p>'
     '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
     '<p><b>Es tranquilo pero muy divertido. Además, cocina genial.</b></p>'
     '<p style="margin-top:8px"><b>Aunque es pequeño, mi barrio tiene de todo.</b></p></div>'),
  ],
  traps=[
    ('Mi hermana es alto.', 'Mi hermana es <strong>alta</strong>.', 'Adjectives agree: hermana → alta'),
    ('Ella es veinte años.', 'Ella <strong>tiene</strong> veinte años.', 'Age uses tener, never ser'),
    ('En mi barrio es un parque.', 'En mi barrio <strong>hay</strong> un parque.', 'What exists = hay; ser does not introduce things'),
    ('El parque es cerca de mi casa.', 'El parque <strong>está</strong> cerca de mi casa.', 'Location takes estar'),
    ('Tiene pelo largo y ojos verde.', 'Tiene el pelo largo y los ojos <strong>verdes</strong>.', 'Ojos is plural — verdes; and Spanish uses el/los with features'),
  ],
  summary=[
    ('Character / looks', 'ser + adjective (agrees)', 'Es alta y simpática.'),
    ('Features', 'tener + el pelo / los ojos...', 'Tiene los ojos verdes.'),
    ('Age', 'tener + años', 'Tiene veinte años.'),
    ('What exists', 'hay + noun', 'Hay un parque.'),
    ('Location', 'estar + place', 'Está cerca de mi casa.'),
    ('Connectors', 'y, pero, también, además, aunque', 'Es tranquilo pero divertido.'),
  ],
  ex1=('Choose the correct word', 'Tap the best option for each sentence.', [
    ('Mi madre ______ muy simpática.', ['es', 'está', 'tiene'], 'es',
     'Character description → ser: es simpática.'),
    ('Mi hermano ______ quince años.', ['tiene', 'es', 'está'], 'tiene',
     'Age always uses tener: tiene quince años.'),
    ('En mi calle ______ una farmacia.', ['hay', 'es', 'está'], 'hay',
     'Introducing what exists → hay una farmacia.'),
    ('La estación ______ al lado del río.', ['está', 'es', 'hay'], 'está',
     'Location → estar: está al lado del río.'),
    ('Mis primas son muy ______ .', ['divertidas', 'divertidos', 'divertida'], 'divertidas',
     'Primas is feminine plural: divertidas.'),
    ('Tiene el pelo ______ y corto.', ['rizado', 'rizada', 'rizados'], 'rizado',
     'Pelo is masculine singular: rizado.'),
  ]),
  ex2=('Complete the description', 'Type the missing word — no accents needed.', [
    ('Mi mejor amigo se ______ Hugo. (is called)', 'llama',
     'Introducing someone: se llama Hugo.'),
    ('Es alto y ______ los ojos marrones. (has)', 'tiene',
     'Features use tener: tiene los ojos marrones.'),
    ('En mi barrio ______ dos parques. (there are)', 'hay',
     'Hay covers both there is and there are: hay dos parques.'),
    ('Mi casa ______ cerca del centro. (is located)', 'esta',
     'Location → está (accent optional when typing).'),
    ('Es tranquilo ______ muy divertido. (but)', 'pero',
     'Contrast connector: pero.'),
  ]),
  ex3=('Agreement and usage', 'Choose the correct option.', [
    ('Which is correct?', ['Las habitaciones son luminosas.', 'Las habitaciones son luminosos.', 'Las habitaciones es luminosa.'], 'Las habitaciones son luminosas.',
     'Plural feminine noun → son luminosas: verb and adjective both agree.'),
    ('"Lo que más me gusta de ella es..." means...', ['What I like most about her is...', 'The thing she likes most is...', 'I like her the most because...'], 'What I like most about her is...',
     'Lo que más me gusta de... = what I like most about...'),
    ('Hay vs está:', ['hay introduces; está locates', 'they are interchangeable', 'está introduces; hay locates'], 'hay introduces; está locates',
     'Hay un parque (it exists); el parque está cerca (where it is).'),
    ('Which sentence is WRONG?', ['Mi abuela es ochenta años.', 'Mi abuela tiene ochenta años.', 'Mi abuela es muy activa.'], 'Mi abuela es ochenta años.',
     'Age needs tener — ser + years is the classic English-speaker error.'),
    ('"Además" is used to...', ['add another point', 'contrast two ideas', 'give a reason'], 'add another point',
     'Además = besides / what is more — it stacks another point.'),
  ]),
  game_desc='Each description tool passes through three question types: meaning, context and production. Reach 100 points to win.',
  items=[
    ('se-llama', 'se llama', 'is called - introducing a person', 'introducing', 'Mi mejor amiga <b>se llama</b> Carla.', 'Mi mejor amiga ______ ______ Carla.', 'se llama'),
    ('es-adj', 'es + adjective', 'is - character and looks with ser', 'describing with ser', 'Carla <b>es</b> baja y muy graciosa.', 'Carla ______ baja y muy graciosa.', 'es'),
    ('tiene-pelo', 'tiene el pelo...', 'has ... hair - features with tener', 'features', '<b>Tiene el pelo</b> rizado y los ojos verdes.', '______ el pelo rizado. (she has)', 'tiene'),
    ('tiene-anos', 'tiene ... años', 'is ... years old - age with tener', 'age', '<b>Tiene veinte años</b>.', '______ veinte años. (she is, age)', 'tiene'),
    ('hay', 'hay', 'there is or there are - what exists', 'existence', 'En mi barrio <b>hay</b> un parque.', 'En mi barrio ______ un parque.', 'hay'),
    ('esta-cerca', 'está cerca de', 'is near - location with estar', 'location', 'El parque <b>está cerca de</b> mi casa.', 'El parque ______ cerca de mi casa.', 'esta'),
    ('lo-que-mas', 'lo que más me gusta', 'what I like most - evaluation frame', 'evaluating', '<b>Lo que más me gusta</b> es su humor.', 'Lo que ______ me gusta es su humor.', 'mas'),
    ('ademas', 'además', 'besides or what is more - adding a point', 'adding', '<b>Además</b>, cocina genial.', '______ , cocina genial. (besides)', 'ademas'),
  ],
  ref_rows=[
    ('Introduce', 'Mi mejor amigo/a se llama… · Mi barrio se llama…'),
    ('Character / looks', 'Es alto/a, simpático/a, gracioso/a… (agree!)'),
    ('Features', 'Tiene el pelo largo / los ojos verdes · Tiene … años'),
    ('Places', 'Hay un parque / dos cafeterías · Está cerca de…'),
    ('Opinion', 'Lo que más me gusta es… · Me encanta porque…'),
    ('Connectors', 'y · pero · también · además · aunque'),
  ],
  task='Write a description in Spanish (40–50 words) of your best friend OR your neighbourhood: introduce them/it, give physical details (ser/tener or hay/estar), say what you like most, and join your sentences with connectors.',
  model='Mi mejor amiga se llama Carla y tiene veintidós años. Es baja, morena y muy graciosa. Tiene el pelo rizado y los ojos verdes. Aunque es un poco tímida, le encanta cantar. Lo que más me gusta de ella es su sentido del humor.',
),
}
