# espanol_b2_w.py — Main Spanish B2 Writing — 8 chapters

CHAPTERS = {}

CHAPTERS['ensayo-opinion'] = dict(
    level='b2', section='writing', num='W01', short='El Ensayo de Opinión',
    title='El Ensayo de Opinión',
    subtitle='Argumenta con claridad y coherencia tu posición sobre un tema',
    game_desc='Practica las estructuras del ensayo argumentativo en español.',
    slides=[
        ('Qué es un ensayo de opinión', None,
         '<p class="slide-explanation">Un ensayo de opinión expone y defiende una tesis con argumentos sólidos y ejemplos. Tiene una estructura clara: introducción, desarrollo y conclusión.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Tesis:</b> posición clara del autor</p>'
         '<p style="margin-top:6px"><b>Argumentos:</b> razones que apoyan la tesis</p>'
         '<p style="margin-top:6px"><b>Contraargumentos:</b> opiniones contrarias que se refutan</p>'
         '<p style="margin-top:6px"><b>Conclusión:</b> síntesis y reafirmación de la tesis</p></div>'),
        ('La introducción: gancho y tesis', None,
         '<p class="slide-explanation">La introducción presenta el tema y enuncia la tesis con claridad. Comienza con un «gancho» que capte la atención del lector.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Gancho:</b> dato sorprendente, pregunta retórica o cita</p>'
         '<p style="margin-top:8px"><b>Contextualización:</b> breve marco del tema</p>'
         '<p style="margin-top:8px"><b>Tesis:</b> «En este ensayo defenderé que...» / «Considero que...»</p></div>'),
        ('El desarrollo: argumentos y ejemplos', None,
         '<p class="slide-explanation">Cada párrafo del desarrollo presenta un argumento apoyado por ejemplos y datos. Los párrafos se conectan con marcadores discursivos.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Marcadores de adición:</b> además, asimismo, por otro lado, también</p>'
         '<p style="margin-top:8px"><b>Marcadores de contraste:</b> sin embargo, no obstante, a pesar de, aunque</p>'
         '<p style="margin-top:8px"><b>Marcadores de causa:</b> debido a, puesto que, dado que, ya que</p></div>'),
        ('La refutación y el contraargumento', None,
         '<p class="slide-explanation">Mencionar y refutar el punto de vista contrario hace el ensayo más sólido y muestra pensamiento crítico.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Introducir:</b> Aunque algunos sostienen que... / Si bien es cierto que...</p>'
         '<p style="margin-top:8px"><b>Refutar:</b> ...sin embargo, los datos muestran que... / ...esto no invalida el hecho de que...</p></div>'),
        ('La conclusión: síntesis y cierre', None,
         '<p class="slide-explanation">La conclusión retoma la tesis, resume los argumentos principales y cierra con una reflexión o llamada a la acción.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Marcadores de conclusión:</b> en conclusión, en definitiva, en suma, por todo lo expuesto</p>'
         '<p style="margin-top:8px"><b>Cierre:</b> «Por todo lo expuesto, queda claro que...» / «En definitiva, es necesario que...»</p></div>'),
    ],
    traps=[
        ('Yo pienso que el cambio climático es malo.', '<strong>Considero que</strong> el cambio climático representa una amenaza real.', 'Evita «yo pienso» en ensayos formales; usa «considero», «sostengo» o «defiendo»'),
        ('Por una parte... Por otra...', 'Por un lado... <strong>Por otro lado</strong>...', 'El par correcto es «por un lado / por otro lado», no «por una parte / por otra»'),
        ('En conclusión, como dije antes, el tema es importante.', '<strong>En definitiva</strong>, los argumentos expuestos demuestran que es urgente actuar.', 'La conclusión no repite literalmente lo dicho; sintetiza y proyecta hacia adelante'),
        ('Sin embargo pero hay excepciones.', '<strong>Sin embargo</strong>, existen excepciones relevantes.', 'No combines dos conectores de contraste en la misma frase'),
        ('Además, también hay otro punto.', '<strong>Asimismo</strong>, conviene destacar otro aspecto fundamental.', 'No acumules «además» y «también» en la misma idea; elige uno'),
    ],
    summary=[
        ('Introducción', 'gancho + contextualización + tesis', 'El aumento del tráfico aéreo plantea serios dilemas medioambientales...'),
        ('Argumento', 'idea principal + ejemplo/dato', 'Los aviones emiten un 2,5 % del CO₂ global, según la IATA.'),
        ('Contraargumento', 'aunque... / si bien...', 'Aunque el avión es contaminante, conecta regiones inaccesibles.'),
        ('Refutación', '...sin embargo / ...esto no invalida', 'Sin embargo, existen alternativas ferroviarias para distancias medias.'),
        ('Conclusión', 'en definitiva / en conclusión', 'En definitiva, es necesario gravar fiscalmente los vuelos de corta distancia.'),
        ('Tesis', 'posición clara del autor', 'Defiendo que se deben reducir los vuelos domésticos en Europa.'),
    ],
    items=[
        ('tesis', 'tesis', 'proposición central que el autor defiende a lo largo del ensayo', 'posición',
         'La ______ del ensayo debe quedar clara desde el primer párrafo.', 'tes', 'tesis'),
        ('argumento', 'argumento', 'razón o prueba que apoya la tesis del ensayo', 'razonamiento',
         'Cada ______ debe respaldarse con datos o ejemplos concretos.', 'argu', 'argumento'),
        ('contraargumento', 'contraargumento', 'opinión contraria a la tesis que se menciona para luego refutarla', 'objeción',
         'Incluir un ______ hace el ensayo más equilibrado y convincente.', 'contra', 'contraargumento'),
        ('refutación', 'refutación', 'respuesta que demuestra que el contraargumento no invalida la tesis', 'rebatimiento',
         'La ______ muestra por qué el argumento contrario no es definitivo.', 'refut', 'refutación'),
        ('marcador', 'marcador discursivo', 'palabra o expresión que organiza y conecta las ideas del texto', 'conector',
         '«Sin embargo» y «además» son ______ que estructuran el ensayo.', 'marc', 'marcador discursivo'),
        ('conclusion', 'conclusión', 'párrafo final que sintetiza los argumentos y reafirma la tesis', 'cierre',
         'La ______ no repite lo dicho, sino que lo sintetiza y proyecta.', 'conclu', 'conclusión'),
        ('coherencia', 'coherencia', 'cualidad de un texto en el que todas las ideas se relacionan de forma lógica', 'cohesión lógica',
         'Un ensayo con ______ presenta ideas ordenadas y bien conectadas.', 'coher', 'coherencia'),
        ('objetividad', 'objetividad', 'actitud de presentar los hechos sin dejarse llevar por emociones personales', 'imparcialidad',
         'La ______ en el ensayo se logra citando fuentes y datos verificables.', 'objet', 'objetividad'),
    ],
    ex1=('Estructuras del ensayo', 'Elige la opción correcta para cada elemento del ensayo de opinión.', [
        ('¿Cuál es la función de la tesis?', ['Presentar la posición del autor', 'Describir el tema sin opinar', 'Resumir los argumentos al final'], 'Presentar la posición del autor',
         'La tesis enuncia claramente la posición del autor al inicio del ensayo.'),
        ('¿Qué marcador es más apropiado para introducir un contraargumento?', ['Sin embargo', 'Si bien es cierto que', 'En conclusión'], 'Si bien es cierto que',
         '«Si bien es cierto que» introduce una idea concesiva antes de refutarla.'),
        ('¿Dónde se coloca la tesis en un ensayo?', ['Al final del ensayo', 'En la introducción', 'En cada párrafo del desarrollo'], 'En la introducción',
         'La tesis se presenta en la introducción para orientar al lector desde el principio.'),
        ('¿Cuál es la función de la refutación?', ['Apoyar el contraargumento', 'Mostrar que el contraargumento no invalida la tesis', 'Presentar un nuevo tema'], 'Mostrar que el contraargumento no invalida la tesis',
         'La refutación demuestra que la objeción contraria no refuta la tesis principal.'),
        ('¿Qué marcador introduce la conclusión?', ['Por otro lado', 'En definitiva', 'Dado que'], 'En definitiva',
         '«En definitiva» y «en conclusión» son marcadores de cierre propios de la conclusión.'),
    ]),
    ex2=('Completa con el marcador correcto', 'Escribe el marcador discursivo adecuado en cada caso.', [
        ('______ el tráfico aéreo genera empleo, también produce emisiones de CO₂.', 'Si bien', 'Si bien introduce una concesión antes de presentar el argumento principal.'),
        ('Los datos son contundentes; ______, no podemos ignorar el problema.', 'por tanto', 'Por tanto indica consecuencia lógica de los datos presentados.'),
        ('______, los gobiernos deben actuar con urgencia ante el cambio climático.', 'En definitiva', 'En definitiva cierra el ensayo sintetizando la posición del autor.'),
        ('Algunos defienden el libre mercado; ______, otros exigen más regulación.', 'sin embargo', 'Sin embargo introduce un contraste entre dos posturas opuestas.'),
    ]),
    ex3=('Reconoce los elementos', 'Identifica a qué parte del ensayo corresponde cada fragmento.', [
        ('«Aunque algunos sostienen que las energías renovables son caras, los datos demuestran que su coste ha caído un 70 % en diez años.»', ['Tesis', 'Contraargumento + refutación', 'Conclusión'], 'Contraargumento + refutación',
         'El fragmento introduce una objeción («aunque») y la refuta con datos.'),
        ('«En definitiva, la transición energética es inevitable y debe acelerarse.»', ['Introducción', 'Argumento', 'Conclusión'], 'Conclusión',
         '«En definitiva» es un marcador de cierre que caracteriza la conclusión.'),
        ('«El 80 % de las energías renovables instaladas en 2023 tienen costes menores que los combustibles fósiles.»', ['Ejemplo/dato que apoya el argumento', 'Tesis', 'Contraargumento'], 'Ejemplo/dato que apoya el argumento',
         'Un dato estadístico concreto sirve de evidencia para respaldar un argumento.'),
        ('«Defiendo que los subsidios a los combustibles fósiles deben eliminarse antes de 2030.»', ['Conclusión', 'Tesis', 'Contraargumento'], 'Tesis',
         '«Defiendo que» señala la posición central del autor: es la tesis.'),
        ('«Asimismo, la inversión en energías limpias crea más puestos de trabajo que los combustibles fósiles.»', ['Contraargumento', 'Argumento de desarrollo', 'Conclusión'], 'Argumento de desarrollo',
         '«Asimismo» añade un argumento adicional en el cuerpo del ensayo.'),
    ]),
)

