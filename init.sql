CREATE TABLE
  IF NOT EXISTS usuarios (
    id INT NOT NULL AUTO_INCREMENT,
    nombre TEXT NOT NULL,
    nombre_usuario TEXT UNIQUE NOT NULL,
    email TEXT NOT NULL,
    contrasena TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    imagen TEXT UNIQUE,
    PRIMARY KEY (id)
  );

CREATE TABLE
  IF NOT EXISTS paises (
    id INT NOT NULL AUTO_INCREMENT,
    nombre TEXT UNIQUE NOT NULL,
    imagen TEXT UNIQUE NOT NULL,
    PRIMARY KEY (id)
  );

CREATE TABLE
  IF NOT EXISTS recetas (
    id INT NOT NULL AUTO_INCREMENT,
    nombre TEXT NOT NULL,
    fecha_publicacion DATE NOT NULL,
    id_usuario INT NOT NULL,
    imagen TEXT UNIQUE,
    id_pais INT NOT NULL,
    descripcion TEXT NOT NULL,
    pasos TEXT NOT NULL,
    INDEX (id_usuario),
    INDEX (id_pais),
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_pais) REFERENCES paises (id) ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (id)
  );

CREATE TABLE
  IF NOT EXISTS medidas (
    id INT NOT NULL AUTO_INCREMENT,
    nombre TEXT NOT NULL,
    PRIMARY KEY (id)
  );

CREATE TABLE
  IF NOT EXISTS ingredientes (
    id INT NOT NULL AUTO_INCREMENT,
    nombre TEXT NOT NULL,
	cantidad INT NOT NULL,
    id_receta INT NOT NULL,
    id_medida INT NOT NULL,
    INDEX (id_receta),
    INDEX (id_medida),
    FOREIGN KEY (id_receta) REFERENCES recetas (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_medida) REFERENCES medidas (id) ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (id)
  );

CREATE TABLE
  IF NOT EXISTS categorias (
    id INT NOT NULL AUTO_INCREMENT,
    nombre TEXT NOT NULL,
    PRIMARY KEY (id)
  );

CREATE TABLE
  IF NOT EXISTS categorias_de_receta (
    id INT NOT NULL AUTO_INCREMENT,
    id_receta INT NOT NULL,
    id_categoria INT NOT NULL,
    INDEX (id_receta),
    INDEX (id_categoria),
    FOREIGN KEY (id_receta) REFERENCES recetas (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_categoria) REFERENCES categorias (id) ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (id)
  );

CREATE TABLE
  IF NOT EXISTS comentarios (
    id INT NOT NULL AUTO_INCREMENT,
    id_receta INT NOT NULL,
    id_usuario INT NOT NULL,
    contenido TEXT NOT NULL,
    FOREIGN KEY (id_receta) REFERENCES recetas (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id) ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (id)
  );

INSERT INTO
  usuarios (nombre, nombre_usuario, email, contrasena, descripcion, imagen)
VALUES
  (
    'Carlos',
    'Charles_01',
    'carloscastillo@uca.edu.ar',
    '1234',
    'Me llamo Carlos y soy de Nicaragua. Me fascinan los platillos típicos del caribe.',
    '1.jpeg'
  ),
  (
    'Francisco',
    'Fran_01',
    'franciscohernandez@uca.edu.ar',
    '8765',
    'Soy Francisco de Buenos Aires. Me gustan los platos con carne y los postres típicos de Argentina.',
    '2.jpeg'
  ),
  (
    'Samantha',
    'Sam_01',
    'samanthajohanson@uca.edu.ar',
    'qwe123',
    'Me llamo Samantha y soy de Suecia. Estoy acostumbrada a los sabores eslavos y escandinavos cuando se trata de comida.',
    '3.jpeg'
  ),
  (
    'Virginia',
    'Vir_01',
    'virginiayunesick@uca.edu.ar',
    'zxc456',
    'Soy Virginia de Santiago del Estero. Me gustan las cosas dulces para acompañar el mate.',
    '4.jpeg'
  );

INSERT INTO
  paises (nombre, imagen)
