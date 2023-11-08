import lib.base_de_datos as base_de_datos


def ultimas_recetas():
    # TODO: Todavia nos falta determinar que recetas son las que vamos a
    # presentar en la pagina de inicio (calculo que las ultimas n agregadas).
    # Luego tendremos que adaptar la query segun sea acorde.

    query = """
        SELECT id, nombre, imagen, descripcion
        FROM receta;
    """

    def registro_a_receta(registro):
        return {
            "id": registro[0],
            "nombre": registro[1],
            "imagen": registro[2],
            "descripcion": registro[3],
        }

    registros = base_de_datos.seleccionar(query)
    recetas = map(registro_a_receta, registros)
    return list(recetas)


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
