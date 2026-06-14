# espanol_c1_w.py — Main Spanish C1 Writing — 6 chapters

CHAPTERS = {}

CHAPTERS['ensayo-argumentativo'] = dict(
    level='c1', section='writing', num='W01', short='El Ensayo Argumentativo',
    title='El Ensayo Argumentativo C1',
    subtitle='Construye argumentos sofisticados con matices, concesiones y refutaciones',
    game_desc='Practica las estrategias del ensayo argumentativo avanzado.',
    slides=[
        ('La argumentación sofisticada', None,
         '<p class="slide-explanation">En C1, el ensayo argumentativo va más allá de exponer pros y contras. Emplea concesiones estratégicas, refutaciones matizadas y lenguaje modal para calibrar la certeza.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Certeza:</b> es indudable que / está demostrado que</p>'
         '<p style="margin-top:6px"><b>Probabilidad:</b> es probable que / cabe la posibilidad de que</p>'
         '<p style="margin-top:6px"><b>Duda:</b> es discutible si / no está claro que</p></div>'),
        ('La concesión estratégica', None,
         '<p class="slide-explanation">Una concesión bien colocada fortalece la tesis porque muestra que el autor conoce las objeciones y puede responderlas.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Patrón:</b> Concesión → Pivote → Refutación</p>'
         '<p style="margin-top:8px"><b>Ejemplo:</b> «Cierto es que la inteligencia artificial crea empleo en algunos sectores; sin embargo, los datos muestran que destruye más puestos de los que genera.»</p></div>'),
        ('El lenguaje modal y la modalización', None,
         '<p class="slide-explanation">La modalización permite al autor matizar sus afirmaciones y evitar el absolutismo que debilita el argumento.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Verbos modales:</b> poder, deber, tener que, convenir, resultar conveniente</p>'
         '<p style="margin-top:8px"><b>Adverbios:</b> aparentemente, presumiblemente, en principio, a todas luces</p>'
         '<p style="margin-top:8px"><b>Subjuntivo de duda:</b> no es seguro que / es posible que / dudo de que</p></div>'),
        ('La polifonía argumentativa', None,
         '<p class="slide-explanation">Citar voces externas (fuentes, expertos, estadísticas) enriquece el argumento y aumenta la credibilidad del ensayo.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Cita de autoridad:</b> según el informe del FMI... / como señala Chomsky...</p>'
         '<p style="margin-top:8px"><b>Dato estadístico:</b> el 73 % de los economistas... / según los datos de la OCDE...</p>'
         '<p style="margin-top:8px"><b>Cita textual integrada:</b> el autor afirma que «la desigualdad es la principal amenaza del siglo XXI»</p></div>'),
        ('El cierre: síntesis y proyección', None,
         '<p class="slide-explanation">La conclusión del ensayo C1 no solo sintetiza; proyecta las implicaciones de la tesis hacia el futuro o hacia el debate más amplio.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Síntesis:</b> «Los argumentos expuestos demuestran que...»</p>'
         '<p style="margin-top:8px"><b>Proyección:</b> «Si no actuamos ahora, las consecuencias serán...»</p>'
         '<p style="margin-top:8px"><b>Llamada al debate:</b> «Queda pendiente la cuestión de si...»</p></div>'),
    ],
    traps=[
        ('Algunos dicen que A es bueno pero otros dicen que no.', 'Si bien algunos defienden que A ofrece ventajas, <strong>los datos empíricos cuestionan</strong> esa posición.', 'Evita la falsa simetría; toma posición con respaldo empírico'),
        ('Es obvio que tengo razón.', 'Los datos disponibles <strong>sugieren con firmeza</strong> que esta posición es la más sólida.', 'El absolutismo debilita; modaliza con precisión'),
        ('En conclusión, es un tema muy complejo.', 'En definitiva, <strong>la complejidad del fenómeno exige</strong> políticas matizadas que combinen incentivos y regulación.', 'La conclusión C1 no evade con «es complejo»; propone'),
        ('Según un estudio, el 50 % están de acuerdo.', 'Según el informe de la OCDE (2024), <strong>el 52 % de los ciudadanos</strong> apoya medidas de control.', 'Cita la fuente con precisión: institución, año y cifra exacta'),
        ('Aunque hay problemas, la solución es fácil.', 'Si bien persisten obstáculos estructurales, <strong>una regulación progresiva podría mitigar</strong> los efectos más dañinos.', 'Las soluciones en C1 son matizadas, no «fáciles»'),
    ],
    summary=[
        ('Concesión', 'cierto es que... / si bien...', 'Cierto es que la IA crea empleo; sin embargo, destruye más del que genera.'),
        ('Modalización', 'es probable que / cabe la posibilidad de', 'Es probable que la regulación reduzca los efectos negativos.'),
        ('Cita de autoridad', 'según el informe de X... / como señala Y...', 'Según el FMI (2024), la desigualdad ha aumentado un 15 %.'),
        ('Refutación matizada', 'los datos cuestionan / la evidencia contradice', 'Los datos empíricos cuestionan la tesis de que el mercado se autorregula.'),
        ('Proyección', 'si no actuamos / las implicaciones son', 'Si no se actúa, las consecuencias serán irreversibles en una década.'),
        ('Síntesis', 'los argumentos expuestos demuestran', 'Los argumentos expuestos demuestran que la regulación es necesaria.'),
    ],
    items=[
        ('concesion', 'concesión estratégica', 'reconocimiento del argumento contrario que se realiza para luego refutarlo con más fuerza', 'admisión táctica',
         'La ______ «si bien hay ventajas...» fortalece la tesis al anticipar la objeción.', 'conces', 'concesión estratégica'),
        ('modalizacion', 'modalización', 'uso de recursos lingüísticos para calibrar la certeza o probabilidad de una afirmación', 'matización',
         'La ______ con «es probable que» evita el absolutismo que debilita el argumento.', 'modal', 'modalización'),
        ('polifonia', 'polifonía argumentativa', 'incorporación de voces externas (fuentes, citas, estadísticas) que enriquecen el argumento', 'apelación a fuentes',
         'La ______ incluye citas de expertos y datos estadísticos para dar credibilidad.', 'polifo', 'polifonía argumentativa'),
        ('refutacion', 'refutación matizada', 'respuesta al contraargumento que reconoce su validez parcial antes de rebatirlo', 'contraargumentación',
         'Una ______ señala los límites del argumento contrario sin descartarlo por completo.', 'refut', 'refutación matizada'),
        ('proyeccion', 'proyección argumentativa', 'extensión de la conclusión hacia las implicaciones futuras o sociales de la tesis', 'apertura prospectiva',
         'La ______ cierra el ensayo señalando qué ocurrirá si no se actúa.', 'proyec', 'proyección argumentativa'),
        ('cita-autoridad', 'cita de autoridad', 'referencia a una fuente experta o institución reconocida para respaldar un argumento', 'argumento de autoridad',
         'La ______ «según el informe del FMI» da credibilidad a la afirmación.', 'cita', 'cita de autoridad'),
        ('falsa-simetria', 'falsa simetría', 'error argumentativo que presenta dos posiciones como equivalentes cuando no lo son', 'equivalencia falsa',
         'La ______ «hay quien dice A y hay quien dice B» evita tomar posición.', 'falsa', 'falsa simetría'),
        ('absolutismo', 'absolutismo argumentativo', 'error que consiste en presentar una afirmación como totalmente cierta sin matices ni evidencia', 'certeza absoluta',
         'El ______ «es obvio que» debilita el argumento porque no admite objeción.', 'absol', 'absolutismo argumentativo'),
    ],
    ex1=('Argumentación avanzada', 'Elige la opción que refleja la estrategia argumentativa más adecuada en C1.', [
        ('¿Cuál es la función de la concesión estratégica?', ['Rendirse ante el contraargumento', 'Reconocer la objeción para refutarla con más fuerza', 'Evitar tomar posición'], 'Reconocer la objeción para refutarla con más fuerza',
         'La concesión es una táctica: admitir parcialmente el contraargumento fortalece la refutación.'),
        ('¿Qué hace la modalización?', ['Afirma con absoluta certeza', 'Calibra el grado de certeza de una afirmación', 'Introduce un contraargumento'], 'Calibra el grado de certeza de una afirmación',
         'La modalización usa recursos como «es probable que» para matizar y evitar el absolutismo.'),
        ('¿Cuál de estas frases usa la polifonía argumentativa?', ['«Creo que la IA es mala.»', '«Según el informe del FMI (2024), la desigualdad ha aumentado un 15 %.»', '«En conclusión, hay que actuar.»'], '«Según el informe del FMI (2024), la desigualdad ha aumentado un 15 %.»',
         'Citar una fuente reconocida con año y datos precisos es polifonía argumentativa.'),
        ('¿Cuál es el error del absolutismo?', ['Usar demasiadas fuentes', 'Afirmar con certeza total sin matices ni evidencia', 'Incluir una concesión'], 'Afirmar con certeza total sin matices ni evidencia',
         'El absolutismo («es obvio que») debilita el argumento porque no admite objeción.'),
        ('¿Qué hace la proyección argumentativa en la conclusión?', ['Resume los argumentos del ensayo', 'Extiende la tesis hacia sus implicaciones futuras', 'Presenta el tema por primera vez'], 'Extiende la tesis hacia sus implicaciones futuras',
         'La proyección señala qué ocurrirá si no se actúa, abriendo el debate más allá del ensayo.'),
    ]),
    ex2=('Completa el argumento', 'Escribe el término o expresión que completa cada fragmento.', [
        ('«______ la IA crea empleo en algunos sectores, los datos muestran que destruye más del que genera.» (concesión)', 'Si bien', 'Si bien introduce una concesión que reconoce un punto válido del contraargumento.'),
        ('«______ el informe del FMI (2024), la desigualdad global ha aumentado un 15 %.» (polifonía)', 'Según', 'Según introduce la cita de una fuente externa con precisión.'),
        ('«Es ______ que la regulación reduzca los efectos más negativos de la IA.» (modalización)', 'probable', 'Es probable que es una expresión de modalización que calibra la certeza.'),
        ('«Si no actuamos ahora, las ______ serán irreversibles en menos de una década.» (proyección)', 'consecuencias', 'La proyección señala las consecuencias futuras de no actuar sobre el problema.'),
    ]),
    ex3=('Identifica la estrategia', 'Identifica qué estrategia argumentativa usa cada fragmento.', [
        ('«Cierto es que la digitalización moderniza la economía; sin embargo, los datos muestran que aumenta la brecha salarial.»', ['Polifonía', 'Falsa simetría', 'Concesión estratégica + refutación'], 'Concesión estratégica + refutación',
         'El patrón concesión («cierto es que») + pivote («sin embargo») + refutación es la estrategia clásica.'),
        ('«Según la OCDE, el 73 % de los economistas apoya una regulación mínima de la IA.»', ['Modalización', 'Cita de autoridad', 'Proyección'], 'Cita de autoridad',
         'Citar la OCDE con un porcentaje preciso es una cita de autoridad que da credibilidad.'),
        ('«Es probable que una regulación progresiva mitigue los efectos más dañinos a corto plazo.»', ['Absolutismo', 'Concesión', 'Modalización'], 'Modalización',
         '«Es probable que» + subjuntivo calibra la certeza de la afirmación: es modalización.'),
        ('«Si la sociedad no establece límites ahora, la concentración de poder tecnológico será irreversible.»', ['Cita de autoridad', 'Proyección argumentativa', 'Falsa simetría'], 'Proyección argumentativa',
         'Anticipar las consecuencias futuras de no actuar es una proyección argumentativa.'),
    ]),
)

