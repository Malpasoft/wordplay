# espanol_c2_w.py — Main Spanish C2 Writing — 5 chapters

CHAPTERS = {}

CHAPTERS['ensayo-academico'] = dict(
    level='c2', section='writing', num='W01', short='El Ensayo Académico C2',
    title='El Ensayo Académico C2',
    subtitle='Construye argumentos con matiz filosófico, rigor metodológico y elegancia',
    game_desc='Practica las estrategias del ensayo académico de nivel C2.',
    slides=[
        ('La complejidad argumentativa en C2', None,
         '<p class="slide-explanation">El ensayo C2 opera en varios registros simultáneamente: es riguroso en el análisis, matizado en las conclusiones y elegante en la expresión. La certeza absoluta es un signo de simpleza; el matiz, de dominio.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Jerarquía argumentativa:</b> argumento principal → argumentos de apoyo → concesiones → refutaciones</p>'
         '<p style="margin-top:8px"><b>Matiz C2:</b> «Esto es verdad bajo ciertas condiciones, pero...»</p>'
         '<p style="margin-top:8px"><b>Certeza vs probabilidad:</b> «está demostrado que» vs «cabe defender que»</p></div>'),
        ('La intertextualidad densa', None,
         '<p class="slide-explanation">El ensayo C2 dialoga con otros textos y pensadores de forma integrada, no como ornamento sino como parte del argumento.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Diálogo con fuentes:</b> No es «Chomsky dice que...» sino «La posición de Chomsky sobre la gramática universal arroja luz sobre la distinción entre...»</p>'
         '<p style="margin-top:8px"><b>Discrepancia con fuente:</b> «Si bien Bourdieu identifica el capital cultural como reproductor de desigualdad, su análisis subestima la agencia individual.»</p></div>'),
        ('La hipótesis de trabajo y las limitaciones', None,
         '<p class="slide-explanation">El ensayo C2 explicita sus hipótesis, su alcance y sus limitaciones. Esta transparencia es una señal de rigor, no de debilidad.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Hipótesis:</b> «Este ensayo parte de la hipótesis de que la desigualdad educativa no se reduce a factores económicos.»</p>'
         '<p style="margin-top:8px"><b>Alcance:</b> «El análisis se circunscribe al contexto de los países de la OCDE.»</p>'
         '<p style="margin-top:8px"><b>Limitaciones:</b> «Una limitación de este enfoque es que...»</p></div>'),
        ('El estilo: densidad sin oscuridad', None,
         '<p class="slide-explanation">El ensayo C2 es denso en ideas pero no oscuro en expresión. Cada oración lleva su peso pero no más de lo que puede soportar.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Incorrecto (oscuro):</b> «La hipostatización fetichizada de las relaciones mercantiles produce una inversión alienante de la subjetividad.»</p>'
         '<p style="margin-top:8px"><b>Correcto (denso pero claro):</b> «El mercado convierte las relaciones sociales en transacciones, borrando su dimensión humana.»</p></div>'),
        ('La conclusión C2: apertura epistemológica', None,
         '<p class="slide-explanation">La conclusión C2 no solo sintetiza y proyecta; abre nuevas preguntas que el ensayo no puede responder, mostrando que el tema es más grande que el texto.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Síntesis:</b> «El análisis realizado permite concluir que...»</p>'
         '<p style="margin-top:8px"><b>Apertura:</b> «Quedan, sin embargo, cuestiones pendientes que exceden el alcance de este trabajo: ¿cómo influye X en Y?, ¿es universalizable esta conclusión?»</p></div>'),
    ],
    traps=[
        ('Es obvio que Chomsky tiene razón.', 'La posición de Chomsky <strong>ofrece un marco productivo</strong>, aunque su alcance universal ha sido cuestionado por enfoques cognitivos más recientes.', 'El diálogo con fuentes en C2 es crítico, no reverencial'),
        ('El tema es muy complejo. Hay muchas opiniones.', 'La complejidad del fenómeno <strong>se articula en torno a tres tensiones irresolubles</strong>: individual/colectivo, eficiencia/equidad, presente/futuro.', 'Organiza la complejidad en tensiones analíticas, no la uses como excusa para no concluir'),
        ('En conclusión, hemos visto que...', 'El análisis realizado permite concluir que...; <strong>quedan, sin embargo, cuestiones que exceden este marco</strong>: ¿cómo afecta X a Y?', 'La conclusión C2 sintetiza Y abre preguntas; no repite lo «visto»'),
        ('Karl Marx dijo que el capitalismo explota a los trabajadores.', 'En el análisis marxista, <strong>la acumulación de capital reproduce sistemáticamente</strong> las condiciones de explotación del trabajo.', 'Integra la idea del pensador en el argumento; no la presentes como simple cita'),
        ('Mi hipótesis es correcta.', 'Los datos analizados <strong>son consistentes con la hipótesis</strong> de partida, aunque no permiten excluir explicaciones alternativas.', 'C2 modaliza las conclusiones: consistente con ≠ prueba definitiva'),
    ],
    summary=[
        ('Hipótesis', 'este ensayo parte de la hipótesis de que...', 'La hipótesis: la desigualdad no se reduce a factores económicos.'),
        ('Intertextualidad crítica', 'si bien X sostiene... su análisis subestima...', 'Bourdieu identifica el capital cultural, pero subestima la agencia individual.'),
        ('Densidad sin oscuridad', 'ideas complejas, expresión clara', '«El mercado borra la dimensión humana de las relaciones» > jerga opaca.'),
        ('Matiz epistémico', 'los datos son consistentes con...', 'Los datos son consistentes con la hipótesis, aunque no la prueban definitivamente.'),
        ('Apertura', 'quedan cuestiones que exceden este marco', '¿Es universalizable esta conclusión? ¿Cómo afecta X a Y?'),
        ('Alcance', 'el análisis se circunscribe a...', 'El análisis se circunscribe a los países de la OCDE entre 2010 y 2025.'),
    ],
    items=[
        ('hipotesis', 'hipótesis de trabajo', 'afirmación provisional que el ensayo se propone defender o explorar mediante el análisis', 'premisa central',
         'La ______ del ensayo delimita el alcance y orienta el análisis desde el primer párrafo.', 'hipót', 'hipótesis de trabajo'),
        ('intertextualidad-critica', 'intertextualidad crítica', 'diálogo con otras fuentes que no solo las cita sino que discrepa de ellas o las reinterpreta', 'diálogo bibliográfico',
         'La ______ señala dónde el autor discrepa de Bourdieu y por qué.', 'intertex', 'intertextualidad crítica'),
        ('matiz-epistemico', 'matiz epistémico', 'distinción entre grados de certeza: demostrado, probable, consistente con, cuestionable', 'gradación de certeza',
         'El ______ «los datos son consistentes con» evita afirmar más de lo que permite la evidencia.', 'matiz', 'matiz epistémico'),
        ('apertura', 'apertura epistemológica', 'señalamiento de preguntas que el ensayo no puede responder, mostrando que el tema supera el texto', 'apertura de debate',
         'La ______ de la conclusión demuestra que el autor reconoce los límites de su análisis.', 'apert', 'apertura epistemológica'),
        ('jerarquia', 'jerarquía argumentativa', 'organización de los argumentos por orden de relevancia, de principal a secundario', 'estructura argumentativa',
         'La ______ sitúa el argumento más fuerte en la posición más destacada del ensayo.', 'jerarq', 'jerarquía argumentativa'),
        ('alcance', 'alcance del análisis', 'delimitación explícita de los límites temáticos, temporales o geográficos del ensayo', 'delimitación',
         'El ______ «países de la OCDE, 2010-2025» acota el campo de aplicación de las conclusiones.', 'alcanc', 'alcance del análisis'),
        ('densidad', 'densidad conceptual', 'característica de un texto que presenta muchas ideas de forma precisa sin resultar oscuro', 'complejidad clara',
         'La ______ del ensayo C2 combina profundidad de ideas con claridad de expresión.', 'densi', 'densidad conceptual'),
        ('agencia', 'agencia individual', 'capacidad del sujeto para actuar de forma autónoma y modificar su entorno a pesar de las estructuras sociales', 'autonomía del sujeto',
         'La ______ es el factor que Bourdieu subestima en su análisis del capital cultural.', 'agenc', 'agencia individual'),
    ],
    ex1=('Ensayo académico C2', 'Elige la opción que refleja el dominio del ensayo C2.', [
        ('¿Cómo se integra una fuente en el ensayo C2?', ['«Chomsky dice que...»', '«La posición de Chomsky ilumina la distinción entre competencia y actuación lingüística.»', '«Según Chomsky, la gramática es innata.»'], '«La posición de Chomsky ilumina la distinción entre competencia y actuación lingüística.»',
         'En C2, la fuente se integra en el argumento; no se cita sino que se interpreta.'),
        ('¿Qué hace la apertura epistemológica en la conclusión?', ['Resume los argumentos del ensayo', 'Señala preguntas que el ensayo no puede responder', 'Presenta la tesis por primera vez'], 'Señala preguntas que el ensayo no puede responder',
         'La apertura muestra que el tema supera el ensayo, señalando futuras líneas de investigación.'),
        ('¿Qué es la densidad conceptual?', ['Un texto lleno de jerga incomprensible', 'Muchas ideas presentadas con claridad sin oscurantismo', 'Un texto muy largo'], 'Muchas ideas presentadas con claridad sin oscurantismo',
         'La densidad C2 es conceptual, no verbal: ideas complejas expresadas con precisión y claridad.'),
        ('¿Cuál es la función de la hipótesis de trabajo?', ['Presentar una conclusión definitiva', 'Delimitar el alcance y orientar el análisis del ensayo', 'Citar una fuente externa'], 'Delimitar el alcance y orientar el análisis del ensayo',
         'La hipótesis indica qué se va a defender o explorar y en qué condiciones.'),
        ('¿Qué expresa el matiz epistémico «los datos son consistentes con»?', ['Certeza absoluta de la hipótesis', 'Los datos apoyan la hipótesis sin probarla definitivamente', 'Los datos refutan la hipótesis'], 'Los datos apoyan la hipótesis sin probarla definitivamente',
         '«Consistente con» es más honesto que «demuestra»: los datos apoyan sin probar definitivamente.'),
    ]),
    ex2=('Expresión C2', 'Completa con la expresión más adecuada para el nivel C2.', [
        ('La posición de Bourdieu ______ luz sobre la reproducción de la desigualdad cultural.', 'arroja', 'Arrojar luz sobre es una expresión más sofisticada que «explica» o «habla de».'),
        ('El análisis se ______ al contexto de los países de la OCDE entre 2010 y 2025.', 'circunscribe', 'Circunscribirse a delimita el alcance del análisis con precisión formal.'),
        ('Los datos son ______ con la hipótesis, aunque no permiten excluir explicaciones alternativas.', 'consistentes', 'Consistente con expresa el matiz epistémico adecuado: apoyo sin prueba definitiva.'),
        ('Quedan cuestiones que ______ el alcance de este trabajo: ¿cómo influye X en Y?', 'exceden', 'Exceder el alcance señala la apertura epistemológica de la conclusión C2.'),
    ]),
    ex3=('C2 vs C1: nivel de sofisticación', 'Elige la formulación que corresponde al nivel C2 (no al C1).', [
        ('Al citar a un pensador:', ['«Bourdieu dice que el capital cultural reproduce la desigualdad.»', '«El análisis de Bourdieu ilumina los mecanismos de reproducción de la desigualdad, aunque subestima la agencia individual.»'], '«El análisis de Bourdieu ilumina los mecanismos de reproducción de la desigualdad, aunque subestima la agencia individual.»',
         'El C2 integra la fuente críticamente; el C1 la cita. La discrepancia con Bourdieu es la marca C2.'),
        ('Al concluir el ensayo:', ['«En conclusión, hemos visto que la desigualdad es un problema complejo.»', '«El análisis realizado sugiere que la desigualdad educativa obedece a factores estructurales e individuales; quedan, sin embargo, preguntas que exceden este marco.»'], '«El análisis realizado sugiere que la desigualdad educativa obedece a factores estructurales e individuales; quedan, sin embargo, preguntas que exceden este marco.»',
         'La conclusión C2 sintetiza con matiz epistémico y abre preguntas; no repite ni simplifica.'),
        ('Al limitar el alcance:', ['«No puedo hablar de todo.»', '«El análisis se circunscribe al contexto de los países de la OCDE entre 2010 y 2025, por lo que sus conclusiones no son directamente extrapolables a otras regiones.»'], '«El análisis se circunscribe al contexto de los países de la OCDE entre 2010 y 2025, por lo que sus conclusiones no son directamente extrapolables a otras regiones.»',
         'El C2 delimita el alcance con precisión técnica; el C1 puede hacerlo de forma más general.'),
    ]),
)

