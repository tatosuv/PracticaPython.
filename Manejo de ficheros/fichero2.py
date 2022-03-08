from io import open

# fichero = open("Archivo.txt", "w") #creamos un archivo txt
# texto = "Hola, estamos trabajando con python, viendo los cursores" #le agregamos texto
# fichero.write(texto) #se lo escribimos
# fichero.close() #cerramos y ejecutamos

# fichero = open("Archivo.txt", "r")
# fichero.seek(10) #este método nos va a leer desde esa posición en adelante
# print(fichero.read())
# fichero.close()

fichero = open("Archivo.txt", "r")
fichero.seek(len(fichero.read())/2) #lo que hacemos acá es decirle que de toooda la longitud, me lleve el cursor a la mitad 
print(fichero.read())
fichero.close()