CHAPTERS['analisis-critico'] = dict(
    level='c1', section='writing', num='W02', short='El Análisis Crítico',
    title='El Análisis Crítico de Textos',
    subtitle='Evalúa la solidez de los argumentos y los recursos retóricos de un texto',
    game_desc='Practica las técnicas del análisis crítico en español C1.',
    slides=[
        ('Del análisis al juicio crítico', None,
         '<p class="slide-explanation">El análisis crítico no solo describe; evalúa. El lector critico identifica la tesis, los argumentos, los recursos retóricos y sus puntos débiles.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Análisis:</b> qué dice el texto y cómo lo dice</p>'
         '<p style="margin-top:8px"><b>Crítica:</b> qué tan sólidos son sus argumentos y qué limitaciones tiene</p></div>'),
        ('Evaluar la solidez argumentativa', None,
         '<p class="slide-explanation">Para evaluar si los argumentos son sólidos, hay que comprobar si las premisas son ciertas, si la conclusión se sigue lógicamente y si hay falacias.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Premisa sólida:</b> apoyada en datos verificables</p>'
         '<p style="margin-top:8px"><b>Lógica válida:</b> la conclusión se deduce de las premisas</p>'
         '<p style="margin-top:8px"><b>Falacia:</b> ad hominem, apelación a la emoción, generalización precipitada</p></div>'),
        ('Las falacias argumentativas', None,
         '<p class="slide-explanation">Una falacia es un error en el razonamiento que puede parecer convincente pero que no es lógicamente válido.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Ad hominem:</b> atacar al hablante, no al argumento</p>'
         '<p style="margin-top:8px"><b>Generalización:</b> «todos los jóvenes son irresponsables»</p>'
         '<p style="margin-top:8px"><b>Apelación a la emoción:</b> usar el miedo o la compasión en lugar de la razón</p>'
         '<p style="margin-top:8px"><b>Falso dilema:</b> «o estás con nosotros o estás contra nosotros»</p></div>'),
        ('Los recursos retóricos y su efecto', None,
         '<p class="slide-explanation">En el análisis crítico identificamos los recursos retóricos y evaluamos su función persuasiva.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Eufemismo:</b> suaviza una realidad negativa → «ajuste laboral» por despido</p>'
         '<p style="margin-top:8px"><b>Eufemismo político:</b> crea distancia emocional para minimizar la crítica</p>'
         '<p style="margin-top:8px"><b>Disfemismo:</b> intensifica algo negativo → «purga» en lugar de «reorganización»</p></div>'),
        ('Formular un juicio crítico fundamentado', None,
         '<p class="slide-explanation">El juicio crítico final evalúa la eficacia y la solidez del texto. Debe estar fundamentado con evidencia del propio texto.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Fórmulas:</b></p>'
         '<p style="margin-top:6px">El argumento resulta convincente porque... / La tesis carece de sustento empírico porque...</p>'
         '<p style="margin-top:6px">El texto incurre en la falacia de... al afirmar que...</p>'
         '<p style="margin-top:6px">Si bien el autor logra persuadir en... su posición se debilita cuando...</p></div>'),
    ],
    traps=[
        ('El texto no tiene lógica.', 'El argumento <strong>incurre en una generalización precipitada</strong> al concluir que todos los jóvenes son irresponsables.', 'Nombra la falacia específica con su denominación técnica'),
        ('El autor usa metáforas.', 'El autor emplea el eufemismo «ajuste laboral» para <strong>minimizar el impacto emocional</strong> de los despidos masivos.', 'Explica el efecto retórico del recurso, no solo su presencia'),
        ('El artículo me parece malo.', 'El artículo <strong>carece de sustento empírico</strong> porque sus afirmaciones no citan ninguna fuente verificable.', 'El juicio crítico se fundamenta en evidencia del texto, no en impresión personal'),
        ('El texto es bueno en general.', 'Si bien el autor construye una tesis coherente, <strong>la argumentación se debilita</strong> en el tercer párrafo, donde recurre a la apelación a la emoción.', 'El análisis crítico identifica puntos fuertes Y debilidades con precisión'),
        ('Hay una falacia al decir «o esto o lo otro».', 'El autor incurre en la falacia del <strong>falso dilema</strong> al afirmar que «o se acepta la propuesta o se abandona el proyecto».', 'Usa el nombre técnico de la falacia y cita el fragmento que la ilustra'),
    ],
    summary=[
        ('Premisa sólida', 'apoyada en datos verificables', 'La premisa del autor está respaldada por datos del INE.'),
        ('Falacia ad hominem', 'atacar al hablante, no al argumento', 'El autor incurre en un ad hominem al descalificar al oponente.'),
        ('Generalización', 'conclusión excesiva de pocos casos', 'La generalización «todos los jóvenes» es una falacia.'),
        ('Eufemismo', 'suaviza una realidad negativa', 'El eufemismo «ajuste laboral» oculta la dureza del despido.'),
        ('Juicio fundamentado', 'evaluación con evidencia textual', 'El argumento carece de sustento porque no cita fuentes.'),
        ('Falso dilema', 'o A o B, sin más opciones', 'El falso dilema «o conmigo o contra mí» es una falacia.'),
    ],
    items=[
        ('falacia', 'falacia', 'error en el razonamiento que puede parecer convincente pero que no es lógicamente válido', 'sofisma',
         'La ______ del falso dilema presenta solo dos opciones cuando hay más posibilidades.', 'falac', 'falacia'),
        ('ad-hominem', 'ad hominem', 'falacia que consiste en atacar a la persona que argumenta en lugar de refutar su argumento', 'ataque personal',
         'Decir «no le creas porque es político» es una falacia ______.', 'ad hom', 'ad hominem'),
        ('eufemismo', 'eufemismo', 'expresión suavizada que sustituye a otra más directa o negativa para minimizar su impacto', 'atenuación',
         'El término «ajuste de plantilla» es un ______ que evita la palabra despido.', 'eufem', 'eufemismo'),
        ('disfemismo', 'disfemismo', 'expresión que intensifica la connotación negativa de algo para provocar rechazo', 'intensificador negativo',
         'Llamar «purga» a una reorganización de personal es un ______ deliberado.', 'disfem', 'disfemismo'),
        ('premisa', 'premisa', 'afirmación de la que parte un argumento y que debe ser cierta para que la conclusión sea válida', 'proposición base',
         'Si la ______ es falsa, el argumento entero se derrumba aunque la lógica sea correcta.', 'prem', 'premisa'),
        ('generalizacion', 'generalización precipitada', 'falacia que extrae una conclusión universal a partir de un número insuficiente de casos', 'generalización indebida',
         'La ______ «todos los inmigrantes...» es un error lógico frecuente en el discurso populista.', 'general', 'generalización precipitada'),
        ('falso-dilema', 'falso dilema', 'falacia que reduce un problema a dos opciones excluyentes ignorando las alternativas', 'disyunción falsa',
         '«O estás a favor o estás en contra» es un ______ que elimina las posiciones intermedias.', 'falso', 'falso dilema'),
        ('apelacion-emocion', 'apelación a la emoción', 'falacia que usa el miedo, la compasión o la indignación en lugar de argumentos racionales', 'argumento emocional',
         'Usar imágenes de niños sufriendo para justificar una política económica es una ______.', 'apelac', 'apelación a la emoción'),
    ],
    ex1=('Análisis crítico', 'Elige la respuesta correcta sobre el análisis crítico de textos.', [
        ('¿Qué distingue el análisis crítico del análisis descriptivo?', ['El análisis crítico solo resume el texto', 'El análisis crítico evalúa la solidez y las limitaciones del texto', 'El análisis crítico describe los recursos sin valorarlos'], 'El análisis crítico evalúa la solidez y las limitaciones del texto',
         'El análisis crítico va más allá de describir: juzga si los argumentos son válidos y qué recursos usa el autor.'),
        ('¿Qué es una falacia ad hominem?', ['Una generalización a partir de pocos casos', 'Atacar a la persona en lugar de refutar su argumento', 'Presentar solo dos opciones'], 'Atacar a la persona en lugar de refutar su argumento',
         'El ad hominem descalifica al hablante («no le creas porque es político») en lugar de refutar lo que dice.'),
        ('¿Cuál es la función del eufemismo en un discurso?', ['Intensificar algo negativo', 'Suavizar una realidad negativa para minimizar su impacto', 'Citar una fuente externa'], 'Suavizar una realidad negativa para minimizar su impacto',
         'El eufemismo («ajuste laboral») reduce el impacto emocional de una realidad negativa (despido).'),
        ('¿Cómo se formula un juicio crítico fundamentado?', ['«El texto me parece malo en general.»', '«El argumento carece de sustento empírico porque no cita fuentes verificables.»', '«El autor usa metáforas y comparaciones.»'], '«El argumento carece de sustento empírico porque no cita fuentes verificables.»',
         'El juicio fundamentado evalúa con evidencia concreta del texto, no con impresiones vagas.'),
        ('¿Qué es el falso dilema?', ['Un argumento con dos premisas', 'Una falacia que reduce el problema a dos opciones ignorando otras', 'Un recurso retórico para persuadir'], 'Una falacia que reduce el problema a dos opciones ignorando otras',
         'El falso dilema («o conmigo o contra mí») presenta solo dos posibilidades cuando hay más.'),
    ]),
    ex2=('Identifica la falacia', 'Escribe el nombre de la falacia que se describe.', [
        ('«No puedes opinar sobre economía porque no tienes carrera universitaria.»', 'ad hominem', 'Se ataca al hablante (su falta de título) en lugar de refutar su argumento.'),
        ('«Los jóvenes de hoy no saben trabajar. He visto a tres que llegaron tarde.»', 'generalización precipitada', 'Tres casos no bastan para concluir que «los jóvenes» en general no saben trabajar.'),
        ('«O aceptas mis condiciones o el proyecto fracasará.»', 'falso dilema', 'Solo se presentan dos opciones cuando puede haber alternativas intermedias.'),
        ('Usar imágenes de catástrofes para apoyar una medida fiscal.', 'apelación a la emoción', 'Las imágenes apelan al miedo o la compasión en lugar de ofrecer argumentos racionales.'),
    ]),
    ex3=('Recurso retórico', 'Identifica el recurso retórico en cada fragmento.', [
        ('«El gobierno ha llevado a cabo un ajuste de plantilla en el sector público.»', ['Disfemismo', 'Eufemismo', 'Falacia ad hominem'], 'Eufemismo',
         '«Ajuste de plantilla» suaviza la realidad de los despidos masivos: es un eufemismo.'),
        ('«La purga de funcionarios impuesta por el gobierno ha destruido miles de vidas.»', ['Eufemismo', 'Apelación a la emoción', 'Disfemismo'], 'Disfemismo',
         '«Purga» intensifica la connotación negativa de la medida para provocar rechazo: es un disfemismo.'),
        ('«Si votamos a este partido, España quedará arruinada para siempre.»', ['Eufemismo', 'Apelación a la emoción', 'Ad hominem'], 'Apelación a la emoción',
         'El miedo a la ruina apela a la emoción en lugar de ofrecer evidencia: es una apelación emocional.'),
        ('«Ciertamente, la propuesta tiene ventajas; sin embargo, sus efectos a largo plazo son inciertos.»', ['Falsa simetría', 'Concesión + modalización', 'Falacia de generalización'], 'Concesión + modalización',
         '«Ciertamente» es una concesión; «son inciertos» modaliza con cautela.'),
    ]),
)

