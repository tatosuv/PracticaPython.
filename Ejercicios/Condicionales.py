# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Bien, sos mayor de edad!! Bravo!!")
else:
    print("No capo, estás verde todavía, te falta madurar.")

'''
#Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''
password = "tatocapo123"

passUser = input("Ingrese su contraseña: ")

if passUser.lower() == password:
    print("La contraseña coincide")
else: 
    print("Incorrecto flaco, probá devuelta")
'''

#Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''
nro1 = int(input("Ingrese un número: "))
nro2 = int(input("Y ahora otro jeje: "))

division = nro1/nro2

if nro2 == 0:
    print("Error, no puede realizarse la división, intente con otro número")
    nro2 = int(input("Ingrese un segundo número: "))
else:
    print("Su división da " + str(division))
'''

#Ejercicio 4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")
'''
# Ejercicio 5
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''
edad = int(input("Ingrese su edad: "))
ingreso = float(input("Su ingreso mensual es: "))

if edad >= 16 and ingreso >= 1000:
    print("Y... según sus ingresos y su edad, usted debería tributar.")
else:
    print("Nada por aquí, siga siga.")
'''

# Ejercicio 6
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (F/M): ")

if sexo == "F":
    if nombre[0].lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre[0].lower() > "n":
        grupo = "A"
    else:
        grupo = "B"

print("Tu grupo es " + grupo)
