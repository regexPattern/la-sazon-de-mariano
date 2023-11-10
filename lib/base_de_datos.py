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


class RegistroNoEncontrado(Exception):
    pass


def seleccionar(query, values=None):
    conexion = Conexion.obtener_instancia()
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(query, values)
        logging.debug(cursor.statement)
        filas = cursor.fetchall()
        return filas
    except mysql.connector.Error as e:
        conexion.rollback()
        logging.error(e)
        raise e


def ejecutar(query, values):
    conexion = Conexion.obtener_instancia()
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(query, values)
        logging.debug(cursor.statement)
        conexion.commit()
    except mysql.connector.Error as e:
        conexion.rollback()
        logging.error(e)
        raise e
