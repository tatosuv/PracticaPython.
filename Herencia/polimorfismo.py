# En POO el polimorfismo significa la capacidad de poder tomar mas de una forma

class Persona():
    def __init__(self):
        self.cedula = 12345

    def mensaje(self):
        print("Este mensaje viene de la clase persona")

class Obrero(Persona):
    def __init__(self):
        self.especialista = 1

    def mensaje(self):
        print("Este mensaje viene de la clase Obrero")

obrero_planta = Obrero()
obrero_planta.mensaje() #el polimorfismo llamó directamente a la clase Obrero, ya que interpretó que estabamos en la clase Obrero