VALUES
  ('Argentina', '1.jpeg'),
  ('China', '2.jpeg'),
  ('España', '3.jpeg'),
  ('Francia', '4.jpeg'),
  ('India', '5.jpeg'),
  ('Italia', '6.jpeg'),
  ('Japón', '7.jpeg'),
  ('México', '8.jpeg'),
  ('Nicaragua', '9.jpeg'),
  ('Suecia', '10.jpeg'),
  ('Inglaterra', '11.jpeg'),
  ('Estados Unidos', '12.jpeg'),
  ('Uzbequistan', '13.jpeg');

INSERT INTO
  recetas (
    nombre,
    fecha_publicacion,
    id_usuario,
    imagen,
    id_pais,
    descripcion,
    pasos
  )
VALUES
  (
    'Arroz caldozo',
    '2023/11/03',
    1,
    'arroz-caldoso.jpeg',
    1,
    '¿Quieres disfrutar de un arroz caldoso casero? Con esta receta podrás deleitarte con este plato tradicional lleno de sabor y textura.',
    'En una olla, calentar un poco de aceite a fuego medio-alto. Agregar el pollo y cocinar hasta que esté dorado por todos lados.
	Retirar de la olla y reservar. En la misma olla, añadir la cebolla, el ajo y el morrón rojo. Cocinar hasta que estén tiernos.
	Agregar el tomate y cocinar por unos minutos hasta que se ablande. Añadir el arroz y mezclar bien con el sofrito.
	Verter el caldo de pollo en la olla y llevar a ebullición. Reducir el fuego a medio-bajo y cocinar durante 15-20 minutos
	o hasta que el arroz esté tierno y el caldo haya adquirido una textura caldosa. Volver a incorporar el pollo a la olla y cocinar por unos minutos más hasta que esté bien caliente.
	Sazonar con sal y pimienta al gusto. Servir el arroz caldoso con pollo caliente. Añadir un poco de perejil fresco picado por encima.'
  ),
  (
    'Pozole verde de pollo',
    '2023/11/16',
    1,
    'pozole-verde-de-pollo.jpeg',
    8,
    'Esta receta de pozole verde de pollo es un giro delicioso al menú clásico mexicano.',
    'En una olla grande, colocar el maíz con suficiente agua para cubrirlo. Llevar a ebullición y reducir el fuego a bajo 30-45 minutos o hasta que esté tierno. Salar a gusto.
    En una olla aparte, colocar las pechugas de pollo, las mitades de cebolla, los dientes de ajo y suficiente agua para cubrir todo. Cocinar a fuego medio hasta que el pollo esté cocido, 20-30 minutos y desmenuzar.
    Asar los chiles verdes en un sartén caliente hasta que la piel se tueste y colocar en una bolsa de plástico sellada unos minutos para que suden. Retirar la piel y las semillas.
    En una licuadora, mezclar los chiles verdes asados, las hojas de cilantro, los dientes de ajo, la cebolla picada, el comino, el orégano seco y sal a gusto hasta obtener una salsa suave y homogénea.
    Calentar un poco de aceite en una sartén grande y agregar la salsa verde. Cocinar a fuego medio durante 5 minutos. Agregar la salsa a la olla con el maíz y cocinar 9-10 minutos a fuego bajo.
    Servir el pozole verde de pollo caliente, acompañado de trozos de pollo desmenuzado, aguacate (palta), cebolla picada, hojas de cilantro y limón según preferencias.'
  ),
  (
    'Natilla',
    '2023/11/09',
    2,
    'natilla.jpeg',
    4,
    'Las natillas caseras tienen ese toque mágico de los postres de antaño.',
    'En una cacerola calentar la leche a fuego medio hasta que esté casi hirviendo. En un bol batir las yemas de huevo con el azúcar hasta que se haga una crema.
    Retirar la cacerola del fuego y agregar despacio la mezcla de yemas revolviendo para evitar que se cocinen demasiado rápido.
    Volver a fuego bajo y continuar revolviendo hasta que la mezcla espese lo suficiente para cubrir la parte posterior de la cuchara, unos 5 a 10 minutos.
    Una vez que las natillas hayan espesado, retirar del fuego y agregar el extracto de vainilla y una pizca de sal mezclando bien.
    Dejar que se enfríen a temperatura ambiente antes de transferir al recipiente. Cubrir con film transparente tocando la superficie para evitar la formación de una película.
    Refrigerar 2 horas antes de servir. Espolvorear un poco de canela en polvo o nuez moscada sobre la parte superior.'
  ),
  (
    'Fresas con chocolate',
    '2023/11/16',
    3,
    'fresas-con-chocolate.jpeg',
    4,
    'Fresas con chocolate, un gesto de cariño en cada bocado. La receta perfecta para sorprender a cualquiera.',
    'Enjuagar las fresas bajo agua fría y secarlas. Es importante que las fresas estén completamente secas antes de sumergirlas en el chocolate para que este se adhiera bien.
    Trocear el chocolate en pequeños trozos. Luego, derretir el chocolate en un recipiente apto para microondas o en un baño maría siempre revolviendo y cuidando que no se queme.
    Insertar un palillo de brocheta o un pincho de madera en la parte superior de cada fresa. Sumergir cada una por completo en el chocolate derretido.
    Colocar las fresas cubiertas de chocolate en una bandeja o plato forrado con papel pergamino y dejar reposar a temperatura ambiente o en el refrigerador hasta que el chocolate esté completamente endurecido.'
  ),
  (
    'Granizado de limon',
    '2023/11/10',
    3,
    'granizado-de-limon.jpeg',
    10,
    '¿Quieres un postre fresco y delicioso? Prueba mi receta de granizado de limón, es como un soplo de brisa fresca en un día de verano.',
    'Rallar la cáscara de la mitad de los limones y exprimir los 4 limones para obtener su jugo.
    En una cacerola, mezclar el azúcar con el agua y la ralladura y hervir unos 3 o 4 minutos. Retirar del fuego y dejar enfriar.
    Verter la mezcla en una bandeja o recipiente apto freezer, incorporar el jugo de limón e integrar todo. Llevar al freezer.
    A la hora, retirar la bandeja o recipiente y raspar con un tenedor para romper los cristales de hielo. Repetir este proceso 30 minutos después, guardar, y repetir nuevamente a los 30 minutos, hasta obtener la textura deseada. Servir el granizado de limón en copas heladas.'
  );

