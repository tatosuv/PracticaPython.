class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def datosPersonales(self):
        print("El nombre de la persona es: " + self.nombre)
        print("La edad de la persona es: " + str(self.edad))
        print("El sexo de la persona es: " + self.sexo)

    
