class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def datosPersonales(self):
        print("El nombre de la persona es: " + self.nombre)
        print("La edad de la persona es: " + str(self.edad))
        print("El sexo de la persona es: " + self.sexo)

    
miPersona = Persona("Tato", 20, "Masculino")
miPersona2 = Persona("María", 20, "Femenino")
miPersona3 = Persona("NN", 20, "No binario")

miPersona.datosPersonales()
miPersona2.datosPersonales()
miPersona3.datosPersonales()