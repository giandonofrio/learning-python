# escribir una funcion que indique si el usuario es mayor de edad

def esMayor(usuario):
    return usuario.edad > 17


class Usuario:
    def __init__(self, edad):
        self.edad = edad


usuario = Usuario(int (input("Indique edad: ")))

resultado = esMayor(usuario)
 
if resultado:
    print("Usted es mayor de edad")
else:
    print ("Usted no es mayor de edad")    
