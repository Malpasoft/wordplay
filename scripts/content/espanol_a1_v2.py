# espanol_a1_v2.py — Main Spanish A1 Vocabulary V07–V12
# V07: comida-bebida, V08: ropa, V09: dias-meses, V10: lugares-ciudad, V11: profesiones, V12: adjetivos

CHAPTERS = {}

CHAPTERS['comida-bebida'] = dict(
    level='a1', num='V07', short='Comida y Bebida',
    words=[
        ('pan', 'pan', 'alimento básico de harina de trigo cocida al horno', 'Compro <b>pan</b> fresco todas las mañanas.'),
        ('agua', 'ˈaɣwa', 'líquido incoloro e inodoro que bebemos para hidratarnos', 'Bebo mucho <b>agua</b> durante el día.'),
        ('leche', 'ˈletʃe', 'líquido blanco que producen los mamíferos', 'El bebé toma <b>leche</b> cada cuatro horas.'),
        ('carne', 'ˈkarne', 'tejido muscular de los animales que se usa como alimento', 'La <b>carne</b> de pollo es muy sana.'),
        ('pescado', 'pesˈkaðo', 'animal marino que se cocina y se come', 'Comemos <b>pescado</b> dos veces a la semana.'),
        ('fruta', 'ˈfruta', 'alimento dulce que producen las plantas', 'La <b>fruta</b> es buena para la salud.'),
        ('verdura', 'berˈðura', 'planta comestible, especialmente sus hojas, tallos y raíces', 'Como <b>verdura</b> en cada comida.'),
        ('arroz', 'aˈroθ', 'cereal en grano que se cuece para comer', 'El <b>arroz</b> con leche es mi postre favorito.'),
        ('huevo', 'ˈweβo', 'producto de la gallina, de forma oval, muy usado en cocina', 'Desayuno dos <b>huevos</b> fritos cada día.'),
        ('café', 'kaˈfe', 'bebida caliente de color oscuro hecha con granos de café', 'Necesito un <b>café</b> para despertarme.'),
        ('zumo', 'ˈθumo', 'líquido que se extrae de las frutas o verduras', 'Bebo un <b>zumo</b> de naranja por las mañanas.'),
        ('queso', 'ˈkeso', 'alimento sólido elaborado con leche cuajada', 'Me encanta el <b>queso</b> manchego.'),
    ]
)

CHAPTERS['ropa'] = dict(
    level='a1', num='V08', short='La Ropa',
    words=[
        ('camisa', 'kaˈmisa', 'prenda de vestir con mangas para la parte superior del cuerpo', 'Lleva una <b>camisa</b> blanca y corbata.'),
        ('pantalón', 'pantaˈlon', 'prenda de vestir que cubre las piernas', 'Necesito un <b>pantalón</b> nuevo para el trabajo.'),
        ('falda', 'ˈfalda', 'prenda de vestir femenina que cubre la parte inferior del cuerpo', 'Lleva una <b>falda</b> larga de color azul.'),
        ('vestido', 'besˈtiðo', 'prenda de vestir femenina de una sola pieza', 'El <b>vestido</b> rojo le queda muy bien.'),
        ('chaqueta', 'tʃaˈketa', 'prenda de vestir con mangas que se pone sobre la ropa', 'Coge la <b>chaqueta</b>, hace frío fuera.'),
        ('abrigo', 'aˈβriɣo', 'prenda de vestir larga y gruesa para el frío', 'En invierno siempre llevo un <b>abrigo</b> de lana.'),
        ('jersey', 'xerˈsei', 'prenda de lana o tejido grueso para el frío', 'Este <b>jersey</b> es muy cómodo y calentito.'),
        ('zapato', 'θaˈpato', 'calzado que cubre el pie', 'Estos <b>zapatos</b> me hacen daño en los pies.'),
        ('calcetín', 'kalθeˈtin', 'prenda de tela que cubre el pie y parte de la pierna', 'Lleva calcetines blancos con las zapatillas.'),
        ('gorra', 'ˈɡora', 'sombrero pequeño con visera', 'Llevo <b>gorra</b> cuando hace mucho sol.'),
        ('bufanda', 'buˈfanda', 'tira de tela que se lleva alrededor del cuello en invierno', 'La <b>bufanda</b> de lana me da mucho calor.'),
        ('ropa', 'ˈropa', 'conjunto de prendas que sirven para cubrir el cuerpo', 'Tengo mucha <b>ropa</b> pero no sé qué ponerme.'),
    ]
)

