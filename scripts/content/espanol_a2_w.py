# espanol_a2_w.py — Main Spanish A2 Writing — 3 chapters (monolingual, all in Spanish)

CHAPTERS = {}

CHAPTERS['correo-informal'] = dict(
    level='a2', section='writing', num='W01', short='El Correo Informal',
    title='El Correo Informal — Escribir a Amigos y Familia',
    subtitle='Aprende a escribir correos electrónicos informales con estructura y vocabulario adecuados',
    game_desc='Practica la estructura y el vocabulario del correo informal en español.',
    slides=[
        ('Estructura del correo informal', None,
         '<p class="slide-explanation">Un correo informal tiene cinco partes: asunto, saludo, cuerpo, despedida y firma.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Asunto:</b> ¡Hola desde Málaga!</p>'
         '<p style="margin-top:6px"><b>Saludo:</b> ¡Hola, Carmen! / Querida Carmen:</p>'
         '<p style="margin-top:6px"><b>Cuerpo:</b> información principal</p>'
         '<p style="margin-top:6px"><b>Despedida:</b> Un beso / Un abrazo / Hasta pronto</p>'
         '<p style="margin-top:6px"><b>Firma:</b> tu nombre</p></div>'),
        ('Saludos y despedidas informales', None,
         '<p class="slide-explanation">Los correos informales usan un tono cálido. La elección del saludo y la despedida marcan el grado de familiaridad.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Saludos:</b> ¡Hola, + nombre! · Querido/a + nombre: · ¡Buenas!</p>'
         '<p style="margin-top:8px"><b>Despedidas:</b> Un beso · Un abrazo · Hasta pronto · Cuídate · Con cariño</p></div>'
         '<p style="margin-top:16px">Querido/a concuerda con el género del destinatario.</p>'),
        ('Hablar del pasado con el pretérito indefinido', None,
         '<p class="slide-explanation">Para contar lo que hiciste usas el pretérito indefinido.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Fui</b> a la playa el sábado. (ir)</p>'
         '<p style="margin-top:8px"><b>Comí</b> en un restaurante increíble. (comer)</p>'
         '<p style="margin-top:8px"><b>Vimos</b> una película muy divertida. (ver)</p></div>'),
        ('Hablar del futuro con ir a + infinitivo', None,
         '<p class="slide-explanation">Para los planes inmediatos usas <b>ir a + infinitivo</b>.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Voy a visitar</b> a mi familia el próximo fin de semana.</p>'
         '<p style="margin-top:8px"><b>Vamos a cenar</b> juntos cuando vuelvas.</p></div>'
         '<p style="margin-top:16px">También puedes usar el futuro simple: <b>visitaré</b>, <b>cenaremos</b>.</p>'),
        ('Conectores para organizar el texto', None,
         '<p class="slide-explanation">Los conectores dan fluidez al correo y organizan la información.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Para añadir:</b> además, también, y</p>'
         '<p style="margin-top:8px"><b>Para contrastar:</b> pero, aunque, sin embargo</p>'
         '<p style="margin-top:8px"><b>Para explicar:</b> porque, ya que, es que</p>'
         '<p style="margin-top:8px"><b>Para concluir:</b> en fin, bueno, total que</p></div>'),
    ],
    traps=[
        ('Querido Carmen: (mujer)', 'Querida Carmen:', 'Querido concuerda con el género: querida para mujer'),
        ('Asunto: (vacío)', 'Asunto: ¡Hola desde Málaga! (siempre con contenido)', 'El asunto debe resumir el tema del correo'),
        ('Hola Ana (sin signo de exclamación de apertura)', '¡Hola, Ana! (con ¡ y coma)', 'En exclamaciones informales se usa ¡ de apertura y coma antes del nombre'),
        ('Hasta luego, besos. (mayúscula innecesaria en «besos»)', 'Hasta luego. Besos.', 'Cada frase empieza con mayúscula; besos puede ser frase independiente'),
        ('Fui a la playa ayer con mis amigos y también fui al mercado y comí mucho y...', 'Fui a la playa. También fui al mercado y comí muy bien.', 'Evita las frases excesivamente largas unidas con «y»'),
    ],
    summary=[
        ('Asunto', 'Tema breve y atractivo', '¡Hola desde Málaga!'),
        ('Saludo', '¡Hola, + nombre! / Querido/a + nombre:', '¡Hola, Carmen!'),
        ('Pasado', 'pretérito indefinido', 'Fui al mercado. Comí muy bien.'),
        ('Futuro', 'ir a + infinitivo / futuro simple', 'Voy a visitarte pronto.'),
        ('Conectores', 'además / pero / porque', 'Fui a la playa, pero llovió.'),
        ('Despedida', 'Un beso / Un abrazo / Cuídate', 'Un abrazo, Sofía.'),
    ],
    items=[
        ('asunto', 'asunto', 'breve descripción del tema principal de un correo electrónico', 'tema',
         'El ______ del correo resume en pocas palabras de qué trata.', 'asun', 'asunto'),
        ('saludo-informal', 'saludo informal', 'fórmula afectuosa con la que se inicia un correo a personas de confianza', 'apertura',
         '«¡Hola, Ana!» o «Querida Ana:» son ejemplos de ______ informal.', 'saludo', 'saludo informal'),
        ('pretind', 'pretérito indefinido', 'tiempo verbal que expresa acciones terminadas en un momento concreto del pasado', 'pasado simple',
         'Para contar lo que hiciste ayer usas el ______.', 'pret', 'pretérito indefinido'),
        ('ir-a', 'ir a + infinitivo', 'construcción perifrástica para expresar planes o intenciones futuras', 'futuro próximo',
         '«Voy a visitar a mi familia» usa la perífrasis ______.', 'ir a', 'ir a + infinitivo'),
        ('conector', 'conector', 'palabra o expresión que relaciona partes del texto y da cohesión al discurso', 'enlace',
         '«Además» y «pero» son ejemplos de ______ textual.', 'conect', 'conector'),
        ('despedida', 'despedida informal', 'fórmula afectuosa con la que se cierra un correo a personas de confianza', 'cierre',
         '«Un abrazo» y «Cuídate» son fórmulas de ______ informal.', 'desped', 'despedida informal'),
        ('tono', 'tono informal', 'registro coloquial y cercano adecuado para la comunicación entre amigos o familia', 'registro coloquial',
         'Los correos a amigos usan un ______ con vocabulario del habla cotidiana.', 'tono', 'tono informal'),
        ('firma', 'firma', 'nombre del remitente que cierra el correo', 'nombre del autor',
         'El correo termina con la despedida y la ______ del remitente.', 'firm', 'firma'),
    ],
    ex1=('Elige la forma correcta', 'Selecciona la mejor opción para cada situación.', [
        ('El correo es para tu amiga María. El saludo correcto es:', ['¡Hola, María!', 'Estimada María:', 'A quien corresponda:'], '¡Hola, María!',
         'Un correo informal a una amiga usa ¡Hola, nombre!'),
        ('Quieres contar lo que hiciste el fin de semana. Usas:', ['el pretérito indefinido', 'el presente', 'el futuro'], 'el pretérito indefinido',
         'Para acciones terminadas en el pasado → pretérito indefinido.'),
        ('Para hablar de tus planes del próximo mes, dices:', ['Voy a visitar a mi familia.', 'Visito a mi familia.', 'Visite a mi familia.'], 'Voy a visitar a mi familia.',
         'Planes futuros → ir a + infinitivo: voy a visitar.'),
        ('El correo es para tu amigo Juan (hombre). El saludo es:', ['Querido Juan:', 'Querida Juan:', 'Estimado Juan:'], 'Querido Juan:',
         'Querido/a concuerda: querido para hombre, querida para mujer.'),
        ('Quieres añadir información. El conector más adecuado es:', ['Además', 'Pero', 'Sin embargo'], 'Además',
         'Además añade información. Pero y sin embargo contrastan.'),
        ('La despedida más apropiada para un correo informal es:', ['Un abrazo', 'Atentamente', 'Le saluda cordialmente'], 'Un abrazo',
         'Un abrazo es informal. Atentamente y le saluda son para correos formales.'),
    ]),
    ex2=('Completa el correo', 'Escribe la palabra o expresión que falta.', [
        ('______ , Laura! ¿Cómo estás? (saludo)', 'Hola',
         'El saludo informal más común: ¡Hola, nombre!'),
        ('El fin de semana ______ a la montaña con mis padres. (pretérito de IR)', 'fui',
         'Pretérito indefinido de IR: fui (yo).'),
        ('______ a visitarte el mes que viene. (plan futuro)', 'Voy',
         'Planes futuros: voy a + infinitivo.'),
        ('La película era muy buena, ______ el final me pareció raro. (contraste)', 'pero',
         'Pero introduce un contraste.'),
        ('Un ______ muy fuerte. Beatriz. (despedida)', 'abrazo',
         'Un abrazo es una despedida informal cariñosa.'),
    ]),
    ex3=('Organiza el correo', 'Elige el orden correcto de los elementos o selecciona la opción adecuada.', [
        ('¿Qué va primero en un correo informal?',
         ['El asunto y el saludo', 'La despedida', 'El cuerpo con la información'],
         'El asunto y el saludo',
         'El asunto resume el tema; el saludo abre el cuerpo del correo.'),
        ('¿Cuál es la despedida adecuada para un correo a un amigo?',
         ['Un beso. Carmen.', 'Le saluda atentamente, Carmen.', 'A quien corresponda.'],
         'Un beso. Carmen.',
         'Un beso + nombre es una despedida informal afectuosa.'),
        ('Para contar lo que hiciste ayer, ¿qué tiempo usas?',
         ['Pretérito indefinido: fui, comí, vi', 'Presente: voy, como, veo', 'Futuro: iré, comeré, veré'],
         'Pretérito indefinido: fui, comí, vi',
         'El pretérito indefinido expresa acciones terminadas en el pasado.'),
        ('¿Cuál de estas frases usa bien los conectores?',
         ['Fui al cine. Además, cené con Ana.', 'Fui al cine además cené con Ana.', 'Además fui al cine pero cené con Ana también pero'],
         'Fui al cine. Además, cené con Ana.',
         'Además va al principio de la frase, seguido de coma, y añade información.'),
        ('¿Cuál de estas opciones es un buen asunto para un correo informal?',
         ['¡Noticias del verano!', 'Ref.: visita', 'Solicitud de información'],
         '¡Noticias del verano!',
         'Un asunto informal es breve, expresivo y puede usar signos de exclamación.'),
    ]),
)

