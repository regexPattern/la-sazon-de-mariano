import json
from flask import Flask, request, render_template


app = Flask(__name__)


with open("base-de-datos.json") as archivo:
    base_de_datos = json.load(archivo)


@app.route("/")
def inicio():
    # TODO: Eventualmente esto va a salir de la DB
    paises = base_de_datos["paises"]
    recomendaciones = base_de_datos["recomendaciones"]

    return render_template("index.html", paises=paises, recomendaciones=recomendaciones)


@app.route("/explorar")
def explorar():
    args = request.args or 0
    return render_template("explorar.html", query=args["query"])


@app.route("/receta/<int:id>")
def receta(id):
    # TODO: Eventualmente esto va a salir de la DB
    recetas = [receta for receta in base_de_datos["recomendaciones"]
               if receta["id"] == id]

    if len(recetas) == 0:
        return render_template("404.html")
    else:
        return render_template("receta.html", receta=recetas[0])


@app.route("/crear-cuenta")
def crear_cuenta():
    return render_template("crear-cuenta.html")


@app.route("/cuenta-creada")
def cuenta_creada():
    return render_template("cuenta-creada.html")


@app.route("/crear-receta")
def crear_receta():
    return render_template("crear-receta.html")


@app.route("/perfil")
def perfil():
    usuario = base_de_datos["usuario"]
    return render_template("perfil.html", usuario=usuario)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
