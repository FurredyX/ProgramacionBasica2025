def mergesort(arr):
    if len(arr) <= 1:
        return arr
    medio = len(arr) // 2
    izquierda = mergesort(arr[:medio])
    derecha = mergesort(arr[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

ingreso = input("Ingrese una lista de números separados por espacio: ")
lista_usuario = [int(x) for x in ingreso.split()]
print("Lista original:", lista_usuario)

lista_ordenada_mergesort = mergesort(lista_usuario)
print("Lista ordenada con Mergesort:", lista_ordenada_mergesort)