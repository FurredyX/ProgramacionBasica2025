# --- Ejercicio 2: Manejo de Inventario ---

inventario = {}

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))
    inventario[nombre] = {"categoria": categoria, "precio": precio, "cantidad": cantidad}
    print("Producto agregado exitosamente.")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado exitosamente.")
    else:
        print("El producto no existe.")

def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    if nombre in inventario:
        print("Detalles del producto:", inventario[nombre])
    else:
        print("Producto no encontrado.")

def mostrar_productos_ordenados():
    productos_ordenados = sorted(inventario.items(), key=lambda x: x[1]["precio"])
    print("Productos ordenados por precio:")
    for nombre, detalles in productos_ordenados:
        print(f"{nombre}: {detalles}")