CHAPTERS['texto-academico'] = dict(
    level='c1', section='writing', num='W03', short='El Texto Académico',
    title='El Texto Académico',
    subtitle='Escribe con rigor, precisión terminológica y estructura académica',
    game_desc='Practica el registro y las convenciones del texto académico en español.',
    slides=[
        ('Características del texto académico', None,
         '<p class="slide-explanation">El texto académico es preciso, objetivo e impersonal. Se dirige a un público especializado y sigue convenciones formales de estructura y citación.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Precisión:</b> vocabulario especializado, sin ambigüedad</p>'
         '<p style="margin-top:6px"><b>Objetividad:</b> lenguaje impersonal, verbos en voz pasiva o con «se»</p>'
         '<p style="margin-top:6px"><b>Estructura:</b> introducción, desarrollo, conclusiones, referencias</p>'
         '<p style="margin-top:6px"><b>Intertextualidad:</b> citas y referencias a otros autores</p></div>'),
        ('El registro académico vs el registro periodístico', None,
         '<p class="slide-explanation">El texto académico difiere del artículo periodístico en precisión terminológica, registro y convenciones de citación.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Periodístico:</b> «La IA está cambiando el mundo.»</p>'
         '<p style="margin-top:8px"><b>Académico:</b> «La inteligencia artificial generativa está reconfigurando los mercados laborales en los países de la OCDE (García, 2024).»</p></div>'),
        ('La objetividad y la impersonalidad', None,
         '<p class="slide-explanation">El texto académico evita la primera persona del singular y usa construcciones impersonales o pasivas.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Incorrecto (primera persona):</b> «En este trabajo voy a analizar...»</p>'
         '<p style="margin-top:8px"><b>Correcto (impersonal):</b> «En el presente trabajo se analiza...»</p>'
         '<p style="margin-top:8px"><b>Correcto (pasiva):</b> «Los datos fueron recogidos mediante encuesta.»</p></div>'),
        ('La citación y las referencias', None,
         '<p class="slide-explanation">Todo texto académico cita sus fuentes. La citación da credibilidad y evita el plagio.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Cita integrada:</b> García (2024) sostiene que «la IA reemplazará el 40 % de los empleos actuales».</p>'
         '<p style="margin-top:8px"><b>Cita entre paréntesis:</b> La IA reemplazará el 40 % de los empleos actuales (García, 2024).</p>'
         '<p style="margin-top:8px"><b>Referencia en lista:</b> García, M. (2024). <i>Inteligencia artificial y mercado laboral.</i> Madrid: Alianza.</p></div>'),
        ('La estructura del texto académico', None,
         '<p class="slide-explanation">Un texto académico tiene partes bien definidas que guían al lector especializado.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Resumen/abstract:</b> síntesis del contenido en 150-200 palabras</p>'
         '<p style="margin-top:6px"><b>Introducción:</b> planteamiento del problema, objetivos, metodología</p>'
         '<p style="margin-top:6px"><b>Desarrollo:</b> análisis por secciones o apartados con título</p>'
         '<p style="margin-top:6px"><b>Conclusiones:</b> hallazgos, limitaciones, líneas futuras</p>'
         '<p style="margin-top:6px"><b>Referencias:</b> lista bibliográfica</p></div>'),
    ],
    traps=[
        ('Voy a hablar de la inteligencia artificial.', 'En el presente trabajo <strong>se analiza</strong> el impacto de la inteligencia artificial generativa en los mercados laborales.', 'El texto académico usa lenguaje impersonal; evita «voy a» y la primera persona del singular'),
        ('La IA es muy importante hoy en día.', 'La inteligencia artificial generativa <strong>está reconfigurando los mercados laborales</strong> en los países de la OCDE (García, 2024).', 'Sustituye adjetivos vagos por afirmaciones precisas con fuente citada'),
        ('Un estudio dice que la IA destruye empleo.', 'García (2024) <strong>demuestra que</strong> la automatización elimina el 40 % de los empleos rutinarios en el sector manufacturero.', 'Cita autor, año y dato preciso; usa un verbo de reporte específico'),
        ('En conclusión, la IA es buena y mala.', 'En conclusión, <strong>los datos analizados sugieren</strong> que la IA incrementa la productividad pero agrava la desigualdad salarial.', 'La conclusión académica evalúa los resultados con precisión, no con dicotomías vagas'),
        ('Este tema es muy complejo y hay muchas opiniones.', 'El debate sobre la gobernanza de la IA <strong>presenta múltiples perspectivas</strong> que se articulan en torno a tres ejes: regulación, innovación y equidad.', 'Organiza la complejidad en categorías analíticas precisas'),
    ],
    summary=[
        ('Impersonalidad', 'se analiza / se ha demostrado', 'En el presente trabajo se analiza el impacto de la IA.'),
        ('Cita integrada', 'García (2024) sostiene que...', 'García (2024) demuestra que la IA elimina el 40 % de empleos rutinarios.'),
        ('Cita parentética', '...(García, 2024).', 'La IA reemplazará el 40 % de los empleos actuales (García, 2024).'),
        ('Registro preciso', 'terminología especializada', '«IA generativa» en lugar del vago «IA moderna».'),
        ('Conclusión académica', 'los resultados sugieren / se concluye que', 'Los resultados sugieren que la regulación reduce la brecha salarial.'),
        ('Abstract', 'síntesis en 150-200 palabras', 'El presente estudio analiza... Los principales hallazgos muestran...'),
    ],
    items=[
        ('impersonalidad', 'impersonalidad', 'rasgo del texto académico que evita la primera persona y usa construcciones con «se» o voz pasiva', 'registro objetivo',
         'La ______ del texto académico se logra con «se analiza» en lugar de «analizo».', 'imperson', 'impersonalidad'),
        ('intertextualidad', 'intertextualidad', 'relación entre un texto y las fuentes y autores que cita o con los que dialoga', 'citación',
         'La ______ del ensayo académico exige citar todas las fuentes consultadas.', 'intertex', 'intertextualidad'),
        ('abstract', 'abstract', 'resumen breve y estructurado que sintetiza el contenido de un trabajo académico', 'resumen ejecutivo',
         'El ______ de 150-200 palabras presenta el objetivo, la metodología y los hallazgos.', 'abstr', 'abstract'),
        ('citacion', 'citación', 'referencia explícita a una fuente externa integrada en el texto con autor, año y datos', 'referencia bibliográfica',
         'La ______ «García (2024)» indica que la idea proviene de esa fuente específica.', 'citac', 'citación'),
        ('terminologia', 'terminología especializada', 'vocabulario técnico y preciso propio de una disciplina académica', 'léxico técnico',
         'El uso de ______ diferencia el texto académico del periodístico o divulgativo.', 'terminol', 'terminología especializada'),
        ('verbo-reporte-acad', 'verbo de reporte académico', 'verbo preciso que introduce las afirmaciones de otro autor: demostrar, señalar, concluir, proponer', 'verbo introductor',
         'García (2024) <b>demuestra que</b>... es más preciso que el vago «dice que».', 'verbo', 'verbo de reporte académico'),
        ('hallazgo', 'hallazgo', 'resultado o descubrimiento significativo que emerge del análisis realizado en la investigación', 'resultado',
         'Los ______ del estudio sugieren que la IA agrava la desigualdad salarial.', 'hallaz', 'hallazgo'),
        ('limitacion', 'limitación del estudio', 'restricción o debilidad del trabajo académico que afecta a la generalización de sus conclusiones', 'restricción metodológica',
         'Una ______ del presente estudio es el reducido tamaño de la muestra analizada.', 'limit', 'limitación del estudio'),
    ],
    ex1=('El texto académico', 'Elige la respuesta correcta sobre las convenciones del texto académico.', [
        ('¿Cómo se expresa la objetividad en el texto académico?', ['Con la primera persona del plural', 'Con construcciones impersonales y voz pasiva', 'Con adjetivos valorativos'], 'Con construcciones impersonales y voz pasiva',
         '«Se analiza» y «los datos fueron recogidos» son las formas impersonales características del texto académico.'),
        ('¿Qué debe incluir una cita integrada?', ['Solo el año', 'Autor, año y verbo de reporte preciso', 'El título de la obra'], 'Autor, año y verbo de reporte preciso',
         'La cita integrada sigue el patrón: García (2024) + verbo de reporte + afirmación.'),
        ('¿Qué es el abstract?', ['La bibliografía del trabajo', 'El resumen breve que sintetiza el contenido del trabajo', 'La introducción completa'], 'El resumen breve que sintetiza el contenido del trabajo',
         'El abstract sintetiza en 150-200 palabras el objetivo, la metodología y los hallazgos.'),
        ('¿Por qué se usa terminología especializada?', ['Para complicar el texto', 'Para ser preciso y evitar ambigüedades', 'Para impresionar al lector'], 'Para ser preciso y evitar ambigüedades',
         'La terminología especializada nombra conceptos con exactitud, sin los múltiples sentidos del lenguaje común.'),
        ('¿Cuál es la función de la sección de limitaciones?', ['Demostrar que el estudio es inútil', 'Mostrar las restricciones que afectan a la generalización de los resultados', 'Resumir los hallazgos'], 'Mostrar las restricciones que afectan a la generalización de los resultados',
         'Las limitaciones informan al lector sobre las condiciones en que los resultados son válidos.'),
    ]),
    ex2=('Registro académico', 'Reescribe o completa cada frase con el registro académico correcto.', [
        ('En el presente trabajo ______ el impacto de la IA en los mercados laborales. (impersonal)', 'se analiza', 'Se analiza es la forma impersonal que sustituye a «voy a analizar».'),
        ('García (2024) ______ que la automatización elimina el 40 % de los empleos rutinarios. (verbo de reporte)', 'demuestra', 'Demostrar es un verbo de reporte preciso para afirmaciones respaldadas por datos.'),
        ('Los ______ del estudio sugieren que la IA agrava la desigualdad salarial.', 'hallazgos', 'Los hallazgos son los resultados o descubrimientos significativos del estudio.'),
        ('Una ______ del presente estudio es el reducido tamaño de la muestra.', 'limitación', 'La limitación señala las restricciones que afectan a la validez de los resultados.'),
    ]),
    ex3=('Académico o no académico', 'Identifica si cada fragmento pertenece a un texto académico o a uno periodístico/divulgativo.', [
        ('«La IA está cambiando el mundo de una forma increíble y nadie puede ignorarlo.»', ['Texto académico', 'Texto periodístico/divulgativo'], 'Texto periodístico/divulgativo',
         'El lenguaje vago («increíble», «nadie») y la primera persona son rasgos del texto periodístico.'),
        ('«García (2024) demuestra que la automatización elimina el 40 % de los empleos rutinarios en el sector manufacturero de la OCDE.»', ['Texto periodístico/divulgativo', 'Texto académico'], 'Texto académico',
         'La cita integrada con autor, año y datos precisos es característica del texto académico.'),
        ('«En el presente estudio se analizan los efectos de la automatización sobre la desigualdad salarial.»', ['Texto periodístico/divulgativo', 'Texto académico'], 'Texto académico',
         'La construcción impersonal «se analizan» y el vocabulario preciso son rasgos del texto académico.'),
        ('«Los robots nos van a quitar el trabajo, eso está claro.»', ['Texto académico', 'Texto periodístico/divulgativo'], 'Texto periodístico/divulgativo',
         'El tono coloquial, la primera persona y la certeza sin fuente son rasgos del texto divulgativo.'),
    ]),
)

