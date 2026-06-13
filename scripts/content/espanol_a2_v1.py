# espanol_a2_v2.py — Main Spanish A2 Vocabulary V01–V06
# V01: tiempo-atmosferico, V02: casa-hogar, V03: transporte, V04: ocio-tiempo-libre
# V05: compras, V06: salud-bienestar

CHAPTERS = {}

CHAPTERS['tiempo-atmosferico'] = dict(
    level='a2', num='V01', short='El Tiempo Atmosférico',
    words=[
        ('sol', 'sol', 'estrella que da luz y calor a la Tierra', 'Hoy brilla el <b>sol</b> y hace mucho calor.'),
        ('lluvia', 'ˈʎuβja', 'agua que cae del cielo en gotas', 'La <b>lluvia</b> riega las plantas del jardín.'),
        ('nieve', 'ˈnjeβe', 'agua helada que cae del cielo en copos blancos', 'Los niños juegan con la <b>nieve</b> en invierno.'),
        ('viento', 'ˈbjento', 'movimiento del aire', 'Hoy hace mucho <b>viento</b> y vuelan los papeles.'),
        ('nube', 'ˈnuβe', 'masa de vapor de agua en el cielo', 'El cielo está cubierto de <b>nubes</b> oscuras.'),
        ('tormenta', 'torˈmenta', 'lluvia fuerte con relámpagos y truenos', 'La <b>tormenta</b> fue muy fuerte anoche.'),
        ('niebla', 'ˈnjeβla', 'masa de vapor de agua muy cerca del suelo que reduce la visibilidad', 'Hay mucha <b>niebla</b> y no se ve bien la carretera.'),
        ('temperatura', 'temperatˈura', 'grado de calor o frío que hace en un lugar', 'La <b>temperatura</b> baja mucho por las noches.'),
        ('calor', 'kaˈlor', 'sensación o estado de alta temperatura', 'No puedo dormir con este <b>calor</b>.'),
        ('frío', 'ˈfrio', 'sensación o estado de baja temperatura', 'Hace mucho <b>frío</b> en invierno en Madrid.'),
        ('paraguas', 'paˈraɣwas', 'utensilio que protege de la lluvia', 'Lleva el <b>paraguas</b>, que hoy va a llover.'),
        ('estación', 'estaˈθjon', 'cada una de las cuatro partes del año: primavera, verano, otoño, invierno', 'La <b>estación</b> favorita de muchos es la primavera.'),
    ]
)

CHAPTERS['casa-hogar'] = dict(
    level='a2', num='V02', short='La Casa y el Hogar',
    words=[
        ('cocina', 'koˈθina', 'habitación de la casa donde se prepara la comida', 'Preparo la comida en la <b>cocina</b>.'),
        ('salón', 'saˈlon', 'habitación principal de la casa para estar y recibir visitas', 'Vemos la tele en el <b>salón</b> por las noches.'),
        ('dormitorio', 'dormiˈtorjo', 'habitación de la casa donde se duerme', 'Mi <b>dormitorio</b> tiene una cama grande.'),
        ('baño', 'ˈbaɲo', 'habitación de la casa con ducha, bañera e inodoro', 'El <b>baño</b> está al final del pasillo.'),
        ('ventana', 'benˈtana', 'apertura en la pared para dar luz y ventilación', 'Abro la <b>ventana</b> cada mañana para ventilar.'),
        ('puerta', 'ˈpwerta', 'elemento que cierra o abre un acceso', 'Cierra la <b>puerta</b> al salir, por favor.'),
        ('mueble', 'ˈmweβle', 'objeto que sirve para equipar y decorar una habitación', 'Los <b>muebles</b> del salón son de madera.'),
        ('silla', 'ˈsiʎa', 'asiento con respaldo para una persona', 'Siéntate en esta <b>silla</b>, por favor.'),
        ('mesa', 'ˈmesa', 'mueble con una superficie plana y patas', 'Comemos todos juntos en la <b>mesa</b>.'),
        ('cama', 'ˈkama', 'mueble donde se duerme', 'Mi <b>cama</b> es muy cómoda y grande.'),
        ('escalera', 'eskaˈlera', 'serie de escalones para subir y bajar entre pisos', 'Subo las <b>escaleras</b> en lugar de coger el ascensor.'),
        ('jardín', 'xarˈðin', 'espacio exterior de una casa con plantas y flores', 'Tenemos un <b>jardín</b> con muchas flores.'),
    ]
)

