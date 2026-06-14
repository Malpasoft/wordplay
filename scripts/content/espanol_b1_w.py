# espanol_b1_w.py — Main Spanish B1 Writing — 8 chapters

CHAPTERS = {}

CHAPTERS['correo-formal'] = dict(
    level='b1', section='writing', num='W01', short='El Correo Formal',
    title='El Correo Formal — Solicitudes y Quejas',
    subtitle='Aprende a escribir correos formales con el tono y las fórmulas adecuados',
    game_desc='Practica las estructuras y fórmulas del correo formal en español.',
    slides=[
        ('Diferencias entre correo formal e informal', None,
         '<p class="slide-explanation">El correo formal usa el tratamiento de usted, un registro elevado y fórmulas protocolarias. Se envía a instituciones, empresas o personas desconocidas.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Formal:</b> Estimado Sr. García: / Me dirijo a usted para...</p>'
         '<p style="margin-top:8px"><b>Informal:</b> ¡Hola, Juan! / Te escribo porque...</p>'
         '<p style="margin-top:8px">La diferencia clave: <b>usted</b> (formal) vs <b>tú</b> (informal).</p></div>'),
        ('Estructura del correo formal', None,
         '<p class="slide-explanation">Un correo formal tiene una estructura clara y ordenada que sigue un protocolo establecido.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Asunto:</b> Solicitud de información sobre el curso de español B2</p>'
         '<p style="margin-top:6px"><b>Saludo:</b> Estimado/a Sr./Sra. + apellido:</p>'
         '<p style="margin-top:6px"><b>Apertura:</b> Me dirijo a usted para... / En relación con...</p>'
         '<p style="margin-top:6px"><b>Cuerpo:</b> información detallada y organizada</p>'
         '<p style="margin-top:6px"><b>Cierre:</b> Quedo a su disposición para cualquier consulta.</p>'
         '<p style="margin-top:6px"><b>Despedida:</b> Atentamente, / Un cordial saludo,</p></div>'),
        ('Fórmulas de saludo y apertura', None,
         '<p class="slide-explanation">Los saludos y la apertura formales siguen fórmulas fijas que debes memorizar.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Saludos:</b> Estimado/a Sr./Sra. García: &nbsp;|&nbsp; A quien corresponda:</p>'
         '<p style="margin-top:8px"><b>Aperturas:</b> Me dirijo a usted para solicitar... &nbsp;|&nbsp; En relación con su anuncio... &nbsp;|&nbsp; Me pongo en contacto con ustedes para...</p></div>'),
        ('Fórmulas de cierre y despedida', None,
         '<p class="slide-explanation">El cierre y la despedida son tan importantes como el saludo. Expresan cortesía y profesionalidad.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Cierres:</b> Quedo a su disposición para cualquier consulta. &nbsp;|&nbsp; En espera de su respuesta, aprovecho la ocasión para saludarle.</p>'
         '<p style="margin-top:8px"><b>Despedidas:</b> Atentamente, &nbsp;|&nbsp; Un cordial saludo, &nbsp;|&nbsp; Reciba un atento saludo,</p></div>'),
        ('Vocabulario para solicitudes y quejas', None,
         '<p class="slide-explanation">Según el propósito del correo, usarás un vocabulario específico.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Solicitudes:</b> les ruego que... &nbsp;|&nbsp; quisiera solicitar... &nbsp;|&nbsp; les agradecería que...</p>'
         '<p style="margin-top:8px"><b>Quejas:</b> me veo obligado/a a informarles de... &nbsp;|&nbsp; lamentablemente... &nbsp;|&nbsp; les comunico que el servicio no fue satisfactorio</p></div>'),
    ],
    traps=[
        ('Estimado Juan:', 'Estimado <strong>Sr. García</strong>: (apellido, no nombre de pila)', 'En correos formales se usa apellido con Sr./Sra., no el nombre propio'),
        ('¡Hola! Te escribo para pedir información.', '<strong>Me dirijo a usted para solicitar información.</strong>', 'Un correo formal no usa hola ni tú'),
        ('Atentamente, (sin nombre ni firma)', 'Atentamente,\n<strong>Ana Torres Sánchez</strong>', 'La despedida siempre va seguida del nombre completo del remitente'),
        ('Quedo a su disposición para cualquier pregunta que tenga.', 'Quedo a su disposición para <strong>cualquier consulta</strong>.', 'En estilo formal se prefiere «consulta» a «pregunta»'),
        ('Un beso, hasta luego.', '<strong>Atentamente,</strong> / <strong>Un cordial saludo,</strong>', 'Las despedidas informales no son apropiadas en un correo formal'),
    ],
    summary=[
        ('Saludo formal', 'Estimado/a Sr./Sra. + apellido:', 'Estimada Sra. López:'),
        ('Apertura', 'Me dirijo a usted para...', 'Me dirijo a usted para solicitar...'),
        ('Solicitud', 'les ruego que / quisiera solicitar', 'Les ruego que me envíen el catálogo.'),
        ('Queja educada', 'me veo obligado/a a informarles de', 'Me veo obligado a informarles de un error.'),
        ('Cierre', 'Quedo a su disposición...', 'Quedo a su disposición para cualquier consulta.'),
        ('Despedida', 'Atentamente, / Un cordial saludo,', 'Atentamente, Ana Torres.'),
    ],
    items=[
        ('usted', 'usted', 'pronombre de segunda persona singular que expresa respeto y distancia formal', 'forma de respeto',
         'En los correos formales te diriges al destinatario con ______.', 'ust', 'usted'),
        ('estimado', 'estimado/a', 'fórmula de saludo formal que precede al título y apellido del destinatario', 'apreciado/a',
         '«______ Sr. García:» es el saludo formal estándar en correos españoles.', 'estim', 'estimado'),
        ('atentamente', 'atentamente', 'fórmula de despedida formal que cierra un correo o carta oficial', 'cordialmente',
         '«______» es la despedida más habitual en correos formales en español.', 'atent', 'atentamente'),
        ('me-dirijo', 'me dirijo a usted para', 'fórmula de apertura formal que indica el propósito del correo', 'me pongo en contacto',
         'La apertura estándar de un correo formal: «______ solicitar información».', 'me dirijo', 'me dirijo a usted para'),
        ('solicitar', 'solicitar', 'verbo formal para pedir algo de manera oficial y protocolaria', 'pedir formalmente',
         'En un correo formal ______ información en lugar de «pedir» información.', 'solic', 'solicitar'),
        ('queja', 'queja formal', 'comunicación escrita en la que se expone una insatisfacción de manera educada y estructurada', 'reclamación',
         'Una ______ formal describe el problema con datos precisos y pide una solución.', 'queja', 'queja formal'),
        ('asunto', 'asunto', 'línea que resume el tema del correo y orienta al destinatario antes de leerlo', 'tema del correo',
         'El ______ del correo formal debe ser claro, breve y descriptivo.', 'asunt', 'asunto'),
        ('registro', 'registro formal', 'variedad de lengua caracterizada por el uso de un vocabulario culto y estructuras complejas', 'nivel formal',
         'Un correo a una empresa requiere un ______ con vocabulario preciso y cortés.', 'regist', 'registro formal'),
    ],
    ex1=('Elige la fórmula correcta', 'Selecciona la opción más adecuada para un correo formal.', [
        ('¿Cuál es el saludo formal más adecuado?', ['Estimada Sra. López:', '¡Hola, María!', 'Buenas tardes:'], 'Estimada Sra. López:',
         'El saludo formal usa Estimado/a + Sr./Sra. + apellido + dos puntos.'),
        ('¿Cuál es la apertura formal correcta?', ['Me dirijo a usted para solicitar información.', 'Te escribo porque quiero saber.', 'Hola, quería preguntarte algo.'], 'Me dirijo a usted para solicitar información.',
         'Me dirijo a usted para... es la apertura formal estándar.'),
        ('¿Cuál es la despedida formal más adecuada?', ['Atentamente, Ana Torres.', 'Un beso, Ana.', 'Hasta luego.'], 'Atentamente, Ana Torres.',
         'Atentamente + nombre completo es la despedida formal estándar.'),
        ('Para pedir algo formalmente, usas:', ['Les ruego que me envíen el folleto.', 'Mándame el folleto.', '¿Me puedes mandar el folleto?'], 'Les ruego que me envíen el folleto.',
         'Les ruego que + subjuntivo es la estructura de solicitud formal.'),
        ('¿Cuál es la forma formal de referirte al destinatario?', ['usted', 'tú', 'vosotros'], 'usted',
         'En correos formales siempre se usa usted (o ustedes para varios destinatarios).'),
        ('¿Qué va en el campo «Asunto»?', ['Solicitud de información sobre el curso B2', '¡Hola!', 'nada'], 'Solicitud de información sobre el curso B2',
         'El asunto debe resumir el propósito del correo de forma breve y clara.'),
    ]),
    ex2=('Completa el correo formal', 'Escribe la palabra o expresión que falta.', [
        ('______ Sra. Martínez: (saludo formal)', 'Estimada',
         'El saludo formal: Estimado/a + título + apellido + dos puntos.'),
        ('Me ______ a usted para solicitar información sobre los cursos. (apertura)', 'dirijo',
         'Me dirijo a usted para... es la apertura formal estándar.'),
        ('Les ______ que me envíen el catálogo por correo electrónico. (solicitud formal)', 'ruego',
         'Les ruego que + subjuntivo: fórmula de solicitud formal.'),
        ('______ a su disposición para cualquier consulta. (cierre)', 'Quedo',
         'Quedo a su disposición... es el cierre formal más habitual.'),
        ('______  , Ana López Ruiz. (despedida)', 'Atentamente',
         'Atentamente + nombre completo: la despedida formal estándar.'),
    ]),
    ex3=('Formal o informal', 'Decide si cada elemento pertenece al registro formal o informal.', [
        ('«¡Hola! ¿Cómo estás?»',
         ['Informal: no es adecuado en un correo formal', 'Formal: es un saludo correcto'],
         'Informal: no es adecuado en un correo formal',
         'En un correo formal se usa Estimado/a Sr./Sra., no Hola.'),
        ('«Atentamente, + nombre completo»',
         ['Formal: es la despedida estándar', 'Informal: demasiado frío'],
         'Formal: es la despedida estándar',
         'Atentamente es la despedida formal más extendida en español.'),
        ('«Les ruego que me envíen información.»',
         ['Formal: usa subjuntivo y tratamiento de usted', 'Informal: demasiado directo'],
         'Formal: usa subjuntivo y tratamiento de usted',
         'Les ruego que + subjuntivo es una estructura formal de solicitud.'),
        ('«Un beso. Hasta pronto.»',
         ['Informal: solo válido entre personas de confianza', 'Formal: es una despedida estándar'],
         'Informal: solo válido entre personas de confianza',
         'Un beso y Hasta pronto son despedidas informales.'),
        ('«Quedo a su disposición para cualquier consulta.»',
         ['Formal: fórmula de cierre protocolaria', 'Informal: suena demasiado cercano'],
         'Formal: fórmula de cierre protocolaria',
         'Esta fórmula es propia del registro formal y muy habitual en correos oficiales.'),
    ]),
)

