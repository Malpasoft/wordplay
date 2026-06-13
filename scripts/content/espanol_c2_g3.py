# espanol_c2_g3.py — Main Spanish C2 grammar G11-G15
# G11: topicalizacion, G12: intensificacion, G13: variacion-linguistica,
# G14: pragmatica-espanol, G15: creatividad-lexica

CHAPTERS = {}

# ---------------------------------------------------------------------------
# G11: TOPICALIZACIÓN Y ÉNFASIS DISCURSIVO
# ---------------------------------------------------------------------------
CHAPTERS['topicalizacion'] = dict(
    level='c2', section='grammar', num='G11',
    short='Topicalización',
    title='Topicalización y Énfasis Discursivo',
    subtitle='Domina la dislocación, la focalización y el orden de palabras para articular el discurso',
    game_desc='Topicalización: dislocación, focalización contrastiva, clivadas y orden de palabras',
    summary=[
        ('Topicalización', 'Anteponer un elemento para convertirlo en tópico: <em>A María, la llamaron ayer</em>', 'A este libro, ya lo leí'),
        ('Dislocación a la izquierda', 'El tópico queda fuera de la oración principal; el pronombre lo retoma: <em>El informe, lo presento yo</em>', 'La reunión, la cancelaron sin avisar'),
        ('Dislocación a la derecha', 'El pronombre va primero; el tópico se añade al final: <em>Lo leyó entero, el documento</em>', 'La llamó dos veces, a su madre'),
        ('Focalización contrastiva', '<em>No</em> + constituyente + <em>sino</em> / énfasis prosódico: <em>No llegó tarde ELLA, sino él</em>', 'No compraron el rojo, sino el azul'),
        ('Eco y clivadas de foco', 'Oraciones escindidas de foco estrecho: <em>Fue ANA quien resolvió el problema</em>', 'Es en julio cuando mejor se vive aquí'),
        ('Orden VS y pasivas temáticas', 'El español admite VS libre para topicalizar el sujeto semántico: <em>Llegaron los resultados</em>', 'Se publicaron tres estudios al respecto'),
    ],
    slides=[
        ('Topicalización en español', None,
         '<p>La <strong>topicalización</strong> traslada un elemento a posición inicial para marcarlo como <em>tópico</em> (de qué trata la oración). Es frecuente en el discurso oral y escrito formal.</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Estrategia</th><th style="padding:6px 10px;text-align:left">Ejemplo</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Dislocación izquierda</td><td style="padding:5px 10px"><em>El libro, ya lo he leído</em></td></tr>'
         '<tr><td style="padding:5px 10px">Dislocación derecha</td><td style="padding:5px 10px"><em>Ya lo he leído, el libro</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">VS temático</td><td style="padding:5px 10px"><em>Llegaron los resultados</em></td></tr>'
         '</tbody></table>'),
        ('Focalización contrastiva', None,
         '<p>La <strong>focalización contrastiva</strong> destaca un constituyente frente a otra alternativa. Se marca con énfasis prosódico o con la construcción <em>no… sino</em>.</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Recurso</th><th style="padding:6px 10px;text-align:left">Ejemplo</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">no… sino</td><td style="padding:5px 10px"><em>No lo dijo ella, sino él</em></td></tr>'
         '<tr><td style="padding:5px 10px">Clivada de foco</td><td style="padding:5px 10px"><em>Fue Ana quien lo resolvió</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Énfasis léxico</td><td style="padding:5px 10px"><em>ELLA llegó tarde, no yo</em></td></tr>'
         '</tbody></table>'),
        ('Clíticos de retoma', None,
         '<p>En la dislocación, el clítico (<em>lo, la, le, los…</em>) retoma obligatoriamente al tópico nominal:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Tópico</th><th style="padding:6px 10px;text-align:left">Oración</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">OD femenino</td><td style="padding:5px 10px"><em>A María, <u>la</u> llamaron ayer</em></td></tr>'
         '<tr><td style="padding:5px 10px">OD masculino</td><td style="padding:5px 10px"><em>El informe, ya <u>lo</u> presento</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">OI</td><td style="padding:5px 10px"><em>A tus padres, <u>les</u> mandé flores</em></td></tr>'
         '</tbody></table>'),
        ('Orden de palabras y discurso', None,
         '<p>El español flexible permite varios órdenes para articular la estructura tema–rema:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Orden</th><th style="padding:6px 10px;text-align:left">Efecto</th><th style="padding:6px 10px;text-align:left">Ejemplo</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">SVO</td><td style="padding:5px 10px">Neutro</td><td style="padding:5px 10px"><em>El juez firmó la sentencia</em></td></tr>'
         '<tr><td style="padding:5px 10px">VS</td><td style="padding:5px 10px">Sujeto como rema</td><td style="padding:5px 10px"><em>Firmó la sentencia el juez</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">OVS</td><td style="padding:5px 10px">OD topicalizado</td><td style="padding:5px 10px"><em>La sentencia la firmó el juez</em></td></tr>'
         '</tbody></table>'),
    ],
    traps=[
        ('*A María llamaron ayer', 'A María la llamaron ayer', 'El clítico de retoma (<em>la</em>) es obligatorio cuando el OD humano está topicalizado a la izquierda.'),
        ('*No ella llegó tarde, sino él', 'No llegó tarde ella, sino él', 'La focalización contrastiva coloca el constituyente enfatizado junto a <em>sino</em>; no se antepone sin más al verbo.'),
        ('*El libro lo ya he leído', 'El libro ya lo he leído', 'El clítico de retoma precede inmediatamente al verbo conjugado; los adverbios van antes del clítico.'),
        ('*Fue Ana la que resolvió el problema (con pasiva refleja)', 'Fue Ana quien resolvió el problema', 'La clivada de foco usa <em>quien/que</em> sin la voz pasiva refleja; <em>fue…la que</em> es incorrecto en este contexto.'),
        ('*Lo leí entero el libro ayer', 'Lo leí entero ayer, el libro', 'En la dislocación a la derecha el tópico va al final absoluto de la enunciación, tras todos los complementos.'),
    ],
    items=[
        dict(term='topicalización', definition='Traslado de un constituyente a posición inicial para marcarlo como tópico del discurso', example='El informe, lo entregué esta mañana', accept=['topicalizacion']),
        dict(term='dislocación a la izquierda', definition='Construcción en la que el tópico precede a la cláusula principal y un clítico lo retoma', example='A esa película, ya la vi tres veces', accept=['dislocacion izquierda', 'left dislocation']),
        dict(term='dislocación a la derecha', definition='Construcción en la que el pronombre va primero y el tópico se añade al final', example='Lo terminé anoche, el informe', accept=['dislocacion derecha', 'right dislocation']),
        dict(term='focalización contrastiva', definition='Estrategia que destaca un elemento frente a una alternativa, con no… sino o énfasis prosódico', example='No lo dijo ella, sino él', accept=['focalizacion contrastiva']),
        dict(term='clítico de retoma', definition='Pronombre átono que coreferencializa el tópico en las construcciones dislocadas', example='A María la llamaron ayer (la = María)', accept=['clitico retoma', 'pronombre retoma']),
        dict(term='orden VS', definition='Orden verbo–sujeto que en español presenta el sujeto como información nueva (rema)', example='Llegaron los resultados esta tarde', accept=['orden verbo sujeto']),
        dict(term='oración clivada', definition='Construcción escindida que focaliza un constituyente: ser + X + que/quien', example='Fue Ana quien presentó el proyecto', accept=['clivada', 'oracion clivada']),
        dict(term='tema–rema', definition='Estructura informativa: el tema es lo conocido, el rema es la información nueva', example='(Tema) El director (Rema) ha dimitido esta mañana', accept=['tema rema', 'topic comment']),
    ],
    ex1=dict(
        title='Identifica la estrategia de topicalización',
        questions=[
            ('¿Qué estrategia se usa en: «El informe, lo presento yo mañana»?',
             ['Dislocación a la derecha', 'Dislocación a la izquierda', 'Focalización no… sino', 'Orden VS'],
             1, 'El constituyente <em>el informe</em> está antepuesto y el clítico <em>lo</em> lo retoma dentro de la oración → dislocación a la izquierda.'),
            ('¿Cuál es el efecto del orden VS en «Llegaron los estudiantes»?',
             ['Topicaliza el sujeto como tema conocido', 'Presenta el sujeto como información nueva (rema)', 'Marca foco contrastivo', 'Crea una oración clivada'],
             1, 'En español el sujeto pospuesto al verbo es típicamente remático (información nueva); aquí <em>los estudiantes</em> es la novedad.'),
            ('Elige la oración gramaticalmente correcta:',
             ['*A María llamaron ayer', 'A María la llamaron ayer', 'A María le llamaron ayer', 'A María lo llamaron ayer'],
             1, 'El objeto directo humano topicalizado exige el clítico de retoma concordado en género: <em>la</em> (femenino).'),
            ('¿Cuál es una oración clivada?',
             ['No ella sino él llegó tarde', 'Fue ella quien llegó tarde', 'Ella llegó tarde, no él', 'Llegó tarde, ella'],
             1, 'La estructura <em>fue + X + quien</em> es la clivada canónica de foco en español.'),
            ('En la dislocación a la derecha: «Lo leyó, el informe», ¿qué función tiene <em>el informe</em>?',
             ['Sujeto remático', 'Tópico pospuesto', 'Objeto directo en posición neutra', 'Complemento circunstancial'],
             1, 'En la dislocación derecha el constituyente final (<em>el informe</em>) es el tópico coreferencializado por el clítico <em>lo</em>.'),
        ]
    ),
    ex2=dict(
        title='Reformula con topicalización',
        questions=[
            ('Reescribe con dislocación a la izquierda: «Presenté ese informe ayer».',
             'Ese informe lo presenté ayer',
             ['ese informe lo presenté ayer', 'ese informe, lo presenté ayer'],
             'El OD <em>ese informe</em> se antepone y el clítico <em>lo</em> lo retoma: <em>Ese informe, lo presenté ayer</em>.'),
            ('Crea una oración clivada que focalice a «María» en: «María ganó el premio».',
             'Fue María quien ganó el premio',
             ['fue maría quien ganó el premio', 'fue maria quien gano el premio'],
             'La clivada canónica: <em>Fue + X + quien + verbo</em> → <em>Fue María quien ganó el premio</em>.'),
            ('Reformula con foco contrastivo (no… sino): «Ella llegó tarde, no él».',
             'No llegó tarde él, sino ella',
             ['no llegó tarde él sino ella', 'no llego tarde el sino ella'],
             'La estructura <em>no… sino</em> contrapone los dos sujetos; el orden más natural es <em>No llegó tarde él, sino ella</em>.'),
        ]
    ),
    ex3=dict(
        title='Elige la opción correcta en contexto',
        questions=[
            ('En un texto formal, ¿cuál de estas opciones topicaliza mejor el OD «el presupuesto»?',
             ['El presupuesto presentamos ayer', 'El presupuesto, lo presentamos ayer', 'El presupuesto presentó ayer', 'Lo presentamos ayer el presupuesto'],
             1, 'La dislocación a la izquierda con clítico (<em>El presupuesto, lo presentamos ayer</em>) es la construcción correcta y habitual.'),
            ('Para expresar que fue Ana —y no otra persona— quien resolvió el problema, usarías:',
             ['Ana resolvió el problema, no otra', 'No otra sino Ana resolvió', 'Fue Ana quien resolvió el problema', 'Ana, la que resolvió el problema'],
             2, 'La clivada <em>Fue Ana quien…</em> es el recurso estándar de focalización de sujeto en español culto.'),
            ('¿Cuál es el tópico en «A ese libro ya le tengo mucho cariño»?',
             ['Ya', 'Mucho cariño', 'A ese libro', 'Le'],
             2, '<em>A ese libro</em> está antepuesto y el clítico <em>le</em> lo retoma dentro de la cláusula → es el tópico.'),
            ('¿Qué construcción presenta el verbo antes que el sujeto para remantizarlo?',
             ['SVO estándar', 'Topicalización izquierda', 'Orden VS', 'Clivada de foco'],
             2, 'El orden VS presenta el sujeto como información nueva (rema); el verbo va primero.'),
        ]
    ),
)

