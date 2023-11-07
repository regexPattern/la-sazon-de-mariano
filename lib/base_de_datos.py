import logging

import mysql.connector


class Conexion:
    __instancia = None

    def __init__(self, **config):
        logging.info("Conexión establecida con la base de datos")
        Conexion.__instancia = mysql.connector.connect(**config)

    @staticmethod
    def obtener_instancia():
        if Conexion.__instancia is None:
            raise Exception("No se ha inicializado ninguna conexión")

        return Conexion.__instancia


def seleccionar(query, valores = None):
    conexion = Conexion.obtener_instancia()
    try:
        cursor = conexion.cursor()
        cursor.execute(query, valores)
        logging.debug(cursor.statement)
        return cursor.fetchall()
    except mysql.connector.Error as e:
        conexion.rollback()
        logging.error(e)
        raise e


def ejecutar(query, valores):
    conexion = Conexion.obtener_instancia()
    try:
        cursor = conexion.cursor()
        cursor.execute(query, valores)
        logging.debug(cursor.statement)
        conexion.commit()
    except mysql.connector.Error as e:
        conexion.rollback()
        logging.error(e)
        raise e