CHAPTERS['narracion'] = dict(
    level='b1', section='writing', num='W02', short='La Narración',
    title='La Narración — Contar una Historia',
    subtitle='Aprende a escribir relatos con estructura, tiempos verbales correctos y conectores temporales',
    game_desc='Practica los elementos clave de la narración en español.',
    slides=[
        ('Estructura de la narración', None,
         '<p class="slide-explanation">Toda buena narración tiene tres partes: introducción (quién, cuándo, dónde), nudo (problema o conflicto) y desenlace (resolución).</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Introducción:</b> Era un martes lluvioso cuando Marta llegó a la ciudad.</p>'
         '<p style="margin-top:8px"><b>Nudo:</b> De repente, se dio cuenta de que había perdido su cartera.</p>'
         '<p style="margin-top:8px"><b>Desenlace:</b> Al final, un amable desconocido se la devolvió.</p></div>'),
        ('Indefinido vs. imperfecto en la narración', None,
         '<p class="slide-explanation">El indefinido narra acciones concretas que hacen avanzar la historia. El imperfecto describe el fondo, los estados y las acciones habituales.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Imperfecto (fondo):</b> Era tarde. Llovía. El bar estaba lleno de gente.</p>'
         '<p style="margin-top:8px"><b>Indefinido (acción):</b> Entró, pidió un café y se sentó cerca de la ventana.</p></div>'
         '<p style="margin-top:16px">Regla: cuando el indefinido y el imperfecto aparecen juntos, el imperfecto es el escenario y el indefinido es la acción.</p>'),
        ('Marcadores temporales para narrar', None,
         '<p class="slide-explanation">Los marcadores temporales organizan la secuencia de los hechos y dan cohesión al relato.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Inicio:</b> Aquella mañana / Un día / Era + hora cuando...</p>'
         '<p style="margin-top:8px"><b>Secuencia:</b> primero, después, luego, a continuación, más tarde</p>'
         '<p style="margin-top:8px"><b>Giro:</b> de repente, de pronto, inesperadamente</p>'
         '<p style="margin-top:8px"><b>Final:</b> al final, por fin, finalmente</p></div>'),
        ('Describir el escenario y los personajes', None,
         '<p class="slide-explanation">La descripción del entorno y los personajes crea la atmósfera del relato y engancha al lector.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Lugar:</b> La ciudad estaba envuelta en niebla. Las calles estaban desiertas.</p>'
         '<p style="margin-top:8px"><b>Personaje:</b> Era un hombre de unos cincuenta años, con el pelo canoso y los ojos cansados.</p></div>'
         '<p style="margin-top:16px">Recuerda: las descripciones usan el <b>imperfecto</b> porque son el fondo del relato.</p>'),
        ('Cómo terminar bien un relato', None,
         '<p class="slide-explanation">El desenlace debe resolver el conflicto y puede incluir una reflexión del narrador o una lección aprendida.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Desenlace sorprendente:</b> Al final, resultó que todo había sido un sueño.</p>'
         '<p style="margin-top:8px"><b>Con reflexión:</b> Desde aquel día, nunca más subestimó la importancia de la amistad.</p>'
         '<p style="margin-top:8px"><b>Abierto:</b> No sabemos qué pasó después, pero aquella noche cambió su vida para siempre.</p></div>'),
    ],
    traps=[
        ('Ayer fui al mercado y compraba frutas.', 'Fui al mercado y <strong>compré</strong> frutas.', 'Acción concreta terminada → indefinido, no imperfecto'),
        ('Hacía mucho frío, de repente entré en la cafetería.', 'Hacía mucho frío. De repente, <strong>entré</strong> en la cafetería.', 'Punto y seguido antes del giro con de repente; la coma sola no basta'),
        ('Primero después de ir al mercado fui a casa.', '<strong>Primero fui al mercado</strong> y <strong>después</strong> me fui a casa.', 'No acumules marcadores; usa uno por hecho'),
        ('Era un día soleado y hace calor.', 'Era un día soleado y <strong>hacía</strong> calor.', 'Toda la descripción del pasado usa imperfecto; no mezcles con presente'),
        ('Finalmente, al final, por fin llegamos.', '<strong>Por fin</strong> llegamos. (un solo marcador de final)', 'No uses varios marcadores de final seguidos'),
    ],
    summary=[
        ('Introducción', 'Imperfecto + escenario', 'Era tarde. El parque estaba vacío.'),
        ('Acción principal', 'Indefinido', 'De repente, escuché un ruido.'),
        ('Secuencia', 'primero / luego / después', 'Primero grité, luego salí corriendo.'),
        ('Giro', 'De repente / de pronto', 'De repente, apareció un perro enorme.'),
        ('Desenlace', 'al final / por fin', 'Al final resultó ser solo un gato.'),
        ('Reflexión', 'Desde entonces / nunca más', 'Desde entonces, siempre llevo linterna.'),
    ],
    items=[
        ('narracion', 'narración', 'texto que cuenta hechos reales o ficticios siguiendo un orden temporal', 'relato',
         'Una ______ bien construida tiene introducción, nudo y desenlace.', 'narr', 'narración'),
        ('indefinido', 'pretérito indefinido', 'tiempo verbal del pasado para acciones concretas y terminadas que hacen avanzar el relato', 'pasado simple',
         'La acción que hace avanzar la historia usa el ______.', 'pret. indef', 'pretérito indefinido'),
        ('imperfecto', 'pretérito imperfecto', 'tiempo verbal del pasado para descripciones, estados y acciones habituales en un relato', 'copretérito',
         'El escenario y la descripción de los personajes usan el ______.', 'pret. imperf', 'pretérito imperfecto'),
        ('nudo', 'nudo', 'parte central del relato donde surge el conflicto o la complicación principal', 'conflicto',
         'El ______ es el momento en que aparece el problema que el protagonista debe resolver.', 'nud', 'nudo'),
        ('desenlace', 'desenlace', 'parte final del relato donde el conflicto se resuelve', 'resolución',
         'El ______ puede ser esperado, sorprendente o abierto.', 'deseñ', 'desenlace'),
        ('de-repente', 'de repente', 'marcador temporal que introduce un giro o acontecimiento inesperado en la narración', 'de pronto',
         '«______ , sonó el teléfono» introduce un cambio brusco en la historia.', 'de rep', 'de repente'),
        ('marcador', 'marcador temporal', 'expresión que indica el orden o el momento de los hechos en una narración', 'conector de tiempo',
         '«Primero», «luego» y «al final» son ______ temporales.', 'marc', 'marcador temporal'),
        ('escenario', 'escenario', 'descripción del lugar y el ambiente donde transcurre la acción del relato', 'ambientación',
         'El ______ se describe con el imperfecto al inicio del relato.', 'escen', 'escenario'),
    ],
    ex1=('Indefinido o imperfecto', 'Elige el tiempo verbal correcto.', [
        ('Cuando llegué, todos ______ . (sentarse, acción de fondo)', ['estaban sentados', 'se sentaron', 'se sientan'], 'estaban sentados',
         'Estado de fondo en el momento de la llegada → imperfecto: estaban sentados.'),
        ('De repente, ______ un grito en el pasillo. (escuchar, acción puntual)', ['oí', 'oía', 'oigo'], 'oí',
         'Acción puntual que hace avanzar el relato → indefinido: oí.'),
        ('Era una noche oscura y ______ mucho frío. (hacer, descripción)', ['hacía', 'hizo', 'hace'], 'hacía',
         'Descripción del ambiente → imperfecto: hacía frío.'),
        ('Primero ______ al mercado y luego fui a casa. (ir)', ['fui', 'iba', 'voy'], 'fui',
         'Acción secuenciada y terminada → indefinido: fui.'),
        ('Mientras yo ______ , sonó el teléfono. (dormir)', ['dormía', 'dormí', 'duermo'], 'dormía',
         'Acción en curso interrumpida → imperfecto: dormía (acción continua).'),
        ('Al final, ______ la maleta y ______ del hotel. (coger, salir)', ['cogió, salió', 'cogía, salía', 'coge, sale'], 'cogió, salió',
         'Acciones que cierran el relato → indefinido: cogió, salió.'),
    ]),
    ex2=('Completa con el marcador correcto', 'Escribe el marcador temporal que mejor encaja.', [
        ('______ , el cielo se oscureció y empezó a llover. (giro inesperado)', 'De repente',
         'De repente introduce un cambio brusco o inesperado.'),
        ('______ llegué, me senté y pedí un café. (primera acción)', 'Primero',
         'Primero introduce la primera de una serie de acciones.'),
        ('Dos horas ______ , recibí la llamada que lo cambió todo. (tiempo transcurrido)', 'después',
         'Después (o más tarde) indica que algo ocurre un tiempo después.'),
        ('______  , conseguimos llegar al refugio antes de la tormenta. (alivio)', 'Por fin',
         'Por fin expresa alivio al lograr algo tras un esfuerzo o espera.'),
        ('______ de aquella experiencia, nunca más volvió a conducir de noche. (reflexión final)', 'Desde entonces',
         'Desde entonces indica un cambio permanente a raíz de lo ocurrido.'),
    ]),
    ex3=('Estructura del relato', 'Elige la opción correcta para cada pregunta.', [
        ('¿Qué tiempo verbal usas para describir el escenario al inicio del relato?',
         ['El imperfecto', 'El indefinido', 'El presente'], 'El imperfecto',
         'Las descripciones de fondo y el escenario usan el imperfecto.'),
        ('¿Qué tiempo verbal usas para las acciones que hacen avanzar la historia?',
         ['El indefinido', 'El imperfecto', 'El presente'], 'El indefinido',
         'Las acciones concretas y terminadas que avanzan el relato usan el indefinido.'),
        ('¿Cuál es el marcador de giro más habitual en la narración?',
         ['De repente', 'Primero', 'Al final'], 'De repente',
         'De repente introduce un giro o acontecimiento inesperado.'),
        ('¿Cuál es la estructura correcta de un relato?',
         ['Introducción → nudo → desenlace', 'Nudo → introducción → desenlace', 'Desenlace → nudo → introducción'],
         'Introducción → nudo → desenlace',
         'La estructura narrativa clásica: plantear el escenario, desarrollar el conflicto, resolver.'),
        ('¿Qué parte del relato resuelve el conflicto principal?',
         ['El desenlace', 'El nudo', 'La introducción'], 'El desenlace',
         'El desenlace resuelve la complicación planteada en el nudo.'),
    ]),
)

