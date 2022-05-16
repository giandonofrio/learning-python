# escribir una función que indique si un número es par o impar

def esPar(n):
    return n % 2 == 0


resultado = esPar(int(input("Indique el numero: ")))

if resultado:
    print("El numero es par")
else:
    print("El numero es impar")
