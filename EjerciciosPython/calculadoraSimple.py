primero = input("Ingrese el primer número: ")
try:
    primero = int(primero)
except:
    primero = "No es un número"

if primero == "No es un número":
    print("El número ingresado no es un entero")
    exit()

segundo = input("Ingrese el segundo número: ")
try:
    segundo = int(segundo)
except:
    segundo = "No es un número"

if segundo == "No es un número":
    print("El número ingresado no es un entero")
    exit()

simbolo = input("Ingrese el símbolo de operación: ")
if simbolo == "+":
    print("El resultado de la suma es: ", primero + segundo)
elif simbolo == "-":
    print("El resultado de la resta es: ", primero - segundo)
elif simbolo == "*":
    print("El resultado de la multiplicación es: ", primero * segundo)
elif simbolo == "/":
    print("El resultado de la división es: ", primero / segundo)
else:
    print("El símbolo ingresado no es válido")