# ---------------------------------------------------------------------------
# G12: INTENSIFICACIÓN Y ATENUACIÓN PRAGMÁTICAS
# ---------------------------------------------------------------------------
CHAPTERS['intensificacion'] = dict(
    level='c2', section='grammar', num='G12',
    short='Intensificación y Atenuación',
    title='Intensificación y Atenuación Pragmáticas',
    subtitle='Usa con precisión recursos de énfasis y suavización en el discurso oral y escrito',
    game_desc='Intensificación y atenuación: superlativo, adverbios, condicional de cortesía, impersonalización',
    summary=[
        ('Intensificadores léxicos', 'Adverbios (<em>muy, sumamente, extraordinariamente</em>), prefijos (<em>super-, ultra-, archi-</em>)', 'un argumento sumamente sólido'),
        ('Intensificación gramatical', 'Superlativo absoluto (-ísimo), aumentativos, reduplicación: <em>riquísimo, grandote, muy muy</em>', 'un problema gravísimo'),
        ('Atenuantes léxicos', '<em>un poco, algo, cierto, relativamente, en cierta medida</em>', 'el resultado es algo decepcionante'),
        ('Atenuación modal', 'Condicional cortés, impersonalización, modo subjuntivo: <em>querría, se podría decir, cabría considerar</em>', 'Cabría revisar este punto'),
        ('Función pragmática', 'Intensificar: implicar énfasis, emoción, evidencia. Atenuar: preservar la imagen, reducir imposición, matizar', 'Fue un éxito rotundo vs. Fue un éxito relativo'),
        ('Registro', 'La intensificación coloquial usa recursos distintos al registro formal: <em>mogollón, súper, brutal</em> (col.) vs. <em>extraordinariamente</em> (formal)', 'registro oral vs. escrito académico'),
    ],
    slides=[
        ('Intensificación', None,
         '<p>La <strong>intensificación</strong> amplifica el significado de una expresión. Puede ser léxica, morfológica o gramatical.</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Recurso</th><th style="padding:6px 10px;text-align:left">Ejemplos</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Adverbio</td><td style="padding:5px 10px"><em>sumamente, extraordinariamente, enormemente</em></td></tr>'
         '<tr><td style="padding:5px 10px">Superlativo -ísimo</td><td style="padding:5px 10px"><em>gravísimo, clarísimo, rapidísimo</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Prefijo</td><td style="padding:5px 10px"><em>ultramoderno, archiconocido, supersimple</em></td></tr>'
         '<tr><td style="padding:5px 10px">Reduplicación</td><td style="padding:5px 10px"><em>muy muy tarde, buenísimo de verdad</em></td></tr>'
         '</tbody></table>'),
        ('Atenuación', None,
         '<p>La <strong>atenuación</strong> reduce el impacto de lo dicho para preservar la cortesía o introducir reservas epistémicas.</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Estrategia</th><th style="padding:6px 10px;text-align:left">Ejemplo</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Adverbio atenuante</td><td style="padding:5px 10px"><em>algo, un poco, bastante, relativamente</em></td></tr>'
         '<tr><td style="padding:5px 10px">Condicional de cortesía</td><td style="padding:5px 10px"><em>querría, podría, debería</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Impersonalización</td><td style="padding:5px 10px"><em>se podría decir, cabría considerar</em></td></tr>'
         '<tr><td style="padding:5px 10px">Subjuntivo modal</td><td style="padding:5px 10px"><em>que yo sepa, si no me equivoco</em></td></tr>'
         '</tbody></table>'),
        ('Función en el discurso', None,
         '<p>Intensificación y atenuación sirven funciones pragmáticas distintas:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Función</th><th style="padding:6px 10px;text-align:left">Efecto</th><th style="padding:6px 10px;text-align:left">Ejemplo</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Énfasis emotivo</td><td style="padding:5px 10px">Intensificar</td><td style="padding:5px 10px"><em>¡Es absolutamente imprescindible!</em></td></tr>'
         '<tr><td style="padding:5px 10px">Imagen positiva</td><td style="padding:5px 10px">Atenuar crítica</td><td style="padding:5px 10px"><em>El texto es algo largo</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Reserva epistémica</td><td style="padding:5px 10px">Atenuar certeza</td><td style="padding:5px 10px"><em>Que yo sepa, llegó ayer</em></td></tr>'
         '</tbody></table>'),
        ('Registro formal vs. coloquial', None,
         '<p>Los recursos de intensificación varían mucho según el registro:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Coloquial</th><th style="padding:6px 10px;text-align:left">Formal/escrito</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px"><em>mogollón de trabajo</em></td><td style="padding:5px 10px"><em>una cantidad ingente de trabajo</em></td></tr>'
         '<tr><td style="padding:5px 10px"><em>súper interesante</em></td><td style="padding:5px 10px"><em>sumamente interesante</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px"><em>brutal el concierto</em></td><td style="padding:5px 10px"><em>el concierto fue excepcional</em></td></tr>'
         '<tr><td style="padding:5px 10px"><em>es que no puedo más</em></td><td style="padding:5px 10px"><em>me resulta francamente insostenible</em></td></tr>'
         '</tbody></table>'),
    ],
    traps=[
        ('*Es muy buenísimo', 'Es buenísimo / Es muy bueno', 'El superlativo -ísimo ya expresa el grado máximo; combinarlo con <em>muy</em> es una redundancia no estándar en el registro culto.'),
        ('*Querría que vinierais, por favor muy urgente', 'Querría que vinierais con cierta urgencia', 'En registros formales mezclar el condicional cortés con marcadores coloquiales de urgencia produce incoherencia de registro.'),
        ('*Cabría intensamente reconsiderar', 'Cabría reconsiderar con detenimiento', '<em>Cabría</em> es ya un atenuante modal; añadir un intensificador de la acción (<em>intensamente</em>) contradice su función cortés.'),
        ('*Un poco imposible', 'prácticamente imposible / casi imposible', '<em>Un poco</em> solo atenúa propiedades graduables; <em>imposible</em> es absoluto y no admite atenuación con <em>un poco</em>.'),
        ('*Llego algo tarde siempre', 'Llego siempre algo tarde', 'El adverbio <em>algo</em> atenúa adjetivos o adverbios, no verbos. <em>Algo</em> modifica <em>tarde</em> (adv.), que a su vez modifica el verbo.'),
    ],
    items=[
        dict(term='intensificación', definition='Operación pragmática que amplifica el significado o el grado de una propiedad', example='Es un problema gravísimo', accept=['intensificacion']),
        dict(term='atenuación', definition='Operación pragmática que reduce el impacto de lo dicho para la imagen o la certeza', example='El resultado es algo decepcionante', accept=['atenuacion']),
        dict(term='superlativo absoluto', definition='Forma en -ísimo que expresa el grado máximo de una cualidad sin comparación', example='un texto clarísimo', accept=['superlativo absoluto', '-isimo']),
        dict(term='condicional de cortesía', definition='Uso del condicional para suavizar peticiones, críticas o afirmaciones', example='Querría hacerte una pregunta', accept=['condicional cortesia', 'condicional de cortesia']),
        dict(term='impersonalización', definition='Eliminación del agente para distribuir la responsabilidad o atenuar la asertividad', example='Cabría revisar este punto', accept=['impersonalizacion']),
        dict(term='reserva epistémica', definition='Marcador que limita la certeza del hablante sobre lo afirmado', example='Que yo sepa, llegó ayer', accept=['reserva epistemica']),
        dict(term='reduplicación expresiva', definition='Repetición de un elemento para reforzar su valor intensivo', example='muy muy tarde, buenísimo buenísimo', accept=['reduplicacion']),
        dict(term='registro', definition='Variedad de lengua asociada a una situación comunicativa específica (formal, coloquial, escrito, oral)', example='mogollón (coloquial) vs. una cantidad ingente (formal)', accept=['registro linguistico']),
    ],
    ex1=dict(
        title='Identifica el recurso de intensificación o atenuación',
        questions=[
            ('¿Qué función tiene <em>algo</em> en «El texto es algo complicado»?',
             ['Intensificar <em>complicado</em>', 'Atenuar <em>complicado</em>', 'Negar que sea complicado', 'Indicar incertidumbre temporal'],
             1, '<em>Algo</em> es un adverbio atenuante: reduce el grado de la propiedad <em>complicado</em> para suavizar la valoración.'),
            ('¿Cuál de estos recursos es un intensificador morfológico?',
             ['Cabría revisar', 'Un poco largo', 'Extraordinariamente rápido', 'Clarísimo'],
             3, 'El sufijo <em>-ísimo</em> en <em>clarísimo</em> es un intensificador morfológico (superlativo absoluto).'),
            ('¿Qué estrategia de atenuación usa «Cabría considerar otra opción»?',
             ['Superlativo absoluto', 'Reduplicación', 'Impersonalización con modal', 'Prefijo intensificador'],
             2, '<em>Cabría</em> impersonaliza (no hay agente explícito) y usa el modal <em>caber</em> en condicional para atenuar la recomendación.'),
            ('¿Cuál de estas expresiones pertenece al registro coloquial y no al formal?',
             ['Un argumento sumamente sólido', 'Me resulta francamente insostenible', 'Mogollón de trabajo', 'Un resultado extraordinariamente positivo'],
             2, '<em>Mogollón de trabajo</em> es expresión coloquial; los otros pertenecen al registro formal o escrito.'),
            ('¿Cuál de estas combinaciones es redundante en el registro culto?',
             ['muy interesante', 'sumamente grave', 'muy buenísimo', 'extraordinariamente útil'],
             2, 'Combinar <em>muy</em> con el superlativo <em>buenísimo</em> es redundante porque <em>-ísimo</em> ya indica el grado máximo.'),
        ]
    ),
    ex2=dict(
        title='Reformula con el registro indicado',
        questions=[
            ('Reformula «Es súper difícil» en registro formal.',
             'Es sumamente difícil',
             ['es sumamente difícil', 'es muy difícil', 'es extraordinariamente difícil', 'resulta sumamente difícil', 'resulta muy difícil'],
             'En registro formal se sustituye <em>súper</em> por un adverbio culto: <em>sumamente, extremadamente, extraordinariamente</em>.'),
            ('Atenúa la crítica en «El informe está mal redactado» usando impersonalización.',
             'Cabría mejorar la redacción del informe',
             ['cabría mejorar la redacción del informe', 'podría mejorarse la redacción', 'convendría revisar la redacción'],
             'La impersonalización con <em>cabría / podría</em> + infinitivo elimina el agente y suaviza la crítica.'),
            ('Intensifica «un resultado positivo» con superlativo absoluto.',
             'un resultado positivísimo',
             ['un resultado positivísimo', 'un resultado positivisimo'],
             'El sufijo <em>-ísimo</em> se añade a la base del adjetivo: <em>positiv- + ísimo = positivísimo</em>.'),
        ]
    ),
    ex3=dict(
        title='Elige la expresión más adecuada',
        questions=[
            ('En un informe académico, ¿cuál es la forma más apropiada de atenuar una afirmación?',
             ['Es que esto es imposible de entender', 'No sé si esto tiene sentido', 'Cabría matizar que los resultados son provisionales', 'Esto es bastante raro, la verdad'],
             2, '<em>Cabría matizar</em> usa la impersonalización y el condicional modal propio del registro académico para atenuar la afirmación.'),
            ('¿Cuál de estos superlativa correctamente el adjetivo «joven»?',
             ['muy joven', 'jovensísimo', 'jovencísimo', 'jovenísimo'],
             2, 'Ante la terminación <em>-en</em>, la vocal temática cambia: <em>joven → jovencísimo</em> (con -c- epentética).'),
            ('Para preservar la imagen del interlocutor al pedir un favor, ¿cuál es el mejor recurso?',
             ['¡Dime la solución!', 'Necesito que me des la solución', 'Querría que me explicaras la solución', '¿No puedes simplemente explicármelo?'],
             2, 'El condicional de cortesía (<em>querría</em>) más el subjuntivo (<em>explicaras</em>) maximizan la atenuación de la petición.'),
            ('¿Cuál de estas construcciones usa la reserva epistémica?',
             ['Obviamente llegó tarde', 'Sin duda lo saben', 'Que yo sepa, no ha llegado aún', 'Está claro que es correcto'],
             2, '<em>Que yo sepa</em> limita explícitamente la certeza del hablante al ámbito de su conocimiento personal.'),
        ]
    ),
)

