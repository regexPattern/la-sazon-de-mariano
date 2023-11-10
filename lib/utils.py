from flask import session


def hay_sesion_activa():
    return session.get("id_usuario")