CHAPTERS['analisis-texto'] = dict(
    level='b2', section='writing', num='W02', short='El Análisis de Texto',
    title='El Análisis de Texto',
    subtitle='Comenta e interpreta textos literarios y periodísticos con rigor',
    game_desc='Practica las técnicas del análisis textual en español.',
    slides=[
        ('Qué es el análisis de texto', None,
         '<p class="slide-explanation">Analizar un texto significa estudiar su contenido, su estructura y sus recursos lingüísticos. Un buen análisis va más allá del resumen e interpreta el significado.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Niveles de análisis:</b></p>'
         '<p style="margin-top:6px">1. <b>Tema:</b> ¿de qué trata el texto?</p>'
         '<p style="margin-top:6px">2. <b>Estructura:</b> ¿cómo se organiza?</p>'
         '<p style="margin-top:6px">3. <b>Recursos:</b> ¿qué recursos lingüísticos usa?</p>'
         '<p style="margin-top:6px">4. <b>Intención:</b> ¿qué quiere conseguir el autor?</p></div>'),
        ('El tema y la idea principal', None,
         '<p class="slide-explanation">El tema es el asunto central del texto. La idea principal es la afirmación más importante que el autor hace sobre ese tema.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Cómo identificar el tema:</b> pregunta «¿de qué habla este texto?»</p>'
         '<p style="margin-top:8px"><b>Cómo formular la idea principal:</b> responde «¿qué dice el autor sobre el tema?»</p>'
         '<p style="margin-top:8px"><b>Ejemplo:</b> Tema: el uso de las redes sociales. Idea principal: las redes sociales afectan negativamente la salud mental de los jóvenes.</p></div>'),
        ('La estructura del texto', None,
         '<p class="slide-explanation">Todo texto tiene una estructura. Identificarla ayuda a comprender cómo el autor organiza sus ideas.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Estructura deductiva:</b> idea principal al inicio → ejemplos y argumentos</p>'
         '<p style="margin-top:8px"><b>Estructura inductiva:</b> ejemplos → idea principal al final</p>'
         '<p style="margin-top:8px"><b>Estructura dialéctica:</b> tesis → antítesis → síntesis</p></div>'),
        ('Los recursos lingüísticos', None,
         '<p class="slide-explanation">Los recursos lingüísticos son las herramientas que el autor usa para dar fuerza, belleza o precisión a su texto.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Metáfora:</b> «la vida es un camino lleno de obstáculos»</p>'
         '<p style="margin-top:6px"><b>Comparación:</b> «el tiempo pasa como el agua»</p>'
         '<p style="margin-top:6px"><b>Ironía:</b> sentido contrario al literal</p>'
         '<p style="margin-top:6px"><b>Enumeración:</b> «paz, tranquilidad, silencio y naturaleza»</p></div>'),
        ('Cómo redactar el análisis', None,
         '<p class="slide-explanation">Un análisis de texto bien escrito presenta las ideas en orden lógico y cita el texto para apoyar cada afirmación.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Fórmulas útiles:</b></p>'
         '<p style="margin-top:6px">El texto trata sobre... / El autor sostiene que... / Como se aprecia en la línea N...</p>'
         '<p style="margin-top:6px">El recurso de la metáfora aparece cuando... / La estructura es deductiva porque...</p></div>'),
    ],
    traps=[
        ('El texto habla de la contaminación.', 'El texto <strong>aborda</strong> el problema de la contaminación atmosférica en las ciudades.', 'Usa verbos precisos: abordar, tratar, analizar, exponer; evita el vago «hablar de»'),
        ('El autor usa una metáfora muy bonita.', 'El autor emplea una metáfora para <strong>intensificar el efecto dramático</strong> de la imagen.', 'Describe el efecto del recurso, no solo su presencia o belleza'),
        ('En conclusión el texto es interesante.', 'En conclusión, el texto <strong>argumenta de manera persuasiva</strong> que la acción climática es urgente.', 'La conclusión del análisis interpreta el texto, no opina vagamente sobre él'),
        ('El significado literal es...', 'El <strong>sentido literal</strong> es..., pero el autor emplea la ironía para sugerir lo contrario.', 'Distingue siempre entre sentido literal y sentido connotado o irónico'),
        ('El autor quiere convencer al lector.', 'El autor <strong>apela a la emoción del lector</strong> mediante el uso de ejemplos personales.', 'Especifica qué estrategia usa el autor para conseguir su propósito'),
    ],
    summary=[
        ('Tema', '¿de qué trata el texto?', 'El texto trata sobre la desigualdad educativa.'),
        ('Idea principal', '¿qué dice el autor sobre el tema?', 'El autor sostiene que la brecha digital agrava la desigualdad.'),
        ('Estructura', 'deductiva / inductiva / dialéctica', 'La estructura es deductiva: la tesis aparece en el primer párrafo.'),
        ('Recursos', 'metáfora / comparación / ironía / enumeración', 'El autor usa la metáfora «el conocimiento es poder» para...'),
        ('Intención', '¿qué quiere conseguir el autor?', 'El autor pretende sensibilizar al lector sobre la urgencia del problema.'),
        ('Cita textual', 'como se aprecia en la línea N...', 'Como se aprecia en la línea 5: «la educación no es un privilegio».'),
    ],
    items=[
        ('tema', 'tema', 'asunto central sobre el que trata un texto', 'asunto',
         'El ______ del artículo es el impacto de las redes sociales en los adolescentes.', 'tem', 'tema'),
        ('idea-principal', 'idea principal', 'afirmación más importante que el autor hace sobre el tema del texto', 'tesis central',
         'La ______ resume en una oración el mensaje esencial del texto.', 'idea', 'idea principal'),
        ('estructura', 'estructura', 'manera en que un texto organiza y distribuye sus partes e ideas', 'organización',
         'La ______ del texto es deductiva: la tesis aparece en el primer párrafo.', 'estruct', 'estructura'),
        ('metafora', 'metáfora', 'figura retórica que identifica dos elementos sin usar «como» ni «cual»', 'imagen',
         'La ______ «la vida es un camino» compara la existencia con un viaje.', 'metáf', 'metáfora'),
        ('comparacion', 'comparación', 'figura que establece una semejanza entre dos elementos con «como» o «cual»', 'símil',
         'La ______ «corre como el viento» ilustra la rapidez del personaje.', 'compar', 'comparación'),
        ('ironia', 'ironía', 'recurso que expresa lo contrario de lo que dicen las palabras de manera deliberada', 'antífrasis',
         'La ______ se detecta cuando el significado real contradice el sentido literal.', 'iron', 'ironía'),
        ('intencion', 'intención del autor', 'propósito comunicativo que el escritor quiere alcanzar con su texto', 'propósito',
         'La ______ del autor es persuadir al lector de que el cambio climático es urgente.', 'intenc', 'intención del autor'),
        ('cita', 'cita textual', 'fragmento literal del texto que se reproduce entre comillas para apoyar un análisis', 'referencia directa',
         'Usa una ______ para respaldar tu interpretación: «como se aprecia en la línea 3».', 'cita', 'cita textual'),
    ],
    ex1=('Elementos del análisis', 'Elige la respuesta correcta para cada pregunta sobre análisis textual.', [
        ('¿Qué pregunta responde el tema de un texto?', ['¿Qué opina el lector?', '¿De qué trata el texto?', '¿Cómo termina el texto?'], '¿De qué trata el texto?',
         'El tema responde a la pregunta «¿de qué trata este texto?»'),
        ('¿Cuál es la diferencia entre metáfora y comparación?', ['La metáfora usa «como»', 'La comparación usa «como»; la metáfora, no', 'Son sinónimos exactos'], 'La comparación usa «como»; la metáfora, no',
         'La comparación establece la semejanza con «como»; la metáfora identifica directamente.'),
        ('¿Qué es una estructura inductiva?', ['La idea principal va al inicio', 'Los ejemplos preceden a la idea principal', 'El texto no tiene conclusión'], 'Los ejemplos preceden a la idea principal',
         'En la estructura inductiva, los casos concretos llevan al lector a la idea general.'),
        ('¿Cuál es la función de una cita textual en el análisis?', ['Sustituir el argumento propio', 'Apoyar la interpretación con evidencia del texto', 'Resumir el texto'], 'Apoyar la interpretación con evidencia del texto',
         'La cita textual proporciona evidencia directa para respaldar la interpretación.'),
        ('¿Qué verbo es más preciso para referirse al contenido de un texto?', ['Hablar de', 'Abordar', 'Decir'], 'Abordar',
         '«Abordar» es un verbo de registro formal y preciso para el análisis textual.'),
    ]),
    ex2=('Completa el análisis', 'Escribe la palabra o expresión adecuada para completar el análisis.', [
        ('El texto ______ el problema de la brecha digital en zonas rurales.', 'aborda', 'Abordar es el verbo de análisis textual más preciso y formal.'),
        ('La ______ del texto es deductiva: la tesis aparece en el primer párrafo.', 'estructura', 'La estructura del texto describe cómo se organizan sus partes.'),
        ('El autor emplea la ______ «la ciudad es una jungla» para destacar el caos urbano.', 'metáfora', 'La metáfora establece una identidad directa sin usar «como».'),
        ('Como se aprecia en la línea 4: «ningún niño debería quedarse sin educación». Esta ______ muestra la posición del autor.', 'cita textual', 'Una cita textual reproduce literalmente las palabras del texto.'),
    ]),
    ex3=('Identifica el recurso', 'Identifica qué recurso lingüístico se usa en cada ejemplo.', [
        ('«El tiempo vuela cuando estás feliz.»', ['Ironía', 'Metáfora', 'Enumeración'], 'Metáfora',
         '«El tiempo vuela» identifica directamente el tiempo con algo que vuela: es una metáfora.'),
        ('«Llegó cansado, hambriento, solo y desesperado.»', ['Comparación', 'Metáfora', 'Enumeración'], 'Enumeración',
         'La lista de cuatro adjetivos consecutivos forma una enumeración.'),
        ('«¡Qué magnífico servicio! Llevamos tres horas esperando.»', ['Metáfora', 'Ironía', 'Comparación'], 'Ironía',
         'El elogio «magnífico» contradice la situación negativa: es ironía.'),
        ('«Sus ojos brillan como estrellas.»', ['Metáfora', 'Ironía', 'Comparación'], 'Comparación',
         'La partícula «como» establece la semejanza: es una comparación o símil.'),
        ('«La tierra llora cuando la olvidamos.»', ['Enumeración', 'Ironía', 'Metáfora'], 'Metáfora',
         'Atribuir a la tierra la acción de llorar es una metáfora (personificación).'),
    ]),
)

