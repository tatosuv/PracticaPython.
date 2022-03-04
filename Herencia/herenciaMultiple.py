class Clase1:
    def saluda(self):
        print("Hola soy el método de la clase 1")

class Clase2:
    def metodo2(self):
        print("Hola soy el método de la clase 2")

class Clase3(Clase1, Clase2):
    def metodo3(self):
        print("Hola soy el método de la clase 3")

c = Clase3() #instancia creada
c.metodo2()
c.saluda()
c.metodo3() # la clase 3 hereda de la clase 2 y también de la clase 1
