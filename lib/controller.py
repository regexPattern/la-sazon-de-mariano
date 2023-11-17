from flask import redirect, render_template, request, session

import lib.model as model
from lib.utils import hay_sesion_activa


def inicio():
    recetas = model.select_ultimas_recetas_agregadas()
    return render_template(
        "index.html", recetas=recetas, hay_sesion_activa=hay_sesion_activa()
    )


def buscar():
    recetas = model.select_recetas_buscadas(request.form["busqueda"])
    return render_template("buscar.html", receta=recetas)


def receta(id):
    receta = model.select_receta(id)
    ingredientes = model.select_ingredientes_receta(id)
    return render_template(
        "receta.html",
        receta=receta,
        ingredientes=ingredientes,
        hay_sesion_activa=hay_sesion_activa(),
    )


def usuario(id):
    usuario = model.select_usuario(id)
    recetas_usuario = model.select_recetas_usuario(id)
    return render_template(
        "usuario.html",
        usuario=usuario,
        recetas=recetas_usuario,
        hay_sesion_activa=hay_sesion_activa(),
    )


def usuario_update(id):
    nuevos_datos_usuario = {
        "nombre": request.form["nombre"],
    }

    model.update_usuario(id, nuevos_datos_usuario)


def signin():
    if hay_sesion_activa():
        return redirect("/")
    else:
        return render_template("signin.html")


def signin_crear_cookie():
    nombre_usuario = request.form["nombre_usuario"]
    password = request.form["password"]

    id_usuario = model.select_id_usuario_con_credenciales(nombre_usuario, password)

    if id_usuario is None:
        # TODO: aca deberia mandar algun tipo de mensaje error de vuelta al signin...
        return render_template("signin.html")
    else:
        session["id_usuario"] = id_usuario
        return redirect("/")


def signup_crear_nuevo_usuario():
    datos_nuevo_usuario = {
        "nombre": request.form["nombre"],
        "nombre_usuario": request.form["nombre-usuario"],
        "email": request.form["email"],
        "contrasenia": request.form["contrasenia"],
        "imagen": request.form["imagen"],
    }

    try:
        model.insert_usuario(datos_nuevo_usuario)
        return redirect("/usuario-creado")
    except:
        # TODO: Realmente no estamos haciendo nada con este mensaje de error en la pantalla.
        params = {"error": "Error al crear el usuario"}
        return render_template("signup.html", params=params)