CHAPTERS['carta-formal-b2'] = dict(
    level='b2', section='writing', num='W03', short='La Carta Formal B2',
    title='La Carta Formal B2 — Reclamaciones e Instancias',
    subtitle='Escribe cartas formales con argumentos sólidos y tono institucional',
    game_desc='Practica el registro y las fórmulas de la carta formal en español B2.',
    slides=[
        ('La carta formal vs el correo formal', None,
         '<p class="slide-explanation">A diferencia del correo electrónico, la carta formal tiene fecha, dirección y referencias en la cabecera. El tono es más elaborado y el vocabulario más culto.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Cabecera:</b> datos del remitente, fecha, destinatario, asunto/referencia</p>'
         '<p style="margin-top:6px"><b>Cuerpo:</b> introducción, exposición, petición</p>'
         '<p style="margin-top:6px"><b>Cierre:</b> fórmula de despedida + firma</p></div>'),
        ('La reclamación formal', None,
         '<p class="slide-explanation">Una reclamación expone un problema concreto y solicita una solución o compensación. Debe ser educada pero firme.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Exponer el problema:</b> Me veo en la necesidad de reclamar... / Es con pesar que me dirijo...</p>'
         '<p style="margin-top:8px"><b>Aportar datos:</b> el día X, número de pedido Y, referencia Z</p>'
         '<p style="margin-top:8px"><b>Solicitar:</b> Por lo expuesto, les ruego que... / Solicito que se proceda a...</p></div>'),
        ('La instancia o solicitud oficial', None,
         '<p class="slide-explanation">La instancia es una carta formal dirigida a una institución pública para solicitar algo: una beca, una plaza, un certificado.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Estructura fija:</b> EXPONE (hechos) → SOLICITA (petición)</p>'
         '<p style="margin-top:8px"><b>Ejemplo:</b> «Que, habiendo finalizado los estudios de grado, SOLICITA que se le expida el título correspondiente.»</p></div>'),
        ('Vocabulario jurídico-administrativo', None,
         '<p class="slide-explanation">Las cartas formales institucionales usan un vocabulario específico que debes conocer.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Verbos:</b> exponer, solicitar, requerir, adjuntar, certificar, acreditar</p>'
         '<p style="margin-top:8px"><b>Sustantivos:</b> instancia, resolución, expediente, recurso, plazo</p>'
         '<p style="margin-top:8px"><b>Fórmulas:</b> en virtud de / de conformidad con / a los efectos oportunos</p></div>'),
        ('El tono: firmeza educada', None,
         '<p class="slide-explanation">Una carta de reclamación debe mantener firmeza sin ser agresiva. La cortesía aumenta las posibilidades de éxito.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Incorrecto:</b> Exijo que me devuelvan el dinero inmediatamente.</p>'
         '<p style="margin-top:8px"><b>Correcto:</b> Les ruego que procedan a la devolución del importe en el plazo más breve posible.</p></div>'),
    ],
    traps=[
        ('Quiero reclamar que el producto no funciona.', '<strong>Me dirijo a ustedes para reclamar</strong> que el producto adquirido el día X presenta un defecto de fabricación.', 'La reclamación formal concreta el problema con fecha y detalle'),
        ('EXIJO que me devuelvan el dinero.', '<strong>Les ruego que procedan a la devolución</strong> del importe abonado.', 'En la carta formal se evita el imperativo exigente; se usa el subjuntivo de petición'),
        ('Le mando esta carta para pedir una beca.', 'Me dirijo a usted <strong>con el fin de solicitar</strong> la concesión de una beca de estudios.', 'El lenguaje formal usa «solicitar» y evita «pedir» y «mandar»'),
        ('Mando los documentos para que los vea.', '<strong>Adjunto la documentación requerida</strong> para su consideración.', '«Adjuntar» es el verbo formal para enviar documentos junto a una carta'),
        ('Espero su respuesta.', '<strong>En espera de su respuesta,</strong> aprovecho la ocasión para saludarle atentamente.', 'El cierre formal combina la expectativa de respuesta con la despedida protocolar'),
    ],
    summary=[
        ('Apertura reclamación', 'Me veo en la necesidad de...', 'Me veo en la necesidad de reclamar la factura incorrecta.'),
        ('Exponer datos', 'fecha, referencia, número de pedido', 'El día 3 de junio, pedido n.º 45678, por importe de 120 €.'),
        ('Petición', 'Les ruego que... / Solicito que...', 'Les ruego que procedan a la devolución del importe.'),
        ('Instancia', 'EXPONE... SOLICITA...', 'EXPONE que ha finalizado el grado. SOLICITA el título.'),
        ('Vocabulario clave', 'adjuntar, acreditar, expediente', 'Adjunto la documentación acreditativa de mis méritos.'),
        ('Cierre formal', 'En espera de su respuesta...', 'En espera de su resolución favorable, le saluda atentamente.'),
    ],
    items=[
        ('reclamacion', 'reclamación', 'carta formal en la que se expone un problema y se pide una solución o compensación', 'queja formal',
         'Presenté una ______ a la empresa por el retraso en la entrega del pedido.', 'reclam', 'reclamación'),
        ('instancia', 'instancia', 'documento formal dirigido a una institución para pedir algo de manera oficial', 'solicitud oficial',
         'Presenté una ______ al rectorado para solicitar la revisión de mi expediente.', 'instant', 'instancia'),
        ('adjuntar', 'adjuntar', 'enviar un documento junto a una carta o correo como material de apoyo', 'aportar',
         '______amos la factura original como prueba del pago realizado.', 'adjunt', 'adjuntar'),
        ('expediente', 'expediente', 'conjunto de documentos que registran la trayectoria académica o administrativa de una persona', 'historial',
         'Mi ______ académico recoge todas las asignaturas aprobadas durante el grado.', 'expedi', 'expediente'),
        ('resolución', 'resolución', 'decisión oficial dictada por una autoridad o institución en respuesta a una solicitud', 'decisión institucional',
         'Espero recibir una ______ favorable antes del plazo establecido.', 'resol', 'resolución'),
        ('plazo', 'plazo', 'período de tiempo establecido para realizar una acción o trámite', 'término',
         'El ______ para presentar la solicitud vence el 30 de junio.', 'plaz', 'plazo'),
        ('requerir', 'requerir', 'solicitar algo de manera formal y con carácter obligatorio o urgente', 'exigir formalmente',
         'La institución ______ la presentación de los documentos originales.', 'requer', 'requerir'),
        ('acreditar', 'acreditar', 'demostrar o certificar oficialmente que algo es cierto o que se cumple un requisito', 'certificar',
         'Debes ______ un nivel B2 de inglés para acceder al programa de intercambio.', 'acredit', 'acreditar'),
    ],
    ex1=('Vocabulario formal', 'Elige la expresión más adecuada en cada contexto de carta formal.', [
        ('¿Cómo se dice formalmente «quiero pedir una beca»?', ['Solicito la concesión de una beca', 'Quiero que me den una beca', 'Pido una beca'], 'Solicito la concesión de una beca',
         'En el registro formal se usa «solicitar» en lugar de «querer» o «pedir».'),
        ('¿Qué fórmula se usa para enviar documentos junto a una carta?', ['Mando los papeles', 'Adjunto la documentación requerida', 'Te envío los documentos'], 'Adjunto la documentación requerida',
         '«Adjunto» es el término formal y preciso para acompañar documentos.'),
        ('¿Cómo se pide una solución educadamente en una reclamación?', ['Exijo la devolución', 'Les ruego que procedan a la devolución', 'Devuélvanme el dinero'], 'Les ruego que procedan a la devolución',
         'El subjuntivo de petición («que procedan») mantiene el tono cortés pero firme.'),
        ('¿Qué documento contiene el historial académico de un estudiante?', ['La instancia', 'El expediente', 'La resolución'], 'El expediente',
         'El expediente académico registra todas las asignaturas, calificaciones y datos del estudiante.'),
        ('¿Qué es una resolución institucional?', ['Una reclamación del ciudadano', 'Una decisión oficial de la institución', 'Un plazo de entrega'], 'Una decisión oficial de la institución',
         'La resolución es la respuesta oficial y vinculante de una institución a una solicitud.'),
    ]),
    ex2=('Completa la carta', 'Elige la palabra correcta para completar cada fragmento de carta formal.', [
        ('______ la documentación acreditativa de mis méritos académicos.', 'Adjunto', 'Adjuntar es el verbo formal para enviar documentos junto a la carta.'),
        ('Les ruego que ______ a la devolución del importe en el plazo más breve posible.', 'procedan', 'El subjuntivo «procedan» expresa la petición de forma educada y formal.'),
        ('El ______ para presentar la solicitud de beca vence el 15 de julio.', 'plazo', 'Plazo designa el período oficial dentro del cual debe realizarse el trámite.'),
        ('En espera de su ______ favorable, le saluda atentamente.', 'resolución', 'Resolución es la decisión oficial que el solicitante espera recibir.'),
    ]),
    ex3=('Carta formal: registro correcto', 'Elige la versión con el registro más apropiado para una carta formal.', [
        ('Para pedir información sobre un proceso de selección:', ['¿Puedes decirme cómo funciona el proceso?', 'Me dirijo a usted para solicitar información sobre el proceso de selección.', 'Hola, quiero saber más sobre el proceso.'], 'Me dirijo a usted para solicitar información sobre el proceso de selección.',
         '«Me dirijo a usted para solicitar» es la apertura formal estándar.'),
        ('Para indicar que envías documentos:', ['Te mando los papeles.', 'Adjunto la documentación requerida para su consideración.', 'Aquí van los documentos.'], 'Adjunto la documentación requerida para su consideración.',
         '«Adjunto» + sustantivo formal es la fórmula adecuada en carta formal.'),
        ('Para cerrar una carta de reclamación:', ['Espero que me contestéis.', 'En espera de su resolución, aprovecho la ocasión para saludarle atentamente.', 'Hasta luego.'], 'En espera de su resolución, aprovecho la ocasión para saludarle atentamente.',
         'El cierre formal combina la expectativa de respuesta con la despedida protocolaria.'),
        ('Para exponer un problema:', ['Mi pedido llegó tarde y estoy muy enfadado.', 'Me veo en la necesidad de comunicarles que el pedido n.º 3421 llegó con siete días de retraso.', 'El pedido tardó mucho.'], 'Me veo en la necesidad de comunicarles que el pedido n.º 3421 llegó con siete días de retraso.',
         'La reclamación formal concreta el problema con número de referencia y datos exactos.'),
    ]),
)

