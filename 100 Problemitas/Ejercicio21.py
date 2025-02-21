import math

print("Calculadora basica")
figura = int(input("Introduce el numero de la figura geometrica\n\n1- Cilindro\n2- Cono\n3- Esfera\n\n"))
if (figura < 1 and figura> 3):
    print("El numero que has ingresado no esta dentro de las opciones\npor favor inicie el programa de nuevo")
else:
    if (figura == 1):
        radio = int(input("Introduce el radio del cilindro: "))
        altura = int(input("Introduce la altura del cilindro: "))
        Area = 2*math.pi*radio*+2*(math.pi+radio**2)
        Volumen = math.pi*(radio**2)*altura
        figura = "Cilindro"
    elif (figura == 2):
        radio = int(input("Introduce el radio del Cono: "))
        altura = int(input("Introduce la altura del Cono: "))
        Area = math.pi*radio*(radio+math.sqrt(radio**2+altura**2))
        Volumen = math.pi*(radio**2)*altura/3
        figura = "Cono"
    elif (figura == 3):
        radio = int(input("Introduce el radio de la esfera: "))
        Area = 4*math.pi*(radio**2)
        Volumen = 4/3*math.pi*(radio**3)
        figura = "Esfera"
    print("El area del", figura, "es: ", Area)
    print("El volumen del", figura, "es: ", Volumen)