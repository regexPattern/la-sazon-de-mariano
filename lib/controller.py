from flask import redirect, render_template, request

import lib.model as model


def inicio():
    recetas = model.ultimas_recetas()
    params = {"recetas": recetas}
    return render_template("index.html", params=params)


def buscar():
    usuarios = model.obtener_resultados_busqueda_usuario(request.form["query"])
    return ""


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
            model.crear_usuario(usuario)
            return redirect("/signin")
        except:
            # TODO: Realmente no estamos haciendo nada con este mensaje de error en la pantalla.
            params = {"error": "Error al crear el usuario"}
            return render_template("signup.html", params=params)
