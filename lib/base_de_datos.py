import logging

import mysql.connector


class BaseDeDatos:
    __instancia = None

    @staticmethod
    def configurar(**config):
        logging.info("Conexión establecida con la base de datos")
        BaseDeDatos.__instancia = mysql.connector.connect(**config)

    @staticmethod
    def obtener_instancia():
        if BaseDeDatos.__instancia is None:
            raise Exception("No se ha inicializado ninguna conexión")

        return BaseDeDatos.__instancia


def sql_select(query, values=None):
    conexion = BaseDeDatos.obtener_instancia()
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


def sql_ejecute(query, values):
    conexion = BaseDeDatos.obtener_instancia()
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(query, values)
        logging.debug(cursor.statement)
        conexion.commit()
    except mysql.connector.Error as e:
        conexion.rollback()
        logging.error(e)
        raise e
