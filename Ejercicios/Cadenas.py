#Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''
nombre = input("Escriba su nombre: ")
numero = int(input("Escriba un número: "))

print((nombre + "\n") * numero)

'''
#Ejercicio 2
#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''
nombre = input("Escriba su nombre: ")

print(nombre.lower())
print(nombre.upper())
print(nombre.capitalize()) # puede ir title() tambien
'''
#Ejercicio3
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
'''
nombre = input("Escriba su nombre: ")

print(nombre.upper() + " tiene " + str(nombre.__len__()) + " letras.")

#o tambien
nombre = input("Escriba su nombre: ")

print(nombre.upper() + " tiene " + str(len(nombre)) + " letras.")
'''
#Ejercicio4
#Los teléfonos de una empresa tienen el siguiente formato "prefijo-número-extension" donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
'''
tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])
'''
# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
'''
frase = input("Escriba una frase: ")

print(frase[::-1])
'''
# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
'''
frase = input("Introduzca una frase: ")
vocal = input("Y ahora introduzca una vocal en minúscula: ")


print("Tu frase es: "+ frase + ", y tu vocal es " + vocal.upper())
print(frase.replace(vocal,vocal.upper()))
'''
# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
'''
correo = input("Escriba su mail: ")
# NuevoCorreo = "@ceu.es" # esto no va

print(correo[:correo.find("@")] + "@ceu.es")
# print(correo.replace(correo.find("@"),NuevoCorreo)) # esto no va
'''
# Ejercicio 8 
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
'''
precio = input("Introduce un precio con 2 decimales: ")

print(precio[:precio.find(".")], "euros y", precio[precio.find(".")+1:], "centimos,")
'''

# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

cumpleanito = input("Ingrese su fecha de nacimiento: ")

print(cumpleanito)
