# espanol_a1_w.py — Main Spanish A1 Writing — 3 chapters (monolingual, all in Spanish)

CHAPTERS = {}

CHAPTERS['mensaje-breve'] = dict(
    level='a1', section='writing', num='W01', short='El Mensaje Breve',
    title='El Mensaje Breve — Notas y SMS',
    subtitle='Aprende a escribir mensajes cortos, notas y SMS en español',
    game_desc='Practica los conceptos clave para escribir mensajes breves en español.',
    slides=[
        ('¿Qué es un mensaje breve?', None,
         '<p class="slide-explanation">Un mensaje breve es un texto corto que comunica una información esencial. Puede ser un SMS, una nota o un mensaje de WhatsApp.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Oye, ¿quedamos a las 5?</b> (SMS informal)</p>'
         '<p style="margin-top:8px"><b>Mamá: he llegado bien. Besos.</b> (nota breve)</p>'
         '<p style="margin-top:8px"><b>¡Feliz cumpleaños! Te llamo luego.</b> (mensaje de WhatsApp)</p></div>'),
        ('Saludos y despedidas', None,
         '<p class="slide-explanation">Los mensajes informales usan saludos y despedidas cortos y afectuosos.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Saludar:</b> Hola · Oye · Buenos días · Buenas</p>'
         '<p style="margin-top:8px"><b>Despedirse:</b> Hasta luego · Besos · Un abrazo · Hasta pronto · Cuídate</p></div>'
         '<p style="margin-top:16px">En mensajes muy informales entre amigos: <b>bss</b> (besos) o simplemente el nombre.</p>'),
        ('El verbo estar para estados', None,
         '<p class="slide-explanation">En mensajes usamos <b>estar</b> para hablar de estados temporales: dónde estamos y cómo nos encontramos.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Estoy en casa.</b> — ubicación</p>'
         '<p style="margin-top:8px"><b>Estoy bien / cansado / ocupado.</b> — estado</p>'
         '<p style="margin-top:8px"><b>Estamos en el metro.</b> — nosotros</p></div>'),
        ('Información esencial', None,
         '<p class="slide-explanation">Un buen mensaje breve responde a: ¿qué?, ¿cuándo?, ¿dónde? — y nada más.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>¿Qué?</b> quedamos / hay partido / llego tarde</p>'
         '<p style="margin-top:8px"><b>¿Cuándo?</b> a las 5 / esta tarde / mañana</p>'
         '<p style="margin-top:8px"><b>¿Dónde?</b> en la puerta / en el bar de siempre / en casa</p></div>'
         '<p style="margin-top:16px">Ejemplo: <b>Oye, llego tarde. Estoy en el metro. ¡Hasta ahora!</b></p>'),
        ('Preguntas cortas', None,
         '<p class="slide-explanation">En los mensajes hacemos preguntas cortas con pronombres interrogativos básicos.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>¿Vienes?</b> / <b>¿Estás en casa?</b> / <b>¿A qué hora quedamos?</b></p>'
         '<p style="margin-top:8px"><b>¿Qué haces?</b> / <b>¿Dónde estás?</b> / <b>¿Cuándo llegas?</b></p></div>'
         '<p style="margin-top:16px">Los signos de apertura <b>¿</b> y <b>¡</b> son obligatorios en español.</p>'),
    ],
    traps=[
        ('Hola, soy bien.', 'Hola, <strong>estoy</strong> bien.', 'Los estados usan estar, no ser'),
        ('¿Cuándo vienes? escribir mañana', 'Escribe con mayúscula: <strong>Mañana</strong> voy.', 'Empieza la frase con mayúscula'),
        ('Hasta luego! (sin apertura)', '<strong>¡</strong>Hasta luego!', 'El signo de exclamación de apertura ¡ es obligatorio en español'),
        ('Estamos de casa.', 'Estamos <strong>en</strong> casa.', 'Ubicación: estar <strong>en</strong> + lugar'),
        ('Cuídate., (coma al final)', 'Cuídate. (sin coma)', 'El punto cierra la frase, la coma no'),
    ],
    summary=[
        ('Saludo', 'Hola / Oye / Buenos días', 'Hola, ¿cómo estás?'),
        ('Estado', 'estar + adjetivo', 'Estoy cansado.'),
        ('Ubicación', 'estar en + lugar', 'Estoy en el trabajo.'),
        ('Info. clave', '¿qué? + ¿cuándo? + ¿dónde?', 'Llego a las 5, en la puerta.'),
        ('Pregunta', '¿Vienes? / ¿Dónde estás?', '¿Quedamos a las 6?'),
        ('Despedida', 'Besos / Un abrazo / Hasta luego', 'Hasta luego. Besos.'),
    ],
    items=[
        ('saludo', 'saludo', 'palabra o frase con que se inicia un mensaje o conversación', 'apertura',
         'El ______ más común en mensajes informales es «Hola».', 'salu', 'saludo'),
        ('despedida', 'despedida', 'frase con la que se cierra un mensaje', 'cierre',
         'Terminé el mensaje con una ______ cariñosa.', 'desped', 'despedida'),
        ('estar', 'estar', 'verbo que expresa estados temporales y ubicaciones', 'encontrarse',
         'Cuando preguntas cómo se siente alguien, usas el verbo ______.', 'est', 'estar'),
        ('ubicacion', 'ubicación', 'lugar donde se encuentra una persona o cosa', 'localización',
         'La ______ se indica con estar + en + lugar.', 'ubic', 'ubicación'),
        ('informal', 'informal', 'registro coloquial propio de la comunicación entre personas de confianza', 'coloquial',
         'Los mensajes entre amigos usan un registro ______.', 'inform', 'informal'),
        ('signo-apertura', '¿ ¡', 'signos de puntuación que abren preguntas y exclamaciones en español', 'apertura',
         'El ______ de interrogación de apertura es obligatorio en español.', 'sig', 'signo'),
        ('nota', 'nota', 'mensaje muy breve escrito para dejar información rápida', 'aviso',
         'Dejé una ______ en la nevera para que supiera que había llegado.', 'not', 'nota'),
        ('sms', 'SMS', 'mensaje de texto corto enviado desde un teléfono móvil', 'mensaje de texto',
         'Envía un ______ si no puedes llamar ahora.', 'SM', 'SMS'),
    ],
    ex1=('Elige la forma correcta', 'Elige la mejor opción para cada hueco.', [
        ('¿Cómo ______ ? Bien, gracias.', ['estás', 'eres', 'tienes'], 'estás',
         'Estado temporal → estar: ¿Cómo estás?'),
        ('Mamá, ______ en casa de Ana.', ['estoy', 'soy', 'hay'], 'estoy',
         'Ubicación → estar: estoy en casa de Ana.'),
        ('______ , María. ¿Quedamos mañana?', ['Hola', 'Hasta luego', 'Besos'], 'Hola',
         'Hola abre el mensaje; hasta luego y besos lo cierran.'),
        ('Llego tarde. ______ en el metro.', ['Estoy', 'Soy', 'Tengo'], 'Estoy',
         'Ubicación temporal → estar: estoy en el metro.'),
        ('Un abrazo, ______  (cierre afectuoso)', ['Ana', 'Hola Ana', '¿Ana?'], 'Ana',
         'El cierre del mensaje termina con el nombre o firma.'),
        ('______ de casa a las 8. (salgo)', ['Salgo', 'Estoy', 'Soy'], 'Salgo',
         'Salgo indica acción en presente; no confundir con estar.'),
    ]),
    ex2=('Completa el mensaje', 'Escribe la palabra que falta. No hacen falta tildes.', [
        ('______ , Pedro. ¿Cómo estás? (saludo informal)', 'Hola',
         'El saludo más común en mensajes informales: Hola.'),
        ('______ en casa. No puedo salir hoy. (ubicación)', 'Estoy',
         'Ubicación → estar: Estoy en casa.'),
        ('Llegamos ______ las 7. (preposición de hora)', 'a',
         'La hora usa la preposición a: a las 7.'),
        ('Hasta ______ , besos. (despedida)', 'luego',
         'Hasta luego es la despedida más habitual.'),
        ('______ mañana a las 5 en el parque? (pregunta de propuesta)', '¿Quedamos',
         'Quedar es el verbo para proponer un encuentro.'),
    ]),
    ex3=('Verdadero o falso', 'Lee las afirmaciones y elige la opción correcta.', [
        ('En español se puede escribir "¿Vienes?" sin el signo de apertura ¿',
         ['Falso: el ¿ de apertura es obligatorio', 'Verdadero: el ¿ es opcional'],
         'Falso: el ¿ de apertura es obligatorio',
         'En español los signos de apertura ¿ y ¡ son obligatorios.'),
        ('Para decir dónde estás usas el verbo SER.',
         ['Falso: se usa ESTAR', 'Verdadero: se usa SER'],
         'Falso: se usa ESTAR',
         'La ubicación siempre usa estar: Estoy en casa, no Soy en casa.'),
        ('«Cuídate» es un saludo de apertura.',
         ['Falso: es una despedida', 'Verdadero: es un saludo'],
         'Falso: es una despedida',
         'Cuídate cierra el mensaje; Hola lo abre.'),
        ('Un mensaje breve debe responder a ¿qué?, ¿cuándo? y ¿dónde?',
         ['Verdadero', 'Falso: solo a ¿qué?'],
         'Verdadero',
         'Un buen mensaje breve contiene la información esencial: qué, cuándo y dónde.'),
        ('El verbo ESTAR se usa para estados temporales.',
         ['Verdadero', 'Falso: ESTAR es solo para ubicaciones'],
         'Verdadero',
         'Estar expresa estados temporales (estoy cansado) y ubicaciones (estoy en casa).'),
    ]),
)

