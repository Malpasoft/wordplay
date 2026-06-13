# espanol_a1_v1.py — Main Spanish A1 Vocabulary V01–V06
# V01: saludos, V02: numeros, V03: colores, V04: familia, V05: cuerpo-humano, V06: animales
# Format: (word, ipa, def_es, ex_es) — ex_es has the word in <b>

CHAPTERS = {}

CHAPTERS['saludos'] = dict(
    level='a1', num='V01', short='Saludos y Despedidas',
    words=[
        ('hola', 'ˈola', 'expresión de saludo informal', '¡<b>Hola</b>! ¿Cómo estás?'),
        ('buenos días', 'ˈbwenos ˈdias', 'saludo que se usa por la mañana', '<b>Buenos días</b>, señora García.'),
        ('buenas tardes', 'ˈbwenas ˈtardes', 'saludo que se usa por la tarde', '<b>Buenas tardes</b>, ¿en qué le puedo ayudar?'),
        ('buenas noches', 'ˈbwenas ˈnotʃes', 'saludo o despedida que se usa por la noche', '<b>Buenas noches</b>, que descanse.'),
        ('adiós', 'aˈðjos', 'expresión de despedida', '<b>Adiós</b>, nos vemos mañana.'),
        ('hasta luego', 'ˈasta ˈlweɣo', 'despedida informal que indica que nos veremos pronto', '<b>Hasta luego</b>, Juan.'),
        ('¿cómo estás?', 'ˈkomo esˈtas', 'pregunta informal para saber el estado de alguien', '<b>¿Cómo estás?</b> Hace tiempo que no te veo.'),
        ('¿cómo te llamas?', 'ˈkomo te ˈʎamas', 'pregunta para saber el nombre de alguien', '<b>¿Cómo te llamas?</b> —Me llamo Ana.'),
        ('me llamo', 'me ˈʎamo', 'expresión para decir el propio nombre', '<b>Me llamo</b> Carlos, mucho gusto.'),
        ('mucho gusto', 'ˈmutʃo ˈɡusto', 'expresión de cortesía al conocer a alguien por primera vez', '<b>Mucho gusto</b>, encantado de conocerte.'),
        ('por favor', 'por faˈβor', 'expresión de cortesía para hacer una petición', '¿Me pasas el agua, <b>por favor</b>?'),
        ('gracias', 'ˈɡraθjas', 'expresión para agradecer algo', '<b>Gracias</b> por tu ayuda.'),
    ]
)

CHAPTERS['numeros'] = dict(
    level='a1', num='V02', short='Los Números',
    words=[
        ('uno', 'ˈuno', 'número 1, la primera cifra natural', 'Tengo <b>uno</b> hermano pequeño.'),
        ('dos', 'dos', 'número 2, la segunda cifra natural', 'Hay <b>dos</b> manzanas en la mesa.'),
        ('tres', 'tres', 'número 3, la tercera cifra natural', 'Son las <b>tres</b> de la tarde.'),
        ('diez', 'djeθ', 'número 10, el resultado de sumar cinco y cinco', 'El autobús llega en <b>diez</b> minutos.'),
        ('veinte', 'ˈbeinte', 'número 20, el doble de diez', 'Tengo <b>veinte</b> años.'),
        ('treinta', 'ˈtreinta', 'número 30, el triple de diez', 'Hay <b>treinta</b> alumnos en clase.'),
        ('cien', 'θjen', 'número 100, diez veces diez', 'Esto cuesta <b>cien</b> euros.'),
        ('primero', 'priˈmero', 'número ordinal que indica el primer lugar en una serie', 'Soy el <b>primero</b> de la fila.'),
        ('segundo', 'seˈɡundo', 'número ordinal que indica el segundo lugar', 'Vivo en el <b>segundo</b> piso.'),
        ('tercero', 'terˈθero', 'número ordinal que indica el tercer lugar', 'Quedó en el <b>tercero</b> puesto.'),
        ('número', 'ˈnumero', 'símbolo o palabra que representa una cantidad', 'Mi <b>número</b> de teléfono es fácil de recordar.'),
        ('cuántos', 'ˈkwantos', 'pronombre o adjetivo interrogativo para preguntar por una cantidad', '<b>¿Cuántos</b> años tienes?'),
    ]
)

