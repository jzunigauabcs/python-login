import os
import mysql.connector
from mysql.connector import Error, IntegrityError
from dotenv import load_dotenv
from tkinter import messagebox

load_dotenv()

DB_CONFIG= {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT')
}



class DBConnector:
    """Clase estática para manejar la conexión a la base de datos."""
    @staticmethod
    def get_connection():
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            if conn.is_connected():
                return conn
        except Error as e:
            messagebox.showerror("Error de Conexión", f"No se pudo conectar a la base de datos.\nError: {e}")
            return None