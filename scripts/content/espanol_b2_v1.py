# espanol_b2_v1.py — Main Spanish B2 Vocabulary V01–V06
# Higher register, academic and professional vocabulary

CHAPTERS = {}

CHAPTERS['economia-global'] = dict(
    level='b2', num='V01', short='Economía Global',
    words=[
        ('globalización', 'ɡloβaliθaˈθjon', 'proceso de integración económica, cultural y política entre países del mundo', 'La <b>globalización</b> ha cambiado el modelo económico mundial.'),
        ('mercado', 'merˈkaðo', 'entorno en el que se intercambian bienes y servicios entre compradores y vendedores', 'El <b>mercado</b> laboral exige cada vez más formación.'),
        ('exportación', 'eksportaˈθjon', 'venta de bienes o servicios producidos en un país a otro país', 'Las <b>exportaciones</b> de vino español han crecido este año.'),
        ('importación', 'importaˈθjon', 'compra de bienes o servicios de otro país', 'La <b>importación</b> de petróleo encarece los precios.'),
        ('déficit', 'ˈdefiθit', 'situación en la que los gastos superan a los ingresos', 'El <b>déficit</b> presupuestario obliga a recortar gastos.'),
        ('inversión', 'imberˈsjon', 'acción de destinar dinero a un negocio o activo esperando beneficio', 'La <b>inversión</b> en tecnología es clave para el futuro.'),
        ('inflación', 'inflaˈθjon', 'aumento generalizado y sostenido de los precios', 'La alta <b>inflación</b> reduce el poder adquisitivo.'),
        ('recesión', 'reθeˈsjon', 'período de disminución de la actividad económica', 'La pandemia provocó una grave <b>recesión</b> mundial.'),
        ('desigualdad', 'desiɣwalˈdað', 'falta de igualdad en la distribución de la riqueza o los recursos', 'La <b>desigualdad</b> económica sigue creciendo en muchos países.'),
        ('aranceles', 'aranˈθeles', 'impuestos que gravan las mercancías importadas o exportadas', 'Los <b>aranceles</b> protegen a los productores nacionales.'),
        ('deuda', 'ˈdewða', 'cantidad de dinero que se debe a otra persona o entidad', 'La <b>deuda</b> pública del país ha aumentado considerablemente.'),
        ('PIB', 'piˈiβ', 'valor total de los bienes y servicios producidos en un país en un año (Producto Interior Bruto)', 'El <b>PIB</b> creció un tres por ciento el año pasado.'),
    ]
)

CHAPTERS['politica-internacional'] = dict(
    level='b2', num='V02', short='Política Internacional',
    words=[
        ('diplomacia', 'diploˈmaθja', 'práctica de gestionar las relaciones entre países mediante negociación', 'La <b>diplomacia</b> es preferible al conflicto armado.'),
        ('tratado', 'traˈtaðo', 'acuerdo formal entre dos o más estados', 'El <b>tratado</b> de paz fue firmado por ambos países.'),
        ('soberanía', 'soβeraˈnia', 'poder supremo de un estado para gobernarse a sí mismo', 'El referéndum decidirá sobre la <b>soberanía</b> del territorio.'),
        ('alianza', 'aˈljanθa', 'unión o acuerdo entre personas, partidos o países con un fin común', 'La <b>alianza</b> militar garantiza la defensa colectiva.'),
        ('sanciones', 'sanˈθjones', 'medidas de presión económica o política que un país impone a otro', 'Las <b>sanciones</b> afectaron gravemente su economía.'),
        ('refugiado', 'refuxˈjaðo', 'persona que huye de su país por persecución, guerra o desastre', 'Miles de <b>refugiados</b> cruzaron la frontera en busca de seguridad.'),
        ('migración', 'miɣraˈθjon', 'desplazamiento de personas de un lugar a otro para establecerse', 'La <b>migración</b> es un fenómeno global complejo.'),
        ('conflicto', 'konˈflikto', 'enfrentamiento o desacuerdo, especialmente armado, entre grupos o países', 'El <b>conflicto</b> armado causó miles de víctimas.'),
        ('cumbre', 'ˈkumbre', 'reunión oficial entre jefes de estado o gobierno', 'La <b>cumbre</b> climática reunió a los líderes mundiales.'),
        ('organización internacional', 'orɣaniθaˈθjon internaθjoˈnal', 'institución formada por varios estados para colaborar en un área común', 'La <b>organización internacional</b> coordinó la ayuda humanitaria.'),
        ('veto', 'ˈbeto', 'derecho de un miembro de un organismo internacional a bloquear una decisión', 'El país ejerció su <b>veto</b> en el Consejo de Seguridad.'),
        ('multilateralismo', 'multilateraˈlismo', 'sistema de cooperación entre varios estados para resolver problemas comunes', 'El <b>multilateralismo</b> es clave para abordar el cambio climático.'),
    ]
)

