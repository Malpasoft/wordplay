# espanol_a2_v2.py — Main Spanish A2 Vocabulary V07–V12
# V07: trabajo-oficina, V08: escuela-educacion, V09: restaurante-cafeteria
# V10: naturaleza-medioambiente, V11: emociones-sentimientos, V12: tecnologia-internet

CHAPTERS = {}

CHAPTERS['trabajo-oficina'] = dict(
    level='a2', num='V07', short='El Trabajo y la Oficina',
    words=[
        ('jefe', 'ˈxefe', 'persona que dirige a otras en un lugar de trabajo', 'Mi <b>jefe</b> es muy exigente pero justo.'),
        ('reunión', 'rewˈnjon', 'encuentro de varias personas para tratar un asunto', 'Tengo una <b>reunión</b> importante a las diez.'),
        ('correo electrónico', 'koˈreo elektrˈoniko', 'mensaje enviado por internet', 'Envíame un <b>correo electrónico</b> con los datos.'),
        ('ordenador', 'ordennaˈðor', 'máquina electrónica que procesa información', 'Trabajo con el <b>ordenador</b> ocho horas al día.'),
        ('impresora', 'impreˈsora', 'máquina que imprime documentos en papel', 'La <b>impresora</b> está sin tinta, hay que comprar más.'),
        ('contrato', 'konˈtrato', 'documento legal que establece las condiciones de trabajo', 'Firmé el <b>contrato</b> de trabajo ayer.'),
        ('sueldo', 'ˈsueldo', 'dinero que se recibe a cambio del trabajo', 'Mi <b>sueldo</b> aumentó el año pasado.'),
        ('vacaciones', 'bakaˈθjones', 'período oficial de descanso en el trabajo', 'Tengo dos semanas de <b>vacaciones</b> en agosto.'),
        ('horario', 'oˈrarjo', 'distribución del tiempo de trabajo a lo largo del día', 'Mi <b>horario</b> de trabajo es de nueve a cinco.'),
        ('colega', 'koˈleɣa', 'compañero de trabajo', 'Mi <b>colega</b> me ayudó con el informe.'),
        ('despacho', 'desˈpatʃo', 'habitación de trabajo en una oficina', 'Tengo mi propio <b>despacho</b> en la tercera planta.'),
        ('informe', 'inˈforme', 'documento escrito que explica información sobre un tema', 'Tengo que escribir un <b>informe</b> para mañana.'),
    ]
)

CHAPTERS['escuela-educacion'] = dict(
    level='a2', num='V08', short='La Escuela y la Educación',
    words=[
        ('asignatura', 'asiɣnaˈtura', 'materia de estudio en la escuela o universidad', 'Mi <b>asignatura</b> favorita es la matemáticas.'),
        ('examen', 'ekˈsamen', 'prueba para evaluar los conocimientos del estudiante', 'Mañana tengo un <b>examen</b> muy importante.'),
        ('nota', 'ˈnota', 'puntuación que evalúa el rendimiento del estudiante', 'Saqué una buena <b>nota</b> en el examen de español.'),
        ('deberes', 'deˈβeres', 'tareas que el profesor asigna para hacer en casa', 'Tengo muchos <b>deberes</b> para mañana.'),
        ('mochila', 'moˈtʃila', 'bolsa que se lleva a la espalda para los libros', 'Meto los libros en la <b>mochila</b> para ir a clase.'),
        ('diccionario', 'dikθjoˈnarjo', 'libro con el significado y la pronunciación de las palabras', 'Busqué la palabra en el <b>diccionario</b>.'),
        ('pizarra', 'piˈθara', 'superficie oscura en la que el profesor escribe en clase', 'El profesor explicó la lección en la <b>pizarra</b>.'),
        ('cuaderno', 'kwaˈðerno', 'conjunto de hojas en blanco para escribir notas', 'Escribo los apuntes en el <b>cuaderno</b>.'),
        ('bolígrafo', 'boˈliɣrafo', 'instrumento para escribir con tinta', 'Necesito un <b>bolígrafo</b> para firmar.'),
        ('biblioteca', 'biβljoˈteka', 'lugar donde se guardan y se pueden leer o pedir libros', 'Fui a la <b>biblioteca</b> a estudiar para el examen.'),
        ('alumno', 'aˈlumno', 'persona que recibe educación en un centro escolar', 'El <b>alumno</b> hizo una pregunta muy interesante.'),
        ('lección', 'lekˈθjon', 'unidad de enseñanza sobre un tema concreto', 'La <b>lección</b> de hoy trata sobre los verbos irregulares.'),
    ]
)