CHAPTERS['dias-meses'] = dict(
    level='a1', num='V09', short='Días y Meses',
    words=[
        ('lunes', 'ˈlunes', 'primer día de la semana laboral', 'El <b>lunes</b> empieza la semana de trabajo.'),
        ('martes', 'ˈmartes', 'segundo día de la semana', 'Los <b>martes</b> tengo clase de español.'),
        ('miércoles', 'ˈmjerkoles', 'tercer día de la semana', 'El <b>miércoles</b> quedamos para comer.'),
        ('viernes', 'ˈbjernes', 'quinto día de la semana, antes del fin de semana', 'El <b>viernes</b> salimos a celebrar el fin de semana.'),
        ('sábado', 'ˈsaβaðo', 'sexto día de la semana, primer día del fin de semana', 'El <b>sábado</b> voy al mercado por la mañana.'),
        ('domingo', 'doˈmiŋɡo', 'séptimo día de la semana, día de descanso', 'El <b>domingo</b> me quedo en casa y descanso.'),
        ('enero', 'eˈnero', 'primer mes del año', 'En <b>enero</b> hace mucho frío en Madrid.'),
        ('marzo', 'ˈmarθo', 'tercer mes del año, inicio de la primavera', 'En <b>marzo</b> empiezan a florecer los árboles.'),
        ('julio', 'ˈxuljo', 'séptimo mes del año, verano en el hemisferio norte', 'En <b>julio</b> hace mucho calor en España.'),
        ('diciembre', 'diˈθjembre', 'duodécimo y último mes del año', 'En <b>diciembre</b> celebramos la Navidad.'),
        ('semana', 'seˈmana', 'período de siete días', 'Esta <b>semana</b> tengo mucho trabajo.'),
        ('mes', 'mes', 'cada una de las doce partes en que se divide el año', 'El próximo <b>mes</b> voy de vacaciones.'),
    ]
)

CHAPTERS['lugares-ciudad'] = dict(
    level='a1', num='V10', short='La Ciudad',
    words=[
        ('calle', 'ˈkaʎe', 'vía pública de una ciudad por donde circulan personas y vehículos', 'Vivo en la <b>calle</b> Mayor, número quince.'),
        ('plaza', 'ˈplaθa', 'espacio abierto y amplio rodeado de edificios en una ciudad', 'Quedamos en la <b>plaza</b> mayor a las doce.'),
        ('tienda', 'ˈtjenda', 'establecimiento donde se venden productos', 'Esta <b>tienda</b> de ropa tiene precios muy buenos.'),
        ('supermercado', 'supermerˈkaðo', 'gran tienda de alimentación con muchos productos', 'Hago la compra en el <b>supermercado</b> los sábados.'),
        ('banco', 'ˈbaŋko', 'establecimiento financiero donde se guarda y maneja el dinero', 'Voy al <b>banco</b> a sacar dinero.'),
        ('farmacia', 'farˈmaθja', 'establecimiento donde se venden medicamentos', 'Compro las medicinas en la <b>farmacia</b>.'),
        ('hospital', 'ospiˈtal', 'centro médico donde se atiende a los enfermos', 'El <b>hospital</b> está cerca de aquí.'),
        ('escuela', 'esˈkwela', 'centro educativo para niños', 'Los niños van a la <b>escuela</b> a las nueve.'),
        ('restaurante', 'restawˈrante', 'establecimiento donde se sirven comidas', 'Cenamos en un <b>restaurante</b> italiano muy bueno.'),
        ('hotel', 'oˈtel', 'establecimiento donde se paga para pasar la noche', 'El <b>hotel</b> tiene vistas al mar.'),
        ('parque', 'ˈparke', 'espacio público con árboles y plantas para el paseo y el ocio', 'Los niños juegan en el <b>parque</b> por las tardes.'),
        ('estación', 'estaˈθjon', 'lugar donde paran los trenes, autobuses o metros', 'La <b>estación</b> de tren está a cinco minutos.'),
    ]
)