CHAPTERS['columna-opinion'] = dict(
    level='c1', section='writing', num='W04', short='La Columna de Opinión',
    title='La Columna de Opinión C1',
    subtitle='Escribe con voz propia, autoridad y elegancia estilística',
    game_desc='Practica el estilo y las estrategias de la columna de opinión avanzada.',
    slides=[
        ('La columna de opinión como género de autor', None,
         '<p class="slide-explanation">La columna de opinión C1 exige una voz personal reconocible, un estilo cuidado y la capacidad de iluminar temas complejos con perspectiva original.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Voz de autor:</b> perspectiva original, tono personal, estilo propio</p>'
         '<p style="margin-top:8px"><b>Elegancia estilística:</b> variedad sintáctica, vocabulario preciso, ritmo</p>'
         '<p style="margin-top:8px"><b>Profundidad:</b> va más allá del hecho noticioso; lo interpreta</p></div>'),
        ('El distanciamiento irónico', None,
         '<p class="slide-explanation">El distanciamiento irónico es una técnica que permite al columnista criticar sin atacar directamente, apelando a la inteligencia del lector.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Ironía suave:</b> «Qué maravilla de transparencia la de nuestros representantes.»</p>'
         '<p style="margin-top:8px"><b>Sarcasmo:</b> «Es de agradecer que, después de tres escándalos, el ministro haya tenido la deferencia de dimitir.»</p></div>'),
        ('La anáfora y la enumeración rítmica', None,
         '<p class="slide-explanation">La anáfora (repetición al inicio de frases) y la enumeración rítmica dan fuerza y musicalidad al texto.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Anáfora:</b> «Hablamos de educación. Hablamos de futuro. Hablamos, en definitiva, de quiénes somos.»</p>'
         '<p style="margin-top:8px"><b>Enumeración rítmica:</b> «paz, libertad, dignidad y memoria»</p></div>'),
        ('La referencia cultural y la intertextualidad', None,
         '<p class="slide-explanation">Las referencias culturales (literarias, filosóficas, históricas) enriquecen la columna y establecen un diálogo con el lector cultivado.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Cita literaria:</b> «Como diría Cervantes, «con la Iglesia hemos topado».»</p>'
         '<p style="margin-top:8px"><b>Referencia histórica:</b> «Estamos ante un nuevo Watergate de la vida política española.»</p>'
         '<p style="margin-top:8px"><b>Referencia filosófica:</b> «La pregunta de Habermas sigue vigente: ¿puede existir democracia sin esfera pública?»</p></div>'),
        ('El cierre de la columna: la imagen final', None,
         '<p class="slide-explanation">El cierre de una columna C1 a menudo usa una imagen, una paradoja o una pregunta que condensa el argumento y permanece en la memoria del lector.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Imagen final:</b> «Al final, el silencio de los que saben siempre es más ensordecedor que el ruido de los que ignoran.»</p>'
         '<p style="margin-top:8px"><b>Paradoja:</b> «Hemos construido un mundo que lo comunica todo y no escucha nada.»</p></div>'),
    ],
    traps=[
        ('Voy a hablar de la corrupción política.', 'La corrupción no es un escándalo puntual: <strong>es el sistema</strong>.', 'El columnista no anuncia su tema; lo golpea desde el principio'),
        ('Es muy irónico que los políticos roben.', 'Es de <strong>agradecer que</strong>, después de tres escándalos, el ministro haya tenido la deferencia de dimitir.', 'La ironía C1 es indirecta y elegante, no explícita'),
        ('En conclusión, la democracia está en peligro.', 'Al final, <strong>el silencio de los que saben es más ensordecedor</strong> que el ruido de los que ignoran.', 'El cierre de la columna C1 usa una imagen o paradoja, no una conclusión plana'),
        ('Muchos autores han hablado de esto.', 'Como señalaba <strong>Habermas</strong>, la democracia sin esfera pública es una contradicción en sus propios términos.', 'Cita un nombre concreto y su idea específica; evita las referencias vagas'),
        ('La corrupción es mala para todos.', 'La corrupción no destruye solo el erario: <strong>corroe la confianza</strong>, que es el tejido del que está hecha la democracia.', 'Busca la imagen precisa que eleva la idea más allá de la obviedad'),
    ],
    summary=[
        ('Voz de autor', 'perspectiva original desde el primer párrafo', 'La corrupción no es un escándalo puntual: es el sistema.'),
        ('Ironía elegante', 'distanciamiento irónico, no sarcasmo grosero', 'Es de agradecer que el ministro haya tenido la deferencia de dimitir.'),
        ('Anáfora', 'repetición al inicio de frases', 'Hablamos de educación. Hablamos de futuro. Hablamos de quiénes somos.'),
        ('Referencia cultural', 'cita literaria, histórica o filosófica', 'Como señalaba Habermas, la democracia sin esfera pública es una contradicción.'),
        ('Imagen final', 'paradoja o imagen que condensa el argumento', 'El silencio de los que saben es más ensordecedor que el ruido de los que ignoran.'),
        ('Ritmo', 'variedad sintáctica, frases cortas y largas alternadas', 'Cortos golpes. Luego una frase larga que desarrolla y amplía la idea.'),
    ],
    items=[
        ('voz-autor', 'voz de autor', 'perspectiva personal reconocible y estilo propio del columnista que distingue su escritura', 'estilo personal',
         'La ______ del columnista se reconoce por su tono, su vocabulario y su perspectiva única.', 'voz', 'voz de autor'),
        ('distanciamiento', 'distanciamiento irónico', 'técnica que permite criticar con elegancia sin atacar directamente, apelando a la inteligencia del lector', 'ironía elegante',
         'El ______ permite al columnista denunciar la corrupción sin perder la cortesía formal.', 'distan', 'distanciamiento irónico'),
        ('anafora', 'anáfora', 'figura retórica que consiste en repetir una palabra o expresión al inicio de frases sucesivas', 'repetición anafórica',
         'La ______ «Hablamos de... Hablamos de...» da ritmo y fuerza al texto.', 'anáf', 'anáfora'),
        ('referencia-cultural', 'referencia cultural', 'alusión a un texto literario, hecho histórico o pensador filosófico que enriquece el argumento', 'intertextualidad',
         'La ______ a Habermas sitúa el debate en el marco del pensamiento democrático contemporáneo.', 'refer', 'referencia cultural'),
        ('imagen-final', 'imagen final', 'figura o paradoja que cierra la columna condensando el argumento de forma memorable', 'cierre impactante',
         'La ______ «el silencio es más ensordecedor que el ruido» permanece en la memoria del lector.', 'imagen', 'imagen final'),
        ('sarcasmo', 'sarcasmo', 'ironía más afilada y directa que critica con dureza usando el elogio para denunciar', 'ironía mordaz',
         'El ______ «es de agradecer que haya dimitido» critica al ministro con elegancia hiriente.', 'sarcas', 'sarcasmo'),
        ('paradoja', 'paradoja', 'afirmación aparentemente contradictoria que encierra una verdad profunda sobre el tema tratado', 'contradicción aparente',
         'La ______ «lo comunica todo y no escucha nada» sintetiza la crítica a la era digital.', 'parad', 'paradoja'),
        ('ritmo', 'ritmo prosístico', 'alternancia de frases cortas y largas que crea musicalidad y dinamismo en el texto', 'cadencia',
         'El ______ de la columna alterna frases breves con otras desarrolladas para mantener la atención.', 'ritmo', 'ritmo prosístico'),
    ],
    ex1=('La columna C1', 'Elige la opción que refleja mejor las características de la columna de opinión C1.', [
        ('¿Qué diferencia la columna C1 del artículo de opinión B2?', ['La columna no tiene argumentos', 'La columna tiene una voz de autor más elaborada y referencias culturales', 'La columna es más corta'], 'La columna tiene una voz de autor más elaborada y referencias culturales',
         'La columna C1 exige un estilo sofisticado, referencias cultas y perspectiva original.'),
        ('¿Qué es el distanciamiento irónico?', ['Atacar directamente al oponente', 'Criticar con elegancia sin ataque directo, apelando a la inteligencia del lector', 'Usar sarcasmo grosero'], 'Criticar con elegancia sin ataque directo, apelando a la inteligencia del lector',
         'El distanciamiento irónico usa el elogio fingido para denunciar sin perder la compostura formal.'),
        ('¿Cuál es la función de la anáfora?', ['Introducir un contraargumento', 'Dar ritmo y fuerza mediante la repetición al inicio de frases', 'Citar una fuente externa'], 'Dar ritmo y fuerza mediante la repetición al inicio de frases',
         'La anáfora crea un ritmo acumulativo que intensifica el impacto del argumento.'),
        ('¿Cómo debe ser el cierre de una columna C1?', ['Resumir los argumentos principales', 'Usar una imagen o paradoja que condense el argumento de forma memorable', 'Anunciar el próximo artículo'], 'Usar una imagen o paradoja que condense el argumento de forma memorable',
         'El cierre de la columna C1 deja una impresión duradera mediante una imagen o paradoja.'),
        ('¿Por qué se usan referencias culturales en la columna?', ['Para demostrar erudición vacía', 'Para enriquecer el argumento y establecer diálogo con el lector cultivado', 'Para cumplir con las normas académicas'], 'Para enriquecer el argumento y establecer diálogo con el lector cultivado',
         'Las referencias culturales sitúan el argumento en un marco más amplio y crean complicidad con el lector.'),
    ]),
    ex2=('Estilo de columnista', 'Completa con la técnica o recurso que se usa en cada fragmento.', [
        ('«Hablamos de educación. Hablamos de futuro. Hablamos de quiénes somos.» Este recurso es una ______.', 'anáfora', 'La anáfora repite «hablamos de» al inicio de cada frase para crear ritmo acumulativo.'),
        ('«Es de agradecer que el ministro haya tenido la deferencia de dimitir.» Es un ejemplo de ______.', 'distanciamiento irónico', 'El elogio fingido critica con elegancia sin atacar directamente: es distanciamiento irónico.'),
        ('«Como señalaba Habermas, la democracia sin esfera pública es una contradicción.» Es una ______.', 'referencia cultural', 'Citar a Habermas enriquece el argumento con una referencia filosófica reconocida.'),
        ('«Hemos construido un mundo que lo comunica todo y no escucha nada.» Es una ______.', 'paradoja', 'La aparente contradicción entre «comunicar» y «no escuchar» forma una paradoja.'),
    ]),
    ex3=('Recursos de la columna', 'Identifica el recurso retórico en cada fragmento.', [
        ('«Luchamos por la paz. Luchamos por la justicia. Luchamos, en fin, por ser humanos.»', ['Sarcasmo', 'Anáfora', 'Imagen final'], 'Anáfora',
         'La repetición de «luchamos por» al inicio de cada frase es una anáfora.'),
        ('«Vivimos en la sociedad del conocimiento y nunca hemos sido tan ignorantes.»', ['Anáfora', 'Referencia cultural', 'Paradoja'], 'Paradoja',
         'La contradicción entre «conocimiento» e «ignorancia» para el mismo sujeto forma una paradoja.'),
        ('«Qué generosa la memoria de los que siempre olvidan.»', ['Paradoja', 'Distanciamiento irónico', 'Anáfora'], 'Distanciamiento irónico',
         'Elogiar la «generosidad» de quienes olvidan es una crítica irónica y elegante.'),
        ('«Como diría Kafka, el proceso continúa aunque nadie sepa muy bien de qué se le acusa.»', ['Anáfora', 'Sarcasmo', 'Referencia cultural'], 'Referencia cultural',
         'Citar a Kafka conecta el hecho noticioso con un marco literario más amplio.'),
    ]),
)

