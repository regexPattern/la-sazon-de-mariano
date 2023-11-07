import lib.base_de_datos as base_de_datos


def obtener_ultimas_recetas():
    query = """
        SELECT id, nombre, imagen, descripcion
        FROM receta;
    """

    return base_de_datos.seleccionar(query)


def obtener_resultados_busqueda_usuario(nombre_usuario):
    query = """
        SELECT id, nombre
        FROM usuario
        WHERE SOUNDEX(usuario.nombre) = SOUNDEX(%s);
    """

    valores = (nombre_usuario,)

    return base_de_datos.seleccionar(query, valores)


def crear_usuario(usuario):
    query = """
        INSERT INTO usuario
        (nombre, nombre_usuario, email, contrasenia, imagen)
        VALUES
        (%s, %s, %s, %s, %s);
    """

    valores = (
        usuario["nombre"],
        usuario["nombre-usuario"],
        usuario["email"],
        usuario["contrasenia"],
        usuario["imagen"],
    )

    base_de_datos.ejecutar(query, valores)
