from flask import redirect, render_template, request, session

import lib.model as model
from lib import base_de_datos


def con_pagina_404(route_handler):
    def wrapper(*args, **kwargs):
        try:
            return route_handler(*args, **kwargs)
        except base_de_datos.RegistroNoEncontrado:
            return render_template("404.html")

    return wrapper


@con_pagina_404
def inicio():
    recetas = model.ultimas_recetas()
    return render_template("index.html", recetas=recetas)


def buscar():
    # usuarios = model.obtener_resultados_busqueda_usuario(request.form["query"])
    return ""


@con_pagina_404
def receta(id_receta):
    receta = model.obtener_receta(id_receta)
    ingredientes = model.select_ingredientes_receta(id_receta)
    return render_template("receta.html", receta=receta, ingredientes=ingredientes)


@con_pagina_404
def perfil_get(id_usuario):
    usuario = model.select_usuario(id_usuario)
    return render_template("perfil.html", usuario=usuario)


def perfil_post(id_usuario):
    nuevos_datos_usuario = {
        "nombre": request.form["nombre"],
    }

    model.update_usuario(id_usuario, nuevos_datos_usuario)

    # TODO: Aca deberia retornar el status o algo asi... o lanzar un exception


def signin_post():
    nombre_usuario = request.form["nombre_usuario"]
    password = request.form["password"]

    session["id_usuario"] = model.select_id_usuario(nombre_usuario, password)


def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        usuario = {
            "nombre": request.form["nombre"],
            "nombre-usuario": request.form["nombre-usuario"],
            "email": request.form["email"],
            "contrasenia": request.form["contrasenia"],
            "imagen": request.form["imagen"],
        }

        try:
            model.insert_usuario(usuario)
            return redirect("/signin")
        except:
            # TODO: Realmente no estamos haciendo nada con este mensaje de error en la pantalla.
            params = {"error": "Error al crear el usuario"}
            return render_template("signup.html", params=params)