CHAPTERS['restaurante-cafeteria'] = dict(
    level='a2', num='V09', short='El Restaurante y la Cafetería',
    words=[
        ('mesa', 'ˈmesa', 'mueble donde se sirve y come la comida en un restaurante', '¿Tienen una <b>mesa</b> para dos personas?'),
        ('carta', 'ˈkarta', 'lista de platos y bebidas disponibles en un restaurante', '¿Me trae la <b>carta</b>, por favor?'),
        ('plato', 'ˈplato', 'preparación culinaria que se sirve como parte de una comida', '¿Cuál es el <b>plato</b> del día?'),
        ('primer plato', 'priˈmer ˈplato', 'plato que se sirve al principio de la comida', 'De <b>primer plato</b> tomaré sopa.'),
        ('segundo plato', 'seˈɡundo ˈplato', 'plato principal que se sirve después del primero', 'De <b>segundo plato</b> quiero carne asada.'),
        ('postre', 'ˈpostre', 'alimento dulce que se toma al final de la comida', 'De <b>postre</b> tomaré un flan de vainilla.'),
        ('cuenta', 'ˈkwenta', 'documento con el total a pagar en un restaurante', 'Por favor, ¿nos puede traer la <b>cuenta</b>?'),
        ('propina', 'proˈpina', 'dinero extra que se da al camarero como agradecimiento', 'Dejamos una <b>propina</b> porque el servicio fue excelente.'),
        ('camarero', 'kamaˈrero', 'persona que sirve en un restaurante o bar', 'El <b>camarero</b> fue muy amable y atento.'),
        ('reserva', 'reˈserβa', 'acción de reservar una mesa con antelación', 'Hice una <b>reserva</b> para cenar el sábado.'),
        ('bebida', 'beˈβiða', 'cualquier líquido que se toma para acompañar la comida', '¿Qué <b>bebida</b> desea tomar?'),
        ('menú', 'meˈnu', 'conjunto de platos a precio fijo que incluye varios cursos', 'Pedimos el <b>menú</b> del día, que incluye postre.'),
    ]
)

CHAPTERS['naturaleza-medioambiente'] = dict(
    level='a2', num='V10', short='La Naturaleza y el Medioambiente',
    words=[
        ('árbol', 'ˈarβol', 'planta grande con tronco, ramas y hojas', 'El <b>árbol</b> del jardín da mucha sombra en verano.'),
        ('flor', 'flor', 'parte de la planta de colores vivos y buen olor', 'Las <b>flores</b> del jardín huelen muy bien.'),
        ('río', 'ˈrio', 'corriente de agua natural que fluye hasta el mar', 'El <b>río</b> que pasa por nuestra ciudad es muy largo.'),
        ('mar', 'mar', 'gran masa de agua salada que cubre gran parte de la Tierra', 'Vamos al <b>mar</b> en verano.'),
        ('montaña', 'monˈtaɲa', 'elevación grande del terreno', 'En invierno hay nieve en la <b>montaña</b>.'),
        ('bosque', 'ˈboske', 'zona grande cubierta de árboles', 'Paseamos por el <b>bosque</b> durante el fin de semana.'),
        ('playa', 'ˈplaʝa', 'zona de arena o piedras junto al mar', 'Pasé las vacaciones en la <b>playa</b>.'),
        ('campo', 'ˈkampo', 'zona rural fuera de la ciudad con cultivos o naturaleza', 'Me gusta dar paseos por el <b>campo</b>.'),
        ('contaminación', 'kontaminaˈθjon', 'presencia de sustancias dañinas en el medioambiente', 'La <b>contaminación</b> del aire es un problema grave.'),
        ('reciclaje', 'reθiˈklaxe', 'proceso de transformar residuos para volver a usarlos', 'El <b>reciclaje</b> ayuda a proteger el medioambiente.'),
        ('medio ambiente', 'ˈmedjo amˈbjente', 'conjunto de condiciones naturales que rodean a los seres vivos', 'Debemos proteger el <b>medio ambiente</b>.'),
        ('planta', 'ˈplanta', 'ser vivo con raíces, tallo y hojas', 'Riego mis <b>plantas</b> cada dos días.'),
    ]
)