CHAPTERS['ciencia-avanzada'] = dict(
    level='b2', num='V03', short='Ciencia Avanzada',
    words=[
        ('hipótesis', 'iˈpotesis', 'suposición provisional que se formula para ser comprobada mediante experimentos', 'El científico formuló una <b>hipótesis</b> sobre el origen del virus.'),
        ('metodología', 'metoðoloˈxia', 'conjunto de métodos y procedimientos usados en una investigación', 'La <b>metodología</b> del estudio fue muy rigurosa.'),
        ('ensayo clínico', 'enˈsaʝo ˈkliniko', 'estudio controlado que prueba la eficacia de un tratamiento en personas', 'El medicamento superó las fases del <b>ensayo clínico</b>.'),
        ('genoma', 'xeˈnoma', 'conjunto completo de información genética de un organismo', 'La secuenciación del <b>genoma</b> humano fue un hito científico.'),
        ('neurociencia', 'newroˈθjenθja', 'ciencia que estudia el sistema nervioso y el cerebro', 'La <b>neurociencia</b> avanza rápidamente gracias a nuevas tecnologías.'),
        ('inteligencia artificial', 'inteliˈxenθja artiˈθjal', 'campo de la informática que desarrolla sistemas capaces de realizar tareas inteligentes', 'La <b>inteligencia artificial</b> está transformando la medicina.'),
        ('algoritmo', 'alˈɡoritmo', 'conjunto de instrucciones ordenadas para resolver un problema', 'El <b>algoritmo</b> clasifica los resultados por relevancia.'),
        ('nanotecnología', 'nanoteknoloˈxia', 'ciencia que trabaja con materiales a escala atómica', 'La <b>nanotecnología</b> podría revolucionar la medicina del futuro.'),
        ('sostenibilidad', 'sosteniβiliˈdað', 'capacidad de satisfacer las necesidades actuales sin comprometer las futuras generaciones', 'El proyecto apuesta por la <b>sostenibilidad</b> medioambiental.'),
        ('innovación', 'inoβaˈθjon', 'introducción de nuevos productos, procesos o ideas', 'La <b>innovación</b> tecnológica impulsa el crecimiento económico.'),
        ('paradigma', 'paraˈðiɣma', 'modelo o patrón que sirve de referencia en una disciplina', 'El descubrimiento supuso un cambio de <b>paradigma</b> en la física.'),
        ('reproducibilidad', 'reproduθiβiliˈdað', 'capacidad de obtener los mismos resultados repitiendo un experimento', 'La <b>reproducibilidad</b> es fundamental en la investigación científica.'),
    ]
)

CHAPTERS['comunicacion-medios'] = dict(
    level='b2', num='V04', short='Comunicación y Medios',
    words=[
        ('periodismo', 'perjoˈðismo', 'actividad profesional de buscar, verificar y difundir noticias', 'El <b>periodismo</b> de investigación es esencial para la democracia.'),
        ('desinformación', 'desinformaˈθjon', 'difusión deliberada de información falsa para engañar', 'La <b>desinformación</b> se extiende rápidamente por las redes sociales.'),
        ('libertad de prensa', 'liβerˈtað de ˈprensa', 'derecho a publicar información y opiniones sin censura', 'La <b>libertad de prensa</b> es un pilar de la democracia.'),
        ('algoritmo', 'alˈɡoritmo', 'sistema automatizado que selecciona el contenido que el usuario ve', 'El <b>algoritmo</b> determina qué noticias aparecen primero.'),
        ('sesgo', 'ˈsesɣo', 'tendencia o inclinación que distorsiona la objetividad', 'El artículo muestra un claro <b>sesgo</b> político.'),
        ('fuente', 'ˈfwente', 'persona o documento del que se obtiene la información', 'El periodista no reveló la identidad de su <b>fuente</b>.'),
        ('plataforma', 'plaˈtaforma', 'empresa o sistema digital que sirve de intermediario entre usuarios', 'Las grandes <b>plataformas</b> controlan la mayor parte del tráfico de información.'),
        ('viralidad', 'βiraliˈðað', 'capacidad de un contenido para difundirse masiva y rápidamente', 'La <b>viralidad</b> de un vídeo puede generar millones de vistas en horas.'),
        ('influencer', 'iŋˈfluenser', 'persona con gran número de seguidores en redes sociales que influye en sus opiniones', 'El <b>influencer</b> promocionó el producto entre sus seguidores.'),
        ('multimedia', 'mulˈtimeðja', 'que combina varios tipos de medios como texto, imagen, audio y vídeo', 'El reportaje <b>multimedia</b> incluía vídeos y gráficos interactivos.'),
        ('ciberseguridad', 'θiβerseɣuriˈðað', 'conjunto de medidas para proteger los sistemas informáticos de ataques', 'La <b>ciberseguridad</b> es una prioridad para las empresas.'),
        ('privacidad', 'priβaθiˈðað', 'derecho a mantener la información personal fuera del conocimiento público', 'Las grandes tecnológicas amenazan nuestra <b>privacidad</b>.'),
    ]
)