CHAPTERS['descripcion-avanzada'] = dict(
    level='b1', section='writing', num='W03', short='La Descripción Avanzada',
    title='La Descripción Avanzada — Personas, Lugares y Objetos',
    subtitle='Enriquece tus descripciones con comparaciones, metáforas y vocabulario variado',
    game_desc='Practica las técnicas de la descripción avanzada en español.',
    slides=[
        ('De lo general a lo específico', None,
         '<p class="slide-explanation">Una descripción avanzada organiza la información de lo más general a lo más específico, usando un vocabulario rico y variado.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>General:</b> Barcelona es una ciudad mediterránea, vibrante y cosmopolita.</p>'
         '<p style="margin-top:8px"><b>Específico:</b> El barrio gótico, con sus calles medievales y sus tiendas de artesanía, es el corazón histórico de la ciudad.</p>'
         '<p style="margin-top:8px"><b>Detalle:</b> Las piedras del suelo, desgastadas por siglos de pasos, brillan con la humedad del amanecer.</p></div>'),
        ('Comparaciones: tan...como / más...que', None,
         '<p class="slide-explanation">Las comparaciones hacen las descripciones más vívidas y precisas.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Igualdad:</b> Sus ojos son <b>tan claros como</b> el cielo de agosto.</p>'
         '<p style="margin-top:8px"><b>Superioridad:</b> La catedral es <b>más imponente de</b> lo que esperaba.</p>'
         '<p style="margin-top:8px"><b>Inferioridad:</b> El apartamento es <b>menos espacioso que</b> el anterior.</p></div>'),
        ('Metáforas y lenguaje figurado', None,
         '<p class="slide-explanation">Las metáforas describen algo en términos de otra cosa, creando imágenes más impactantes.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Sin metáfora:</b> El río tiene agua marrón y turbulenta.</p>'
         '<p style="margin-top:8px"><b>Con metáfora:</b> El río es una serpiente de barro que serpentea entre los campos.</p>'
         '<p style="margin-top:8px"><b>Sin metáfora:</b> El pueblo es muy pequeño y silencioso.</p>'
         '<p style="margin-top:8px"><b>Con metáfora:</b> El pueblo duerme entre montañas, ajeno al ruido del mundo.</p></div>'),
        ('Vocabulario sensorial', None,
         '<p class="slide-explanation">Apelar a los cinco sentidos hace que las descripciones sean más ricas e inmersivas.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Vista:</b> brillante, opaco, translúcido, centelleante, apagado</p>'
         '<p style="margin-top:8px"><b>Oído:</b> silencioso, estruendoso, susurrante, estridente, melodioso</p>'
         '<p style="margin-top:8px"><b>Tacto:</b> suave, rugoso, sedoso, áspero, frío al tacto</p>'
         '<p style="margin-top:8px"><b>Olfato:</b> fragante, rancio, penetrante, sutil</p></div>'),
        ('Estructura de la descripción avanzada', None,
         '<p class="slide-explanation">Una descripción avanzada bien estructurada sigue el esquema: presentación general → características físicas → atmósfera/impresión → valoración personal.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p>1. <b>General:</b> La casa de mis abuelos es una construcción del siglo pasado.</p>'
         '<p style="margin-top:8px">2. <b>Físico:</b> Tiene muros de piedra, ventanas estrechas y un tejado de pizarra gris.</p>'
         '<p style="margin-top:8px">3. <b>Atmósfera:</b> Por dentro huele a madera y a lavanda, y la luz entra tamizada.</p>'
         '<p style="margin-top:8px">4. <b>Valoración:</b> Para mí, ese lugar es sinónimo de paz y de recuerdos felices.</p></div>'),
    ],
    traps=[
        ('Es muy, muy bonito y muy grande y muy especial.', 'Es <strong>impresionante</strong>, de una amplitud sorprendente y con un encanto especial.', 'Evita repetir «muy» y «es»; usa sinónimos y adjetivos más precisos'),
        ('Sus ojos son como el cielo. (comparación incompleta)', 'Sus ojos son <strong>tan claros como</strong> el cielo de agosto.', 'Las comparaciones de igualdad necesitan «tan... como»'),
        ('La ciudad está muy moderna y antigua a la vez.', 'La ciudad <strong>es</strong> moderna en algunos barrios y de sabor antiguo en otros.', 'No uses estar para características permanentes; y reconcilia el contraste con una subordinada'),
        ('Huele a flores y hace olor a pan.', 'Huele a flores y a pan recién horneado.', 'El olfato se describe con OLER A, no con hacer olor'),
        ('Es más grande que yo pensaba.', 'Es más grande de lo que pensaba.', 'Con verbos (pensaba, esperaba) la comparación usa «de lo que», no «que»'),
    ],
    summary=[
        ('Estructura', 'general → físico → atmósfera → valoración', 'Del conjunto a los detalles.'),
        ('Comparación igualdad', 'tan + adj + como', 'Es tan silencioso como una biblioteca.'),
        ('Comparación superior.', 'más + adj + de lo que', 'Es más grande de lo que esperaba.'),
        ('Metáfora', 'A es B (imagen equivalente)', 'El río es una cinta de plata.'),
        ('Sentidos', 'verbos sensoriales: oler, sonar...', 'Huele a mar y a sal.'),
        ('Valoración', 'En mi opinión / Me parece...', 'Para mí, es un lugar único.'),
    ],
    items=[
        ('comparacion', 'comparación', 'recurso estilístico que establece una relación de semejanza o diferencia entre dos elementos', 'analogía',
         '«Tan rápido como el viento» es una ______ de igualdad.', 'comp', 'comparación'),
        ('metafora', 'metáfora', 'figura retórica que describe un elemento en términos de otro con el que comparte rasgos', 'imagen',
         '«El tiempo es un río que no vuelve atrás» es una ______.', 'met', 'metáfora'),
        ('vocabulario-sensorial', 'vocabulario sensorial', 'conjunto de palabras que apelan a los cinco sentidos para crear imágenes vívidas', 'lenguaje de los sentidos',
         'El ______ incluye palabras de vista, oído, tacto, olfato y gusto.', 'vocab', 'vocabulario sensorial'),
        ('adjetivo-preciso', 'adjetivo preciso', 'calificativo que transmite una imagen específica y evita la vaguedad', 'adjetivo específico',
         '«Centelleante» es más ______ que «brillante» para describir los ojos de alguien.', 'adjeti', 'adjetivo preciso'),
        ('estructura-desc', 'estructura descriptiva', 'organización del texto de lo general a lo específico para describir de manera ordenada', 'orden descriptivo',
         'La ______ va de la presentación general al detalle y la valoración.', 'estruct', 'estructura descriptiva'),
        ('atmosfera', 'atmósfera', 'sensación global que transmite un lugar o una situación, creada por detalles sensoriales y emocionales', 'ambiente',
         'La ______ de un lugar se describe con detalles sensoriales y emocionales.', 'atm', 'atmósfera'),
        ('sinónimo', 'sinónimo', 'palabra que tiene el mismo significado o uno muy parecido a otra', 'equivalente léxico',
         'Usar ______ evita la repetición y enriquece el texto.', 'sinón', 'sinónimo'),
        ('valoracion-desc', 'valoración', 'juicio personal del escritor sobre lo que describe, que cierra la descripción', 'opinión personal',
         'La ______ cierra la descripción con la impresión subjetiva del autor.', 'valor', 'valoración'),
    ],
    ex1=('Elige la opción correcta', 'Selecciona la construcción adecuada.', [
        ('Sus ojos eran ______ el mar en verano.', ['tan azules como', 'más azules que', 'tan azules que'], 'tan azules como',
         'Comparación de igualdad: tan + adjetivo + como.'),
        ('El palacio es más imponente ______ esperaba.', ['de lo que', 'que', 'como'], 'de lo que',
         'Comparación superior con verbo → de lo que: más... de lo que esperaba.'),
        ('¿Cuál de estas frases usa una metáfora?', ['La ciudad es un laberinto de piedra.', 'La ciudad tiene muchas calles.', 'La ciudad es muy grande.'], 'La ciudad es un laberinto de piedra.',
         'Laberinto de piedra es una metáfora que describe la ciudad en términos de otra cosa.'),
        ('Para describir el olfato de un lugar usas:', ['Huele a mar y a sal.', 'Es oloroso a mar.', 'Hace olor a sal.'], 'Huele a mar y a sal.',
         'El olfato se describe con OLER A: huele a, olía a.'),
        ('¿Cuál adjetivo es más preciso para describir el sonido de una cascada?', ['atronador', 'muy ruidoso', 'grande'], 'atronador',
         'Atronador es específico para sonidos muy intensos; muy ruidoso es vago.'),
        ('En una descripción avanzada, ¿qué va primero?', ['La presentación general', 'La valoración personal', 'Los detalles sensoriales'], 'La presentación general',
         'La estructura descriptiva va de lo general a lo específico.'),
    ]),
    ex2=('Mejora las frases', 'Escribe una palabra o expresión más precisa que complete la idea.', [
        ('El río es ______ que avanza lentamente. (metáfora con serpiente)', 'una serpiente',
         'El río es una serpiente que avanza... — metáfora que lo describe en términos de otro elemento.'),
        ('Es más antiguo ______ lo que habíamos imaginado. (comparación)', 'de',
         'Más + adjetivo + de lo que + verbo: es más antiguo de lo que imaginábamos.'),
        ('El jardín ______ a rosas y a tierra mojada. (sentido olfativo)', 'olía',
         'Olfato en el pasado: olía a rosas — verbo oler en imperfecto.'),
        ('La montaña ______ entre la niebla como un gigante dormido. (verbo de apariencia)', 'emergía',
         'Emerger/surgir son más precisos y literarios que aparecer para describir un paisaje.'),
        ('Sus ojos eran tan ______ como el cielo de invierno. (adjetivo de color frío)', 'grises',
         'Tan + adjetivo + como: tan grises como el cielo de invierno — comparación vívida.'),
    ]),
    ex3=('Correcto o mejorable', 'Elige la versión más efectiva.', [
        ('¿Cuál descripción es más avanzada?',
         ['Es una ciudad muy bonita con muchas cosas que ver.', 'Es una ciudad de arquitectura imponente, donde cada rincón esconde una historia.', 'La ciudad tiene museos y restaurantes.'],
         'Es una ciudad de arquitectura imponente, donde cada rincón esconde una historia.',
         'La segunda opción usa vocabulario preciso, metáfora y estructura elaborada.'),
        ('¿Cuál comparación es correcta?',
         ['Era tan ruidoso como una discoteca.', 'Era más ruidoso que pensaba.', 'Era tan ruidoso que una discoteca.'],
         'Era tan ruidoso como una discoteca.',
         'Comparación de igualdad: tan + adjetivo + como + referente.'),
        ('¿Cuál frase usa metáfora?',
         ['El sol era una bola de fuego en el horizonte.', 'El sol estaba muy caliente.', 'El sol brillaba mucho.'],
         'El sol era una bola de fuego en el horizonte.',
         'Bola de fuego es una metáfora que describe el sol en términos de otra cosa.'),
        ('¿Qué frase describe mejor el silencio de un lugar?',
         ['Solo se oía el susurro del viento entre los pinos.', 'Era muy silencioso.', 'No había ruido.'],
         'Solo se oía el susurro del viento entre los pinos.',
         'El vocabulario sensorial (susurro, pinos) crea una imagen más vívida que "muy silencioso".'),
        ('¿Cuál es la estructura correcta de una descripción avanzada?',
         ['General → físico → sensorial → valoración', 'Valoración → físico → sensorial', 'Sensorial → general → físico'],
         'General → físico → sensorial → valoración',
         'La descripción avanzada va de lo general a los detalles específicos y termina con la valoración.'),
    ]),
)

