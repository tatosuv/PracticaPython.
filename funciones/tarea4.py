# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.
# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
# Escribir una función que reciba un número entero positivo y devuelva su factorial.


def saludo():
    print("Hola amiga!")

saludo()

def saludar(nombre):
    saludo = "Hola "
    saludoCompleto = saludo + nombre
    return saludoCompleto

print(saludar("Tato"))

def numero(a):
    num= int(input("Escriba su número entero positivo: "))
    factorial= num * (num-1)
    return factorial
print(numero(4))