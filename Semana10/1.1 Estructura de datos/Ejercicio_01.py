def analizar_texto(texto):
    palabras = texto.lower().split()
    palabras_unicas = set(palabras)
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    palabra_mas_frecuente = max(frecuencia, key=frecuencia.get)
    max_frecuencia = frecuencia[palabra_mas_frecuente]
    print("Resumen del análisis:")
    print(f"Número total de palabras: {len(palabras)}")
    print(f"Cantidad de palabras únicas: {len(palabras_unicas)}")
    print("Frecuencia de cada palabra:")
    for palabra, count in frecuencia.items():
        print(f"  {palabra}: {count}")
    print(f"Palabra más frecuente: '{palabra_mas_frecuente}' (Aparece {max_frecuencia} veces)")
texto_usuario = input("Ingrese un texto para analizar: ")
analizar_texto(texto_usuario)