def verificacion(palabra):
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        return f'"{palabra}" es un palíndromo.'
    else:
        return f'"{palabra}" no es un palíndromo.'

lectura = input("Ingrese una palabra: ")
print(verificacion(lectura))