CHAPTERS['formulario'] = dict(
    level='a1', section='writing', num='W02', short='El Formulario',
    title='El Formulario — Rellenar Datos Personales',
    subtitle='Aprende a completar formularios y fichas con información personal básica',
    game_desc='Practica el vocabulario y las estructuras para rellenar formularios en español.',
    slides=[
        ('¿Qué es un formulario?', None,
         '<p class="slide-explanation">Un formulario es un documento con espacios en blanco que hay que rellenar con información personal: nombre, apellidos, dirección, etc.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Nombre:</b> Ana &nbsp; <b>Apellido:</b> García &nbsp; <b>Edad:</b> 25</p>'
         '<p style="margin-top:8px"><b>Nacionalidad:</b> española &nbsp; <b>Teléfono:</b> 612 345 678</p>'
         '<p style="margin-top:8px"><b>Correo electrónico:</b> ana.garcia@email.com</p></div>'),
        ('Datos personales básicos', None,
         '<p class="slide-explanation">Los formularios usan un vocabulario estándar para pedir información.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Nombre</b> — first name &nbsp;|&nbsp; <b>Apellidos</b> — surname(s)</p>'
         '<p style="margin-top:8px"><b>Fecha de nacimiento</b> — date of birth &nbsp;|&nbsp; <b>Lugar de nacimiento</b> — place of birth</p>'
         '<p style="margin-top:8px"><b>Domicilio</b> — home address &nbsp;|&nbsp; <b>Código postal</b> — postcode</p>'
         '<p style="margin-top:8px"><b>DNI / Pasaporte</b> — ID / passport &nbsp;|&nbsp; <b>Estado civil</b> — marital status</p></div>'),
        ('La fecha en español', None,
         '<p class="slide-explanation">En español la fecha se escribe en orden <b>día / mes / año</b>.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>15/03/1998</b> = el quince de marzo de mil novecientos noventa y ocho</p>'
         '<p style="margin-top:8px"><b>1/01/2000</b> = el uno de enero del dos mil</p></div>'
         '<p style="margin-top:16px">Los meses se escriben en <b>minúscula</b>: enero, febrero, marzo...</p>'),
        ('Nacionalidad y profesión', None,
         '<p class="slide-explanation">La nacionalidad y la profesión van en minúscula en español y concuerdan en género.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>español / española</b> &nbsp;|&nbsp; <b>francés / francesa</b></p>'
         '<p style="margin-top:8px"><b>médico / médica</b> &nbsp;|&nbsp; <b>estudiante</b> (igual para ambos géneros)</p>'
         '<p style="margin-top:8px"><b>Soy estudiante.</b> &nbsp;|&nbsp; <b>Soy española.</b></p></div>'),
        ('Números de teléfono y correos', None,
         '<p class="slide-explanation">Los teléfonos españoles tienen 9 cifras. El correo electrónico usa arroba (@) y punto (.).</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Teléfono:</b> 612 345 678 (móvil) &nbsp;|&nbsp; 91 234 56 78 (fijo)</p>'
         '<p style="margin-top:8px"><b>Correo:</b> nombre@dominio.es &nbsp; — arroba = @ &nbsp; punto = .</p></div>'),
    ],
    traps=[
        ('Nombre: García, Ana (orden incorrecto)', 'Nombre: <strong>Ana</strong> &nbsp; Apellido: <strong>García</strong>', 'El nombre va antes que los apellidos en el formulario'),
        ('Fecha: 1998/03/15 (orden americano)', 'Fecha: <strong>15/03/1998</strong> (día/mes/año)', 'En España la fecha sigue el orden día/mes/año'),
        ('Nacionalidad: Española (con mayúscula)', 'Nacionalidad: <strong>española</strong> (minúscula)', 'Nacionalidades y profesiones van en minúscula en español'),
        ('Estado civil: Casada (para un hombre)', 'Estado civil: <strong>Casado</strong>', 'El estado civil concuerda con el género del hablante'),
        ('Domicilio: Calle Mayor 3, 2º A (sin número de piso)', 'Domicilio: Calle Mayor 3, 2º A (bien escrito)', 'El domicilio incluye calle, número y piso cuando corresponde'),
    ],
    summary=[
        ('Nombre / Apellidos', 'nombre propio / apellido(s)', 'Ana García López'),
        ('Fecha de nacimiento', 'día/mes/año', '15/03/1998'),
        ('Nacionalidad', 'minúscula + género', 'español / española'),
        ('Profesión', 'minúscula + género', 'médico / médica'),
        ('Domicilio', 'calle + número + piso', 'Calle Mayor, 5, 3.º B'),
        ('Correo / Teléfono', 'formato estándar', 'ana@email.es / 612 345 678'),
    ],
    items=[
        ('nombre', 'nombre', 'identificación propia de una persona, distinta de los apellidos', 'nombre de pila',
         'En el formulario escribe tu ______ primero y después los apellidos.', 'nom', 'nombre'),
        ('apellido', 'apellido', 'nombre de familia que se transmite de padres a hijos', 'cognomen',
         'En España se suelen tener dos ______: el del padre y el de la madre.', 'apell', 'apellidos'),
        ('domicilio', 'domicilio', 'dirección del lugar donde vive habitualmente una persona', 'dirección',
         'El ______ incluye la calle, el número y el código postal.', 'domic', 'domicilio'),
        ('fecha-nac', 'fecha de nacimiento', 'día, mes y año en que nació una persona', 'nacimiento',
         'La ______ se escribe en orden día/mes/año en España.', 'fecha', 'fecha de nacimiento'),
        ('nacionalidad', 'nacionalidad', 'condición legal de pertenecer a un país como ciudadano', 'ciudadanía',
         'La ______ se escribe en minúscula: española, francesa, mexicana.', 'nacion', 'nacionalidad'),
        ('estado-civil', 'estado civil', 'situación legal de una persona respecto al matrimonio', 'situación familiar',
         'Las opciones del ______ son: soltero/a, casado/a, divorciado/a, viudo/a.', 'estado', 'estado civil'),
        ('codigo-postal', 'código postal', 'número que identifica una zona geográfica para el servicio postal', 'CP',
         'En España el ______ tiene cinco cifras.', 'cod', 'código postal'),
        ('profesion', 'profesión', 'actividad laboral a la que se dedica una persona', 'oficio',
         'La ______ se escribe en minúscula en los formularios.', 'profes', 'profesión'),
    ],
    ex1=('Elige la opción correcta', 'Selecciona la respuesta más adecuada.', [
        ('En un formulario español, la fecha de nacimiento se escribe:', ['15/03/1998', '1998/03/15', '03-15-1998'], '15/03/1998',
         'En España la fecha sigue el orden día/mes/año.'),
        ('La nacionalidad en un formulario se escribe:', ['española', 'Española', 'ESPAÑOLA'], 'española',
         'Las nacionalidades se escriben en minúscula en español.'),
        ('¿Qué significa "Apellidos" en un formulario?', ['El nombre de familia', 'El nombre de pila', 'La dirección'], 'El nombre de familia',
         'Apellidos = surname(s). En España suelen ser dos.'),
        ('El ______ identifica la zona para recibir cartas.', ['código postal', 'domicilio', 'estado civil'], 'código postal',
         'El código postal tiene 5 cifras y identifica la zona postal.'),
        ('¿Cuál de estas profesiones va en minúscula?', ['médico', 'Médico', 'MÉDICO'], 'médico',
         'Las profesiones y nacionalidades se escriben en minúscula.'),
        ('"Estado civil" se refiere a:', ['La situación respecto al matrimonio', 'La dirección', 'El lugar de nacimiento'], 'La situación respecto al matrimonio',
         'Las opciones son: soltero/a, casado/a, divorciado/a, viudo/a.'),
    ]),
    ex2=('Completa el formulario', 'Escribe la palabra que corresponde. No hacen falta tildes.', [
        ('Mi ______ es Miguel y mis apellidos son Torres Ruiz. (nombre de pila)', 'nombre',
         'Nombre = first name, la identificación propia de la persona.'),
        ('Fecha de nacimiento: ______ /07/1995 (el día)', '14',
         'El día va primero: 14/07/1995.'),
        ('Soy de México. Mi ______ es mexicana. (pertenencia a un país)', 'nacionalidad',
         'Nacionalidad = la condición de pertenecer a un país.'),
        ('Mi ______ es Calle Mayor, 7, 2.º A. (donde vivo)', 'domicilio',
         'Domicilio = la dirección de tu vivienda habitual.'),
        ('Soy ______ . Trabajo en un hospital. (profesión médica)', 'medico',
         'Médico/médica, en minúscula, es la profesión sanitaria por excelencia.'),
    ]),
    ex3=('¿Verdadero o falso?', 'Decide si cada afirmación es correcta.', [
        ('En España la fecha se escribe mes/día/año.',
         ['Falso: se escribe día/mes/año', 'Verdadero'],
         'Falso: se escribe día/mes/año',
         'El orden español es día/mes/año, por ejemplo: 15/03/1998.'),
        ('Las nacionalidades se escriben con mayúscula en español.',
         ['Falso: se escriben en minúscula', 'Verdadero'],
         'Falso: se escriben en minúscula',
         'A diferencia del inglés, en español las nacionalidades van en minúscula.'),
        ('El código postal español tiene 5 cifras.',
         ['Verdadero', 'Falso: tiene 4 cifras'],
         'Verdadero',
         'El código postal español siempre tiene 5 cifras.'),
        ('Los apellidos se escriben antes del nombre en los formularios españoles.',
         ['Falso: el nombre va primero', 'Verdadero'],
         'Falso: el nombre va primero',
         'En los formularios se pone Nombre y luego Apellidos.'),
        ('"Domicilio" significa la dirección donde vives.',
         ['Verdadero', 'Falso: significa la profesión'],
         'Verdadero',
         'Domicilio es el lugar de residencia habitual de una persona.'),
    ]),
)

