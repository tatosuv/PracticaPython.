class Persona:
    def __init__(self, nombre, edad, apellido, sexo):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.sexo = sexo

    def datosPersonales(self):
        print(f"El nombre de la persona es {self.nombre}")
        print(f"La edad de la persona es {self.edad}")
        print(f"El apellido de la persona es {self.apellido}")
        print(f"El sexo de la persona es {self.sexo}")


miPersona = Persona("Pepe", 20, "Gonzalez", "Masculino")

miPersona.datosPersonales()


print("*************AQUI COMIENZA OTRA PERSONA****************")

# HERENCIA

#Creamos otra clase que se va a llamar Empleado

class Empleado(Persona): #va a heredar todos los atributos de la clase persona
    def datosEmpleado(self, vacaciones, salario): #acá no estamos haciendo referencia a ningun atributo de la clase padre. Por eso no va el self
        print("Sus días de vacaciones son ", vacaciones)
        print("Su salario es: ", salario)

miPersona2 = Empleado("María", 22, "Luna", "Femenino")
miPersona2.datosPersonales()
miPersona2.datosEmpleado(30,50000) #acá estaría agregando los atributos de la herencia.

# NUNCA la clase padre puede heredar de la clase hija.