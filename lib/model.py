import lib.base_de_datos as base_de_datos

def _registro_a_receta(registro):
    return {
        "id": registro[0],
        "nombre": registro[1],
        "imagen": registro[2],
        "descripcion": registro[3],
    }


def ultimas_recetas():
    query = """
        SELECT id, nombre, imagen, descripcion
        FROM receta;
    """

    registros = base_de_datos.seleccionar(query)
    recetas = map(_registro_a_receta, registros)
    return list(recetas)


def obtener_receta(codigo):
    query = """
        SELECT id, nombre, imagen, descripcion
        FROM receta
        WHERE receta.id = %s;
    """

    values = (codigo,)

    registros = base_de_datos.seleccionar(query, values)
    receta = next(map(_registro_a_receta, registros))
    return receta


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
