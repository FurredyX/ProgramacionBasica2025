print("Calculadora basica")
num1 = int(input("Ingresas el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
operacion = int(input("¿Que operacion deseas hacer?\n\nIngresa 1 para sumar\nIngresa 2 para restar\nIngresa 3 para multiplicar\nIngresa 4 para dividir\n\n"))
if (operacion == 1):
    resultado = num1 + num2
    print("El resultado es: ", resultado)
elif (operacion == 2):
    resultado = num1 - num2
    print("El resultado es: ", resultado)
elif (operacion == 3):
    resultado = num1 * num2
    print("El resultado es: ", resultado)
elif (operacion == 4):
    resultado = num1 / num2
    print("El resultado es: ", resultado)
elif (operacion > 1 and operacion<4):
    print("El numero que has ingresado no esta dentro de las opciones\npor favor inicie el programa de nuevo")