CHAPTERS['transporte'] = dict(
    level='a2', num='V03', short='El Transporte',
    words=[
        ('autobús', 'awtoˈβus', 'vehículo grande de transporte público que sigue una ruta fija', 'Cojo el <b>autobús</b> para ir al trabajo.'),
        ('metro', 'ˈmetro', 'tren eléctrico que circula bajo tierra por la ciudad', 'El <b>metro</b> es el transporte más rápido en la ciudad.'),
        ('tren', 'tren', 'vehículo de transporte que circula por raíles', 'El <b>tren</b> de alta velocidad llega en dos horas.'),
        ('avión', 'aˈβjon', 'vehículo de transporte aéreo', 'El <b>avión</b> tarda tres horas en llegar.'),
        ('coche', 'ˈkotʃe', 'vehículo de motor de cuatro ruedas para el transporte personal', 'Voy al trabajo en <b>coche</b> todos los días.'),
        ('bicicleta', 'biθiˈkleta', 'vehículo de dos ruedas que se mueve pedaleando', 'Voy al trabajo en <b>bicicleta</b> cuando hace buen tiempo.'),
        ('taxi', 'ˈtaksi', 'coche de alquiler con conductor que lleva pasajeros', 'Llamé a un <b>taxi</b> porque perdí el último metro.'),
        ('barco', 'ˈbarko', 'vehículo que se mueve por el agua', 'Cruzamos el mar en <b>barco</b>.'),
        ('aeropuerto', 'aeroˈpwerto', 'instalación donde despegan y aterrizan los aviones', 'El <b>aeropuerto</b> está a veinte minutos del centro.'),
        ('billete', 'biˈʎete', 'documento que autoriza a viajar en un medio de transporte', 'Compré el <b>billete</b> de tren por internet.'),
        ('parada', 'paˈraða', 'lugar donde se detienen los autobuses o el metro', 'La <b>parada</b> del autobús está al lado de mi casa.'),
        ('maleta', 'maˈleta', 'bolsa rígida con ruedas para llevar ropa al viajar', 'Hice la <b>maleta</b> la noche antes del viaje.'),
    ]
)

CHAPTERS['ocio-tiempo-libre'] = dict(
    level='a2', num='V04', short='Ocio y Tiempo Libre',
    words=[
        ('película', 'peˈlikula', 'obra cinematográfica que se proyecta en el cine o la televisión', 'Vimos una <b>película</b> muy emocionante anoche.'),
        ('música', 'ˈmusika', 'arte de combinar sonidos de manera armoniosa', 'Escucho <b>música</b> mientras hago ejercicio.'),
        ('libro', 'ˈliβro', 'conjunto de hojas impresas que forman una obra', 'Leo un <b>libro</b> antes de dormir cada noche.'),
        ('deporte', 'deˈporte', 'actividad física que se practica siguiendo unas reglas', 'Practico <b>deporte</b> tres veces a la semana.'),
        ('viaje', 'ˈbjaxe', 'desplazamiento a un lugar lejano', 'El próximo verano haré un <b>viaje</b> a Italia.'),
        ('fiesta', 'ˈfjesta', 'celebración en la que se reúnen personas para divertirse', 'Organizamos una <b>fiesta</b> para su cumpleaños.'),
        ('fotografía', 'fotoɣraˈfia', 'imagen captada con una cámara', 'Saco muchas <b>fotografías</b> cuando viajo.'),
        ('juego', 'ˈxweɣo', 'actividad de entretenimiento con reglas definidas', 'Los niños prefieren los <b>juegos</b> al aire libre.'),
        ('teatro', 'teˈatro', 'arte de representar obras dramáticas en un escenario', 'Fuimos al <b>teatro</b> a ver una comedia.'),
        ('concierto', 'konˈθjerto', 'actuación musical en directo ante un público', 'El <b>concierto</b> duró tres horas sin descanso.'),
        ('vacaciones', 'bakaˈθjones', 'período de descanso del trabajo o estudios', 'En <b>vacaciones</b> voy a la playa.'),
        ('hobby', 'ˈxoβi', 'actividad que se hace en el tiempo libre por placer', 'Mi <b>hobby</b> favorito es la fotografía.'),
    ]
)

