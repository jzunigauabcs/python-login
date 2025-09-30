from mysql.connector import IntegrityError, Error
from db.db_connector import DBConnector
from tkinter import messagebox


class UserModel:
    def __init__(self):
        pass

    def create_user(self, username, password, firstname, lastname):
        conn = DBConnector.get_connection()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            #query = "INSERT INTO users (username, password, firstname, lastname) VALUES (%s, %s, %s, %s)"
            #cursor.execute(query, (username, password, firstname, lastname))
            args = (username, password, firstname, lastname);
            cursor.callproc("SP_STORE_USER", args)
            conn.commit()
            return True
        except IntegrityError as e:
            messagebox.showerror("Error de registro", f"El nombre de usuario '{username}' ya existe en la base de datos")
            return False
        except Error as e:
            messagebox.showerror("Error de registro",
                                 f"Ocurrió un error en la base de datos {e}")
            return False
        finally:
            if conn.is_connected():
                conn.close()