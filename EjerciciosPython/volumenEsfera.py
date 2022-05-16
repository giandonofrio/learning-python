# escribir una función que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3
import math


def calcularVolumen(r):
    return 4/3 * math.pi * r ** 3


radio = int(input("Ingrese el radio de la Esfera: "))

resultado = calcularVolumen(radio)

print ("El volumen de la esfera es: " + str (resultado))