CHAPTERS['emociones-sentimientos'] = dict(
    level='a2', num='V11', short='Emociones y Sentimientos',
    words=[
        ('feliz', 'feˈliθ', 'que experimenta alegría y satisfacción', 'Estoy muy <b>feliz</b> por las buenas noticias.'),
        ('triste', 'ˈtriste', 'que experimenta tristeza o pena', 'Estoy <b>triste</b> porque mi amigo se va de viaje.'),
        ('enfadado', 'emˈfaðaðo', 'que experimenta enojo o irritación', 'Está <b>enfadado</b> porque llegamos tarde.'),
        ('asustado', 'asusˈtaðo', 'que experimenta miedo', 'El niño estaba <b>asustado</b> por la tormenta.'),
        ('sorprendido', 'sorprenˈdiðo', 'que está inesperadamente afectado por algo', 'Estaba muy <b>sorprendido</b> con el regalo.'),
        ('nervioso', 'nerˈβjoso', 'que experimenta tensión o agitación antes de algo importante', 'Estoy <b>nervioso</b> antes del examen.'),
        ('cansado', 'kanˈsaðo', 'que experimenta fatiga o falta de energía', 'Estoy muy <b>cansado</b> después de trabajar todo el día.'),
        ('aburrido', 'abuˈriðo', 'que no tiene nada interesante que hacer', 'Estoy <b>aburrido</b>, no hay nada que hacer.'),
        ('emocionado', 'emoθjoˈnaðo', 'que experimenta entusiasmo e ilusión', 'Estoy muy <b>emocionado</b> con el viaje.'),
        ('preocupado', 'preoκuˈpaðo', 'que está inquieto por algo', 'Estoy <b>preocupado</b> por los resultados del médico.'),
        ('amor', 'aˈmor', 'sentimiento de afecto intenso hacia otra persona', 'El <b>amor</b> es el sentimiento más poderoso.'),
        ('sentir', 'senˈtir', 'experimentar una emoción o una sensación', '¿Cómo te <b>sientes</b> hoy?'),
    ]
)

CHAPTERS['tecnologia-internet'] = dict(
    level='a2', num='V12', short='Tecnología e Internet',
    words=[
        ('móvil', 'ˈmoβil', 'teléfono portátil sin cable', 'Llama a tu madre por el <b>móvil</b>.'),
        ('internet', 'inˈternet', 'red mundial de ordenadores conectados entre sí', 'Busqué la información en <b>internet</b>.'),
        ('aplicación', 'aplikaˈθjon', 'programa informático para un dispositivo', 'Descargué una <b>aplicación</b> para aprender idiomas.'),
        ('contraseña', 'kontraˈseɲa', 'combinación secreta de letras y números para acceder a algo', 'Cambié mi <b>contraseña</b> por seguridad.'),
        ('red social', 'red soˈθjal', 'plataforma de internet para compartir contenido y comunicarse', 'Subo fotos a mi <b>red social</b> favorita.'),
        ('mensaje', 'menˈsaxe', 'comunicación escrita enviada por teléfono o internet', 'Te mando un <b>mensaje</b> para confirmar la cita.'),
        ('pantalla', 'panˈtaʎa', 'superficie en la que se muestra la imagen de un dispositivo', 'La <b>pantalla</b> de mi móvil está rota.'),
        ('batería', 'bateˈria', 'dispositivo que almacena energía para el móvil u ordenador', 'La <b>batería</b> del móvil está casi agotada.'),
        ('cargador', 'karɣaˈðor', 'dispositivo que recarga la batería de un aparato', '¿Me prestas tu <b>cargador</b>? El mío se ha roto.'),
        ('wifi', 'ˈwifi', 'conexión inalámbrica a internet', '¿Cuál es la contraseña del <b>wifi</b>?'),
        ('vídeo', 'ˈbiðeo', 'grabación de imágenes en movimiento', 'Vi un <b>vídeo</b> muy gracioso en internet.'),
        ('descargar', 'deskarˈɣar', 'transferir datos de internet al dispositivo propio', '¿Puedo <b>descargar</b> esta película?'),
    ]
)
