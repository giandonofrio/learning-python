dato = input("Ingrese un dato: ")

lista  = ["Hola", "Mundo", "!"]

if lista.count(dato) > 0:
    print("El dato", dato, "se encuentra en la lista")
else:
    print ("El dato", dato, "no se encuentra en la lista")