INSERT INTO
  medidas (nombre)
VALUES
  ('kilo'),
  ('litro');

INSERT INTO
  ingredientes (nombre, cantidad, id_receta, id_medida)
VALUES
  ('pechugas de pollo, cortadas en trozos', 1, 1, 1),
  ('cebolla, picada', 1, 1, 1),
  ('dientes de ajo, picados', 2, 1, 1),
  ('pimiento rojo, cortado en trozos', 1, 1, 1),
  ('tomate maduro, picado', 1, 1, 1),
  ('taza de arroz', 1, 1, 1),
  ('tazas de caldo de pollo', 4, 1, 1),
  ('Aceite de oliva, sal y pimienta a gusto', 1, 1, 1),
  ('Un puñado de perejil fresco picado (opcional)', 1, 1, 1),
  ('Algo', 1,2,1),
  ('Algo', 1,3,1),
  ('Algo', 1,4,1),
  ('Algo', 1,5,1);

INSERT INTO
  categorias (nombre)
VALUES
  ('Con lactosa'),
  ('Sin lactosa'),
  ('Con gluten'),
  ('Sin gluten'),
  ('Con TACC'),
  ('Sin TACC'),
  ('Con mani'),
  ('Sin mani'),
  ('Con frutos secos'),
  ('Sin frutos secos'),
  ('Con mariscos'),
  ('Sin mariscos'),
  ('Con huevo'),
  ('Sin huevo'),
  ('Apto celiaco'),
  ('Vegetariano'),
  ('Vegano'),
  ('Pescetariano'),
  ('Carnivoro');

INSERT INTO
  categorias_de_receta (id_receta, id_categoria)
VALUES
  (1, 14),
  (1, 19),
  (2, 6),
  (2, 14),
  (2, 15),
  (2, 19),
  (3, 1),
  (3, 3),
  (3, 8),
  (3, 10),
  (3, 13),
  (4, 4),
  (4, 6),
  (4, 8),
  (4, 10),
  (4, 16),
  (4, 17),
  (5, 2),
  (5, 14),
  (5, 16),
  (5, 17);
