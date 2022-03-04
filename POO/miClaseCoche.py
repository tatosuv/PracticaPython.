class Coche(): #Creamos nuestro molde
    def __init__(self): #lo podemos definir de esta forma tambien
        self.__marca="Audi"
        self.color="Rojo"
        self.__ruedas=4 #con el __ lo que hago es encapsular esa característica, es decir, no se va a poder modificar desde el exterior, solo puedo modificar desde adentro de la clase.
        self.enmarcha=False #Aplicamos las características

    def arrancar(self, arrancamos): #Creamos un método/función # También puedo encapsular los métodos
        self.enmarcha=arrancamos
        if(self.enmarcha): #Esto lo toma como que es Verdadero
            return "El coche está en marcha"
        else:
            return "El coche se encuentra apagado"

    def __str__(self): #Nos sirve para poner las características #creamos un método
        return "Este auto es marca {}, de color {} y tiene {} ruedas".format(self.__marca, self.color, self.__ruedas)

miCoche=Coche() #instanciamos la clase  
print(miCoche.arrancar(False)) #Encendemos y apagamos el vehículo.
print(str(miCoche)) #Mostramos en pantalla


#encapsulamiento: nos sirven para que las características (lineas 3 a 6), no sean modificadas desde el exterior.

print("*************OTRO VEHICULO************")

miCoche2= Coche()
miCoche2.__ruedas=20 #le estamos diciendo que este coche va a tener 20 ruedas
miCoche2.__marca= "Real Madrid"
print(miCoche2.arrancar(True))
print(str(miCoche2))

# Esto lo que me hace es modificar las características que le asignamos a la clase, no queremos que pase eso, por eso tenemos que encapsular
