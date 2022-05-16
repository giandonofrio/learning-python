# escribir una función que reciba nombre y apellido y los vaya agregando a
# un archivo

def agregaDatosAAarchivo(nombre, apellido):
    c = open("datos.txt", "a")
    c.write(nombre + " " + apellido + "\n")
    c.close()


while True:
    nombre = str(input("Ingrese el nombre (para salir escriba 'exit'): "))
    apellido = str(input("Ingrese el apellido (para salir escriba 'exit'): "))
    if nombre == "exit" or apellido == "exit":
        exit()
    else:
        agregaDatosAAarchivo(nombre, apellido)