CHAPTERS['redaccion-opinion'] = dict(
    level='b1', section='writing', num='W04', short='La Redacción de Opinión',
    title='La Redacción de Opinión — Argumentar y Convencer',
    subtitle='Aprende a expresar y defender tu opinión con argumentos sólidos y conectores adecuados',
    game_desc='Practica los conectores y estructuras para expresar opinión en español.',
    slides=[
        ('Estructura de una redacción de opinión', None,
         '<p class="slide-explanation">Una redacción de opinión tiene tres partes: introducción con tu postura, desarrollo con argumentos y ejemplos, y conclusión que resume tu posición.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Introducción:</b> En mi opinión, las redes sociales tienen más ventajas que inconvenientes.</p>'
         '<p style="margin-top:8px"><b>Desarrollo:</b> En primer lugar... / Por otro lado... / Por ejemplo...</p>'
         '<p style="margin-top:8px"><b>Conclusión:</b> En conclusión, creo que... / Por todo lo anterior...</p></div>'),
        ('Expresar opinión en español', None,
         '<p class="slide-explanation">Existen muchas formas de expresar opinión en español, con distintos grados de certeza.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Certeza:</b> Estoy convencido/a de que... / Es evidente que...</p>'
         '<p style="margin-top:8px"><b>Opinión:</b> En mi opinión... / Creo que... / Desde mi punto de vista...</p>'
         '<p style="margin-top:8px"><b>Duda:</b> No estoy seguro/a de que... (+ subjuntivo) / Me parece que quizás...</p></div>'),
        ('Dar razones y ejemplos', None,
         '<p class="slide-explanation">Cada argumento debe ir acompañado de una razón y, si es posible, un ejemplo concreto.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Introducir razón:</b> porque / ya que / puesto que / dado que</p>'
         '<p style="margin-top:8px"><b>Ejemplo:</b> Por ejemplo... / Como muestra de ello... / Un claro ejemplo es...</p>'
         '<p style="margin-top:8px"><b>Modelo:</b> Las redes sociales son beneficiosas <b>ya que</b> facilitan la comunicación. <b>Por ejemplo</b>, permiten contactar con personas de todo el mundo.</p></div>'),
        ('Conectores de opinión y argumentación', None,
         '<p class="slide-explanation">Los conectores organizan y dan cohesión al texto argumentativo.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Añadir:</b> Además, también, por otro lado, asimismo</p>'
         '<p style="margin-top:8px"><b>Contrastar:</b> Sin embargo, aunque, a pesar de (que), no obstante</p>'
         '<p style="margin-top:8px"><b>Concluir:</b> En conclusión, en definitiva, por todo lo anterior, en resumen</p></div>'),
        ('La conclusión eficaz', None,
         '<p class="slide-explanation">La conclusión retoma la tesis inicial y la refuerza con lo argumentado. No debe añadir ideas nuevas.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Fórmulas de conclusión:</b></p>'
         '<p style="margin-top:8px">En conclusión, <b>creo que</b> los beneficios superan claramente a los inconvenientes.</p>'
         '<p style="margin-top:8px">En definitiva, <b>es necesario</b> encontrar un equilibrio entre la tecnología y la vida real.</p>'
         '<p style="margin-top:8px">Por todo lo anterior, <b>me reafirmo en</b> mi posición inicial.</p></div>'),
    ],
    traps=[
        ('En mi opinión creo que...', '<strong>En mi opinión</strong>, las redes sociales son... (sin repetir «creo que»)', 'No acumules marcadores de opinión; elige uno'),
        ('Por ejemplo: las redes sociales.', 'Por ejemplo, las redes sociales <strong>permiten</strong> comunicarse globalmente.', 'El ejemplo debe ilustrar una idea completa, no solo nombrar un concepto'),
        ('En conclusión, otro argumento es...', 'En conclusión, <strong>los argumentos anteriores demuestran que</strong>...', 'La conclusión no añade argumentos nuevos; sintetiza lo ya dicho'),
        ('Creo que el medio ambiente está importante.', 'Creo que el medio ambiente <strong>es</strong> importante.', 'Importancia como característica permanente → SER, no ESTAR'),
        ('Pero, sin embargo, no obstante,...', '<strong>Sin embargo</strong>, hay que considerar también...', 'No acumules varios conectores de contraste seguidos'),
    ],
    summary=[
        ('Introducción', 'Tesis + postura clara', 'En mi opinión, las redes son beneficiosas.'),
        ('Argumento', 'idea + razón (porque/ya que) + ejemplo', 'Son útiles ya que conectan personas. Por ejemplo...'),
        ('Contraste', 'Sin embargo / Aunque', 'Sin embargo, también tienen riesgos.'),
        ('Añadir', 'Además / Por otro lado', 'Además, fomentan la creatividad.'),
        ('Conclusión', 'En conclusión / En definitiva', 'En conclusión, los beneficios superan los riesgos.'),
        ('Certeza', 'Estoy convencido/a de que', 'Estoy convencida de que el cambio es posible.'),
    ],
    items=[
        ('tesis', 'tesis', 'postura o posición clara que el autor defiende a lo largo de su redacción de opinión', 'argumento central',
         'La ______ se expone en la introducción y se retoma en la conclusión.', 'tes', 'tesis'),
        ('argumento', 'argumento', 'razón o prueba que apoya una postura y ayuda a convencer al lector', 'razonamiento',
         'Cada ______ debe ir acompañado de una razón y un ejemplo concreto.', 'argum', 'argumento'),
        ('en-mi-opinion', 'en mi opinión', 'expresión que introduce el punto de vista personal del autor', 'desde mi punto de vista',
         '«______ , las nuevas tecnologías son imprescindibles» presenta la postura del autor.', 'en mi', 'en mi opinión'),
        ('porque', 'porque / ya que', 'conjunción causal que introduce la razón de una afirmación', 'dado que',
         'Las redes son útiles ______ permiten comunicarse a distancia.', 'porq', 'porque'),
        ('sin-embargo', 'sin embargo', 'conector adversativo que introduce un contraste o una objeción a lo anterior', 'no obstante',
         '«______ , también hay que considerar los riesgos» introduce un contraargumento.', 'sin emb', 'sin embargo'),
        ('ademas', 'además', 'conector aditivo que añade un nuevo argumento o información al anterior', 'asimismo',
         '«______  , fomentan la participación ciudadana» añade un argumento.', 'adem', 'además'),
        ('en-conclusion', 'en conclusión', 'conector que introduce el resumen final de los argumentos y refuerza la tesis', 'en definitiva',
         '«______ , los beneficios superan los inconvenientes» cierra la redacción.', 'en conc', 'en conclusión'),
        ('ejemplo', 'por ejemplo', 'expresión que introduce un caso concreto para ilustrar un argumento', 'como muestra de ello',
         '«______ , muchos jóvenes usan las redes para estudiar» ilustra el argumento.', 'por ej', 'por ejemplo'),
    ],
    ex1=('Conectores de opinión', 'Elige el conector más adecuado.', [
        ('Las ciudades son más contaminantes que el campo. ______ , ofrecen más oportunidades.', ['Sin embargo', 'Por ejemplo', 'Ya que'], 'Sin embargo',
         'Sin embargo introduce una idea que contrasta con la anterior.'),
        ('Las redes facilitan la comunicación. ______ , son una fuente de información.', ['Además', 'Sin embargo', 'En conclusión'], 'Además',
         'Además añade un argumento o información nueva.'),
        ('El transporte público ______ reduce la contaminación porque disminuye el número de coches.', ['ya que', 'sin embargo', 'en conclusión'], 'ya que',
         'Ya que introduce la causa o razón de la afirmación anterior.'),
        ('______ , existen aplicaciones para aprender idiomas de forma gratuita.', ['Por ejemplo', 'Sin embargo', 'En definitiva'], 'Por ejemplo',
         'Por ejemplo introduce un caso concreto que ilustra el argumento.'),
        ('Los teléfonos son útiles. ______ , deben usarse con moderación.', ['No obstante', 'Además', 'Por ejemplo'], 'No obstante',
         'No obstante (= sin embargo) introduce una objeción o matización.'),
        ('______ , creo que la tecnología mejora nuestra calidad de vida.', ['En conclusión', 'Por ejemplo', 'Ya que'], 'En conclusión',
         'En conclusión resume y cierra la argumentación.'),
    ]),
    ex2=('Completa la redacción', 'Escribe la palabra o expresión que falta.', [
        ('En mi ______ , las ciudades necesitan más zonas verdes. (postura)', 'opinión',
         'En mi opinión introduce la postura personal del autor.'),
        ('El deporte es beneficioso, ______ reduce el estrés y mejora la salud. (razón)', 'ya que',
         'Ya que (= porque) introduce la causa.'),
        ('______ , hay estudios que demuestran que el ejercicio alarga la vida. (ilustración)', 'Por ejemplo',
         'Por ejemplo introduce un caso o dato concreto.'),
        ('______ , no todo el mundo puede permitirse un gimnasio. (objeción)', 'Sin embargo',
         'Sin embargo introduce un contraargumento o una limitación.'),
        ('En ______ , los beneficios del deporte superan sus inconvenientes. (resumen)', 'conclusión',
         'En conclusión resume los argumentos y refuerza la tesis.'),
    ]),
    ex3=('Estructura de la opinión', 'Elige la opción correcta.', [
        ('¿Dónde se expone la tesis en una redacción de opinión?',
         ['En la introducción', 'En la conclusión', 'En el desarrollo'], 'En la introducción',
         'La tesis se expone al principio y se retoma en la conclusión.'),
        ('¿Qué conector usas para añadir un argumento nuevo?',
         ['Además', 'Sin embargo', 'Por ejemplo'], 'Además',
         'Además añade información o un nuevo argumento.'),
        ('¿Qué conector usas para introducir un contraste?',
         ['Sin embargo', 'Además', 'Ya que'], 'Sin embargo',
         'Sin embargo introduce una idea contraria o una objeción.'),
        ('¿Qué debe incluir la conclusión?',
         ['Un resumen de los argumentos y la reafirmación de la tesis', 'Un argumento nuevo y una pregunta', 'Solo una frase corta'], 'Un resumen de los argumentos y la reafirmación de la tesis',
         'La conclusión sintetiza lo dicho y refuerza la postura inicial.'),
        ('¿Cuál es la mejor tesis para una redacción sobre el transporte público?',
         ['En mi opinión, el transporte público beneficia a toda la sociedad.', 'El transporte público existe en muchas ciudades.', 'Hay muchos tipos de transporte.'],
         'En mi opinión, el transporte público beneficia a toda la sociedad.',
         'La tesis debe expresar claramente la postura del autor sobre el tema.'),
    ]),
)