CHAPTERS['articulo-opinion'] = dict(
    level='b2', section='writing', num='W04', short='El Artículo de Opinión',
    title='El Artículo de Opinión',
    subtitle='Escribe columnas y artículos para un periódico con voz propia',
    game_desc='Practica el género del artículo de opinión en español.',
    slides=[
        ('El artículo de opinión: características', None,
         '<p class="slide-explanation">El artículo de opinión aparece en periódicos y revistas. El autor da su punto de vista de manera razonada y busca influir en el lector, con un estilo más personal que el ensayo académico.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Características:</b> voz personal, actualidad, brevedad, ironía permitida</p>'
         '<p style="margin-top:8px"><b>Diferencia con el ensayo:</b> el artículo es más informal, más breve y más cercano al lector</p></div>'),
        ('El titular y la entrada', None,
         '<p class="slide-explanation">El titular debe captar la atención y resumir la posición del autor. La entrada (primer párrafo) desarrolla el titular y presenta el tema.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Titular:</b> breve, impactante, puede ser una pregunta o una paradoja</p>'
         '<p style="margin-top:8px"><b>Entrada:</b> contextualiza el tema y engancha al lector en 2-3 frases</p>'
         '<p style="margin-top:8px"><b>Ejemplo:</b> «El silencio también tiene derechos» (titular sobre contaminación acústica)</p></div>'),
        ('El cuerpo: argumentos y estilo', None,
         '<p class="slide-explanation">El cuerpo del artículo desarrolla la posición con 2-3 argumentos. El estilo puede ser más directo y hasta irónico que en el ensayo académico.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Argumentos:</b> datos, anécdotas, ejemplos cotidianos, comparaciones</p>'
         '<p style="margin-top:8px"><b>Estilo:</b> primera persona (yo, nosotros), pregunta retórica, ironía</p>'
         '<p style="margin-top:8px"><b>Ejemplo:</b> «¿Cuánto ruido más podemos soportar?»</p></div>'),
        ('La pregunta retórica y la ironía', None,
         '<p class="slide-explanation">Estos dos recursos son frecuentes en el artículo de opinión y le dan fuerza y vivacidad al texto.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Pregunta retórica:</b> pregunta sin respuesta esperada que invita a reflexionar</p>'
         '<p style="margin-top:8px"><b>Ironía:</b> elogiar algo negativo o criticar algo con tono de alabanza</p>'
         '<p style="margin-top:8px"><b>Ejemplo de ironía:</b> «Qué maravilloso es que los políticos se suban el sueldo en tiempos de crisis.»</p></div>'),
        ('El cierre: conclusión con gancho', None,
         '<p class="slide-explanation">El cierre de un artículo de opinión debe dejar huella. Puede terminar con una pregunta, una paradoja o una llamada a la acción.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Cierre con pregunta:</b> «¿Hasta cuándo vamos a tolerar este ruido?»</p>'
         '<p style="margin-top:8px"><b>Cierre con paradoja:</b> «Vivimos en la era de la comunicación y nunca hemos hablado menos.»</p>'
         '<p style="margin-top:8px"><b>Cierre con llamada:</b> «Es hora de que cada uno de nosotros tome partido.»</p></div>'),
    ],
    traps=[
        ('Voy a hablar de la contaminación acústica.', '<strong>El ruido nos está matando</strong> — y nadie parece importarle.', 'El artículo de opinión comienza con impacto; no anuncia su tema de forma plana'),
        ('Yo creo que el gobierno debería actuar.', 'El gobierno <strong>lleva años ignorando</strong> el problema del ruido urbano.', 'En el artículo de opinión se muestra la opinión con afirmaciones directas, no solo con «yo creo»'),
        ('¿Por qué el gobierno no hace nada? Porque no le importa.', '¿Por qué el gobierno no actúa? <strong>Esa es la pregunta que todos deberíamos hacernos.</strong>', 'La pregunta retórica no se responde directamente; invita a la reflexión del lector'),
        ('El titular: «Mi opinión sobre el ruido»', '«<strong>El silencio también tiene derechos</strong>»', 'El titular de un artículo de opinión debe ser impactante y sugerente, no descriptivo'),
        ('Además hay otro problema que es la falta de leyes.', '<strong>A esto se suma</strong> la ausencia de una legislación eficaz contra el ruido.', 'Varía los conectores de adición para dar ritmo y evitar la repetición de «además»'),
    ],
    summary=[
        ('Titular', 'breve, impactante, sugerente', '«El silencio también tiene derechos»'),
        ('Entrada', 'contextualizar + enganchar', 'Las ciudades modernas son cada vez más ruidosas...'),
        ('Argumento 1', 'dato o anécdota', 'Según la OMS, el ruido causa 12.000 muertes prematuras al año en Europa.'),
        ('Argumento 2', 'comparación o ejemplo cotidiano', 'Un bar con música alta supera los 90 dB: el límite seguro es 65 dB.'),
        ('Recurso', 'pregunta retórica / ironía', '¿Cuánto ruido más podemos soportar?'),
        ('Cierre', 'pregunta / paradoja / llamada', 'Es hora de que cada uno de nosotros tome partido.'),
    ],
    items=[
        ('editorial', 'artículo de opinión', 'texto periodístico en el que el autor defiende su punto de vista sobre un tema de actualidad', 'columna de opinión',
         'El ______ del domingo abordaba la crisis del sistema sanitario público.', 'artículo', 'artículo de opinión'),
        ('titular', 'titular', 'frase breve e impactante que encabeza un artículo y resume su posición o tema', 'encabezado',
         'Un buen ______ despierta la curiosidad del lector y anticipa la tesis del autor.', 'titul', 'titular'),
        ('pregunta-retorica', 'pregunta retórica', 'pregunta que no espera respuesta directa sino que invita al lector a reflexionar', 'interrogación retórica',
         'La ______ «¿Hasta cuándo seguiremos callados?» apela a la conciencia del lector.', 'pregunta', 'pregunta retórica'),
        ('ironia', 'ironía', 'recurso que elogia algo negativo o critica con tono de alabanza para denunciar una situación', 'antífrasis',
         'El autor usa la ______ al decir «qué maravillosa gestión» sobre el caos del aeropuerto.', 'iron', 'ironía'),
        ('voz-personal', 'voz personal', 'uso de la primera persona para expresar la posición y el estilo propios del columnista', 'primera persona',
         'La ______ del articulista se manifiesta en el uso de «considero» y «defiendo».', 'voz', 'voz personal'),
        ('actualidad', 'actualidad', 'vigencia o relevancia de un tema en el momento en que se escribe el artículo', 'vigencia',
         'Un artículo de opinión trata temas de ______ que interesan al lector de hoy.', 'actual', 'actualidad'),
        ('paradoja', 'paradoja', 'afirmación aparentemente contradictoria que encierra una verdad profunda', 'contradicción aparente',
         'La ______ «somos ricos en pobreza» critica la desigualdad con una imagen impactante.', 'parad', 'paradoja'),
        ('llamada-accion', 'llamada a la acción', 'cierre que invita al lector a hacer algo o a cambiar su actitud', 'apelación',
         'La ______ «es hora de que actuemos» cierra el artículo con energía movilizadora.', 'llamada', 'llamada a la acción'),
    ],
    ex1=('El artículo de opinión', 'Elige la respuesta correcta sobre este género periodístico.', [
        ('¿En qué se diferencia el artículo de opinión del ensayo académico?', ['Es más largo y formal', 'Es más personal, breve e informal', 'No tiene argumentos'], 'Es más personal, breve e informal',
         'El artículo de opinión permite un tono más personal e incluso irónico que el ensayo académico.'),
        ('¿Cuál es la función del titular?', ['Resumir todos los argumentos', 'Captar la atención y anticipar la posición del autor', 'Presentar los datos estadísticos'], 'Captar la atención y anticipar la posición del autor',
         'El titular debe ser impactante y sugerente, no solo descriptivo.'),
        ('¿Qué hace una pregunta retórica en un artículo?', ['Pide al lector que responda', 'Invita al lector a reflexionar', 'Introduce un contraargumento'], 'Invita al lector a reflexionar',
         'La pregunta retórica no espera respuesta literal; activa la reflexión del lector.'),
        ('¿Cuál es un buen cierre para un artículo de opinión?', ['«Este es el final del artículo.»', '«¿Hasta cuándo vamos a tolerar este ruido?»', '«En resumen, como ya dije antes...»'], '«¿Hasta cuándo vamos a tolerar este ruido?»',
         'Un cierre con pregunta retórica deja al lector con una reflexión activa.'),
        ('¿Qué estilo es habitual en el artículo de opinión pero no en el ensayo?', ['Citas de fuentes académicas', 'Ironía y pregunta retórica', 'Estructura deductiva'], 'Ironía y pregunta retórica',
         'La ironía y la pregunta retórica dan vivacidad al artículo de opinión y son infrecuentes en el ensayo académico.'),
    ]),
    ex2=('Completa el artículo', 'Escribe el recurso o la palabra que falta en cada fragmento.', [
        ('El ______ del artículo resume en pocas palabras la posición del autor sobre el tema.', 'titular', 'El titular encabeza el artículo y capta la atención del lector.'),
        ('«¿Cuántos más deben morir antes de que actuemos?» Es un ejemplo de ______.', 'pregunta retórica', 'La pregunta retórica no espera respuesta; apela a la conciencia del lector.'),
        ('El autor usa la ______ cuando dice «qué fantástico que los impuestos suban para pagar más deuda».', 'ironía', 'La ironía elogia algo negativo para criticarlo indirectamente.'),
        ('El artículo cierra con una ______: «es hora de que cada uno de nosotros tome partido».', 'llamada a la acción', 'La llamada a la acción invita al lector a cambiar su actitud o comportamiento.'),
    ]),
    ex3=('Reconoce el recurso', 'Identifica qué recurso se usa en cada fragmento del artículo.', [
        ('«¡Qué suerte tenemos de pagar tasas universitarias que suben cada año!»', ['Paradoja', 'Ironía', 'Pregunta retórica'], 'Ironía',
         'Elogiar algo negativo («qué suerte») para criticarlo es una ironía.'),
        ('«Vivimos en la era de la comunicación y nunca hemos hablado menos.»', ['Comparación', 'Ironía', 'Paradoja'], 'Paradoja',
         'La aparente contradicción entre comunicación y silencio es una paradoja.'),
        ('«¿De verdad creemos que podemos resolver el cambio climático sin cambiar nada?»', ['Ironía', 'Paradoja', 'Pregunta retórica'], 'Pregunta retórica',
         'La pregunta no espera una respuesta literal; es una pregunta retórica.'),
        ('«Somos ricos en recursos y pobres en voluntad política.»', ['Pregunta retórica', 'Paradoja', 'Ironía'], 'Paradoja',
         'La contradicción «ricos / pobres» sobre el mismo sujeto forma una paradoja.'),
    ]),
)

