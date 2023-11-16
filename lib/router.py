from flask import redirect, render_template, request

import lib.controller as controller
from lib.utils import hay_sesion_activa


def configurar(app):
    @app.route("/")
    def inicio():
        return controller.inicio()

    @app.route("/buscar")
    def buscar():
        return render_template("buscar.html")

    @app.route("/receta/<id>")
    def receta(id):
        return controller.receta(id)

    @app.route("/receta/crear", methods=["GET", "POST"])
    def receta_crear():
        return render_template("receta-crear.html")

    @app.route("/usuario/<id>", methods=["GET", "PUT"])
    def usuario(id):
        if request.method == "PUT":
            if hay_sesion_activa():
                controller.usuario_update(id)
            else:
                return redirect("/signin")

        return controller.usuario(id)

    @app.route("/signin", methods=["GET", "POST"])
    def signin():
        if request.method == "GET":
            return controller.signin()
        else:
            return controller.signin_crear_cookie()

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        if request.method == "GET":
            if hay_sesion_activa():
                return redirect("/")
            else:
                return render_template("signup.html")
        else:
            return controller.signup_crear_nuevo_usuario()

    @app.route("/usuario-creado")
    def usuario_creado():
        return render_template("usuario-creado.html");

    @app.errorhandler(404)
    def no_encontrado(_):
        return render_template("404.html")
