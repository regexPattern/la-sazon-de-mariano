import base64
import os
from datetime import datetime

from flask import app, redirect, render_template, request, session

import lib.model as model
from lib.utils import hay_sesion_activa


def inicio():
    recetas = model.select_ultimas_recetas()
    paises = model.select_paises()
    return render_template(
        "index.html",
        recetas=recetas,
        paises=paises,
        hay_sesion_activa=hay_sesion_activa(),
    )


def buscar():
    recetas = model.select_recetas_buscadas(request.form["busqueda"])
    return render_template("buscar.html", recetas=recetas)


def receta(id):
    receta = model.select_receta(id)
    ingredientes = model.select_ingredientes_receta(id)
    comentarios = model.select_comentarios(id)
    return render_template(
        "receta.html",
        receta=receta,
        ingredientes=ingredientes,
        comentarios=comentarios,
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
        "contrasena": request.form["contrasena"],
        "email": request.form["email"],
        "descripcion": request.form["descripcion"],
    }

    try:
        model.update_usuario(id, nuevos_datos_usuario)
    finally:
        return redirect(f"/usuario/{id}")


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
        "nombre_usuario": request.form["nombre_usuario"],
        "descripcion": request.form["descripcion"],
        "email": request.form["email"],
        "contrasenia": request.form["contrasenia"],
    }

    try:
        id_usuario_insertado = model.insert_usuario(datos_nuevo_usuario)
        imagen = request.files["imagen"]
        extension = imagen.filename.split(".")[-1]
        nombre_archivo_imagen = str(id_usuario_insertado) + "." + extension
        model.update_imagen_usuario(nombre_archivo_imagen, id_usuario_insertado)
        return redirect("/usuario-creado")
    except:
        params = {"error": "Error al crear el usuario"}
        return render_template("signup.html", params=params)


def get_crear_nueva_receta():
    medidas = model.select_medidas()
    paises = model.select_paises()
    categorias = model.select_categorias()
    return render_template(
        "receta-crear.html", medidas=medidas, paises=paises, categorias=categorias, hay_sesion_activa=hay_sesion_activa()
    )


def crear_nueva_receta(app):
    receta_nueva = {
        "nombre": request.form["nombre"],
        "descripcion": request.form["pasos"],
        "fecha_publicacion": datetime.now().strftime("%Y-%m-%d"),
        "id_usuario": hay_sesion_activa()["id"],
        "id_pais": int(request.form["id_pais"]),
        "pasos": request.form["pasos"],
    }

    id_receta_insertada = model.insert_receta(receta_nueva)

    imagen = request.files["imagen"]
    extension = imagen.filename.split(".")[-1]
    nombre_archivo_imagen = str(id_receta_insertada) + "." + extension
    imagen.save(os.path.join(app.config["UPLOAD_FOLDER"], "recetas", nombre_archivo_imagen))

    model.update_imagen_receta(nombre_archivo_imagen, id_receta_insertada)

    """for ingrediente in request.json["ingredientes"]:
        datos_ingrediente = {
            "nombre": ingrediente["ingrediente"],
            "cantidad": ingrediente["cantidad"],
            "id_receta": id_receta_insertada,
            "id_medida": ingrediente["id_medida"],
        }
        model.insert_ingrediente(datos_ingrediente)"""

    return redirect("/")


def agregar_imagen_receta():
    request.files["imagen"]


def comentar_receta(id_receta, id_usuario):
    comentario = request.form["contenido"]
    model.publicar_comentario(id_receta, id_usuario, comentario)
    return redirect(f"/receta/{id_receta}")


def usuario_delete(id):
    try:
        model.delete_usuario(id)
    finally:
        return redirect("/")
