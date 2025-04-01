def km_a_millas(km):
    return km * 0.621371

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def litros_a_galones(l):
    return l * 0.264172

import conversor

def menu_conversion():
    print("\nMenú de Conversión:")
    print("1. Kilómetros a millas")
    print("2. Celsius a Fahrenheit")
    print("3. Litros a galones")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        km = float(input("Ingrese kilómetros: "))
        print(f"{km} km = {conversor.km_a_millas(km)} millas")
    elif opcion == "2":
        c = float(input("Ingrese grados Celsius: "))
        print(f"{c}°C = {conversor.celsius_a_fahrenheit(c)}°F")
    elif opcion == "3":
        l = float(input("Ingrese litros: "))
        print(f"{l} litros = {conversor.litros_a_galones(l)} galones")
    elif opcion == "4":
        return
    else:
        print("Opción no válida.")
    menu_conversion()

# Iniciar el menú
menu_conversion()