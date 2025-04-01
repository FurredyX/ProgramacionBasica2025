def imperativo():
    print("--- Paradigma Imperativo ---")
    numeros = list(map(int, input("Ingrese una lista de números separados por espacio: ").split()))
    suma = 0
    for num in numeros:
        suma += num
    print(f"La suma de los números es: {suma}")

def calcular_factorial(n):
    """Función estructurada para calcular el factorial de un número."""
    if n == 0:
        return 1
    else:
        return n * calcular_factorial(n - 1)

def estructurado():
    print("--- Paradigma Estructurado ---")
    num = int(input("Ingrese un número para calcular su factorial: "))
    print(f"El factorial de {num} es {calcular_factorial(num)}")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def modular():
    print("--- Paradigma Modular ---")
    from modulo_operaciones import suma, resta
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    print(f"Suma de {a} y {b}: {suma(a, b)}")
    print(f"Resta de {a} y {b}: {resta(a, b)}")

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrar_info(self):
        return f"Vehículo: {self.marca} {self.modelo}"

def poo():
    print("--- Paradigma Orientado a Objetos ---")
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    auto = Vehiculo(marca, modelo)
    print(auto.mostrar_info())

imperativo()
estructurado()
modular()
poo()