class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def eliminar_contacto(self, nombre):
        self.contactos = [contacto for contacto in self.contactos if contacto.nombre != nombre]

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
        return None

    def listar_contactos(self):
        for contacto in self.contactos:
            print(contacto)

def mostrar_menu():
    print("\nAgenda de Contactos")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Listar contactos")
    print("5. Salir")

def main():
    agenda = Agenda()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agenda.agregar_contacto(Contacto(nombre, telefono, email))
        elif opcion == '2':
            nombre = input("Nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)
        elif opcion == '3':
            nombre = input("Nombre del contacto a buscar: ")
            contacto = agenda.buscar_contacto(nombre)
            if contacto:
                print(contacto)
            else:
                print("Contacto no encontrado.")
        elif opcion == '4':
            agenda.listar_contactos()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()