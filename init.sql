CREATE TABLE usuario (
	id INT NOT NULL AUTO_INCREMENT,
	nombre TEXT NOT NULL,
	nombre_usuario TEXT NOT NULL UNIQUE,
	email TEXT NOT NULL UNIQUE,
	contrasenia TEXT NOT NULL,
	imagen MEDIUMBLOB NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE receta (
	id INT NOT NULL AUTO_INCREMENT,
	nombre TEXT NOT NULL,
	fecha_publicacion DATE NOT NULL,
	id_usuario INT NOT NULL,
	imagen MEDIUMBLOB NOT NULL,
	descripcion TEXT NOT NULL,
	instrucciones TEXT NOT NULL,
	PRIMARY KEY (id),
	INDEX (id_usuario),
	FOREIGN KEY(id_usuario) REFERENCES usuario(id) ON UPDATE RESTRICT ON DELETE RESTRICT
);

INSERT INTO usuario (
	nombre,
	nombre_usuario,
	email,
	contrasenia,
	imagen
) VALUES (
	"Carlos",
	"carlosecp",
	"carlos@gmail.com",
	"carlos123",
	""
);

INSERT INTO receta (
	nombre,
	fecha_publicacion,
	id_usuario,
	imagen,
	descripcion,
	instrucciones
) VALUES (
	"Arroz caldoso",
	CURDATE(),
	1,
	"",
	"¿Quieres disfrutar de un arroz caldoso casero? Con esta receta podrás deleitarte con este plato tradicional lleno de sabor y textura.",
	"En una olla, calentar un poco de aceite a fuego medio-alto. Agregar el pollo y cocinar hasta que esté dorado por todos lados. Retirar de la olla y reservar.
	En la misma olla, añadir la cebolla, el ajo y el pimiento rojo. Cocinar hasta que estén tiernos. Agregar el tomate y cocinar por unos minutos hasta que se ablande.
	Añadir el arroz y mezclar bien con el sofrito. Verter el caldo de pollo en la olla y llevar a ebullición.
	Reducir el fuego a medio-bajo y cocinar durante 15-20 minutos o hasta que el arroz esté tierno y el caldo haya adquirido una textura caldosa.
	Volver a incorporar el pollo a la olla y cocinar por unos minutos más hasta que esté bien caliente. Sazonar con sal y pimienta al gusto.
	Servir el arroz caldoso con pollo caliente. Añadir un poco de perejil fresco picado por encima."
);

INSERT INTO receta (
	nombre,
	fecha_publicacion,
	id_usuario,
	imagen,
	descripcion,
	instrucciones
) VALUES (
	"Tepache",
	CURDATE(),
	1,
	"",
	"Desde la piña hasta esa burbujeante delicia, te guío paso a paso para preparar un Tepache que sorprenda a todos. ¡Refrescante y natural!",
	"Pelar la piña, cortar la pulpa en trozos y colocarlos en un recipiente grande.
	Agregar el piloncillo, las cáscaras de piña, la canela y los clavos de olor. Cubrir todo con agua y revolver suavemente. 
	Tapar el recipiente con un paño limpio y dejarlo reposar a temperatura ambiente. Dejar fermentar durante 1-2 días, probando ocasionalmente para verificar el sabor.
	Una vez que alcance el nivel deseado de fermentación, colar, dejando unos trozos de piña. Llevar a la heladera y servir bien frío."
);

INSERT INTO receta (
	nombre,
	fecha_publicacion,
	id_usuario,
	imagen,
	descripcion,
	instrucciones
) VALUES (
	"Garbanzos con espinacas",
	CURDATE(),
	1,
	"",
	"Aprende a preparar la auténtica receta sevillana de garbanzos con espinacas en casa. Descubre los secretos de este plato tradicional español!",
	"Remojar los garbanzos durante 8 hrs/ 12 hrs con abundante agua. Pasado ese tiempo escurrir y colocar en una olla con abundante agua hirviendo. Cocinar durante 2 hrs aprox. con pizca de sal. Cocinar hasta que estén blandos (esto dependerá del tipo de garbanzo).
    Pasado el tiempo, colar los garbanzos y guardar 1 taza del caldo. Reservar.
    Por otro lado, picar chiquita la cebolla y el diente de ajo.
    En una sartén amplia poner un chorrito de aceite, el ajo, la cebolla hasta que esté transparente. Agregar el pan previamente tostado y desmenuzado. Dorar 2 min. Agregar las especias mencionadas en la receta, y las espinacas. Saltear 5 min.
    Agregar los garbanzos previamente cocidos, junto con el caldo reservado y la salsa de tomate, revolver y cocinar durante 7 min. Rectificar la sal y pimienta si hace falta.
    Cocinar a fuego medio por 20 minutos más y apagar. Dejar enfriar antes de servir."
);

INSERT INTO receta (
	nombre,
	fecha_publicacion,
	id_usuario,
	imagen,
	descripcion,
	instrucciones
) VALUES (
	"Torrejas de espinaca",
	CURDATE(),
	1,
	"",
	"Receta de Torrejas de Espinaca y al Horno! Riquísimas, sanas y listas en 7 pasos! Todos sus trucos y detalles en esta receta!",
	"En un recipiente colocar la acelga, sal, pimienta, manzana rallada e ir mezclando.
    Agregar la harina y continuar revolviendo todo.
    Por último incorporar el queso azul y las nueces. Mezclar todo y refrigerar en el congelador por 30 minutos.
    Una vez pasado este tiempo, con ayuda de una cuchara agarrar la preparación de a poco e ir formando unas bolitas, corazones, triángulos, la forma que les guste."
);
