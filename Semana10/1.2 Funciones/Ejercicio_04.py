def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 1:
        return numeros_ordenados[n // 2]
    else:
        medio1 = numeros_ordenados[n // 2 - 1]
        medio2 = numeros_ordenados[n // 2]
        return (medio1 + medio2) / 2

def calcular_desviacion_estandar(numeros):
    media = calcular_promedio(numeros)
    varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
    return varianza ** 0.5

def calculadora_estadisticas(*args):
    if not args:
        return "No se ingresaron números."
    
    promedio = calcular_promedio(args)
    mediana = calcular_mediana(args)
    desviacion = calcular_desviacion_estandar(args)
    
    return {
        "Promedio": promedio,
        "Mediana": mediana,
        "Desviación estándar": desviacion
    }

ingreso = input("Ingrese una lista de números separados por espacio: ")
datos = []
for valor in ingreso.split():
    try:
        datos.append(float(valor))
    except ValueError:
        print(f"Valor ignorado: '{valor}' no es un número válido.")

if datos:
    resultado = calculadora_estadisticas(*datos)
    print("Resultados:", resultado)
else:
    print("No se ingresaron números válidos.")