CHAPTERS['resena'] = dict(
    level='b1', section='writing', num='W05', short='La Reseña',
    title='La Reseña — Recomendar Libros y Películas',
    subtitle='Aprende a escribir reseñas de libros, películas y otros productos culturales',
    game_desc='Practica el vocabulario y la estructura para escribir reseñas en español.',
    slides=[
        ('¿Qué es una reseña?', None,
         '<p class="slide-explanation">Una reseña es un texto en el que presentas, describes brevemente y valoras una obra cultural (libro, película, serie, restaurante...).</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>1. Presentación:</b> ¿Qué es? ¿De quién es? ¿De qué trata?</p>'
         '<p style="margin-top:8px"><b>2. Descripción:</b> Los aspectos más importantes sin destripar el final.</p>'
         '<p style="margin-top:8px"><b>3. Valoración:</b> ¿Qué te gustó? ¿Qué mejorarías? ¿Lo recomiendas?</p></div>'),
        ('Vocabulario para hablar de libros', None,
         '<p class="slide-explanation">El vocabulario específico de las reseñas de libros te permite ser más preciso y profesional.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>El género:</b> novela, cuento, thriller, novela histórica, poesía, ensayo</p>'
         '<p style="margin-top:8px"><b>El argumento:</b> la trama, el argumento, la historia</p>'
         '<p style="margin-top:8px"><b>Los personajes:</b> el protagonista, el antagonista, el narrador</p>'
         '<p style="margin-top:8px"><b>El estilo:</b> el ritmo, la prosa, el lenguaje, el tono</p></div>'),
        ('Vocabulario para hablar de películas', None,
         '<p class="slide-explanation">Para reseñar películas o series necesitas un vocabulario diferente.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>El género:</b> comedia, drama, thriller, documental, ciencia ficción</p>'
         '<p style="margin-top:8px"><b>La producción:</b> el director/la directora, el reparto, la banda sonora, los efectos especiales</p>'
         '<p style="margin-top:8px"><b>La valoración:</b> impresionante, emocionante, decepcionante, predecible, original</p></div>'),
        ('Expresar valoración sin desvelar el final', None,
         '<p class="slide-explanation">Una buena reseña no revela el final (spoiler). Usa expresiones vagas para hablar del desenlace.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Bien:</b> El desenlace es completamente inesperado y te deja sin palabras.</p>'
         '<p style="margin-top:8px"><b>Bien:</b> No voy a revelar cómo termina, pero te aseguro que no lo adivinarás.</p>'
         '<p style="margin-top:8px"><b>Mal:</b> Al final resulta que el detective era el asesino.</p></div>'),
        ('Recomendar o no recomendar', None,
         '<p class="slide-explanation">La reseña debe terminar con una recomendación clara, dirigida al público adecuado.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Recomendar:</b> La recomiendo sin reservas. / Es una lectura imprescindible para...</p>'
         '<p style="margin-top:8px"><b>Con matices:</b> La recomiendo a los amantes del género, aunque los finales abiertos pueden frustrar.</p>'
         '<p style="margin-top:8px"><b>No recomendar:</b> A pesar de sus buenas críticas, no la recomendaría porque...</p></div>'),
    ],
    traps=[
        ('La película es sobre un detective que mata al final.', 'La película sigue a un detective en un caso <strong>cuyo desenlace sorprende</strong>.', 'No reveles el final; usa expresiones vagas para hablar del desenlace'),
        ('El libro está muy bien y me gustó.', 'El libro está escrito con una prosa ágil y me <strong>enganchó desde las primeras páginas</strong>.', 'Evita valoraciones vagas; sé específico sobre lo que valoras'),
        ('El protagonista se llama Pedro y es detective y investiga y...', 'El protagonista, un detective de mediana edad, <strong>investiga</strong> un misterio que...', 'Usa frases subordinadas en lugar de coordinar todo con «y»'),
        ('Es una novela de amor romántica y tiene mucho amor.', 'Es una <strong>novela romántica</strong> de gran intensidad emocional.', 'Evita la redundancia: novela de amor romántica → novela romántica'),
        ('No me gustó nada. Es mala.', 'A pesar de su premisa interesante, la trama resulta <strong>predecible</strong> y el ritmo se hace lento.', 'Justifica siempre las valoraciones negativas con razones específicas'),
    ],
    summary=[
        ('Presentación', 'título + autor/director + género', 'Es una novela de Isabel Allende.'),
        ('Argumento', 'La historia trata de... / La trama gira en torno a...', 'La trama gira en torno a un viaje.'),
        ('Valoración positiva', 'Lo que más me gustó fue...', 'Lo que más me gustó fue el ritmo.'),
        ('Valoración negativa', 'Sin embargo, el final me pareció...', 'El final me pareció algo previsible.'),
        ('Recomendación', 'La recomiendo / No la recomendaría', 'La recomiendo a los amantes del género.'),
        ('Público', 'ideal para / perfecta para quienes...', 'Ideal para quienes disfrutan del suspense.'),
    ],
    items=[
        ('resena', 'reseña', 'texto crítico breve en el que se presenta y valora una obra cultural', 'crítica',
         'Una ______ de cine incluye la presentación, el argumento parcial y la valoración.', 'rese', 'reseña'),
        ('trama', 'trama', 'secuencia de los hechos y conflictos que conforman la historia de una obra', 'argumento',
         'La ______ de la novela tiene varios giros inesperados que mantienen el suspense.', 'tram', 'trama'),
        ('protagonista', 'protagonista', 'personaje principal de una obra narrativa o cinematográfica en torno al cual gira la historia', 'personaje principal',
         'El ______ de la película es un joven detective recién llegado a la ciudad.', 'protag', 'protagonista'),
        ('genero', 'género', 'categoría que clasifica una obra según sus características formales y temáticas', 'tipo de obra',
         'El ______ de la novela es el thriller psicológico.', 'gén', 'género'),
        ('valoracion', 'valoración', 'juicio crítico sobre los méritos y defectos de una obra', 'crítica',
         'La ______ de una reseña debe ser específica y justificada.', 'valor', 'valoración'),
        ('recomendar', 'recomendar', 'aconsejar a alguien que vea, lea o pruebe algo que has valorado positivamente', 'aconsejar',
         'Al final de la reseña debes ______ la obra al público adecuado.', 'recom', 'recomendar'),
        ('banda-sonora', 'banda sonora', 'música compuesta o seleccionada especialmente para acompañar una película o serie', 'música de la película',
         'La ______ del documental contribuye a crear una atmósfera muy emotiva.', 'banda', 'banda sonora'),
        ('ritmo', 'ritmo', 'velocidad y fluidez con que se desarrolla la trama de una obra narrativa o audiovisual', 'cadencia narrativa',
         'El ______ de la novela se acelera en los últimos capítulos.', 'ritm', 'ritmo'),
    ],
    ex1=('Vocabulario de la reseña', 'Elige la palabra más adecuada para cada hueco.', [
        ('La ______ de la novela tarda en arrancar, pero a partir del tercer capítulo engancha.', ['trama', 'banda sonora', 'reparto'], 'trama',
         'La trama es la secuencia de hechos de una obra narrativa.'),
        ('El ______ de la película es un joven médico que descubre un secreto familiar.', ['protagonista', 'director', 'género'], 'protagonista',
         'El protagonista es el personaje principal de la historia.'),
        ('Es una novela de ______ histórico ambientada en la España del siglo XIX.', ['género', 'trama', 'reparto'], 'género',
         'Género clasifica la obra: novela histórica, thriller, comedia...'),
        ('La ______ del documental es impresionante y complementa perfectamente las imágenes.', ['banda sonora', 'trama', 'valoración'], 'banda sonora',
         'La banda sonora es la música que acompaña una película o documental.'),
        ('No voy a ______ el final, pero te garantizo que te sorprenderá.', ['desvelar', 'recomendar', 'presentar'], 'desvelar',
         'Desvelar = revelar; en una reseña evitamos desvelar el final (spoiler).'),
        ('La ______ de la novela es lenta al principio pero se acelera al final.', ['trama', 'banda sonora', 'valoración'], 'trama',
         'La trama también hace referencia al ritmo y desarrollo de la historia.'),
    ]),
    ex2=('Completa la reseña', 'Escribe la palabra o expresión que falta.', [
        ('La ______ de la película gira en torno a un robo imposible. (argumento)', 'trama',
         'La trama es la historia o argumento de una obra.'),
        ('El ______ es Pedro Almodóvar, uno de los directores más reconocidos del cine español. (quien dirige)', 'director',
         'El director es quien realiza y supervisa la producción de una película.'),
        ('Lo que más me gustó fue el ______ de los actores principales. (trabajo de actores)', 'reparto',
         'El reparto es el conjunto de actores que interpretan los papeles de la película.'),
        ('La ______ sin reservas a todos los amantes del suspense. (consejo positivo)', 'recomiendo',
         'Recomendar es aconsejar a alguien que vea o lea algo.'),
        ('Sin embargo, el ______ final me pareció algo previsible. (cómo termina)', 'desenlace',
         'El desenlace es la resolución final de la trama.'),
    ]),
    ex3=('Buenas y malas prácticas', 'Elige la versión correcta para cada situación.', [
        ('¿Cómo hablas del final sin desvelarlo?',
         ['El desenlace es inesperado y te dejará sin palabras.', 'Al final el protagonista muere.', 'El final no me gustó.'],
         'El desenlace es inesperado y te dejará sin palabras.',
         'Evita el spoiler; habla del impacto del final, no de lo que ocurre.'),
        ('¿Cuál es la valoración más específica y útil?',
         ['La actuación de la protagonista es extraordinariamente matizada y emotiva.', 'Está muy bien.', 'Me gustó mucho.'],
         'La actuación de la protagonista es extraordinariamente matizada y emotiva.',
         'La valoración específica da información concreta al lector; evita frases vagas.'),
        ('¿A quién diriges la recomendación?',
         ['La recomiendo a los amantes del suspense psicológico.', 'La recomiendo a todo el mundo.', 'No sé si recomendarla.'],
         'La recomiendo a los amantes del suspense psicológico.',
         'Una recomendación específica es más útil porque ayuda al lector a saber si la obra es para él.'),
        ('¿Cuál es la mejor descripción del género?',
         ['Es un thriller psicológico con elementos de drama familiar.', 'Es un libro de misterio y cosas así.', 'Es un libro interesante.'],
         'Es un thriller psicológico con elementos de drama familiar.',
         'El género se define con precisión para orientar al lector sobre qué tipo de obra es.'),
        ('¿Qué estructura sigue una reseña?',
         ['Presentación → argumento parcial → valoración → recomendación', 'Opinión → presentación → resumen completo', 'Resumen completo → opinión'],
         'Presentación → argumento parcial → valoración → recomendación',
         'La reseña presenta la obra, describe parte del argumento sin spoilers, valora y recomienda.'),
    ]),
)

