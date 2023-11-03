import logging
import mysql.connector


def crear_conexion(host, user, password, database):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )


def seleccionar(conexion, query):
    try:
        cursor = conexion.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as e:
        conexion.rollback()
        logging.error(e)


def ejecutar(conexion, query, valores):
    try:
        cursor = conexion.cursor()
        cursor.execute(query, valores)
        conexion.commit()
    except mysql.connector.Error as e:
        conexion.rollback()
        logging.error(e)