CHAPTERS['descripcion'] = dict(
    level='a2', section='writing', num='W02', short='La Descripción',
    title='La Descripción — Describir Personas y Lugares',
    subtitle='Aprende a describir personas, objetos y lugares con detalle y precisión',
    game_desc='Practica el vocabulario y las estructuras para describir en español.',
    slides=[
        ('¿Qué es una descripción?', None,
         '<p class="slide-explanation">Una descripción presenta las características de una persona, un lugar u objeto para que el lector pueda imaginarlo.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Mi ciudad favorita es Granada.</b> (frase de inicio)</p>'
         '<p style="margin-top:8px"><b>Está en el sur de España y tiene mucha historia.</b> (ubicación y rasgo)</p>'
         '<p style="margin-top:8px"><b>Lo que más me gusta es la Alhambra.</b> (opinión personal)</p></div>'),
        ('SER vs ESTAR en las descripciones', None,
         '<p class="slide-explanation">SER describe características permanentes; ESTAR describe estados o ubicaciones temporales.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Ser:</b> Mi amiga <b>es</b> alta y morena. (características físicas)</p>'
         '<p style="margin-top:8px"><b>Estar:</b> Hoy <b>está</b> muy cansada. (estado temporal)</p>'
         '<p style="margin-top:8px"><b>Ser:</b> El pueblo <b>es</b> pequeño y tranquilo.</p>'
         '<p style="margin-top:8px"><b>Estar:</b> El pueblo <b>está</b> en la montaña.</p></div>'),
        ('Adjetivos de descripción', None,
         '<p class="slide-explanation">Los adjetivos concuerdan en género y número con el sustantivo que describen.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Físico:</b> alto/a, bajo/a, delgado/a, moreno/a, rubio/a, joven, mayor</p>'
         '<p style="margin-top:8px"><b>Personalidad:</b> simpático/a, amable, serio/a, divertido/a, trabajador/a</p>'
         '<p style="margin-top:8px"><b>Lugares:</b> grande, pequeño/a, moderno/a, antiguo/a, tranquilo/a, animado/a</p></div>'),
        ('Organizar la descripción', None,
         '<p class="slide-explanation">Una buena descripción va de lo general a lo específico y usa conectores para dar fluidez.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p>1. <b>Presentación general:</b> Mi hermano se llama Pablo. Tiene treinta años.</p>'
         '<p style="margin-top:8px">2. <b>Aspecto físico:</b> Es moreno, con los ojos marrones y muy simpático.</p>'
         '<p style="margin-top:8px">3. <b>Personalidad / opinión:</b> Es muy trabajador. Lo que más me gusta de él es su sentido del humor.</p></div>'),
        ('Expresar gustos y opiniones', None,
         '<p class="slide-explanation">En una descripción podemos añadir nuestra valoración personal usando expresiones de opinión.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Lo que más me gusta es / son</b> las tapas.</p>'
         '<p style="margin-top:8px"><b>En mi opinión,</b> es el mejor lugar para vivir.</p>'
         '<p style="margin-top:8px"><b>Me parece</b> un sitio muy especial.</p></div>'),
    ],
    traps=[
        ('Mi amigo está moreno y alto.', 'Mi amigo <strong>es</strong> moreno y alto.', 'Las características físicas permanentes usan SER'),
        ('La ciudad está grande.', 'La ciudad <strong>es</strong> grande.', 'El tamaño es una característica permanente → SER'),
        ('Mi amiga es muy simpatica y es trabajadora y es inteligente y es...', 'Mi amiga es simpática, trabajadora e inteligente.', 'Usa la coma para unir adjetivos; no repitas SER'),
        ('Los ojos son azules a mi amigo.', 'Mi amigo tiene los ojos azules.', 'Para describir partes del cuerpo: TENER + artículo + sustantivo + adjetivo'),
        ('Alto chico con pelo negro.', 'Es un chico alto con el pelo negro.', 'Las descripciones necesitan verbo; no uses solo adjetivos sueltos'),
    ],
    summary=[
        ('Características permanentes', 'ser + adjetivo', 'Es alto y moreno.'),
        ('Estados temporales', 'estar + adjetivo', 'Está cansado hoy.'),
        ('Ubicación', 'estar en + lugar', 'Está en el norte de España.'),
        ('Partes del cuerpo', 'tener + artículo + sustantivo + adj.', 'Tiene los ojos azules.'),
        ('Opinión', 'Lo que más me gusta / Me parece', 'Me parece un lugar fantástico.'),
        ('Conectores', 'además / también / sin embargo', 'Es grande. Además, es muy moderna.'),
    ],
    items=[
        ('descripcion', 'descripción', 'texto que presenta las características de una persona, lugar u objeto', 'retrato',
         'Una ______ eficaz va de lo más general a los detalles específicos.', 'descr', 'descripción'),
        ('adjetivo', 'adjetivo', 'palabra que indica una característica o cualidad del sustantivo', 'calificativo',
         'Los ______ concuerdan en género y número con el sustantivo.', 'adjeti', 'adjetivo'),
        ('concordancia', 'concordancia', 'acuerdo de género y número entre el sustantivo y sus modificadores', 'acuerdo',
         'La ______ exige que «alta» vaya con sustantivos femeninos.', 'concord', 'concordancia'),
        ('ser-permanente', 'ser (permanente)', 'uso de ser para expresar características que no cambian o son esenciales', 'cualidad permanente',
         'El carácter y el físico son permanentes; los describes con ______.', 'ser', 'ser'),
        ('estar-temporal', 'estar (temporal)', 'uso de estar para expresar estados que pueden cambiar', 'estado cambiante',
         'El cansancio es temporal; lo describes con ______.', 'estar', 'estar'),
        ('tener-cuerpo', 'tener + parte del cuerpo', 'construcción para describir características físicas de partes del cuerpo', 'descripción física',
         '«Tiene los ojos verdes» usa el verbo ______ para describir el cuerpo.', 'tener', 'tener'),
        ('lo-que-mas', 'lo que más me gusta', 'expresión para destacar el aspecto más valorado de algo', 'opinión personal',
         '«______ es la arquitectura medieval» da una valoración personal.', 'lo que más', 'lo que más me gusta'),
        ('opinion', 'en mi opinión', 'expresión que introduce un punto de vista personal', 'a mi juicio',
         '«______, es el mejor restaurante de la ciudad» introduce una valoración.', 'en mi', 'en mi opinión'),
    ],
    ex1=('SER o ESTAR', 'Elige el verbo correcto para cada frase.', [
        ('Mi profesora ______ muy amable y paciente. (carácter)', ['es', 'está', 'tiene'], 'es',
         'El carácter es permanente → ser: es amable.'),
        ('El pueblo ______ en la costa norte. (ubicación)', ['está', 'es', 'tiene'], 'está',
         'Ubicación → estar: está en la costa norte.'),
        ('Hoy mi hermano ______ muy contento porque aprobó. (estado)', ['está', 'es', 'tiene'], 'está',
         'Estado temporal → estar: está contento hoy.'),
        ('La catedral ______ muy antigua, del siglo XII. (característica)', ['es', 'está', 'parece'], 'es',
         'Característica permanente → ser: es muy antigua.'),
        ('Mi abuela ______ los ojos azules. (parte del cuerpo)', ['tiene', 'es', 'está'], 'tiene',
         'Partes del cuerpo → tener: tiene los ojos azules.'),
        ('El mercado ______ muy animado los fines de semana. (estado)', ['está', 'es', 'tiene'], 'está',
         'Estado variable → estar: está muy animado los fines de semana.'),
    ]),
    ex2=('Completa la descripción', 'Escribe la palabra que falta.', [
        ('Mi amiga Clara ______ alta y delgada. Tiene el pelo largo y rubio. (aspecto físico permanente)', 'es',
         'Aspecto físico permanente → ser: es alta y delgada.'),
        ('Su ciudad ______ en el centro de España, rodeada de montañas. (ubicación)', 'está',
         'Ubicación → estar: está en el centro.'),
        ('Tiene los ojos ______ y una sonrisa muy bonita. (color)', 'marrones',
         'Los ojos marrones son los más comunes en España.'),
        ('Lo que más me ______ es la gastronomía de la región. (gusto)', 'gusta',
         'Lo que más me gusta es + nombre singular.'),
        ('En mi ______ , es el lugar más bonito del mundo. (opinión)', 'opinión',
         'En mi opinión introduce una valoración personal.'),
    ]),
    ex3=('Elige la descripción correcta', 'Selecciona la opción que describe correctamente.', [
        ('¿Cómo describes el tamaño de una ciudad?',
         ['La ciudad es grande.', 'La ciudad está grande.', 'La ciudad tiene grande.'],
         'La ciudad es grande.',
         'El tamaño es permanente → ser: la ciudad es grande.'),
        ('¿Cómo describes que tu amigo está cansado hoy?',
         ['Mi amigo está muy cansado hoy.', 'Mi amigo es muy cansado hoy.', 'Mi amigo tiene cansado.'],
         'Mi amigo está muy cansado hoy.',
         'Estado temporal → estar: está cansado.'),
        ('¿Cómo describes los ojos de alguien?',
         ['Tiene los ojos negros.', 'Es los ojos negros.', 'Está los ojos negros.'],
         'Tiene los ojos negros.',
         'Partes del cuerpo → tener + artículo + sustantivo + adjetivo.'),
        ('¿Cuál de estas frases es una opinión personal correcta?',
         ['Me parece un sitio muy especial.', 'Parece muy especial el sitio a mí.', 'El sitio tiene especial.'],
         'Me parece un sitio muy especial.',
         'Me parece + sustantivo + adjetivo: me parece un sitio especial.'),
        ('¿Cuál organización es la más adecuada para una descripción?',
         ['General → detalle → opinión', 'Opinión → general → detalle', 'Detalle → opinión → general'],
         'General → detalle → opinión',
         'Una descripción eficaz va de lo más general a los detalles y termina con la valoración personal.'),
    ]),
)