# ---------------------------------------------------------------------------
# G13: VARIACIÓN LINGÜÍSTICA DEL ESPAÑOL
# ---------------------------------------------------------------------------
CHAPTERS['variacion-linguistica'] = dict(
    level='c2', section='grammar', num='G13',
    short='Variación Lingüística',
    title='Variación Lingüística del Español',
    subtitle='Comprende los dialectos, registros y la norma panhispánica del español mundial',
    game_desc='Variación lingüística: seseo, voseo, yeísmo, variación léxica y norma panhispánica',
    summary=[
        ('Variedades dialectales', 'El español tiene variedades regionales: peninsular (norte/sur), canario, caribeño, andino, rioplatense, mexicano-centroamericano', 'distinción s/z en España; seseo en América y sur de España'),
        ('Variación fonológica', 'Distinción vs. seseo, voseo, yeísmo, aspiración de -s, debilitamiento de -d-', 'caza/casa (distinción) = /θ/; (seseo) = /s/'),
        ('Voseo', 'Uso de <em>vos</em> + formas verbales propias en Argentina, Uruguay, partes de Centroamérica', 'vos tenés, vos hablás (rioplatense)'),
        ('Variación léxica', 'Palabras diferentes para el mismo referente según la región: <em>coche/carro/auto</em>, <em>piso/apartamento/departamento</em>', 'ordenador (España) / computadora (América) / computador (Cono Sur)'),
        ('Registros y estilos', 'Formal/informal, escrito/oral, estándar/coloquial. El hablante C2 maneja todos los registros con conciencia de sus diferencias', 'uso de <em>usted</em> vs. <em>tú/vos</em>'),
        ('Norma panhispánica', 'La RAE/ASALE publican normas que reconocen la pluralidad del español estándar; no hay un único estándar correcto', 'DPD (Diccionario Panhispánico de Dudas)'),
    ],
    slides=[
        ('Dialectos del español', None,
         '<p>El español cuenta con más de 500 millones de hablantes repartidos en variedades regionales con rasgos propios:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Variedad</th><th style="padding:6px 10px;text-align:left">Zona</th><th style="padding:6px 10px;text-align:left">Rasgo destacado</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Castellana (norte)</td><td style="padding:5px 10px">Centro-norte de España</td><td style="padding:5px 10px">Distinción s/θ, tuteo</td></tr>'
         '<tr><td style="padding:5px 10px">Andaluza/Canaria</td><td style="padding:5px 10px">Sur España, Canarias</td><td style="padding:5px 10px">Seseo, aspiración de -s</td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Caribeña</td><td style="padding:5px 10px">Cuba, PR, RD, Venezuela</td><td style="padding:5px 10px">Aspiración -s, -r final</td></tr>'
         '<tr><td style="padding:5px 10px">Rioplatense</td><td style="padding:5px 10px">Argentina, Uruguay</td><td style="padding:5px 10px">Voseo, sh/zh para ll/y</td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Andina</td><td style="padding:5px 10px">Perú, Bolivia, Ecuador</td><td style="padding:5px 10px">Conservadurismo consonántico</td></tr>'
         '</tbody></table>'),
        ('Fenómenos fonológicos', None,
         '<p>Algunos rasgos fonológicos definen las principales variedades:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Fenómeno</th><th style="padding:6px 10px;text-align:left">Descripción</th><th style="padding:6px 10px;text-align:left">Ejemplo</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Seseo</td><td style="padding:5px 10px">c/z = /s/ (América, sur España)</td><td style="padding:5px 10px"><em>caza = casa</em> para el hablante seseante</td></tr>'
         '<tr><td style="padding:5px 10px">Distinción</td><td style="padding:5px 10px">c/z = /θ/, s = /s/ (norte España)</td><td style="padding:5px 10px"><em>caza</em> [kaθa] ≠ <em>casa</em> [kasa]</td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Yeísmo</td><td style="padding:5px 10px">ll = y = /ʝ/ (más del 90% del mundo hispanohablante)</td><td style="padding:5px 10px"><em>pollo = poyo</em> para el yeísta</td></tr>'
         '<tr><td style="padding:5px 10px">Aspiración -s</td><td style="padding:5px 10px">-s final/implosiva → [h] o cero</td><td style="padding:5px 10px"><em>los mismos</em> → [loh ˈmizmoh]</td></tr>'
         '</tbody></table>'),
        ('Voseo y tuteo', None,
         '<p>El <strong>voseo</strong> usa <em>vos</em> con formas verbales propias como pronombre de segunda persona singular:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Pronombre</th><th style="padding:6px 10px;text-align:left">Verbo (HABLAR)</th><th style="padding:6px 10px;text-align:left">Zona</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px"><em>tú</em></td><td style="padding:5px 10px"><em>tú hablas</em></td><td style="padding:5px 10px">España, México, Perú…</td></tr>'
         '<tr><td style="padding:5px 10px"><em>vos</em></td><td style="padding:5px 10px"><em>vos hablás</em></td><td style="padding:5px 10px">Argentina, Uruguay, partes de Centroamérica</td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px"><em>vos</em></td><td style="padding:5px 10px"><em>vos hablás / hablás</em></td><td style="padding:5px 10px">Colombia (zonas), Chile (informal)</td></tr>'
         '</tbody></table>'),
        ('Variación léxica y norma panhispánica', None,
         '<p>El mismo referente tiene nombres distintos según la variedad:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">España</th><th style="padding:6px 10px;text-align:left">México/CA</th><th style="padding:6px 10px;text-align:left">Cono Sur</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px"><em>coche</em></td><td style="padding:5px 10px"><em>carro</em></td><td style="padding:5px 10px"><em>auto</em></td></tr>'
         '<tr><td style="padding:5px 10px"><em>ordenador</em></td><td style="padding:5px 10px"><em>computadora</em></td><td style="padding:5px 10px"><em>computador</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px"><em>piso</em></td><td style="padding:5px 10px"><em>apartamento</em></td><td style="padding:5px 10px"><em>departamento</em></td></tr>'
         '<tr><td style="padding:5px 10px"><em>zumo</em></td><td style="padding:5px 10px"><em>jugo</em></td><td style="padding:5px 10px"><em>jugo</em></td></tr>'
         '</tbody></table>'
         '<p style="margin-top:8px">La norma panhispánica (RAE + ASALE) reconoce todas estas variantes como correctas dentro de sus propias variedades.</p>'),
    ],
    traps=[
        ('*En Argentina dicen «vos hablas»', 'En Argentina dicen «vos hablás»', 'El voseo rioplatense usa formas verbales propias: presente -ás/-és/-ís; no coinciden con las del tuteo.'),
        ('*El seseo es incorrecto', 'El seseo es la norma en América y sur de España', 'El seseo no es un error: es la variante estándar en la mayoría del mundo hispanohablante. Solo el norte de España mantiene la distinción s/θ.'),
        ('*Pollo y poyo son homófonos en todas partes', 'Son homófonos solo en zonas con yeísmo', 'El yeísmo es mayoritario pero no universal; en algunas zonas rurales de España y América todavía se distingue /ʎ/ (ll) de /j/ (y).'),
        ('*Coche es incorrecto en México', 'Coche es correcto pero poco usado; carro es el preferido', 'Cada variante léxica es correcta dentro de su comunidad; <em>coche</em> se entiende en México pero suena foráneo.'),
        ('*Usted es siempre formal', 'Usted puede ser informal o de confianza en zonas de Colombia y América Central', 'El valor social de <em>usted</em> varía geográficamente: en Colombia y Costa Rica se usa también entre íntimos.'),
    ],
    items=[
        dict(term='seseo', definition='Fenómeno fonológico por el que c/z y s se pronuncian con el mismo sonido /s/', example='caza y casa son homófonos para un hablante seseante', accept=['seseo']),
        dict(term='distinción', definition='Mantenimiento de dos fonemas distintos: s = /s/ y c/z = /θ/', example='caza [kaθa] ≠ casa [kasa] (norte de España)', accept=['distincion', 'distinción s-z']),
        dict(term='voseo', definition='Uso del pronombre <em>vos</em> con sus formas verbales propias como segunda persona singular', example='vos hablás, vos tenés (rioplatense)', accept=['voseo']),
        dict(term='yeísmo', definition='Fusión de ll (/ʎ/) e y (/j/) en un solo sonido /ʝ/', example='pollo y poyo suenan igual para el yeísta', accept=['yeismo', 'yeísmo']),
        dict(term='aspiración de -s', definition='Pronunciación de la -s implosiva o final como [h] o su elisión', example='los mismos → [loh ˈmizmoh]', accept=['aspiracion de s', 'aspiracion']),
        dict(term='variación léxica', definition='Existencia de palabras distintas para el mismo referente en diferentes variedades del español', example='coche (España) / carro (México) / auto (Argentina)', accept=['variacion lexica']),
        dict(term='norma panhispánica', definition='Conjunto de normas lingüísticas establecidas por la RAE y la ASALE que reconocen la pluralidad del español estándar', example='El DPD (Diccionario Panhispánico de Dudas) refleja esta norma', accept=['norma panhispanica']),
        dict(term='registro', definition='Variedad de lengua condicionada por la situación comunicativa: formal, informal, escrito, oral, técnico, coloquial', example='<em>fallecer</em> (formal) vs. <em>palmarla</em> (coloquial)', accept=['registro']),
    ],
    ex1=dict(
        title='Identifica el fenómeno de variación lingüística',
        questions=[
            ('¿Qué fenómeno explica que en Argentina «vos tenés» sea lo habitual?',
             ['Tuteo', 'Voseo', 'Ustedeo', 'Leísmo'],
             1, 'El <em>voseo</em> usa <em>vos</em> como pronombre de segunda persona singular; las formas verbales son propias: <em>tenés, hablás, vivís</em>.'),
            ('¿Qué rasgo fonológico caracteriza al español del norte de España frente al de América?',
             ['Yeísmo generalizado', 'Aspiración de -s', 'Distinción s/θ', 'Seseo'],
             2, 'El norte de España mantiene la <em>distinción</em> entre /s/ y /θ/ (c, z), mientras que América y el sur de España practican el seseo.'),
            ('¿Cuál de estas palabras es la variante preferida en México para referirse a un automóvil?',
             ['Coche', 'Auto', 'Carro', 'Vehículo'],
             2, 'En México y América Central, <em>carro</em> es la palabra habitual; <em>coche</em> es española y <em>auto</em> es del Cono Sur.'),
            ('¿Qué organismo elabora la norma panhispánica del español?',
             ['Solo la RAE (Real Academia Española)', 'La RAE junto con las Academias americanas (ASALE)', 'El Instituto Cervantes', 'La ONU'],
             1, 'La norma panhispánica es obra conjunta de la RAE y la Asociación de Academias de la Lengua Española (ASALE).'),
            ('El yeísmo hace que sean homófonos:',
             ['caza y casa', 'pollo y poyo', 'vaca y baca', 'hola y ola'],
             1, 'El yeísmo fusiona /ʎ/ (ll) y /j/ (y), haciendo indistinguibles <em>pollo</em> y <em>poyo</em> para quienes no distinguen.'),
        ]
    ),
    ex2=dict(
        title='Transforma según la variedad indicada',
        questions=[
            ('Adapta «tú hablas muy bien» al voseo rioplatense.',
             'Vos hablás muy bien',
             ['vos hablás muy bien', 'vos hablas muy bien'],
             'El voseo rioplatense: pronombre <em>vos</em> + forma verbal de segunda persona con acento en la última sílaba: <em>hablás</em>.'),
            ('Indica el equivalente de <em>ordenador</em> (España) en el español de México.',
             'computadora',
             ['computadora'],
             'En México y gran parte de América se usa <em>computadora</em> donde España dice <em>ordenador</em>.'),
            ('¿Cómo se pronuncia <em>zapato</em> en una variedad seseante?',
             'sapato',
             ['sapato', '[sapato]'],
             'En el seseo, la z se pronuncia /s/: <em>zapato</em> → [sapato].'),
        ]
    ),
    ex3=dict(
        title='Variación en contexto',
        questions=[
            ('Un hablante dice «cerrá la puerta». ¿De qué variedad es probablemente?',
             ['España (norte)', 'México', 'Rioplatense (Argentina/Uruguay)', 'Caribeña (Cuba/Puerto Rico)'],
             2, 'El imperativo voseante <em>cerrá</em> (sin -s final) es propio del español rioplatense; el tuteo daría <em>cierra</em>.'),
            ('¿Cuál de estas afirmaciones sobre el seseo es correcta?',
             ['Solo ocurre en América Latina', 'Es un error lingüístico que debe corregirse', 'Es la norma en América y en el sur de España', 'Solo aparece en habla informal'],
             2, 'El seseo es la norma estándar en toda América hispanohablante y en Canarias y Andalucía; no es un error.'),
            ('Un argentino y un español hablan del mismo objeto: uno dice <em>auto</em> y el otro <em>coche</em>. ¿Qué tipo de variación es?',
             ['Fonológica', 'Morfológica', 'Léxica', 'Pragmática'],
             2, 'El mismo referente tiene denominaciones distintas según la región: es variación <em>léxica</em>.'),
            ('¿Qué significa que el español tenga una norma panhispánica?',
             ['Solo hay un español correcto, el de España', 'Cada variedad regional es igualmente válida según sus propias normas', 'Las variedades americanas son dialectos del español español', 'La RAE decide qué variantes son incorrectas'],
             1, 'La norma panhispánica reconoce la diversidad del español: <em>carro, coche</em> y <em>auto</em> son todos correctos en sus contextos.'),
        ]
    ),
)

