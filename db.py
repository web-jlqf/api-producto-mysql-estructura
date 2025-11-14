# db.py
import mysql.connector

def get_connection():
    # Ajusta estos datos a tu entorno
    return mysql.connector.connect(
        host="127.0.0.1",
        user="web",
        password="web123456",
        database="web-dbase"
    )