CHAPTERS['postal'] = dict(
    level='a2', section='writing', num='W03', short='La Postal',
    title='La Postal — Saludos desde un Viaje',
    subtitle='Aprende a escribir una postal con información sobre tus vacaciones',
    game_desc='Practica el vocabulario y las estructuras para escribir una postal en español.',
    slides=[
        ('¿Qué es una postal?', None,
         '<p class="slide-explanation">Una postal es un mensaje muy breve que mandas desde un lugar de vacaciones. Tiene cuatro partes: saludo, dónde estás, qué haces y despedida.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>¡Hola, Marcos!</b> (saludo)</p>'
         '<p style="margin-top:6px"><b>Estoy en Sevilla con mi familia.</b> (dónde)</p>'
         '<p style="margin-top:6px"><b>Hace mucho calor y la ciudad es preciosa.</b> (qué tal)</p>'
         '<p style="margin-top:6px"><b>Ayer visité la Giralda.</b> (actividad)</p>'
         '<p style="margin-top:6px"><b>Un beso, Isabel.</b> (despedida)</p></div>'),
        ('Hablar del tiempo atmosférico', None,
         '<p class="slide-explanation">En las postales es habitual hablar del tiempo. Se usa el verbo <b>hacer</b>.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Hace sol / calor / frío / viento / buen tiempo / mal tiempo.</b></p>'
         '<p style="margin-top:8px"><b>Está lloviendo.</b> / <b>Está nublado.</b></p>'
         '<p style="margin-top:8px"><b>Hay niebla.</b> / <b>Hay tormenta.</b></p></div>'),
        ('Hablar de actividades en el pasado', None,
         '<p class="slide-explanation">Para contar lo que ya hiciste en el viaje usas el <b>pretérito indefinido</b>.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Visité</b> el museo arqueológico. (visitar)</p>'
         '<p style="margin-top:8px"><b>Comí</b> una paella increíble en el puerto. (comer)</p>'
         '<p style="margin-top:8px"><b>Fui</b> a la playa dos veces. (ir)</p></div>'),
        ('Expresar sensaciones y valoraciones', None,
         '<p class="slide-explanation">Para hablar de cómo te sientes o de tu opinión sobre el lugar usas ESTAR y SER.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Estoy muy feliz / relajado/a / encantado/a.</b> (estado)</p>'
         '<p style="margin-top:8px"><b>La ciudad es preciosa / increíble / muy animada.</b> (característica)</p>'
         '<p style="margin-top:8px"><b>¡Me encanta!</b> / <b>¡Es fantástico!</b> (valoración)</p></div>'),
        ('Planes y actividades futuras', None,
         '<p class="slide-explanation">Para mencionar lo que piensas hacer más adelante en el viaje usas <b>ir a + infinitivo</b> o el futuro.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Mañana voy a visitar</b> la catedral.</p>'
         '<p style="margin-top:8px"><b>Esta tarde vamos a ir</b> de compras al mercado.</p>'
         '<p style="margin-top:8px"><b>La semana que viene volveremos</b> a casa.</p></div>'),
    ],
    traps=[
        ('Es sol y calor.', '<strong>Hace</strong> sol y calor.', 'El tiempo atmosférico usa HACER: hace sol, hace calor'),
        ('Querido Marcos (mujer escribiendo a un hombre)', 'Querido Marcos (correcto: Marcos es hombre)', 'Querido/a concuerda con el destinatario, no con quien escribe'),
        ('Visité el museo y fue muy bien.', 'Visité el museo y estuvo muy bien.', 'ESTAR para estados: estuvo muy bien, no fue muy bien'),
        ('Estoy en la playa desde el lunes.', 'Llevo en la playa desde el lunes. / Estoy en la playa desde el lunes. (correcto, pero...)', 'Correcto; también puedes variar: llevo dos días en la playa'),
        ('¡Hasta pronto!, besos', '¡Hasta pronto! Besos, Isabel.', 'No pongas coma después de una exclamación; úsala como frase independiente'),
    ],
    summary=[
        ('Saludo', '¡Hola, + nombre!', '¡Hola, Marcos!'),
        ('Ubicación', 'Estar en + lugar', 'Estoy en Sevilla con mi familia.'),
        ('Tiempo atmosférico', 'Hacer + sol/calor/frío', 'Hace mucho calor.'),
        ('Actividad pasada', 'Pretérito indefinido', 'Ayer visité la Giralda.'),
        ('Valoración', 'Ser + adjetivo / ¡Me encanta!', 'La ciudad es preciosa.'),
        ('Despedida', 'Un beso / Un abrazo + nombre', 'Un beso, Isabel.'),
    ],
    items=[
        ('postal', 'postal', 'tarjeta con imagen en el anverso que se manda como recuerdo desde un lugar de vacaciones', 'tarjeta postal',
         'Mandé una ______ desde Roma con una foto del Coliseo.', 'post', 'postal'),
        ('tiempo-atm', 'tiempo atmosférico', 'condiciones climáticas de un lugar en un momento determinado', 'clima',
         'Para describir el ______ en las postales usamos: hace calor, llueve...', 'tiempo', 'tiempo atmosférico'),
        ('hacer-tiempo', 'hacer + clima', 'construcción impersonal para expresar condiciones meteorológicas', 'construcción meteo',
         '«Hace sol» y «hace frío» usan el verbo ______ + clima.', 'hac', 'hacer'),
        ('pretind-viaje', 'pretérito indefinido', 'tiempo verbal para contar lo que ya hiciste en el viaje', 'pasado simple',
         'Para contar las actividades del viaje usas el ______.', 'pret', 'pretérito indefinido'),
        ('valoracion', 'valoración', 'juicio o apreciación subjetiva sobre algo o alguien', 'opinión',
         '«¡Me encanta!» y «es fantástico» son expresiones de ______.', 'valor', 'valoración'),
        ('ir-a-viaje', 'ir a + infinitivo', 'perífrasis para expresar planes concretos en el futuro próximo', 'futuro próximo',
         '«Mañana voy a visitar la catedral» usa la estructura ______.', 'ir a', 'ir a + infinitivo'),
        ('encantado', 'estar encantado/a', 'expresión de satisfacción o entusiasmo intenso con una situación', 'estar feliz',
         '«______ con el viaje» expresa un estado de gran satisfacción.', 'estoy enc', 'estoy encantado'),
        ('despedida-postal', 'despedida', 'fórmula con la que se cierra el mensaje de una postal', 'cierre',
         '«Un beso, Ana» es una ______ típica de una postal informal.', 'desped', 'despedida'),
    ],
    ex1=('Elige la forma correcta', 'Selecciona la opción que completa mejor la frase.', [
        ('______ mucho calor aquí en Málaga. (tiempo atmosférico)', ['Hace', 'Es', 'Está'], 'Hace',
         'Tiempo atmosférico → hacer: hace calor.'),
        ('La catedral ______ impresionante. (opinión permanente)', ['es', 'está', 'hace'], 'es',
         'Característica permanente → ser: es impresionante.'),
        ('Ayer ______ la Alhambra por la tarde. (actividad pasada)', ['visité', 'visito', 'voy a visitar'], 'visité',
         'Actividad completada en el pasado → pretérito indefinido: visité.'),
        ('Mañana ______ a ver el barrio antiguo. (plan futuro)', ['vamos', 'fuimos', 'vamos a ir'], 'vamos a ir',
         'Plan futuro → ir a + infinitivo: vamos a ir.'),
        ('Estoy ______ con este viaje. (satisfacción intensa)', ['encantado', 'encantada', 'encantados'], 'encantado',
         'Encantado/a concuerda con el género del hablante.'),
        ('______ , Sergio! Te escribo desde Bilbao. (saludo)', ['¡Hola', 'Hasta luego', 'Un beso'], '¡Hola',
         'El saludo abre la postal; hasta luego y un beso la cierran.'),
    ]),
    ex2=('Completa la postal', 'Escribe la palabra que falta.', [
        ('¡Hola, Rosa! Estoy en Valencia con mis amigos. ______ mucho sol. (tiempo)', 'Hace',
         'Tiempo atmosférico → hacer: hace sol.'),
        ('Ayer ______ al mercado central y probé la paella. (pretérito de IR)', 'fui',
         'Pretérito indefinido de IR: fui (yo).'),
        ('La ciudad ______ muy animada y moderna. (característica)', 'es',
         'Característica permanente → ser: es animada.'),
        ('Mañana voy ______ visitar el museo de Bellas Artes. (estructura futura)', 'a',
         'Ir a + infinitivo: voy a visitar.'),
        ('Un ______ , María. (despedida)', 'beso',
         'Un beso + nombre es la despedida clásica de una postal informal.'),
    ]),
    ex3=('Corrige los errores', 'Elige la versión correcta de cada frase.', [
        ('«Es mucho calor aquí.»',
         ['Hace mucho calor aquí.', 'Está mucho calor aquí.', 'Hay mucho calor aquí.'],
         'Hace mucho calor aquí.',
         'El tiempo atmosférico usa HACER: hace calor, no es calor.'),
        ('«La playa fue muy bonita.»',
         ['La playa es muy bonita.', 'La playa está muy bonita.', 'La playa tiene bonita.'],
         'La playa es muy bonita.',
         'Una característica permanente usa SER. FUE solo sería correcto si la playa ya no existe.'),
        ('«Ayer visito el castillo.»',
         ['Ayer visité el castillo.', 'Ayer voy a visitar el castillo.', 'Ayer visitaré el castillo.'],
         'Ayer visité el castillo.',
         'Con ayer → pretérito indefinido: visité.'),
        ('«Mañana visitamos el museo.» (expresar un plan)',
         ['Mañana vamos a visitar el museo.', 'Mañana visitamos el museo. (también correcto)', 'Las dos son correctas'],
         'Las dos son correctas',
         'Ir a + infinitivo y el presente con valor de futuro son ambos correctos para planes.'),
        ('«¡Hasta pronto!, besos, Ana»',
         ['¡Hasta pronto! Besos, Ana.', '¡Hasta pronto!, Besos, Ana.', 'Hasta pronto, besos, Ana'],
         '¡Hasta pronto! Besos, Ana.',
         'Después de una exclamación va punto. Besos comienza frase nueva con mayúscula.'),
    ]),
)
