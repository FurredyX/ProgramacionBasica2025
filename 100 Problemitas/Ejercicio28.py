class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

cuenta = CuentaBancaria(1000)

while True:
    print("\n1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        cuenta.consultar_saldo()
    elif opcion == '2':
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        cuenta.depositar(cantidad)
    elif opcion == '3':
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        cuenta.retirar(cantidad)
    elif opcion == '4':
        print("Gracias por usar el sistema bancario.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")