CHAPTERS['carta-informal'] = dict(
    level='b1', section='writing', num='W06', short='La Carta Informal',
    title='La Carta Informal — Escribir a Amigos y Familia',
    subtitle='Aprende a escribir cartas informales con la estructura y el tono adecuados',
    game_desc='Practica las fórmulas y estructuras de la carta informal en español.',
    slides=[
        ('Carta vs. correo electrónico informal', None,
         '<p class="slide-explanation">La carta informal y el correo informal son similares pero la carta tiene elementos físicos propios: lugar y fecha arriba a la derecha, y el texto manuscrito.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Arriba a la derecha:</b> Madrid, 14 de junio de 2026</p>'
         '<p style="margin-top:8px"><b>Saludo:</b> Querido/a + nombre: (con dos puntos o coma)</p>'
         '<p style="margin-top:8px"><b>Apertura:</b> Gracias por tu carta. / Me alegró mucho saber que...</p>'
         '<p style="margin-top:8px"><b>Cuerpo, despedida y firma:</b> como en el correo informal</p></div>'),
        ('Fórmulas para responder a una carta', None,
         '<p class="slide-explanation">Cuando respondes a una carta, es habitual hacer referencia a lo que ha escrito el otro.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Agradecer la carta:</b> Gracias por tu carta / Me alegró mucho recibir noticias tuyas.</p>'
         '<p style="margin-top:8px"><b>Referirse al contenido:</b> Me alegra saber que estás bien. / Me sorprendió enterarme de que...</p>'
         '<p style="margin-top:8px"><b>Enlazar temas:</b> En cuanto a lo que me comentas sobre... / Respecto a tu pregunta...</p></div>'),
        ('Tono y registro informal', None,
         '<p class="slide-explanation">En una carta informal puedes ser más expresivo y espontáneo que en una formal. Usa el tuteo y un vocabulario cercano.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Expresar sentimientos:</b> Me alegró mucho / Qué pena que / ¡Qué bien que!</p>'
         '<p style="margin-top:8px"><b>Preguntar por el otro:</b> ¿Cómo te va? / ¿Qué tal el trabajo? / Espero que estés bien.</p>'
         '<p style="margin-top:8px"><b>Hablar de planes:</b> Me muero de ganas de verte / Tengo muchas ganas de que vengas.</p></div>'),
        ('La postdata (P.D.)', None,
         '<p class="slide-explanation">La postdata (P.D.) es una nota breve que se añade al final de la carta, después de la firma, para añadir algo olvidado.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>P.D.:</b> Se me olvidaba decirte que el sábado hay una fiesta en casa de Ana. ¿Vienes?</p>'
         '<p style="margin-top:8px"><b>P.D.:</b> Saluda de mi parte a tus padres.</p></div>'),
        ('Despedidas y firmas informales', None,
         '<p class="slide-explanation">La despedida y la firma informales reflejan la calidez de la relación con el destinatario.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Despedidas:</b> Un beso muy fuerte · Un abrazo · Con todo mi cariño · Hasta pronto</p>'
         '<p style="margin-top:8px"><b>Cierres:</b> Escríbeme pronto. · Espero saber de ti. · No tardes en contestar.</p>'
         '<p style="margin-top:8px"><b>Firma:</b> solo el nombre de pila o el apodo.</p></div>'),
    ],
    traps=[
        ('Madrid, 14/06/2026', 'Madrid, <strong>14 de junio de 2026</strong>', 'En las cartas la fecha se escribe con letras, no con números'),
        ('Querido Ana:', 'Querida Ana:', 'Querido/a concuerda con el género del destinatario'),
        ('Gracias por me escribir.', 'Gracias por <strong>escribirme</strong>.', 'Después de «por» va infinitivo; el pronombre se une al infinitivo'),
        ('Me alegra mucho que vienes.', 'Me alegra mucho que <strong>vengas</strong>.', 'Me alegra que + subjuntivo, no indicativo'),
        ('Besos. Tu amiga, Ana. (orden invertido)', 'Con todo mi cariño, <strong>Ana.</strong>', 'La firma va sola, después de la despedida; no antes'),
    ],
    summary=[
        ('Fecha y lugar', 'Ciudad, día de mes de año', 'Madrid, 14 de junio de 2026'),
        ('Saludo', 'Querido/a + nombre:', 'Querida Laura:'),
        ('Apertura', 'Gracias por tu carta. / Me alegró...', 'Me alegró mucho recibir noticias tuyas.'),
        ('Referencia', 'En cuanto a lo que me comentas...', 'Respecto a tu pregunta sobre los cursos...'),
        ('Despedida', 'Un abrazo / Con cariño', 'Un beso muy fuerte.'),
        ('P.D.', 'P.D.: + nota breve olvidada', 'P.D.: Saluda a tu madre de mi parte.'),
    ],
    items=[
        ('carta-informal', 'carta informal', 'texto escrito y generalmente manuscrito que se dirige a personas de confianza con un tono cercano', 'carta personal',
         'Una ______ comienza con el lugar y la fecha arriba a la derecha.', 'carta', 'carta informal'),
        ('querido', 'querido/a', 'fórmula de saludo afectuoso que abre una carta informal y concuerda con el género del destinatario', 'estimado/a (informal)',
         '«______ Pablo:» abre una carta a un amigo; «______ María:» a una amiga.', 'querid', 'querido/a'),
        ('pd', 'P.D.', 'nota añadida al final de la carta después de la firma para incluir algo olvidado', 'postdata',
         'La ______ va después de la firma y empieza con «Se me olvidaba decirte...»', 'PD', 'P.D.'),
        ('apertura-carta', 'apertura', 'primera frase de la carta que agradece la carta recibida o explica el motivo de escribir', 'inicio de la carta',
         '«Gracias por tu carta» es una ______ típica de la carta informal.', 'apert', 'apertura'),
        ('referirse', 'referirse a', 'mencionar o aludir a algo que el destinatario ha escrito en su carta anterior', 'hacer referencia',
         '«En cuanto a lo que me comentas...» sirve para ______ al contenido de la carta recibida.', 'refer', 'referirse a'),
        ('postdata', 'postdata', 'nota breve que se añade después de la firma para incluir información olvidada', 'nota final',
         'La ______ (P.D.) va siempre después de la firma.', 'postd', 'postdata'),
        ('fecha-carta', 'fecha en la carta', 'indicación del lugar y la fecha en que se escribe la carta, situada arriba a la derecha', 'datación',
         'La ______ se escribe como «Madrid, 14 de junio de 2026».', 'fecha', 'fecha en la carta'),
        ('tuteo', 'tuteo', 'uso del pronombre tú para dirigirse al interlocutor, propio del registro informal', 'tratamiento informal',
         'Las cartas informales usan el ______ : «espero que estés bien».', 'tute', 'tuteo'),
    ],
    ex1=('Elige la opción correcta', 'Selecciona la fórmula o la palabra adecuada.', [
        ('¿Dónde va la fecha en una carta informal?', ['Arriba a la derecha', 'Arriba a la izquierda', 'Al final de la carta'], 'Arriba a la derecha',
         'El lugar y la fecha se escriben arriba a la derecha en las cartas.'),
        ('¿Cómo escribes la fecha en una carta?', ['Madrid, 14 de junio de 2026', 'Madrid, 14/06/2026', '14-6-26, Madrid'], 'Madrid, 14 de junio de 2026',
         'En las cartas la fecha se escribe con letras: día + de + mes + de + año.'),
        ('El saludo para tu amiga Clara es:', ['Querida Clara:', 'Querido Clara:', 'Estimada Clara:'], 'Querida Clara:',
         'Querida (femenino) para una mujer; estimada es demasiado formal.'),
        ('¿Cuál es una buena fórmula de apertura para una respuesta?', ['Me alegró mucho recibir tu carta.', '¡Hola! ¿Cómo estás?', 'Me dirijo a usted para...'], 'Me alegró mucho recibir tu carta.',
         'Me alegró recibir tu carta es la apertura clásica cuando respondes a una carta.'),
        ('¿Qué es la P.D.?', ['Una nota añadida después de la firma', 'El saludo inicial', 'La despedida'], 'Una nota añadida después de la firma',
         'P.D. = postdata: nota breve al final de la carta para algo olvidado.'),
        ('¿Cuál es una despedida informal correcta?', ['Con todo mi cariño, Marta.', 'Atentamente, Marta.', 'Le saluda cordialmente, Marta.'], 'Con todo mi cariño, Marta.',
         'Con todo mi cariño es informal; atentamente y le saluda son formales.'),
    ]),
    ex2=('Completa la carta', 'Escribe la palabra o expresión que falta.', [
        ('Sevilla, 10 ______ mayo de 2026. (preposición de fecha)', 'de',
         'La fecha usa de: 10 de mayo de 2026.'),
        ('______ Manuel: (saludo informal a un hombre)', 'Querido',
         'Querido (masculino) + nombre + dos puntos.'),
        ('Me ______ mucho recibir tu carta después de tanto tiempo. (sentimiento positivo)', 'alegró',
         'Me alegró (indefinido) mucho recibir tu carta: fórmula de apertura.'),
        ('En ______ a lo que me preguntas sobre el trabajo... (referencia)', 'cuanto',
         'En cuanto a lo que me preguntas... sirve para referirse al contenido de la carta recibida.'),
        ('______ : Se me olvidaba decirte que el sábado hay una exposición. (nota final)', 'P.D.',
         'P.D. (postdata) introduce una nota añadida después de la firma.'),
    ]),
    ex3=('Carta vs. correo / formal vs. informal', 'Elige la opción correcta.', [
        ('¿Qué elemento está solo en la carta informal, no en el correo?', ['La fecha y el lugar arriba a la derecha', 'El asunto del mensaje', 'El saludo con el nombre'], 'La fecha y el lugar arriba a la derecha',
         'En la carta física se escribe el lugar y la fecha arriba; en el correo está la línea de asunto.'),
        ('¿Cuál de estas despedidas es informal?', ['Un abrazo muy fuerte.', 'Atentamente.', 'Reciba un cordial saludo.'], 'Un abrazo muy fuerte.',
         'Un abrazo es informal; atentamente y reciba un cordial saludo son formales.'),
        ('«Me alegra que vengas» o «Me alegra que vienes»: ¿cuál es correcta?', ['Me alegra que vengas.', 'Me alegra que vienes.', 'Las dos son correctas.'], 'Me alegra que vengas.',
         'Me alegra que + subjuntivo: vengas, no vienes.'),
        ('¿Qué tono usas en una carta a un amigo?', ['Informal, cercano y espontáneo', 'Formal y protocolario', 'Técnico y preciso'], 'Informal, cercano y espontáneo',
         'Las cartas informales usan el tuteo y un tono afectuoso y natural.'),
        ('¿Dónde va la firma en una carta informal?', ['Después de la despedida y la P.D.', 'Antes del saludo', 'En el margen izquierdo'], 'Después de la despedida y la P.D.',
         'La firma cierra la carta, después de la despedida y, si existe, la postdata.'),
    ]),
)

