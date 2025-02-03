
import mysql.connector
from tkinter import messagebox

class Database:
    def __init__(self):
        pass
    def Connect(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="seusenha",
                database="contatos"

            )
            return conn
        except mysql.connector.Error as err:
            messagebox.showerror(err)
    def CriandoBanco(self):
        try:
            conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Lucca1209#"
            )
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS contatos;")
            conn.close()

            conn = self.Connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute("""
                 CREATE TABLE IF NOT EXISTS contatos(
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(100),
                        telefone VARCHAR(15),
                        instagram VARCHAR(100),
                        email VARCHAR(100)
                    )"""
                )
                conn.commit()
                conn.close()
                
        except mysql.connector.Error as err:
            messagebox.showerror(err)
