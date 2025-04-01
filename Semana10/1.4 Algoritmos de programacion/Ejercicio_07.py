import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivot]
    medio = [x for x in arr if x == pivot]
    derecha = [x for x in arr if x > pivot]
    return quicksort(izquierda) + medio + quicksort(derecha)

def busqueda_binaria(arr, objetivo):
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

tamano_lista = int(input("Ingrese el tamaño de la lista: "))
lista = [random.randint(1, 100) for _ in range(tamano_lista)]
print("Lista original:", lista)

lista_ordenada = quicksort(lista)
print("Lista ordenada:", lista_ordenada)

numero_a_buscar = int(input("Ingrese el número a buscar: "))
resultado = busqueda_binaria(lista_ordenada, numero_a_buscar)
if resultado != -1:
    print(f"El número {numero_a_buscar} se encuentra en la posición {resultado}.")
else:
    print(f"El número {numero_a_buscar} no está en la lista.")