CHAPTERS['biografia-resumen'] = dict(
    level='b1', section='writing', num='W07', short='La Biografía Breve',
    title='La Biografía Breve — Contar una Vida',
    subtitle='Aprende a escribir una breve biografía estructurada de una persona real o ficticia',
    game_desc='Practica los tiempos y las estructuras para escribir biografías en español.',
    slides=[
        ('Estructura de la biografía', None,
         '<p class="slide-explanation">Una biografía breve presenta la vida de una persona en orden cronológico: nacimiento, educación, carrera, logros y legado.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>1. Nacimiento:</b> Nació en Madrid en 1950.</p>'
         '<p style="margin-top:8px"><b>2. Educación:</b> Estudió Medicina en la Universidad Complutense.</p>'
         '<p style="margin-top:8px"><b>3. Carrera:</b> Trabajó como investigadora durante veinte años.</p>'
         '<p style="margin-top:8px"><b>4. Logros:</b> Recibió el Premio Nacional en 1998.</p>'
         '<p style="margin-top:8px"><b>5. Legado:</b> Es conocida por sus aportaciones a la ciencia española.</p></div>'),
        ('Tiempos verbales en la biografía', None,
         '<p class="slide-explanation">El indefinido narra los hitos biográficos. El imperfecto describe el contexto o los rasgos de personalidad.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Indefinido (hitos):</b> Nació, estudió, publicó, recibió el premio, murió.</p>'
         '<p style="margin-top:8px"><b>Imperfecto (contexto):</b> Era una persona muy dedicada. Vivía en un pequeño apartamento.</p>'
         '<p style="margin-top:8px"><b>Presente (legado):</b> Hoy en día, su obra sigue siendo una referencia mundial.</p></div>'),
        ('Vocabulario biográfico', None,
         '<p class="slide-explanation">El vocabulario de la biografía incluye expresiones para situar en el tiempo y describir la trayectoria vital.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Nacimiento:</b> nació en... / es natural de... / vino al mundo en...</p>'
         '<p style="margin-top:8px"><b>Estudios:</b> estudió en... / se licenció en... / se doctoró en...</p>'
         '<p style="margin-top:8px"><b>Carrera:</b> comenzó a trabajar / llegó a ser / fue nombrado/a</p>'
         '<p style="margin-top:8px"><b>Logros:</b> publicó / descubrió / ganó / recibió el premio</p>'
         '<p style="margin-top:8px"><b>Legado:</b> es conocido/a por / su obra influyó en</p></div>'),
        ('Marcadores temporales biográficos', None,
         '<p class="slide-explanation">Los marcadores temporales son esenciales para situar los hechos en el tiempo.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Inicio:</b> desde muy joven / en su infancia / a los diez años</p>'
         '<p style="margin-top:8px"><b>Secuencia:</b> más tarde / posteriormente / con el tiempo / años después</p>'
         '<p style="margin-top:8px"><b>Culminación:</b> finalmente / al cabo de los años / en la cima de su carrera</p></div>'),
        ('Legado e influencia', None,
         '<p class="slide-explanation">El cierre de la biografía evalúa el impacto y el legado de la persona.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-range:6px">'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Es conocido/a por:</b> Es conocida por sus novelas traducidas a veinte idiomas.</p>'
         '<p style="margin-top:8px"><b>Su obra influyó en:</b> Su pensamiento influyó en toda una generación de escritores.</p>'
         '<p style="margin-top:8px"><b>Hoy en día:</b> Hoy en día, su nombre es sinónimo de innovación científica.</p></div>'),
    ],
    traps=[
        ('Nació en el año 1950 en Madrid en España.', 'Nació en Madrid en 1950.', 'No repitas información de ubicación; combina lugar y año con economía'),
        ('Estudió y fue médico y luego ganó un premio.', 'Estudió medicina, ejerció como médico y <strong>posteriormente</strong> recibió un premio.', 'Evita la coordinación excesiva con «y»; usa conectores temporales'),
        ('Es conocida para sus novelas.', 'Es conocida <strong>por</strong> sus novelas.', 'Es conocido/a POR sus logros, no para'),
        ('Llegó a ser un científico famoso.', 'Llegó a ser <strong>una</strong> científica <strong>de renombre</strong>.', 'Concuerda el artículo con el género; usa adjetivos más precisos que famoso'),
        ('Hoy en día su obra todavía sigue siendo relevante aún.', 'Hoy en día su obra <strong>sigue siendo</strong> relevante.', 'No acumules «todavía» y «aún» con «sigue siendo»; elige uno'),
    ],
    summary=[
        ('Nacimiento', 'nació en + lugar + año', 'Nació en Sevilla en 1923.'),
        ('Formación', 'estudió / se licenció en', 'Estudió Filosofía en Madrid.'),
        ('Carrera', 'comenzó a / llegó a ser', 'Llegó a ser directora del museo.'),
        ('Logros', 'publicó / ganó / recibió', 'Recibió el Premio Nobel en 1999.'),
        ('Legado', 'es conocido/a por / su obra influyó', 'Es conocida por sus ensayos.'),
        ('Hoy en día', 'sigue siendo / su nombre es sinónimo de', 'Sigue siendo una referencia.'),
    ],
    items=[
        ('biografia', 'biografía', 'texto que narra la vida de una persona real con datos ordenados cronológicamente', 'semblanza',
         'Una ______ breve recoge los hitos más importantes de la vida de alguien.', 'biogr', 'biografía'),
        ('nacio', 'nacer en', 'verbo que indica el lugar y el momento en que una persona vino al mundo', 'venir al mundo',
         '«______ Madrid en 1950» sitúa el origen de la persona.', 'nació en', 'nacer en'),
        ('licenciarse', 'licenciarse en', 'obtener el título universitario de licenciatura en una disciplina', 'graduarse en',
         '«Se ______ Derecho por la Universidad de Valencia» indica la formación universitaria.', 'licenci', 'licenció en'),
        ('llegar-a-ser', 'llegar a ser', 'expresión que indica el punto de mayor éxito o reconocimiento en una carrera', 'convertirse en',
         '«______ directora del Banco Central» expresa el punto culminante de su carrera.', 'llegó a', 'llegar a ser'),
        ('es-conocido', 'ser conocido/a por', 'expresión que resume el legado o la fama de una persona', 'ser famoso/a por',
         '«______ sus experimentos con la luz» resume su contribución científica.', 'es conocid', 'ser conocido/a por'),
        ('marcador-bio', 'marcador temporal', 'expresión que sitúa un hecho en el tiempo dentro de una narración biográfica', 'referencia temporal',
         '«Más tarde» y «años después» son ______ temporales que conectan hitos biográficos.', 'marc', 'marcador temporal'),
        ('legado', 'legado', 'conjunto de obras, ideas o valores que una persona deja a las generaciones futuras', 'herencia',
         'El ______ de Picasso sigue influyendo en el arte contemporáneo.', 'leg', 'legado'),
        ('hoy-en-dia', 'hoy en día', 'expresión que sitúa algo en el momento presente y contrasta con el pasado biográfico', 'actualmente',
         '«______ , su obra se estudia en todo el mundo» cierra la biografía con el impacto actual.', 'hoy', 'hoy en día'),
    ],
    ex1=('Tiempos verbales', 'Elige el tiempo verbal correcto para cada contexto biográfico.', [
        ('Pablo Picasso ______ en Málaga en 1881. (nacimiento)', ['nació', 'nacía', 'nace'], 'nació',
         'Hecho biográfico concreto → indefinido: nació.'),
        ('De joven, ______ una persona muy creativa e inquieta. (descripción de carácter)', ['era', 'fue', 'es'], 'era',
         'Descripción de carácter en el pasado → imperfecto: era.'),
        ('En 1937, ______ el Guernica, su obra más famosa. (hito)', ['pintó', 'pintaba', 'pinta'], 'pintó',
         'Hito biográfico concreto → indefinido: pintó.'),
        ('Hoy en día su obra ______ en los principales museos del mundo. (legado)', ['se exhibe', 'se exhibió', 'se exhibía'], 'se exhibe',
         'El legado actual se expresa en presente: se exhibe.'),
        ('______ a ser el artista más influyente del siglo XX. (culminación)', ['Llegó', 'Llegaba', 'Llega'], 'Llegó',
         'Hito biográfico → indefinido: llegó a ser.'),
        ('Cuando ______ joven, viajó a París para formarse. (contexto)', ['era', 'fue', 'es'], 'era',
         'Contexto de un hecho pasado → imperfecto: cuando era joven (contexto) + viajó (acción).'),
    ]),
    ex2=('Completa la biografía', 'Escribe la palabra o expresión que falta.', [
        ('María de Maeztu ______ en Vitoria en 1882. (nacimiento)', 'nació',
         'Hecho biográfico → indefinido: nació en Vitoria en 1882.'),
        ('Se ______ en Filosofía y Letras por la Universidad de Salamanca. (título universitario)', 'licenció',
         'Licenciarse en: se licenció en Filosofía y Letras.'),
        ('Años ______ , fundó la Residencia de Señoritas en Madrid. (tiempo transcurrido)', 'después',
         'Años después indica que algo ocurre un tiempo más tarde.'),
        ('Es conocida ______ su labor en la educación de la mujer en España. (preposición de logro)', 'por',
         'Es conocida por + sus logros o contribuciones.'),
        ('______ en día, su figura es reconocida como pionera del feminismo español. (presente)', 'Hoy',
         'Hoy en día sitúa el legado en el momento presente.'),
    ]),
    ex3=('Estructura y corrección', 'Elige la opción correcta.', [
        ('¿Qué tiempo verbal usas para narrar los hitos biográficos?', ['El pretérito indefinido', 'El imperfecto', 'El presente'], 'El pretérito indefinido',
         'Los hitos biográficos (nació, estudió, recibió) usan el indefinido.'),
        ('¿Cuál es el marcador temporal más adecuado para introducir el legado?', ['Hoy en día', 'De repente', 'Primero'], 'Hoy en día',
         'Hoy en día sitúa el legado en el momento actual, en contraste con el pasado biográfico.'),
        ('¿Cuál de estas frases describe mejor el legado?', ['Es conocida por sus aportaciones a la ciencia.', 'Es conocida para sus aportaciones.', 'Fue conocida para sus aportaciones.'], 'Es conocida por sus aportaciones a la ciencia.',
         'Es conocido/a POR + sustantivo es la expresión correcta de legado.'),
        ('¿Cuál es la estructura correcta de una biografía?', ['Nacimiento → formación → carrera → logros → legado', 'Legado → carrera → nacimiento', 'Logros → nacimiento → formación'], 'Nacimiento → formación → carrera → logros → legado',
         'La biografía sigue un orden cronológico de la vida a las contribuciones.'),
        ('¿Cuál de estas frases expresa el inicio de la carrera?', ['Comenzó a trabajar como periodista a los veintidós años.', 'Era periodista joven.', 'Le gustaba el periodismo.'], 'Comenzó a trabajar como periodista a los veintidós años.',
         'Comenzar a + infinitivo + dato de tiempo expresa el inicio de la carrera.'),
    ]),
)