CHAPTERS['analisis-literario'] = dict(
    level='c2', section='writing', num='W02', short='El Análisis Literario',
    title='El Análisis Literario C2',
    subtitle='Interpreta textos literarios con perspectiva teórica y sensibilidad estética',
    game_desc='Practica el análisis literario avanzado en español C2.',
    slides=[
        ('La especificidad del análisis literario', None,
         '<p class="slide-explanation">El análisis literario C2 no solo identifica recursos: los interpreta en relación con el sentido global de la obra, su contexto histórico y los debates teóricos que iluminan su lectura.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Tres niveles:</b> textual (qué dice), formal (cómo lo dice), ideológico (qué implica)</p>'
         '<p style="margin-top:8px"><b>Contexto:</b> época, corriente literaria, posición del autor</p>'
         '<p style="margin-top:8px"><b>Perspectiva teórica:</b> estructuralismo, feminismo, poscolonialismo, marxismo cultural...</p></div>'),
        ('La ironía y la ambigüedad literaria', None,
         '<p class="slide-explanation">La gran literatura a menudo resiste lecturas únicas. El análisis C2 reconoce y explica la ambigüedad como una riqueza, no como un defecto.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Ironía dramática:</b> el lector sabe algo que el personaje ignora</p>'
         '<p style="margin-top:8px"><b>Ambigüedad semántica:</b> una imagen puede interpretarse de dos formas igualmente válidas</p>'
         '<p style="margin-top:8px"><b>Fórmula:</b> «Esta imagen admite al menos dos lecturas: por un lado... por otro...»</p></div>'),
        ('El análisis de la voz y el punto de vista', None,
         '<p class="slide-explanation">La voz narrativa y el punto de vista determinan qué podemos saber y cuánto podemos confiar en lo que se nos cuenta.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Narrador no fiable:</b> narrador cuya perspectiva está distorsionada por su psicología o sus intereses</p>'
         '<p style="margin-top:8px"><b>Ejemplo:</b> «El narrador presenta los hechos como un triunfo; sin embargo, el lector atento percibe los síntomas de su autoengaño.»</p></div>'),
        ('La intertextualidad literaria', None,
         '<p class="slide-explanation">La intertextualidad literaria identifica las fuentes, los modelos y las reescrituras que enriquecen la obra analizada.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Alusión:</b> referencia implícita a otra obra que enriquece el significado</p>'
         '<p style="margin-top:8px"><b>Parodia:</b> reescritura que transforma el modelo con distancia crítica o humorística</p>'
         '<p style="margin-top:8px"><b>Palimpsesto:</b> la obra se escribe «sobre» otra anterior que sigue visible</p></div>'),
        ('La perspectiva teórica como herramienta', None,
         '<p class="slide-explanation">Una perspectiva teórica ilumina aspectos del texto que una lectura neutral pasaría por alto. En C2, se usa la teoría como herramienta, no como dogma.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Lectura feminista:</b> cómo se construye el género en el texto</p>'
         '<p style="margin-top:8px"><b>Lectura poscolonial:</b> cómo se representa el «otro» colonial</p>'
         '<p style="margin-top:8px"><b>Fórmula:</b> «Una lectura feminista del texto revela que...»</p></div>'),
    ],
    traps=[
        ('El autor usa muchos recursos literarios.', 'El autor emplea la ironía dramática para <strong>generar una distancia entre lo que el lector sabe y lo que el personaje cree</strong>, intensificando el efecto trágico.', 'Integra análisis e interpretación: nombra el recurso, explica su efecto y su función en el texto'),
        ('El texto es ambiguo, no se entiende bien.', 'La ambigüedad semántica de la imagen final <strong>admite dos lecturas igualmente válidas</strong>: la redención del personaje o su definitiva condena.', 'La ambigüedad no es falta de comprensión; es una riqueza que el análisis C2 explica'),
        ('El narrador cuenta la historia.', 'El narrador, cuya perspectiva está <strong>distorsionada por el autoengaño</strong>, presenta los hechos como un triunfo que el lector atento reconoce como fracaso.', 'Evalúa la fiabilidad del narrador y su efecto en la experiencia lectora'),
        ('El libro fue escrito en el siglo XX.', 'El texto <strong>se inscribe en el existencialismo literario</strong> de mediados del siglo XX y dialoga con la visión sartreana de la libertad como condena.', 'La contextualización en C2 conecta el texto con la corriente literaria e ideológica específica'),
        ('Una lectura feminista diría que la mujer está oprimida.', 'Una lectura feminista del texto revela cómo <strong>el silencio de la protagonista funciona como forma de resistencia</strong> ante las expectativas patriarcales.', 'La lectura teórica en C2 es específica: qué mecanismo concreto ilumina la teoría en este texto'),
    ],
    summary=[
        ('Ironía dramática', 'el lector sabe lo que el personaje ignora', 'El lector sabe que el narrador miente, aunque el personaje lo crea.'),
        ('Narrador no fiable', 'perspectiva distorsionada por psicología o interés', 'El narrador presenta su fracaso como triunfo: es un narrador no fiable.'),
        ('Ambigüedad', 'dos lecturas válidas simultáneas', 'La imagen admite dos lecturas: redención o condena definitiva.'),
        ('Intertextualidad', 'alusión, parodia, palimpsesto', 'El texto es un palimpsesto del Quijote: reescritura crítica del original.'),
        ('Perspectiva teórica', 'feminista / poscolonial / marxista', 'Una lectura poscolonial revela cómo se exotiza al personaje indígena.'),
        ('Tres niveles', 'textual + formal + ideológico', 'Nivel textual: la trama. Formal: la ironía. Ideológico: la crítica al poder.'),
    ],
    items=[
        ('ironia-dramatica', 'ironía dramática', 'recurso por el que el lector conoce información que el personaje ignora, creando distancia y tensión', 'ironía situacional',
         'La ______ revela al lector el engaño del protagonista antes de que este lo descubra.', 'ironía', 'ironía dramática'),
        ('narrador-no-fiable', 'narrador no fiable', 'narrador cuya perspectiva está distorsionada por su psicología, sus intereses o su limitado conocimiento', 'narrador sesgado',
         'El ______ presenta su fracaso como un éxito, lo que el lector atento detecta.', 'narr', 'narrador no fiable'),
        ('ambiguedad-literaria', 'ambigüedad literaria', 'característica de un texto que admite dos o más lecturas igualmente válidas sin que una cancele a la otra', 'polisemia textual',
         'La ______ del final del cuento no es un defecto; es la fuente de su riqueza interpretativa.', 'ambig', 'ambigüedad literaria'),
        ('palimpsesto', 'palimpsesto', 'texto que se escribe «sobre» otro anterior, cuya huella sigue siendo visible en la reescritura', 'reescritura',
         'La novela es un ______ del Quijote: reescribe el mito del héroe con ironía posmoderna.', 'palim', 'palimpsesto'),
        ('perspectiva-teorica', 'perspectiva teórica', 'marco interpretativo (feminismo, marxismo, poscolonialismo) que ilumina aspectos específicos del texto', 'enfoque crítico',
         'Una ______ feminista del texto revela cómo el silencio de la protagonista es resistencia.', 'perspect', 'perspectiva teórica'),
        ('nivel-ideologico', 'nivel ideológico', 'dimensión del análisis que examina qué valores, poder e ideología construye o reproduce el texto', 'capa ideológica',
         'El ______ del texto revela cómo la novela naturaliza la jerarquía de clases.', 'nivel', 'nivel ideológico'),
        ('alusión', 'alusión literaria', 'referencia implícita a otra obra o figura que enriquece el significado sin nombrarse explícitamente', 'referencia velada',
         'La ______ a Penélope evoca la espera y la fidelidad sin necesidad de citar a Homero.', 'alus', 'alusión literaria'),
        ('corriente-literaria', 'corriente literaria', 'movimiento o tendencia estética compartida por un grupo de autores en una época determinada', 'movimiento literario',
         'El texto se inscribe en el realismo mágico, ______ asociada a la narrativa latinoamericana del siglo XX.', 'corriente', 'corriente literaria'),
    ],
    ex1=('Análisis literario C2', 'Elige la opción que refleja el dominio del análisis literario en C2.', [
        ('¿Qué es un narrador no fiable?', ['Un narrador que no conoce el final de la historia', 'Un narrador cuya perspectiva está distorsionada por su psicología o sus intereses', 'Un narrador en primera persona'], 'Un narrador cuya perspectiva está distorsionada por su psicología o sus intereses',
         'El narrador no fiable presenta una versión de los hechos que el lector atento reconoce como sesgada o engañosa.'),
        ('¿Cómo trata la ambigüedad el análisis C2?', ['La considera un defecto del texto', 'La interpreta como una riqueza que admite dos o más lecturas válidas', 'La ignora y elige una sola interpretación'], 'La interpreta como una riqueza que admite dos o más lecturas válidas',
         'En C2, la ambigüedad no es un problema de comprensión: es una característica que el análisis explica.'),
        ('¿Cuál es la diferencia entre la ironía y la ironía dramática?', ['Son sinónimos exactos', 'La ironía dramática es la que conoce el lector pero no el personaje', 'La ironía dramática solo aparece en el teatro'], 'La ironía dramática es la que conoce el lector pero no el personaje',
         'La ironía dramática crea tensión porque el lector ve lo que el personaje no puede ver.'),
        ('¿Qué es un palimpsesto literario?', ['Un texto que no tiene fuentes', 'Un texto que se escribe «sobre» otro anterior cuya huella sigue visible', 'Un tipo de narrador omnisciente'], 'Un texto que se escribe «sobre» otro anterior cuya huella sigue visible',
         'El palimpsesto es una reescritura que transforma el modelo original manteniéndolo como referencia.'),
        ('¿Cómo se usa la perspectiva teórica en el análisis C2?', ['Como un dogma que determina la interpretación', 'Como una herramienta que ilumina aspectos específicos del texto', 'Como sustituto del análisis textual'], 'Como una herramienta que ilumina aspectos específicos del texto',
         'En C2, la teoría es un instrumento de análisis, no una ideología que se aplica mecánicamente.'),
    ]),
    ex2=('Términos del análisis literario', 'Completa con el término adecuado.', [
        ('El narrador presenta su propio fracaso como un triunfo. Es un narrador ______.', 'no fiable', 'El narrador no fiable distorsiona los hechos por su psicología o sus intereses.'),
        ('El texto reescribe el Quijote con ironía posmoderna. Es un ______.', 'palimpsesto', 'El palimpsesto escribe «sobre» un texto anterior cuya huella sigue siendo visible.'),
        ('La referencia implícita a Penélope evoca la espera sin citar a Homero. Es una ______.', 'alusión literaria', 'La alusión enriquece el significado sin nombrar explícitamente la fuente.'),
        ('Una ______ feminista del texto revela cómo el silencio de la protagonista es una forma de resistencia.', 'perspectiva teórica', 'La perspectiva teórica ilumina aspectos del texto que una lectura neutral pasaría por alto.'),
    ]),
    ex3=('Nivel de análisis', 'Identifica a qué nivel de análisis pertenece cada fragmento.', [
        ('«La novela narra la historia de un exiliado que regresa a su país veinte años después.»', ['Nivel formal', 'Nivel textual', 'Nivel ideológico'], 'Nivel textual',
         'Describir la trama o el argumento es el nivel textual del análisis.'),
        ('«El autor emplea el monólogo interior para revelar la disociación entre la voz pública y la conciencia privada del protagonista.»', ['Nivel textual', 'Nivel ideológico', 'Nivel formal'], 'Nivel formal',
         'Analizar el recurso narrativo (monólogo interior) y su efecto es el nivel formal.'),
        ('«Una lectura poscolonial revela que la representación del personaje indígena reproduce el exotismo colonial que la novela pretende criticar.»', ['Nivel textual', 'Nivel formal', 'Nivel ideológico'], 'Nivel ideológico',
         'Examinar qué ideología construye o contradice el texto es el nivel ideológico.'),
        ('«La ambigüedad del final admite dos lecturas: la reconciliación o la ironía definitiva sobre la imposibilidad del regreso.»', ['Nivel textual', 'Nivel formal + interpretativo', 'Nivel ideológico'], 'Nivel formal + interpretativo',
         'Identificar la ambigüedad y ofrecer dos interpretaciones combina el nivel formal con el interpretativo.'),
    ]),
)

