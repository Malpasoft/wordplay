"""espanol/ C2 Grammar – G01–G05"""

CHAPTERS = {}

# ─────────────────────────────────────────────
# G01 · gramatica-discursiva · Gramática del Discurso: Coherencia y Cohesión
# ─────────────────────────────────────────────
CHAPTERS['gramatica-discursiva'] = dict(
    level='c2', section='grammar', num='G01',
    short='Gramática del Discurso',
    title='La Gramática del Discurso: Coherencia y Cohesión Textual',
    subtitle='Analiza y construye textos con cohesión léxica, referencial y estructural a nivel C2',
    slides=[
        ('Cohesión: Los Cinco Mecanismos', None, """
<p style="margin:0 0 12px;font-size:.9rem">La cohesión mantiene unidos los elementos del texto mediante mecanismos formales.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Mecanismo</th><th style="padding:6px 8px;text-align:left">Descripción</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Referencia</td><td style="padding:6px 8px">Pronombres, demostrativos, artículo</td><td style="padding:6px 8px"><em>Juan llegó. <u>Él</u> estaba cansado</em></td></tr>
<tr><td style="padding:6px 8px">Sustitución</td><td style="padding:6px 8px">Un elemento reemplaza a otro</td><td style="padding:6px 8px"><em>¿Quieres café? — Sí, <u>uno</u> solo</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Elipsis</td><td style="padding:6px 8px">Omisión de elemento recuperable</td><td style="padding:6px 8px"><em>¿Has comido? — Sí, <u>Ø</u></em></td></tr>
<tr><td style="padding:6px 8px">Conjunción</td><td style="padding:6px 8px">Conectores que relacionan oraciones</td><td style="padding:6px 8px"><em>Llueve, <u>sin embargo</u> saldremos</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Cohesión léxica</td><td style="padding:6px 8px">Repetición, sinonimia, hiponimia</td><td style="padding:6px 8px"><em>El perro… <u>el animal</u>… <u>el can</u></em></td></tr>
</table>"""),
        ('La Referencia: Anáfora, Catáfora y Deixis', None, """
<p style="margin:0 0 12px;font-size:.9rem">Los elementos referenciales apuntan a entidades dentro o fuera del texto.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Tipo</th><th style="padding:6px 8px;text-align:left">Dirección</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Anáfora</td><td style="padding:6px 8px">Retoma lo ya dicho</td><td style="padding:6px 8px"><em>Compré un libro. <u>Este</u> me encantó</em></td></tr>
<tr><td style="padding:6px 8px">Catáfora</td><td style="padding:6px 8px">Anticipa lo que vendrá</td><td style="padding:6px 8px"><em><u>Esto</u> es lo que importa: la honestidad</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Deixis personal</td><td style="padding:6px 8px">Yo/tú/él (contexto comunicativo)</td><td style="padding:6px 8px"><em><u>Yo</u> llegué antes que <u>tú</u></em></td></tr>
<tr><td style="padding:6px 8px">Deixis espacial</td><td style="padding:6px 8px">Aquí/ahí/allí</td><td style="padding:6px 8px"><em>Ven <u>aquí</u> / Pon <u>eso</u> allí</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Deixis textual</td><td style="padding:6px 8px">Este/ese/aquel (posición en el texto)</td><td style="padding:6px 8px"><em><u>Aquello</u> de lo que hablamos ayer</em></td></tr>
</table>"""),
        ('Progresión Temática y Estructura Tema-Rema', None, """
<p style="margin:0 0 12px;font-size:.9rem">Cada oración tiene un punto de partida conocido (tema) y una aportación nueva (rema).</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Tipo</th><th style="padding:6px 8px;text-align:left">Patrón</th><th style="padding:6px 8px;text-align:left">Ejemplo esquemático</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Progresión lineal</td><td style="padding:6px 8px">Rema₁ → Tema₂</td><td style="padding:6px 8px">Juan fue al mercado. El mercado estaba cerrado.</td></tr>
<tr><td style="padding:6px 8px">Tema constante</td><td style="padding:6px 8px">Tema₁ = Tema₂ = Tema₃</td><td style="padding:6px 8px">Juan llegó. Juan saludó. Juan se sentó.</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Progresión ramificada</td><td style="padding:6px 8px">Hipertema → subtemas</td><td style="padding:6px 8px">El informe tiene dos partes. La primera… La segunda…</td></tr>
</table>
<p style="margin:12px 0 0;font-size:.83rem">En español, el rema (información nueva) tiende a ir al final de la oración.</p>"""),
        ('Cohesión Léxica: Redes Semánticas', None, """
<p style="margin:0 0 12px;font-size:.9rem">La cohesión léxica se logra mediante relaciones entre palabras.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Recurso</th><th style="padding:6px 8px;text-align:left">Descripción</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Repetición</td><td style="padding:6px 8px">Misma palabra (énfasis)</td><td style="padding:6px 8px"><em>La paz. Solo la paz importa</em></td></tr>
<tr><td style="padding:6px 8px">Sinonimia</td><td style="padding:6px 8px">Palabra de significado similar</td><td style="padding:6px 8px"><em>el automóvil… el vehículo… el coche</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Antonimia</td><td style="padding:6px 8px">Contraste semántico</td><td style="padding:6px 8px"><em>riqueza / pobreza</em></td></tr>
<tr><td style="padding:6px 8px">Hiponimia</td><td style="padding:6px 8px">General → específico</td><td style="padding:6px 8px"><em>animal → perro → labrador</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Meronimia</td><td style="padding:6px 8px">Todo → parte</td><td style="padding:6px 8px"><em>cara → nariz, ojos, boca</em></td></tr>
<tr><td style="padding:6px 8px">Isotopía</td><td style="padding:6px 8px">Red de términos del mismo campo</td><td style="padding:6px 8px"><em>hospital, médico, paciente, diagnóstico</em></td></tr>
</table>"""),
    ],
    traps=[
        ('*El libro lo compré. Él fue caro.', 'El libro lo compré. Fue caro.', '<em>Él</em> solo funciona como referencia a una persona, no a una cosa. Para objetos, use el pronombre neutro o estructuras sin pronombre.'),
        ('*Esto es lo que me gusta: leer, correr, y ella también.', 'Esto es lo que me gusta: leer y correr.', 'La catáfora <em>esto</em> debe estar seguida de su referente de forma inmediata y coherente.'),
        ('*Juan llegó cansado. El hombre se sentó.', 'Juan llegó cansado. Se sentó.', 'La sustitución con hiperónimo (<em>el hombre</em>) es válida, pero la elipsis verbal suele ser más natural en español.'),
        ('*Sin embargo, y además, el proyecto tuvo éxito.', 'Sin embargo, el proyecto tuvo éxito. Además, superó las expectativas.', 'No se encadenan conectores de funciones contrarias en la misma oración.'),
        ('*Isotopía: el campo semántico «cocina» incluye: coche, mesa, sartén.', 'Isotopía: el campo semántico «cocina» incluye: sartén, olla, cuchillo, fuego.', 'La isotopía exige que todos los términos pertenezcan coherentemente al mismo campo semántico.'),
    ],
    summary=[
        ('cohesión referencial', 'Pronombres y demostrativos retoman/anticipan elementos', '<em>Juan llegó; él estaba cansado</em>'),
        ('anáfora', 'El elemento referencial sigue al antecedente', '<em>Compré el libro; este me encantó</em>'),
        ('catáfora', 'El elemento referencial precede al referente', '<em>Esto es clave: la honestidad</em>'),
        ('tema-rema', 'Tema = información dada; rema = información nueva', 'Juan (tema) llegó tarde (rema)'),
        ('progresión temática', 'Lineal, constante o ramificada', 'Rema₁ → Tema₂ en progresión lineal'),
        ('cohesión léxica', 'Sinonimia, hiponimia, meronimia, isotopía', '<em>el vehículo… el coche… el automóvil</em>'),
        ('elipsis', 'Omisión de elemento recuperable del contexto', '<em>¿Has llegado? — Sí, [he llegado]</em>'),
    ],
    ex1=dict(
        title='Ejercicio 1: Mecanismos de cohesión',
        questions=[
            ('«El informe ya está redactado. ___ será entregado mañana.» El elemento subrayado es:',
             ['una catáfora', 'una anáfora pronominal', 'una elipsis', 'una conjunción'], 1,
             '<em>Este</em> retoma <em>el informe</em> ya mencionado → anáfora pronominal.'),
            ('«___ es lo que propongo: reducir los costes.» El subrayado es:',
             ['una anáfora', 'una catáfora', 'una sustitución', 'una repetición'], 1,
             '<em>Esto</em> anticipa el referente que viene después → catáfora.'),
            ('«El proyecto terminó. ___ fue un éxito.» ¿Qué pronombre corresponde?',
             ['Él', 'Este', 'Aquel', 'Eso'], 1,
             'Para objetos/eventos, el demostrativo neutro <em>esto/eso/aquello</em> o <em>este/ese/aquel</em> — aquí <em>este</em> con valor anafórico a evento.'),
            ('«Compramos fruta en el mercado: manzanas, peras y naranjas.» La relación entre <em>fruta</em> y los tres términos es:',
             ['sinonimia', 'antonimia', 'hiponimia', 'meronimia'], 2,
             '<em>Manzanas/peras/naranjas</em> son hipónimos de <em>fruta</em> (clase-miembro).'),
            ('En el texto «Juan estudió. Juan aprobó. Juan celebró», la progresión temática es:',
             ['lineal', 'constante', 'ramificada', 'mixta'], 1,
             'El mismo tema (Juan) se mantiene en todas las oraciones → progresión de tema constante.'),
            ('«El informe tiene dos partes. La primera trata del contexto. La segunda analiza los datos.» Progresión:',
             ['lineal', 'constante', 'ramificada', 'anafórica'], 2,
             'Un hipertema (<em>el informe</em>) genera subtemas (<em>la primera parte, la segunda parte</em>) → progresión ramificada.'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Identifica y completa',
        questions=[
            ('«Había una vez una princesa. _______ vivía en un castillo encantado.» Pronombre de anáfora correcto:',
             'Esta', ['Esta', 'Ella', 'Eso'],
             '<em>Esta</em> retoma <em>la princesa</em> con valor anafórico de proximidad textual.'),
            ('«Los científicos presentaron los resultados. _______ fueron sorprendentes.» Forma correcta:',
             'Estos', ['Estos', 'Ellos', 'Aquellos'],
             '<em>Estos</em> retoma <em>los resultados</em> (no personas, sin pronombre tónico).'),
            ('«Llueve mucho. _______, saldremos igualmente.» Conector de contraste:',
             'Sin embargo', ['Sin embargo', 'Por lo tanto', 'Además'],
             '<em>Sin embargo</em> introduce el contraste entre la lluvia y la decisión de salir.'),
            ('El mecanismo de cohesión en «el automóvil… el vehículo… el coche» es:',
             'sinonimia', ['sinonimia', 'hiponimia', 'catáfora'],
             'Tres palabras de significado próximo → cohesión por sinonimia.'),
            ('«¿Has visto la película? — Sí, _______ [vi].» Mecanismo de cohesión:',
             'elipsis', ['elipsis', 'sustitución', 'anáfora'],
             'El verbo <em>vi</em> se omite porque es recuperable → elipsis verbal.'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Cohesión y coherencia',
        questions=[
            ('¿Cuál de estos textos presenta mayor cohesión referencial?',
             ['Juan llegó. Juan se sentó. Juan habló.',
              'Juan llegó. Él se sentó. El hombre habló.',
              'Juan llegó. Este se sentó. Aquel habló.',
              'Juan llegó. Se sentó. Habló.'], 3,
             'La elipsis del sujeto es el recurso más natural en español; evita la repetición innecesaria.'),
            ('La isotopía léxica en un texto sobre medicina incluiría:',
             ['silla, ventana, cuaderno', 'paciente, diagnóstico, tratamiento', 'feliz, triste, enfadado', 'rápido, lento, pausado'], 1,
             '<em>Paciente, diagnóstico, tratamiento</em> pertenecen al campo semántico médico → isotopía.'),
            ('¿Cuál uso del demostrativo es catafórico?',
             ['El libro era azul. Este me gustó.', 'Esto es lo que quiero: libertad.', 'Aquellos días fueron felices.', 'Ese hombre de allí es mi padre.'], 1,
             '<em>Esto</em> precede a su referente (<em>libertad</em>) → catáfora.'),
            ('En «El proyecto fue aprobado. Además, recibirá financiación extra.», el conector:',
             ['introduce contraste', 'añade información', 'introduce consecuencia', 'introduce concesión'], 1,
             '<em>Además</em> añade una nueva información positiva → función de adición.'),
            ('¿Qué tipo de cohesión léxica hay entre <em>nariz</em> y <em>cara</em>?',
             ['sinonimia', 'antonimia', 'hiponimia', 'meronimia'], 3,
             '<em>Nariz</em> es parte de <em>cara</em> → relación todo-parte = meronimia.'),
        ]
    ),
    game_desc='Cohesión textual: referencia, sustitución, elipsis, progresión temática',
    items=[
        dict(term='anáfora', definition='Elemento referencial que retoma algo mencionado anteriormente', example='Juan llegó tarde. Él estaba cansado.', accept=['anáfora']),
        dict(term='catáfora', definition='Elemento referencial que anticipa algo mencionado después', example='Esto es lo que propongo: cancelar la reunión.', accept=['catáfora']),
        dict(term='elipsis', definition='Omisión de un elemento recuperable por el contexto', example='¿Has terminado? — Sí, [he terminado].', accept=['elipsis']),
        dict(term='isotopía', definition='Red de términos del mismo campo semántico que mantiene la unidad temática', example='hospital, médico, enfermera, diagnóstico, paciente', accept=['isotopía']),
        dict(term='progresión lineal', definition='El rema de una oración se convierte en el tema de la siguiente', example='Juan fue al mercado. El mercado estaba cerrado.', accept=['progresión lineal', 'progresión temática lineal']),
        dict(term='tema-rema', definition='Estructura informativa: tema = dado, rema = nuevo', example='Juan (tema) llegó tarde (rema).', accept=['tema-rema', 'tema rema']),
        dict(term='hiponimia', definition='Relación clase-miembro: el hipónimo es más específico que el hiperónimo', example='manzana (hipónimo) — fruta (hiperónimo)', accept=['hiponimia']),
        dict(term='sustitución', definition='Reemplazar un elemento por otro de significado equivalente en el contexto', example='¿Quieres un café? — Sí, uno solo.', accept=['sustitución']),
    ]
)

# ─────────────────────────────────────────────
# G02 · verbos-percepcion · Los Verbos de Percepción y Causativos
# ─────────────────────────────────────────────
CHAPTERS['verbos-percepcion'] = dict(
    level='c2', section='grammar', num='G02',
    short='Verbos de Percepción',
    title='Los Verbos de Percepción y las Construcciones Causativas',
    subtitle='Controla los matices de ver/oír + infinitivo/gerundio y las construcciones con hacer y dejar',
    slides=[
        ('Ver/Oír + Infinitivo vs. Gerundio', None, """
<p style="margin:0 0 12px;font-size:.9rem">La elección entre infinitivo y gerundio cambia el aspecto de la percepción.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Construcción</th><th style="padding:6px 8px;text-align:left">Aspecto</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">ver/oír + infinitivo</td><td style="padding:6px 8px">Acción completa percibida</td><td style="padding:6px 8px"><em>Vi salir al director</em></td></tr>
<tr><td style="padding:6px 8px">ver/oír + gerundio</td><td style="padding:6px 8px">Proceso en curso percibido</td><td style="padding:6px 8px"><em>Vi al director saliendo</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">ver/oír + que + ind</td><td style="padding:6px 8px">Percepción reportada</td><td style="padding:6px 8px"><em>Vi que salía / que había salido</em></td></tr>
<tr><td style="padding:6px 8px">Posición del CD</td><td style="padding:6px 8px">Antes del infinitivo o después</td><td style="padding:6px 8px"><em>Vi salir al director / Lo vi salir</em></td></tr>
</table>"""),
        ('Hacer + Infinitivo: La Causativa', None, """
<p style="margin:0 0 12px;font-size:.9rem"><em>Hacer</em> con infinitivo expresa que el sujeto provoca que otro realice la acción.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Construcción</th><th style="padding:6px 8px;text-align:left">Causado</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">hacer + inf (sin causado explícito)</td><td style="padding:6px 8px">Implícito</td><td style="padding:6px 8px"><em>Hizo limpiar la oficina</em></td></tr>
<tr><td style="padding:6px 8px">hacer + inf + a/que (causado)</td><td style="padding:6px 8px">CD o CI</td><td style="padding:6px 8px"><em>Hizo trabajar a los empleados / Hizo que trabajaran</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">hacerse + inf (reflexiva)</td><td style="padding:6px 8px">En beneficio propio</td><td style="padding:6px 8px"><em>Se hizo cortar el pelo</em></td></tr>
<tr><td style="padding:6px 8px">hacer + que + subj</td><td style="padding:6px 8px">Causativo analítico</td><td style="padding:6px 8px"><em>Hizo que todos salieran</em></td></tr>
</table>"""),
        ('Dejar + Infinitivo: Causativo Permisivo', None, """
<p style="margin:0 0 12px;font-size:.9rem"><em>Dejar</em> con infinitivo expresa permiso o no interferencia.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Construcción</th><th style="padding:6px 8px;text-align:left">Significado</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">dejar + inf</td><td style="padding:6px 8px">Permitir actuar</td><td style="padding:6px 8px"><em>Déjame hablar</em></td></tr>
<tr><td style="padding:6px 8px">dejar + que + subj</td><td style="padding:6px 8px">Permitir que otro haga</td><td style="padding:6px 8px"><em>Deja que ella lo explique</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">no dejar + inf</td><td style="padding:6px 8px">Impedir, prohibir</td><td style="padding:6px 8px"><em>No me dejas dormir</em></td></tr>
<tr><td style="padding:6px 8px">dejar de + inf</td><td style="padding:6px 8px">Cesativo (dejar de hacer)</td><td style="padding:6px 8px"><em>Dejó de fumar</em></td></tr>
</table>"""),
        ('Otros Verbos de Percepción y Sentido', None, """
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Verbo</th><th style="padding:6px 8px;text-align:left">Complemento</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">sentir</td><td style="padding:6px 8px">+ inf / ger / que + ind</td><td style="padding:6px 8px"><em>Sintió temblar la tierra / temblando</em></td></tr>
<tr><td style="padding:6px 8px">notar</td><td style="padding:6px 8px">+ adj / que + ind / cómo + ind</td><td style="padding:6px 8px"><em>Noté que estaba nerviosa / cómo temblaba</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">observar</td><td style="padding:6px 8px">+ cómo + ind</td><td style="padding:6px 8px"><em>Observó cómo lo construían</em></td></tr>
<tr><td style="padding:6px 8px">percibir</td><td style="padding:6px 8px">+ que + ind / cómo + ind</td><td style="padding:6px 8px"><em>Percibió que algo había cambiado</em></td></tr>
</table>"""),
    ],
    traps=[
        ('*Vi al director salir de la oficina inmediatamente (acción completa).', 'Vi al director salir de la oficina.', 'Con infinitivo se percibe la acción completa. <em>Inmediatamente</em> no indica proceso → infinitivo es correcto.'),
        ('*Hicieron que los empleados que limpiar.', 'Hicieron que los empleados limpiaran.', '<em>Hacer que + subj</em>: causativo analítico con subjuntivo, no infinitivo.'),
        ('*Déjame que hable.', 'Déjame hablar. / Deja que yo hable.', 'Con mismo sujeto → <em>déjame hablar</em> (inf). Con diferente sujeto → <em>deja que + subj</em>.'),
        ('*Oí a los pájaros cantar (proceso en curso, momento dado).', 'Oí a los pájaros cantando.', 'Proceso en curso percibido → gerundio: <em>oí a los pájaros <u>cantando</u>.</em>'),
        ('*Se hizo construir la casa por sí mismo.', 'Se hizo construir la casa (por un constructor).', '<em>Hacerse + inf</em> implica encargo a otro, no que lo haga uno mismo.'),
    ],
    summary=[
        ('ver/oír + inf', 'Percepción de acción completa', '<em>Vi llegar el tren</em>'),
        ('ver/oír + ger', 'Percepción de proceso en curso', '<em>Vi al tren llegando</em>'),
        ('hacer + inf', 'Causativo: causar que alguien haga algo', '<em>Hizo salir a todos</em>'),
        ('hacer que + subj', 'Causativo analítico', '<em>Hizo que salieran todos</em>'),
        ('dejar + inf', 'Permisivo: permitir que alguien haga algo', '<em>Déjame hablar</em>'),
        ('dejar que + subj', 'Permisivo con diferente sujeto', '<em>Deja que ella lo explique</em>'),
        ('notar/percibir + cómo', 'Percepción de proceso con cómo + indicativo', '<em>Noté cómo temblaba</em>'),
    ],
    ex1=dict(
        title='Ejercicio 1: Percepción y causativas',
        questions=[
            ('___ salir a todos los invitados a la vez — fue algo impresionante.',
             ['Vi a', 'Vi', 'Noté', 'Observé a'], 0,
             '<em>Ver + a + persona + infinitivo</em> (acción completa): <em><u>Vi a</u> todos los invitados salir.</em>'),
            ('___ los niños jugando en el jardín cuando pasé.',
             ['Vi a', 'Hice', 'Noté a', 'Observé'], 0,
             '<em>Ver + a + personas + gerundio</em> (proceso en curso): <em><u>Vi a</u> los niños jugando.</em>'),
            ('El jefe ___ al equipo repetir el análisis desde el principio.',
             ['dejó', 'hizo', 'notó', 'oyó'], 1,
             '<em>Hacer + inf</em> expresa causación directa: <em>hizo repetir al equipo.</em>'),
            ('— ¿Puedo usar el ordenador? — Claro, ___ lo usar.',
             ['hazle', 'déjale', 'deja', 'hazla'], 2,
             '<em>Dejar + inf</em> = permiso: <em><u>deja</u> usarlo.</em> (o: déjale usarlo)'),
            ('___ que algo había cambiado nada más entrar en la sala.',
             ['Noté', 'Hice', 'Vi', 'Percibí'], 3,
             '<em>Percibir que + indicativo</em>: percepción cognitiva de un estado: <em><u>Percibí</u> que algo había cambiado.</em>'),
            ('Nos ___ construir el proyecto sin ayuda externa.',
             ['hicieron', 'dejaron', 'vieron', 'oyeron'], 1,
             '<em>Dejar + inf</em> = permitir: <em>nos <u>dejaron</u> construirlo.</em>'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Infinitivo o gerundio',
        questions=[
            ('Cuando llegué, los trabajadores estaban en plena tarea. Los vi _______ (trabajar).',
             'trabajando', ['trabajando', 'trabajar'],
             'Proceso en curso en el momento de la percepción → gerundio: <em>los vi <u>trabajando</u>.</em>'),
            ('El tren llegó en el momento en que me asomé. Lo vi _______ (llegar).',
             'llegar', ['llegar', 'llegando'],
             'Acción puntual completa percibida → infinitivo: <em>lo vi <u>llegar</u>.</em>'),
            ('Oímos a los músicos _______ (tocar) durante toda la tarde desde la calle.',
             'tocando', ['tocando', 'tocar'],
             'Duración en curso → gerundio: <em>oímos a los músicos <u>tocando</u>.</em>'),
            ('Me hicieron _______ (esperar) más de dos horas en el vestíbulo.',
             'esperar', ['esperar', 'esperando'],
             'Causativa con <em>hacer + inf</em>: <em>me hicieron <u>esperar</u>.</em>'),
            ('Deja que ella _______ (decidir) a qué hora salimos.',
             'decida', ['decida', 'decidir'],
             '<em>Dejar que + subj</em> con diferente sujeto: <em>deja que ella <u>decida</u>.</em>'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Elige la construcción correcta',
        questions=[
            ('Para expresar que forzaste a alguien a trabajar, dices:',
             ['Lo dejé trabajar.', 'Lo hice trabajar.', 'Lo noté trabajar.', 'Lo vi trabajar.'], 1,
             '<em>Hacer + inf</em> = causativo (forzar/provocar): <em>Lo <u>hice</u> trabajar.</em>'),
            ('Para expresar que diste permiso a alguien, dices:',
             ['Lo hice hablar.', 'Lo noté hablar.', 'Lo dejé hablar.', 'Lo oí hablar.'], 2,
             '<em>Dejar + inf</em> = permisivo: <em>Lo <u>dejé</u> hablar.</em>'),
            ('«Sentí el suelo _______ bajo mis pies.» La forma que indica proceso es:',
             ['temblar', 'temblando', 'que temblaba', 'temblado'], 1,
             'Gerundio = proceso en curso: <em>Sentí el suelo <u>temblando</u>.</em>'),
            ('«___ que el proyecto acabaría a tiempo.» Percepción cognitiva:',
             ['Vi', 'Oí', 'Percibí', 'Dejé'], 2,
             '<em>Percibir que + ind</em> = percepción cognitiva de un hecho: <em><u>Percibí</u> que acabaría.</em>'),
            ('«Se ___ cortar el pelo en la mejor peluquería.» Causativa reflexiva:',
             ['hizo', 'dejó', 'vio', 'notó'], 0,
             '<em>Hacerse + inf</em> = causativa reflexiva (para beneficio propio): <em>se <u>hizo</u> cortar el pelo.</em>'),
        ]
    ),
    game_desc='Verbos de percepción y causativos: ver/oír + inf/ger, hacer y dejar',
    items=[
        dict(term='ver + infinitivo', definition='Percepción de una acción completa', example='Vi llegar a María.', accept=['ver + infinitivo', 'oír + infinitivo']),
        dict(term='ver + gerundio', definition='Percepción de una acción en progreso', example='Vi a María llegando.', accept=['ver + gerundio', 'oír + gerundio']),
        dict(term='hacer + infinitivo', definition='Causativa directa: provocar que alguien haga algo', example='Hicieron esperar a los clientes.', accept=['hacer + infinitivo', 'causativa hacer']),
        dict(term='hacer que + subjuntivo', definition='Causativa analítica con diferente sujeto', example='Hizo que todos salieran.', accept=['hacer que + subjuntivo']),
        dict(term='dejar + infinitivo', definition='Causativa permisiva: permitir que alguien haga algo', example='Déjame explicarlo.', accept=['dejar + infinitivo', 'dejar permisivo']),
        dict(term='dejar que + subjuntivo', definition='Permisivo con diferente sujeto explícito', example='Deja que ella decida.', accept=['dejar que + subjuntivo']),
        dict(term='hacerse + infinitivo', definition='Causativa reflexiva: encargar algo para el propio beneficio', example='Se hizo construir una casa.', accept=['hacerse + infinitivo']),
        dict(term='percibir/notar + cómo', definition='Percepción cognitiva de un proceso con cómo + indicativo', example='Noté cómo cambiaba su expresión.', accept=['percibir + cómo', 'notar + cómo']),
    ]
)

# ─────────────────────────────────────────────
# G03 · aspecto-lexico · El Aspecto Léxico (Aktionsart)
# ─────────────────────────────────────────────
CHAPTERS['aspecto-lexico'] = dict(
    level='c2', section='grammar', num='G03',
    short='Aspecto Léxico',
    title='El Aspecto Léxico (Aktionsart): Clases de Situación y Aspecto Gramatical',
    subtitle='Comprende la interacción entre el tipo léxico de los verbos y los tiempos gramaticales del español',
    slides=[
        ('Las Cuatro Clases de Situación', None, """
<p style="margin:0 0 12px;font-size:.9rem">Los verbos se clasifican según sus propiedades aspectuales internas (Aktionsart).</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Clase</th><th style="padding:6px 8px;text-align:left">Dinámico</th><th style="padding:6px 8px;text-align:left">Télico</th><th style="padding:6px 8px;text-align:left">Puntual</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Estado</td><td style="padding:6px 8px">No</td><td style="padding:6px 8px">No</td><td style="padding:6px 8px">No</td><td style="padding:6px 8px"><em>saber, tener, querer</em></td></tr>
<tr><td style="padding:6px 8px">Actividad</td><td style="padding:6px 8px">Sí</td><td style="padding:6px 8px">No</td><td style="padding:6px 8px">No</td><td style="padding:6px 8px"><em>correr, hablar, nadar</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Realización</td><td style="padding:6px 8px">Sí</td><td style="padding:6px 8px">Sí</td><td style="padding:6px 8px">No</td><td style="padding:6px 8px"><em>escribir una carta, pintar un cuadro</em></td></tr>
<tr><td style="padding:6px 8px">Logro</td><td style="padding:6px 8px">Sí</td><td style="padding:6px 8px">Sí</td><td style="padding:6px 8px">Sí</td><td style="padding:6px 8px"><em>llegar, encontrar, morir</em></td></tr>
</table>"""),
        ('Cómo el Aspecto Gramatical Modifica el Aktionsart', None, """
<p style="margin:0 0 12px;font-size:.9rem">La interacción entre el tiempo verbal y el Aktionsart puede cambiar el significado.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Verbo</th><th style="padding:6px 8px;text-align:left">Pretérito indefinido</th><th style="padding:6px 8px;text-align:left">Imperfecto</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">saber (estado)</td><td style="padding:6px 8px"><em>supo</em> = <strong>encontró/descubrió</strong></td><td style="padding:6px 8px"><em>sabía</em> = estado continuo</td></tr>
<tr><td style="padding:6px 8px">conocer (estado)</td><td style="padding:6px 8px"><em>conoció</em> = <strong>conoció por 1ª vez</strong></td><td style="padding:6px 8px"><em>conocía</em> = ya lo conocía</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">querer (estado)</td><td style="padding:6px 8px"><em>quiso</em> = <strong>intentó</strong></td><td style="padding:6px 8px"><em>quería</em> = deseaba</td></tr>
<tr><td style="padding:6px 8px">no querer (estado)</td><td style="padding:6px 8px"><em>no quiso</em> = <strong>se negó</strong></td><td style="padding:6px 8px"><em>no quería</em> = no deseaba</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">poder (estado)</td><td style="padding:6px 8px"><em>pudo</em> = <strong>logró</strong></td><td style="padding:6px 8px"><em>podía</em> = tenía capacidad</td></tr>
</table>"""),
        ('Complementos que Cambian el Aktionsart', None, """
<p style="margin:0 0 12px;font-size:.9rem">El CD puede convertir una actividad en realización (efecto telicizante).</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Sin CD específico → actividad</th><th style="padding:6px 8px;text-align:left">Con CD específico → realización</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>correr</em> (sin límite)</td><td style="padding:6px 8px"><em>correr diez kilómetros</em> (límite)</td></tr>
<tr><td style="padding:6px 8px"><em>leer</em> (indefinido)</td><td style="padding:6px 8px"><em>leer la novela</em> (hasta el final)</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>escribir</em></td><td style="padding:6px 8px"><em>escribir un informe</em></td></tr>
<tr><td style="padding:6px 8px"><em>comer</em></td><td style="padding:6px 8px"><em>comer la manzana</em></td></tr>
</table>"""),
        ('Aktionsart en la Narrativa', None, """
<p style="margin:0 0 12px;font-size:.9rem">En la narrativa, el Aktionsart y el tiempo verbal interaccionan de manera predecible.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Tiempo verbal</th><th style="padding:6px 8px;text-align:left">Clases preferentes</th><th style="padding:6px 8px;text-align:left">Función</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Imperfecto</td><td style="padding:6px 8px">Estados, actividades</td><td style="padding:6px 8px">Escenario/fondo</td></tr>
<tr><td style="padding:6px 8px">Indefinido</td><td style="padding:6px 8px">Logros, realizaciones</td><td style="padding:6px 8px">Eventos/primer plano</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Pluscuamperfecto</td><td style="padding:6px 8px">Realizaciones, logros</td><td style="padding:6px 8px">Evento anterior al pasado</td></tr>
</table>"""),
    ],
    traps=[
        ('*Ayer supe la noticia — (con imperfecto para estado de conocimiento nuevo).', 'Ayer supe la noticia. (indefinido = descubrí)', '<em>Supo</em> en indefinido indica adquisición repentina del conocimiento.'),
        ('Corrí durante una hora (actividad) ≠ Corrí la maratón (realización).', 'Corrí durante una hora vs. Corrí la maratón.', '<em>Correr</em> es actividad sin CD; con CD específico pasa a realización con límite natural.'),
        ('*Conocía a María en la fiesta.', 'Conocí a María en la fiesta.', '<em>Conocer</em> en indefinido = primer encuentro (logro). Imperfecto = ya la conocía.'),
        ('*Pude el ejercicio ayer (con acepción de capacidad).', 'Pude terminar el ejercicio. (= logré)', '<em>Pudo</em> en indefinido = logró, no simplemente tenía capacidad.'),
        ('El gerundio es incompatible con los logros puros: *estaba llegando (punto único).', 'Estaba llegando = proceso de aproximación; llegó = el logro.', 'Con verbos de logro, el gerundio indica la fase previa al logro, no el logro en sí.'),
    ],
    summary=[
        ('estado', 'No dinámico, no télico, no puntual: saber, tener, querer', '<em>Sabía la respuesta (continuo)</em>'),
        ('actividad', 'Dinámico, atélico: correr, hablar, nadar', '<em>Corrí durante una hora</em>'),
        ('realización', 'Dinámico, télico, durativo: escribir una carta', '<em>Escribí el informe en dos horas</em>'),
        ('logro', 'Dinámico, télico, puntual: llegar, morir, encontrar', '<em>Llegó a las tres</em>'),
        ('estado + indefinido', 'Cambio de estado (incoativo): supo = descubrió', '<em>Supo la verdad = la descubrió</em>'),
        ('telicización por CD', 'CD específico convierte actividad en realización', '<em>correr → correr 10 km</em>'),
        ('imperfecto/indefinido', 'Fondo (estados/actividades) / primer plano (logros/realizaciones)', 'Era tarde (imperf.) cuando llegó (ind.)'),
    ],
    ex1=dict(
        title='Ejercicio 1: Clases de Aktionsart',
        questions=[
            ('¿A qué clase pertenece «escribir una carta»?',
             ['estado', 'actividad', 'realización', 'logro'], 2,
             '<em>Escribir una carta</em>: dinámico, télico (tiene un límite natural), durativo → realización.'),
            ('¿A qué clase pertenece «llegar»?',
             ['estado', 'actividad', 'realización', 'logro'], 3,
             '<em>Llegar</em>: puntual, télico → logro.'),
            ('«Supo que había mentido» — ¿Qué significado tiene <em>supo</em> en indefinido?',
             ['sabía ya', 'descubrió', 'dudaba', 'preguntó'], 1,
             'Estado + indefinido → cambio de estado incoativo: <em>supo = descubrió, se enteró.</em>'),
            ('¿Cuál de estos verbos pasa de actividad a realización al añadir un CD?',
             ['saber', 'llegar', 'leer', 'existir'], 2,
             '<em>Leer</em> (actividad) + <em>la novela</em> (CD específico) = realización con límite.'),
            ('En la narrativa, ¿qué tiempo se usa para el fondo/escenario?',
             ['indefinido', 'imperfecto', 'pluscuamperfecto', 'presente'], 1,
             'El imperfecto expresa estados y actividades de fondo; el indefinido avanza la trama.'),
            ('«No quiso hablar con nadie» — <em>no quiso</em> significa:',
             ['no deseaba', 'se negó', 'no podía', 'no intentó'], 1,
             '<em>No querer</em> en indefinido = negativa/rechazo activo: <em>se negó.</em>'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Aspecto y tiempo',
        questions=[
            ('¿Cómo cambia el significado de «conocer» según el tiempo? Completa: «Cuando le conocí, ya _______ a su familia.»',
             'conocía', ['conocía', 'conocí'],
             '<em>Conocer</em> en imperfecto = estado continuo (ya la conocía antes).'),
            ('La diferencia entre «corrí» y «corrí 10 km»: el primero es _______ y el segundo es _______.',
             'actividad / realización', ['actividad / realización', 'logro / actividad'],
             'CD específico (10 km) teliciza el verbo: actividad → realización.'),
            ('«Ayer _______ (poder) terminar el proyecto a tiempo.» (= lo logramos)',
             'pudimos', ['pudimos', 'podíamos'],
             '<em>Poder</em> en indefinido = logro (capacidad realizada): <em><u>pudimos</u> terminar.</em>'),
            ('En la frase «Hacía sol cuando <em>llegué</em>», ¿qué tiempo es <em>hacía sol</em>?',
             'indefinido', ['indefinido', 'imperfecto', 'pluscuamperfecto'],
             '<em>Hacía sol</em> es imperfecto — estado de fondo en el que ocurre el logro <em>llegué</em>.'),
            ('«Mientras _______ (leer) el periódico, sonó el teléfono.» Actividad de fondo:',
             'leía', ['leía', 'leí'],
             'Actividad de fondo → imperfecto: <em>mientras <u>leía</u> el periódico.</em>'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Aktionsart en contexto',
        questions=[
            ('¿Cuál de estos sintagmas convierte <em>comer</em> en una realización?',
             ['comer con amigos', 'comer la tortilla entera', 'comer mucho', 'comer con prisa'], 1,
             'CD específico y limitado (<em>la tortilla entera</em>) teliciza el verbo → realización.'),
            ('«Cuando era niño, _______ (saber) muchas canciones.» ¿Qué forma es correcta?',
             ['sabía', 'supo', 'ha sabido', 'habrá sabido'], 0,
             'Estado continuo en el pasado → imperfecto: <em><u>sabía</u> muchas canciones.</em>'),
            ('«De repente _______ (encontrar) la solución.» El verbo es un logro en:',
             ['imperfecto', 'indefinido', 'futuro', 'pluscuamperfecto'], 1,
             'Logros en narrativa → indefinido: <em><u>encontró</u> la solución</em> (puntual, télico).'),
            ('¿Qué tiene de especial «estaba llegando» frente a «llegó»?',
             ['es un estado', 'indica la fase previa al logro', 'es un hábito pasado', 'indica futuro'], 1,
             'Con verbos de logro, el gerundio indica el proceso de acercamiento al punto: <em>estaba llegando = se estaba acercando.</em>'),
            ('La clase Aktionsart de «morir» es:',
             ['estado', 'actividad', 'realización', 'logro'], 3,
             '<em>Morir</em>: télico, puntual → logro.'),
        ]
    ),
    game_desc='Aspecto léxico: clases de situación, interacción con tiempos y narrativa',
    items=[
        dict(term='estado', definition='Clase Aktionsart: no dinámico, atélico, sin límite natural (saber, tener, amar)', example='Sabía la respuesta.', accept=['estado', 'verbo de estado']),
        dict(term='actividad', definition='Clase Aktionsart: dinámico, atélico, sin límite natural (correr, hablar)', example='Corrió durante una hora.', accept=['actividad', 'verbo de actividad']),
        dict(term='realización', definition='Clase Aktionsart: dinámico, télico, durativo (escribir una carta, construir una casa)', example='Escribió la carta en media hora.', accept=['realización', 'verbo de realización']),
        dict(term='logro', definition='Clase Aktionsart: dinámico, télico, puntual (llegar, encontrar, morir)', example='El tren llegó a las tres.', accept=['logro', 'verbo de logro']),
        dict(term='telicización', definition='Proceso por el que un CD específico convierte una actividad en realización', example='correr → correr 10 km', accept=['telicización']),
        dict(term='estado + indefinido', definition='Estado en indefinido → cambio de estado incoativo (adquisición)', example='supo = descubrió / conoció = conoció por primera vez', accept=['estado + indefinido', 'cambio de estado']),
        dict(term='fondo narrativo', definition='El imperfecto sitúa estados y actividades como escenario del relato', example='Llovía cuando llegamos.', accept=['fondo narrativo', 'imperfecto narrativo']),
        dict(term='primer plano narrativo', definition='El indefinido avanza la trama con logros y realizaciones', example='De repente llegó María.', accept=['primer plano narrativo', 'indefinido narrativo']),
    ]
)

# ─────────────────────────────────────────────
# G04 · tiempos-literarios · Tiempos Literarios y Variación en el Registro
# ─────────────────────────────────────────────
CHAPTERS['tiempos-literarios'] = dict(
    level='c2', section='grammar', num='G04',
    short='Tiempos Literarios',
    title='Los Tiempos Literarios y la Variación Dialectal en los Tiempos del Pasado',
    subtitle='Reconoce el pretérito anterior, el futuro de subjuntivo y las diferencias España-América en el pasado',
    slides=[
        ('El Pretérito Anterior: Anterioridad Inmediata', None, """
<p style="margin:0 0 12px;font-size:.9rem">El pretérito anterior (hubo + participio) expresa una acción inmediatamente anterior a otra del pasado. Hoy es casi exclusivo del registro literario.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Formación</th><th style="padding:6px 8px;text-align:left">Ejemplo literario</th><th style="padding:6px 8px;text-align:left">Equivalente coloquial</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">hubo + participio</td><td style="padding:6px 8px"><em>Cuando hubo terminado, se marchó</em></td><td style="padding:6px 8px"><em>Cuando terminó, se marchó</em></td></tr>
<tr><td style="padding:6px 8px">hubiste + part.</td><td style="padding:6px 8px"><em>Apenas hubiste dicho eso…</em></td><td style="padding:6px 8px"><em>Apenas dijiste eso…</em></td></tr>
</table>
<p style="margin:10px 0 0;font-size:.83rem">Aparece solo tras <em>cuando, después de que, apenas, en cuanto, no bien, tan pronto como</em> + acción puntual inmediata.</p>"""),
        ('El Futuro de Subjuntivo', None, """
<p style="margin:0 0 12px;font-size:.9rem">El futuro de subjuntivo (amare / hubiere amado) es arcaico. Sobrevive en lenguaje jurídico, refranes y fórmulas.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Contexto</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Texto legal</td><td style="padding:6px 8px"><em>El que infringiere esta norma…</em></td></tr>
<tr><td style="padding:6px 8px">Refrán</td><td style="padding:6px 8px"><em>Adonde fueres, haz lo que vieres</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Bíblico/formal</td><td style="padding:6px 8px"><em>Sea lo que fuere</em></td></tr>
</table>
<p style="margin:10px 0 0;font-size:.83rem">En el español moderno se sustituye por presente de subjuntivo o indicativo.</p>"""),
        ('Variación España vs. Latinoamérica en el Pasado', None, """
<p style="margin:0 0 12px;font-size:.9rem">El uso del pretérito perfecto compuesto varía significativamente entre regiones.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Contexto</th><th style="padding:6px 8px;text-align:left">España (perf. compuesto)</th><th style="padding:6px 8px;text-align:left">Latinoamérica (indefinido)</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Hoy</td><td style="padding:6px 8px"><em>He llegado esta mañana</em></td><td style="padding:6px 8px"><em>Llegué esta mañana</em></td></tr>
<tr><td style="padding:6px 8px">Experiencia vital</td><td style="padding:6px 8px"><em>He estado en París</em></td><td style="padding:6px 8px"><em>Estuve en París</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Noticia reciente</td><td style="padding:6px 8px"><em>Ha ganado el Premio Nobel</em></td><td style="padding:6px 8px"><em>Ganó el Premio Nobel</em></td></tr>
</table>"""),
        ('El Imperfecto con Valor de Condicional', None, """
<p style="margin:0 0 12px;font-size:.9rem">En el habla coloquial y en el discurso periodístico, el imperfecto puede sustituir al condicional.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Registro</th><th style="padding:6px 8px;text-align:left">Con imperfecto</th><th style="padding:6px 8px;text-align:left">Con condicional</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Coloquial hipotético</td><td style="padding:6px 8px"><em>Si supiera, <u>te lo decía</u></em></td><td style="padding:6px 8px"><em>Si supiera, <u>te lo diría</u></em></td></tr>
<tr><td style="padding:6px 8px">Periodístico</td><td style="padding:6px 8px"><em>El acuerdo <u>se firmaba</u> ayer</em></td><td style="padding:6px 8px"><em>El acuerdo se firmó ayer</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Deseo hipotético</td><td style="padding:6px 8px"><em>¡Yo me <u>iba</u> ahora mismo!</em></td><td style="padding:6px 8px"><em>¡Yo me iría ahora mismo!</em></td></tr>
</table>"""),
    ],
    traps=[
        ('*Hubo terminado cuando llegué.', 'Cuando hubo terminado, llegué.', 'El pretérito anterior va en la subordinada temporal; la acción principal va en indefinido.'),
        ('*Si hubiere sabido, habría venido (moderno).', 'Si hubiera sabido, habría venido.', 'El futuro de subjuntivo es arcaico. En el español moderno se usa el imperfecto de subjuntivo.'),
        ('*Llegaste ayer por la mañana (en España con referencia a hoy).', 'Has llegado esta mañana (España) / Llegaste esta mañana (Latinoamérica).', 'En España, el perfecto compuesto se usa para acciones del mismo día o conectadas al presente.'),
        ('*No bien terminé el examen, lo entregué (oral moderno).', 'En cuanto terminé el examen, lo entregué.', '<em>No bien</em> con pretérito anterior es literario; en el habla actual se usa indefinido.'),
        ('*Hube escrito la carta (sin referencia a acción inmediatamente posterior).', 'Escribí la carta.', 'El pretérito anterior solo aparece cuando la acción es inmediatamente anterior a otra acción pasada.'),
    ],
    summary=[
        ('pretérito anterior', 'Hubo + participio — acción inmediatamente anterior (literario)', '<em>Cuando hubo terminado, salió</em>'),
        ('futuro de subjuntivo', 'Amare/hubiere amado — arcaico, solo jurídico y refranes', '<em>Adonde fueres, haz lo que vieres</em>'),
        ('perfecto compuesto (España)', 'He + part — hoy, esta semana, experiencia vital', '<em>He llegado esta mañana</em>'),
        ('indefinido (Latinoamérica)', 'Sustituye al perf. compuesto en casi todos los contextos', '<em>Llegué esta mañana</em>'),
        ('imperfecto por condicional', 'Coloquial/periodístico: si supiera, te lo decía', '<em>Si pudiera, lo hacía hoy mismo</em>'),
        ('condicional por imperfecto subj.', 'Registro formal de hipótetico: habría hecho', '<em>Si lo hubiera sabido, habría venido</em>'),
        ('no bien/apenas + pret. ant.', 'Anterioridad inmediata en prosa narrativa formal', '<em>Apenas hubo dicho eso, salieron</em>'),
    ],
    ex1=dict(
        title='Ejercicio 1: Tiempos literarios y variación',
        questions=[
            ('«Cuando _______ el informe, lo presentó al comité.» (literario, anterioridad inmediata)',
             ['terminó', 'había terminado', 'hubo terminado', 'terminara'], 2,
             'Pretérito anterior = anterioridad inmediata en registro literario: <em>cuando <u>hubo terminado</u>.</em>'),
            ('«El que _______ esta normativa recibirá una multa.» (texto jurídico)',
             ['infringe', 'infringiera', 'infringiere', 'haya infringido'], 2,
             'Futuro de subjuntivo en texto legal: <em>el que <u>infringiere</u>.</em>'),
            ('En España, ¿cuál es la forma más natural para hablar de algo ocurrido hoy?',
             ['Llegué esta mañana', 'He llegado esta mañana', 'Había llegado esta mañana', 'Llegaría esta mañana'], 1,
             'En España, el perfecto compuesto (<em>he llegado</em>) se usa para acciones del mismo día.'),
            ('En Latinoamérica, ¿cuál es la forma habitual para la misma situación?',
             ['He llegado esta mañana', 'Llegué esta mañana', 'Había llegado esta mañana', 'Llego esta mañana'], 1,
             'En Latinoamérica, el indefinido sustituye al perfecto compuesto incluso para hoy.'),
            ('«Si tuviera dinero, me _______ (ir) ahora mismo.» Forma coloquial:',
             ['iría', 'iba', 'fuera', 'vaya'], 1,
             'Imperfecto con valor de condicional en registro coloquial: <em>me <u>iba</u>.</em>'),
            ('El pretérito anterior aparece solo después de:',
             ['porque, aunque, si', 'cuando, apenas, no bien, en cuanto', 'pero, sino, sin embargo', 'que, el que, quien'], 1,
             'Las conjunciones temporales de anterioridad inmediata introducen el pretérito anterior.'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Completa con la forma adecuada',
        questions=[
            ('El texto jurídico dice: «Quien _______ (falsificar) documentos será sancionado.»',
             'falsificare', ['falsificare', 'falsifique', 'falsificara'],
             'Futuro de subjuntivo en texto legal: <em><u>falsificare</u>.</em>'),
            ('(España, experiencia vital) «¿Alguna vez _______ (estar) en Tokio?»',
             'has estado', ['has estado', 'estuviste', 'habías estado'],
             'Perfecto compuesto para experiencia vital en España: <em><u>Has estado</u> en Tokio?</em>'),
            ('(Latinoamérica) «¿Alguna vez _______ (estar) en Tokio?»',
             'estuviste', ['estuviste', 'has estado', 'habías estado'],
             'En Latinoamérica, indefinido para experiencia vital: <em><u>Estuviste</u> en Tokio?</em>'),
            ('Apenas _______ (terminar) de hablar cuando empezaron los aplausos. (Literario)',
             'hubo terminado', ['hubo terminado', 'terminó', 'había terminado'],
             'Pretérito anterior tras <em>apenas</em>: <em>Apenas <u>hubo terminado</u>.</em>'),
            ('«Si pudiera, lo _______ (hacer) ahora mismo.» Forma coloquial:',
             'hacía', ['hacía', 'haría', 'hiciera'],
             'Imperfecto por condicional en registro coloquial: <em>lo <u>hacía</u>.</em>'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Identifica el tiempo y el registro',
        questions=[
            ('«Adonde fueres, haz lo que vieres.» ¿Qué tiempo verbal es <em>fueres</em>?',
             ['imperfecto de subjuntivo', 'futuro de subjuntivo', 'presente de subjuntivo', 'condicional'], 1,
             '<em>Fueres</em> = futuro de subjuntivo arcaico, conservado en refranes.'),
            ('«No bien hubo salido el sol, los pájaros comenzaron a cantar.» ¿Qué tiempo es <em>hubo salido</em>?',
             ['pluscuamperfecto', 'pretérito anterior', 'futuro perfecto', 'condicional compuesto'], 1,
             '<em>Hubo salido</em> = pretérito anterior (anterioridad inmediata, registro literario).'),
            ('¿En qué variedad del español es más natural «¿Ya comiste?» (en lugar de «¿Ya has comido?»)?',
             ['España peninsular', 'Latinoamérica', 'Español formal escrito', 'Periodismo europeo'], 1,
             'En Latinoamérica el indefinido sustituye al perfecto compuesto en todos los contextos.'),
            ('«Si tuviéramos más tiempo, lo hacíamos mejor.» ¿Qué forma sustituye al condicional?',
             ['el pluscuamperfecto', 'el imperfecto de indicativo', 'el futuro', 'el presente'], 1,
             'El imperfecto de indicativo (<em>hacíamos</em>) sustituye al condicional en registro coloquial.'),
            ('¿En qué contexto es correcto usar el futuro de subjuntivo hoy en día?',
             ['conversación informal', 'texto legal o jurídico', 'correo electrónico', 'narrativa moderna'], 1,
             'El futuro de subjuntivo sobrevive en textos legales/jurídicos y fórmulas formulaicas.'),
        ]
    ),
    game_desc='Pretérito anterior, futuro de subjuntivo y variación dialectal en el pasado',
    items=[
        dict(term='pretérito anterior', definition='Hubo + participio: acción inmediatamente anterior en registro literario', example='Cuando hubo terminado, se fue.', accept=['pretérito anterior']),
        dict(term='futuro de subjuntivo', definition='Forma arcaica (amare) conservada en textos legales y refranes', example='El que infringiere esta norma…', accept=['futuro de subjuntivo']),
        dict(term='perfecto compuesto (España)', definition='He + participio: acciones del mismo día o conectadas al presente (España)', example='He llegado esta mañana.', accept=['perfecto compuesto España', 'pretérito perfecto compuesto']),
        dict(term='indefinido (latinoamérica)', definition='Sustituyeal perfecto compuesto en casi todos los contextos en Latinoamérica', example='Llegué esta mañana.', accept=['indefinido latinoamérica']),
        dict(term='imperfecto por condicional', definition='En registro coloquial, el imperfecto puede reemplazar al condicional', example='Si pudiera, lo hacía ya.', accept=['imperfecto por condicional']),
        dict(term='anterioridad inmediata', definition='El pretérito anterior indica que la acción ocurrió inmediatamente antes de otra', example='No bien hubo salido, llegaron.', accept=['anterioridad inmediata']),
        dict(term='variación dialectal', definition='Diferencias en el uso de tiempos del pasado entre España y Latinoamérica', example='He comido (ES) / Comí (LA)', accept=['variación dialectal', 'variación regional']),
        dict(term='imperfecto periodístico', definition='Uso del imperfecto para presentar hechos recientes como si fueran en curso', example='El acuerdo se firmaba ayer.', accept=['imperfecto periodístico']),
    ]
)

# ─────────────────────────────────────────────
# G05 · estilo-nominal · El Estilo Nominal y la Escritura Académica
# ─────────────────────────────────────────────
CHAPTERS['estilo-nominal'] = dict(
    level='c2', section='grammar', num='G05',
    short='Estilo Nominal',
    title='El Estilo Nominal y la Escritura Académica en Español',
    subtitle='Domina el estilo nominal, la nominalización y los recursos retóricos del texto académico y formal',
    slides=[
        ('El Estilo Nominal: Definición y Recursos', None, """
<p style="margin:0 0 12px;font-size:.9rem">El estilo nominal subordina el verbo al sustantivo, característico del registro académico y jurídico.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Estilo verbal (coloquial)</th><th style="padding:6px 8px;text-align:left">Estilo nominal (formal)</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>Los precios subieron mucho</em></td><td style="padding:6px 8px"><em>Se produjo un fuerte aumento de los precios</em></td></tr>
<tr><td style="padding:6px 8px"><em>Los científicos descubrieron</em></td><td style="padding:6px 8px"><em>El descubrimiento por parte de los científicos</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>Se decidió que…</em></td><td style="padding:6px 8px"><em>La decisión de que…</em></td></tr>
<tr><td style="padding:6px 8px"><em>Hay que analizar los datos</em></td><td style="padding:6px 8px"><em>Es necesario proceder al análisis de los datos</em></td></tr>
</table>"""),
        ('Nominalización: Sufijos Productivos', None, """
<p style="margin:0 0 12px;font-size:.9rem">Los sustantivos deverbales y deadjetivales son el núcleo del estilo nominal.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Sufijo</th><th style="padding:6px 8px;text-align:left">Base</th><th style="padding:6px 8px;text-align:left">Nominalización</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">-ción/-sión</td><td style="padding:6px 8px">analizar</td><td style="padding:6px 8px"><em>el análisis / la analización</em></td></tr>
<tr><td style="padding:6px 8px">-miento</td><td style="padding:6px 8px">desarrollar</td><td style="padding:6px 8px"><em>el desarrollo / el desenvolvimiento</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">-eza/-dad</td><td style="padding:6px 8px">rico / real</td><td style="padding:6px 8px"><em>la riqueza / la realidad</em></td></tr>
<tr><td style="padding:6px 8px">-aje</td><td style="padding:6px 8px">montar</td><td style="padding:6px 8px"><em>el montaje</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">-ura</td><td style="padding:6px 8px">alto / frío</td><td style="padding:6px 8px"><em>la altura / la frialdad</em></td></tr>
<tr><td style="padding:6px 8px">Infinitivo</td><td style="padding:6px 8px">deber</td><td style="padding:6px 8px"><em>el deber / el poder</em></td></tr>
</table>"""),
        ('Verbos de Apoyo y Perífrasis Nominales', None, """
<p style="margin:0 0 12px;font-size:.9rem">El estilo nominal combina verbos de apoyo (hacer, realizar, llevar a cabo, efectuar) con sustantivos deverbales.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Verbo simple</th><th style="padding:6px 8px;text-align:left">Verbo de apoyo + sustantivo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>analizar</em></td><td style="padding:6px 8px"><em>llevar a cabo un análisis de</em></td></tr>
<tr><td style="padding:6px 8px"><em>proponer</em></td><td style="padding:6px 8px"><em>realizar una propuesta sobre</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>decidir</em></td><td style="padding:6px 8px"><em>tomar una decisión acerca de</em></td></tr>
<tr><td style="padding:6px 8px"><em>comparar</em></td><td style="padding:6px 8px"><em>efectuar una comparación entre</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>revisar</em></td><td style="padding:6px 8px"><em>proceder a la revisión de</em></td></tr>
</table>"""),
        ('Recursos de la Escritura Académica', None, """
<p style="margin:0 0 12px;font-size:.9rem">El texto académico combina nominalización, pasiva, impersonal y marcadores de evidencialidad.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Recurso</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Pasiva refleja</td><td style="padding:6px 8px"><em>Se observa un aumento significativo</em></td></tr>
<tr><td style="padding:6px 8px">Impersonal</td><td style="padding:6px 8px"><em>Cabe señalar que / conviene destacar</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Evidencialidad</td><td style="padding:6px 8px"><em>Según los datos analizados / de acuerdo con</em></td></tr>
<tr><td style="padding:6px 8px">Modalidad epistémica</td><td style="padding:6px 8px"><em>Cabría afirmar / podría considerarse</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Primera persona plural</td><td style="padding:6px 8px"><em>Proponemos / observamos / concluimos</em></td></tr>
</table>"""),
    ],
    traps=[
        ('*Se produjo un suceso de incremento de precios.', 'Se produjo un incremento de precios.', 'La nominalización no necesita complementos redundantes. El sustantivo deverbal incluye ya el significado del proceso.'),
        ('*El análisis de los datos fue realizado por nosotros.', 'Se procedió al análisis de los datos. / Los datos fueron analizados.', 'En el texto académico se prefiere la impersonal o la pasiva refleja para evitar el agente explícito.'),
        ('*Hacemos un análisis de los resultados que tenemos.', 'Se lleva a cabo un análisis de los resultados obtenidos.', 'El estilo académico prefiere el verbo de apoyo formal (<em>llevar a cabo</em>) y el participio adjetival (<em>obtenidos</em>).'),
        ('*La llegada de los resultados se produjo ayer.', 'Los resultados llegaron ayer. / Se obtuvieron los resultados ayer.', 'No toda acción merece nominalización. El estilo verbal es más natural cuando la acción es concreta y puntual.'),
        ('*El descubrimiento fue que los datos eran incorrectos.', 'El análisis reveló que los datos eran incorrectos.', 'La nominalización del predicado (<em>fue que</em>) es forzada. Mejor usar verbo pleno.'),
    ],
    summary=[
        ('estilo nominal', 'Sustantivo deverbal + verbo de apoyo en lugar de verbo simple', '<em>llevar a cabo un análisis = analizar</em>'),
        ('nominalización -ción', 'Proceso verbal → sustantivo', '<em>analizar → el análisis</em>'),
        ('verbos de apoyo', 'realizar, efectuar, llevar a cabo, proceder a', '<em>realizar una propuesta</em>'),
        ('pasiva refleja', 'Se + verbo 3ª persona (impersonal)', '<em>Se observa un incremento</em>'),
        ('impersonal formal', 'Cabe + inf, conviene + inf, es preciso + inf', '<em>Cabe señalar que los datos muestran…</em>'),
        ('evidencialidad', 'Según, de acuerdo con, conforme a + fuente', '<em>Según los datos analizados…</em>'),
        ('1ª persona plural (we académico)', 'Nosotros como sujeto colectivo de investigación', '<em>Concluimos que… / Observamos que…</em>'),
    ],
    ex1=dict(
        title='Ejercicio 1: Estilo nominal y académico',
        questions=[
            ('¿Cuál de estas frases corresponde a un estilo nominal formal?',
             ['Los precios subieron mucho.', 'Se registró un fuerte incremento de los precios.', 'Los precios fueron muy altos.', 'Que los precios subieran fue un problema.'], 1,
             '<em>Se registró un fuerte incremento</em> usa pasiva refleja + nominalización → estilo nominal formal.'),
            ('«Analizar los resultados» → Forma nominal con verbo de apoyo:',
             ['hacer el análisis', 'llevar a cabo el análisis de los resultados', 'analizar de los resultados', 'hacer analización'], 1,
             '<em>Llevar a cabo el análisis de los resultados</em> = verbo de apoyo formal + nominalización.'),
            ('¿Cuál de estos sufijos forma sustantivos deverbales en español?',
             ['-mente', '-ción', '-mente', '-ísimo'], 1,
             '<em>-ción/-sión</em> forma sustantivos deverbales: <em>analizar → el análisis; decidir → la decisión.</em>'),
            ('En el texto académico, para evitar el agente explícito, se prefiere:',
             ['la 1ª persona del singular', 'la pasiva refleja o la impersonal', 'el gerundio', 'el condicional'], 1,
             'La pasiva refleja (<em>se observa</em>) y las impersonales (<em>cabe señalar</em>) ocultan el agente en textos académicos.'),
            ('«Conviene destacar que los resultados son significativos.» Este es un ejemplo de:',
             ['verbo de apoyo', 'impersonal formal', 'pasiva perifrástica', 'nominalización'], 1,
             '<em>Conviene + inf</em> es una construcción impersonal formal del registro académico.'),
            ('¿Cuál de estas formas evita la primera persona en el texto académico?',
             ['Yo analizo los datos.', 'Se procede al análisis de los datos.', 'Tú analizas los datos.', 'Ellos analizaron los datos.'], 1,
             'La pasiva refleja (<em>se procede</em>) elimina el sujeto → recurso habitual en textos científicos.'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Transforma al estilo nominal',
        questions=[
            ('«Los investigadores propusieron una solución.» → Estilo nominal: «_______ una propuesta de solución.»',
             'Se realizó', ['Se realizó', 'Se propuso', 'Fue propuesta'],
             '<em>Realizar una propuesta</em> = verbo de apoyo + nominalización de <em>proponer</em>.'),
            ('«Decidieron continuar el proyecto.» → «Se tomó _______ de continuar el proyecto.»',
             'la decisión', ['la decisión', 'el acuerdo', 'la conclusión'],
             '<em>Tomar una decisión de + inf</em> = verbo de apoyo + nominalización de <em>decidir</em>.'),
            ('«Compararon los dos modelos.» → «Se procedió a la _______ de los dos modelos.»',
             'comparación', ['comparación', 'comparativa', 'comparancia'],
             '<em>La comparación</em> = nominalización de <em>comparar</em> con sufijo <em>-ción</em>.'),
            ('«Analizaron los datos obtenidos.» → «_______ un análisis exhaustivo de los datos obtenidos.»',
             'Se llevó a cabo', ['Se llevó a cabo', 'Se realizó sobre', 'Se hizo de'],
             '<em>Llevar a cabo un análisis</em> = verbo de apoyo formal para nominalización de <em>analizar</em>.'),
            ('Completa la frase académica: «_______ señalar que los resultados confirman la hipótesis.»',
             'Cabe', ['Cabe', 'Hay', 'Se puede'],
             '<em>Cabe + infinitivo</em> = construcción impersonal formal del registro académico.'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Registro académico',
        questions=[
            ('¿Cuál de estas frases es más apropiada para un trabajo académico?',
             ['Creo que los datos son correctos.', 'A mi modo de ver, creo que los datos son correctos.', 'Los datos analizados sugieren que los resultados son coherentes.', 'Los datos son muy buenos.'], 2,
             'Evidencialidad (<em>los datos analizados sugieren</em>) + nominalización → apropiado para el registro académico.'),
            ('En el texto académico, «se observa» es preferible a «yo observo» porque:',
             ['es más corto', 'elimina el sujeto y objetiva el enunciado', 'suena más coloquial', 'es un tiempo diferente'], 1,
             'La pasiva refleja elimina el agente y otorga objetividad al discurso científico.'),
            ('¿Cuál de estos verbos de apoyo se usa más en registros académicos?',
             ['hacer', 'llevar a cabo', 'poner', 'meter'], 1,
             '<em>Llevar a cabo</em> es el verbo de apoyo más formal y frecuente en textos académicos.'),
            ('«De acuerdo con los datos presentados…» es un ejemplo de:',
             ['atenuación', 'evidencialidad', 'topicalización', 'elipsis'], 1,
             '<em>De acuerdo con</em> señala la fuente de la información → evidencialidad.'),
            ('¿Qué tipo de nominalización es «el descubrimiento»?',
             ['deadjetival', 'deverbal con sufijo -miento', 'infinitivo sustantivado', 'préstamo'], 1,
             '<em>Descubrimiento</em> proviene de <em>descubrir</em> + sufijo <em>-miento</em> → nominalización deverbal.'),
        ]
    ),
    game_desc='Estilo nominal, nominalización y escritura académica en español',
    items=[
        dict(term='estilo nominal', definition='Registro formal que prefiere sustantivos deverbales + verbos de apoyo sobre verbos simples', example='Se llevó a cabo el análisis. (= se analizó)', accept=['estilo nominal']),
        dict(term='verbo de apoyo', definition='Verbo semánticamente vacío que acompaña al sustantivo deverbal: realizar, efectuar, llevar a cabo', example='realizar una propuesta', accept=['verbo de apoyo', 'verbo soporte']),
        dict(term='nominalización deverbal', definition='Sustantivo formado a partir de un verbo mediante un sufijo', example='analizar → el análisis; decidir → la decisión', accept=['nominalización deverbal']),
        dict(term='pasiva refleja', definition='Se + verbo en 3ª persona: recurso impersonal del texto formal', example='Se observa un incremento significativo.', accept=['pasiva refleja']),
        dict(term='cabe + infinitivo', definition='Construcción impersonal formal equivalente a «es posible» o «es conveniente»', example='Cabe señalar que los resultados son positivos.', accept=['cabe + infinitivo', 'cabe señalar']),
        dict(term='evidencialidad', definition='Recurso que indica la fuente de la información', example='Según los datos analizados / de acuerdo con los estudios previos', accept=['evidencialidad']),
        dict(term='sufijo -ción/-sión', definition='Sufijo productor de sustantivos deverbales de proceso', example='analizar → el análisis / decidir → la decisión', accept=['sufijo -ción', 'sufijo -sión']),
        dict(term='primera persona plural académica', definition='Nosotros como sujeto colectivo de la investigación', example='Concluimos que los datos confirman la hipótesis.', accept=['primera persona plural académica', 'nosotros académico']),
    ]
)
