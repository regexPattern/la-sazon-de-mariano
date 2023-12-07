from flask import abort

from lib._mysql_db import BASE, insertDB, selectDB, updateDB


def select_ultimas_recetas():
    query = """
        SELECT id, nombre, imagen, descripcion
        FROM recetas
        ORDER BY fecha_publicacion ASC;
    """

    return selectDB(BASE, query)


def select_receta(id):
    query = """
        SELECT r.nombre nombre, u.id id_usuario, u.nombre nombre_usuario, r.fecha_publicacion, r.imagen, r.descripcion, r.pasos
        FROM recetas AS r
        INNER JOIN usuarios AS u
        ON r.id_usuario = u.id
        WHERE r.id = %s;
    """

    values = (id,)
    filas_recetas = selectDB(BASE, query, values)

    if filas_recetas is None or len(filas_recetas) == 0:
        abort(404)

    return filas_recetas[0]


def select_ingredientes_receta(id):
    query = """
        SELECT ing.nombre nombre, ing.cantidad cantidad, med.nombre medida
        FROM ingredientes ing
        INNER JOIN medidas med
        ON ing.id_medida = med.id
        WHERE ing.id_receta = %s;
    """

    values = (id,)
    return selectDB(BASE, query, values)


def select_usuario(id):
    query = """
        SELECT id, nombre, imagen
        FROM usuarios
        WHERE id = %s;
    """

    values = (id,)
    perfiles = selectDB(BASE, query, values)

    if perfiles is None or len(perfiles) == 0:
        abort(404)

    return perfiles[0]


def select_recetas_usuario(id):
    query = """
        SELECT id, nombre, imagen
        FROM recetas
        WHERE id_usuario = %s;
    """

    values = (id,)
    return selectDB(BASE, query, values)


def select_id_usuario_con_credenciales(nombre_usuario, password):
    query = """
        SELECT id
        FROM usuarios
        WHERE nombre_usuario = %s AND contrasena = %s;
    """

    values = (nombre_usuario, password)
    ids_usuarios = selectDB(BASE, query, values)

    if ids_usuarios is None or len(ids_usuarios) == 0:
        return None

    return ids_usuarios[0]


def select_recetas_buscadas(busqueda):
    query = """
        SELECT rec.id, rec.nombre, rec.imagen, rec.descripcion
        FROM recetas rec
        INNER JOIN paises pais
        ON rec.id_pais = pais.id
        WHERE rec.nombre LIKE %s OR pais.nombre LIKE %s ;
      """

    valores = ("%" + busqueda + "%", "%" + busqueda + "%")

    return selectDB(BASE, query, valores)


def insert_usuario(datos_usuario):
    query = """
        INSERT INTO usuarios
        (nombre, nombre_usuario, descripcion, email, contrasena)
        VALUES
        (%s, %s, %s, %s, %s);
    """

    valores = (
        datos_usuario["nombre"],
        datos_usuario["nombre_usuario"],
        datos_usuario["descripcion"],
        datos_usuario["email"],
        datos_usuario["contrasenia"],
    )

    insertDB(BASE, query, valores)
    
    return selectDB(BASE, "SELECT MAX(id) id FROM usuarios;")[0]["id"]


def select_medidas():
    query = """
        SELECT id, nombre
        FROM medidas;
    """

    return selectDB(BASE, query)


def select_paises():
    query = """
        SELECT id, nombre, imagen
        FROM paises;
    """

    return selectDB(BASE, query)


def select_categorias():
    query = """
        SELECT id, nombre
        FROM categorias;
    """

    return selectDB(BASE, query)


def insert_ingrediente(datos_ingrediente):
    query = """
        INSERT INTO ingredientes
        (nombre, cantidad, id_receta, id_medida)
        VALUES
        (%s, %s, %s, %s);
    """

    valores = (
        datos_ingrediente["nombre"],
        datos_ingrediente["cantidad"],
        datos_ingrediente["id_receta"],
        datos_ingrediente["id_medida"],
    )

    insertDB(BASE, query, valores)


def insert_receta(datos_receta):
    query = """
        INSERT INTO recetas
        (nombre, descripcion, fecha_publicacion, id_usuario, id_pais, pasos)
        VALUES
        (%s, %s, %s, %s, %s, %s);
    """

    valores = (
        datos_receta["nombre"],
        datos_receta["descripcion"],
        datos_receta["fecha_publicacion"],
        datos_receta["id_usuario"],
        datos_receta["id_pais"],
        datos_receta["pasos"],
    )

    insertDB(BASE, query, valores)

    query = """
        SELECT MAX(id) FROM recetas;
    """

    return selectDB(BASE, query)[0]["MAX(id)"]


def update_usuario(id, datos_actualizados_usuario):
    query = """
        UPDATE usuarios SET nombre = %s, contrasena = %s, email = %s, descripcion = %s WHERE id = %s;
    """

    values = (
        datos_actualizados_usuario["nombre"],
        datos_actualizados_usuario["contrasena"],
        datos_actualizados_usuario["email"],
        datos_actualizados_usuario["descripcion"],
        id,
    )

    updateDB(BASE, query, values)


def select_comentarios(id):
    query = """
        SELECT id_usuario, contenido, usuarios.nombre nombre_usuario
        FROM comentarios
        INNER JOIN usuarios
        ON id_usuario=usuarios.id
        WHERE id_receta = %s;
    """

    values = (id,)
    return selectDB(BASE, query, values)


def publicar_comentario(id_receta, id_usuario, comentario):
    query = """
        INSERT INTO comentarios
        (id_receta, id_usuario, contenido)
        VALUES
        (%s, %s, %s);
    """

    values = (id_receta, id_usuario, comentario)

    insertDB(BASE, query, values)


def update_imagen_receta(nombre_imagen, id_receta):
    query = """
        UPDATE recetas
        SET imagen = %s
        WHERE id = %s;
    """

    values = (nombre_imagen, id_receta)

    updateDB(BASE, query, values)


def update_imagen_usuario(nombre_imagen, id_usuario_insertado):
    query = """
        UPDATE usuarios
        SET imagen = %s
        WHERE id = %s;
    """

    values = (nombre_imagen, id_usuario_insertado)
    print(values)

    updateDB(BASE, query, values)