CHAPTERS['carta-institucional'] = dict(
    level='c1', section='writing', num='W05', short='La Carta Institucional',
    title='La Carta Institucional C1',
    subtitle='Domina el lenguaje jurídico-administrativo y los géneros institucionales',
    game_desc='Practica los géneros epistolares institucionales en español C1.',
    slides=[
        ('El lenguaje jurídico-administrativo', None,
         '<p class="slide-explanation">El lenguaje institucional tiene fórmulas fijas, construcciones impersonales y un vocabulario jurídico-administrativo preciso que debe dominarse en C1.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Verbos clave:</b> disponer, acordar, requerir, notificar, certificar, elevar (a instancia superior)</p>'
         '<p style="margin-top:8px"><b>Sustantivos:</b> resolución, providencia, auto, recurso de alzada, trámite, diligencia</p>'
         '<p style="margin-top:8px"><b>Fórmulas:</b> en uso de las atribuciones que le confiere... / visto lo actuado...</p></div>'),
        ('El recurso administrativo', None,
         '<p class="slide-explanation">El recurso es una carta formal por la que el ciudadano impugna una resolución administrativa que considera injusta o incorrecta.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Estructura:</b> datos del recurrente → resolución impugnada → fundamentos de derecho → solicitud</p>'
         '<p style="margin-top:8px"><b>Ejemplo:</b> «El/la abajo firmante, [...], interpone recurso de reposición contra la Resolución de fecha X...»</p></div>'),
        ('El certificado y la declaración jurada', None,
         '<p class="slide-explanation">El certificado es un documento oficial que acredita un hecho. La declaración jurada es una manifestación formal de verdad bajo responsabilidad legal.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Certificado:</b> «D./Dña. [...] CERTIFICA que... Y para que conste, firma el presente certificado en [...], a [...] de [...] de [...].»</p>'
         '<p style="margin-top:8px"><b>Declaración jurada:</b> «Declaro bajo juramento que los datos aportados son verídicos.»</p></div>'),
        ('El lenguaje de la notificación oficial', None,
         '<p class="slide-explanation">La notificación informa al ciudadano de una decisión administrativa. Su lenguaje es impersonal, formal y preciso.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Fórmulas:</b> «Por la presente se le notifica que...» / «En cumplimiento de lo dispuesto en...» / «Transcurrido el plazo establecido sin que...»</p>'
         '<p style="margin-top:8px"><b>Consecuencias:</b> «...se procederá a archivar la solicitud» / «...caducará el expediente»</p></div>'),
        ('La exposición de motivos', None,
         '<p class="slide-explanation">La exposición de motivos explica las razones jurídicas o de hecho que justifican una solicitud o resolución. Suele preceder a la parte dispositiva.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Estructura:</b> EXPONE (hechos) → SOLICITA (petición) → FUNDAMENTA (base legal)</p>'
         '<p style="margin-top:8px"><b>Fórmulas:</b> «En virtud de lo expuesto...» / «Al amparo del artículo X de la Ley Y...» / «Fundamenta su solicitud en...»</p></div>'),
    ],
    traps=[
        ('Quiero recurrir la decisión.', 'El/la abajo firmante <strong>interpone recurso de reposición</strong> contra la Resolución de fecha X, por las razones que a continuación se exponen.', 'El recurso usa fórmulas fijas: «interponer recurso» + tipo + contra + resolución identificada'),
        ('La empresa me certifica que trabajé allí.', '<strong>CERTIFICA que D./Dña. Ana Torres Sánchez prestó servicios</strong> en esta empresa entre el 1 de enero de 2022 y el 31 de diciembre de 2023.', 'El certificado usa verbo en mayúscula, nombre completo del interesado y datos precisos'),
        ('Por la ley X tengo derecho a pedir esto.', '<strong>Al amparo del artículo 14 de la Constitución Española</strong> y del artículo 3 de la Ley 39/2015, solicita...', 'Cita el artículo y la ley específica con su número; evita referencias vagas'),
        ('Le digo que tiene 15 días para contestar.', '<strong>Se le notifica que dispone de un plazo de quince días hábiles</strong> para interponer los recursos que estime oportunos.', 'La notificación usa lenguaje impersonal y especifica «días hábiles»'),
        ('Declaro que todo lo que digo es verdad.', '<strong>Declaro bajo mi responsabilidad</strong> que los datos aportados son verídicos, comprometiéndome a acreditar documentalmente cualquier extremo si fuera requerido para ello.', 'La declaración responsable usa fórmula legal completa con cláusula de responsabilidad'),
    ],
    summary=[
        ('Recurso', 'interponer recurso de reposición contra...', 'El abajo firmante interpone recurso contra la Resolución de 3 de junio.'),
        ('Certificado', 'CERTIFICA que... Y para que conste...', 'CERTIFICA que D. Luis García prestó servicios entre 2022 y 2023.'),
        ('Notificación', 'Por la presente se le notifica que...', 'Por la presente se le notifica que dispone de 15 días hábiles.'),
        ('Base legal', 'Al amparo del artículo X de la Ley Y', 'Al amparo del artículo 14 de la Constitución Española, solicita...'),
        ('Declaración responsable', 'Declaro bajo mi responsabilidad que...', 'Declaro que los datos son verídicos y me comprometo a acreditarlos.'),
        ('Parte dispositiva', 'EXPONE... SOLICITA...', 'EXPONE los hechos. SOLICITA la concesión de la beca.'),
    ],
    items=[
        ('recurso', 'recurso administrativo', 'escrito formal por el que el ciudadano impugna una resolución administrativa que considera incorrecta', 'impugnación',
         'El ______ de reposición debe interponerse en el plazo de un mes desde la notificación.', 'recurs', 'recurso administrativo'),
        ('resolución', 'resolución administrativa', 'decisión oficial dictada por una autoridad administrativa en respuesta a un trámite o solicitud', 'acto administrativo',
         'La ______ deniega la beca alegando que los requisitos no han sido acreditados.', 'resol', 'resolución administrativa'),
        ('certificar', 'certificar', 'hacer constar oficialmente un hecho mediante un documento firmado por la autoridad competente', 'acreditar oficialmente',
         'El secretario ______ que el interesado cumple todos los requisitos establecidos en la convocatoria.', 'certif', 'certificar'),
        ('notificar', 'notificar', 'comunicar oficialmente a una persona una decisión o acto administrativo que le afecta', 'comunicar oficialmente',
         'La administración ______ al interesado que su solicitud ha sido denegada.', 'notif', 'notificar'),
        ('exposicion-motivos', 'exposición de motivos', 'parte de un escrito formal en la que se explican las razones de hecho y de derecho que justifican la solicitud', 'justificación',
         'La ______ precede a la parte dispositiva y fundamenta la solicitud en la ley aplicable.', 'exposic', 'exposición de motivos'),
        ('amparo', 'al amparo de', 'expresión legal que indica la norma o artículo que sirve de base jurídica a una solicitud', 'con base en',
         '______ el artículo 14 de la Constitución Española, solicita la revisión del expediente.', 'al amparo de', 'al amparo de'),
        ('plazo-habiles', 'días hábiles', 'días laborables, excluidos sábados, domingos y festivos, que se cuentan para los plazos administrativos', 'días laborables',
         'Dispone de quince ______ para interponer el recurso correspondiente.', 'días', 'días hábiles'),
        ('interponer', 'interponer', 'presentar formalmente un recurso o reclamación ante la autoridad competente', 'presentar formalmente',
         'El ciudadano ______ un recurso de alzada ante el órgano superior jerárquico.', 'interpon', 'interponer'),
    ],
    ex1=('Lenguaje institucional', 'Elige la expresión más adecuada en cada contexto institucional.', [
        ('¿Cómo se comienza un recurso administrativo?', ['«Hola, quiero recurrir la resolución.»', '«El abajo firmante interpone recurso de reposición contra la Resolución de fecha X.»', '«Me opongo a la decisión que han tomado.»'], '«El abajo firmante interpone recurso de reposición contra la Resolución de fecha X.»',
         'El recurso usa fórmulas fijas: «el abajo firmante interpone recurso de» + tipo.'),
        ('¿Qué indica «al amparo de» en un escrito?', ['El plazo para recurrir', 'La norma jurídica que sirve de base a la solicitud', 'La autoridad que firma el documento'], 'La norma jurídica que sirve de base a la solicitud',
         '«Al amparo del artículo X de la Ley Y» indica la base legal de la solicitud.'),
        ('¿Qué son los días hábiles?', ['Todos los días del año', 'Los días laborables, excluidos festivos y fines de semana', 'Los días en que la administración está cerrada'], 'Los días laborables, excluidos festivos y fines de semana',
         'Los días hábiles son los días laborables que se cuentan para los plazos administrativos.'),
        ('¿Cómo se certifica un hecho en un documento oficial?', ['«Le digo que Ana trabajó aquí.»', '«CERTIFICA que D./Dña. Ana Torres prestó servicios entre las fechas X e Y.»', '«Ana trabajó en esta empresa.»'], '«CERTIFICA que D./Dña. Ana Torres prestó servicios entre las fechas X e Y.»',
         'El certificado usa el verbo en mayúscula, nombre completo y datos precisos.'),
        ('¿Cuál es la función de la exposición de motivos?', ['Presentar los datos del solicitante', 'Explicar las razones de hecho y de derecho que justifican la solicitud', 'Indicar el plazo de respuesta'], 'Explicar las razones de hecho y de derecho que justifican la solicitud',
         'La exposición de motivos fundamenta la solicitud antes de la parte dispositiva.'),
    ]),
    ex2=('Fórmulas institucionales', 'Completa con la expresión institucional adecuada.', [
        ('______ del artículo 23 de la Constitución Española, solicita la revisión del expediente.', 'Al amparo', 'Al amparo de + artículo + ley indica la base jurídica de la solicitud.'),
        ('El abajo firmante ______ recurso de reposición contra la Resolución de 3 de junio de 2026.', 'interpone', 'Interponer es el verbo formal para presentar un recurso administrativo.'),
        ('Por la presente se le ______ que dispone de quince días hábiles para recurrir.', 'notifica', 'Notificar es comunicar oficialmente una decisión o plazo administrativo.'),
        ('El director ______ que D. Luis García ha superado satisfactoriamente el proceso de selección.', 'certifica', 'Certificar hace constar oficialmente un hecho mediante la firma de la autoridad competente.'),
    ]),
    ex3=('Género institucional', 'Identifica a qué género institucional pertenece cada fragmento.', [
        ('«El abajo firmante interpone recurso de alzada contra la Resolución de 15 de mayo de 2026, por considerar que vulnera el artículo 14 de la Constitución.»', ['Notificación', 'Certificado', 'Recurso administrativo'], 'Recurso administrativo',
         '«Interpone recurso de alzada contra la Resolución» es la fórmula del recurso administrativo.'),
        ('«CERTIFICA que D. Martín López Gómez prestó servicios en esta entidad entre el 1 de enero y el 31 de diciembre de 2025.»', ['Recurso', 'Certificado', 'Notificación'], 'Certificado',
         'El verbo en mayúscula «CERTIFICA» y los datos precisos caracterizan el certificado oficial.'),
        ('«Por la presente se le notifica que su solicitud ha sido denegada y que dispone de un mes para interponer los recursos oportunos.»', ['Certificado', 'Notificación administrativa', 'Recurso'], 'Notificación administrativa',
         '«Por la presente se le notifica» es la fórmula característica de la notificación.'),
        ('«Declaro bajo mi responsabilidad que los datos aportados son verídicos y me comprometo a acreditarlos si fuera requerido.»', ['Notificación', 'Certificado', 'Declaración responsable'], 'Declaración responsable',
         '«Declaro bajo mi responsabilidad» es la fórmula de la declaración responsable.'),
    ]),
)

