num1 = 1 ; num2 = 1
Fb = int(input("Ingresa un numero que sea >= 0 para generar la secuencia de fibonacci: "))
if (Fb > 3):
    print("\nLos sucesion de tamaño", Fb, "Es la siguiente:\n\n0 1 1", end=" ")
    for i in range(1, Fb-2):
        num3 = num1 + num2
        print(num3, end=" ")
        num1 = num2
        num2 = num3
elif (Fb == 3):
    print("\nLos sucesion de tamaño", Fb, "Es la siguiente:\n\n0 1 1")
elif (Fb == 2):
    print("\nLos sucesion de tamaño", Fb, "Es la siguiente:\n\n0 1")
elif (Fb == 1):
    print("\nLos sucesion de tamaño", Fb, "Es la siguiente:\n\n0")
else:
    print("\nHas ingresado un numero que no estaba en el intervalo")
print("\n")