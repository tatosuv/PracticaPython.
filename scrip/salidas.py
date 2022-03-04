from ctypes.wintypes import tagPOINT
from turtle import Terminator


a = "tato" 
b = 24
c = "Argentina"

print("Me llamo {} y mi edad es {}, país de origen {}".format(a,b,c)) #el format lo que hace es decir cuales son los parámetros que vamos a tomar para las llaves
#se usa cuanto tenemos que concatenar muchas variables
#en las llaves podemos poner el índice, por ej {0}, {1}, etc

# es lo mismo que hacer 

# print("Me llamo ", a, "y mi edad es",b)
#print("Me llamo {nombre} y mi edad es {edad}, pais de origen {pais}".format(nombre=a, edad=b, pais=c))



#si ponemos la f al principio del print, nos ahorramos poner el format al final

print(f"Me llamo {a} y mi edad es {b}, país de origen {c}")


