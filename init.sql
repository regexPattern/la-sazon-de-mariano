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

INSERT INTO
	usuario (
		nombre,
		nombre_usuario,
		email,
		contrasenia,
		imagen
	)
VALUES
	(
		"Carlos",
		"carlosecp",
		"carlos@gmail.com",
		"carlos123",
		""
	);

INSERT INTO
	receta (
		nombre,
		fecha_publicacion,
		id_usuario,
		imagen,
		descripcion,
		instrucciones
	)
VALUES
	(
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