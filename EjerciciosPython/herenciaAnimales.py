class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print("Hola soy un ", self.tipo, " y mi sonido es ", self.onomatopeya)


class Perro(Animal):
    tipo = "perro"
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print("Soy un perro extendido")


class Gato(Animal):
    tipo = "gato"
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print("Soy un gato extendido")


class Canario(Animal):
    tipo = "canario"


gato = Gato("Garfield", "Miau")
gato.saludo()

perro = Perro("Firulais", "Guau")
perro.saludo()

canario = Canario("Piolin", "Pio")
canario.saludo()