CHAPTERS['narracion-avanzada'] = dict(
    level='b2', section='writing', num='W05', short='La Narración Avanzada',
    title='La Narración Avanzada',
    subtitle='Escribe relatos con técnicas de punto de vista, flashback y suspense',
    game_desc='Practica las técnicas narrativas avanzadas en español.',
    slides=[
        ('El narrador y el punto de vista', None,
         '<p class="slide-explanation">El narrador es quien cuenta la historia. El punto de vista (perspectiva) determina cuánto sabe y qué puede contar.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Narrador omnisciente:</b> sabe todo sobre todos los personajes (3.ª persona)</p>'
         '<p style="margin-top:6px"><b>Narrador protagonista:</b> cuenta su propia historia (1.ª persona)</p>'
         '<p style="margin-top:6px"><b>Narrador testigo:</b> observa desde fuera, sabe poco (3.ª persona)</p></div>'),
        ('El flashback y el flash-forward', None,
         '<p class="slide-explanation">El flashback interrumpe la narración para volver al pasado. El flash-forward anticipa el futuro. Ambos añaden profundidad a la historia.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Flashback:</b> «De repente, recordó aquella tarde de verano de hace treinta años...»</p>'
         '<p style="margin-top:8px"><b>Flash-forward:</b> «Lo que no sabía entonces era que, cinco años después, todo cambiaría.»</p></div>'),
        ('El suspense y la tensión narrativa', None,
         '<p class="slide-explanation">El suspense mantiene al lector en vilo. Se crea con frases cortas, silencios, preguntas sin responder y detalles inquietantes.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Frases cortas:</b> Abrió la puerta. Silencio. Avanzó despacio.</p>'
         '<p style="margin-top:8px"><b>Detalle inquietante:</b> «Sobre la mesa había una taza de café todavía caliente. Nadie debería estar allí.»</p></div>'),
        ('La descripción de personajes y ambientes', None,
         '<p class="slide-explanation">En la narración avanzada, los personajes y los ambientes se describen con precisión sensorial y psicológica.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Descripción física:</b> rasgos concretos y significativos, no catálogo</p>'
         '<p style="margin-top:8px"><b>Descripción psicológica:</b> motivaciones, miedos, contradicciones del personaje</p>'
         '<p style="margin-top:8px"><b>Ambiente:</b> luz, sonido, olor para crear atmósfera</p></div>'),
        ('El diálogo en la narración', None,
         '<p class="slide-explanation">El diálogo hace avanzar la acción y revela el carácter de los personajes. En español se marca con raya (—), no con comillas dobles.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Reglas del diálogo:</b></p>'
         '<p style="margin-top:6px">— Texto del personaje —dijo el narrador con un acotación.</p>'
         '<p style="margin-top:6px"><b>Verbos:</b> dijo, respondió, susurró, exclamó, preguntó, añadió</p></div>'),
    ],
    traps=[
        ('El protagonista tenía pelo negro y ojos azules y era alto y delgado.', 'El protagonista era alto y de mirada intensa; su pelo oscuro caía sobre una frente pensativa.', 'Evita el catálogo de rasgos; selecciona los detalles que definen la personalidad'),
        ('De repente, todo cambió.', 'De repente, la puerta se abrió de golpe. El sonido resonó en el silencio.', '«De repente» pierde fuerza si no va seguido de un detalle concreto y sensorial'),
        ('"¿Qué haces aquí?" preguntó Ana.', '—¿Qué haces aquí? —preguntó Ana con voz temblorosa.', 'En narrativa española el diálogo usa raya (—) y las acotaciones van en minúscula tras la raya'),
        ('Recordó cuando era niño y jugaba en el jardín de su casa.', 'De repente, un olor a hierba húmeda lo transportó treinta años atrás, al jardín de su infancia.', 'El flashback es más efectivo si usa un detonante sensorial concreto, no solo «recordó que»'),
        ('El narrador omnisciente dijo lo que pensaban todos.', 'El narrador omnisciente <strong>conocía los pensamientos</strong> de todos los personajes y los revelaba con precisión.', 'El narrador omnisciente no «dice»; conoce, accede, revela'),
    ],
    summary=[
        ('Narrador omnisciente', '3.ª persona, todo lo sabe', 'El narrador conocía hasta el más íntimo pensamiento de Elena.'),
        ('Narrador protagonista', '1.ª persona, perspectiva limitada', 'Nunca entendí por qué ella decidió marcharse.'),
        ('Flashback', 'De repente, recordó...', 'De repente, el olor a café lo llevó veinte años atrás.'),
        ('Suspense', 'frases cortas + detalle inquietante', 'La puerta estaba abierta. Nadie debería haber entrado.'),
        ('Diálogo', '— Texto —acotación.', '—¿Dónde estuviste anoche? —preguntó en voz baja.'),
        ('Descripción sensorial', 'luz, sonido, olor, textura', 'El sótano olía a humedad y a algo que no supo identificar.'),
    ],
    items=[
        ('narrador', 'narrador', 'voz que cuenta la historia y organiza el relato desde una perspectiva determinada', 'voz narrativa',
         'El ______ omnisciente conoce los pensamientos de todos los personajes.', 'narr', 'narrador'),
        ('flashback', 'flashback', 'técnica narrativa que interrumpe el presente para volver al pasado', 'analepsis',
         'El ______ se introduce con «de repente, recordó...» o «años antes...»', 'flash', 'flashback'),
        ('suspense', 'suspense', 'tensión narrativa que mantiene al lector en incertidumbre sobre lo que va a ocurrir', 'tensión',
         'El ______ se crea con frases cortas y detalles inquietantes.', 'susp', 'suspense'),
        ('omnisciente', 'narrador omnisciente', 'narrador en tercera persona que conoce los pensamientos y sentimientos de todos los personajes', 'narrador total',
         'El ______ accede a la conciencia de todos los personajes de la historia.', 'omnisc', 'narrador omnisciente'),
        ('acotacion', 'acotación', 'frase del narrador que introduce o complementa las palabras de un personaje en el diálogo', 'indicación narrativa',
         'La ______ «dijo ella en voz baja» añade matiz emocional al diálogo.', 'acotac', 'acotación'),
        ('atm-sfera', 'atmósfera', 'ambiente emocional o sensorial de un relato creado mediante detalles descriptivos', 'ambiente',
         'La ______ del cuento de terror se crea con oscuridad, silencio y frío.', 'atmósf', 'atmósfera'),
        ('perspectiva', 'perspectiva narrativa', 'punto de vista adoptado por el narrador para contar los hechos', 'punto de vista',
         'La ______ del narrador protagonista es subjetiva y limitada a su experiencia.', 'perspect', 'perspectiva narrativa'),
        ('descripcion-sensorial', 'descripción sensorial', 'técnica que activa los cinco sentidos del lector mediante detalles de luz, sonido, olor, textura y sabor', 'imagen sensorial',
         'La ______ «olía a canela y a hogar» sitúa al lector en la escena de forma inmediata.', 'descrip', 'descripción sensorial'),
    ],
    ex1=('Técnicas narrativas', 'Elige la respuesta correcta sobre las técnicas de la narración avanzada.', [
        ('¿Qué es un flashback?', ['Una descripción del futuro', 'Una vuelta al pasado dentro de la narración', 'Un tipo de narrador'], 'Una vuelta al pasado dentro de la narración',
         'El flashback interrumpe el presente narrativo para mostrar un episodio del pasado.'),
        ('¿Cómo se marca el diálogo en español?', ['Con comillas dobles: "..."', 'Con comillas simples: \'...\'', 'Con raya: —...'], 'Con raya: —...',
         'En español el diálogo se introduce con una raya (—), no con comillas.'),
        ('¿Qué crea el suspense?', ['Párrafos largos y detallados', 'Frases cortas y detalles inquietantes', 'Un narrador omnisciente'], 'Frases cortas y detalles inquietantes',
         'El ritmo corto y los detalles perturbadores generan tensión e incertidumbre en el lector.'),
        ('¿Cuál es la característica del narrador omnisciente?', ['Solo cuenta lo que ve', 'Conoce los pensamientos de todos los personajes', 'Narra en primera persona'], 'Conoce los pensamientos de todos los personajes',
         'El narrador omnisciente tiene acceso total a la mente de todos los personajes.'),
        ('¿Cómo se introduce eficazmente un flashback?', ['«Ahora voy a contar lo que pasó antes.»', '«De repente, el olor a café lo llevó veinte años atrás.»', '«El narrador explicó el pasado.»'], '«De repente, el olor a café lo llevó veinte años atrás.»',
         'Un detonante sensorial concreto hace el flashback más vívido e inmediato.'),
    ]),
    ex2=('Completa el relato', 'Escribe el término o recurso que corresponde a cada fragmento.', [
        ('«La puerta estaba abierta. Silencio. Avanzó despacio.» Este fragmento crea ______.', 'suspense', 'Las frases cortas y la ausencia de explicación generan tensión narrativa.'),
        ('«El narrador conocía cada pensamiento de los personajes.» Es un narrador ______.', 'omnisciente', 'El narrador omnisciente tiene acceso total a la mente de todos los personajes.'),
        ('«—¿Dónde estuviste? —preguntó ella en voz baja.» La frase «preguntó ella en voz baja» es una ______.', 'acotación', 'La acotación complementa el diálogo con información sobre el tono o la actitud.'),
        ('«De repente, el olor a tierra húmeda lo trasladó a su infancia.» Es un ______.', 'flashback', 'El detonante sensorial introduce una vuelta al pasado: un flashback.'),
    ]),
    ex3=('Identifica la técnica', 'Identifica qué técnica narrativa se usa en cada fragmento.', [
        ('«Lo que ella no sabía entonces era que, cinco años después, su vida cambiaría para siempre.»', ['Flashback', 'Flash-forward', 'Suspense'], 'Flash-forward',
         'Anticipar el futuro desde el presente narrativo es un flash-forward.'),
        ('«Sus ojos brillaban con una intensidad que resultaba difícil de sostener. Había algo oscuro en ellos.»', ['Diálogo', 'Descripción psicológica', 'Flashback'], 'Descripción psicológica',
         'La descripción de rasgos que revelan el interior del personaje es descripción psicológica.'),
        ('«El sótano olía a humedad y a algo que ella prefirió no identificar. Cada paso resonaba.»', ['Flash-forward', 'Narrador omnisciente', 'Descripción sensorial + suspense'], 'Descripción sensorial + suspense',
         'Los detalles sensoriales (olor, sonido) crean atmósfera y tensión simultáneamente.'),
        ('«Recuerdo que aquel verano olía a jazmín y a libertad.»', ['Flash-forward', 'Flashback en primera persona', 'Suspense'], 'Flashback en primera persona',
         'El narrador protagonista vuelve al pasado: es un flashback narrado en primera persona.'),
    ]),
)

