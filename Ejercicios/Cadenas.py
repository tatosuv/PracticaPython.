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

nombre = input("Escriba su nombre: ")

print(nombre.upper() + " tiene " + str(nombre.__len__()) + " letras.")

#o tambien
nombre = input("Escriba su nombre: ")

print(nombre.upper() + " tiene " + str(len(nombre)) + " letras.")

#Ejercicio4
#Los teléfonos de una empresa tienen el siguiente formato "prefijo-número-extension" donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.



