def convertir_temperatura(valor, origen, destino):
    if origen == "C" and destino == "F":
        return valor * 9/5 + 32
    elif origen == "C" and destino == "K":
        return valor + 273.15
    elif origen == "F" and destino == "C":
        return (valor - 32) * 5/9
    elif origen == "F" and destino == "K":
        return (valor - 32) * 5/9 + 273.15
    elif origen == "K" and destino == "C":
        return valor - 273.15
    elif origen == "K" and destino == "F":
        return (valor - 273.15) * 9/5 + 32
    else:
        return "Conversión no válida"

# Ejemplo de uso
valor = int(input("Introduce el tercer número: "))
origen = input("Introduce la escala de origen (entre C, F o K) : ")
destino = input("Introduce la escala de destino (entre C, F o K): ")

resultado = convertir_temperatura(valor, origen, destino)
print(f"{valor}°{origen} equivale a {resultado}°{destino}")
