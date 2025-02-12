Num = int(input("Ingresa un numero que sea >= 0 para sacar su factorial: "))
if (Num > 0):
    for i in range(Num, 2, -1):
        Num = Num * (i - 1)
    print("El resultado es igual a: ", Num)
elif(Num == 0):
    Num = 1
    print("El resultado es igual a: ", Num)
else:
    print("Has ingresado un numero que no estaba en el intervalo")