CHAPTERS['colores'] = dict(
    level='a1', num='V03', short='Los Colores',
    words=[
        ('rojo', 'ˈroxo', 'color de la sangre y de los tomates maduros', 'El semáforo está en <b>rojo</b>, no puedes pasar.'),
        ('azul', 'aˈθul', 'color del cielo y del mar', 'Llevo una camisa <b>azul</b> hoy.'),
        ('verde', 'ˈberðe', 'color de las plantas y la hierba', 'Las hojas de los árboles son <b>verdes</b>.'),
        ('amarillo', 'amaˈriʎo', 'color del sol y los limones', 'Compré un bolso <b>amarillo</b> muy bonito.'),
        ('blanco', 'ˈblaŋko', 'color de la nieve y la leche', 'La pared de mi habitación es <b>blanca</b>.'),
        ('negro', 'ˈneɣro', 'color de la oscuridad, opuesto al blanco', 'Lleva un abrigo <b>negro</b> muy elegante.'),
        ('naranja', 'naˈranxa', 'color de la fruta naranja', 'El otoño tiene colores <b>naranja</b> y marrón.'),
        ('rosa', 'ˈrosa', 'color entre el rojo y el blanco, color de las rosas', 'Le regalé flores <b>rosas</b> a mi madre.'),
        ('marrón', 'maˈron', 'color del chocolate y la tierra', 'El perro tiene el pelo <b>marrón</b>.'),
        ('gris', 'ɡris', 'color entre el blanco y el negro', 'El cielo está <b>gris</b> porque va a llover.'),
        ('morado', 'moˈraðo', 'color entre el azul y el rojo, color de las uvas', 'Las uvas son de color <b>morado</b>.'),
        ('de qué color', 'de ke koˈlor', 'expresión para preguntar por el color de algo', '<b>¿De qué color</b> es tu coche? —Es rojo.'),
    ]
)

CHAPTERS['familia'] = dict(
    level='a1', num='V04', short='La Familia',
    words=[
        ('madre', 'ˈmaðre', 'mujer que tiene hijos o ha dado a luz', 'Mi <b>madre</b> cocina muy bien.'),
        ('padre', 'ˈpaðre', 'hombre que tiene hijos', 'Mi <b>padre</b> trabaja en un hospital.'),
        ('hermano', 'erˈmano', 'persona que tiene los mismos padres que otra', 'Mi <b>hermano</b> tiene doce años.'),
        ('hermana', 'erˈmana', 'mujer que tiene los mismos padres que otra', 'Mi <b>hermana</b> estudia medicina.'),
        ('abuelo', 'aˈβwelo', 'padre del padre o de la madre', 'Mi <b>abuelo</b> tiene ochenta años.'),
        ('abuela', 'aˈβwela', 'madre del padre o de la madre', 'Mi <b>abuela</b> me enseña a cocinar.'),
        ('hijo', 'ˈixo', 'persona en relación con sus padres', 'Tengo un <b>hijo</b> de cinco años.'),
        ('hija', 'ˈixa', 'mujer en relación con sus padres', 'Su <b>hija</b> estudia en la universidad.'),
        ('tío', 'ˈtio', 'hermano del padre o de la madre', 'Mi <b>tío</b> vive en Barcelona.'),
        ('tía', 'ˈtia', 'hermana del padre o de la madre', 'Mi <b>tía</b> tiene dos perros.'),
        ('primo', 'ˈprimo', 'hijo del tío o la tía', 'Mi <b>primo</b> y yo jugamos juntos de pequeños.'),
        ('familia', 'faˈmilja', 'grupo de personas unidas por lazos de sangre o matrimonio', 'Mi <b>familia</b> es muy grande y unida.'),
    ]
)

