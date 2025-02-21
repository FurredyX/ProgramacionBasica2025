def convertir_unidades(valor, unidad_origen, unidad_destino):
    conversiones = {
        'metros': {
            'kilometros': valor / 1000,
            'centimetros': valor * 100,
            'milimetros': valor * 1000
        },
        'kilometros': {
            'metros': valor * 1000,
            'centimetros': valor * 100000,
            'milimetros': valor * 1000000
        },
        'centimetros': {
            'metros': valor / 100,
            'kilometros': valor / 100000,
            'milimetros': valor * 10
        },
        'milimetros': {
            'metros': valor / 1000,
            'kilometros': valor / 1000000,
            'centimetros': valor / 10
        }
    }

    if unidad_origen in conversiones and unidad_destino in conversiones[unidad_origen]:
        return conversiones[unidad_origen][unidad_destino]
    else:
        return None

# Leer valores desde la entrada del usuario
valor = float(input("Ingrese el valor a convertir: "))
unidad_origen = input("Ingrese la unidad de origen (metros, kilometros, centimetros, milimetros): ")
unidad_destino = input("Ingrese la unidad de destino (metros, kilometros, centimetros, milimetros): ")

resultado = convertir_unidades(valor, unidad_origen, unidad_destino)
if resultado is not None:
    print(f"{valor} {unidad_origen} son {resultado} {unidad_destino}")
else:
    print("Conversión no válida")