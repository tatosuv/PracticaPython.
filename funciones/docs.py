#Lo que haremos es integrarle una documentación a las funciones y clases que hagamos



# def saludar(arg):
#     """Esta función lo que hace es saludar""" #Gracias a este comentario podemos entender qué hace la función
#     print("Hola", arg)

# help(saludar) #consulto a ver de que trata la función saludar



class Persona:
    """Aquí colocamos el nombre de nuestra clase"""
    def __init__(self):
        """Aquí inicializamos las características de la persona"""
        pass

    def estado(self):
        """Aquí consultamos el estado de las parsonas"""
        pass


i = Persona()

help(Persona)