import logging
from flask import Flask

from lib import base_de_datos, router


CONFIGURACION_CONEXION = {
    "host": "localhost",
    "user": "user",
    "password": "password",
    "database": "recetario"
}


logging.basicConfig(level=logging.DEBUG)


def main():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config["SECRET_KEY"] = "SOsVMlbxQFy5LsbG0pUmXQ6PxxGHEcoO6BFoSyLXufyRL5TrQ9xfNRc27rjCIH3hAFu3yGaqXG1Kxba0EZfsGsJgUw0Jjbt2Agbc"

    conexion = base_de_datos.crear_conexion(**CONFIGURACION_CONEXION)
    logging.info("Conexión establecida con la base de datos")

    router.init(app, conexion)
    app.run("0.0.0.0", 5000, debug=True)


if __name__ == "__main__":
    main()
