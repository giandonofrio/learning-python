# escribir una aplicación que reciba una cantidad infinita de números hasta
# decir basta, luego que devuelva la suma de los números ingresados


from unittest import result


lista = []
print("Ingrese numero y para salir escriba 'basta': ")
while True:
    valor = input("Ingrese numero: ")
    if valor == "basta":
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print("Dato invalido")
            break
resultado = 0
for x in lista:
    resultado += x

print("La suma final es: " ,str (resultado))