CHAPTERS['presentacion-personal'] = dict(
    level='a1', section='writing', num='W03', short='La Presentación Personal',
    title='La Presentación Personal — Quién soy yo',
    subtitle='Aprende a presentarte por escrito con información básica sobre ti mismo',
    game_desc='Practica las estructuras para presentarte en español.',
    slides=[
        ('¿Qué es una presentación personal?', None,
         '<p class="slide-explanation">Una presentación personal es un texto corto donde explicas quién eres, de dónde eres, cuántos años tienes y qué te gusta.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Me llamo Lucía. Tengo veinte años.</b></p>'
         '<p style="margin-top:8px"><b>Soy española y vivo en Madrid.</b></p>'
         '<p style="margin-top:8px"><b>Me gusta mucho la música y los deportes.</b></p></div>'),
        ('Presentarse: nombre y edad', None,
         '<p class="slide-explanation">Para decir el nombre usas <b>me llamo</b> o <b>mi nombre es</b>. Para la edad, <b>tengo + número + años</b>.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Me llamo Carlos.</b> / <b>Mi nombre es Carlos.</b></p>'
         '<p style="margin-top:8px"><b>Tengo veinticinco años.</b> (NOT: Tengo 25 años de edad)</p></div>'
         '<p style="margin-top:16px">¡Ojo! En español decimos <b>tengo</b> años, no <b>soy</b> años.</p>'),
        ('Origen y residencia', None,
         '<p class="slide-explanation">Para el origen usas <b>soy de</b> + ciudad/país. Para la residencia, <b>vivo en</b> + lugar.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Soy de Argentina.</b> (origen)</p>'
         '<p style="margin-top:8px"><b>Soy argentina.</b> (nacionalidad)</p>'
         '<p style="margin-top:8px"><b>Vivo en Buenos Aires.</b> (residencia)</p></div>'),
        ('Profesión y estudios', None,
         '<p class="slide-explanation">Para hablar de la profesión o los estudios usas el verbo <b>ser</b> o <b>estudiar / trabajar</b>.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Soy estudiante.</b> / <b>Soy profesora.</b></p>'
         '<p style="margin-top:8px"><b>Estudio inglés en la universidad.</b></p>'
         '<p style="margin-top:8px"><b>Trabajo en una empresa de tecnología.</b></p></div>'),
        ('Gustos e intereses', None,
         '<p class="slide-explanation">Para hablar de lo que te gusta usas <b>me gusta</b> + sustantivo singular o infinitivo, y <b>me gustan</b> + sustantivo plural.</p>'
         '<div style="background:var(--paper);padding:16px;margin:20px 0;border-radius:6px">'
         '<p><b>Me gusta la música.</b> (singular)</p>'
         '<p style="margin-top:8px"><b>Me gustan los deportes.</b> (plural)</p>'
         '<p style="margin-top:8px"><b>Me gusta leer y escuchar podcasts.</b> (infinitivo)</p></div>'),
    ],
    traps=[
        ('Tengo veinticinco años de edad.', 'Tengo veinticinco años. (sin «de edad»)', 'No se añade «de edad» en el habla natural'),
        ('Soy veinte años.', 'Tengo veinte años.', 'La edad usa TENER, no SER'),
        ('Me llamo de Carlos.', 'Me llamo Carlos. (sin «de»)', 'Me llamo va directo seguido del nombre, sin preposición'),
        ('Me gusta los deportes.', 'Me gustan los deportes.', 'Con sustantivo plural: me guSTAN'),
        ('Soy de vivo en Madrid.', 'Soy de Sevilla y vivo en Madrid.', 'No mezcles soy de (origen) y vivo en (residencia) en la misma cláusula'),
    ],
    summary=[
        ('Nombre', 'Me llamo / Mi nombre es', 'Me llamo Ana.'),
        ('Edad', 'Tengo + número + años', 'Tengo veinte años.'),
        ('Origen', 'Soy de + ciudad/país', 'Soy de México.'),
        ('Nacionalidad', 'Soy + adj. nac.', 'Soy mexicana.'),
        ('Residencia', 'Vivo en + lugar', 'Vivo en Ciudad de México.'),
        ('Gustos', 'Me gusta(n) + sustantivo/infinitivo', 'Me gusta la música.'),
    ],
    items=[
        ('llamarse', 'llamarse', 'verbo reflexivo que se usa para decir el propio nombre', 'denominarse',
         'Para presentarte usas: «Me ______ Ana».', 'llam', 'llamo'),
        ('tener-anos', 'tener años', 'expresión para indicar la edad de una persona', 'edad',
         'En español la edad se expresa con TENER: «______ veinte años».', 'teng', 'tengo'),
        ('ser-de', 'ser de', 'expresión que indica el lugar de origen de una persona', 'provenir de',
         'Para decir de dónde eres: «______ México».', 'soy', 'soy de'),
        ('vivir-en', 'vivir en', 'expresión que indica el lugar de residencia actual', 'residir en',
         'Para decir dónde vives: «______ Madrid».', 'vivo', 'vivo en'),
        ('me-gusta', 'me gusta / me gustan', 'construcción para expresar gustos con sustantivos o infinitivos', 'gustar',
         'Con sustantivo plural: «______ los deportes» (me gustan).', 'me gust', 'me gustan'),
        ('profesion-ser', 'ser + profesión', 'construcción que expresa la profesión o el rol social de una persona', 'trabajar de',
         'Para decir tu profesión: «______ estudiante».', 'soy', 'soy'),
        ('estudiar', 'estudiar', 'verbo que indica la actividad de adquirir conocimientos en un centro académico', 'cursar',
         '«______ español en la academia» — actividad de aprendizaje.', 'estudi', 'estudio'),
        ('presentacion', 'presentación', 'texto breve en el que alguien se da a conocer con sus datos básicos', 'introducción',
         'Escribe una ______ personal de tres líneas con tu nombre, edad y un gusto.', 'present', 'presentación'),
    ],
    ex1=('Elige la forma correcta', 'Selecciona la opción que completa mejor la frase.', [
        ('______ Marta. (presentar el nombre)', ['Me llamo', 'Soy de', 'Tengo'], 'Me llamo',
         'Para el nombre: me llamo + nombre propio.'),
        ('______ veintidós años. (edad)', ['Tengo', 'Soy', 'Estoy'], 'Tengo',
         'La edad usa tener: tengo veintidós años.'),
        ('______ de Perú pero vivo en España. (origen)', ['Soy', 'Estoy', 'Tengo'], 'Soy',
         'El origen usa ser de: soy de Perú.'),
        ('______ la música y los videojuegos. (gustos, plural)', ['Me gustan', 'Me gusta', 'Me gusto'], 'Me gustan',
         'Con sustantivo plural → me gustan: me gustan los videojuegos.'),
        ('______ estudiante de Medicina. (profesión)', ['Soy', 'Estoy', 'Tengo'], 'Soy',
         'La profesión usa ser: soy estudiante, soy médico.'),
        ('Vivo ______ Barcelona. (residencia)', ['en', 'de', 'a'], 'en',
         'Residencia: vivir en + lugar — vivo en Barcelona.'),
    ]),
    ex2=('Completa la presentación', 'Escribe la palabra que falta.', [
        ('______ llamo Javier. Tengo treinta años. (nombre)', 'Me',
         'Me llamo + nombre: la fórmula estándar para presentarse.'),
        ('Soy ______ Madrid pero ahora vivo en Valencia. (origen)', 'de',
         'Origen: soy de + ciudad/país.'),
        ('______ gusta mucho el cine y la fotografía. (gusto singular)', 'Me',
         'Gusto singular → me gusta: me gusta el cine.'),
        ('Soy ______ en una empresa de informática. (profesión)', 'programador',
         'Soy + profesión en minúscula: soy programador.'),
        ('______ en un piso en el centro de la ciudad. (residencia)', 'Vivo',
         'Residencia: vivo en + lugar.'),
    ]),
    ex3=('¿Correcto o incorrecto?', 'Decide si la frase es correcta o tiene un error.', [
        ('"Soy veinte años." — ¿correcto?',
         ['Incorrecto: Tengo veinte años.', 'Correcto'],
         'Incorrecto: Tengo veinte años.',
         'La edad en español usa TENER, no SER.'),
        ('"Me gustan la música." — ¿correcto?',
         ['Incorrecto: Me gusta la música.', 'Correcto'],
         'Incorrecto: Me gusta la música.',
         'La música es singular → me gusta (no me gustan).'),
        ('"Soy de México y vivo en Madrid." — ¿correcto?',
         ['Correcto', 'Incorrecto'],
         'Correcto',
         'Soy de (origen) y vivo en (residencia) es la distinción correcta.'),
        ('"Me llamo de Ana." — ¿correcto?',
         ['Incorrecto: Me llamo Ana.', 'Correcto'],
         'Incorrecto: Me llamo Ana.',
         'Me llamo va directamente seguido del nombre, sin preposición de.'),
        ('"Soy estudiante." — ¿correcto para hablar de la profesión?',
         ['Correcto', 'Incorrecto: se debe usar ESTAR'],
         'Correcto',
         'Las profesiones usan SER: soy estudiante, soy médico, soy profesora.'),
    ]),
)
