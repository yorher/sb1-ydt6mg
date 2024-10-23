from crud import GestorProductos
from producto import Producto

def menu():
    print("\n=== SISTEMA DE GESTIÓN DE PRODUCTOS ===")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    return input("Seleccione una opción: ")

def main():
    gestor = GestorProductos()

    while True:
        opcion = menu()

        if opcion == "1":
            try:
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad en stock: "))
                producto = Producto(nombre, precio, cantidad)
                gestor.agregar_producto(producto)
            except ValueError:
                print("Error: Por favor ingrese valores válidos")

        elif opcion == "2":
            gestor.listar_productos()

        elif opcion == "3":
            try:
                id = int(input("ID del producto a actualizar: "))
                nombre = input("Nuevo nombre: ")
                precio = float(input("Nuevo precio: "))
                cantidad = int(input("Nueva cantidad: "))
                producto = Producto(nombre, precio, cantidad)
                gestor.actualizar_producto(id, producto)
            except ValueError:
                print("Error: Por favor ingrese valores válidos")

        elif opcion == "4":
            try:
                id = int(input("ID del producto a eliminar: "))
                gestor.eliminar_producto(id)
            except ValueError:
                print("Error: Por favor ingrese un ID válido")

        elif opcion == "5":
            gestor.cerrar()
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()