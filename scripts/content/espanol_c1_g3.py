"""espanol/ C1 Grammar – G11–G15"""

CHAPTERS = {}

# ─────────────────────────────────────────────
# G11 · ser-estar-c1 · SER, ESTAR y HABER: Usos Especiales
# ─────────────────────────────────────────────
CHAPTERS['ser-estar-c1'] = dict(
    level='c1', section='grammar', num='G11',
    short='SER, ESTAR y HABER',
    title='SER, ESTAR y HABER: Usos Especiales y Diferencias Sutiles',
    subtitle='Controla los contextos ambiguos y los usos avanzados de los tres verbos copulativos',
    slides=[
        ('SER y ESTAR con Adjetivos: Repaso y Casos Especiales', None, """
<p style="margin:0 0 12px;font-size:.9rem">A nivel C1 importa no solo la regla general, sino los contextos donde la diferencia es sutil o cambia el significado.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Contexto</th><th style="padding:6px 8px;text-align:left">SER</th><th style="padding:6px 8px;text-align:left">ESTAR</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Adjetivos de valoración</td><td style="padding:6px 8px"><em>Es bueno</em> (cualidad estable)</td><td style="padding:6px 8px"><em>Está bueno</em> (sabor/estado físico)</td></tr>
<tr><td style="padding:6px 8px">Adjetivos de posición</td><td style="padding:6px 8px">— (no se usa)</td><td style="padding:6px 8px"><em>Está de pie / sentado / tumbado</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Adjetivos de edad</td><td style="padding:6px 8px"><em>Es joven</em> (categoría)</td><td style="padding:6px 8px"><em>Está joven</em> (sorpresa/cambio)</td></tr>
<tr><td style="padding:6px 8px">Participios</td><td style="padding:6px 8px"><em>Es decidido</em> (carácter)</td><td style="padding:6px 8px"><em>Está decidido</em> (ha tomado decisión)</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Locativo de actos</td><td style="padding:6px 8px"><em>El concierto es en Madrid</em></td><td style="padding:6px 8px"><em>El libro está en la mesa</em></td></tr>
</table>"""),
        ('ESTAR: Usos Avanzados y Expresiones Idiomáticas', None, """
<p style="margin:0 0 12px;font-size:.9rem">Estar aparece en construcciones que van más allá del simple estado.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Construcción</th><th style="padding:6px 8px;text-align:left">Significado</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Estar de + sustantivo</td><td style="padding:6px 8px">Función temporal</td><td style="padding:6px 8px"><em>Está de director esta semana</em></td></tr>
<tr><td style="padding:6px 8px">Estar como + sustantivo</td><td style="padding:6px 8px">Desempeñar papel</td><td style="padding:6px 8px"><em>Trabaja como intérprete</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Estar para + inf</td><td style="padding:6px 8px">Disposición/a punto</td><td style="padding:6px 8px"><em>No estoy para bromas / El postre está para comer</em></td></tr>
<tr><td style="padding:6px 8px">Estar por + inf</td><td style="padding:6px 8px">Acción pendiente</td><td style="padding:6px 8px"><em>El trabajo está por terminar</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Estar que + frase</td><td style="padding:6px 8px">Estado intenso</td><td style="padding:6px 8px"><em>Está que muerde de rabia</em></td></tr>
</table>"""),
        ('SER: Usos Menos Conocidos', None, """
<p style="margin:0 0 12px;font-size:.9rem">Ser no solo indica identidad o característica permanente — tiene usos discursivos importantes.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Uso</th><th style="padding:6px 8px;text-align:left">Ejemplo</th><th style="padding:6px 8px;text-align:left">Nota</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Ser + que (explicativo)</td><td style="padding:6px 8px"><em>Es que no pude venir</em></td><td style="padding:6px 8px">Excusa/aclaración</td></tr>
<tr><td style="padding:6px 8px">Ser en oraciones escindidas</td><td style="padding:6px 8px"><em>Fue en París donde lo conoció</em></td><td style="padding:6px 8px">Focalización</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Ser + hora/fecha</td><td style="padding:6px 8px"><em>Son las tres; Es lunes</em></td><td style="padding:6px 8px">Siempre ser, nunca estar</td></tr>
<tr><td style="padding:6px 8px">Ser de + material/origen</td><td style="padding:6px 8px"><em>La mesa es de madera</em></td><td style="padding:6px 8px">Composición/procedencia</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Ser + adj con cambio</td><td style="padding:6px 8px"><em>¡Hoy está muy guapa!</em></td><td style="padding:6px 8px">Estar indica sorpresa por cambio</td></tr>
</table>"""),
        ('HABER: Impersonal vs. SER/ESTAR Locativos', None, """
<p style="margin:0 0 12px;font-size:.9rem">Haber expresa existencia; estar expresa localización de algo ya conocido.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Contraste</th><th style="padding:6px 8px;text-align:left">Hay / Haber</th><th style="padding:6px 8px;text-align:left">Está / Estar</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Existencia</td><td style="padding:6px 8px"><em>Hay un libro en la mesa</em> (nuevo)</td><td style="padding:6px 8px"><em>El libro está en la mesa</em> (conocido)</td></tr>
<tr><td style="padding:6px 8px">Personas</td><td style="padding:6px 8px"><em>Hay mucha gente aquí</em></td><td style="padding:6px 8px"><em>La gente está aquí</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Error frecuente</td><td style="padding:6px 8px">*Hay el libro en la mesa</td><td style="padding:6px 8px">Con artículo definido → estar</td></tr>
<tr><td style="padding:6px 8px">Haber en tiempos comp.</td><td style="padding:6px 8px"><em>Habría habido</em> (cond perf)</td><td style="padding:6px 8px">Nunca concuerda con el sujeto</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Haber que + inf</td><td style="padding:6px 8px"><em>Hay que estudiar</em> (impersonal)</td><td style="padding:6px 8px">vs. tener que (personal)</td></tr>
</table>"""),
    ],
    traps=[
        ('*Está en Madrid el concierto.', 'El concierto es en Madrid.', '<em>Ser</em> localiza eventos programados; <em>estar</em> localiza personas y objetos.'),
        ('*Es muy cansado hoy.', 'Está muy cansado hoy.', 'El cansancio es un estado temporal → <em>estar</em>.'),
        ('*Hay el banco a la vuelta.', 'El banco está a la vuelta.', 'Con artículo definido (referencia conocida) se usa <em>estar</em>, no <em>haber</em>.'),
        ('*Están las tres.', 'Son las tres.', 'La hora siempre se expresa con <em>ser</em>.'),
        ('*Es decidido a irse.', 'Está decidido a irse.', '<em>Es decidido</em> describe el carácter; <em>está decidido</em> indica que ya tomó la decisión.'),
    ],
    summary=[
        ('ser + adj', 'Característica esencial o categoría', '<em>Es inteligente / Es médico</em>'),
        ('estar + adj', 'Estado o condición actual', '<em>Está cansado / Está lista</em>'),
        ('ser/estar + participio', 'ser = cualidad; estar = estado resultante', '<em>Es ordenado / Está ordenado</em>'),
        ('hay + indef', 'Existencia (información nueva)', '<em>Hay un problema</em>'),
        ('el X está en', 'Localización (referencia conocida)', '<em>El problema está en la gestión</em>'),
        ('ser de/en eventos', 'Material, origen, lugar de evento', '<em>La mesa es de roble / La cena es en casa</em>'),
        ('estar de + sust', 'Función temporal', '<em>Está de jefa esta semana</em>'),
    ],
    ex1=dict(
        title='Ejercicio 1: SER, ESTAR o HABER',
        questions=[
            ('La película ___ en el cine Rex a las ocho.',
             ['es', 'está', 'hay', 'tiene'], 0,
             '<em>Ser</em> localiza eventos programados: <em>La película <u>es</u> en el cine Rex.</em>'),
            ('No ___ nadie en la sala cuando llegamos.',
             ['era', 'estaba', 'había', 'fue'], 2,
             '<em>Haber</em> expresa existencia (impersonal): <em><u>había</u> nadie.</em>'),
            ('La directora ___ de viaje esta semana.',
             ['es', 'está', 'hay', 'tiene'], 1,
             '<em>Estar de</em> indica función/situación temporal: <em><u>está</u> de viaje.</em>'),
            ('Ese niño ___ muy listo — saca las mejores notas.',
             ['es', 'está', 'hay', 'tiene'], 0,
             '<em>Ser listo</em> describe la inteligencia como cualidad estable.'),
            ('¡Mira qué guapa ___ hoy!',
             ['es', 'está', 'hay', 'tiene'], 1,
             '<em>Estar</em> expresa la sorpresa ante un cambio o estado del momento.'),
            ('El informe ___ por revisar — nadie lo ha revisado aún.',
             ['es', 'está', 'hay', 'tiene'], 1,
             '<em>Estar por + inf</em> indica que la acción está pendiente de realizarse.'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Completa con la forma correcta',
        questions=[
            ('El trabajo ya _______ terminado; solo falta entregarlo.',
             'está', ['está', 'es', 'estaba'],
             '<em>Estar + participio</em> expresa resultado/estado: <em><u>está</u> terminado.</em>'),
            ('Cuando era joven, mi abuelo _______ muy alto.',
             'era', ['era', 'estaba', 'había'],
             '<em>Ser</em> para características físicas permanentes: <em><u>era</u> alto.</em>'),
            ('En esta ciudad _______ tres museos históricos.',
             'hay', ['hay', 'están', 'son'],
             '<em>Haber</em> introduce información nueva (no artículo definido): <em><u>hay</u> tres museos.</em>'),
            ('El paciente _______ mucho mejor desde la operación.',
             'está', ['está', 'es', 'hay'],
             '<em>Estar mejor</em> = estado de salud actual → <em><u>está</u>.</em>'),
            ('La reunión _______ en la sala de conferencias del tercer piso.',
             'es', ['es', 'está', 'hay'],
             '<em>Ser</em> localiza eventos programados: <em>La reunión <u>es</u> en la sala.</em>'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Elige la opción correcta',
        questions=[
            ('«La película ___ muy buena» — el crítico opina que tiene calidad artística.',
             ['es', 'está', 'hay', 'fue'], 0,
             '<em>Ser buena</em> = valoración de calidad objetiva/estable.'),
            ('«El café ___ muy bueno» — al cliente le gusta el sabor de esta taza.',
             ['es', 'está', 'hay', 'fue'], 1,
             '<em>Estar bueno</em> = valoración sensorial del momento (sabor).'),
            ('¿___ algún banco por aquí cerca?',
             ['Es', 'Está', 'Hay', 'Tiene'], 2,
             '<em>Haber</em> en pregunta de existencia: <em>¿<u>Hay</u> algún banco?</em>'),
            ('Mi hermano ___ de guardia en el hospital este fin de semana.',
             ['es', 'está', 'hay', 'tiene'], 1,
             '<em>Estar de guardia</em> = función temporal.'),
            ('¿A qué hora ___ la presentación de mañana?',
             ['es', 'está', 'hay', 'tiene'], 0,
             '<em>Ser</em> para eventos programados con hora: <em>¿A qué hora <u>es</u>?</em>'),
        ]
    ),
    game_desc='SER, ESTAR y HABER en contextos avanzados',
    items=[
        dict(term='ser de + material', definition='Indica de qué está hecho algo', example='La escultura es de bronce.', accept=['ser de + material', 'ser de material']),
        dict(term='estar de + sustantivo', definition='Desempeñar una función de forma temporal', example='Está de jefe esta semana.', accept=['estar de + sustantivo', 'estar de']),
        dict(term='estar por + infinitivo', definition='Indica que algo todavía no se ha realizado', example='El proyecto está por terminar.', accept=['estar por + infinitivo', 'estar por']),
        dict(term='hay + indefinido', definition='Expresa existencia de algo no conocido/nuevo', example='Hay un mensaje para ti.', accept=['hay + indefinido', 'haber + indefinido']),
        dict(term='ser + hora', definition='Expresar la hora con ser (nunca estar)', example='Son las cinco y media.', accept=['ser + hora', 'ser la hora']),
        dict(term='estar + participio', definition='Resultado o estado de una acción completada', example='La puerta está cerrada.', accept=['estar + participio']),
        dict(term='ser + participio', definition='Voz pasiva perifrástica con ser', example='El informe fue aprobado por el director.', accept=['ser + participio', 'ser pasivo']),
        dict(term='haber que + infinitivo', definition='Obligación impersonal', example='Hay que respetar las normas.', accept=['haber que + infinitivo', 'hay que']),
    ]
)

# ─────────────────────────────────────────────
# G12 · pronominal-c1 · El Sistema Pronominal: Clíticos y Combinaciones
# ─────────────────────────────────────────────
CHAPTERS['pronominal-c1'] = dict(
    level='c1', section='grammar', num='G12',
    short='El Sistema Pronominal',
    title='El Sistema Pronominal: Clíticos, Posición y Combinaciones',
    subtitle='Domina las combinaciones de clíticos, la posición y los usos especiales del pronombre',
    slides=[
        ('Los Pronombres Átonos: Formas y Funciones', None, """
<p style="margin:0 0 12px;font-size:.9rem">Los clíticos son átonos: se apoyan en el verbo y expresan CD, CI o ambos.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Persona</th><th style="padding:6px 8px;text-align:left">CD</th><th style="padding:6px 8px;text-align:left">CI</th><th style="padding:6px 8px;text-align:left">Reflexivo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">1ª sg</td><td style="padding:6px 8px">me</td><td style="padding:6px 8px">me</td><td style="padding:6px 8px">me</td></tr>
<tr><td style="padding:6px 8px">2ª sg</td><td style="padding:6px 8px">te</td><td style="padding:6px 8px">te</td><td style="padding:6px 8px">te</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">3ª sg masc</td><td style="padding:6px 8px">lo</td><td style="padding:6px 8px">le</td><td style="padding:6px 8px">se</td></tr>
<tr><td style="padding:6px 8px">3ª sg fem</td><td style="padding:6px 8px">la</td><td style="padding:6px 8px">le</td><td style="padding:6px 8px">se</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">1ª pl</td><td style="padding:6px 8px">nos</td><td style="padding:6px 8px">nos</td><td style="padding:6px 8px">nos</td></tr>
<tr><td style="padding:6px 8px">3ª pl</td><td style="padding:6px 8px">los / las</td><td style="padding:6px 8px">les</td><td style="padding:6px 8px">se</td></tr>
</table>"""),
        ('Combinación de Dos Clíticos: Orden y Regla SE', None, """
<p style="margin:0 0 12px;font-size:.9rem">Cuando hay dos clíticos, el CI va primero y el CD después. Le/les + lo/la/los/las → se lo/la/los/las.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Combinación</th><th style="padding:6px 8px;text-align:left">Forma correcta</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">le + lo</td><td style="padding:6px 8px">se lo</td><td style="padding:6px 8px"><em>Se lo doy a él</em></td></tr>
<tr><td style="padding:6px 8px">le + la</td><td style="padding:6px 8px">se la</td><td style="padding:6px 8px"><em>Se la expliqué</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">les + los</td><td style="padding:6px 8px">se los</td><td style="padding:6px 8px"><em>Se los mandé</em></td></tr>
<tr><td style="padding:6px 8px">me + lo</td><td style="padding:6px 8px">me lo</td><td style="padding:6px 8px"><em>Me lo dijiste</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">te + la</td><td style="padding:6px 8px">te la</td><td style="padding:6px 8px"><em>Te la presto</em></td></tr>
</table>"""),
        ('Posición de los Clíticos', None, """
<p style="margin:0 0 12px;font-size:.9rem">La posición depende del tipo de forma verbal.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Forma verbal</th><th style="padding:6px 8px;text-align:left">Posición</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Verbo conjugado</td><td style="padding:6px 8px">Antes (proclítico)</td><td style="padding:6px 8px"><em>Lo veo / Me llama</em></td></tr>
<tr><td style="padding:6px 8px">Infinitivo (solo)</td><td style="padding:6px 8px">Después (enclítico)</td><td style="padding:6px 8px"><em>Verlo / Llamarme</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Gerundio (solo)</td><td style="padding:6px 8px">Después</td><td style="padding:6px 8px"><em>Viéndolo / Llamándome</em></td></tr>
<tr><td style="padding:6px 8px">Imperativo afirmativo</td><td style="padding:6px 8px">Después</td><td style="padding:6px 8px"><em>Dímelo / Llámame</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Imperativo negativo</td><td style="padding:6px 8px">Antes</td><td style="padding:6px 8px"><em>No me digas / No lo hagas</em></td></tr>
<tr><td style="padding:6px 8px">Perífrasis verbal</td><td style="padding:6px 8px">Antes del conjugado o tras inf/ger</td><td style="padding:6px 8px"><em>Lo quiero hacer / Quiero hacerlo</em></td></tr>
</table>"""),
        ('Leísmo, Laísmo y Loísmo', None, """
<p style="margin:0 0 12px;font-size:.9rem">Variaciones en el uso de los pronombres de tercera persona.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Fenómeno</th><th style="padding:6px 8px;text-align:left">Descripción</th><th style="padding:6px 8px;text-align:left">Aceptado</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Leísmo personal</td><td style="padding:6px 8px">Le vi (= lo vi, pers. masc.) CD → le</td><td style="padding:6px 8px">Sí (norma culta, RAE acepta)</td></tr>
<tr><td style="padding:6px 8px">Leísmo de cosa</td><td style="padding:6px 8px">Le busqué (el libro) → le en lugar de lo</td><td style="padding:6px 8px">No</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Laísmo</td><td style="padding:6px 8px">La dije (a ella) — CI → la</td><td style="padding:6px 8px">No</td></tr>
<tr><td style="padding:6px 8px">Loísmo</td><td style="padding:6px 8px">Lo dije (a él) — CI → lo</td><td style="padding:6px 8px">No</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Pronombre ético</td><td style="padding:6px 8px">¡No te me vayas! — implicación afectiva</td><td style="padding:6px 8px">Coloquial, sí</td></tr>
</table>"""),
    ],
    traps=[
        ('*Le vi el coche (refiriéndose a la cosa).', 'Lo vi / Lo compré (el coche).', 'El leísmo de cosa no está aceptado. Para objetos inanimados, CD → <em>lo/la/los/las</em>.'),
        ('*La dije que viniera.', 'Le dije que viniera.', 'El laísmo no está aceptado. CI siempre → <em>le/les</em>.'),
        ('*Dámelo a mí primero.', 'Dámelo. / Dámelo a mí.', 'Con imperativo afirmativo el clítico va después del verbo unido: <em>Dá-me-lo</em>.'),
        ('*Le + lo → lelo.', 'Le + lo → se lo.', 'La combinación CI <em>le/les</em> + CD <em>lo/la</em> se convierte en <em>se lo/la/los/las</em>.'),
        ('*No diciéndole nada.', 'No le digas nada. / Sin decirle nada.','El imperativo negativo requiere <em>no</em> + verbo conjugado; el gerundio solo no forma negativo imperativo.'),
    ],
    summary=[
        ('CD 3ª persona', 'lo, la, los, las', '<em>Lo vi / Las compré</em>'),
        ('CI 3ª persona', 'le, les', '<em>Le dije la verdad</em>'),
        ('le/les + lo/la', 'se lo/la/los/las', '<em>Se lo expliqué (= le expliqué el libro)</em>'),
        ('Posición proclítica', 'Antes del verbo conjugado', '<em>Me lo dijo</em>'),
        ('Posición enclítica', 'Unido tras inf/ger/imp. afirm.', '<em>Decírmelo / Dímelo</em>'),
        ('Leísmo personal', 'Le vi (a él) — RAE acepta', '<em>Le invité a la fiesta</em>'),
        ('Pronombre ético', 'Implicación afectiva sin función gramatical', '<em>¡No te me vayas tan pronto!</em>'),
    ],
    ex1=dict(
        title='Ejercicio 1: Pronombres en contexto',
        questions=[
            ('— ¿Le has dado el regalo a María? — Sí, ___ ___ di ayer.',
             ['le lo', 'se lo', 'lo le', 'la le'], 1,
             'Le + lo → <em>se lo</em>: <em><u>Se lo</u> di ayer.</em>'),
            ('— ¿Puedes traerme el libro? — Claro, voy a traér___ ahora mismo.',
             ['lo te', 'te lo', 'me lo', 'le la'], 1,
             'El clítico enclítico en infinitivo: <em>traér<u>te</u>lo</em>. Pero aquí la respuesta con los datos es <em>te lo</em> en posición proclítica o enclítica.'),
            ('No ___ digas nada a tus padres sobre esto.',
             ['les', 'los', 'las', 'se'], 0,
             'CI 3ª plural → <em>les</em>: <em>No <u>les</u> digas nada.</em>'),
            ('¡Escúcha___ bien, que es importante!',
             ['me', 'le', 'lo', 'la'], 0,
             'Imperativo afirmativo + CD 1ª persona: <em>Escúcha<u>me</u>.</em>'),
            ('___ llamaron pero no estaba en casa.',
             ['Me', 'Le', 'Lo', 'La'], 0,
             'CD/reflexivo 1ª persona (me llamaron = llamaron a mí): <em><u>Me</u> llamaron.</em>'),
            ('¿Puedo ver ___ fotos de la boda?',
             ['lo', 'los', 'la', 'las'], 3,
             'CD femenino plural <em>fotos</em> → <em><u>las</u></em>.'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Reescribe con clíticos',
        questions=[
            ('Tienes que devolver el libro a tu amigo. → Tienes que _______ _______.',
             'devolvérselo', ['devolvérselo', 'se lo devolver'],
             'CI <em>le</em> + CD <em>lo</em> → <em>se lo</em> enclítico en infinitivo: <em>devolver<u>sélo</u>.</em>'),
            ('Da el documento a nosotros. → _______.',
             'Dánoslo', ['Dánoslo', 'Nos lo da'],
             'Imperativo afirmativo + CI <em>nos</em> + CD <em>lo</em>: <em><u>Dánoslo</u>.</em>'),
            ('No expliques el problema a los estudiantes. → No _______ _______ expliques.',
             'se lo', ['se lo', 'les lo'],
             'Imperativo negativo con CI/CD: <em>No <u>se lo</u> expliques.</em>'),
            ('Estoy contando una historia a ella. → _______.',
             'Se la estoy contando', ['Se la estoy contando', 'Le la estoy contando'],
             'CI <em>le</em> + CD <em>la</em> → <em><u>se la</u></em>: <em><u>Se la</u> estoy contando.</em>'),
            ('Manda las fotos a tus amigos. → _______.',
             'Mándaselas', ['Mándaselas', 'Mándales las'],
             'Imperativo afirmativo + CI <em>les</em> + CD <em>las</em> → <em><u>Mándaselas</u>.</em>'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Posición correcta',
        questions=[
            ('¿Cuándo ___ vas a contar la verdad?',
             ['me lo', 'lo me', 'me la', 'la me'], 0,
             'CI <em>me</em> antes que CD <em>lo</em> (la verdad → la verdad): pero <em>la</em> verdad → debería ser <em>me la</em>. Corrección: <em><u>me la</u> vas a contar</em>.'),
            ('Deja ___ en paz, por favor.',
             ['me', 'a me', 'a mí', 'conmigo'], 0,
             'Con imperativo afirmativo, clítico unido o proclítico separado: <em>Déja<u>me</u> en paz.</em>'),
            ('No ___ hagas eso.',
             ['me lo', 'melo', 'lo me', 'me'], 0,
             'Imperativo negativo: clíticos van antes del verbo: <em>No <u>me lo</u> hagas.</em>'),
            ('___ la entregaron ayer mismo.',
             ['Se', 'Le', 'La', 'Lo'], 0,
             'CI <em>le</em> + CD <em>la</em> → <em><u>Se</u> la entregaron.</em>'),
            ('Voy a explicár___ mañana.',
             ['telo', 'te lo', 'lo te', 'les lo'], 1,
             'Enclítico en infinitivo: <em>explicár<u>te</u>lo</em> — o proclítico: <em>Te lo</em> voy a explicar.'),
        ]
    ),
    game_desc='Pronombres clíticos: combinaciones, posición y norma culta',
    items=[
        dict(term='clítico de CI', definition='Pronombre átono de objeto indirecto: me, te, le, nos, os, les', example='Le dije la verdad.', accept=['clítico de CI', 'pronombre de CI', 'le les']),
        dict(term='clítico de CD', definition='Pronombre átono de objeto directo: me, te, lo, la, nos, os, los, las', example='Lo compré ayer.', accept=['clítico de CD', 'pronombre de CD']),
        dict(term='regla se lo', definition='Le/les + lo/la/los/las → se lo/la/los/las', example='Se lo expliqué a Juan.', accept=['regla se lo', 'le + lo → se lo']),
        dict(term='enclítico', definition='Clítico unido tras infinitivo, gerundio o imperativo afirmativo', example='Decírmelo / Dímelo', accept=['enclítico']),
        dict(term='proclítico', definition='Clítico colocado antes del verbo conjugado', example='Me lo dijo ayer.', accept=['proclítico']),
        dict(term='leísmo personal', definition='Uso de le como CD para personas masculinas (aceptado por la RAE)', example='Le vi en la calle (= lo vi, a él).', accept=['leísmo personal', 'leísmo']),
        dict(term='laísmo', definition='Uso incorrecto de la/las como CI femenino', example='*La dije que viniera.', accept=['laísmo']),
        dict(term='pronombre ético', definition='Clítico sin función gramatical que expresa implicación afectiva', example='¡No te me vayas tan pronto!', accept=['pronombre ético', 'dativo ético']),
    ]
)

# ─────────────────────────────────────────────
# G13 · subordinadas-c1 · Subordinadas Sustantivas: Modo y Diferencias Semánticas
# ─────────────────────────────────────────────
CHAPTERS['subordinadas-c1'] = dict(
    level='c1', section='grammar', num='G13',
    short='Subordinadas: Modo',
    title='Subordinadas Sustantivas: Modo y Diferencias Semánticas',
    subtitle='Controla cuándo una subordinada exige indicativo o subjuntivo según el verbo principal',
    slides=[
        ('Verbos de Comunicación y Pensamiento: Indicativo', None, """
<p style="margin:0 0 12px;font-size:.9rem">Los verbos que afirman, informan o creen exigen <strong>indicativo</strong> en la subordinada.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Verbo principal</th><th style="padding:6px 8px;text-align:left">Modo</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">decir, afirmar, señalar</td><td style="padding:6px 8px">indicativo</td><td style="padding:6px 8px"><em>Dice que viene mañana</em></td></tr>
<tr><td style="padding:6px 8px">saber, conocer, recordar</td><td style="padding:6px 8px">indicativo</td><td style="padding:6px 8px"><em>Sé que tiene razón</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">creer, pensar, suponer</td><td style="padding:6px 8px">indicativo</td><td style="padding:6px 8px"><em>Creo que llegará tarde</em></td></tr>
<tr><td style="padding:6px 8px">ver, notar, comprobar</td><td style="padding:6px 8px">indicativo</td><td style="padding:6px 8px"><em>Noto que está nervioso</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">es evidente/cierto/claro</td><td style="padding:6px 8px">indicativo</td><td style="padding:6px 8px"><em>Es evidente que lo sabe</em></td></tr>
</table>"""),
        ('Verbos de Influencia, Deseo y Emoción: Subjuntivo', None, """
<p style="margin:0 0 12px;font-size:.9rem">Los verbos que influyen en otro sujeto, desean o valoran exigen <strong>subjuntivo</strong>.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Verbo principal</th><th style="padding:6px 8px;text-align:left">Modo</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">querer, desear, esperar</td><td style="padding:6px 8px">subjuntivo</td><td style="padding:6px 8px"><em>Quiero que vengas</em></td></tr>
<tr><td style="padding:6px 8px">pedir, ordenar, prohibir</td><td style="padding:6px 8px">subjuntivo</td><td style="padding:6px 8px"><em>Pide que lo haga</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">alegrarse de, temer, sorprender</td><td style="padding:6px 8px">subjuntivo</td><td style="padding:6px 8px"><em>Me alegra que estés aquí</em></td></tr>
<tr><td style="padding:6px 8px">es importante/necesario/posible</td><td style="padding:6px 8px">subjuntivo</td><td style="padding:6px 8px"><em>Es posible que llueva</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">dudar de, negar</td><td style="padding:6px 8px">subjuntivo</td><td style="padding:6px 8px"><em>Dudo que lo sepa</em></td></tr>
</table>"""),
        ('Verbos que Cambian de Modo al Negarse', None, """
<p style="margin:0 0 12px;font-size:.9rem">Al negar algunos verbos de certeza o pensamiento, el modo pasa a subjuntivo.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Afirmativo + indicativo</th><th style="padding:6px 8px;text-align:left">Negativo + subjuntivo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>Creo que viene</em></td><td style="padding:6px 8px"><em>No creo que venga</em></td></tr>
<tr><td style="padding:6px 8px"><em>Pienso que tiene razón</em></td><td style="padding:6px 8px"><em>No pienso que tenga razón</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>Es cierto que lo sabe</em></td><td style="padding:6px 8px"><em>No es cierto que lo sepa</em></td></tr>
<tr><td style="padding:6px 8px"><em>Parece que está enfermo</em></td><td style="padding:6px 8px"><em>No parece que esté enfermo</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>Es verdad que lo hizo</em></td><td style="padding:6px 8px"><em>No es verdad que lo hiciera</em></td></tr>
</table>"""),
        ('Mismo Sujeto: Infinitivo en lugar de que + Subjuntivo', None, """
<p style="margin:0 0 12px;font-size:.9rem">Cuando el sujeto de la principal y la subordinada es el mismo, se prefiere el infinitivo.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Mismo sujeto → infinitivo</th><th style="padding:6px 8px;text-align:left">Diferente sujeto → que + subj</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>Quiero comer</em></td><td style="padding:6px 8px"><em>Quiero que él coma</em></td></tr>
<tr><td style="padding:6px 8px"><em>Prefiero quedarme</em></td><td style="padding:6px 8px"><em>Prefiero que te quedes tú</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>Espero aprobar</em></td><td style="padding:6px 8px"><em>Espero que apruebes</em></td></tr>
<tr><td style="padding:6px 8px"><em>Siento llegar tarde</em></td><td style="padding:6px 8px"><em>Siento que llegues tarde</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px"><em>Temo equivocarme</em></td><td style="padding:6px 8px"><em>Temo que se equivoque</em></td></tr>
</table>"""),
    ],
    traps=[
        ('*Creo que venga mañana.', 'Creo que viene mañana.', '<em>Creer</em> en afirmativo + indicativo: expresa certeza del hablante.'),
        ('*No creo que viene.', 'No creo que venga.', '<em>No creer</em> + subjuntivo: la negación convierte la certeza en duda.'),
        ('*Quiero que voy al cine.', 'Quiero ir al cine.', 'Mismo sujeto → infinitivo, no <em>que + subjuntivo</em>.'),
        ('*Es evidente que lo sepa.', 'Es evidente que lo sabe.','Expresiones de certeza (<em>es evidente, es claro, es obvio</em>) exigen indicativo.'),
        ('*Pido que vas al médico.', 'Pido que vayas al médico.', '<em>Pedir</em> exige subjuntivo en la subordinada (diferente sujeto).'),
    ],
    summary=[
        ('certeza → indicativo', 'saber/creer/ver/es cierto + que + indic.', '<em>Creo que tiene razón</em>'),
        ('negación de certeza → subjuntivo', 'no creer/no pensar/no es cierto + que + subj.', '<em>No creo que tenga razón</em>'),
        ('influencia → subjuntivo', 'querer/pedir/permitir/prohibir + que + subj.', '<em>Pide que lo hagas</em>'),
        ('emoción → subjuntivo', 'alegrarse/temer/sorprender + que + subj.', '<em>Me sorprende que no lo sepa</em>'),
        ('mismo sujeto', 'verbo principal + infinitivo', '<em>Espero aprobar</em>'),
        ('diferente sujeto', 'verbo principal + que + subjuntivo', '<em>Espero que apruebes</em>'),
        ('duda → subjuntivo', 'dudar de / es posible / es probable + que + subj.', '<em>Es posible que llueva</em>'),
    ],
    ex1=dict(
        title='Ejercicio 1: Indicativo o Subjuntivo',
        questions=[
            ('El médico dice que el paciente ___ mejor muy pronto.',
             ['estará', 'esté', 'estuvo', 'estaría'], 0,
             '<em>Decir</em> con sentido informativo → indicativo: <em><u>estará</u> mejor.</em>'),
            ('No es verdad que nosotros ___ el dinero.',
             ['tomamos', 'tomáramos', 'tomemos', 'hayamos tomado'], 2,
             '<em>No es verdad que</em> → subjuntivo: <em><u>hayamos tomado</u></em> (perfecto) o <em>tomemos</em>.'),
            ('Me sorprende que ella no ___ nada sobre el cambio.',
             ['sabe', 'supo', 'sepa', 'sabría'], 2,
             '<em>Sorprender</em> (emoción) → subjuntivo: <em><u>sepa</u>.</em>'),
            ('Pienso que la propuesta ___ interesante.',
             ['es', 'sea', 'fuera', 'sería'], 0,
             '<em>Pensar</em> afirmativo → indicativo: <em><u>es</u> interesante.</em>'),
            ('No pienso que la propuesta ___ tan buena como dicen.',
             ['es', 'sea', 'fuera', 'sería'], 1,
             '<em>No pensar</em> → subjuntivo: <em><u>sea</u> tan buena.</em>'),
            ('La directora pidió que todos ___ el informe antes del viernes.',
             ['entregan', 'entregaron', 'entreguen', 'entregarán'], 2,
             '<em>Pedir</em> → subjuntivo: <em><u>entreguen</u> el informe.</em>'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Completa con infinitivo o que + subjuntivo',
        questions=[
            ('Espero _______ (poder) asistir a la conferencia.',
             'poder', ['poder', 'que pueda'],
             'Mismo sujeto → infinitivo: <em>Espero <u>poder</u> asistir.</em>'),
            ('Mi jefe exige que nosotros _______ (llegar) puntualmente.',
             'lleguemos', ['lleguemos', 'llegamos'],
             'Diferente sujeto + exigir → subjuntivo: <em>que <u>lleguemos</u>.</em>'),
            ('Es importante _______ (descansar) bien antes del examen.',
             'descansar', ['descansar', 'que descanse'],
             'Con sujeto impersonal + mismo destinatario implícito → infinitivo: <em>Es importante <u>descansar</u>.</em>'),
            ('No creo que ellos _______ (tener) suficiente experiencia.',
             'tengan', ['tengan', 'tienen'],
             '<em>No creer</em> → subjuntivo: <em>que <u>tengan</u>.</em>'),
            ('Temo _______ (equivocarse) en el análisis.',
             'equivocarme', ['equivocarme', 'que me equivoque'],
             'Mismo sujeto → infinitivo reflexivo: <em>Temo <u>equivocarme</u>.</em>'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Elige la forma correcta',
        questions=[
            ('Es evidente que el proyecto ___ un gran esfuerzo.',
             ['requiere', 'requiera', 'requiriera', 'requerirá'], 0,
             '<em>Es evidente que</em> → indicativo: <em><u>requiere</u>.</em>'),
            ('Dudo mucho que ellos ___ a tiempo.',
             ['llegan', 'lleguen', 'llegaron', 'llegaban'], 1,
             '<em>Dudar</em> → subjuntivo: <em><u>lleguen</u> a tiempo.</em>'),
            ('Me alegra que todo ___ bien.',
             ['sale', 'salga', 'salió', 'saldría'], 1,
             '<em>Alegrar</em> (emoción) → subjuntivo presente: <em><u>salga</u> bien.</em>'),
            ('Está claro que el mercado ___ una recuperación.',
             ['experimenta', 'experimente', 'experimentara', 'haya experimentado'], 0,
             '<em>Está claro que</em> → indicativo: <em><u>experimenta</u>.</em>'),
            ('No está claro que la medida ___ los resultados esperados.',
             ['produce', 'produzca', 'produjo', 'produjera'], 1,
             '<em>No está claro que</em> → subjuntivo: <em><u>produzca</u>.</em>'),
        ]
    ),
    game_desc='Controla el modo en las subordinadas sustantivas según el verbo principal',
    items=[
        dict(term='creer + indicativo', definition='Verbo de opinión en afirmativo → indicativo', example='Creo que tiene razón.', accept=['creer + indicativo']),
        dict(term='no creer + subjuntivo', definition='Negación de opinión → subjuntivo', example='No creo que tenga razón.', accept=['no creer + subjuntivo']),
        dict(term='querer + subjuntivo', definition='Verbo de deseo con diferente sujeto → subjuntivo', example='Quiero que vengas.', accept=['querer + subjuntivo']),
        dict(term='mismo sujeto + infinitivo', definition='Cuando el sujeto es el mismo en ambas cláusulas, se usa infinitivo', example='Espero aprobar el examen.', accept=['mismo sujeto + infinitivo', 'infinitivo mismo sujeto']),
        dict(term='es cierto + indicativo', definition='Expresiones de certeza → indicativo', example='Es cierto que lo hizo.', accept=['es cierto + indicativo']),
        dict(term='no es cierto + subjuntivo', definition='Negación de certeza → subjuntivo', example='No es cierto que lo hiciera.', accept=['no es cierto + subjuntivo']),
        dict(term='es posible + subjuntivo', definition='Expresiones de posibilidad/valoración → subjuntivo', example='Es posible que llueva mañana.', accept=['es posible + subjuntivo']),
        dict(term='pedir + subjuntivo', definition='Verbos de influencia siempre exigen subjuntivo (distinto sujeto)', example='Le pidió que enviara el informe.', accept=['pedir + subjuntivo', 'verbos de influencia + subjuntivo']),
    ]
)

# ─────────────────────────────────────────────
# G14 · regimen-preposicional · El Régimen Preposicional de Verbos y Adjetivos
# ─────────────────────────────────────────────
CHAPTERS['regimen-preposicional'] = dict(
    level='c1', section='grammar', num='G14',
    short='Régimen Preposicional',
    title='El Régimen Preposicional de Verbos y Adjetivos',
    subtitle='Aprende qué preposición exige cada verbo y adjetivo en español estándar',
    slides=[
        ('Verbos con Preposición A', None, """
<p style="margin:0 0 12px;font-size:.9rem">Muchos verbos exigen <em>a</em> antes de su complemento nominal o de infinitivo.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Verbo</th><th style="padding:6px 8px;text-align:left">Ejemplo</th><th style="padding:6px 8px;text-align:left">Nota</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">aprender a + inf</td><td style="padding:6px 8px"><em>Aprende a cocinar</em></td><td style="padding:6px 8px">Habilidad</td></tr>
<tr><td style="padding:6px 8px">ayudar a + inf</td><td style="padding:6px 8px"><em>Me ayudó a resolverlo</em></td><td style="padding:6px 8px">Asistencia</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">comenzar/empezar a + inf</td><td style="padding:6px 8px"><em>Empezó a llover</em></td><td style="padding:6px 8px">Incoativo</td></tr>
<tr><td style="padding:6px 8px">llegar a + inf</td><td style="padding:6px 8px"><em>Llegó a ser director</em></td><td style="padding:6px 8px">Logro progresivo</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">obligar a + inf</td><td style="padding:6px 8px"><em>Le obligaron a firmar</em></td><td style="padding:6px 8px">Coerción</td></tr>
<tr><td style="padding:6px 8px">jugar a + sust</td><td style="padding:6px 8px"><em>Juegan al fútbol</em></td><td style="padding:6px 8px">Deporte/juego</td></tr>
</table>"""),
        ('Verbos con Preposición DE y EN', None, """
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Verbo + DE</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">depender de</td><td style="padding:6px 8px"><em>Depende del tiempo</em></td></tr>
<tr><td style="padding:6px 8px">olvidarse de</td><td style="padding:6px 8px"><em>Se olvidó de llamar</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">tratar de + inf</td><td style="padding:6px 8px"><em>Trata de mejorar</em></td></tr>
<tr><td style="padding:6px 8px">hablar de + sust</td><td style="padding:6px 8px"><em>Habla de política</em></td></tr>
</table>
<table style="width:100%;border-collapse:collapse;font-size:.83rem;margin-top:8px">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Verbo + EN</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">pensar en</td><td style="padding:6px 8px"><em>Pienso en ti</em></td></tr>
<tr><td style="padding:6px 8px">confiar en</td><td style="padding:6px 8px"><em>Confío en ella</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">insistir en + inf</td><td style="padding:6px 8px"><em>Insiste en venir</em></td></tr>
<tr><td style="padding:6px 8px">tardar en + inf</td><td style="padding:6px 8px"><em>Tardó en responder</em></td></tr>
</table>"""),
        ('Verbos con CON, POR y PARA', None, """
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Verbo + CON</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">contar con</td><td style="padding:6px 8px"><em>Cuento contigo</em></td></tr>
<tr><td style="padding:6px 8px">soñar con</td><td style="padding:6px 8px"><em>Sueña con viajar</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">encontrarse con</td><td style="padding:6px 8px"><em>Me encontré con Ana</em></td></tr>
</table>
<table style="width:100%;border-collapse:collapse;font-size:.83rem;margin-top:8px">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Verbo + POR / PARA</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">preocuparse por</td><td style="padding:6px 8px"><em>Se preocupa por su salud</em></td></tr>
<tr><td style="padding:6px 8px">luchar por</td><td style="padding:6px 8px"><em>Lucha por sus derechos</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">prepararse para</td><td style="padding:6px 8px"><em>Se prepara para el examen</em></td></tr>
<tr><td style="padding:6px 8px">optar por</td><td style="padding:6px 8px"><em>Optó por no ir</em></td></tr>
</table>"""),
        ('Adjetivos con Preposición', None, """
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Adjetivo + prep</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">capaz de + inf/sust</td><td style="padding:6px 8px"><em>Es capaz de todo</em></td></tr>
<tr><td style="padding:6px 8px">orgulloso de + sust</td><td style="padding:6px 8px"><em>Está orgulloso de su trabajo</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">acostumbrado a + inf/sust</td><td style="padding:6px 8px"><em>Está acostumbrado a trabajar</em></td></tr>
<tr><td style="padding:6px 8px">harto de + sust/inf</td><td style="padding:6px 8px"><em>Estoy harto de esperar</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">interesado en + sust</td><td style="padding:6px 8px"><em>Está interesado en el proyecto</em></td></tr>
<tr><td style="padding:6px 8px">listo para + inf/sust</td><td style="padding:6px 8px"><em>Estoy listo para salir</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">contento con + sust</td><td style="padding:6px 8px"><em>Estoy contento con el resultado</em></td></tr>
</table>"""),
    ],
    traps=[
        ('*Pienso de ti constantemente.', 'Pienso en ti constantemente.', '<em>Pensar</em> con complemento de pensamiento → <em>en</em>: <em>pienso <u>en</u> ti.</em>'),
        ('*Cuento de ti para el proyecto.', 'Cuento contigo para el proyecto.', '<em>Contar con</em> = depender de alguien. <em>Contar de</em> = narrar sobre algo.'),
        ('*Dependo a mis padres económicamente.', 'Dependo de mis padres económicamente.', '<em>Depender</em> exige <em>de</em>, no <em>a</em>.'),
        ('*Tardé de contestar el correo.', 'Tardé en contestar el correo.', '<em>Tardar en + inf</em>: <em>tardé <u>en</u> contestar.</em>'),
        ('*Está acostumbrado con el frío.', 'Está acostumbrado al frío.', '<em>Acostumbrado a</em>: <em>acostumbrado <u>al</u> frío</em> (a + el).'),
    ],
    summary=[
        ('aprender/empezar/ayudar/llegar + a + inf', 'Preposición a ante infinitivo', '<em>Empezó a trabajar</em>'),
        ('hablar/olvidarse/depender/tratar + de', 'Preposición de', '<em>Olvidé de llamarla / habla de política</em>'),
        ('pensar/confiar/insistir/tardar + en', 'Preposición en', '<em>Confía en ella / tarda en responder</em>'),
        ('contar/soñar/encontrarse + con', 'Preposición con', '<em>Cuento contigo</em>'),
        ('preocuparse/luchar/interesarse + por', 'Preposición por', '<em>Se preocupa por el resultado</em>'),
        ('capaz/orgulloso/harto + de', 'Adjetivo + de', '<em>Está harto de esperar</em>'),
        ('acostumbrado/listo/interesado + a/para/en', 'Adjetivos con distintas preps', '<em>Acostumbrado a; listo para; interesado en</em>'),
    ],
    ex1=dict(
        title='Ejercicio 1: Elige la preposición correcta',
        questions=[
            ('Llevamos meses soñando ___ viajar por toda América del Sur.',
             ['de', 'con', 'en', 'a'], 1,
             '<em>Soñar con</em>: <em>soñando <u>con</u> viajar.</em>'),
            ('La empresa depende ___ los contratos públicos para su supervivencia.',
             ['a', 'de', 'en', 'con'], 1,
             '<em>Depender de</em>: <em>depende <u>de</u> los contratos.</em>'),
            ('El equipo tardó mucho ___ adaptarse al nuevo sistema.',
             ['de', 'a', 'en', 'con'], 2,
             '<em>Tardar en + inf</em>: <em>tardó <u>en</u> adaptarse.</em>'),
            ('¿Puedo contar ___ tu ayuda para el evento de mañana?',
             ['de', 'a', 'con', 'en'], 2,
             '<em>Contar con</em> = depender de: <em>contar <u>con</u> tu ayuda.</em>'),
            ('Me olvidé completamente ___ hacer la reserva.',
             ['a', 'de', 'en', 'con'], 1,
             '<em>Olvidarse de + inf</em>: <em>olvidé <u>de</u> hacer.</em>'),
            ('El candidato optó ___ retirarse antes de que publicaran los resultados.',
             ['a', 'de', 'en', 'por'], 3,
             '<em>Optar por</em>: <em>optó <u>por</u> retirarse.</em>'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Completa con la preposición adecuada',
        questions=[
            ('Estoy muy orgulloso _______ ti y de todo lo que has conseguido.',
             'de', ['de', 'con', 'en'],
             '<em>Orgulloso de</em>: <em>orgulloso <u>de</u> ti.</em>'),
            ('Lleva años luchando _______ mejorar las condiciones laborales.',
             'por', ['por', 'a', 'de'],
             '<em>Luchar por</em>: <em>luchando <u>por</u> mejorar.</em>'),
            ('¿Estáis ya listos _______ salir?',
             'para', ['para', 'de', 'en'],
             '<em>Listo para + inf</em>: <em>listos <u>para</u> salir.</em>'),
            ('Insistió _______ revisar cada detalle del contrato.',
             'en', ['en', 'a', 'de'],
             '<em>Insistir en + inf</em>: <em>insistió <u>en</u> revisar.</em>'),
            ('Comenzó _______ sentirse mejor después del tratamiento.',
             'a', ['a', 'de', 'en'],
             '<em>Comenzar a + inf</em>: <em>comenzó <u>a</u> sentirse mejor.</em>'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Elige la combinación correcta',
        questions=[
            ('El estudiante estaba acostumbrado ___ trabajar bajo presión.',
             ['de', 'con', 'a', 'en'], 2,
             '<em>Acostumbrado a + inf</em>: <em>acostumbrado <u>a</u> trabajar.</em>'),
            ('¿Piensas mucho ___ el futuro?',
             ['de', 'con', 'a', 'en'], 3,
             '<em>Pensar en</em> (reflexión) → <em><u>en</u> el futuro.</em>'),
            ('Quedé ___ Luis para vernos el sábado.',
             ['a', 'con', 'de', 'en'], 1,
             '<em>Quedar con</em> (citar a alguien): <em>quedé <u>con</u> Luis.</em>'),
            ('El proyecto consistía ___ tres fases principales.',
             ['a', 'de', 'con', 'en'], 3,
             '<em>Consistir en</em>: <em>consistía <u>en</u> tres fases.</em>'),
            ('El director se preocupa mucho ___ sus empleados.',
             ['en', 'de', 'por', 'con'], 2,
             '<em>Preocuparse por</em>: <em>se preocupa <u>por</u> sus empleados.</em>'),
        ]
    ),
    game_desc='El régimen preposicional de verbos y adjetivos en español estándar',
    items=[
        dict(term='tardar en', definition='Emplear tiempo antes de hacer algo', example='Tardó mucho en responder.', accept=['tardar en']),
        dict(term='contar con', definition='Depender de alguien o tener algo disponible', example='Cuento contigo para el proyecto.', accept=['contar con']),
        dict(term='olvidarse de', definition='No recordar hacer algo', example='Se olvidó de enviar el correo.', accept=['olvidarse de']),
        dict(term='depender de', definition='Estar condicionado por algo o alguien', example='El resultado depende del esfuerzo.', accept=['depender de']),
        dict(term='insistir en', definition='Repetir o mantener con firmeza una acción o postura', example='Insistió en venir a pesar del cansancio.', accept=['insistir en']),
        dict(term='orgulloso de', definition='Adjetivo que expresa satisfacción por algo propio o ajeno', example='Estamos orgullosos de vuestro trabajo.', accept=['orgulloso de']),
        dict(term='acostumbrado a', definition='Habituado a algo o a realizar una acción', example='Está acostumbrado a trabajar tarde.', accept=['acostumbrado a']),
        dict(term='optar por', definition='Elegir entre varias posibilidades', example='Optaron por cancelar el evento.', accept=['optar por']),
    ]
)

# ─────────────────────────────────────────────
# G15 · modalidad-epistemica · Modalidad y Atenuación en el Discurso
# ─────────────────────────────────────────────
CHAPTERS['modalidad-epistemica'] = dict(
    level='c1', section='grammar', num='G15',
    short='Modalidad y Atenuación',
    title='La Modalidad Epistémica y la Atenuación en el Discurso',
    subtitle='Usa atenuadores, intensificadores y verbos modales para modular tu discurso con precisión',
    slides=[
        ('La Modalidad Epistémica: Certeza y Probabilidad', None, """
<p style="margin:0 0 12px;font-size:.9rem">La modalidad epistémica expresa el grado de certeza del hablante respecto a lo que dice.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Grado</th><th style="padding:6px 8px;text-align:left">Expresión</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Certeza total</td><td style="padding:6px 8px">sin duda, evidentemente, claramente</td><td style="padding:6px 8px"><em>Sin duda, es la mejor opción</em></td></tr>
<tr><td style="padding:6px 8px">Alta probabilidad</td><td style="padding:6px 8px">debe de, seguramente, probablemente</td><td style="padding:6px 8px"><em>Debe de tener treinta años</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Posibilidad media</td><td style="padding:6px 8px">quizás/tal vez + subj/ind, puede que</td><td style="padding:6px 8px"><em>Quizás venga mañana</em></td></tr>
<tr><td style="padding:6px 8px">Hipótesis</td><td style="padding:6px 8px">podría, debería, al parecer</td><td style="padding:6px 8px"><em>Podría ser que estuviera enfermo</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Duda/incertidumbre</td><td style="padding:6px 8px">no está claro, es dudoso, tal vez</td><td style="padding:6px 8px"><em>No está claro que funcione</em></td></tr>
</table>"""),
        ('Atenuadores del Discurso', None, """
<p style="margin:0 0 12px;font-size:.9rem">Los atenuadores reducen la fuerza de una afirmación o crítica, clave en el registro formal.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Tipo</th><th style="padding:6px 8px;text-align:left">Expresión</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Cuantificación parcial</td><td style="padding:6px 8px">en cierta medida, hasta cierto punto</td><td style="padding:6px 8px"><em>En cierta medida, tiene razón</em></td></tr>
<tr><td style="padding:6px 8px">Aproximación</td><td style="padding:6px 8px">algo, un tanto, relativamente</td><td style="padding:6px 8px"><em>El texto es algo denso</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Evidencialidad</td><td style="padding:6px 8px">al parecer, según parece, se dice que</td><td style="padding:6px 8px"><em>Al parecer, dimitirá en breve</em></td></tr>
<tr><td style="padding:6px 8px">Cortesía verbal</td><td style="padding:6px 8px">quisiera, podría, me gustaría</td><td style="padding:6px 8px"><em>Quisiera hacer una observación</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Impersonalización</td><td style="padding:6px 8px">se podría decir, cabría afirmar</td><td style="padding:6px 8px"><em>Cabría decir que el enfoque es limitado</em></td></tr>
</table>"""),
        ('Intensificadores del Discurso', None, """
<p style="margin:0 0 12px;font-size:.9rem">Los intensificadores refuerzan la asertividad o el argumento.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Tipo</th><th style="padding:6px 8px;text-align:left">Expresión</th><th style="padding:6px 8px;text-align:left">Ejemplo</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Certeza asertiva</td><td style="padding:6px 8px">indudablemente, sin lugar a dudas</td><td style="padding:6px 8px"><em>Indudablemente, es el mejor candidato</em></td></tr>
<tr><td style="padding:6px 8px">Énfasis afirmativo</td><td style="padding:6px 8px">desde luego, por supuesto, naturalmente</td><td style="padding:6px 8px"><em>Desde luego, lo apoyaremos</em></td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Reformulación enfática</td><td style="padding:6px 8px">es decir, o sea, en otras palabras</td><td style="padding:6px 8px"><em>Es decir, debemos actuar ya</em></td></tr>
<tr><td style="padding:6px 8px">Adición enfática</td><td style="padding:6px 8px">incluso, hasta, ni siquiera</td><td style="padding:6px 8px"><em>Incluso los expertos se equivocaron</em></td></tr>
</table>"""),
        ('Conectores de Argumento y Contraargumento', None, """
<p style="margin:0 0 12px;font-size:.9rem">El discurso formal requiere conectores precisos para organizar el argumento.</p>
<table style="width:100%;border-collapse:collapse;font-size:.83rem">
<tr style="background:var(--amber);color:#000"><th style="padding:6px 8px;text-align:left">Función</th><th style="padding:6px 8px;text-align:left">Conector</th></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Adición</td><td style="padding:6px 8px">además, asimismo, igualmente, del mismo modo</td></tr>
<tr><td style="padding:6px 8px">Contraste</td><td style="padding:6px 8px">sin embargo, no obstante, ahora bien, en cambio</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Consecuencia</td><td style="padding:6px 8px">por lo tanto, por consiguiente, de ahí que + subj</td></tr>
<tr><td style="padding:6px 8px">Concesión</td><td style="padding:6px 8px">si bien, aunque, aun así, a pesar de ello</td></tr>
<tr style="background:var(--paper);color:var(--ink)"><td style="padding:6px 8px">Conclusión</td><td style="padding:6px 8px">en conclusión, en definitiva, en suma, así pues</td></tr>
<tr><td style="padding:6px 8px">Explicación</td><td style="padding:6px 8px">es decir, o sea, esto es, a saber</td></tr>
</table>"""),
    ],
    traps=[
        ('*Debe ser tarde ya.', 'Debe de ser tarde ya.', '<em>Deber de + inf</em> expresa probabilidad/deducción. <em>Deber + inf</em> sin <em>de</em> expresa obligación.'),
        ('*Quizás viene mañana (con certeza hipotética).', 'Quizás venga mañana (hipótesis) / Quizás viene mañana (más seguridad).', '<em>Quizás/tal vez + subjuntivo</em> = hipótesis; + <em>indicativo</em> = más probable. Ambas son aceptadas.'),
        ('*Cabría decir que el texto es muy mal.', 'Cabría decir que el texto adolece de ciertos problemas.', 'En el discurso formal se prefieren expresiones elaboradas. <em>Muy mal</em> resulta demasiado directo y coloquial.'),
        ('*Sin duda, podría ser que llegue tarde.', 'Sin duda llegará tarde. / Podría ser que llegara tarde.', 'No mezcles marcadores de certeza con marcadores de duda en la misma cláusula.'),
        ('*Por lo tanto, no obstante mejoramos.', 'No obstante, seguimos mejorando. / Por lo tanto, debemos mejorar.', '<em>Por lo tanto</em> (consecuencia) y <em>no obstante</em> (contraste) no se combinan en la misma oración.'),
    ],
    summary=[
        ('certeza', 'sin duda, evidentemente, indudablemente + indicativo', '<em>Sin duda es la mejor solución</em>'),
        ('probabilidad alta', 'deber de + inf, seguramente, probablemente', '<em>Debe de tener razón</em>'),
        ('posibilidad', 'quizás/tal vez + subj, puede que + subj', '<em>Puede que venga mañana</em>'),
        ('atenuación', 'en cierta medida, algo, al parecer, quisiera', '<em>Al parecer, dimitirá pronto</em>'),
        ('contraste discursivo', 'sin embargo, no obstante, ahora bien', '<em>Sin embargo, los datos muestran lo contrario</em>'),
        ('consecuencia', 'por lo tanto, por consiguiente, de ahí que + subj', '<em>Por lo tanto, debemos actuar</em>'),
        ('conclusión', 'en definitiva, en conclusión, en suma', '<em>En definitiva, el proyecto es viable</em>'),
    ],
    ex1=dict(
        title='Ejercicio 1: Marcadores de modalidad',
        questions=[
            ('El proyecto ___ tener algún fallo técnico — los resultados son inexplicables.',
             ['debe', 'debe de', 'tiene que', 'puede'], 1,
             '<em>Deber de + inf</em> expresa deducción/probabilidad: <em><u>debe de</u> tener algún fallo.</em>'),
            ('___ sea necesario revisar todo el procedimiento desde el principio.',
             ['Quizás', 'Sin duda', 'Evidentemente', 'Claramente'], 0,
             '<em>Quizás + subj</em> (sea) expresa posibilidad/hipótesis.'),
            ('___, las ventas han crecido un 15% este trimestre.',
             ['Al parecer', 'Sin embargo', 'Por lo tanto', 'A pesar de'], 0,
             '<em>Al parecer</em> = evidencialidad (la información viene de fuera): <em><u>Al parecer</u>, las ventas…</em>'),
            ('El enfoque es correcto; ___, los resultados tardarán en verse.',
             ['sin embargo', 'por lo tanto', 'además', 'es decir'], 0,
             '<em>Sin embargo</em> introduce contraste/matiz: <em><u>Sin embargo</u>, los resultados tardarán.</em>'),
            ('Estudió mucho; ___, aprobó con matrícula de honor.',
             ['sin embargo', 'no obstante', 'por consiguiente', 'al parecer'], 2,
             '<em>Por consiguiente</em> introduce consecuencia lógica: <em><u>por consiguiente</u>, aprobó.</em>'),
            ('___, el texto presenta ciertas carencias metodológicas.',
             ['Hasta cierto punto', 'Sin duda alguna', 'Desde luego', 'Evidentemente'], 0,
             '<em>Hasta cierto punto</em> atenúa la afirmación: <em><u>Hasta cierto punto</u>, el texto presenta carencias.</em>'),
        ]
    ),
    ex2=dict(
        title='Ejercicio 2: Completa con el marcador adecuado',
        questions=[
            ('_______ se ha producido un malentendido: nadie fue informado del cambio.',
             'Al parecer', ['Al parecer', 'Por lo tanto', 'Asimismo'],
             '<em>Al parecer</em> indica que la información procede de una fuente externa.'),
            ('La propuesta es innovadora; _______, requiere una mayor dotación presupuestaria.',
             'sin embargo', ['sin embargo', 'además', 'por consiguiente'],
             '<em>Sin embargo</em> introduce contraste entre ventaja y limitación.'),
            ('La empresa mejoró su eficiencia y, _______, redujo costes en un 20%.',
             'asimismo', ['asimismo', 'sin embargo', 'no obstante'],
             '<em>Asimismo</em> añade información paralela (= también, del mismo modo).'),
            ('_______ llegar a tiempo si salimos ahora.',
             'Podríamos', ['Podríamos', 'Deberíamos', 'Tendremos que'],
             '<em>Podríamos</em> expresa posibilidad con cortesía, atenuando la certeza.'),
            ('El análisis es correcto; _______, no tiene en cuenta las variables externas.',
             'ahora bien', ['ahora bien', 'por lo tanto', 'en definitiva'],
             '<em>Ahora bien</em> introduce una restricción o matiz a lo dicho anteriormente.'),
        ]
    ),
    ex3=dict(
        title='Ejercicio 3: Registro formal y marcadores',
        questions=[
            ('Para expresar probabilidad con deducción lógica, usamos:',
             ['sin duda', 'debe de + inf', 'quizás + subj', 'al parecer'], 1,
             '<em>Deber de + inf</em> = deducción/probabilidad alta basada en evidencia.'),
            ('¿Cuál de estos marcadores es un atenuador?',
             ['indudablemente', 'en cierta medida', 'desde luego', 'sin duda'], 1,
             '<em>En cierta medida</em> atenúa: no afirma totalmente, sino parcialmente.'),
            ('Para introducir una consecuencia lógica, usamos:',
             ['sin embargo', 'no obstante', 'por consiguiente', 'si bien'], 2,
             '<em>Por consiguiente</em> (= por lo tanto) expresa consecuencia.'),
            ('¿Cuál expresa contraste con lo anterior?',
             ['además', 'asimismo', 'no obstante', 'por lo tanto'], 2,
             '<em>No obstante</em> (= sin embargo) introduce contraste o matiz.'),
            ('¿Cuál de estos usos es incorrecto?',
             ['Debe de llover — deducción', 'Debe llover — obligación', 'Debe de llover — obligación', 'Debe salir — obligación'], 2,
             '<em>Debe de + inf</em> es deducción, no obligación. La obligación se expresa con <em>debe + inf</em> sin <em>de</em>.'),
        ]
    ),
    game_desc='Modalidad epistémica, atenuadores e intensificadores del discurso formal',
    items=[
        dict(term='deber de + infinitivo', definition='Expresa probabilidad o deducción del hablante', example='Debe de ser tarde.', accept=['deber de + infinitivo', 'deber de']),
        dict(term='al parecer', definition='Atenuador evidencial: indica que la información viene de fuera', example='Al parecer, dimitirá mañana.', accept=['al parecer']),
        dict(term='sin embargo', definition='Conector de contraste: introduce una idea que limita la anterior', example='Es eficiente; sin embargo, es caro.', accept=['sin embargo']),
        dict(term='en cierta medida', definition='Atenuador cuantificador: la afirmación es parcialmente verdadera', example='En cierta medida, tiene razón.', accept=['en cierta medida']),
        dict(term='por consiguiente', definition='Conector de consecuencia: lo siguiente se deduce de lo anterior', example='Estudió mucho; por consiguiente, aprobó.', accept=['por consiguiente', 'por lo tanto']),
        dict(term='quizás + subjuntivo', definition='Expresa posibilidad o hipótesis (mayor incertidumbre)', example='Quizás venga mañana.', accept=['quizás + subjuntivo', 'tal vez + subjuntivo']),
        dict(term='indudablemente', definition='Intensificador de certeza absoluta', example='Indudablemente, es el mejor candidato.', accept=['indudablemente', 'sin duda alguna']),
        dict(term='en definitiva', definition='Marcador de conclusión: resume o cierra el argumento', example='En definitiva, el proyecto es viable.', accept=['en definitiva', 'en conclusión']),
    ]
)