CHAPTERS['texto-expositivo'] = dict(
    level='c2', section='writing', num='W03', short='El Texto Expositivo',
    title='El Texto Expositivo C2',
    subtitle='Expón conocimientos complejos con claridad, precisión y estructura ejemplar',
    game_desc='Practica la exposición académica de temas complejos en español C2.',
    slides=[
        ('La exposición de alto nivel', None,
         '<p class="slide-explanation">El texto expositivo C2 hace accesible lo complejo sin simplificarlo. La claridad no es ausencia de profundidad: es el dominio de articular lo difícil con precisión.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Principio C2:</b> la dificultad del tema no justifica la oscuridad de la expresión</p>'
         '<p style="margin-top:8px"><b>Herramienta clave:</b> la definición operativa + el ejemplo ilustrativo + la distinción conceptual</p></div>'),
        ('La definición operativa', None,
         '<p class="slide-explanation">En el texto expositivo avanzado, los conceptos se definen con precisión para que el lector sepa exactamente qué entiende el autor por cada término.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Fórmula:</b> «Por X entendemos aquí...» / «En el sentido en que lo usamos, X designa...»</p>'
         '<p style="margin-top:8px"><b>Distinción:</b> «No hay que confundir X con Y: mientras X designa..., Y se refiere a...»</p></div>'),
        ('La articulación conceptual', None,
         '<p class="slide-explanation">La articulación conceptual conecta ideas abstractas con ejemplos concretos y establece las relaciones entre los conceptos: causa, consecuencia, contraste, inclusión.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Causa:</b> este fenómeno se debe a / tiene su origen en</p>'
         '<p style="margin-top:8px"><b>Consecuencia:</b> de ello se sigue que / esto conlleva que</p>'
         '<p style="margin-top:8px"><b>Inclusión:</b> X es un caso particular de Y / X forma parte del conjunto más amplio de Z</p></div>'),
        ('La objetividad y la perspectiva', None,
         '<p class="slide-explanation">El texto expositivo C2 es objetivo pero no neutro: selecciona qué explicar y cómo. El autor muestra su perspectiva a través de qué elige incluir y enfatizar.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Énfasis:</b> cabe subrayar que / conviene destacar que / es crucial señalar que</p>'
         '<p style="margin-top:8px"><b>Perspectiva implícita:</b> qué se omite revela tanto como lo que se incluye</p></div>'),
        ('El cierre expositivo C2', None,
         '<p class="slide-explanation">El cierre del texto expositivo C2 sintetiza las ideas clave y puede señalar implicaciones o proyecciones sin convertirse en un ensayo de opinión.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Síntesis:</b> «En suma, los tres factores analizados (X, Y, Z) permiten comprender...»</p>'
         '<p style="margin-top:8px"><b>Proyección neutra:</b> «El estudio de este fenómeno abre la vía a investigaciones sobre...»</p></div>'),
    ],
    traps=[
        ('La globalización es cuando los países se relacionan entre sí.', 'Por globalización <strong>entendemos aquí el proceso de integración económica, cultural y política</strong> que ha intensificado la interdependencia entre estados desde la década de 1980.', 'La definición operativa en C2 es precisa, histórica y delimitada'),
        ('Es complicado de explicar.', 'Este fenómeno puede articularse en torno a dos dimensiones interrelacionadas: <strong>la estructural y la subjetiva</strong>.', 'En C2 no hay temas demasiado complicados: los descompones en dimensiones y las explicas con orden'),
        ('También hay que mencionar otros factores.', '<strong>Cabe añadir, en este punto, que</strong> los factores institucionales modulan el impacto de las causas estructurales.', 'Articula cada adición con un marcador preciso que indique la relación lógica'),
        ('En conclusión, es un tema muy amplio.', 'En suma, los tres factores analizados —económico, cultural e institucional— <strong>permiten comprender la complejidad del fenómeno</strong> sin reducirlo a una sola causa.', 'El cierre expositivo C2 sintetiza articulando los factores; no constata la amplitud del tema'),
        ('No hay que confundir globalización con internacionalización.', 'No hay que confundir globalización con internacionalización: <strong>mientras la primera implica una integración profunda que desdibuja las fronteras</strong>, la segunda designa simplemente la extensión de relaciones entre estados soberanos.', 'La distinción conceptual en C2 define las diferencias con precisión y simetría'),
    ],
    summary=[
        ('Definición operativa', 'por X entendemos aquí...', 'Por globalización entendemos el proceso de integración económica iniciado en los 80.'),
        ('Distinción conceptual', 'no hay que confundir X con Y', 'Globalización ≠ internacionalización: la primera desdibuja fronteras, la segunda no.'),
        ('Articulación', 'de ello se sigue / esto conlleva', 'De ello se sigue que la interdependencia aumenta la vulnerabilidad ante crisis globales.'),
        ('Énfasis', 'cabe subrayar / conviene destacar', 'Cabe subrayar que el factor institucional actúa como modulador de las causas estructurales.'),
        ('Síntesis', 'en suma, los factores X, Y, Z permiten comprender...', 'En suma, los tres factores permiten comprender la complejidad del fenómeno.'),
        ('Dimensiones', 'descomponer en dimensiones para explicar', 'El fenómeno tiene dos dimensiones: la estructural y la subjetiva.'),
    ],
    items=[
        ('definicion-operativa', 'definición operativa', 'delimitación precisa del sentido en que se usa un concepto en un texto académico concreto', 'definición de trabajo',
         'La ______ «por globalización entendemos aquí...» acota el término para este análisis.', 'defin', 'definición operativa'),
        ('distincion-conceptual', 'distinción conceptual', 'diferenciación precisa entre dos conceptos relacionados que podrían confundirse', 'delimitación de conceptos',
         'La ______ entre globalización e internacionalización evita la confusión terminológica.', 'distinct', 'distinción conceptual'),
        ('articulacion', 'articulación conceptual', 'conexión explícita entre ideas mediante marcadores de causa, consecuencia, contraste o inclusión', 'conexión lógica',
         'La ______ «de ello se sigue que» conecta el análisis con su implicación lógica.', 'articul', 'articulación conceptual'),
        ('enfasis', 'énfasis expositivo', 'señalamiento de las ideas que el autor considera más importantes mediante fórmulas especiales', 'subrayado',
         '«Cabe subrayar que» es una fórmula de ______ que destaca la idea más relevante.', 'énfas', 'énfasis expositivo'),
        ('dimension', 'dimensión analítica', 'aspecto o plano de un fenómeno complejo que se analiza de forma separada para facilitar la comprensión', 'plano de análisis',
         'El fenómeno se articula en dos ______: la estructural y la subjetiva.', 'dimen', 'dimensión analítica'),
        ('exposicion', 'texto expositivo', 'texto que presenta y explica información sobre un tema de forma objetiva y organizada', 'texto informativo',
         'El ______ C2 hace accesible lo complejo sin simplificarlo ni oscurecerlo.', 'expos', 'texto expositivo'),
        ('sintesis-expositiva', 'síntesis expositiva', 'párrafo final que recoge los elementos principales analizados y sus relaciones sin opinar', 'cierre expositivo',
         'La ______ articula los factores X, Y, Z sin reducir el fenómeno a una sola causa.', 'síntesis', 'síntesis expositiva'),
        ('implicacion', 'implicación', 'consecuencia o significado que se sigue de los hechos expuestos sin que el autor lo diga explícitamente', 'consecuencia lógica',
         'La ______ del análisis es que la interdependencia global aumenta la vulnerabilidad ante crisis.', 'implic', 'implicación'),
    ],
    ex1=('Texto expositivo C2', 'Elige la opción que refleja el dominio del texto expositivo en C2.', [
        ('¿Qué es una definición operativa?', ['Una definición de diccionario', 'La delimitación precisa del sentido en que se usa un concepto en el texto concreto', 'Una definición filosófica universal'], 'La delimitación precisa del sentido en que se usa un concepto en el texto concreto',
         'La definición operativa delimita el término para el análisis específico, no para todos los contextos.'),
        ('¿Qué hace la articulación conceptual?', ['Resume el texto', 'Conecta ideas mediante relaciones lógicas: causa, consecuencia, contraste', 'Cita fuentes externas'], 'Conecta ideas mediante relaciones lógicas: causa, consecuencia, contraste',
         'La articulación usa marcadores precisos («de ello se sigue», «esto conlleva») para conectar ideas.'),
        ('¿Cómo se diferencia el texto expositivo C2 del C1?', ['Es más corto', 'Opera con definiciones operativas, distinciones conceptuales y articulación más sofisticada', 'No tiene estructura'], 'Opera con definiciones operativas, distinciones conceptuales y articulación más sofisticada',
         'El C2 explicita el sentido de cada término y articula las relaciones lógicas con mayor precisión.'),
        ('¿Cuál es la función del énfasis expositivo?', ['Expresar la opinión del autor', 'Señalar las ideas que el autor considera más importantes del análisis', 'Introducir una cita'], 'Señalar las ideas que el autor considera más importantes del análisis',
         '«Cabe subrayar que» y «conviene destacar que» orientan al lector hacia los puntos clave.'),
        ('¿Por qué se descompone un fenómeno en dimensiones?', ['Para hacerlo más largo', 'Para facilitar el análisis de aspectos complejos de forma ordenada', 'Para evitar las conclusiones'], 'Para facilitar el análisis de aspectos complejos de forma ordenada',
         'La descomposición en dimensiones permite analizar la complejidad sin perder la coherencia.'),
    ]),
    ex2=('Expresión expositiva C2', 'Completa con la fórmula expositiva adecuada.', [
        ('______ globalización entendemos aquí el proceso de integración económica que intensifica la interdependencia.', 'Por', 'Por X entendemos aquí... es la fórmula de la definición operativa.'),
        ('______ confundir globalización con internacionalización: la primera desdibuja fronteras; la segunda, no.', 'No hay que', 'No hay que confundir X con Y introduce la distinción conceptual.'),
        ('______ ello se sigue que la interdependencia aumenta la vulnerabilidad ante crisis globales.', 'De', 'De ello se sigue que conecta el análisis con su implicación lógica.'),
        ('______ subrayar que el factor institucional actúa como modulador de las causas estructurales.', 'Cabe', 'Cabe subrayar que es una fórmula de énfasis expositivo.'),
    ]),
    ex3=('Articulación lógica', 'Identifica qué relación lógica expresa cada marcador.', [
        ('«Este fenómeno tiene su origen en la desregulación financiera de los años ochenta.»', ['Consecuencia', 'Causa', 'Distinción'], 'Causa',
         '«Tiene su origen en» expresa la causa del fenómeno analizado.'),
        ('«De ello se sigue que la interdependencia global aumenta la vulnerabilidad ante crisis sistémicas.»', ['Causa', 'Consecuencia', 'Distinción'], 'Consecuencia',
         '«De ello se sigue que» introduce la consecuencia lógica del análisis.'),
        ('«La globalización ≠ internacionalización: mientras la primera integra profundamente, la segunda solo extiende relaciones.»', ['Consecuencia', 'Inclusión', 'Distinción conceptual'], 'Distinción conceptual',
         'Definir qué no es X (no confundir con Y) establece una distinción conceptual.'),
        ('«X es un caso particular de Y, que a su vez forma parte del conjunto más amplio de Z.»', ['Causa', 'Consecuencia', 'Inclusión jerárquica'], 'Inclusión jerárquica',
         '«Es un caso particular de» establece una relación de inclusión entre los conceptos.'),
    ]),
)