CHAPTERS['literatura-escritura'] = dict(
    level='b2', num='V05', short='Literatura y Escritura',
    words=[
        ('narrador', 'naraˈðor', 'voz que cuenta la historia dentro de una obra literaria', 'El <b>narrador</b> omnisciente conoce los pensamientos de todos los personajes.'),
        ('protagonista', 'protaɣoˈnista', 'personaje principal de una obra literaria o cinematográfica', 'El <b>protagonista</b> de la novela viaja por toda Europa.'),
        ('argumento', 'arɣuˈmento', 'secuencia de los hechos principales que ocurren en una obra', 'El <b>argumento</b> de la novela es muy original.'),
        ('metáfora', 'meˈtafora', 'figura retórica que describe algo comparándolo con otra cosa diferente', '«El tiempo es oro» es una <b>metáfora</b> muy conocida.'),
        ('ironía', 'iˈronia', 'figura retórica que expresa lo contrario de lo que se quiere decir', 'El autor usa la <b>ironía</b> para criticar la sociedad.'),
        ('género literario', 'ˈxenero literˈarjo', 'categoría en que se clasifica una obra literaria según su forma y contenido', 'La novela negra es un <b>género literario</b> muy popular.'),
        ('estilo', 'esˈtilo', 'manera propia de un autor de usar el lenguaje', 'El <b>estilo</b> de García Márquez es inconfundible.'),
        ('ensayo', 'enˈsaʝo', 'texto en prosa que desarrolla una opinión o análisis sobre un tema', 'Escribió un <b>ensayo</b> brillante sobre la identidad nacional.'),
        ('poema', 'poˈema', 'texto literario escrito en verso con recursos rítmicos y expresivos', 'Recitó un <b>poema</b> de Neruda de memoria.'),
        ('trama', 'ˈtrama', 'conjunto de sucesos y conflictos que conforman la historia', 'La <b>trama</b> de la novela tiene muchos giros inesperados.'),
        ('personaje', 'persoˈnaxe', 'ser ficticio que participa en los hechos de una obra narrativa', 'El <b>personaje</b> principal evoluciona mucho a lo largo de la novela.'),
        ('crítica literaria', 'ˈkritika literˈarja', 'análisis y valoración de una obra literaria', 'La <b>crítica literaria</b> recibió la novela con gran entusiasmo.'),
    ]
)

CHAPTERS['filosofia-etica'] = dict(
    level='b2', num='V06', short='Filosofía y Ética',
    words=[
        ('ética', 'ˈetika', 'rama de la filosofía que estudia los principios morales del comportamiento humano', 'La <b>ética</b> médica exige respetar la autonomía del paciente.'),
        ('moral', 'moˈral', 'conjunto de normas y valores que distinguen el bien del mal en una sociedad', 'La <b>moral</b> de cada sociedad varía según su cultura e historia.'),
        ('dilema', 'diˈlema', 'situación en la que es difícil elegir entre dos opciones igualmente válidas o problemáticas', 'El médico se enfrentó a un <b>dilema</b> ético difícil.'),
        ('justicia', 'xusˈtiθja', 'principio moral que implica dar a cada uno lo que merece', 'La <b>justicia</b> social exige igualdad de oportunidades.'),
        ('libertad', 'liβerˈtað', 'capacidad de actuar según la propia voluntad sin restricciones', 'La <b>libertad</b> de expresión es un derecho fundamental.'),
        ('derechos humanos', 'deˈretʃos uˈmanos', 'derechos básicos e inalienables que corresponden a toda persona', 'La organización defiende los <b>derechos humanos</b> en todo el mundo.'),
        ('igualdad', 'iɣwalˈdað', 'principio de que todas las personas tienen el mismo valor y los mismos derechos', 'La <b>igualdad</b> de género sigue siendo una lucha pendiente.'),
        ('relativismo', 'relatiˈβismo', 'doctrina que sostiene que la verdad o los valores morales dependen del contexto', 'El <b>relativismo</b> moral dificulta el consenso sobre valores universales.'),
        ('utilitarismo', 'utilitaˈrismo', 'doctrina ética que considera bueno lo que produce el mayor bienestar para el mayor número', 'El <b>utilitarismo</b> justifica una acción por sus consecuencias.'),
        ('argumento', 'arɣuˈmento', 'razonamiento que se usa para demostrar o refutar una proposición', 'Su <b>argumento</b> filosófico era brillante pero difícil de rebatir.'),
        ('paradoja', 'paraˈðoxa', 'afirmación que parece contradictoria pero puede ser verdad', 'La <b>paradoja</b> del mentiroso es un clásico de la lógica.'),
        ('consenso', 'konˈsenso', 'acuerdo al que llegan la mayoría de los miembros de un grupo', 'El debate terminó con un <b>consenso</b> sobre los principios básicos.'),
    ]
)
