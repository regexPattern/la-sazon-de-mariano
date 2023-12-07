from flask import redirect, render_template, request, session

import lib.controller as controller
import lib.model as model
from lib.utils import hay_sesion_activa


def configurar(app):
    @app.route("/")
    def inicio():
        return controller.inicio()

    @app.route("/buscar", methods=["POST"])
    def buscar():
        return controller.buscar()

    @app.route("/receta/<id>", methods=["GET", "POST"])
    def receta(id):
        if request.method == "GET":
            return controller.receta(id)
        else:
            if hay_sesion_activa():
                return controller.comentar_receta(id, hay_sesion_activa()["id"])
            else:
                return redirect("/signin")

    @app.route("/receta/crear", methods=["GET", "POST"])
    def receta_crear():
        if not hay_sesion_activa():
            return redirect("/signin")

        if request.method == "POST":
            return controller.crear_nueva_receta(app)
        else:
            return controller.get_crear_nueva_receta()

    @app.route("/usuario/<id>", methods=["GET", "POST"])
    def usuario(id):
        if request.method == "POST":
            if hay_sesion_activa()['id'] == 1:
                return controller.usuario_delete(id)
            else:
                return redirect("/")
        else:
            return controller.usuario(id)

    @app.route("/usuario/<id>/update", methods=["GET", "POST"])
    def usuario_update(id):
        if request.method == "POST":
            if hay_sesion_activa():
                return controller.usuario_update(id)
            else:
                return redirect("/signin")
        else:
            usuario = model.select_usuario(id)
            return render_template("update.html", usuario=usuario)

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

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect("/signin")

    @app.route("/usuario-creado")
    def usuario_creado():
        return render_template("usuario-creado.html")

    @app.errorhandler(404)
    def no_encontrado(_):
        return render_template("404.html")