CHAPTERS['resumen-academico'] = dict(
    level='b2', section='writing', num='W06', short='El Resumen Académico',
    title='El Resumen Académico',
    subtitle='Sintetiza textos académicos con fidelidad, objetividad y precisión',
    game_desc='Practica las técnicas del resumen y la síntesis académica en español.',
    slides=[
        ('Qué es un resumen académico', None,
         '<p class="slide-explanation">Un resumen académico sintetiza las ideas principales de un texto con las propias palabras del estudiante, sin añadir opiniones ni interpretaciones.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Fidelidad:</b> no cambies el sentido del original</p>'
         '<p style="margin-top:6px"><b>Objetividad:</b> no añadas tu opinión</p>'
         '<p style="margin-top:6px"><b>Brevedad:</b> entre el 20-30 % de la extensión original</p>'
         '<p style="margin-top:6px"><b>Reformulación:</b> usa tus propias palabras, no copies literalmente</p></div>'),
        ('Cómo identificar las ideas principales', None,
         '<p class="slide-explanation">Para resumir bien, primero hay que distinguir las ideas principales de los ejemplos y los detalles secundarios.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Ideas principales:</b> afirmaciones generales que el autor defiende</p>'
         '<p style="margin-top:8px"><b>Ideas secundarias:</b> ejemplos, anécdotas, datos concretos</p>'
         '<p style="margin-top:8px"><b>Técnica:</b> subraya la oración temática de cada párrafo</p></div>'),
        ('Cómo reformular sin copiar', None,
         '<p class="slide-explanation">La reformulación (paráfrasis) consiste en expresar la misma idea con palabras distintas. Evita el plagio y demuestra comprensión real del texto.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Cambia:</b> sinónimos, estructura de la oración, voz activa/pasiva</p>'
         '<p style="margin-top:8px"><b>Original:</b> «Las energías renovables han reducido su coste un 70 %.»</p>'
         '<p style="margin-top:8px"><b>Reformulado:</b> «El precio de las energías limpias ha caído drásticamente en la última década.»</p></div>'),
        ('El lenguaje del resumen', None,
         '<p class="slide-explanation">El resumen usa el presente para referirse al texto y verbos de reporte para introducir las ideas del autor.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Verbos de reporte:</b> el autor sostiene / afirma / señala / argumenta / concluye</p>'
         '<p style="margin-top:8px"><b>Estructura:</b> El texto aborda... / El autor sostiene que... / En la segunda parte, se analiza...</p></div>'),
        ('Errores frecuentes en el resumen', None,
         '<p class="slide-explanation">Conocer los errores más comunes ayuda a evitarlos en tu propio resumen.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Copiar literalmente:</b> no reformulas → plagio</p>'
         '<p style="margin-top:6px"><b>Añadir opinión:</b> «yo creo que el autor tiene razón» → no es objetivo</p>'
         '<p style="margin-top:6px"><b>Incluir demasiados detalles:</b> los ejemplos no van en el resumen</p>'
         '<p style="margin-top:6px"><b>Cambiar el sentido:</b> sintetiza, no deformes la idea original</p></div>'),
    ],
    traps=[
        ('El texto dice que las energías renovables son baratas.', 'El autor <strong>sostiene que</strong> el coste de las energías renovables ha disminuido significativamente.', 'Usa un verbo de reporte preciso en lugar del vago «dice que»'),
        ('Yo creo que el autor tiene razón.', 'El autor <strong>concluye que</strong> la transición energética es necesaria e inevitable.', 'El resumen no incluye tu opinión; reformula la posición del autor'),
        ('El autor dice que hay muchos problemas, por ejemplo la contaminación y el tráfico.', 'El autor <strong>identifica diversos problemas medioambientales</strong> en las ciudades contemporáneas.', 'Los ejemplos no van en el resumen; generaliza la idea que ejemplifican'),
        ('«Las energías renovables han reducido su coste un 70 %» (copia literal)', 'El precio de las energías limpias <strong>ha caído drásticamente</strong> en la última década.', 'Reformula siempre con tus propias palabras para evitar el plagio'),
        ('El texto habla de muchas cosas interesantes.', 'El texto <strong>analiza</strong> las causas económicas y sociales del abandono rural.', 'Concreta el contenido del texto con precisión; evita afirmaciones vagas'),
    ],
    summary=[
        ('Función', 'sintetizar sin opinar', 'El resumen presenta las ideas del autor con objetividad.'),
        ('Verbo de reporte', 'el autor sostiene / afirma / concluye', 'El autor sostiene que la energía solar es ya más barata que el carbón.'),
        ('Reformulación', 'misma idea, palabras distintas', '«Los costes han bajado» → «el precio ha disminuido drásticamente»'),
        ('Sin ejemplos', 'generaliza los ejemplos', 'Los ejemplos del texto no se incluyen en el resumen.'),
        ('Sin opinión', 'objetividad total', 'No escribas «yo creo» ni «me parece» en un resumen académico.'),
        ('Extensión', '20-30 % del original', 'Un texto de 400 palabras → resumen de 80-120 palabras.'),
    ],
    items=[
        ('resumir', 'resumir', 'sintetizar las ideas principales de un texto con las propias palabras del autor del resumen', 'sintetizar',
         'Para ______ bien, identifica primero la idea principal de cada párrafo.', 'resum', 'resumir'),
        ('parafrasear', 'paráfrasis', 'reformulación de una idea con palabras distintas pero con el mismo significado', 'reformulación',
         'La ______ evita el plagio y demuestra que has comprendido el texto original.', 'parás', 'paráfrasis'),
        ('verbo-reporte', 'verbo de reporte', 'verbo que introduce las afirmaciones de otro autor: sostener, afirmar, señalar, concluir', 'verbo introductor',
         '«El autor ______ que la situación es grave» → usa sostiene o afirma.', 'verbo', 'verbo de reporte'),
        ('objetividad', 'objetividad', 'cualidad del resumen que excluye las opiniones personales del redactor', 'imparcialidad',
         'La ______ del resumen prohíbe escribir «yo creo» o «me parece».', 'objet', 'objetividad'),
        ('idea-principal', 'idea principal', 'afirmación central de un párrafo que resume su contenido esencial', 'oración temática',
         'La ______ suele aparecer al inicio o al final de cada párrafo.', 'idea', 'idea principal'),
        ('fidelidad', 'fidelidad', 'respeto al sentido y al contenido del texto original en el resumen', 'exactitud',
         'La ______ al texto exige no añadir ni cambiar el sentido de las ideas del autor.', 'fidel', 'fidelidad'),
        ('plagio', 'plagio', 'copia literal de fragmentos de un texto sin indicar que son palabras del autor original', 'copia',
         'Copiar frases enteras del texto sin reformularlas constituye un ______.', 'plagi', 'plagio'),
        ('sintetizar', 'síntesis', 'proceso de reducir varias ideas a su núcleo esencial manteniendo la coherencia', 'compendio',
         'Una buena ______ del texto ocupa entre el 20 y el 30 % de la extensión original.', 'sínt', 'síntesis'),
    ],
    ex1=('Técnicas del resumen', 'Elige la respuesta correcta sobre el resumen académico.', [
        ('¿Qué extensión debe tener un resumen académico?', ['El 80 % del original', 'Entre el 20 y el 30 % del original', 'Exactamente la mitad del original'], 'Entre el 20 y el 30 % del original',
         'Un resumen bien hecho tiene entre el 20 y el 30 % de la extensión del texto original.'),
        ('¿Qué se debe hacer con los ejemplos del texto original?', ['Incluirlos todos en el resumen', 'Generalizarlos en una idea amplia', 'Copiarlos literalmente'], 'Generalizarlos en una idea amplia',
         'Los ejemplos ilustran una idea; en el resumen, se expresa esa idea de forma general.'),
        ('¿Cuál es la función de los verbos de reporte?', ['Expresar la opinión del redactor', 'Introducir las ideas del autor del texto original', 'Conectar párrafos'], 'Introducir las ideas del autor del texto original',
         'Los verbos de reporte (sostiene, afirma, concluye) atribuyen correctamente las ideas al autor.'),
        ('¿Por qué hay que reformular el texto con las propias palabras?', ['Para cambiar el sentido del texto', 'Para evitar el plagio y demostrar comprensión', 'Para que el resumen sea más largo'], 'Para evitar el plagio y demostrar comprensión',
         'La paráfrasis demuestra que has comprendido realmente el texto.'),
        ('¿Se puede incluir la propia opinión en un resumen académico?', ['Sí, si es breve', 'No, el resumen es objetivo', 'Solo en la conclusión'], 'No, el resumen es objetivo',
         'El resumen académico presenta solo las ideas del autor original con total objetividad.'),
    ]),
    ex2=('Verbo de reporte correcto', 'Completa con el verbo de reporte más adecuado.', [
        ('El autor ______ que la pobreza energética afecta a más de 3 millones de hogares en España.', 'señala', 'Señalar es un verbo de reporte preciso para datos y cifras concretas.'),
        ('En la conclusión, el autor ______ que la transición energética es urgente e inevitable.', 'concluye', 'Concluir introduce la posición final del autor al término del texto.'),
        ('El texto ______ las principales causas de la desigualdad educativa en zonas rurales.', 'analiza', 'Analizar describe la operación intelectual que el texto realiza sobre su tema.'),
        ('El autor ______ que el coste de las energías renovables ha caído drásticamente.', 'afirma', 'Afirmar introduce una declaración directa y contundente del autor.'),
    ]),
    ex3=('Resumen correcto o incorrecto', 'Identifica si la práctica del resumen es correcta o incorrecta.', [
        ('Escribir en el resumen: «Yo creo que el autor tiene razón en sus argumentos.»', ['Correcto: es una síntesis objetiva', 'Incorrecto: añade opinión personal', 'Correcto: resume la posición del autor'], 'Incorrecto: añade opinión personal',
         'El resumen no incluye opiniones del redactor; solo las ideas del autor original.'),
        ('Escribir en el resumen: «El autor sostiene que las energías renovables son ya más baratas que el carbón.»', ['Correcto: usa verbo de reporte y reformula', 'Incorrecto: copia el texto', 'Incorrecto: añade un ejemplo'], 'Correcto: usa verbo de reporte y reformula',
         'El verbo de reporte y la reformulación hacen de este un resumen correcto.'),
        ('Incluir en el resumen todos los ejemplos que aparecen en el texto.', ['Correcto: los ejemplos son ideas principales', 'Incorrecto: los ejemplos son ideas secundarias', 'Correcto: enriquece el resumen'], 'Incorrecto: los ejemplos son ideas secundarias',
         'Los ejemplos ilustran las ideas principales pero no son la idea en sí; no van en el resumen.'),
        ('Copiar literalmente dos frases del texto sin comillas ni indicación de fuente.', ['Correcto si son frases cortas', 'Incorrecto: es plagio', 'Correcto: la reformulación es optativa'], 'Incorrecto: es plagio',
         'Copiar sin reformular ni indicar la fuente constituye plagio, aunque sean frases cortas.'),
    ]),
)

