from flask import redirect, render_template, request, session

import lib.controller as controller

# TODO: Realmente no me gusta agregar esta indireccion en el router, hace las
# cosas mas dificiles de entender en mi opinion. Habria que ver si prescindimos
# del controller mas bien.


def configurar(app):
    @app.route("/")
    def inicio():
        return controller.inicio()

    @app.route("/buscar")
    def buscar():
        return render_template("buscar.html")

    @app.route("/receta/<codigo>")
    def receta(codigo):
        return controller.receta(codigo)

    @app.route("/perfil/<codigo>", methods=["GET", "POST"])
    def perfil(codigo):
        if session.get("id_usuario") and request.method == "POST":
            controller.perfil_post(codigo)

        return controller.perfil_get(codigo)

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        return render_template("signup.html")

    @app.route("/signin", methods=["GET", "POST"])
    def signin():
        if request.method == "GET":
            return render_template("signin.html")
        else:
            controller.signin_post()
            return redirect("/")

    @app.route("/crear-receta", methods=["GET", "POST"])
    def crear_receta():
        return render_template("crear-receta.html")
