#Clases y Objetos
class Gelatina: #Inicializamos el molde.
     def __init__(self, sabor, color, tamaño): #Self se refiere a un parámetro especial de python, que nos sirven para acceder a todas las caracteristicas que tiene nuestra clase.
         self.sabor=sabor #sabor, color y tamaño son caracteristicas de nuestro objeto
         self.color=color
         self.tamaño=tamaño #a cada una de las variables le asigno su significado con el SELF

     def imprimir (self): #este es nuestro método
         print("La gelatina es de "+ self.sabor)
         print("La gelatina se ve "+ self.color)
         print("La gelatina es "+ self.tamaño)

gel1 = Gelatina("Frutilla", "Roja", "Grande") #esta es mi primer instancia
gel2 = Gelatina("Mora", "Azul", "Chica")
gel3 = Gelatina("Pomelo", "Naranja", "Grande")
gel4 = Gelatina("Uva", "Violeta", "Chica")

gel1.imprimir() # llamo a mi instancia + la función
gel2.imprimir()
gel3.imprimir()
gel4.imprimir()




#los contrsuctores "init" nos permiten inicializar las caracteristicas que tenga niestra gelatina o las variables