CHAPTERS['cuerpo-humano'] = dict(
    level='a1', num='V05', short='El Cuerpo Humano',
    words=[
        ('cabeza', 'kaˈβeθa', 'parte superior del cuerpo donde están los ojos, la boca y el cerebro', 'Me duele la <b>cabeza</b> desde esta mañana.'),
        ('ojo', 'ˈoxo', 'órgano de la vista', 'Tiene los <b>ojos</b> azules muy bonitos.'),
        ('nariz', 'naˈriθ', 'órgano de la cara para oler y respirar', 'Me sangra la <b>nariz</b>.'),
        ('boca', 'ˈboka', 'apertura de la cara para hablar, comer y beber', 'Habla con la <b>boca</b> llena, eso no está bien.'),
        ('oído', 'oˈiðo', 'órgano para escuchar', 'Tengo el <b>oído</b> derecho tapado.'),
        ('mano', 'ˈmano', 'parte del cuerpo al final del brazo, con cinco dedos', 'Lávate las <b>manos</b> antes de comer.'),
        ('brazo', 'ˈbraθo', 'miembro superior del cuerpo entre el hombro y la mano', 'Me rompí el <b>brazo</b> jugando al fútbol.'),
        ('pierna', 'ˈpjerna', 'miembro inferior del cuerpo entre la cadera y el pie', 'Tengo las <b>piernas</b> cansadas de tanto caminar.'),
        ('pie', 'pje', 'parte final de la pierna sobre la que se apoya el cuerpo', 'Me duele el <b>pie</b> con estos zapatos nuevos.'),
        ('espalda', 'esˈpalda', 'parte posterior del tronco', 'Tengo dolor de <b>espalda</b> por trabajar sentado.'),
        ('estómago', 'esˈtomaɣo', 'órgano del sistema digestivo situado en el abdomen', 'Me duele el <b>estómago</b> después de comer tanto.'),
        ('corazón', 'koraˈθon', 'órgano que bombea la sangre por el cuerpo', 'El médico escuchó mi <b>corazón</b> con el estetoscopio.'),
    ]
)

CHAPTERS['animales'] = dict(
    level='a1', num='V06', short='Los Animales',
    words=[
        ('perro', 'ˈpero', 'animal doméstico fiel que ladra', 'Mi <b>perro</b> se llama Max y le encanta jugar.'),
        ('gato', 'ˈɡato', 'animal doméstico que maúlla y ronronea', 'El <b>gato</b> duerme todo el día en el sofá.'),
        ('pájaro', 'ˈpaxaro', 'animal con plumas y alas que puede volar', 'El <b>pájaro</b> canta todas las mañanas en el jardín.'),
        ('pez', 'peθ', 'animal acuático con escamas que vive en el agua', 'Tengo tres <b>peces</b> en una pecera.'),
        ('caballo', 'kaˈβaʎo', 'animal grande con cuatro patas que sirve para montar', 'El <b>caballo</b> galopa muy rápido por el campo.'),
        ('vaca', 'ˈbaka', 'animal doméstico de granja que da leche', 'La <b>vaca</b> pasta tranquilamente en el prado.'),
        ('cerdo', 'ˈθerðo', 'animal de granja de color rosado', 'El <b>cerdo</b> gruñe en el corral.'),
        ('gallina', 'ɡaˈʎina', 'ave de corral que pone huevos', 'La <b>gallina</b> pone un huevo cada día.'),
        ('conejo', 'koˈnexo', 'animal pequeño con orejas largas', 'El <b>conejo</b> come zanahorias en el jardín.'),
        ('ratón', 'raˈton', 'animal roedor pequeño de color gris o blanco', 'El <b>ratón</b> corrió por el suelo de la cocina.'),
        ('elefante', 'eleˈfante', 'el animal terrestre más grande, con trompa larga', 'El <b>elefante</b> tiene una memoria excelente.'),
        ('león', 'leˈon', 'animal felino grande conocido como el rey de la selva', 'El <b>león</b> ruge con mucha fuerza.'),
    ]
)
