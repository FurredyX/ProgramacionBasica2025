from Ejercicio_02 import agregar_producto
from Ejercicio_02 import eliminar_producto
from Ejercicio_02 import buscar_producto
from Ejercicio_02 import mostrar_productos_ordenados

agenda = []

def agregar_contacto():
    nombre = input("Ingrese el nombre: ")
    numero = input("Ingrese el número: ")
    correo = input("Ingrese el correo: ")
    agenda.append((nombre, numero, correo))
    print("Contacto agregado exitosamente.")

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    for contacto in agenda:
        if contacto[0] == nombre:
            print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
            return
    print("Contacto no encontrado.")

def listar_contactos():
    agenda_ordenada = sorted(agenda, key=lambda x: x[0])
    print("Lista de contactos ordenada:")
    for contacto in agenda_ordenada:
        print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")

# Menú de opciones
while True:
    print("\nMenú de opciones:")
    print("1. Agregar producto al inventario")
    print("2. Eliminar producto del inventario")
    print("3. Buscar producto en inventario")
    print("4. Mostrar productos ordenados por precio")
    print("5. Agregar contacto")
    print("6. Buscar contacto")
    print("7. Listar contactos ordenados")
    print("8. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        mostrar_productos_ordenados()
    elif opcion == "5":
        agregar_contacto()
    elif opcion == "6":
        buscar_contacto()
    elif opcion == "7":
        listar_contactos()
    elif opcion == "8":
        break
    else:
        print("Opción no válida. Intente nuevamente.")
