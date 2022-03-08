import pickle # importamos la librería pickle ya que tiene los ficheros

class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def datosPersonales(self):
        print("El nombre de la persona es: " + self.nombre)
        print("La edad de la persona es: " + str(self.edad))
        print("El sexo de la persona es: " + self.sexo)

miPersona1 = Persona("María", 22, "Femenino")
miPersona2 = Persona("Jorge", 22, "Masculino")
miPersona3 = Persona("Coco", 22, "Marciano")

listaPersona = [miPersona1,miPersona2,miPersona3]

fichero = open("Personas", "wb")
pickle.dump(listaPersona, fichero)
fichero.close()
del(fichero)

ficheroleer = open("Personas", "rb")
miPersona = pickle.load(ficheroleer)
ficheroleer.close()

for i in miPersona:
    print(i.datosPersonales())