CHAPTERS['dialogo'] = dict(
    level='b1', section='writing', num='W08', short='El Diálogo Escrito',
    title='El Diálogo Escrito — Conversaciones en Papel',
    subtitle='Aprende a escribir diálogos con la puntuación y los verbos de habla correctos',
    game_desc='Practica los elementos del diálogo escrito en español.',
    slides=[
        ('La raya en el diálogo español', None,
         '<p class="slide-explanation">En español los diálogos escritos usan la raya (—) para introducir las intervenciones de cada personaje, no las comillas dobles.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Incorrecto:</b> "Buenos días", dijo Ana.</p>'
         '<p style="margin-top:8px"><b>Correcto:</b> —Buenos días —dijo Ana.</p>'
         '<p style="margin-top:8px"><b>Sin verbo de habla:</b> —Buenos días.</p>'
         '<p style="margin-top:8px"><b>Con acotación:</b> —Buenos días —dijo Ana sonriendo.</p></div>'),
        ('Verbos de habla', None,
         '<p class="slide-explanation">Los verbos de habla introducen o acompañan lo que dice un personaje. Varían según el tono y la emoción.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Neutros:</b> dijo, respondió, contestó, preguntó, añadió</p>'
         '<p style="margin-top:8px"><b>Emotivos:</b> exclamó, susurró, gritó, murmuró, protestó</p>'
         '<p style="margin-top:8px"><b>De pensamiento:</b> pensó (para el monólogo interior)</p></div>'
         '<p style="margin-top:16px">Evita repetir siempre «dijo»: varía con respondió, añadió, etc.</p>'),
        ('Puntuación del diálogo', None,
         '<p class="slide-explanation">La puntuación del diálogo sigue reglas específicas en español.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Sin verbo al final:</b> —No me lo creo. (punto dentro)</p>'
         '<p style="margin-top:8px"><b>Con verbo al final:</b> —No me lo creo —respondió Ana.</p>'
         '<p style="margin-top:8px"><b>Pregunta:</b> —¿Estás seguro? —preguntó.</p>'
         '<p style="margin-top:8px"><b>Exclamación:</b> —¡Cuidado! —gritó.</p></div>'),
        ('Acotaciones escénicas', None,
         '<p class="slide-explanation">Las acotaciones describen los gestos, el tono o las acciones que acompañan las palabras de un personaje.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Sin acotación:</b> —No lo sé.</p>'
         '<p style="margin-top:8px"><b>Con acotación antes:</b> Ana suspiró profundamente antes de responder:</p>'
         '<p style="margin-top:8px"><b>Con acotación intercalada:</b> —No lo sé —confesó Ana, mirando al suelo—. Y eso me asusta.</p></div>'),
        ('Discurso directo vs. indirecto', None,
         '<p class="slide-explanation">El discurso directo reproduce las palabras exactas; el indirecto las parafrasea con cambios verbales.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Directo:</b> —Estoy cansado —dijo Pedro.</p>'
         '<p style="margin-top:8px"><b>Indirecto:</b> Pedro dijo que estaba cansado.</p>'
         '<p style="margin-top:8px"><b>Pregunta directa:</b> —¿Vienes? —preguntó Ana.</p>'
         '<p style="margin-top:8px"><b>Pregunta indirecta:</b> Ana preguntó si venía.</p></div>'),
    ],
    traps=[
        ('"Hola", dijo Ana.', '—Hola —dijo Ana.', 'En español el diálogo usa la raya (—), no las comillas dobles'),
        ('—Buenos días. —Dijo Ana. (punto y mayúscula en el verbo)', '—Buenos días —dijo Ana. (minúscula en el verbo)', 'Después de la raya de cierre el verbo de habla va en minúscula'),
        ('Dijo que viene mañana. (discurso indirecto)', 'Dijo que <strong>vendría</strong> mañana. (condicional)', 'En discurso indirecto el futuro se convierte en condicional'),
        ('—¿Estás bien?. —preguntó. (punto después de la interrogación)', '—¿Estás bien? —preguntó.', 'No se pone punto después de los signos de interrogación o exclamación'),
        ('Dijo, respondió, dijo, respondió... (repetición)', 'Varía: dijo, contestó, añadió, murmuró...', 'Evita repetir siempre el mismo verbo de habla; usa sinónimos'),
    ],
    summary=[
        ('Raya', '— + palabras del personaje', '—Buenos días.'),
        ('Con verbo de habla', '— palabras — dijo/respondió.', '—Hola —dijo Ana.'),
        ('Verbos variados', 'dijo/respondió/exclamó/murmuró', 'No repitas siempre «dijo».'),
        ('Acotación', 'descripción de gesto o tono', '—No lo sé —confesó, mirando al suelo.'),
        ('Discurso indirecto', 'dijo que + imperfecto/condicional', 'Dijo que estaba cansado.'),
        ('Pregunta indirecta', 'preguntó si / cuándo / qué...', 'Preguntó si vendría.'),
    ],
    items=[
        ('raya', 'raya', 'signo de puntuación (—) que introduce las intervenciones de los personajes en el diálogo español', 'guion largo',
         'En el diálogo español se usa la ______ (—) en lugar de las comillas.', 'ray', 'raya'),
        ('verbo-habla', 'verbo de habla', 'verbo que introduce o acompaña las palabras de un personaje en un diálogo', 'verbum dicendi',
         'Dijo, respondió y exclamó son ejemplos de ______ de habla.', 'verbo', 'verbo de habla'),
        ('acotacion', 'acotación', 'descripción breve de los gestos, el tono o las acciones que acompañan las palabras de un personaje', 'indicación escénica',
         'La ______ «mirando al suelo» enriquece el diálogo con información no verbal.', 'acot', 'acotación'),
        ('discurso-directo', 'discurso directo', 'reproducción literal de las palabras de una persona entre rayas o comillas', 'estilo directo',
         'El ______ reproduce exactamente lo que dijo el personaje, con sus propias palabras.', 'discurso dir', 'discurso directo'),
        ('discurso-indirecto', 'discurso indirecto', 'paráfrasis de las palabras de alguien con los cambios verbales y pronominales necesarios', 'estilo indirecto',
         'En el ______, «voy» se convierte en «iba» y «mañana» en «al día siguiente».', 'discurso ind', 'discurso indirecto'),
        ('exclamar', 'exclamar', 'verbo de habla que indica que el personaje dice algo con énfasis o sorpresa', 'gritar de sorpresa',
         '«¡No puede ser! — ______ Ana» indica que ella lo dice con sorpresa.', 'exclam', 'exclamó'),
        ('murmurar', 'murmurar', 'verbo de habla que indica que el personaje habla en voz baja, casi en secreto', 'susurrar',
         '«—Tengo miedo — ______ él» indica que lo dice muy bajo.', 'murm', 'murmuró'),
        ('pregunta-indirecta', 'pregunta indirecta', 'pregunta transmitida en discurso indirecto, que introduce «si», «qué», «cuándo», etc.', 'pregunta en discurso indirecto',
         '«¿Vienes?» se convierte en ______ : «Preguntó si vendría».', 'preg. ind', 'pregunta indirecta'),
    ],
    ex1=('Puntúa el diálogo', 'Elige la versión correctamente puntuada.', [
        ('¿Cuál es la forma correcta de introducir el diálogo en español?',
         ['—Buenos días —dijo Ana.', '"Buenos días", dijo Ana.', '«Buenos días», dijo Ana.'],
         '—Buenos días —dijo Ana.',
         'En español se usa la raya (—) para introducir el diálogo, no las comillas.'),
        ('¿Dónde va el punto en un diálogo sin verbo de habla?',
         ['—No lo sé. (dentro, antes de la raya de cierre)', '—No lo sé —. (fuera)', '—No lo sé — . (con espacio)'],
         '—No lo sé. (dentro, antes de la raya de cierre)',
         'Cuando no hay verbo de habla, el punto cierra el enunciado dentro.'),
        ('¿Cuál es el verbo de habla más adecuado para indicar que alguien habla muy bajo?',
         ['murmuró', 'gritó', 'dijo'], 'murmuró',
         'Murmurar indica que alguien habla en voz muy baja.'),
        ('Elige la transformación correcta al discurso indirecto: —Estoy cansado, dijo Pedro.',
         ['Pedro dijo que estaba cansado.', 'Pedro dijo que está cansado.', 'Pedro dijo «estoy cansado».'],
         'Pedro dijo que estaba cansado.',
         'En discurso indirecto el presente (estoy) se convierte en imperfecto (estaba).'),
        ('¿Qué es una acotación en un diálogo?',
         ['Una descripción del gesto o el tono del personaje', 'El verbo de habla', 'Las palabras del personaje'],
         'Una descripción del gesto o el tono del personaje',
         'Las acotaciones describen acciones, gestos o emociones que acompañan las palabras.'),
        ('¿Cuál es la forma correcta de una pregunta en discurso indirecto?',
         ['Preguntó si vendría al día siguiente.', 'Preguntó que si vendrías mañana.', 'Preguntó «¿vendrás mañana?»'],
         'Preguntó si vendría al día siguiente.',
         'Pregunta indirecta: preguntó si + condicional (vendría); mañana → al día siguiente.'),
    ]),
    ex2=('Transforma al discurso indirecto', 'Escribe la forma correcta.', [
        ('«Tengo hambre» → Pedro dijo que ______ hambre. (transforma al indirecto)', 'tenía',
         'En discurso indirecto el presente (tengo) → imperfecto (tenía).'),
        ('«¿Puedes venir?» → Ana preguntó si ______ venir. (transforma)', 'podía',
         'Pregunta indirecta: preguntó si + imperfecto: podía venir.'),
        ('«Mañana llegaré» → Dijo que ______ al día siguiente. (transforma)', 'llegaría',
         'En discurso indirecto el futuro (llegaré) → condicional (llegaría); mañana → al día siguiente.'),
        ('«¡Cuidado!» → ______ que tuviera cuidado. (transforma imperativo)', 'Dijo / Advirtió',
         'El imperativo en discurso indirecto → que + subjuntivo imperfecto: que tuviera cuidado.'),
        ('Escribe la raya para introducir el diálogo: ______ Buenas tardes. (solo la raya)', '—',
         'La raya larga (—) introduce cada intervención en el diálogo español.'),
    ]),
    ex3=('Discurso directo vs. indirecto', 'Elige la opción correcta.', [
        ('¿Cuál es el símbolo que introduce el diálogo en español?',
         ['La raya —', 'Las comillas ""', 'Los paréntesis ()'],
         'La raya —',
         'En español el diálogo se introduce con la raya (—), no con comillas dobles.'),
        ('«Vendré mañana» en discurso indirecto es:',
         ['Dijo que vendría al día siguiente.', 'Dijo que vendrá mañana.', 'Dijo «vendré mañana».'],
         'Dijo que vendría al día siguiente.',
         'Futuro → condicional; mañana → al día siguiente en discurso indirecto.'),
        ('¿Qué verbo usas para indicar que alguien habla con mucha fuerza y volumen?',
         ['gritó', 'murmuró', 'susurró'],
         'gritó',
         'Gritar indica un tono muy elevado; murmurar y susurrar indican lo contrario.'),
        ('¿Dónde se escribe el verbo de habla respecto a las palabras del personaje?',
         ['Después de las palabras, separado por raya', 'Antes de las palabras, sin raya', 'Entre comillas con el personaje'],
         'Después de las palabras, separado por raya',
         '—Buenas tardes —dijo Ana. El verbo va después de la raya de cierre.'),
        ('¿Qué son las acotaciones en un diálogo?',
         ['Descripciones de gestos o tonos que acompañan las palabras', 'Las preguntas del personaje', 'Los verbos de habla'],
         'Descripciones de gestos o tonos que acompañan las palabras',
         'Las acotaciones aportan información contextual: «—No lo sé —respondió, mirando al suelo.»'),
    ]),
)
