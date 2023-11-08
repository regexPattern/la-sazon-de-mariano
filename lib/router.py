from flask import render_template
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

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        return render_template("signup.html")

    @app.route("/signin")
    def signin():
        return render_template("signin.html")

    @app.route("/crear-receta", methods=["GET", "POST"])
    def crear_receta():
        return render_template("crear-receta.html")