# ---------------------------------------------------------------------------
# G14: PRAGMÁTICA DEL ESPAÑOL: ACTOS DE HABLA E IMPLICATURAS
# ---------------------------------------------------------------------------
CHAPTERS['pragmatica-espanol'] = dict(
    level='c2', section='grammar', num='G14',
    short='Pragmática',
    title='Pragmática: Actos de Habla e Implicaturas',
    subtitle='Analiza actos ilocutivos, implicaturas y estrategias de cortesía en el español',
    game_desc='Pragmática: actos de habla, máximas de Grice, implicaturas y cortesía lingüística',
    summary=[
        ('Actos de habla', 'Austin/Searle: actos locutivos (enunciado), ilocutivos (intención) y perlocutivos (efecto en el oyente)', 'decir «¿Puedes cerrar la puerta?» es una petición, no una pregunta'),
        ('Tipos de actos ilocutivos', 'Asertivos, directivos, compromisivos, expresivos, declarativos', '<em>Te prometo que llamaré</em> (compromisivo)'),
        ('Principio de cooperación (Grice)', 'Máximas de cantidad, cualidad, relación y modo que rigen la conversación eficiente', 'violar la cantidad crea implicaturas'),
        ('Implicatura conversacional', 'Significado implícito que el oyente infiere porque el hablante no ha sido completamente explícito', '«¿Tienes hora?» → «Son las tres» (no solo sí/no)'),
        ('Cortesía lingüística', 'Estrategias positivas (solidaridad) y negativas (no intromisión) para gestionar la imagen del interlocutor', 'atenuar con condicional; usar <em>usted</em>'),
        ('Deixis', 'Referencias deícticas de persona, lugar y tiempo que solo se interpretan en contexto', '<em>aquí, ahora, yo, eso</em> dependen del contexto'),
    ],
    slides=[
        ('Actos de habla', None,
         '<p>Todo enunciado realiza simultáneamente varios <strong>actos de habla</strong>:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Nivel</th><th style="padding:6px 10px;text-align:left">Definición</th><th style="padding:6px 10px;text-align:left">Ejemplo</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Locutivo</td><td style="padding:5px 10px">El enunciado en sí</td><td style="padding:5px 10px"><em>«¿Puedes abrir la ventana?»</em></td></tr>'
         '<tr><td style="padding:5px 10px">Ilocutivo</td><td style="padding:5px 10px">La intención del hablante</td><td style="padding:5px 10px">Petición (no pregunta)</td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Perlocutivo</td><td style="padding:5px 10px">El efecto en el oyente</td><td style="padding:5px 10px">El oyente abre la ventana</td></tr>'
         '</tbody></table>'),
        ('Tipos de actos ilocutivos', None,
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Tipo</th><th style="padding:6px 10px;text-align:left">Función</th><th style="padding:6px 10px;text-align:left">Ejemplo</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Asertivo</td><td style="padding:5px 10px">Afirmar/describir</td><td style="padding:5px 10px"><em>Llueve</em></td></tr>'
         '<tr><td style="padding:5px 10px">Directivo</td><td style="padding:5px 10px">Pedir/ordenar</td><td style="padding:5px 10px"><em>Cierra la puerta</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Compromisivo</td><td style="padding:5px 10px">Comprometerse</td><td style="padding:5px 10px"><em>Te juro que vendré</em></td></tr>'
         '<tr><td style="padding:5px 10px">Expresivo</td><td style="padding:5px 10px">Expresar sentimiento</td><td style="padding:5px 10px"><em>¡Gracias! / Lo siento</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Declarativo</td><td style="padding:5px 10px">Transformar la realidad</td><td style="padding:5px 10px"><em>Os declaro marido y mujer</em></td></tr>'
         '</tbody></table>'),
        ('Máximas de Grice', None,
         '<p>El <strong>Principio de Cooperación</strong> de Grice establece que los hablantes cooperan siguiendo cuatro máximas:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Máxima</th><th style="padding:6px 10px;text-align:left">Regla</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Cantidad</td><td style="padding:5px 10px">Di lo necesario; ni más ni menos</td></tr>'
         '<tr><td style="padding:5px 10px">Cualidad</td><td style="padding:5px 10px">No digas lo que crees falso</td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Relación</td><td style="padding:5px 10px">Sé relevante</td></tr>'
         '<tr><td style="padding:5px 10px">Modo</td><td style="padding:5px 10px">Sé claro y ordenado</td></tr>'
         '</tbody></table>'
         '<p style="margin-top:8px">Cuando se viola una máxima, el oyente infiere una <em>implicatura conversacional</em>.</p>'),
        ('Cortesía e imagen', None,
         '<p>La <strong>teoría de la imagen</strong> (Brown &amp; Levinson) explica las estrategias de cortesía:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Cortesía</th><th style="padding:6px 10px;text-align:left">Estrategia</th><th style="padding:6px 10px;text-align:left">Ejemplo</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Positiva</td><td style="padding:5px 10px">Solidaridad, aprobación</td><td style="padding:5px 10px"><em>¡Qué buena idea! ¿Podrías ayudarme?</em></td></tr>'
         '<tr><td style="padding:5px 10px">Negativa</td><td style="padding:5px 10px">No intromisión, autonomía</td><td style="padding:5px 10px"><em>Si no es molestia, te agradecería que…</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Encubierta</td><td style="padding:5px 10px">Indirecta, ambigua</td><td style="padding:5px 10px"><em>Aquí abre mucho la ventana, ¿verdad?</em> (= petición)</td></tr>'
         '</tbody></table>'),
    ],
    traps=[
        ('*Confundir el acto locutivo con el ilocutivo', 'Distinguir qué se dice (locutivo) de qué se intenta hacer (ilocutivo)', '«¿Tienes hora?» → acto locutivo: pregunta sobre posesión; acto ilocutivo: petición de información.'),
        ('*Una implicatura es parte del significado literal', 'La implicatura es inferida, no codificada', '«Algo estudié» implica «No estudié mucho», pero no lo dice literalmente; es una implicatura por violación de la máxima de cantidad.'),
        ('*La cortesía negativa siempre usa <em>no</em>', 'Cortesía negativa = respetar la autonomía del otro; no tiene que ver con la negación', 'La cortesía negativa incluye pedir disculpas antes de hacer una petición, usar condicionales, etc.'),
        ('*Los actos declarativos son simples afirmaciones', 'Los declarativos transforman la realidad social con el enunciado mismo', 'Decir «te despido» crea el hecho del despido; no es solo una descripción.'),
        ('*La deixis siempre se refiere al presente', 'La deixis puede ser espacial, temporal o personal, y siempre depende del contexto de enunciación', '<em>Mañana</em> en una carta del siglo XIX no es mañana para el lector actual: es deixis temporal relativa al momento de escritura.'),
    ],
    items=[
        dict(term='acto de habla', definition='Acción que se realiza al emitir un enunciado: locutivo (qué se dice), ilocutivo (qué se hace), perlocutivo (efecto)', example='«¿Puedes abrir la puerta?» es un acto directivo', accept=['acto de habla', 'acto ilocutivo']),
        dict(term='implicatura', definition='Significado implícito que el oyente infiere a partir del principio de cooperación y las máximas de Grice', example='«Algo estudié» implica «No estudié mucho»', accept=['implicatura conversacional']),
        dict(term='máxima de cantidad', definition='Regla de Grice: di lo necesario, ni más ni menos información de la que la conversación requiere', example='Responder «Sí» a «¿Me podrías decir la hora?» viola la cantidad', accept=['maxima de cantidad']),
        dict(term='máxima de relevancia', definition='Regla de Grice: cada contribución debe ser pertinente al tema de la conversación', example='Responder a «¿Cómo estás?» con «Hoy es martes» viola la relevancia', accept=['maxima de relevancia', 'maxima de relacion']),
        dict(term='cortesía positiva', definition='Estrategia de cortesía que expresa solidaridad, aprobación o cercanía con el interlocutor', example='«¡Qué buena idea! ¿Podrías ayudarme?»', accept=['cortesia positiva']),
        dict(term='cortesía negativa', definition='Estrategia de cortesía que respeta la autonomía del interlocutor minimizando la imposición', example='«Si no es molestia, te agradecería que…»', accept=['cortesia negativa']),
        dict(term='deixis', definition='Mecanismo por el que expresiones como <em>yo, aquí, ahora</em> señalan elementos del contexto de enunciación', example='<em>aquí</em> significa donde está el hablante en el momento de hablar', accept=['deixis']),
        dict(term='principio de cooperación', definition='Principio de Grice según el cual los interlocutores asumen que el otro habla de manera relevante y veraz', example='Las implicaturas surgen cuando se viola o simula violar una máxima', accept=['principio de cooperacion', 'cooperacion']),
    ],
    ex1=dict(
        title='Identifica el tipo de acto de habla',
        questions=[
            ('«Te juro que estaré allí a las ocho». ¿Qué tipo de acto ilocutivo es?',
             ['Asertivo', 'Directivo', 'Compromisivo', 'Expresivo'],
             2, 'El hablante se compromete a realizar una acción futura → acto <em>compromisivo</em>.'),
            ('«Queda usted despedido». ¿Qué tipo de acto ilocutivo es?',
             ['Directivo', 'Declarativo', 'Asertivo', 'Expresivo'],
             1, 'El enunciado transforma la realidad social (crea el despido con la palabra) → acto <em>declarativo</em>.'),
            ('A dice «¿Tienes frío?» cuando la ventana está abierta. ¿Cuál es el acto ilocutivo real?',
             ['Pregunta sobre el estado físico de B', 'Petición indirecta de cerrar la ventana', 'Queja sobre el frío', 'Orden de cerrar la ventana'],
             1, 'La pregunta es una <em>petición indirecta</em> (acto directivo encubierto): A quiere que B cierre la ventana.'),
            ('¿Cuál de estas expresiones es un acto expresivo?',
             ['Cierra la puerta', 'Te prometo que vendré', 'Lo siento mucho', 'Mañana llueve'],
             2, '<em>Lo siento</em> expresa el estado emocional del hablante → acto <em>expresivo</em>.'),
            ('¿Qué máxima de Grice se viola cuando alguien responde a una pregunta con mucha más información de la necesaria?',
             ['Máxima de cualidad', 'Máxima de modo', 'Máxima de cantidad', 'Máxima de relación'],
             2, 'Dar más información de la necesaria viola la <em>máxima de cantidad</em> («di lo necesario; no más»).'),
        ]
    ),
    ex2=dict(
        title='Explica la implicatura',
        questions=[
            ('A pregunta: «¿Cómo fue el examen?» B responde: «Bueno, salí vivo». ¿Qué implica B?',
             'B implica que el examen fue difícil o que no le fue bien',
             ['que el examen fue difícil', 'que le fue mal', 'b implica que el examen fue difícil'],
             'La respuesta viola la máxima de cantidad (no da la información directa) e implica por relevancia que el examen fue duro.'),
            ('«Si no es mucha molestia, ¿podrías revisar el informe?» ¿Qué estrategia de cortesía usa?',
             'Cortesía negativa (respeta la autonomía del interlocutor)',
             ['cortesía negativa', 'cortesia negativa'],
             'La expresión <em>si no es mucha molestia</em> minimiza la imposición sobre el interlocutor → cortesía negativa.'),
            ('¿Qué tipo de deixis hay en «Nos vemos aquí mañana»?',
             'Deixis espacial (aquí) y temporal (mañana)',
             ['espacial y temporal', 'deixis espacial y temporal'],
             '<em>Aquí</em> es deixis espacial (lugar del hablante); <em>mañana</em> es deixis temporal (relativa al momento de enunciación).'),
        ]
    ),
    ex3=dict(
        title='Aplicación pragmática',
        questions=[
            ('¿Cuál de estas expresiones es la petición indirecta más cortés?',
             ['Dame ese libro', 'Necesito ese libro', '¿Te importaría prestarme ese libro?', 'Préstame el libro'],
             2, 'La pregunta indirecta con <em>¿Te importaría…?</em> usa la forma interrogativa + condicional para maximizar la cortesía negativa.'),
            ('Un hablante dice «Algo sé de cocina» cuando se le pregunta si cocina bien. ¿Qué implica?',
             ['Que cocina muy bien', 'Que no sabe nada de cocina', 'Que sabe relativamente poco de cocina', 'Que le gusta mucho cocinar'],
             2, 'La escala <em>algo → bastante → mucho</em> genera la implicatura de cantidad: si usara <em>mucho</em> lo diría; <em>algo</em> implica «no mucho».'),
            ('¿Cuál es la diferencia entre el acto locutivo y el ilocutivo en «¿Puedes pasarme la sal?»?',
             ['No hay diferencia', 'Locutivo: pregunta sobre capacidad; ilocutivo: petición', 'Locutivo: petición; ilocutivo: pregunta', 'Ambos son preguntas sobre la capacidad'],
             1, 'El acto locutivo es una pregunta sobre capacidad física; el acto ilocutivo (intención real) es una petición directa de la sal.'),
            ('¿Qué teoría explica por qué «Aquí hace calor» puede interpretarse como una petición de abrir la ventana?',
             ['Teoría de la referencia', 'Teoría de los actos de habla (indirectos)', 'Gramática generativa', 'Morfología derivativa'],
             1, 'La <em>teoría de los actos de habla indirectos</em> (Searle) explica cómo un enunciado puede tener una fuerza ilocutiva diferente de su forma gramatical.'),
        ]
    ),
)

