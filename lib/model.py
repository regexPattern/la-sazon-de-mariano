import lib.base_de_datos as base_de_datos


def ultimas_recetas():
    query = """
        SELECT id, nombre, imagen, descripcion
        FROM recetas;
    """

    return base_de_datos.seleccionar(query)


def obtener_receta(id_receta):
    query = """
        SELECT r.nombre nombre, u.id id_usuario, u.nombre nombre_usuario, r.fecha_publicacion, r.imagen, r.descripcion, r.pasos
        FROM recetas AS r
        INNER JOIN usuarios AS u
        ON r.id_usuario = u.id
        WHERE r.id = %s;
    """

    values = (id_receta,)
    filas_recetas = base_de_datos.seleccionar(query, values)

    if len(filas_recetas) == 0:
        raise base_de_datos.RegistroNoEncontrado("Receta no encontrada")

    return filas_recetas[0]


def select_ingredientes_receta(id_receta):
    query = """
        SELECT i.nombre, ir.cantidad
        FROM ingredientes AS i
        INNER JOIN ingredientes_de_receta AS ir
        ON ir.id_ingrediente = i.id AND ir.id_receta = %s;
    """

    values = (id_receta,)

    return base_de_datos.seleccionar(query, values)


def select_usuario(id_usuario):
    query = """
        SELECT id, nombre, imagen
        FROM usuarios
        WHERE id = %s;
    """

    values = (id_usuario,)

    perfiles = base_de_datos.seleccionar(query, values)

    if len(perfiles) == 0:
        raise base_de_datos.RegistroNoEncontrado

    return perfiles[0]


def select_id_usuario(nombre_usuario, password):
    query = """
        SELECT id
        FROM usuarios
        WHERE nombre_usuario = %s AND contrasena = %s;
    """

    values = (nombre_usuario, password)

    ids_usuarios = base_de_datos.seleccionar(query, values)
    return ids_usuarios[0]



def select_usuarios_buscados(nombre_usuario):
    query = """
        SELECT id, nombre
        FROM usuarios
        WHERE SOUNDEX(nombre) = SOUNDEX(%s);
    """

    valores = (nombre_usuario,)

    return base_de_datos.seleccionar(query, valores)


def insert_usuario(datos_usuario):
    query = """
        INSERT INTO usuarios
        (nombre, nombre_usuario, email, contrasenia, imagen)
        VALUES
        (%s, %s, %s, %s, %s);
    """

    valores = (
        datos_usuario["nombre"],
        datos_usuario["nombre-usuario"],
        datos_usuario["email"],
        datos_usuario["contrasenia"],
        datos_usuario["imagen"],
    )

    base_de_datos.ejecutar(query, valores)


def update_usuario(id_usuario, nuevos_datos_usuario):
    query = """
        UPDATE usuarios
        SET nombre = %s
        WHERE id = %s;
    """

    values = (nuevos_datos_usuario["nombre"], id_usuario)

    base_de_datos.ejecutar(query, values)