CHAPTERS['discurso'] = dict(
    level='c2', section='writing', num='W04', short='El Discurso',
    title='El Discurso — Oratoria y escritura retórica',
    subtitle='Escribe y estructura discursos con fuerza retórica y dominio de la persuasión',
    game_desc='Practica la escritura de discursos con recursos retóricos avanzados.',
    slides=[
        ('El discurso como género total', None,
         '<p class="slide-explanation">El discurso integra todos los géneros: argumenta (ensayo), narra (relato), expone (texto académico) y apela emocionalmente (poesía). El dominio del discurso en C2 es la cumbre de la competencia retórica.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Ethos:</b> autoridad y credibilidad del orador</p>'
         '<p style="margin-top:6px"><b>Pathos:</b> apelación a la emoción del auditorio</p>'
         '<p style="margin-top:6px"><b>Logos:</b> argumento racional y datos</p></div>'),
        ('La estructura clásica del discurso', None,
         '<p class="slide-explanation">La retórica clásica organizaba el discurso en cinco partes que siguen siendo útiles hoy.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>1. Exordio:</b> captar la atención y la benevolencia del público</p>'
         '<p style="margin-top:4px"><b>2. Narratio:</b> exposición de los hechos</p>'
         '<p style="margin-top:4px"><b>3. Argumentatio:</b> pruebas y argumentos</p>'
         '<p style="margin-top:4px"><b>4. Refutatio:</b> rebatir los argumentos contrarios</p>'
         '<p style="margin-top:4px"><b>5. Peroratio:</b> conclusión apelativa y llamada a la acción</p></div>'),
        ('El exordio: gancho y posicionamiento', None,
         '<p class="slide-explanation">El exordio debe captar la atención en los primeros segundos y establecer la credibilidad del orador. En la escritura del discurso, esto equivale al primer párrafo.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Tipos de exordio:</b> pregunta provocadora / anécdota / dato impactante / paradoja</p>'
         '<p style="margin-top:8px"><b>Ejemplo:</b> «Hace setenta años, en este mismo edificio, se firmó el tratado que debía acabar con todas las guerras. Hoy estamos aquí porque no acabó con ninguna.»</p></div>'),
        ('El pathos y la apelación emocional legítima', None,
         '<p class="slide-explanation">El pathos es poderoso y legítimo cuando apoya argumentos racionales; es manipulador cuando los sustituye. El discurso C2 combina logos y pathos de forma ética.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Pathos legítimo:</b> la emoción acompaña al argumento racional</p>'
         '<p style="margin-top:8px"><b>Pathos manipulador:</b> la emoción sustituye al argumento</p>'
         '<p style="margin-top:8px"><b>Recursos:</b> anáfora, paralelismo, pregunta retórica, imagen vívida</p></div>'),
        ('La peroratio: llamada a la acción', None,
         '<p class="slide-explanation">La peroratio cierra el discurso con fuerza. Resume los argumentos y moviliza al auditorio hacia una acción o actitud.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Fórmulas:</b> «El momento de actuar es ahora.» / «La historia nos juzgará por lo que hagamos hoy.»</p>'
         '<p style="margin-top:8px"><b>Recursos finales:</b> tricolon («libertad, justicia, memoria»), anáfora, pregunta retórica</p></div>'),
    ],
    traps=[
        ('Hoy voy a hablar de la educación.', '<strong>Hace veinte años</strong>, uno de cada cinco niños en este país no terminaba la educación básica. Hoy seguimos aquí, discutiendo si es posible cambiar esa cifra.', 'El exordio del discurso no anuncia el tema; lo golpea con un dato, una paradoja o una anécdota'),
        ('La gente sufre mucho y es muy triste.', 'Los datos hablan de cifras; <strong>detrás de cada cifra hay una familia</strong> que ha tenido que elegir entre pagar el alquiler y comprar los libros de texto.', 'El pathos legítimo humaniza los datos; no sustituye el argumento por la emoción'),
        ('En conclusión, debemos actuar ya.', 'La historia <strong>no nos preguntará si teníamos miedo</strong>; nos preguntará qué hicimos a pesar de él. <strong>El momento de actuar es hoy.</strong>', 'La peroratio del discurso cierra con fuerza retórica, no con una frase genérica'),
        ('Además, también hay otro problema que es importante.', 'A este argumento <strong>se suma un segundo, igualmente decisivo</strong>: la desigualdad en el acceso a la tecnología.', 'La transición entre argumentos del discurso usa marcadores de adición precisos y valorativos'),
        ('Quiero decir que es urgente actuar.', '<strong>Es urgente actuar</strong> porque cada año que pasa son doscientas mil familias más que no pueden costear la educación de sus hijos.', 'El discurso no anuncia lo que «quiere decir»; lo dice directamente con datos que lo justifican'),
    ],
    summary=[
        ('Ethos', 'autoridad y credibilidad del orador', 'El orador establece su ethos al citar su experiencia directa con el problema.'),
        ('Pathos', 'apelación emocional que acompaña al argumento', 'Detrás de cada cifra hay una familia: el pathos humaniza el dato.'),
        ('Logos', 'argumento racional y datos', 'El logos: el 20 % de los niños no termina la educación básica.'),
        ('Exordio', 'gancho que capta la atención', 'El tratado de hace setenta años que no acabó con ninguna guerra.'),
        ('Peroratio', 'llamada a la acción con fuerza retórica', 'La historia nos juzgará por lo que hagamos hoy.'),
        ('Tricolon', 'tres elementos en paralelo', '«Libertad, justicia, memoria» — el poder del número tres.'),
    ],
    items=[
        ('ethos', 'ethos', 'dimensión retórica que construye la autoridad y la credibilidad del orador ante el auditorio', 'autoridad del orador',
         'El orador establece su ______ citando su experiencia directa con el problema.', 'ethos', 'ethos'),
        ('pathos', 'pathos', 'dimensión retórica que apela a las emociones del auditorio para hacerlo más receptivo al argumento', 'apelación emocional',
         'El ______ legítimo acompaña al argumento racional; el manipulador lo sustituye.', 'pathos', 'pathos'),
        ('logos', 'logos', 'dimensión retórica basada en el argumento racional, los datos y la lógica', 'argumento racional',
         'El ______ del discurso incluye datos estadísticos verificables y razonamientos lógicos.', 'logos', 'logos'),
        ('exordio', 'exordio', 'parte inicial del discurso que capta la atención y establece la credibilidad del orador', 'introducción del discurso',
         'El ______ impacta con un dato, una paradoja o una anécdota desde la primera frase.', 'exord', 'exordio'),
        ('peroratio', 'peroratio', 'parte final del discurso que sintetiza el argumento y moviliza al auditorio hacia la acción', 'cierre del discurso',
         'La ______ cierra con fuerza retórica: «la historia nos juzgará por lo que hagamos hoy».', 'perorat', 'peroratio'),
        ('tricolon', 'tricolon', 'figura retórica que enumera tres elementos en paralelo para crear un ritmo poderoso', 'serie de tres',
         'El ______ «libertad, justicia, memoria» condensa el mensaje en tres términos de peso igual.', 'tricol', 'tricolon'),
        ('paralelismo', 'paralelismo', 'figura retórica que repite la misma estructura sintáctica en frases sucesivas para crear ritmo e impacto', 'estructura paralela',
         'El ______ «luchamos para vivir, luchamos para aprender, luchamos para existir» acumula fuerza.', 'parali', 'paralelismo'),
        ('peroratio-accion', 'llamada a la acción', 'frase o párrafo final que moviliza al auditorio hacia un comportamiento concreto', 'movilización del auditorio',
         'La ______ «el momento de actuar es hoy» cierra el discurso con energía movilizadora.', 'llamada', 'llamada a la acción'),
    ],
    ex1=('El discurso retórico', 'Elige la respuesta correcta sobre la escritura de discursos en C2.', [
        ('¿Qué es el ethos en la retórica clásica?', ['La apelación a las emociones del público', 'La autoridad y la credibilidad del orador', 'Los datos y argumentos racionales'], 'La autoridad y la credibilidad del orador',
         'El ethos es la dimensión retórica que construye la credibilidad del orador ante el auditorio.'),
        ('¿Cuándo es legítimo el pathos?', ['Cuando sustituye al argumento racional', 'Cuando acompaña al argumento racional y lo humaniza', 'Cuando se usa en lugar de datos'], 'Cuando acompaña al argumento racional y lo humaniza',
         'El pathos es legítimo cuando humaniza los datos; manipulador cuando los sustituye.'),
        ('¿Cuál es la función del exordio?', ['Presentar todos los argumentos', 'Captar la atención y establecer la credibilidad del orador', 'Refutar el argumento contrario'], 'Captar la atención y establecer la credibilidad del orador',
         'El exordio es el gancho inicial que abre el discurso con impacto y establece el ethos.'),
        ('¿Qué es un tricolon?', ['Una estructura de tres partes del discurso', 'Una figura retórica que enumera tres elementos en paralelo', 'Un tipo de anáfora'], 'Una figura retórica que enumera tres elementos en paralelo',
         'El tricolon («libertad, justicia, memoria») crea un ritmo poderoso mediante la serie de tres.'),
        ('¿Cuál es la función de la peroratio?', ['Exponer los hechos objetivamente', 'Cerrar el discurso sintetizando y movilizando al auditorio', 'Refutar los argumentos contrarios'], 'Cerrar el discurso sintetizando y movilizando al auditorio',
         'La peroratio es el cierre retórico que deja al auditorio listo para actuar.'),
    ]),
    ex2=('Recursos del discurso', 'Identifica o completa el recurso retórico.', [
        ('«Hace setenta años se firmó el tratado que debía acabar con todas las guerras. Hoy estamos aquí porque no acabó con ninguna.» Es el ______ del discurso.', 'exordio', 'El exordio usa una paradoja histórica para captar la atención desde la primera frase.'),
        ('«La historia no nos preguntará si teníamos miedo; nos preguntará qué hicimos a pesar de él.» Es una ______.', 'peroratio', 'La peroratio cierra con una frase de fuerza retórica que moviliza al auditorio.'),
        ('«Luchamos por la educación. Luchamos por la igualdad. Luchamos, en fin, por el futuro.» Es una ______.', 'anáfora', 'La anáfora repite «luchamos por» al inicio de cada frase para crear ritmo acumulativo.'),
        ('«Libertad, justicia, dignidad.» Es un ______.', 'tricolon', 'El tricolon enumera tres elementos en paralelo para crear un ritmo poderoso y memorable.'),
    ]),
    ex3=('Ethos, pathos, logos', 'Identifica qué dimensión retórica usa cada fragmento.', [
        ('«Llevo treinta años trabajando en este campo. He visto las consecuencias de la inacción.»', ['Pathos', 'Logos', 'Ethos'], 'Ethos',
         'Citar la experiencia propia construye la autoridad del orador: es ethos.'),
        ('«El 23 % de los niños en este país vive por debajo del umbral de la pobreza, según UNICEF (2025).»', ['Ethos', 'Pathos', 'Logos'], 'Logos',
         'Un dato estadístico verificable de una fuente reconocida es logos.'),
        ('«Detrás de ese 23 % hay una niña que no puede hacer los deberes porque no hay luz en su casa.»', ['Logos', 'Ethos', 'Pathos'], 'Pathos',
         'La imagen concreta y humana que apela a la compasión del auditorio es pathos.'),
        ('«¿Podemos permitirnos ignorar esta realidad? ¿Podemos mirar hacia otro lado?»', ['Logos', 'Ethos', 'Pathos'], 'Pathos',
         'La pregunta retórica que apela a la conciencia moral del auditorio es un recurso de pathos.'),
    ]),
)