CHAPTERS['comentario-critico'] = dict(
    level='c1', section='writing', num='W06', short='El Comentario Crítico',
    title='El Comentario Crítico de Texto',
    subtitle='Integra análisis, interpretación y valoración con rigor y perspectiva',
    game_desc='Practica el comentario crítico integrado en español C1.',
    slides=[
        ('El comentario crítico integrado', None,
         '<p class="slide-explanation">El comentario crítico C1 integra análisis (qué dice y cómo), interpretación (qué significa) y valoración (qué tan sólido y eficaz es). No son pasos separados: se entrelazan.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Análisis:</b> identifica tesis, estructura, recursos</p>'
         '<p style="margin-top:6px"><b>Interpretación:</b> explica el significado e implicaciones del texto</p>'
         '<p style="margin-top:6px"><b>Valoración:</b> juzga la solidez de los argumentos y la eficacia retórica</p></div>'),
        ('La contextualización del texto', None,
         '<p class="slide-explanation">El comentario C1 contextualiza el texto en su marco histórico, cultural o ideológico. Esta perspectiva enriquece la interpretación.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Fórmulas:</b> «Este texto se inscribe en el debate sobre...» / «Escrito en el contexto de..., el autor...»</p>'
         '<p style="margin-top:8px"><b>Ejemplo:</b> «Este artículo se inscribe en el debate sobre la regulación de la IA que sacude los foros internacionales desde 2022.»</p></div>'),
        ('La integración de análisis e interpretación', None,
         '<p class="slide-explanation">En el comentario avanzado, el análisis del recurso va seguido inmediatamente de su interpretación: qué efecto produce y qué significa.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Análisis solo:</b> «El autor usa una metáfora.»</p>'
         '<p style="margin-top:8px"><b>Análisis + interpretación:</b> «El autor emplea la metáfora de la «jaula de oro» para sugerir que el bienestar material puede convertirse en una trampa que anula la libertad.»</p></div>'),
        ('La valoración argumentativa', None,
         '<p class="slide-explanation">La valoración evalúa si los argumentos son sólidos, si los recursos retóricos son eficaces y si hay limitaciones o falacias en el texto.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Fórmulas:</b></p>'
         '<p style="margin-top:6px">El argumento resulta convincente porque... / Si bien la tesis es sólida, la argumentación flaquea cuando...</p>'
         '<p style="margin-top:6px">El autor incurre en la falacia de... al afirmar que...</p>'
         '<p style="margin-top:6px">La eficacia retórica del texto reside en...</p></div>'),
        ('La conclusión del comentario', None,
         '<p class="slide-explanation">La conclusión del comentario crítico sintetiza el análisis, la interpretación y la valoración, y puede abrirse a una perspectiva más amplia.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Síntesis:</b> «En definitiva, el texto construye un argumento sólido que...»</p>'
         '<p style="margin-top:8px"><b>Perspectiva:</b> «...aunque su eficacia persuasiva depende de que el lector comparta ciertos presupuestos ideológicos.»</p></div>'),
    ],
    traps=[
        ('El texto trata de la IA.', 'Este texto <strong>se inscribe en el debate contemporáneo</strong> sobre la gobernanza de la inteligencia artificial, que ha cobrado urgencia desde la irrupción de los modelos generativos.', 'El comentario C1 contextualiza el texto, no solo resume su tema'),
        ('El autor usa una metáfora.', 'El autor emplea la metáfora de la «jaula de oro» para <strong>sugerir que el bienestar material puede anular la libertad</strong>.', 'Integra el análisis con su interpretación: qué efecto produce el recurso'),
        ('El texto es bueno.', 'La eficacia retórica del texto <strong>reside en la combinación de datos estadísticos y apelación emocional</strong>, que actúa sobre el intelecto y la sensibilidad del lector.', 'La valoración fundamenta el juicio con evidencia retórica específica'),
        ('En conclusión, el texto es interesante.', 'En definitiva, el texto construye un argumento sólido, aunque <strong>su eficacia persuasiva depende de que el lector ya comparta</strong> ciertos presupuestos ideológicos.', 'La conclusión del comentario C1 evalúa; no se limita a calificar vagamente'),
        ('El autor quiere convencer.', 'El autor apela a la autoridad científica mediante datos del IPCC para <strong>dotar de objetividad una tesis que, en su formulación política, es discutible</strong>.', 'Especifica qué estrategia usa el autor Y evalúa su legitimidad crítica'),
    ],
    summary=[
        ('Contextualización', 'el texto se inscribe en...', 'Este texto se inscribe en el debate sobre la regulación de la IA.'),
        ('Análisis + interpretación', 'recurso → significado/efecto', 'La metáfora de la «jaula de oro» sugiere que el bienestar puede anular la libertad.'),
        ('Valoración', 'el argumento resulta convincente porque...', 'El argumento es sólido porque combina datos del IPCC con una tesis coherente.'),
        ('Limitación', 'la argumentación flaquea cuando...', 'La tesis flaquea cuando generaliza a partir de un solo caso.'),
        ('Conclusión', 'síntesis + perspectiva', 'En definitiva, el texto es persuasivo, aunque presupone un lector ya convencido.'),
        ('Integración', 'análisis, interpretación y valoración entrelazados', 'No analizar primero y valorar después; integrar ambos niveles en cada párrafo.'),
    ],
    items=[
        ('comentario-critico', 'comentario crítico', 'género textual que integra análisis, interpretación y valoración de un texto de forma entrelazada', 'análisis valorativo',
         'El ______ va más allá del resumen: interpreta y evalúa los argumentos y recursos del texto.', 'coment', 'comentario crítico'),
        ('contextualizacion', 'contextualización', 'proceso de situar el texto en su marco histórico, cultural o ideológico para enriquecer la interpretación', 'encuadre',
         'La ______ indica el debate o el momento histórico en que se inscribe el texto.', 'context', 'contextualización'),
        ('interpretacion', 'interpretación', 'explicación del significado profundo y las implicaciones de los argumentos y recursos del texto', 'lectura profunda',
         'La ______ va más allá de describir el recurso: explica qué sugiere o implica.', 'interpret', 'interpretación'),
        ('valoracion-retorica', 'valoración retórica', 'juicio sobre la eficacia de los recursos persuasivos usados por el autor del texto', 'evaluación persuasiva',
         'La ______ identifica qué recursos funcionan bien y cuáles debilitan el argumento.', 'valor', 'valoración retórica'),
        ('eficacia-persuasiva', 'eficacia persuasiva', 'medida en que el texto logra convencer al lector mediante argumentos y recursos retóricos', 'poder de convicción',
         'La ______ del texto depende de la solidez de los argumentos y del registro elegido.', 'eficac', 'eficacia persuasiva'),
        ('presupuesto', 'presupuesto ideológico', 'idea o valor que el texto da por sentado sin justificarlo explícitamente', 'idea implícita',
         'El texto presupone que el crecimiento económico es siempre deseable, sin cuestionarlo.', 'presup', 'presupuesto ideológico'),
        ('síntesis-comentario', 'síntesis del comentario', 'conclusión que integra el análisis, la interpretación y la valoración en una evaluación global', 'cierre valorativo',
         'La ______ del comentario evalúa el texto globalmente sin limitarse a resumirlo.', 'síntesis', 'síntesis del comentario'),
        ('perspectiva-critica', 'perspectiva crítica', 'punto de vista desde el que se evalúa el texto, que puede ser ideológico, cultural o teórico', 'ángulo de análisis',
         'Adoptar una ______ feminista sobre el texto ilumina aspectos que el autor no menciona.', 'perspect', 'perspectiva crítica'),
    ],
    ex1=('El comentario crítico integrado', 'Elige la opción que muestra la práctica correcta del comentario crítico C1.', [
        ('¿Qué distingue el comentario crítico C1 del análisis de texto B2?', ['El C1 solo describe los recursos', 'El C1 integra análisis, interpretación y valoración de forma entrelazada', 'El C1 es más breve'], 'El C1 integra análisis, interpretación y valoración de forma entrelazada',
         'En C1, el análisis del recurso va inmediatamente seguido de su interpretación y valoración.'),
        ('¿Qué añade la contextualización al comentario?', ['Resume el texto', 'Sitúa el texto en su marco histórico o cultural para enriquecer la interpretación', 'Presenta la opinión del comentarista'], 'Sitúa el texto en su marco histórico o cultural para enriquecer la interpretación',
         'La contextualización explica en qué debate o momento se inscribe el texto.'),
        ('¿Cuál es la diferencia entre análisis e interpretación?', ['No hay diferencia', 'El análisis describe qué hace el texto; la interpretación explica qué significa', 'La interpretación es un resumen'], 'El análisis describe qué hace el texto; la interpretación explica qué significa',
         'El análisis identifica recursos; la interpretación explica su efecto y significado.'),
        ('¿Cuál es un ejemplo de valoración retórica fundamentada?', ['«El texto es muy bueno.»', '«La eficacia retórica reside en la combinación de datos y apelación emocional.»', '«El autor usa varias metáforas.»'], '«La eficacia retórica reside en la combinación de datos y apelación emocional.»',
         'La valoración fundamentada identifica qué recursos crean la eficacia y por qué funcionan.'),
        ('¿Qué es un presupuesto ideológico en un texto?', ['Una cita de autoridad', 'Una idea que el texto da por sentada sin justificarla', 'Un argumento explícito del autor'], 'Una idea que el texto da por sentada sin justificarla',
         'El presupuesto ideológico es una idea implícita que el texto asume como verdadera sin defenderla.'),
    ]),
    ex2=('Integrar análisis e interpretación', 'Completa con la interpretación que corresponde al análisis dado.', [
        ('El autor emplea la metáfora «la ciudad es una jungla» para ______.', 'sugerir que la vida urbana es violenta, impredecible y regida por la ley del más fuerte', 'La metáfora de la jungla asocia la ciudad con la ausencia de ley y la violencia natural.'),
        ('El texto se inscribe en el debate sobre ______ que ha cobrado urgencia desde la irrupción de los modelos generativos en 2022.', 'la regulación de la inteligencia artificial', 'La contextualización sitúa el texto en el debate contemporáneo sobre la IA.'),
        ('La eficacia persuasiva del texto reside en ______.', 'la combinación de datos estadísticos verificables y una apelación emocional que actúa sobre la sensibilidad del lector', 'La combinación de pathos y logos es una estrategia retórica eficaz.'),
        ('La argumentación flaquea cuando el autor ______.', 'generaliza a partir de un solo caso sin datos que lo respalden', 'Una generalización sin evidencia suficiente es una debilidad argumentativa.'),
    ]),
    ex3=('Nivel del comentario', 'Identifica si el fragmento corresponde al análisis, la interpretación o la valoración.', [
        ('«El autor emplea la anáfora «Hablamos de...» en tres frases consecutivas.»', ['Interpretación', 'Valoración', 'Análisis'], 'Análisis',
         'Identificar el recurso y su localización en el texto es el nivel del análisis.'),
        ('«Mediante la anáfora, el autor crea un efecto acumulativo que eleva el tono hasta convertir el argumento en un llamamiento moral.»', ['Análisis', 'Valoración', 'Interpretación'], 'Interpretación',
         'Explicar el efecto y el significado del recurso es el nivel de la interpretación.'),
        ('«El recurso es eficaz porque su ritmo hipnótico impide que el lector se detenga a cuestionar las premisas.»', ['Análisis', 'Interpretación', 'Valoración'], 'Valoración',
         'Juzgar si el recurso funciona y por qué es el nivel de la valoración retórica.'),
        ('«El texto incurre en la falacia de la apelación a la emoción al sustituir datos por imágenes impactantes.»', ['Análisis', 'Interpretación', 'Valoración'], 'Valoración',
         'Identificar una falacia y juzgar que debilita el argumento es una valoración crítica.'),
    ]),
)
