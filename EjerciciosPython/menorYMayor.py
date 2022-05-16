# escribir una función que encuentre el elemento menor y el mayor de una lista

lista = [21, 2122, 87343, 98348, 12, 94843, 91, 918428, -345]

menor = "init"
mayor = "init"

for x in lista:
    if menor == "init" or mayor == "init":
        menor = x
        mayor = x
    else:
        menor = x if x < menor else menor
        mayor = x if x > mayor else mayor

print("El menor numero es: ", menor)
print("El mayor numero es: ", mayor)
