def fibonacci(numero):
    a = 0 
    b = 1
    for _ in range(numero):
        print(a, end=" ")
        na = b
        nb = a + b
        a = na
        b = nb
    return
numero = 10
print(fibonacci(numero))