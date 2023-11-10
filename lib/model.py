from flask import abort

from lib.base_de_datos import sql_ejecutar, sql_seleccionar


def recetas_select_ultimas_agregadas():
    query = """
        SELECT id, nombre, imagen, descripcion
        FROM recetas;
    """

    return sql_seleccionar(query)


def receta_select(id):
    query = """
        SELECT r.nombre nombre, u.id id_usuario, u.nombre nombre_usuario, r.fecha_publicacion, r.imagen, r.descripcion, r.pasos
        FROM recetas AS r
        INNER JOIN usuarios AS u
        ON r.id_usuario = u.id
        WHERE r.id = %s;
    """

    values = (id,)
    filas_recetas = sql_seleccionar(query, values)

    if len(filas_recetas) == 0:
        abort(404)

    return filas_recetas[0]


def receta_select_ingredientes(id):
    query = """
        SELECT i.nombre, ir.cantidad
        FROM ingredientes AS i
        INNER JOIN ingredientes_de_receta AS ir
        ON ir.id_ingrediente = i.id AND ir.id_receta = %s;
    """

    values = (id,)
    return sql_seleccionar(query, values)


def select_usuario(id):
    query = """
        SELECT id, nombre, imagen
        FROM usuarios
        WHERE id = %s;
    """

    values = (id,)
    perfiles = sql_seleccionar(query, values)

    if len(perfiles) == 0:
        abort(404)

    return perfiles[0]


def select_id_usuario_con_credenciales(nombre_usuario, password):
    query = """
        SELECT id
        FROM usuarios
        WHERE nombre_usuario = %s AND contrasena = %s;
    """

    values = (nombre_usuario, password)
    ids_usuarios = sql_seleccionar(query, values)

    if len(ids_usuarios) == 0:
        return None

    return ids_usuarios[0]


def select_usuarios_buscados(nombre_usuario):
    query = """
        SELECT id, nombre
        FROM usuarios
        WHERE SOUNDEX(nombre_usuario) = SOUNDEX(%s);
    """

    valores = (nombre_usuario,)

    return sql_seleccionar(query, valores)


def usuario_insert(datos_usuario):
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

    sql_ejecutar(query, valores)


def usuario_update(id, datos_actualizados_usuario):
    query = """
        UPDATE usuarios
        SET nombre = %s
        WHERE id = %s;
    """

    values = (datos_actualizados_usuario["nombre"], id)

    sql_ejecutar(query, values)
