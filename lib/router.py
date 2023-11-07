import lib.controller as controller


def configurar(app):
    @app.route("/")
    def inicio():
        return controller.inicio()

    @app.route("/buscar", methods=["GET", "POST"])
    def buscar():
        return controller.buscar()

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        return controller.signup()

    @app.route("/signin")
    def signin():
        return ""

    @app.route("/crear-receta", methods=["GET", "POST"])
    def crear_receta():
        # TODO: return controller.crear_receta()
        return ""
        
