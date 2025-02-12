import math

print("Iniciando el programa...")  # Mensaje de prueba

def es_primo(num, n=2):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % n == 0:
        return False
    if n > math.isqrt(num):
        return True
    return es_primo(num, n + 1 if n == 2 else n + 2)

if __name__ == "__main__":
    print("Programa listo para recibir entrada.")  # Mensaje de prueba
    while True:
        try:
            entrada = input("Introduce un número (o 'q' para salir): ")
            if entrada.lower() == 'q':
                break
            numero = int(entrada)
            resultado = es_primo(numero)
            print(f"El número {numero} {'es' if resultado else 'no es'} primo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

    print("Programa finalizado.")  # Mensaje de prueba
