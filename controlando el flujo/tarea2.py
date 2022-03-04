# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.


#1

from tkinter import N


edad = int(input("Ingrese su edad: "))

if edad >=18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")


#2 

contraseña = "contraseña"

contraseñaUser = input("Introduzca su contraseña: ")

if contraseña == contraseñaUser.lower():
    print("Son iguales")
else:
    print("No son iguales")


#3

numero1 = int(input("Introduzca un número: "))
numero2 = int(input("Introduzca otro número: "))
division = numero1/numero2

if numero2 == 0:
    print("Se detectó un número inválido, pruebe nuevamente")
else:
    print(division)