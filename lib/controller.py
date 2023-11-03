from . import base_de_datos


def obtener_ultimas_recetas(conexion):
    query = """
        SELECT id, nombre, imagen, descripcion
        FROM receta;
    """

    return base_de_datos.seleccionar(conexion, query)


def crear_usuario(conexion, usuario):
    query = """
        INSERT INTO usuario
        (nombre, nombre_usuario, email, contrasenia, imagen);
        VALUES
        (%s, %s, %s, %s);
    """

    valores = (
        usuario["nombre"],
        usuario["nombre_usuario"],
        usuario["email"],
        usuario["contrasenia"],
        usuario["imagen"]
    )

    base_de_datos.ejecutar(conexion, query, valores)