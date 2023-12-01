CREATE TABLE
  IF NOT EXISTS usuarios (
    id INT NOT NULL AUTO_INCREMENT,
    nombre TEXT NOT NULL,
    nombre_usuario TEXT UNIQUE NOT NULL,
    email TEXT NOT NULL,
    contrasena TEXT NOT NULL,
    imagen TEXT UNIQUE NOT NULL,
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
    imagen TEXT UNIQUE NOT NULL,
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
  usuarios (nombre, nombre_usuario, email, contrasena, imagen)
VALUES
  (
    'Carlos',
    'Charles_01',
    'carloscastillo@uca.edu.ar',
    '1234',
    '1.jpeg'
  ),
  (
    'Francisco',
    'Fran_01',
    'franciscohernandez@uca.edu.ar',
    '8765',
    '2.jpeg'
  ),
  (
    'Samantha',
    'Sam_01',
    'SamanthaJohanson@uca.edu.ar',
    'qwe123',
    '3.jpeg'
  ),
  (
    'Virginia',
    'Vir_01',
    'virginiayunesick@uca.edu.ar',
    'zxc456',
    '4.jpeg'
  );

INSERT INTO
  paises (nombre, imagen)
VALUES
  ('Argentina', '1.jpeg'),
  ('India', '2.jpeg'),
  ('Mexico', '3.jpeg'),
  ('Nicaragua', '4.jpeg'),
  ('Estados Unidos', '5.jpeg'),
  ('Inglaterra', '6.jpeg'),
  ('Francia', '7.jpeg'),
  ('Italia', '8.jpeg'),
  ('España', '9.jpeg'),
  ('Uzbequistan', '10.jpeg'),
  ('Suecia', '11.jpeg'),
  ('Japon', '12.jpeg'),
  ('China', '13.jpeg');

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
  );

INSERT INTO
  medidas (nombre)
VALUES
  ('kilo'),
  ('litro');

INSERT INTO
  ingredientes (nombre, id_receta, id_medida)
VALUES
  ('pechugas de pollo, cortadas en trozos', 1, 1),
  ('1 cebolla, picada', 1, 1),
  ('2 dientes de ajo, picados', 1, 1),
  ('1 pimiento rojo, cortado en trozos', 1, 1),
  ('1 tomate maduro, picado', 1, 1),
  ('1 taza de arroz', 1, 1),
  ('4 tazas de caldo de pollo', 1, 1),
  ('Aceite de oliva, sal y pimienta a gusto', 1, 1),
  (
    'Un puñado de perejil fresco picado (opcional)',
    1,
    1
  );

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
  (1, 19);
