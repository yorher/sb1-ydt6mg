from db import BaseDatos
from producto import Producto
from mysql.connector import Error

class GestorProductos:
    def __init__(self):
        self.db = BaseDatos()

    def agregar_producto(self, producto):
        try:
            sql = 'INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s)'
            self.db.cursor.execute(sql, (producto.nombre, producto.precio, producto.cantidad))
            self.db.conexion.commit()
            print(f"Producto '{producto.nombre}' agregado exitosamente")
        except Error as e:
            print(f"Error al agregar producto: {e}")

    def listar_productos(self):
        try:
            self.db.cursor.execute('SELECT * FROM productos')
            productos = self.db.cursor.fetchall()
            if not productos:
                print("No hay productos registrados")
                return
            
            print("\nLista de Productos:")
            print("ID | Nombre | Precio | Cantidad")
            print("-" * 40)
            for producto in productos:
                print(f"{producto[0]} | {producto[1]} | ${producto[2]} | {producto[3]}")
        except Error as e:
            print(f"Error al listar productos: {e}")

    def actualizar_producto(self, id, producto):
        try:
            sql = '''UPDATE productos 
                    SET nombre = %s, precio = %s, cantidad = %s 
                    WHERE id = %s'''
            self.db.cursor.execute(sql, (producto.nombre, producto.precio, producto.cantidad, id))
            self.db.conexion.commit()
            if self.db.cursor.rowcount > 0:
                print(f"Producto con ID {id} actualizado exitosamente")
            else:
                print(f"No se encontró un producto con ID {id}")
        except Error as e:
            print(f"Error al actualizar producto: {e}")

    def eliminar_producto(self, id):
        try:
            self.db.cursor.execute('DELETE FROM productos WHERE id = %s', (id,))
            self.db.conexion.commit()
            if self.db.cursor.rowcount > 0:
                print(f"Producto con ID {id} eliminado exitosamente")
            else:
                print(f"No se encontró un producto con ID {id}")
        except Error as e:
            print(f"Error al eliminar producto: {e}")

    def cerrar(self):
        self.db.cerrar()