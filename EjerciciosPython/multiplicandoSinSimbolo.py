# multiplicar dos números sin usar el símbolo de multiplicación

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
resultado = 0

for x in range (a):
    resultado += b

print("El resultado es: ", resultado)
