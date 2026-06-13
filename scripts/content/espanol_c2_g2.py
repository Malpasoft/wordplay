"""espanol/ C2 Grammar – G06–G10"""

CHAPTERS = {}

# ─────────────────────────────────────────────
# G06 · construcciones-sinteticas · Construcciones Sintéticas y Estructuras Reducidas
# ─────────────────────────────────────────────
CHAPTERS['construcciones-sinteticas'] = dict(
    level='c2', section='grammar', num='G06',
    short='Construcciones Sintéticas',
    title='Construcciones Sintéticas y Estructuras Reducidas',
    subtitle='Domina el uso avanzado del participio, gerundio e infinitivo en construcciones absolutas y reducidas',
    slides=[
        ('El Participio Absoluto', None, """
<p style="margin:0 0 12px;font-size:.9rem">El participio concuerda con su propio sujeto y equivale a una subordinada adverbial.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Construcción</th><th style="padding:6px 8px;text-align:left">Valor</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Part. + sujeto propio</td><td style="padding:6px 8px">Temporal/causal</td><td style="padding:6px 8px"><em>Terminado el trabajo, salimos</em></td></tr>
<tr><td style="padding:6px 8px">Concuerda con su sujeto</td><td style="padding:6px 8px">Concordancia obligatoria</td><td style="padding:6px 8px"><em>Firmados los contratos, procedimos</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Una vez + participio</td><td style="padding:6px 8px">Temporal (más coloquial)</td><td style="padding:6px 8px"><em>Una vez aprobado el proyecto, comenzamos</em></td></tr>
<tr><td style="padding:6px 8px">Visto lo visto / dicho esto</td><td style="padding:6px 8px">Frases hechas</td><td style="padding:6px 8px"><em>Visto lo visto, lo mejor es retirarse</em></td></tr>
</table>"""),
        ('El Gerundio en Usos Avanzados', None, """
<p style="margin:0 0 12px;font-size:.9rem">El gerundio puede expresar diversas relaciones adverbiales, pero tiene restricciones importantes.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Valor</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Simultáneo</td><td style="padding:6px 8px"><em>Llegó cantando</em></td></tr>
<tr><td style="padding:6px 8px">Causal</td><td style="padding:6px 8px"><em>Siendo tan tarde, cancelaron</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Condicional</td><td style="padding:6px 8px"><em>Estudiando así, suspenderás</em></td></tr>
<tr><td style="padding:6px 8px">Concesivo</td><td style="padding:6px 8px"><em>Aun siendo difícil, lo intentó</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Modal</td><td style="padding:6px 8px"><em>Contestó sonriendo</em></td></tr>
<tr><td style="padding:6px 8px">RESTRICCIÓN: postnominal</td><td style="padding:6px 8px">*Una carta explicando → solo con verbos de actividad/proceso: <em>una imagen mostrando</em> es marginal</td></tr>
</table>"""),
        ('Al + Infinitivo y De + Infinitivo Compuesto', None, """
<p style="margin:0 0 12px;font-size:.9rem">El infinitivo en construcciones preposicionales expresa relaciones temporales, causales y condicionales.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Construcción</th><th style="padding:6px 8px;text-align:left">Valor</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">al + inf</td><td style="padding:6px 8px">Tiempo/causa simultánea</td><td style="padding:6px 8px"><em>Al llegar, llamó por teléfono</em></td></tr>
<tr><td style="padding:6px 8px">de + inf compuesto</td><td style="padding:6px 8px">Condición irreal (formal)</td><td style="padding:6px 8px"><em>De haberlo sabido, no habría venido</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">con + inf compuesto</td><td style="padding:6px 8px">Concesión hipotética</td><td style="padding:6px 8px"><em>Con haberlo dicho antes, todo iría mejor</em></td></tr>
<tr><td style="padding:6px 8px">sin + inf</td><td style="padding:6px 8px">Negación de simultaneidad</td><td style="padding:6px 8px"><em>Se fue sin despedirse</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">por + inf</td><td style="padding:6px 8px">Causa (resultado posterior)</td><td style="padding:6px 8px"><em>Por llegar tarde, perdió el tren</em></td></tr>
</table>"""),
        ('Oraciones Copulativas Escindidas', None, """
<p style="margin:0 0 12px;font-size:.9rem">Las pseudoescindidas (<em>lo que + ser</em>) focalizan el predicado nominal.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Tipo</th><th style="padding:6px 8px;text-align:left">Ejemplo</th><th style="padding:6px 8px;text-align:left">Función</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Pseudoescindida con lo que</td><td style="padding:6px 8px"><em>Lo que necesitas es descansar</em></td><td style="padding:6px 8px">Focaliza el predicado</td></tr>
<tr><td style="padding:6px 8px">Pseudoescindida con donde</td><td style="padding:6px 8px"><em>Donde vive es en Madrid</em></td><td style="padding:6px 8px">Focaliza el circunstancial</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Escindida con es + que</td><td style="padding:6px 8px"><em>Es que no pude venir</em></td><td style="padding:6px 8px">Excusa/explicación</td></tr>
</table>"""),
    ],
    traps=[
        ('*Terminando el proyecto, salimos.', 'Terminado el proyecto, salimos.', 'Para acción anterior (participio absoluto), se usa el <em>participio</em>, no el gerundio.'),
        ('*Una carta anunciando la decisión (postnominal general).', 'Una carta en la que se anuncia la decisión.', 'El gerundio postnominal es muy restringido en español. Use oración de relativo para modificar sustantivos.'),
        ('*De haber sabido, no vengo.', 'De haberlo sabido, no habría venido.', '<em>De + infinitivo compuesto</em> requiere condicional compuesto en la apódosis (<em>habría venido</em>).'),
        ('*Firmada los contratos, procedimos.', 'Firmados los contratos, procedimos.', 'El participio absoluto concuerda en género y número con su propio sujeto: <em>firmad<u>os</u> los contratos.</em>'),
        ('*Al terminar el examen, los estudiantes salieron (gerundio).', 'Al terminar el examen, los estudiantes salieron.', '<em>Al + infinitivo</em> es correcto para simultaneidad/causa. No use gerundio en esta construcción.'),
    ],
    summary=[
        ('participio absoluto', 'Participio + sujeto propio, concuerda en género y número', '<em>Terminada la reunión, nos fuimos</em>'),
        ('gerundio simultáneo', 'Acción en curso al mismo tiempo que la principal', '<em>Llegó corriendo</em>'),
        ('gerundio causal', 'Causa de la acción principal', '<em>Siendo tarde, cancelamos</em>'),
        ('al + infinitivo', 'Simultaneidad o causa inmediata', '<em>Al llegar, encontró el mensaje</em>'),
        ('de + inf compuesto', 'Condición irreal formal', '<em>De haberlo sabido, no habría ido</em>'),
        ('con + inf compuesto', 'Concesión hipotética', '<em>Con haberlo avisado, todo iría mejor</em>'),
        ('pseudoescindida', 'Lo que + ser + rema (foco en predicado)', '<em>Lo que quiero es descansar</em>'),
    ],
    ex1=dict(
        title='Ejercicio 1: Construcciones sintéticas',
        questions=[
            ('«_______ el acuerdo, comenzaron las obras.» Construcción absoluta correcta:',
             ['Firmando', 'Firmado', 'Al firmar', 'Por firmar'], 1,
             'Participio absoluto (anterioridad): <em><u>Firmado</u> el acuerdo, comenzaron.</em>'),
            ('«___ tarde, decidieron cancelar el vuelo.» Gerundio causal:',
             ['Siendo', 'Estando', 'Habiendo', 'Teniendo'], 0,
             '<em>Siendo tan tarde</em> = gerundio causal: la causa del cancelamiento.'),
            ('«___ haberlo sabido antes, lo habrían evitado.» Construcción condicional formal:',
             ['Por', 'De', 'Con', 'Al'], 1,
             '<em>De + inf compuesto</em> = condición irreal formal: <em><u>De</u> haberlo sabido.</em>'),
            ('«Lo que necesita este proyecto es ___ financiación adicional.»',
             ['de', 'una', 'la', 'más'], 1,
             'Pseudoescindida: <em>Lo que necesita… es <u>una</u> financiación adicional.</em>'),
            ('«___ llegar a casa, recibió la llamada.» Simultaneidad:',
             ['De', 'Por', 'Al', 'Sin'], 2,
             '<em>Al + infinitivo</em> expresa simultaneidad/causa inmediata: <em><u>Al</u> llegar.</em>'),
            ('«___ haberlo dicho antes, todo habría sido más fácil.» Concesión hipotética:',
             ['De', 'Por', 'Con', 'Sin'], 2,
             '<em>Con + inf compuesto</em> = concesión hipotética: <em><u>Con</u> haberlo dicho antes.</em>'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Transforma usando construcciones sintéticas',
        questions=[
            ('«Cuando terminaron las clases, los alumnos salieron.» → Construcción absoluta:',
             'Terminadas las clases, los alumnos salieron.', ['Terminadas las clases, los alumnos salieron.', 'Terminando las clases, salieron.'],
             'Participio absoluto: <em><u>Terminadas</u> las clases</em> (concuerda con <em>las clases</em>).'),
            ('«Si lo hubieran sabido, lo habrían evitado.» → Formal con de + inf:',
             'De haberlo sabido, lo habrían evitado.', ['De haberlo sabido, lo habrían evitado.', 'Al haberlo sabido, lo evitarían.'],
             '<em>De + inf compuesto</em> = condicional irreal formal.'),
            ('«Porque era muy tarde, cancelaron el evento.» → Gerundio causal:',
             'Siendo muy tarde, cancelaron el evento.', ['Siendo muy tarde, cancelaron el evento.', 'Habiendo sido tarde, cancelaron.'],
             'Gerundio causal: <em><u>Siendo</u> muy tarde, cancelaron.</em>'),
            ('«Lo que quiero es que me escuchen.» Identifica la construcción:',
             'pseudoescindida', ['pseudoescindida', 'participio absoluto', 'gerundio concesivo'],
             '<em>Lo que + quiero + es + que</em> → pseudoescindida con focalización del predicado.'),
            ('«Se fue sin que nadie lo viera.» → Sin + infinitivo (mismo sujeto):',
             'Se fue sin despedirse.', ['Se fue sin despedirse.', 'Se fue no despidiéndose.'],
             '<em>Sin + inf</em> con mismo sujeto: <em>se fue sin <u>despedirse</u>.</em>'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Valor de las construcciones',
        questions=[
            ('«Aun siendo difícil, lo intentó.» ¿Qué valor tiene el gerundio?',
             ['simultáneo', 'causal', 'concesivo', 'condicional'], 2,
             '<em>Aun + gerundio</em> = valor concesivo: a pesar de que era difícil, lo intentó.'),
            ('«Estudiando así, suspenderás.» ¿Qué valor tiene el gerundio?',
             ['simultáneo', 'causal', 'concesivo', 'condicional'], 3,
             '<em>Gerundio</em> con valor condicional: si estudias así, suspenderás.'),
            ('«Firmados los contratos, el proyecto comenzó.» El participio expresa:',
             ['simultaneidad', 'anterioridad inmediata', 'causa', 'concesión'], 1,
             'Participio absoluto = anterioridad temporal inmediata respecto a la acción principal.'),
            ('«Al comunicarse los resultados, el equipo celebró.» ¿Qué indica <em>al</em> + infinitivo?',
             ['condición', 'causa/simultaneidad', 'concesión', 'modo'], 1,
             '<em>Al + inf</em> = simultaneidad/causa inmediata: cuando se comunicaron los resultados.'),
            ('¿Cuál de estas construcciones expresa condición irreal pasada de forma formal?',
             ['Al haberlo sabido', 'De haberlo sabido', 'Por haberlo sabido', 'Sin haberlo sabido'], 1,
             '<em>De + infinitivo compuesto</em> = condición irreal pasada (registro formal).'),
        ]
    ),
    game_desc='Participio absoluto, gerundio avanzado y construcciones preposicionales con infinitivo',
    items=[
        dict(term='participio absoluto', definition='Participio con sujeto propio que concuerda en género y número', example='Terminada la reunión, nos marchamos.', accept=['participio absoluto']),
        dict(term='gerundio causal', definition='Gerundio que expresa la causa de la acción principal', example='Siendo tarde, cancelaron el vuelo.', accept=['gerundio causal']),
        dict(term='gerundio concesivo', definition='Gerundio que expresa un obstáculo que no impide la acción principal', example='Aun siendo difícil, lo consiguió.', accept=['gerundio concesivo']),
        dict(term='al + infinitivo', definition='Construción preposicional que expresa simultaneidad o causa inmediata', example='Al llegar, nos saludó.', accept=['al + infinitivo']),
        dict(term='de + infinitivo compuesto', definition='Condición irreal pasada en registro formal', example='De haberlo sabido, no habría venido.', accept=['de + infinitivo compuesto']),
        dict(term='con + infinitivo compuesto', definition='Concesión hipotética', example='Con haberlo dicho antes, todo sería diferente.', accept=['con + infinitivo compuesto']),
        dict(term='pseudoescindida', definition='Lo que + verbo + ser + rema: focaliza el predicado', example='Lo que quiero es descansar.', accept=['pseudoescindida']),
        dict(term='gerundio condicional', definition='Gerundio que expresa condición hipotética', example='Estudiando así, no aprobarás.', accept=['gerundio condicional']),
    ]
)

# ─────────────────────────────────────────────
# G07 · negacion-c2 · La Negación: Tipos y Construcciones Complejas
# ─────────────────────────────────────────────
CHAPTERS['negacion-c2'] = dict(
    level='c2', section='grammar', num='G07',
    short='La Negación Avanzada',
    title='La Negación: Tipos, Alcance y Construcciones Complejas',
    subtitle='Domina la negación proposicional, de constituyente, la doble negación y las palabras de polaridad negativa',
    slides=[
        ('Tipos de Negación', None, """
<p style="margin:0 0 12px;font-size:.9rem">La negación afecta al predicado completo o a un constituyente específico.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Tipo</th><th style="padding:6px 8px;text-align:left">Alcance</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Proposicional</td><td style="padding:6px 8px">Niega todo el predicado</td><td style="padding:6px 8px"><em>No viene nadie</em></td></tr>
<tr><td style="padding:6px 8px">De constituyente</td><td style="padding:6px 8px">Niega un elemento específico</td><td style="padding:6px 8px"><em>No el libro, sino la revista</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Metalingüística</td><td style="padding:6px 8px">Rechaza una expresión previa</td><td style="padding:6px 8px"><em>No estoy cansado, sino agotado</em></td></tr>
<tr><td style="padding:6px 8px">Descriptiva</td><td style="padding:6px 8px">Describe un estado negativo</td><td style="padding:6px 8px"><em>La reunión no fue productiva</em></td></tr>
</table>"""),
        ('La Doble Negación en Español', None, """
<p style="margin:0 0 12px;font-size:.9rem">A diferencia del inglés, en español los negativos se acumulan sin cancelarse.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Indefinido negativo</th><th style="padding:6px 8px;text-align:left">Antes del verbo (sin no)</th><th style="padding:6px 8px;text-align:left">Después del verbo (con no)</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">nadie</td><td style="padding:6px 8px"><em>Nadie vino</em></td><td style="padding:6px 8px"><em>No vino nadie</em></td></tr>
<tr><td style="padding:6px 8px">nunca / jamás</td><td style="padding:6px 8px"><em>Nunca lo diré</em></td><td style="padding:6px 8px"><em>No lo diré nunca</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">nada</td><td style="padding:6px 8px"><em>Nada importa</em></td><td style="padding:6px 8px"><em>No importa nada</em></td></tr>
<tr><td style="padding:6px 8px">ningún/ninguno</td><td style="padding:6px 8px"><em>Ningún problema hay</em></td><td style="padding:6px 8px"><em>No hay ningún problema</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">tampoco</td><td style="padding:6px 8px"><em>Tampoco lo sabe</em></td><td style="padding:6px 8px"><em>No lo sabe tampoco</em></td></tr>
</table>"""),
        ('Ni: Coordinación Negativa', None, """
<p style="margin:0 0 12px;font-size:.9rem"><em>Ni</em> coordina dos o más elementos negativos y puede funcionar como intensificador.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Construcción</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Ni... ni... (coordinación)</td><td style="padding:6px 8px"><em>No vino ni Juan ni María</em></td></tr>
<tr><td style="padding:6px 8px">ni siquiera (énfasis)</td><td style="padding:6px 8px"><em>Ni siquiera lo intentó</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">ni que + subj (rechazo)</td><td style="padding:6px 8px"><em>¡Ni que fuera tan difícil!</em></td></tr>
<tr><td style="padding:6px 8px">Sin ni siquiera + inf</td><td style="padding:6px 8px"><em>Se fue sin ni siquiera despedirse</em></td></tr>
</table>"""),
        ('Palabras de Polaridad Negativa', None, """
<p style="margin:0 0 12px;font-size:.9rem">Ciertas expresiones solo aparecen en contextos negativos, interrogativos o hipotéticos.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Expresión</th><th style="padding:6px 8px;text-align:left">Significado</th><th style="padding:6px 8px;text-align:left">Contexto</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">en absoluto</td><td style="padding:6px 8px">De ninguna manera</td><td style="padding:6px 8px"><em>No estoy de acuerdo en absoluto</em></td></tr>
<tr><td style="padding:6px 8px">en mi vida</td><td style="padding:6px 8px">Jamás (énfasis)</td><td style="padding:6px 8px"><em>En mi vida he visto algo así</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">ni por asomo</td><td style="padding:6px 8px">Ni de lejos</td><td style="padding:6px 8px"><em>Ni por asomo llegará a tiempo</em></td></tr>
<tr><td style="padding:6px 8px">ni pizca</td><td style="padding:6px 8px">Nada en absoluto</td><td style="padding:6px 8px"><em>No tiene ni pizca de talento</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">para nada</td><td style="padding:6px 8px">En absoluto (coloquial)</td><td style="padding:6px 8px"><em>No me gusta para nada</em></td></tr>
</table>"""),
    ],
    traps=[
        ('*No viene nadie = Viene alguien (doble negación cancela).', 'No viene nadie = Nadie viene (doble negación refuerza en español).', 'En español la doble negación es reforzadora, no cancela como en inglés.'),
        ('*Nadie no vino.', 'Nadie vino. / No vino nadie.', 'Cuando el indefinido negativo va antes del verbo, no se añade <em>no</em>.'),
        ('*No le gusta tampoco la pizza.', 'Tampoco le gusta la pizza. / No le gusta la pizza tampoco.', '<em>Tampoco</em> antes del verbo no lleva <em>no</em>; después del verbo puede ir con <em>no</em>.'),
        ('*¡Ni que sería tan difícil!', '¡Ni que fuera tan difícil!', '<em>Ni que</em> exige subjuntivo (imperfecto): <em>ni que <u>fuera</u>.</em>'),
        ('*No estoy de acuerdo en absoluto nada.', 'No estoy de acuerdo en absoluto.', '<em>En absoluto</em> ya es un reforzador total; no se combina con <em>nada</em>.'),
    ],
    summary=[
        ('negación proposicional', 'No + verbo: niega el predicado completo', '<em>No vino nadie / Nadie vino</em>'),
        ('negación de constituyente', 'No X, sino Y: corrige un elemento específico', '<em>No el lunes, sino el martes</em>'),
        ('negación metalingüística', 'Rechaza la expresión previa, no el hecho', '<em>No estoy cansado, sino agotado</em>'),
        ('doble negación reforzadora', 'No… nadie / nunca / nada (refuerza, no cancela)', '<em>No vino nadie</em>'),
        ('ni siquiera', 'Intensificador negativo (ni el mínimo esperado)', '<em>Ni siquiera lo intentó</em>'),
        ('ni que + subj', 'Rechazo enfático o incredulidad', '<em>¡Ni que fuera tan difícil!</em>'),
        ('en absoluto / en mi vida', 'Palabras de polaridad negativa (solo en contextos negativos)', '<em>No me gusta en absoluto</em>'),
    ],
    ex1=dict(
        title='Ejercicio 1: Tipos de negación',
        questions=[
            ('«No el presidente, sino el ministro firmó el acuerdo.» ¿Qué tipo de negación es?',
             ['proposicional', 'metalingüística', 'de constituyente', 'descriptiva'], 2,
             '<em>No X, sino Y</em> = negación de constituyente: solo se niega el sujeto, no el predicado.'),
            ('«No estoy triste, sino decepcionado.» ¿Qué tipo de negación es?',
             ['proposicional', 'metalingüística', 'de constituyente', 'descriptiva'], 1,
             'Se rechaza la etiqueta <em>triste</em> y se sustituye por <em>decepcionado</em> → negación metalingüística.'),
            ('¿Cuál de estas frases usa correctamente la doble negación?',
             ['No vino nadie no.', 'Nadie no vino.', 'No vino nadie.', 'No nadie vino.'], 2,
             '<em>No vino nadie</em>: <em>no</em> antes del verbo + <em>nadie</em> después → doble negación correcta.'),
            ('«___ lo intentó antes de rendirse.» Intensificador del mínimo:',
             ['No', 'Ni siquiera', 'Tampoco', 'En absoluto'], 1,
             '<em>Ni siquiera</em> indica que ni el mínimo esfuerzo se realizó.'),
            ('¿Qué modo exige «ni que»?',
             ['indicativo', 'infinitivo', 'subjuntivo', 'condicional'], 2,
             '<em>Ni que + subjuntivo</em>: <em>¡Ni que <u>fuera</u> tan difícil!</em>'),
            ('«En mi vida he visto algo así.» ¿Qué significa <em>en mi vida</em>?',
             ['en el futuro', 'durante mi vida', 'jamás en mi vida', 'poco en mi vida'], 2,
             '<em>En mi vida</em> es una expresión de polaridad negativa que significa <em>jamás, nunca.</em>'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Forma negativa correcta',
        questions=[
            ('«Ninguna persona llegó a tiempo.» ¿Cómo se dice con <em>no</em>?',
             'No llegó ninguna persona a tiempo.', ['No llegó ninguna persona a tiempo.', 'No llegó nadie persona a tiempo.'],
             '<em>Ninguna persona</em> puede ir después del verbo con <em>no</em> antes.'),
            ('«Nunca lo haré.» ¿Cómo se dice con <em>no</em> + verbo primero?',
             'No lo haré nunca.', ['No lo haré nunca.', 'No nunca lo haré.'],
             '<em>Nunca</em> puede ir antes (sin <em>no</em>) o después del verbo (con <em>no</em>).'),
            ('Expresa incredulidad con <em>ni que</em>: «¡Como si fuera tan fácil!»',
             '¡Ni que fuera tan fácil!', ['¡Ni que fuera tan fácil!', '¡Ni que sería tan fácil!'],
             '<em>Ni que + imperfecto subjuntivo</em>: <em>¡Ni que <u>fuera</u> tan fácil!</em>'),
            ('«No me gustó nada de nada.» ¿Cuál es el reforzador?',
             'de nada', ['de nada', 'nada de nada', 'en absoluto'],
             '<em>Nada de nada</em> es el reforzador intensivo del rechazo total.'),
            ('«Tampoco ella lo sabe.» ¿Cómo se dice con <em>no</em>?',
             'Ella no lo sabe tampoco.', ['Ella no lo sabe tampoco.', 'Ella tampoco no lo sabe.'],
             '<em>Tampoco</em> después del verbo va con <em>no</em>: <em>no lo sabe <u>tampoco</u>.</em>'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Elige la negación correcta',
        questions=[
            ('Para negar con énfasis total: «No me interesa _______.»',
             ['nada', 'en absoluto', 'para nada', 'cualquiera de las anteriores'], 3,
             'Nada, en absoluto y para nada son todas formas válidas de negación total.'),
            ('¿Cuál de estas oraciones es incorrecta?',
             ['Nadie vino.', 'No vino nadie.', 'Nadie no vino.', 'No vino ninguno.'], 2,
             '<em>Nadie no vino</em> es agramatical: con <em>nadie</em> antes del verbo no se añade <em>no</em>.'),
            ('«Ni que _______ (ser) la última oportunidad.» Forma correcta:',
             ['es', 'sea', 'fuera', 'sería'], 2,
             '<em>Ni que + imperfecto de subjuntivo</em>: <em>ni que <u>fuera</u>.</em>'),
            ('En «Ni siquiera lo miró», <em>ni siquiera</em> intensifica:',
             ['el tiempo', 'la negación del mínimo esperado', 'la causa', 'la consecuencia'], 1,
             '<em>Ni siquiera</em> = «ni el mínimo que se podría esperar» → énfasis negativo máximo.'),
            ('¿Cuál expresión NO es de polaridad negativa?',
             ['en absoluto', 'en mi vida', 'ni por asomo', 'sin embargo'], 3,
             '<em>Sin embargo</em> es un conector de contraste, no de polaridad negativa.'),
        ]
    ),
    game_desc='Negación: tipos, doble negación, ni siquiera y palabras de polaridad negativa',
    items=[
        dict(term='negación proposicional', definition='No + verbo: niega el predicado completo', example='No vino nadie a la reunión.', accept=['negación proposicional']),
        dict(term='negación de constituyente', definition='No X, sino Y: corrige un elemento específico del enunciado', example='No el lunes, sino el martes.', accept=['negación de constituyente']),
        dict(term='negación metalingüística', definition='Rechaza una expresión o etiqueta previa y propone otra mejor', example='No estoy triste, sino decepcionado.', accept=['negación metalingüística']),
        dict(term='doble negación', definition='En español la doble negación refuerza (no cancela)', example='No vino nadie = Nadie vino.', accept=['doble negación']),
        dict(term='ni siquiera', definition='Intensificador negativo: ni el mínimo esperado se cumplió', example='Ni siquiera lo intentó.', accept=['ni siquiera']),
        dict(term='ni que + subjuntivo', definition='Rechazo enfático o incredulidad ante una afirmación implícita', example='¡Ni que fuera tan difícil!', accept=['ni que + subjuntivo']),
        dict(term='en absoluto', definition='Palabra de polaridad negativa: niega de manera total y enfática', example='No estoy de acuerdo en absoluto.', accept=['en absoluto']),
        dict(term='ni por asomo', definition='Palabra de polaridad negativa: ni de lejos, en absoluto', example='Ni por asomo llegará a tiempo.', accept=['ni por asomo']),
    ]
)

# ─────────────────────────────────────────────
# G08 · perifrasis-c2 · Las Perífrasis Verbales: Clasificación y Valores
# ─────────────────────────────────────────────
CHAPTERS['perifrasis-c2'] = dict(
    level='c2', section='grammar', num='G08',
    short='Las Perífrasis Verbales',
    title='Las Perífrasis Verbales: Clasificación Completa y Valores',
    subtitle='Domina la clasificación de las perífrasis modales y aspectuales y sus diferencias de significado',
    slides=[
        ('Perífrasis Modales', None, """
<p style="margin:0 0 12px;font-size:.9rem">Las perífrasis modales expresan obligación, posibilidad y probabilidad.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Perífrasis</th><th style="padding:6px 8px;text-align:left">Valor</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">tener que + inf</td><td style="padding:6px 8px">Obligación personal</td><td style="padding:6px 8px"><em>Tengo que estudiar</em></td></tr>
<tr><td style="padding:6px 8px">haber que + inf</td><td style="padding:6px 8px">Obligación impersonal</td><td style="padding:6px 8px"><em>Hay que estudiar</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">deber + inf</td><td style="padding:6px 8px">Obligación moral</td><td style="padding:6px 8px"><em>Debes respetar las normas</em></td></tr>
<tr><td style="padding:6px 8px">deber de + inf</td><td style="padding:6px 8px">Probabilidad/deducción</td><td style="padding:6px 8px"><em>Debe de ser tarde</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">poder + inf</td><td style="padding:6px 8px">Posibilidad/capacidad/permiso</td><td style="padding:6px 8px"><em>Puede llover / Puedes irte</em></td></tr>
<tr><td style="padding:6px 8px">haber de + inf</td><td style="padding:6px 8px">Obligación moderada (formal)</td><td style="padding:6px 8px"><em>He de entregar el informe</em></td></tr>
</table>"""),
        ('Perífrasis Aspectuales: Fases del Evento', None, """
<p style="margin:0 0 12px;font-size:.9rem">Las perífrasis aspectuales expresan las fases temporal del proceso.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Fase</th><th style="padding:6px 8px;text-align:left">Perífrasis</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Incoativa</td><td style="padding:6px 8px">ponerse a, echarse a, romper a + inf</td><td style="padding:6px 8px"><em>Se puso a llorar</em></td></tr>
<tr><td style="padding:6px 8px">Progresiva</td><td style="padding:6px 8px">estar + gerundio</td><td style="padding:6px 8px"><em>Está estudiando</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Durativa</td><td style="padding:6px 8px">llevar + gerundio / seguir/continuar + ger</td><td style="padding:6px 8px"><em>Lleva dos horas esperando</em></td></tr>
<tr><td style="padding:6px 8px">Terminativa</td><td style="padding:6px 8px">acabar de, terminar de, dejar de + inf</td><td style="padding:6px 8px"><em>Acaba de llegar / Dejó de fumar</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Resultativa</td><td style="padding:6px 8px">tener + participio, llevar + participio</td><td style="padding:6px 8px"><em>Tengo escritas tres cartas</em></td></tr>
</table>"""),
        ('Diferencias entre Perífrasis Similares', None, """
<p style="margin:0 0 12px;font-size:.9rem">Algunas perífrasis aspectuales tienen diferencias sutiles que conviene precisar.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Contraste</th><th style="padding:6px 8px;text-align:left">Diferencia</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">acabar de + inf vs. acabar + gerundio</td><td style="padding:6px 8px"><em>Acaba de llegar</em> (reciente) vs. <em>Acabó llorando</em> (resultado)</td></tr>
<tr><td style="padding:6px 8px">dejar de + inf vs. dejar + inf</td><td style="padding:6px 8px"><em>Dejó de fumar</em> (cesativo) vs. <em>Déjame hablar</em> (permisivo)</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">ponerse a vs. echarse a vs. romper a</td><td style="padding:6px 8px"><em>Ponerse a</em> (voluntario); <em>echarse a</em> / <em>romper a</em> (espontáneo)</td></tr>
<tr><td style="padding:6px 8px">soler vs. acostumbrar a</td><td style="padding:6px 8px">Ambas indican hábito; <em>acostumbrar</em> es más formal</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">ir a + inf vs. estar a punto de</td><td style="padding:6px 8px"><em>Voy a salir</em> (intención/futuro) vs. <em>está a punto de salir</em> (inminencia)</td></tr>
</table>"""),
        ('Perífrasis de Pasiva', None, """
<p style="margin:0 0 12px;font-size:.9rem">Las perífrasis pasivas expresan proceso, resultado o acumulación de acciones.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Perífrasis</th><th style="padding:6px 8px;text-align:left">Valor</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">ser + participio</td><td style="padding:6px 8px">Proceso (pasiva de proceso)</td><td style="padding:6px 8px"><em>El informe fue aprobado</em></td></tr>
<tr><td style="padding:6px 8px">estar + participio</td><td style="padding:6px 8px">Estado resultante</td><td style="padding:6px 8px"><em>El informe está aprobado</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">tener + participio</td><td style="padding:6px 8px">Resultado acumulado (activa)</td><td style="padding:6px 8px"><em>Tengo escrito el informe</em></td></tr>
<tr><td style="padding:6px 8px">llevar + participio</td><td style="padding:6px 8px">Acumulación progresiva</td><td style="padding:6px 8px"><em>Llevo leídas tres novelas</em></td></tr>
</table>"""),
    ],
    traps=[
        ('*Debe llegar tarde (deducción).', 'Debe de llegar tarde (deducción).', '<em>Deber de + inf</em> = probabilidad/deducción. <em>Deber + inf</em> sin <em>de</em> = obligación moral.'),
        ('*Llevo dos horas esperado.', 'Llevo dos horas esperando.', '<em>Llevar + gerundio</em> (durativo): la acción aún continúa → gerundio, no participio.'),
        ('*Acabé llorando (reciente).', 'Acabo de llegar (reciente). Acabé llorando (resultado).', '<em>Acabar de + inf</em> = reciente; <em>acabar + gerundio</em> = resultado final del proceso.'),
        ('*Romper a trabajar (voluntario).', 'Ponerse a trabajar (voluntario). Romper a llorar (espontáneo).', '<em>Romper a</em> y <em>echarse a</em> se usan para reacciones espontáneas y emotivas.'),
        ('*Tengo escrita muchas cartas.', 'Tengo escritas muchas cartas.', 'El participio en <em>tener + participio</em> concuerda con el CD: <em>tener escrita<u>s</u> muchas carta<u>s</u>.</em>'),
    ],
    summary=[
        ('tener que vs. haber que', 'Personal (tener que) vs. impersonal (haber que)', '<em>Tengo que ir / Hay que ir</em>'),
        ('deber vs. deber de', 'Obligación (deber) vs. probabilidad (deber de)', '<em>Debes llamar / Debe de ser tarde</em>'),
        ('incoativas', 'Ponerse a (voluntario), echarse/romper a (espontáneo)', '<em>Se puso a estudiar / Rompió a llorar</em>'),
        ('acabar de vs. acabar + ger', 'Reciente (acabar de) vs. resultado (acabar + ger)', '<em>Acaba de llegar / Acabó llorando</em>'),
        ('llevar + ger/part', 'Durativo (ger: proceso en curso) / acumulativo (part: resultado)', '<em>Lleva horas esperando / Lleva leídas tres</em>'),
        ('ser/estar + participio', 'Proceso (ser) vs. estado resultante (estar)', '<em>Fue aprobado / Está aprobado</em>'),
        ('tener + participio', 'Resultado acumulado en la esfera del sujeto (activa)', '<em>Tengo escritas tres cartas</em>'),
    ],
    ex1=dict(
        title='Ejercicio 1: Perífrasis modales',
        questions=[
            ('«___ de tener mucho dinero para llevar ese estilo de vida.» Deducción:',
             ['Tiene que', 'Debe de', 'Hay que', 'Puede'], 1,
             '<em>Deber de + inf</em> = deducción/probabilidad: <em><u>Debe de</u> tener mucho dinero.</em>'),
            ('«___ respetar las señales de tráfico.» Obligación impersonal:',
             ['Tienes que', 'Debes', 'Hay que', 'Puedes'], 2,
             '<em>Haber que + inf</em> = obligación impersonal (sin sujeto): <em><u>Hay que</u> respetar.</em>'),
            ('«He ___ entregar el proyecto antes del viernes.» Obligación formal:',
             ['de', 'que', 'a', 'para'], 0,
             '<em>Haber de + inf</em> = obligación moderada, registro formal: <em>He <u>de</u> entregar.</em>'),
            ('«___ llover mañana, así que lleva paraguas.» Posibilidad:',
             ['Debe', 'Hay que', 'Puede', 'Tiene que'], 2,
             '<em>Poder + inf</em> = posibilidad: <em><u>Puede</u> llover.</em>'),
            ('«___ estudiar más para aprobar.» Obligación personal:',
             ['Hay que', 'Tienes que', 'Debes de', 'Puedes'], 1,
             '<em>Tener que + inf</em> = obligación personal: <em><u>Tienes que</u> estudiar.</em>'),
            ('«___ ser la una — todo el mundo está comiendo.» Deducción:',
             ['Tiene que', 'Debe de', 'Hay que', 'Va a'], 1,
             '<em>Deber de + inf</em> expresa la deducción del hablante basada en evidencia.'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Perífrasis aspectuales',
        questions=[
            ('«Al oír la noticia, _______ (echarse) a llorar.» Inicio espontáneo:',
             'se echó', ['se echó', 'se puso'],
             '<em>Echarse a + inf</em> = inicio espontáneo/emotivo: <em><u>se echó</u> a llorar.</em>'),
            ('«_______ dos años viviendo en Madrid.» Duración hasta ahora:',
             'Llevo', ['Llevo', 'Acabo de'],
             '<em>Llevar + gerundio</em> = duración continua hasta el momento presente.'),
            ('«El informe ya _______ terminado.» Estado resultante:',
             'está', ['está', 'es', 'fue'],
             '<em>Estar + participio</em> = estado resultante: <em>el informe ya <u>está</u> terminado.</em>'),
            ('«_______ leer cincuenta páginas del libro.» Acumulación:',
             'Llevo leídas', ['Llevo leídas', 'Acabo de leer'],
             '<em>Llevar + participio</em> = resultado acumulado progresivo: <em><u>Llevo leídas</u> cincuenta páginas.</em>'),
            ('«_______ de cenar — la comida aún está caliente.» Acción reciente:',
             'Acabamos', ['Acabamos', 'Acabamos de'],
             '<em>Acabar de + inf</em> = acción muy reciente: <em><u>Acabamos de</u> cenar.</em>'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Elige la perífrasis correcta',
        questions=[
            ('Para indicar que una acción empezó hace tiempo y sigue ahora, usamos:',
             ['ponerse a + inf', 'llevar + gerundio', 'acabar de + inf', 'romper a + inf'], 1,
             '<em>Llevar + gerundio</em> = duración continua hasta el presente.'),
            ('Para indicar que una acción fue completada hace muy poco, usamos:',
             ['acabar + gerundio', 'acabar de + inf', 'llevar + participio', 'tener + participio'], 1,
             '<em>Acabar de + inf</em> = acción recién completada.'),
            ('«Rompió a cantar» indica un inicio:',
             ['voluntario y planificado', 'espontáneo y emotivo', 'forzado por otro', 'habitual'], 1,
             '<em>Romper a + inf</em> = inicio súbito, espontáneo, generalmente emotivo.'),
            ('La diferencia entre <em>fue aprobado</em> y <em>está aprobado</em>:',
             ['no hay diferencia', 'fue = proceso; está = estado resultante', 'fue = pasado; está = presente siempre', 'son agramaticales'], 1,
             '<em>Ser + part</em> = proceso/evento pasivo; <em>estar + part</em> = estado resultante de ese proceso.'),
            ('«Tengo escritas tres cartas.» El participio concuerda con:',
             ['el sujeto (yo)', 'el verbo tener', 'el CD (tres cartas)', 'el tiempo verbal'], 2,
             'En <em>tener + participio</em>, el participio concuerda con el CD: <em>cartas</em> → <em>escrita<u>s</u></em>.'),
        ]
    ),
    game_desc='Perífrasis modales y aspectuales: clasificación, fases y diferencias de significado',
    items=[
        dict(term='deber de + infinitivo', definition='Probabilidad o deducción del hablante', example='Debe de estar en casa.', accept=['deber de + infinitivo']),
        dict(term='llevar + gerundio', definition='Duración continua de una acción hasta el momento presente', example='Lleva tres horas esperando.', accept=['llevar + gerundio']),
        dict(term='acabar de + infinitivo', definition='Acción muy reciente, recién completada', example='Acaba de llegar.', accept=['acabar de + infinitivo']),
        dict(term='echarse a / romper a', definition='Inicio súbito y espontáneo, generalmente emotivo', example='Rompió a llorar al oír la noticia.', accept=['echarse a', 'romper a']),
        dict(term='ponerse a + infinitivo', definition='Inicio voluntario de una actividad', example='Se puso a estudiar cuando llegó.', accept=['ponerse a + infinitivo']),
        dict(term='tener + participio', definition='Resultado acumulado; el participio concuerda con el CD', example='Tengo leídas cien páginas.', accept=['tener + participio']),
        dict(term='ser + participio', definition='Pasiva perifrástica: expresa el proceso de la acción pasiva', example='El acuerdo fue firmado ayer.', accept=['ser + participio']),
        dict(term='estar + participio', definition='Estado resultante de una acción pasiva anterior', example='El acuerdo ya está firmado.', accept=['estar + participio']),
    ]
)

# ─────────────────────────────────────────────
# G09 · discurso-referido · El Discurso Referido Avanzado
# ─────────────────────────────────────────────
CHAPTERS['discurso-referido'] = dict(
    level='c2', section='grammar', num='G09',
    short='Discurso Referido',
    title='El Discurso Referido: Formas Avanzadas y el Discurso Libre Indirecto',
    subtitle='Analiza y reproduce enunciados con estilo directo, indirecto y libre indirecto con plena precisión',
    slides=[
        ('Concordancia Temporal en el Estilo Indirecto', None, """
<p style="margin:0 0 12px;font-size:.9rem">Al pasar al estilo indirecto con verbo principal en pasado, los tiempos del discurso original retroceden.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Estilo directo</th><th style="padding:6px 8px;text-align:left">Estilo indirecto (verbo principal en pasado)</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>«Tengo frío»</em></td><td style="padding:6px 8px">Dijo que <em>tenía</em> frío</td></tr>
<tr><td style="padding:6px 8px"><em>«Llegué tarde»</em></td><td style="padding:6px 8px">Dijo que <em>había llegado</em> tarde</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>«Vendré mañana»</em></td><td style="padding:6px 8px">Dijo que <em>vendría</em> al día siguiente</td></tr>
<tr><td style="padding:6px 8px"><em>«He visto la película»</em></td><td style="padding:6px 8px">Dijo que <em>había visto</em> la película</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>«Habré terminado»</em></td><td style="padding:6px 8px">Dijo que <em>habría terminado</em></td></tr>
</table>"""),
        ('Cambios Pronominales y de Adverbio', None, """
<p style="margin:0 0 12px;font-size:.9rem">En el estilo indirecto también cambian los pronombres, posesivos y adverbios.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Estilo directo</th><th style="padding:6px 8px;text-align:left">Estilo indirecto</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>yo / tú / nosotros</em></td><td style="padding:6px 8px">él/ella / yo (u)/ ellos</td></tr>
<tr><td style="padding:6px 8px"><em>aquí / ahí</em></td><td style="padding:6px 8px"><em>allí / en ese lugar</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>hoy / mañana / ayer</em></td><td style="padding:6px 8px"><em>ese día / al día siguiente / el día anterior</em></td></tr>
<tr><td style="padding:6px 8px"><em>este / esta</em></td><td style="padding:6px 8px"><em>ese / esa / aquel</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>mi / tu / nuestro</em></td><td style="padding:6px 8px"><em>su / mi / su</em> (según el caso)</td></tr>
</table>"""),
        ('Mandatos y Preguntas en Estilo Indirecto', None, """
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Tipo</th><th style="padding:6px 8px;text-align:left">Directo</th><th style="padding:6px 8px;text-align:left">Indirecto</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Mandato</td><td style="padding:6px 8px"><em>«Ven aquí»</em></td><td style="padding:6px 8px">Me pidió que <em>fuera</em> allí</td></tr>
<tr><td style="padding:6px 8px">Pregunta sí/no</td><td style="padding:6px 8px"><em>«¿Has comido?»</em></td><td style="padding:6px 8px">Preguntó <em>si</em> había comido</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Pregunta qu-</td><td style="padding:6px 8px"><em>«¿Cuándo vendrás?»</em></td><td style="padding:6px 8px">Preguntó <em>cuándo</em> vendría</td></tr>
<tr><td style="padding:6px 8px">Exclamativa</td><td style="padding:6px 8px"><em>«¡Qué calor hace!»</em></td><td style="padding:6px 8px">Dijo <em>que hacía</em> mucho calor</td></tr>
</table>"""),
        ('El Discurso Libre Indirecto', None, """
<p style="margin:0 0 12px;font-size:.9rem">El discurso libre indirecto (DLI) mezcla la perspectiva del narrador y la del personaje sin verbo de reporte.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Tipo</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Estilo directo</td><td style="padding:6px 8px">María pensó: «No puedo seguir así»</td></tr>
<tr><td style="padding:6px 8px">Estilo indirecto</td><td style="padding:6px 8px">María pensó que no podía seguir así</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Discurso libre indirecto</td><td style="padding:6px 8px">María se detuvo. No podía seguir así. ¿Qué haría?</td></tr>
</table>
<p style="margin:10px 0 0;font-size:.83rem">El DLI adopta los tiempos del EI pero sin verbo introductor; la perspectiva es del personaje, no del narrador.</p>"""),
    ],
    traps=[
        ('*Dijo que «mañana vendría».', 'Dijo que vendría al día siguiente.', 'En estilo indirecto, <em>mañana</em> se convierte en <em>al día siguiente</em>.'),
        ('*Preguntó si que había comido.', 'Preguntó si había comido.', 'La pregunta sí/no en EI usa solo <em>si</em>, sin <em>que</em>.'),
        ('*Me ordenó que viniera aquí.', 'Me ordenó que fuera allí.', '<em>Aquí</em> → <em>allí</em>; <em>ir</em> (en lugar de <em>venir</em> si la perspectiva cambia).'),
        ('*Dijo que «él» vendría (reproduciendo el yo del hablante original).', 'Dijo que vendría. / Dijo que yo vendría (según el contexto).', 'Los pronombres cambian según la nueva perspectiva enunciativa.'),
        ('*Le pidió que «ven».', 'Le pidió que viniera.', 'El mandato en EI usa <em>que + imperfecto de subjuntivo</em>.'),
    ],
    summary=[
        ('presente → imperfecto', 'Retroceso temporal en EI con verbo principal en pasado', '<em>«Tengo» → dijo que tenía</em>'),
        ('futuro → condicional', 'Retroceso temporal del futuro', '<em>«Vendré» → dijo que vendría</em>'),
        ('perfecto → pluscuamperfecto', 'Retroceso del pretérito perfecto', '<em>«He visto» → dijo que había visto</em>'),
        ('mañana → al día siguiente', 'Cambio de adverbio temporal', '<em>«Hoy» → ese día</em>'),
        ('mandato → que + subj', 'Imperativo en EI → pidió que + imperfecto subj.', '<em>«Ven» → pidió que fuera</em>'),
        ('pregunta sí/no → si', 'Pregunta directa cerrada → si + indicativo/condicional', '<em>«¿Has comido?» → si había comido</em>'),
        ('DLI', 'Sin verbo introductor; perspectiva del personaje en tiempos de EI', 'No podía seguir así. ¿Qué haría? (sin «dijo que»)'),
    ],
    ex1=dict(
        title='Ejercicio 1: Transforma al estilo indirecto',
        questions=[
            ('«Mañana iré al médico.» → Dijo que _______.',
             ['iría al día siguiente', 'irá mañana', 'había ido al día siguiente', 'fuera al día siguiente'], 0,
             'Futuro → condicional; mañana → al día siguiente: <em>dijo que <u>iría al día siguiente</u>.</em>'),
            ('«¿Has terminado el informe?» → Me preguntó si _______.',
             ['habré terminado', 'había terminado', 'he terminado', 'hubiera terminado'], 1,
             'Pretérito perfecto → pluscuamperfecto: <em>si <u>había terminado</u> el informe.</em>'),
            ('«Ven aquí ahora mismo.» → Me pidió que _______.',
             ['vine allí en ese momento', 'fuera allí en ese momento', 'venga aquí en ese momento', 'ir allí entonces'], 1,
             'Mandato → que + imperfecto subj.; aquí → allí; ahora → en ese momento: <em>que <u>fuera allí en ese momento</u>.</em>'),
            ('«Tengo mucho trabajo.» → Dijo que _______.',
             ['tiene', 'tenía', 'había tenido', 'tuviera'], 1,
             'Presente → imperfecto en EI: <em>dijo que <u>tenía</u> mucho trabajo.</em>'),
            ('«¿Por qué no vino nadie?» → Preguntó _______.',
             ['si no vino nadie', 'por qué no había venido nadie', 'que por qué no vino nadie', 'si no viniera nadie'], 1,
             'Pregunta qu- → pregunta indirecta con <em>por qué</em> + condicional/pluscpf: <em><u>por qué no había venido nadie</u>.</em>'),
            ('«Habremos llegado para las ocho.» → Dijo que _______.',
             ['habrán llegado', 'llegarían', 'habrían llegado', 'llegaran'], 2,
             'Futuro perfecto → condicional compuesto: <em>dijo que <u>habrían llegado</u> para las ocho.</em>'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Identifica el tipo de discurso',
        questions=[
            ('«Juan se detuvo. ¿Qué habría hecho mal? Nadie lo entendería.» ¿Qué tipo de discurso es?',
             'discurso libre indirecto', ['discurso libre indirecto', 'estilo indirecto', 'estilo directo'],
             'Sin verbo de reporte, perspectiva del personaje, tiempos del EI → Discurso Libre Indirecto.'),
            ('«Me preguntó si había terminado el proyecto.» ¿Qué tipo es?',
             'estilo indirecto', ['estilo indirecto', 'discurso libre indirecto', 'estilo directo'],
             'Con verbo de reporte (<em>preguntó</em>) + si + pluscuamperfecto → estilo indirecto.'),
            ('«Dijo: "Esta noche no puedo salir."» ¿Qué tipo es?',
             'estilo directo', ['estilo directo', 'estilo indirecto', 'discurso libre indirecto'],
             'Verbo de reporte + dos puntos + comillas/guion → estilo directo.'),
            ('En el EI, «hoy» se convierte en:',
             'ese día', ['ese día', 'mañana', 'ayer', 'entonces'],
             '<em>Hoy</em> en EI → <em>ese día</em> (el día en que ocurrió).'),
            ('El DLI se caracteriza por:',
             'perspectiva del personaje sin verbo de reporte', ['tiempos del estilo directo', 'perspectiva del personaje sin verbo de reporte', 'siempre en presente', 'siempre en futuro'],
             'El DLI adopta los tiempos del EI pero elimina el verbo introductor, mezclando la voz del narrador y del personaje.'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Estilo indirecto completo',
        questions=[
            ('«Ayer estuve en el hospital.» → Dijo que _______ en el hospital.',
             ['estuvo', 'había estado', 'estaría', 'habría estado'], 1,
             'Indefinido → pluscuamperfecto en EI: <em>dijo que <u>había estado</u>.</em>'),
            ('«Llámame mañana.» → Me pidió que _______ al día siguiente.',
             ['llamara', 'llame', 'llamaré', 'he llamado'], 0,
             'Imperativo → que + imperfecto subj.: <em>que me <u>llamara</u>.</em>'),
            ('«¿Dónde vives?» → Me preguntó _______ vivía.',
             ['si', 'dónde', 'que dónde', 'adonde'], 1,
             'Pregunta de lugar → <em>dónde</em> (conserva la palabra interrogativa): <em><u>dónde</u> vivía.</em>'),
            ('«Creo que tienes razón.» → Dijo que _______ razón.',
             ['tengo', 'tenía', 'tuviera', 'habría tenido'], 1,
             'Presente → imperfecto en EI: <em>dijo que <u>tenía</u> razón.</em>'),
            ('En el DLI, ¿qué rasgo lo distingue del EI?',
             ['usa el futuro en vez del condicional', 'no tiene verbo introductor de discurso', 'siempre usa el modo subjuntivo', 'no cambia los pronombres'], 1,
             'El DLI elimina el verbo de reporte (<em>dijo que, pensó que</em>) pero mantiene los tiempos del EI.'),
        ]
    ),
    game_desc='Estilo directo, indirecto, DLI y cambios de tiempo, pronombre y adverbio',
    items=[
        dict(term='estilo directo', definition='Reproducción literal de las palabras originales con verbo de reporte', example='Dijo: «No puedo venir.»', accept=['estilo directo']),
        dict(term='estilo indirecto', definition='Reproducción con verbo de reporte + que, con cambios de tiempo y pronombre', example='Dijo que no podía venir.', accept=['estilo indirecto']),
        dict(term='discurso libre indirecto', definition='Perspectiva del personaje sin verbo de reporte, con tiempos del EI', example='No podía venir. ¿Qué haría?', accept=['discurso libre indirecto', 'DLI']),
        dict(term='retroceso temporal', definition='En EI con verbo en pasado, los tiempos avanzan un paso hacia el pasado', example='«Tengo» → tenía; «vendré» → vendría', accept=['retroceso temporal']),
        dict(term='mañana → al día siguiente', definition='Cambio de adverbio temporal en el paso al EI', example='«Mañana vengo» → dijo que vendría al día siguiente', accept=['mañana → al día siguiente']),
        dict(term='mandato en EI', definition='Imperativo → pidió/ordenó/rogó + que + imperfecto de subjuntivo', example='«Ven» → me pidió que fuera.', accept=['mandato en EI', 'imperativo en estilo indirecto']),
        dict(term='pregunta sí/no en EI', definition='Pregunta cerrada → preguntó si + indicativo/condicional', example='«¿Has comido?» → preguntó si había comido.', accept=['pregunta sí/no en EI']),
        dict(term='verbos de reporte', definition='Decir, afirmar, señalar, añadir, reconocer, negar, aclarar, insistir en que', example='Señaló que el proyecto necesitaba revisión.', accept=['verbos de reporte']),
    ]
)

# ─────────────────────────────────────────────
# G10 · generos-textuales · Los Géneros Textuales: Estructura y Rasgos
# ─────────────────────────────────────────────
CHAPTERS['generos-textuales'] = dict(
    level='c2', section='grammar', num='G10',
    short='Géneros Textuales',
    title='Los Géneros Textuales: Estructura y Rasgos Lingüísticos',
    subtitle='Identifica y produce textos de diferentes géneros usando los rasgos léxicos y gramaticales apropiados',
    slides=[
        ('Tipos de Texto: Clasificación', None, """
<p style="margin:0 0 12px;font-size:.9rem">Los textos se clasifican según su función comunicativa y sus rasgos formales.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Tipo</th><th style="padding:6px 8px;text-align:left">Función</th><th style="padding:6px 8px;text-align:left">Ejemplos</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Narrativo</td><td style="padding:6px 8px">Relatar eventos</td><td style="padding:6px 8px">Cuento, novela, crónica</td></tr>
<tr><td style="padding:6px 8px">Descriptivo</td><td style="padding:6px 8px">Representar características</td><td style="padding:6px 8px">Retrato, catálogo, guía</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Argumentativo</td><td style="padding:6px 8px">Convencer/persuadir</td><td style="padding:6px 8px">Ensayo, editorial, debate</td></tr>
<tr><td style="padding:6px 8px">Expositivo</td><td style="padding:6px 8px">Informar y explicar</td><td style="padding:6px 8px">Artículo científico, manual</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Instructivo</td><td style="padding:6px 8px">Guiar una acción</td><td style="padding:6px 8px">Receta, manual de uso</td></tr>
<tr><td style="padding:6px 8px">Dialógico</td><td style="padding:6px 8px">Intercambio comunicativo</td><td style="padding:6px 8px">Entrevista, debate, carta</td></tr>
</table>"""),
        ('El Texto Argumentativo: Estructura y Recursos', None, """
<p style="margin:0 0 12px;font-size:.9rem">El ensayo argumentativo sigue una estructura clara y usa recursos retóricos precisos.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Parte</th><th style="padding:6px 8px;text-align:left">Función</th><th style="padding:6px 8px;text-align:left">Marcadores típicos</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Tesis</td><td style="padding:6px 8px">Posición del autor</td><td style="padding:6px 8px"><em>En este trabajo se sostiene que…</em></td></tr>
<tr><td style="padding:6px 8px">Argumentos</td><td style="padding:6px 8px">Justificación de la tesis</td><td style="padding:6px 8px"><em>En primer lugar… asimismo… por otro lado…</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Contraargumento</td><td style="padding:6px 8px">Objeción prevista</td><td style="padding:6px 8px"><em>No obstante… si bien es cierto que…</em></td></tr>
<tr><td style="padding:6px 8px">Refutación</td><td style="padding:6px 8px">Respuesta al contraargumento</td><td style="padding:6px 8px"><em>Sin embargo… ahora bien…</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Conclusión</td><td style="padding:6px 8px">Cierre y síntesis</td><td style="padding:6px 8px"><em>En definitiva… en conclusión…</em></td></tr>
</table>"""),
        ('El Texto Expositivo: Rasgos Lingüísticos', None, """
<p style="margin:0 0 12px;font-size:.9rem">Los textos expositivos formales comparten rasgos gramaticales específicos.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Rasgo</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Nominalizaciones</td><td style="padding:6px 8px"><em>El análisis de los datos revela…</em></td></tr>
<tr><td style="padding:6px 8px">Pasiva refleja/impersonal</td><td style="padding:6px 8px"><em>Se observa / Cabe señalar</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Evidencialidad</td><td style="padding:6px 8px"><em>Según los datos / De acuerdo con</em></td></tr>
<tr><td style="padding:6px 8px">Léxico técnico/formal</td><td style="padding:6px 8px"><em>paradigma, hipótesis, metodología</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Impersonalidad</td><td style="padding:6px 8px"><em>Se concluye / los resultados muestran</em></td></tr>
</table>"""),
        ('El Texto Narrativo: Rasgos Temporales', None, """
<p style="margin:0 0 12px;font-size:.9rem">La narrativa usa el tiempo verbal para construir la perspectiva del relato.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Recurso</th><th style="padding:6px 8px;text-align:left">Función</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Imperfecto</td><td style="padding:6px 8px">Fondo/escenario</td><td style="padding:6px 8px"><em>Era tarde, llovía, las calles estaban vacías</em></td></tr>
<tr><td style="padding:6px 8px">Indefinido</td><td style="padding:6px 8px">Eventos en primer plano</td><td style="padding:6px 8px"><em>De repente llegó un hombre</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Pluscuamperfecto</td><td style="padding:6px 8px">Evento previo al pasado</td><td style="padding:6px 8px"><em>Supo entonces lo que había ocurrido</em></td></tr>
<tr><td style="padding:6px 8px">Presente histórico</td><td style="padding:6px 8px">Víveza narrativa</td><td style="padding:6px 8px"><em>Y de repente, el hombre se gira y dispara</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">DLI</td><td style="padding:6px 8px">Perspectiva del personaje</td><td style="padding:6px 8px"><em>¿Qué haría? No podía seguir</em></td></tr>
</table>"""),
    ],
    traps=[
        ('*El texto argumentativo no necesita citar fuentes.', 'El texto argumentativo formal debe apoyar sus argumentos con evidencias y citas.', 'Sin evidencia o justificación, el argumento es una mera opinión, no un argumento válido.'),
        ('*En el texto expositivo, el autor expresa su opinión directamente.', 'El texto expositivo busca la objetividad; la opinión pertenece al argumentativo.', 'La confusión entre expositivo (informar) y argumentativo (persuadir) es frecuente en C2.'),
        ('*La conclusión introduce argumentos nuevos.', 'La conclusión sintetiza la tesis y los argumentos sin introducir información nueva.', 'La conclusión cierra el texto; los argumentos nuevos se desarrollan en el cuerpo.'),
        ('*El texto instructivo usa verbos en indicativo.', 'El texto instructivo usa el imperativo, el infinitivo o el indicativo de mandato (Tomará X pastillas).', 'La instrucción requiere formas verbales de mandato o procedimiento, no de descripción.'),
        ('*El presente histórico puede sustituir al imperfecto de fondo.', 'El presente histórico sustituye al indefinido (primer plano), no al imperfecto.', 'El presente histórico aporta viveza a los eventos del primer plano narrativo, no al fondo.'),
    ],
    summary=[
        ('texto narrativo', 'Relata eventos con perspectiva temporal; usa indefinido/imperfecto/pluscpf', '<em>Cuento, novela, crónica</em>'),
        ('texto argumentativo', 'Tesis → argumentos → contraargumento → refutación → conclusión', '<em>Ensayo, editorial, debate</em>'),
        ('texto expositivo', 'Informa con objetividad: nominalización, pasiva, evidencialidad', '<em>Artículo científico, manual</em>'),
        ('texto instructivo', 'Guía una acción: imperativo, infinitivo o indicativo de mandato', '<em>Receta, manual de uso</em>'),
        ('tesis', 'Posición del autor en el argumento', '<em>En este trabajo se sostiene que…</em>'),
        ('contraargumento', 'Objeción prevista; se introduce con si bien/no obstante', '<em>No obstante, algunos sostienen que…</em>'),
        ('evidencialidad', 'Señalar la fuente; recurso del texto expositivo y argumentativo', '<em>Según los datos / De acuerdo con</em>'),
    ],
    ex1=dict(
        title='Ejercicio 1: Identifica el género textual',
        questions=[
            ('«Se mezclan los ingredientes y se hornea a 180°C durante 30 minutos.» ¿Qué tipo de texto es?',
             ['narrativo', 'argumentativo', 'instructivo', 'descriptivo'], 2,
             'Instrucciones de procedimiento (se + verbo impersonal) → texto instructivo.'),
            ('«La pobreza energética afecta a millones de hogares. Cabe señalar que, según los datos del INE…» ¿Qué tipo es?',
             ['argumentativo', 'expositivo', 'narrativo', 'instructivo'], 1,
             'Objetividad, evidencialidad, impersonalidad → texto expositivo.'),
            ('«Estoy convencido de que la energía nuclear es necesaria. En primer lugar, es más eficiente…» ¿Qué tipo es?',
             ['argumentativo', 'expositivo', 'descriptivo', 'narrativo'], 0,
             'Tesis explícita + argumentos → texto argumentativo.'),
            ('En la narrativa, el imperfecto se usa para:',
             ['los eventos del primer plano', 'el fondo/escenario', 'la conclusión', 'la tesis'], 1,
             'El imperfecto describe el escenario y los estados de fondo en la narrativa.'),
            ('¿Qué parte del texto argumentativo introduce una objeción?',
             ['la tesis', 'el argumento', 'el contraargumento', 'la conclusión'], 2,
             'El contraargumento recoge la objeción prevista para después refutarla.'),
            ('«Según los estudios analizados, se observa una correlación entre…» Este es un ejemplo de:',
             ['tesis argumentativa', 'texto instructivo', 'texto expositivo con evidencialidad', 'discurso libre indirecto'], 2,
             'Evidencialidad (<em>según los estudios</em>) + impersonalidad (<em>se observa</em>) → texto expositivo.'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Recursos del género',
        questions=[
            ('En un ensayo académico, para introducir la tesis, usas:',
             'En este trabajo se sostiene que', ['En este trabajo se sostiene que', 'Yo creo que', 'Me parece que'],
             'La tesis académica se presenta con impersonalidad: <em>se sostiene, se propone, se argumenta</em>.'),
            ('El marcador típico para introducir el contraargumento en un ensayo es:',
             'Si bien es cierto que', ['Si bien es cierto que', 'En primer lugar', 'En definitiva'],
             '<em>Si bien es cierto que</em> introduce la objeción o el aspecto concesivo antes de refutarlo.'),
            ('Para concluir un texto argumentativo, el marcador más apropiado es:',
             'En definitiva', ['En definitiva', 'En primer lugar', 'Sin embargo'],
             '<em>En definitiva</em> cierra el texto con síntesis.'),
            ('En un texto instructivo, la voz más habitual para dar instrucciones es:',
             'imperativo / infinitivo / se + verbo', ['imperativo / infinitivo / se + verbo', 'pasiva perifrástica', 'imperfecto de indicativo'],
             'Imperativo (<em>agita</em>), infinitivo (<em>agitar</em>) o impersonal (<em>se agita</em>) son los recursos del texto instructivo.'),
            ('El «presente histórico» aporta en la narrativa:',
             'viveza a los eventos del primer plano', ['viveza a los eventos del primer plano', 'información de fondo', 'conclusión', 'instrucción'],
             'El presente histórico sustituye al indefinido y aporta viveza e inmediatez a los eventos narrados.'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Aplica los conocimientos',
        questions=[
            ('¿Cuál de estos fragmentos pertenece a un texto expositivo?',
             ['«Estoy a favor de las energías renovables porque son el futuro.»', '«Se observa un aumento progresivo en el uso de las energías renovables.»', '«¡Usad energías renovables ya!»', '«Era un día soleado cuando llegamos a la planta solar.»'], 1,
             'Impersonal + evidencial + neutro → texto expositivo: <em>Se observa un aumento progresivo.</em>'),
            ('¿En qué tipo de texto es esencial la «tesis»?',
             ['narrativo', 'argumentativo', 'expositivo', 'instructivo'], 1,
             'La tesis (posición del autor) es el elemento central del texto argumentativo.'),
            ('¿Qué marcador introduce un argumento adicional?',
             ['sin embargo', 'no obstante', 'asimismo', 'en definitiva'], 2,
             '<em>Asimismo</em> (= del mismo modo, igualmente) introduce un argumento que suma al anterior.'),
            ('El texto narrativo usa el pluscuamperfecto para:',
             ['el fondo descriptivo', 'la tesis', 'eventos anteriores al pasado principal', 'la conclusión'], 2,
             'El pluscuamperfecto ubica eventos que ocurrieron antes del pasado narrado (antes del pasado).'),
            ('¿Cuál de estos NO es un rasgo del texto expositivo académico?',
             ['nominalizaciones', 'pasiva refleja', 'primera persona del singular enfática', 'evidencialidad'], 2,
             'El texto expositivo académico evita la primera persona singular enfática; prefiere la impersonalidad o el nosotros académico.'),
        ]
    ),
    game_desc='Géneros textuales: narrativo, argumentativo, expositivo, instructivo — rasgos y estructura',
    items=[
        dict(term='texto argumentativo', definition='Expone una tesis y la defiende con argumentos, contraargumentos y conclusión', example='Ensayo, editorial, artículo de opinión', accept=['texto argumentativo']),
        dict(term='texto expositivo', definition='Informa objetivamente usando impersonales, evidencialidad y nominalizaciones', example='Artículo científico, enciclopedia', accept=['texto expositivo']),
        dict(term='texto narrativo', definition='Relata eventos con perspectiva temporal: imperfecto (fondo) + indefinido (primer plano)', example='Novela, cuento, crónica', accept=['texto narrativo']),
        dict(term='tesis', definition='Posición o hipótesis del autor que se defiende en el texto argumentativo', example='En este trabajo se sostiene que el cambio climático es irreversible.', accept=['tesis']),
        dict(term='contraargumento', definition='Objeción prevista que el autor introduce para luego refutar', example='Si bien es cierto que hay costes, estos se compensan con los beneficios.', accept=['contraargumento']),
        dict(term='presente histórico', definition='Uso del presente para narrar eventos pasados con mayor viveza', example='Y de repente, el general se levanta y grita.', accept=['presente histórico']),
        dict(term='evidencialidad', definition='Recurso que señala la fuente de la información', example='Según los datos del INE / De acuerdo con los estudios', accept=['evidencialidad']),
        dict(term='texto instructivo', definition='Guía una acción usando imperativo, infinitivo o se + verbo', example='Receta, manual de instrucciones', accept=['texto instructivo']),
    ]
)