CHAPTERS['escritura-creativa'] = dict(
    level='c2', section='writing', num='W05', short='La Escritura Creativa',
    title='La Escritura Creativa C2',
    subtitle='Escribe con plena autonomía estilística y voz literaria propia',
    game_desc='Practica la escritura creativa con dominio estilístico en español C2.',
    slides=[
        ('La voz literaria propia', None,
         '<p class="slide-explanation">En C2, la escritura creativa no imita modelos: los ha asimilado y los ha superado para crear una voz propia. La voz de autor es el conjunto de elecciones estilísticas que definen la escritura de una persona.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Elementos de la voz:</b> registro, ritmo, vocabulario elegido, perspectiva, temas recurrentes</p>'
         '<p style="margin-top:8px"><b>Ejercicio C2:</b> reescribir el mismo episodio desde tres registros distintos</p></div>'),
        ('La elipsis y lo no dicho', None,
         '<p class="slide-explanation">Lo que no se dice es tan importante como lo que se dice. La elipsis y el silencio narrativo son técnicas de maestría que crean densidad e invitan a la participación del lector.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Elipsis narrativa:</b> salta sobre un período de tiempo sin narrarlo</p>'
         '<p style="margin-top:8px"><b>Silencio significativo:</b> lo que el personaje no dice revela más que sus palabras</p>'
         '<p style="margin-top:8px"><b>Ejemplo:</b> «Se despidieron. Tres años después, ella lo vio en el andén de la estación de Lyon.» (Los tres años: elipsis)</p></div>'),
        ('La imagen central y el principio de economía', None,
         '<p class="slide-explanation">La escritura creativa C2 selecciona: un detalle preciso vale más que una descripción exhaustiva. El principio de economía dicta que cada palabra justifica su presencia.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Imagen central:</b> un detalle concreto que condensa el significado</p>'
         '<p style="margin-top:8px"><b>Economía:</b> sin adjetivos ornamentales, sin adverbios innecesarios</p>'
         '<p style="margin-top:8px"><b>Ejemplo pobre:</b> «Era una noche muy oscura y tremendamente fría.»</p>'
         '<p style="margin-top:8px"><b>Ejemplo rico:</b> «La escarcha había cubierto los cristales. Nadie en la calle.»</p></div>'),
        ('El punto de vista y la distancia narrativa', None,
         '<p class="slide-explanation">Elegir el punto de vista correcto es una decisión fundamental. La distancia narrativa (cuánto sabe el narrador, cuánta emoción muestra) determina el tono del texto.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Cercanía máxima:</b> flujo de conciencia, monólogo interior</p>'
         '<p style="margin-top:8px"><b>Distancia máxima:</b> narrador frío, casi periodístico</p>'
         '<p style="margin-top:8px"><b>Distancia media:</b> tercera persona con acceso a la conciencia de un personaje</p></div>'),
        ('La revisión como parte del proceso creativo', None,
         '<p class="slide-explanation">En C2, la escritura creativa implica múltiples revisiones. Escribir es reescribir: la primera versión es el material, no el producto final.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Preguntas de revisión:</b></p>'
         '<p style="margin-top:6px">¿Cada palabra justifica su presencia? ¿El ritmo sirve al tono? ¿Lo no dicho funciona?</p>'
         '<p style="margin-top:6px">¿La imagen central es lo bastante precisa? ¿El punto de vista es coherente?</p></div>'),
    ],
    traps=[
        ('Era una noche muy oscura y tremendamente fría.', 'La escarcha había cubierto los cristales. <strong>Nadie en la calle.</strong>', 'Un detalle preciso y una frase nominal crean más atmósfera que dos adjetivos vagos'),
        ('El personaje sentía muchas emociones encontradas.', 'Apoyó la frente en el cristal frío. <strong>No dijo nada.</strong>', 'Muestra la emoción a través de un gesto concreto; no la nombres'),
        ('De repente, todo cambió para siempre a partir de ese momento.', '<strong>Tres años después</strong>, ella lo vio en el andén de la estación de Lyon.', 'La elipsis narrativa salta el tiempo con una sola frase; no lo announces ni lo expliques'),
        ('El narrador explicó lo que pensaba el personaje con detalle.', 'Cerró la puerta. <strong>¿Qué haría con todo ese silencio?</strong>', 'El pensamiento del personaje en forma de pregunta es más vívido que su exposición indirecta'),
        ('Escribió una historia larga y detallada con muchos adjetivos.', 'Reescribió la primera versión eliminando <strong>la mitad de los adjetivos</strong> y todos los adverbios innecesarios.', 'La revisión C2 aplica el principio de economía: cada palabra debe justificarse'),
    ],
    summary=[
        ('Voz de autor', 'registro, ritmo, vocabulario, perspectiva', 'La voz de autor es reconocible incluso sin el nombre del escritor.'),
        ('Elipsis', 'salta el tiempo en una frase', '«Tres años después...» — la elipsis condensa el paso del tiempo.'),
        ('Economía', 'cada palabra justifica su presencia', 'Un detalle preciso vale más que una descripción exhaustiva.'),
        ('Mostrar, no decir', 'emoción a través de gesto o imagen', 'No «sentía tristeza»: «apoyó la frente en el cristal frío».'),
        ('Distancia narrativa', 'cercanía / distancia / media', 'Flujo de conciencia = cercanía máxima; narrador frío = distancia máxima.'),
        ('Revisión', 'reescribir es parte del proceso', '¿Cada palabra es necesaria? ¿El ritmo sirve al tono?'),
    ],
    items=[
        ('voz-literaria', 'voz literaria', 'conjunto de elecciones estilísticas (registro, ritmo, vocabulario, perspectiva) que definen la escritura de un autor', 'estilo personal',
         'La ______ de un escritor es reconocible incluso sin que aparezca su nombre.', 'voz', 'voz literaria'),
        ('elipsis-narrativa', 'elipsis narrativa', 'salto temporal en el relato que omite un período de tiempo sin narrarlo explícitamente', 'salto temporal',
         'La ______ «tres años después» condensa el paso del tiempo en tres palabras.', 'elipsis', 'elipsis narrativa'),
        ('economia-narrativa', 'economía narrativa', 'principio estilístico según el cual cada palabra debe justificar su presencia en el texto', 'principio de economía',
         'La ______ dicta eliminar los adjetivos ornamentales y los adverbios innecesarios.', 'econom', 'economía narrativa'),
        ('mostrar-no-decir', 'mostrar, no decir', 'principio de escritura creativa que expresa las emociones mediante gestos e imágenes concretas en lugar de nombrarlas', 'show, don\'t tell',
         'El principio «______» prefiere «apoyó la frente en el cristal» a «sentía tristeza».', 'mostrar', 'mostrar, no decir'),
        ('distancia-narrativa', 'distancia narrativa', 'grado de proximidad entre el narrador y la conciencia de los personajes, que determina el tono del texto', 'perspectiva narrativa',
         'La ______ máxima es el flujo de conciencia; la mínima, el narrador frío y periodístico.', 'distan', 'distancia narrativa'),
        ('flujo-conciencia', 'flujo de conciencia', 'técnica narrativa que reproduce el pensamiento del personaje en su forma más directa e ininterrumpida', 'monólogo interior',
         'El ______ de Joyce en el Ulises imita la asociación libre del pensamiento humano.', 'flujo', 'flujo de conciencia'),
        ('revision', 'revisión creativa', 'proceso de reescritura que aplica los principios de economía, ritmo y coherencia de voz al texto inicial', 'reescritura',
         'La ______ elimina la mitad de los adjetivos y comprueba que cada frase gana su lugar.', 'revis', 'revisión creativa'),
        ('imagen-central', 'imagen central', 'detalle concreto y preciso que condensa el significado de una escena o de todo el relato', 'imagen nuclear',
         'La ______ «la escarcha en los cristales» crea más atmósfera que varios adjetivos vagos.', 'imagen', 'imagen central'),
    ],
    ex1=('Escritura creativa C2', 'Elige la opción que refleja el dominio de la escritura creativa en C2.', [
        ('¿Qué es la elipsis narrativa?', ['Una figura de estilo que repite palabras', 'Un salto temporal que omite un período sin narrarlo', 'Un tipo de narrador'], 'Un salto temporal que omite un período sin narrarlo',
         'La elipsis salta sobre el tiempo con una sola frase («tres años después»).'),
        ('¿Qué significa «mostrar, no decir»?', ['Usar descripciones largas y detalladas', 'Expresar emociones mediante gestos e imágenes concretas en lugar de nombrarlas', 'Evitar las emociones en el texto'], 'Expresar emociones mediante gestos e imágenes concretas en lugar de nombrarlas',
         '«Apoyó la frente en el cristal» muestra la tristeza sin decir «estaba triste».'),
        ('¿Qué es el principio de economía narrativa?', ['Escribir textos cortos', 'Cada palabra debe justificar su presencia; eliminar lo ornamental', 'Usar solo sustantivos y verbos'], 'Cada palabra debe justificar su presencia; eliminar lo ornamental',
         'La economía exige revisar y eliminar lo que no añade significado o ritmo.'),
        ('¿Qué es la voz literaria de un autor?', ['El tema recurrente de sus obras', 'El conjunto de elecciones estilísticas que hacen reconocible su escritura', 'La longitud media de sus frases'], 'El conjunto de elecciones estilísticas que hacen reconocible su escritura',
         'La voz es el resultado de múltiples elecciones: registro, ritmo, vocabulario, perspectiva.'),
        ('¿Cuál es la función de la revisión creativa?', ['Corregir las faltas de ortografía', 'Aplicar los principios de economía, ritmo y coherencia de voz al texto inicial', 'Añadir más descripción'], 'Aplicar los principios de economía, ritmo y coherencia de voz al texto inicial',
         'La revisión C2 es una reescritura profunda que aplica criterios estilísticos, no solo ortográficos.'),
    ]),
    ex2=('Técnica creativa', 'Identifica la técnica o el principio aplicado en cada ejemplo.', [
        ('«Se despidieron. Tres años después, ella lo vio en el andén.» El salto de tres años es una ______.', 'elipsis narrativa', 'La elipsis omite tres años de historia en una sola frase.'),
        ('«Apoyó la frente en el cristal frío. No dijo nada.» Expresa tristeza sin nombrarla: es ______.', 'mostrar, no decir', 'El gesto concreto muestra la emoción sin decir «estaba triste».'),
        ('«La escarcha había cubierto los cristales. Nadie en la calle.» Crea atmósfera con precisión: es ______.', 'imagen central', 'Un detalle preciso vale más que una lista de adjetivos vagos.'),
        ('«¿Qué haría con todo ese silencio?» Es el pensamiento del personaje expresado como ______.', 'flujo de conciencia', 'La pregunta directa reproduce el pensamiento interno del personaje.'),
    ]),
    ex3=('Principio de economía', 'Identifica cuál de las dos versiones aplica mejor el principio de economía narrativa.', [
        ('Versión A: «Era una noche tremendamente oscura y muy fría y llovía con mucha fuerza.» / Versión B: «Llovía. El frío.»', ['Versión A', 'Versión B'], 'Versión B',
         'La versión B elimina adjetivos redundantes y crea un ritmo más tenso con frases nominales.'),
        ('Versión A: «El personaje sentía una profunda tristeza en su interior.» / Versión B: «Cerró los ojos. Respiró.»', ['Versión A', 'Versión B'], 'Versión B',
         'Los gestos concretos muestran la emoción sin nombrarla: principio de «mostrar, no decir».'),
        ('Versión A: «Se despidieron y luego pasaron tres largos años durante los cuales no se vieron.» / Versión B: «Se despidieron. Tres años después, la vio en el andén.»', ['Versión A', 'Versión B'], 'Versión B',
         'La elipsis de la versión B es más elegante y económica que la explicación de la versión A.'),
    ]),
)
