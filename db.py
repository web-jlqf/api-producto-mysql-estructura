# db.py
import mysql.connector

def get_connection():
    # Ajusta estos datos a tu entorno
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu_password",
        database="academia_db"
    )
