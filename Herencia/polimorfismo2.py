class Gato():
    def hablar(self):
        print("Miau")

class Perro(Gato):
    def hablar(self):
        print("Guau")

def escucharMascotas(animal):
    animal.hablar()


miMascota = Perro() #si acá ponemos Gato(), en el renglon siguiente nos saldría Miau
escucharMascotas(miMascota) # llama al método/función de Perro porque el código relaciona que nosotros estamos en la clase Perro
