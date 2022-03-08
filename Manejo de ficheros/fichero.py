from io import open

#fichero = open("archivo.txt", "w") #La creación y la apertura. la "w" es por write, si quisieramos leer el archivo debería ser "r"
#texto = "Hola Mundo\nEstudio Python" #El \n es para dar un salto de linea. Lo que hicimos acá es escribir el texto que quiero que se vea en el txt.
#fichero.write(texto) #La manipulación
#fichero.close() # Cierro

# fichero = open("archivo.txt", "r") #Leer
# texto = fichero.read()
# fichero.close()
# print(texto)

# fichero = open("archivo.txt", "r") #Leer
#linea = fichero.readlines() #Esto lo que hace es covertir en lista lo que tenemos en el archivo
#fichero.close()
#print(linea[0]) #le digo q me imprima el índice 0

fichero = open("archivo.txt", "a") #La "a" es de append(agregar)
fichero.write("\n Esto es el método append")
fichero.close()
print(fichero)