CHAPTERS['ensayo-comparativo'] = dict(
    level='b2', section='writing', num='W07', short='El Ensayo Comparativo',
    title='El Ensayo Comparativo',
    subtitle='Compara y contrasta dos posiciones, sistemas o fenómenos con rigor',
    game_desc='Practica la estructura del ensayo comparativo en español.',
    slides=[
        ('Qué es el ensayo comparativo', None,
         '<p class="slide-explanation">El ensayo comparativo analiza las semejanzas y diferencias entre dos temas, sistemas, posiciones o fenómenos, y llega a una conclusión valorativa.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Objetivo:</b> identificar qué tienen en común y en qué difieren dos elementos</p>'
         '<p style="margin-top:8px"><b>Resultado:</b> conclusión valorativa sobre cuál es mejor, más eficaz o más adecuado</p></div>'),
        ('Dos estructuras posibles', None,
         '<p class="slide-explanation">Hay dos formas principales de organizar el ensayo comparativo.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Estructura por bloques:</b> primero describes el elemento A completo, luego el elemento B completo</p>'
         '<p style="margin-top:8px"><b>Estructura punto por punto:</b> comparas A y B aspecto por aspecto</p>'
         '<p style="margin-top:8px"><b>Recomendación:</b> la estructura punto por punto facilita la comparación directa</p></div>'),
        ('Marcadores de comparación y contraste', None,
         '<p class="slide-explanation">Los marcadores de comparación y contraste son esenciales en este tipo de ensayo.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Semejanza:</b> de la misma manera, igualmente, asimismo, al igual que, tanto A como B</p>'
         '<p style="margin-top:8px"><b>Diferencia:</b> en cambio, por el contrario, mientras que, a diferencia de, sin embargo</p>'
         '<p style="margin-top:8px"><b>Conclusión valorativa:</b> en definitiva, pese a todo, en última instancia</p></div>'),
        ('Criterios de comparación', None,
         '<p class="slide-explanation">Para comparar dos elementos de forma rigurosa, debes elegir los mismos criterios para ambos.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Ejemplo:</b> comparar educación pública y privada por criterios de: coste, calidad, acceso, resultados</p>'
         '<p style="margin-top:8px"><b>Error:</b> comparar A según un criterio y B según otro diferente</p></div>'),
        ('La conclusión valorativa', None,
         '<p class="slide-explanation">La conclusión del ensayo comparativo no solo resume; toma una posición sobre cuál de los dos elementos es preferible o más adecuado.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Fórmulas:</b></p>'
         '<p style="margin-top:6px">En definitiva, aunque ambos modelos tienen ventajas, el modelo A resulta más eficaz porque...</p>'
         '<p style="margin-top:6px">Pese a las similitudes, el sistema B ofrece mayores garantías de equidad.</p></div>'),
    ],
    traps=[
        ('A es bueno. B también es bueno.', '<strong>Tanto A como B</strong> presentan ventajas, pero difieren en su accesibilidad y coste.', 'La comparación debe ser analítica, no una lista de elogios'),
        ('A tiene muchas cosas. B tiene muchas cosas diferentes.', 'A destaca por su eficiencia, <strong>mientras que</strong> B sobresale por su equidad.', 'Usa marcadores de contraste para articular las diferencias con precisión'),
        ('Por un lado, A. Por otro lado, B. Conclusión: ambos son válidos.', 'Pese a las similitudes, <strong>el modelo A resulta más adecuado</strong> para contextos urbanos por su red de transporte.', 'La conclusión del comparativo toma posición; no es válido concluir «ambos son buenos» sin valorar'),
        ('A es igual que B en todo.', 'A y B comparten el objetivo de reducir emisiones, pero <strong>difieren en el método y el coste</strong>.', 'Si los elementos fueran idénticos, no habría nada que comparar; distingue con precisión'),
        ('La comparación: «A es mejor que B.»', 'En definitiva, A resulta más eficaz que B <strong>en términos de coste y rapidez de implementación</strong>.', 'La valoración debe especificar en qué criterios y por qué, no ser una afirmación vaga'),
    ],
    summary=[
        ('Estructura bloques', 'A completo → B completo', 'Párrafos 1-2: educación pública. Párrafos 3-4: educación privada.'),
        ('Estructura punto por punto', 'aspecto 1: A vs B / aspecto 2: A vs B', 'Coste: pública vs privada. Calidad: pública vs privada.'),
        ('Semejanza', 'al igual que / igualmente / tanto A como B', 'Tanto la escuela pública como la privada buscan la excelencia académica.'),
        ('Diferencia', 'en cambio / mientras que / a diferencia de', 'La escuela pública es gratuita; en cambio, la privada tiene costes elevados.'),
        ('Criterios iguales', 'mismos parámetros para A y B', 'Compara ambos modelos por: coste, acceso, resultados, recursos.'),
        ('Conclusión valorativa', 'toma de posición razonada', 'En definitiva, el modelo público garantiza mayor equidad social.'),
    ],
    items=[
        ('comparacion', 'comparación', 'análisis de las semejanzas y diferencias entre dos o más elementos', 'cotejo',
         'La ______ entre los dos sistemas muestra ventajas e inconvenientes en cada uno.', 'compar', 'comparación'),
        ('criterio', 'criterio', 'parámetro o norma que se usa para analizar y juzgar un elemento', 'parámetro',
         'Compara los dos modelos usando los mismos ______ para ser objetivo.', 'criter', 'criterio'),
        ('contraste', 'contraste', 'diferencia significativa entre dos elementos que se comparan', 'diferencia',
         'El ______ entre los dos sistemas es más profundo en cuanto al coste y al acceso.', 'contrast', 'contraste'),
        ('semejanza', 'semejanza', 'característica común que comparten dos o más elementos comparados', 'similitud',
         'La ______ entre ambos modelos reside en su objetivo de reducir emisiones.', 'semej', 'semejanza'),
        ('punto-por-punto', 'estructura punto por punto', 'organización del ensayo comparativo en la que cada aspecto se analiza para los dos elementos simultáneamente', 'análisis por categorías',
         'La ______ compara coste, calidad y acceso de cada sistema en párrafos separados.', 'punto', 'estructura punto por punto'),
        ('bloque', 'estructura por bloques', 'organización del ensayo comparativo en la que se describe cada elemento completo antes de pasar al siguiente', 'presentación separada',
         'En la ______, primero describes el modelo A y luego el modelo B.', 'bloqu', 'estructura por bloques'),
        ('valoracion', 'valoración', 'juicio razonado que establece cuál de los elementos comparados es preferible o más adecuado', 'evaluación comparativa',
         'La ______ final del ensayo toma posición sobre qué modelo es más eficaz y por qué.', 'valor', 'valoración'),
        ('marcador-contraste', 'marcador de contraste', 'conector que señala una diferencia entre dos ideas o elementos: mientras que, en cambio, a diferencia de', 'conector adversativo',
         '«______ la energía solar es intermitente, la eólica puede generarse de noche.»', 'marcador', 'marcador de contraste'),
    ],
    ex1=('El ensayo comparativo', 'Elige la respuesta correcta sobre este tipo de texto.', [
        ('¿Qué hace el ensayo comparativo?', ['Describe un solo elemento con detalle', 'Analiza semejanzas y diferencias entre dos elementos', 'Narra una historia con dos personajes'], 'Analiza semejanzas y diferencias entre dos elementos',
         'El ensayo comparativo coteja dos elementos en función de los mismos criterios.'),
        ('¿Cuál es la ventaja de la estructura punto por punto?', ['Describe cada elemento de forma completa', 'Facilita la comparación directa aspecto por aspecto', 'Evita repetir los marcadores'], 'Facilita la comparación directa aspecto por aspecto',
         'La estructura punto por punto compara A y B en cada criterio, lo que hace la comparación más clara.'),
        ('¿Qué marcador expresa semejanza?', ['Sin embargo', 'Al igual que', 'A diferencia de'], 'Al igual que',
         '«Al igual que» establece una similitud entre los dos elementos comparados.'),
        ('¿Qué debe hacer la conclusión del ensayo comparativo?', ['Describir el segundo elemento', 'Tomar una posición valorativa razonada', 'Resumir todos los ejemplos'], 'Tomar una posición valorativa razonada',
         'La conclusión del comparativo evalúa cuál de los elementos es preferible y por qué.'),
        ('¿Qué error debes evitar en el ensayo comparativo?', ['Usar marcadores de contraste', 'Comparar A y B con criterios diferentes', 'Incluir una conclusión'], 'Comparar A y B con criterios diferentes',
         'Los mismos criterios deben aplicarse a ambos elementos para que la comparación sea justa.'),
    ]),
    ex2=('Marcadores de comparación', 'Escribe el marcador de comparación o contraste adecuado.', [
        ('La educación pública es gratuita; ______, la privada tiene tasas elevadas.', 'en cambio', 'En cambio introduce un contraste directo entre dos ideas opuestas.'),
        ('______ la escuela pública, la privada también busca la excelencia académica.', 'Al igual que', 'Al igual que establece una semejanza entre dos elementos.'),
        ('______ el modelo finlandés destaca por su equidad, el modelo anglosajón prioriza la competitividad.', 'Mientras que', 'Mientras que introduce un contraste simultáneo entre dos ideas.'),
        ('En definitiva, ______ sus diferencias, ambos modelos persiguen el mismo objetivo.', 'pese a', 'Pese a introduce una concesión antes de la conclusión valorativa.'),
    ]),
    ex3=('Semejanza o diferencia', 'Identifica si el fragmento expresa semejanza o diferencia entre los elementos.', [
        ('«Tanto el modelo A como el modelo B buscan reducir la huella de carbono.»', ['Diferencia', 'Semejanza', 'Conclusión valorativa'], 'Semejanza',
         '«Tanto A como B» establece que los dos elementos comparten una característica.'),
        ('«El modelo A es más económico; a diferencia de él, el modelo B requiere mayor inversión inicial.»', ['Semejanza', 'Conclusión valorativa', 'Diferencia'], 'Diferencia',
         '«A diferencia de» introduce explícitamente una diferencia entre los dos modelos.'),
        ('«En definitiva, aunque ambos son válidos, el modelo A resulta más eficaz para contextos urbanos.»', ['Diferencia', 'Semejanza', 'Conclusión valorativa'], 'Conclusión valorativa',
         '«En definitiva» + valoración razonada es la conclusión del ensayo comparativo.'),
        ('«Igualmente, los dos sistemas apuestan por las energías limpias como eje de la transición.»', ['Diferencia', 'Semejanza', 'Conclusión valorativa'], 'Semejanza',
         '«Igualmente» señala que los dos sistemas coinciden en un punto.'),
    ]),
)

