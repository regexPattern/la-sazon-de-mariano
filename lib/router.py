from flask import redirect, render_template, request

from . import base_de_datos
from . import controller


def init(app, conexion):
    @app.route("/")
    def inicio():
        recetas = controller.obtener_ultimas_recetas(conexion)
        params = { "recetas": recetas }
        print(params)
        return render_template("index.html")

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        if request.method == "GET":
            return render_template("signup.html")
        else:
            usuario = {
                "nombre": request.form["nombre"],
                "nombre_usuario": request.form["nombre_usuario"],
                "email": request.form["email"],
                "contrasenia": request.form["contrasenia"],
                "imagen": request.form["imagen"],
            }

            try:
                base_de_datos.crear_usuario(conexion, usuario)
                return redirect("/signin")
            except:
                # TODO: Realmente no estamos haciendo nada con este mensaje de error en la pantalla.
                params = { "error": "Error al crear el usuario" }
                return render_template("signup.html", params)

    @app.route("/signin")
    def signin():
        pass
