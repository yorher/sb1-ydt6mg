import mysql.connector
from mysql.connector import Error

class BaseDatos:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='tienda'
            )
            self.cursor = self.conexion.cursor()
            self.crear_base_datos()
            self.crear_tabla()
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")

    def crear_base_datos(self):
        try:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS tienda")
            self.cursor.execute("USE tienda")
        except Error as e:
            print(f"Error al crear la base de datos: {e}")

    def crear_tabla(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    precio DECIMAL(10,2) NOT NULL,
                    cantidad INT NOT NULL
                )
            ''')
            self.conexion.commit()
        except Error as e:
            print(f"Error al crear la tabla: {e}")

    def cerrar(self):
        if self.conexion.is_connected():
            self.cursor.close()
            self.conexion.close()