CHAPTERS['informe'] = dict(
    level='b2', section='writing', num='W08', short='El Informe',
    title='El Informe — Exponer datos y proponer soluciones',
    subtitle='Escribe informes formales con datos, análisis y recomendaciones',
    game_desc='Practica la estructura y el lenguaje del informe formal en español.',
    slides=[
        ('Qué es un informe', None,
         '<p class="slide-explanation">Un informe es un documento formal que presenta datos sobre una situación, los analiza y propone conclusiones o recomendaciones. Es objetivo, organizado y preciso.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Tipos:</b> informe de situación, informe de investigación, informe de evaluación, informe de progreso</p>'
         '<p style="margin-top:8px"><b>Características:</b> objetividad, estructura clara, lenguaje impersonal o formal</p></div>'),
        ('Estructura del informe', None,
         '<p class="slide-explanation">Un informe tiene partes bien definidas que facilitan la lectura y el análisis de la información.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>1. Título e introducción:</b> contexto y objetivo del informe</p>'
         '<p style="margin-top:6px"><b>2. Metodología:</b> cómo se recogieron los datos</p>'
         '<p style="margin-top:6px"><b>3. Resultados:</b> datos y hechos organizados</p>'
         '<p style="margin-top:6px"><b>4. Análisis / discusión:</b> interpretación de los datos</p>'
         '<p style="margin-top:6px"><b>5. Conclusiones y recomendaciones:</b> qué se propone hacer</p></div>'),
        ('El lenguaje del informe', None,
         '<p class="slide-explanation">El informe usa un lenguaje impersonal, preciso y objetivo. Se prefiere la voz pasiva o las construcciones impersonales.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Impersonal:</b> se observa que... / se constata que... / los datos muestran que...</p>'
         '<p style="margin-top:8px"><b>Voz pasiva:</b> los resultados fueron recogidos mediante encuestas</p>'
         '<p style="margin-top:8px"><b>Verbos clave:</b> constatar, observar, registrar, analizar, concluir, recomendar</p></div>'),
        ('Las recomendaciones', None,
         '<p class="slide-explanation">La sección de recomendaciones es el punto más valorado del informe. Propone acciones concretas basadas en el análisis.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Fórmulas:</b> se recomienda que... / se propone implementar... / sería conveniente que...</p>'
         '<p style="margin-top:8px"><b>Ejemplo:</b> Se recomienda ampliar el horario del servicio de atención al cliente en un 30 %.»</p></div>'),
        ('El uso de datos y gráficos', None,
         '<p class="slide-explanation">Los datos son el núcleo del informe. Deben presentarse con claridad y referenciarse correctamente.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Presentar datos:</b> según los datos recogidos... / los resultados indican que... / el X % de los encuestados...</p>'
         '<p style="margin-top:8px"><b>Comentar un gráfico:</b> como se observa en el gráfico 1... / el gráfico muestra un aumento del X %...</p></div>'),
    ],
    traps=[
        ('Yo creo que el problema es grave.', '<strong>Los datos indican que</strong> la situación es crítica en el 60 % de los casos.', 'El informe usa lenguaje impersonal; evita la primera persona y los juicios sin datos'),
        ('Hay muchos problemas.', 'Se han detectado <strong>tres problemas principales</strong>: falta de personal, demoras en la entrega y fallos en el sistema.', 'El informe nombra y enumera los problemas con precisión; no los describe vagamente'),
        ('Deberían hacer algo.', 'Se recomienda <strong>implementar un protocolo de atención al cliente</strong> en un plazo de tres meses.', 'Las recomendaciones son concretas, con acción específica y, si es posible, plazo'),
        ('El 50 % de los clientes están contentos.', 'El <strong>52 % de los encuestados</strong> califica el servicio de satisfactorio o muy satisfactorio.', 'Los datos exactos y la fuente dan credibilidad; evita redondear de forma imprecisa'),
        ('En conclusión, el servicio es malo.', 'En conclusión, se constata que <strong>el tiempo de respuesta supera en un 40 % el objetivo establecido</strong>.', 'La conclusión del informe se basa en los datos analizados, no en una impresión general'),
    ],
    summary=[
        ('Introducción', 'contexto + objetivo', 'Este informe analiza la satisfacción de los clientes en el primer trimestre de 2026.'),
        ('Metodología', 'cómo se recogieron los datos', 'Los datos fueron recogidos mediante 300 encuestas telefónicas.'),
        ('Resultados', 'datos y hechos concretos', 'El 52 % de los encuestados califica el servicio de satisfactorio.'),
        ('Análisis', 'interpretación de los datos', 'Se observa que las quejas aumentan un 30 % en horario de tarde.'),
        ('Recomendaciones', 'se recomienda que...', 'Se recomienda ampliar el horario de atención en un 20 %.'),
        ('Lenguaje impersonal', 'se constata / los datos muestran', 'Se constata que el tiempo de espera supera el objetivo.'),
    ],
    items=[
        ('informe', 'informe', 'documento formal que presenta y analiza datos sobre una situación y propone recomendaciones', 'reporte',
         'El ______ de satisfacción recoge los resultados de las encuestas del primer trimestre.', 'inform', 'informe'),
        ('objetivo', 'objetivo del informe', 'propósito o finalidad que guía la recogida y el análisis de los datos', 'finalidad',
         'El ______ del informe es identificar las causas del descenso en la satisfacción del cliente.', 'objet', 'objetivo del informe'),
        ('metodologia', 'metodología', 'explicación de cómo se recogieron y trataron los datos del informe', 'método',
         'La ______ describe si los datos proceden de encuestas, observaciones o documentos oficiales.', 'metodol', 'metodología'),
        ('constatar', 'constatar', 'comprobar y hacer constar un hecho de manera objetiva en un informe', 'verificar',
         'Se ______ que el tiempo de respuesta ha aumentado un 40 % respecto al trimestre anterior.', 'const', 'constatar'),
        ('recomendar', 'recomendación', 'propuesta de acción concreta basada en el análisis de los datos del informe', 'propuesta',
         'La ______ principal es ampliar el equipo de atención al cliente en horario de tarde.', 'recom', 'recomendación'),
        ('impersonal', 'lenguaje impersonal', 'estilo del informe que evita la primera persona y usa construcciones con «se» o pasiva', 'registro objetivo',
         'El ______ del informe usa «se observa que» en lugar de «yo observo que».', 'impers', 'lenguaje impersonal'),
        ('encuesta', 'encuesta', 'instrumento de recogida de datos que consiste en preguntas formuladas a una muestra de personas', 'cuestionario',
         'Los datos proceden de una ______ realizada a 500 clientes entre enero y marzo.', 'encuest', 'encuesta'),
        ('muestra', 'muestra', 'grupo representativo de personas o elementos seleccionados para el estudio', 'grupo de análisis',
         'La ______ del estudio incluye 300 clientes de diferentes perfiles y regiones.', 'muestr', 'muestra'),
    ],
    ex1=('El informe formal', 'Elige la respuesta correcta sobre el informe como género textual.', [
        ('¿Qué caracteriza el lenguaje de un informe?', ['Primera persona y tono personal', 'Lenguaje impersonal y objetivo', 'Ironía y pregunta retórica'], 'Lenguaje impersonal y objetivo',
         'El informe usa construcciones impersonales como «se observa» o «los datos indican».'),
        ('¿Qué sección del informe propone acciones concretas?', ['La metodología', 'Los resultados', 'Las recomendaciones'], 'Las recomendaciones',
         'Las recomendaciones son la sección donde se proponen acciones basadas en el análisis.'),
        ('¿Cuál es la función de la metodología?', ['Proponer soluciones', 'Explicar cómo se recogieron los datos', 'Resumir el informe'], 'Explicar cómo se recogieron los datos',
         'La metodología describe el proceso de recogida y tratamiento de los datos.'),
        ('¿Cómo se formula una recomendación en un informe?', ['«Hay que hacerlo mejor.»', '«Se recomienda implementar un protocolo en tres meses.»', '«Yo creo que deberían actuar.»'], '«Se recomienda implementar un protocolo en tres meses.»',
         'La recomendación es concreta, usa «se recomienda» y especifica una acción y un plazo.'),
        ('¿Qué tipo de lenguaje debe evitarse en un informe?', ['Voz pasiva', 'Datos estadísticos', 'Primera persona y juicios sin datos'], 'Primera persona y juicios sin datos',
         'El informe exige objetividad; la primera persona y los juicios sin evidencia son incorrectos.'),
    ]),
    ex2=('Lenguaje del informe', 'Completa con la expresión impersonal adecuada.', [
        ('______ que el tiempo de respuesta ha aumentado un 40 % respecto al trimestre anterior.', 'Se constata', 'Se constata introduce un hecho verificado de forma objetiva e impersonal.'),
        ('______ implementar un sistema de turnos para reducir el tiempo de espera.', 'Se recomienda', 'Se recomienda introduce una propuesta de acción concreta en lenguaje impersonal.'),
        ('______ recogidos mediante encuestas telefónicas a 300 clientes.', 'Los datos fueron', 'La voz pasiva «fueron recogidos» es apropiada en el lenguaje formal del informe.'),
        ('______ en el gráfico 1 que las quejas aumentan en horario de tarde.', 'Como se observa', 'Como se observa introduce la referencia a una tabla o gráfico de forma impersonal.'),
    ]),
    ex3=('Estructura del informe', 'Identifica a qué sección del informe pertenece cada fragmento.', [
        ('«Los datos fueron recogidos mediante 300 encuestas telefónicas realizadas en enero de 2026.»', ['Resultados', 'Metodología', 'Recomendaciones'], 'Metodología',
         'Describir el método de recogida de datos corresponde a la sección de metodología.'),
        ('«El 52 % de los encuestados califica el servicio de satisfactorio o muy satisfactorio.»', ['Análisis', 'Recomendaciones', 'Resultados'], 'Resultados',
         'Los datos concretos extraídos de la encuesta forman parte de la sección de resultados.'),
        ('«Se recomienda ampliar el horario de atención al cliente en un 20 % a partir del segundo trimestre.»', ['Resultados', 'Metodología', 'Recomendaciones'], 'Recomendaciones',
         '«Se recomienda» con una acción concreta corresponde a la sección de recomendaciones.'),
        ('«Se observa que las quejas se concentran en el tramo horario de 14:00 a 16:00 h.»', ['Recomendaciones', 'Metodología', 'Análisis / discusión'], 'Análisis / discusión',
         'Interpretar los datos y observar patrones es propio de la sección de análisis.'),
    ]),
)
