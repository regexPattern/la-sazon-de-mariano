from flask import Flask

from lib import router

def main():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config[
        "SECRET_KEY"
    ] = "SOsVMlbxQFy5LsbG0pUmXQ6PxxGHEcoO6BFoSyLXufyRL5TrQ9xfNRc27rjCIH3hAFu3yGaqXG1Kxba0EZfsGsJgUw0Jjbt2Agbc"
    app.config["UPLOAD_FOLDER"] = "./static/img/"

    router.configurar(app)
    app.run("0.0.0.0", 5000, debug=True)



if __name__ == "__main__":
    main()
