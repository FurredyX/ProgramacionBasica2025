def suma_serie(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

n = int(input("Introduce un número: "))
resultado = suma_serie(n)
print(f"La suma de la serie hasta {n} es: {resultado}")