# ---------------------------------------------------------------------------
# G15: CREATIVIDAD LÉXICA: FORMACIÓN DE PALABRAS
# ---------------------------------------------------------------------------
CHAPTERS['creatividad-lexica'] = dict(
    level='c2', section='grammar', num='G15',
    short='Creatividad Léxica',
    title='Creatividad Léxica: Formación de Palabras',
    subtitle='Analiza derivación, composición, parasíntesis, préstamos y neologismos del español actual',
    game_desc='Formación de palabras: derivación, composición, parasíntesis, acortamientos y neologismos',
    summary=[
        ('Derivación', 'Formación de palabras con prefijos y sufijos: <em>re-, des-, -ción, -mente, -ismo, -ista</em>', '<em>releer, deshacer, globalización, claramente</em>'),
        ('Composición', 'Unión de dos o más bases léxicas: <em>N+N, V+N, Adj+N</em>', '<em>lavaplatos, cortacésped, mediodía, altavoz</em>'),
        ('Parasíntesis', 'Derivación simultánea con prefijo y sufijo sin que existan las formas intermedias', '<em>aterrizar (*tierra → *terrizar → aterrizar)</em>'),
        ('Acortamientos', 'Abreviación de palabras largas: apócope, aféresis, acronimia, siglas', '<em>foto (fotografía), bus (autobús), DNI, ONG</em>'),
        ('Préstamos y neologismos', 'Adopción de palabras extranjeras (anglicismos, galicismos) y creación de nuevas palabras', '<em>internet, chatear, hackear, selfi</em>'),
        ('Creatividad en el español actual', 'Formación por analogía, calcos, palabras-maleta (blended words)', '<em>franquismo → kirchnerismo, infotainment → infoentretenimiento</em>'),
    ],
    slides=[
        ('Derivación', None,
         '<p>La <strong>derivación</strong> añade afijos (prefijos o sufijos) a una base para crear nuevas palabras:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Tipo</th><th style="padding:6px 10px;text-align:left">Afijo</th><th style="padding:6px 10px;text-align:left">Ejemplo</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Prefijación</td><td style="padding:5px 10px"><em>re-, des-, in-, pre-</em></td><td style="padding:5px 10px"><em>releer, deshacer, inútil, prever</em></td></tr>'
         '<tr><td style="padding:5px 10px">Sufijación nominal</td><td style="padding:5px 10px"><em>-ción, -idad, -ismo</em></td><td style="padding:5px 10px"><em>globalización, realidad, capitalismo</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Sufijación adverbial</td><td style="padding:5px 10px"><em>-mente</em></td><td style="padding:5px 10px"><em>claramente, lentamente</em></td></tr>'
         '<tr><td style="padding:5px 10px">Sufijación verbal</td><td style="padding:5px 10px"><em>-ear, -izar, -ificar</em></td><td style="padding:5px 10px"><em>chatear, globalizar, simplificar</em></td></tr>'
         '</tbody></table>'),
        ('Composición y parasíntesis', None,
         '<p><strong>Composición</strong>: unión de dos bases léxicas. <strong>Parasíntesis</strong>: prefijo + base + sufijo simultáneos.</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Proceso</th><th style="padding:6px 10px;text-align:left">Estructura</th><th style="padding:6px 10px;text-align:left">Ejemplo</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Composición N+N</td><td style="padding:5px 10px">sustantivo + sustantivo</td><td style="padding:5px 10px"><em>mediodía, bocacalle</em></td></tr>'
         '<tr><td style="padding:5px 10px">Composición V+N</td><td style="padding:5px 10px">verbo + sustantivo</td><td style="padding:5px 10px"><em>lavaplatos, cortacésped</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Parasíntesis</td><td style="padding:5px 10px">prefijo + base + sufijo</td><td style="padding:5px 10px"><em>aterrizar, enrojecer, encuadernar</em></td></tr>'
         '</tbody></table>'),
        ('Acortamientos y siglas', None,
         '<p>El español reduce palabras largas por distintos procedimientos:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Procedimiento</th><th style="padding:6px 10px;text-align:left">Resultado</th><th style="padding:6px 10px;text-align:left">Ejemplo</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Apócope</td><td style="padding:5px 10px">Supresión del final</td><td style="padding:5px 10px"><em>foto &lt; fotografía, bici &lt; bicicleta</em></td></tr>'
         '<tr><td style="padding:5px 10px">Aféresis</td><td style="padding:5px 10px">Supresión del inicio</td><td style="padding:5px 10px"><em>bus &lt; autobús, norabuena &lt; enhorabuena</em></td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Siglas</td><td style="padding:5px 10px">Iniciales leídas como letras</td><td style="padding:5px 10px"><em>DNI, ONG, URL</em></td></tr>'
         '<tr><td style="padding:5px 10px">Acrónimos</td><td style="padding:5px 10px">Siglas leídas como palabras</td><td style="padding:5px 10px"><em>OTAN, RENFE, OVNI</em></td></tr>'
         '</tbody></table>'),
        ('Préstamos, neologismos y calcos', None,
         '<p>El español adopta palabras del exterior y crea otras por analogía o fusión:</p>'
         '<table style="border-collapse:collapse;width:100%;font-size:.9rem"><thead><tr style="background:var(--amber);color:#fff">'
         '<th style="padding:6px 10px;text-align:left">Proceso</th><th style="padding:6px 10px;text-align:left">Ejemplo</th><th style="padding:6px 10px;text-align:left">Origen</th></tr></thead><tbody>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Anglicismo adaptado</td><td style="padding:5px 10px"><em>chatear, hackear, selfi</em></td><td style="padding:5px 10px">to chat, to hack, selfie</td></tr>'
         '<tr><td style="padding:5px 10px">Calco semántico</td><td style="padding:5px 10px"><em>ratón (mouse), nube (cloud)</em></td><td style="padding:5px 10px">inglés técnico</td></tr>'
         '<tr style="background:var(--paper)"><td style="padding:5px 10px">Palabra-maleta</td><td style="padding:5px 10px"><em>infoentretenimiento</em></td><td style="padding:5px 10px">información + entretenimiento</td></tr>'
         '<tr><td style="padding:5px 10px">Analogía</td><td style="padding:5px 10px"><em>kirchnerismo, bolsonarismo</em></td><td style="padding:5px 10px">como franquismo, nazismo</td></tr>'
         '</tbody></table>'),
    ],
    traps=[
        ('*La parasíntesis es solo un tipo de composición', 'La parasíntesis combina prefijación y sufijación simultáneas', '<em>aterrizar</em> no es composición (no existe *terrizar) ni simple derivación; el prefijo y el sufijo se añaden a la vez.'),
        ('*Selfi es un anglicismo no aceptado por la RAE', 'Selfi está en el diccionario de la RAE desde 2014', 'La RAE acepta préstamos adaptados a la ortografía española; <em>selfi</em> es la forma recomendada (no <em>selfie</em>).'),
        ('*Las siglas siempre se leen letra por letra', 'Las siglas que forman sílabas se leen como palabras (acrónimos)', '<em>OTAN</em> se lee [ó-tan], no letra por letra; <em>DNI</em> sí se lee letra por letra.'),
        ('*Chat-ear es derivación simple', 'Chatear es un préstamo integrado mediante derivación verbal (-ear)', 'La base es el anglicismo <em>chat</em> + el sufijo verbalizador <em>-ear</em>; es préstamo + sufijación, no derivación puramente hispánica.'),
        ('*Los calcos semánticos son siempre galicismos', 'Los calcos semánticos pueden venir de cualquier lengua', '<em>Ratón</em> (de <em>mouse</em>) y <em>nube</em> (de <em>cloud</em>) son calcos del inglés, no del francés.'),
    ],
    items=[
        dict(term='derivación', definition='Formación de palabras mediante la adición de prefijos o sufijos a una base léxica', example='releer (re- + leer), globalización (global + -ización)', accept=['derivacion']),
        dict(term='composición', definition='Formación de palabras mediante la unión de dos o más bases léxicas independientes', example='lavaplatos (lavar + platos), mediodía (medio + día)', accept=['composicion']),
        dict(term='parasíntesis', definition='Formación de palabras mediante la adición simultánea de prefijo y sufijo a una base, sin etapas intermedias', example='aterrizar (a- + tierra + -izar)', accept=['parasintesis']),
        dict(term='acrónimo', definition='Sigla que se lee como una sola palabra, no letra por letra', example='OTAN [ó-tan], RENFE, OVNI', accept=['acronimo']),
        dict(term='apócope', definition='Reducción de una palabra por supresión de elementos finales', example='foto < fotografía, bici < bicicleta', accept=['apocope']),
        dict(term='calco semántico', definition='Adopción del significado de una palabra extranjera trasladado a una palabra ya existente en la lengua', example='ratón (del inglés mouse)', accept=['calco semantico', 'calco']),
        dict(term='neologismo', definition='Palabra de creación reciente incorporada al léxico de una lengua', example='infoentretenimiento, selfi, tuitear', accept=['neologismo']),
        dict(term='palabra-maleta', definition='Palabra formada por la fusión de partes de dos palabras: blended word', example='infoentretenimiento = información + entretenimiento', accept=['palabra maleta', 'blended word']),
    ],
    ex1=dict(
        title='Identifica el proceso de formación',
        questions=[
            ('¿Qué proceso forma la palabra <em>lavaplatos</em>?',
             ['Derivación por sufijación', 'Composición V+N', 'Parasíntesis', 'Acrónimo'],
             1, '<em>Lavaplatos</em> = <em>lavar + platos</em>: dos bases unidas → <em>composición</em> de tipo Verbo+Nombre.'),
            ('¿Qué proceso genera <em>aterrizar</em>?',
             ['Derivación simple con prefijo', 'Composición de dos sustantivos', 'Parasíntesis (a- + tierra + -izar)', 'Calco del inglés'],
             2, '<em>Aterrizar</em> no puede formarse sin el prefijo <em>a-</em> y el sufijo <em>-izar</em> juntos (*terrizar no existe) → <em>parasíntesis</em>.'),
            ('¿Cuál de estas palabras es un acrónimo?',
             ['DNI', 'OTAN', 'ONG', 'URL'],
             1, '<em>OTAN</em> se pronuncia como una palabra [ó-tan] → es un <em>acrónimo</em>. DNI, ONG y URL se deletrean.'),
            ('¿Qué proceso produce <em>chatear</em>?',
             ['Composición V+N', 'Calco semántico', 'Préstamo + sufijación verbal (-ear)', 'Apócope'],
             2, '<em>Chat</em> (inglés) + sufijo verbalizador <em>-ear</em> → <em>chatear</em>: anglicismo integrado mediante derivación.'),
            ('¿Cuál es un ejemplo de calco semántico del inglés?',
             ['Chatear', 'Ratón (= mouse informático)', 'Selfi', 'OTAN'],
             1, '<em>Ratón</em> toma el significado de <em>mouse</em> aplicándolo a una palabra española ya existente → <em>calco semántico</em>.'),
        ]
    ),
    ex2=dict(
        title='Analiza morfológicamente',
        questions=[
            ('Descompón <em>globalización</em> en sus morfemas y explica el proceso.',
             'global + -iz(ar) + -ación: sufijación doble (global → globalizar → globalización)',
             ['global + -izar + -acion', 'global + ización', 'global iz acion'],
             '<em>Global</em> (base adj.) + <em>-izar</em> (verbalizar) + <em>-ación</em> (nominalizar la acción): dos sufijaciones en cadena.'),
            ('¿Cuál es la palabra completa de la que viene <em>bici</em>? ¿Qué proceso es?',
             'bicicleta; apócope (supresión del final)',
             ['bicicleta', 'bicicleta apocope'],
             '<em>Bici</em> < <em>bicicleta</em>: se suprimen los elementos finales → <em>apócope</em>.'),
            ('Crea un neologismo en español para el concepto inglés «to google» (buscar en un buscador de internet) siguiendo el patrón de <em>chatear</em>.',
             'googlear',
             ['googlear'],
             'El sufijo <em>-ear</em> es el verbalizador estándar para anglicismos en español: <em>chat → chatear</em>, <em>google → googlear</em>. La RAE acepta <em>googlear</em>.'),
        ]
    ),
    ex3=dict(
        title='Formación de palabras en contexto',
        questions=[
            ('¿Cuál de estos procesos no existe en español?',
             ['Parasíntesis', 'Composición', 'Infijación (inserción en la raíz)', 'Derivación'],
             2, 'La <em>infijación</em> (insertar un morfema dentro de la raíz) no es productiva en español; la lengua usa prefijación y sufijación.'),
            ('¿Cuál de estas palabras es una palabra-maleta?',
             ['lavaplatos', 'globalización', 'infoentretenimiento', 'aterrizar'],
             2, '<em>Infoentretenimiento</em> fusiona partes de <em>información</em> y <em>entretenimiento</em> → palabra-maleta (<em>blended word</em>).'),
            ('La RAE recomienda <em>selfi</em> en lugar de <em>selfie</em>. ¿Por qué?',
             ['Porque selfie es una palabra inventada', 'Para adaptar el préstamo a la ortografía española', 'Porque selfi viene del francés', 'Para evitar el anglicismo'],
             1, 'La RAE adapta los préstamos a las convenciones ortográficas del español: <em>selfie</em> → <em>selfi</em> (sin -e final, como <em>taxi</em>).'),
            ('¿Cuál de estos términos es un neologismo por analogía?',
             ['Foto (< fotografía)', 'Infoentretenimiento', 'Kirchnerismo', 'OTAN'],
             2, '<em>Kirchnerismo</em> se forma por analogía con <em>franquismo, nazismo, marxismo</em>: nombre propio + <em>-ismo</em> para designar una corriente política.'),
        ]
    ),
)
