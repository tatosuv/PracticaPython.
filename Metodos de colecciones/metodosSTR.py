#métodos en cadena de texto
i = input("Ingrese su nombre:")

print("El nombre de la persona es", i.upper()) # hace que lo que haya puesto en el i se ponga en mayúscula
print("El nombre de la persona es", i.lower()) # hace que lo que haya puesto en j se ponga en minúscula
print("El nombre de la persona es", i.capitalize()) # hace que lo que haya puesto en c se vuelva la primer letra mayúscula

texto = "Hola, me llamo Lisandro"
print("La cantidad de veces que figura el nombre Lisandro en el texto es de ", texto.count("Lisandro")) #cuenta la cantidad de veces que figura "Lisandro", en la cadena que le digamos.
print("La palabra que buscas se encuentra en el índice ", texto.find("Lisandro"))
print(texto.isdigit()) #nos dice si lo que tenemos en el parámetro 'texto' es un dígito(número) o no. Nos devuelve True/False
print(texto.split(" ")) #agrupa las palabras como en listas

j = "abc123"
print(j.isalnum()) #determina si lo que esta en j es alfanumérico