CHAPTERS['compras'] = dict(
    level='a2', num='V05', short='Las Compras',
    words=[
        ('precio', 'ˈpreθjo', 'cantidad de dinero que cuesta algo', 'El <b>precio</b> de este abrigo es muy alto.'),
        ('dinero', 'diˈnero', 'conjunto de billetes y monedas usados para comprar', 'No tengo suficiente <b>dinero</b> para comprarlo.'),
        ('tarjeta', 'tarˈxeta', 'tarjeta de crédito o débito para pagar', 'Pago con <b>tarjeta</b>, no llevo efectivo.'),
        ('descuento', 'desˈkwento', 'reducción en el precio original de un artículo', 'Hay un <b>descuento</b> del veinte por ciento.'),
        ('talla', 'ˈtaʎa', 'medida de la ropa que corresponde al cuerpo de una persona', '¿Cuál es tu <b>talla</b> de camisa?'),
        ('probador', 'proβaˈðor', 'cabina en una tienda para probarse la ropa', '¿Puedo usar el <b>probador</b> para probarme el vestido?'),
        ('recibo', 'reˈθiβo', 'documento que confirma que se ha realizado un pago', 'Guarda el <b>recibo</b> por si necesitas devolver la compra.'),
        ('oferta', 'oˈferta', 'producto disponible a un precio rebajado', 'Hay una <b>oferta</b> especial en electrónica.'),
        ('caja', 'ˈkaxa', 'lugar en una tienda donde se paga', 'Espera en la cola de la <b>caja</b> para pagar.'),
        ('bolsa', 'ˈbolsa', 'recipiente de papel o plástico para llevar las compras', 'Lleva tu propia <b>bolsa</b> para ayudar al medioambiente.'),
        ('tener', 'teˈner', 'disponer de algo o poseerlo', '¿<b>Tiene</b> este modelo en azul?'),
        ('devolver', 'deβolˈβer', 'retornar un artículo comprado a la tienda', 'Quiero <b>devolver</b> estos zapatos, me aprietan.'),
    ]
)

CHAPTERS['salud-bienestar'] = dict(
    level='a2', num='V06', short='Salud y Bienestar',
    words=[
        ('médico', 'ˈmeðiko', 'profesional de la salud que diagnostica y cura enfermedades', 'Tengo cita con el <b>médico</b> mañana.'),
        ('enfermedad', 'efermeˈðað', 'estado en el que el cuerpo no funciona bien', 'La gripe es una <b>enfermedad</b> vírica.'),
        ('dolor', 'doˈlor', 'sensación física desagradable causada por una lesión o enfermedad', 'Tengo un <b>dolor</b> de espalda muy fuerte.'),
        ('medicina', 'meðiˈθina', 'sustancia que se toma para curar una enfermedad', 'El médico me recetó una <b>medicina</b> para la tos.'),
        ('pastilla', 'pasˈtiʎa', 'comprimido de medicamento que se toma por la boca', 'Toma una <b>pastilla</b> después de cada comida.'),
        ('alergia', 'aˈlerxja', 'reacción exagerada del cuerpo a ciertas sustancias', 'Tengo <b>alergia</b> al polen en primavera.'),
        ('fiebre', 'ˈfjeβre', 'temperatura corporal por encima de lo normal', 'El niño tiene <b>fiebre</b> y hay que llamar al médico.'),
        ('gripe', 'ˈɡripe', 'enfermedad vírica con fiebre, dolor de cabeza y cansancio', 'Estoy en cama con la <b>gripe</b>.'),
        ('herida', 'eˈriða', 'daño o lesión en la piel causada por un golpe o corte', 'Tiene una <b>herida</b> en la rodilla del accidente.'),
        ('vacuna', 'baˈkuna', 'sustancia que se inyecta para proteger contra enfermedades', 'Me puse la <b>vacuna</b> contra la gripe.'),
        ('ejercicio', 'exerˈθiθjo', 'actividad física que se hace para mantenerse en forma', 'Hago <b>ejercicio</b> media hora cada día.'),
        ('descanso', 'desˈkanso', 'período de reposo para recuperar energías', 'El médico me recomendó mucho <b>descanso</b>.'),
    ]
)