CHAPTERS['profesiones'] = dict(
    level='a1', num='V11', short='Las Profesiones',
    words=[
        ('médico', 'ˈmeðiko', 'persona que estudia medicina y cura enfermedades', 'El <b>médico</b> me ha recetado antibióticos.'),
        ('profesor', 'profeˈsor', 'persona que enseña en una escuela o universidad', 'Mi <b>profesor</b> de español es muy paciente.'),
        ('enfermero', 'eferˈmero', 'persona que cuida a los enfermos en un hospital', 'El <b>enfermero</b> me puso la inyección sin dolor.'),
        ('policía', 'poliˈθia', 'agente que mantiene el orden público', 'El <b>policía</b> nos indicó cómo llegar.'),
        ('bombero', 'bomˈbero', 'persona que apaga incendios y rescata personas', 'Los <b>bomberos</b> llegaron muy rápido al incendio.'),
        ('cocinero', 'koθiˈnero', 'persona que trabaja cocinando en un restaurante', 'El <b>cocinero</b> prepara platos deliciosos.'),
        ('camarero', 'kamaˈrero', 'persona que sirve en un bar o restaurante', 'El <b>camarero</b> nos trajo la cuenta.'),
        ('abogado', 'aβoˈɡaðo', 'persona que estudia leyes y defiende a sus clientes', 'Necesito hablar con un <b>abogado</b>.'),
        ('ingeniero', 'iŋxeˈnjero', 'persona que diseña y construye máquinas y edificios', 'El <b>ingeniero</b> revisó los planos del edificio.'),
        ('periodista', 'perjoˈðista', 'persona que escribe noticias para periódicos o televisión', 'La <b>periodista</b> entrevistó al presidente.'),
        ('arquitecto', 'arkiˈtekto', 'persona que diseña y planifica edificios', 'El <b>arquitecto</b> diseñó una casa moderna.'),
        ('trabajo', 'traˈβaxo', 'actividad que realiza una persona para ganar dinero', 'Mi <b>trabajo</b> empieza a las nueve de la mañana.'),
    ]
)

CHAPTERS['adjetivos-descripcion'] = dict(
    level='a1', num='V12', short='Adjetivos Básicos',
    words=[
        ('grande', 'ˈɡrande', 'que tiene un tamaño mayor de lo normal', 'Vivo en un piso muy <b>grande</b>.'),
        ('pequeño', 'peˈkeɲo', 'que tiene un tamaño menor de lo normal', 'Tengo un perro <b>pequeño</b> y adorable.'),
        ('alto', 'ˈalto', 'que mide más de lo normal de pie a cabeza', 'Mi hermano es muy <b>alto</b>, mide dos metros.'),
        ('bajo', 'ˈbaxo', 'que tiene poca estatura o altura', 'El niño es todavía <b>bajo</b> para su edad.'),
        ('gordo', 'ˈɡorðo', 'que tiene mucho peso o volumen en el cuerpo', 'El gato está muy <b>gordo</b> porque come mucho.'),
        ('delgado', 'delˈɡaðo', 'que tiene poco peso o volumen en el cuerpo', 'Está muy <b>delgada</b> porque hace mucho deporte.'),
        ('joven', 'ˈxoβen', 'que tiene poca edad', 'Es muy <b>joven</b>, solo tiene veinte años.'),
        ('viejo', 'ˈbjexo', 'que tiene mucha edad', 'El edificio es muy <b>viejo</b>, tiene cien años.'),
        ('bonito', 'boˈnito', 'que tiene buen aspecto o causa agrado al verlo', 'Tiene un jardín muy <b>bonito</b> lleno de flores.'),
        ('feo', 'ˈfeo', 'que no tiene buen aspecto o que resulta desagradable de ver', 'El tiempo está muy <b>feo</b> hoy, llueve mucho.'),
        ('bueno', 'ˈbweno', 'que tiene buenas cualidades o que es de calidad', 'Este restaurante tiene una comida muy <b>buena</b>.'),
        ('malo', 'ˈmalo', 'que tiene malas cualidades o que no es de calidad', 'Hoy tengo un día muy <b>malo</b>, todo sale mal.'),
    ]
)
