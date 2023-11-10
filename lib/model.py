import lib.base_de_datos as base_de_datos


def ultimas_recetas():
    query = """
        SELECT id, nombre, imagen, descripcion
        FROM recetas;
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


def obtener_receta(codigo):
    query = """
        SELECT r.nombre, u.id, u.nombre, r.fecha_publicacion, r.imagen, r.descripcion, r.instrucciones
        FROM recetas AS r
        INNER JOIN usuarios AS u
        ON r.id_usuario = u.id
        WHERE r.id = %s;
    """

    values = (codigo,)

    def registro_a_receta(registro):
        return {
            "nombre": registro[0],
            "id_usuario": registro[1],
            "nombre_usuario": registro[2],
            "fecha_publicacion": registro[3],
            "imagen": registro[4],
            "descripcion": registro[5],
            "pasos": registro[6],
        }

    registros = base_de_datos.seleccionar(query, values)
    receta = next(map(registro_a_receta, registros))
    return receta


def obtener_ingredientes_de_receta(codigo):
    query = """
        SELECT i.nombre, ir.cantidad
        FROM ingredientes AS i
        INNER JOIN ingredientes_de_receta AS ir
        ON ir.id_ingrediente = i.id AND ir.id_receta = %s;
    """

    values = (codigo,)

    def registro_a_ingrediente(registro):
        return {
            "nombre": registro[0],
            "cantidad": registro[1],
        }

    registros = base_de_datos.seleccionar(query, values)
    ingredientes = map(registro_a_ingrediente, registros)
    return list(ingredientes)


def obtener_resultados_busqueda_usuario(nombre_usuario):
    query = """
        SELECT id, nombre
        FROM usuarios
        WHERE SOUNDEX(nombre) = SOUNDEX(%s);
    """

    valores = (nombre_usuario,)

    return base_de_datos.seleccionar(query, valores)


def crear_usuario(usuario):
    query = """
        INSERT INTO usuarios
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
