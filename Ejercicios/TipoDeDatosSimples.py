#Ejercicio1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
''''

print("Hola Mundo!")
'''
#Ejercicio2
#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
''''

a = "Hola Mundo!"
print(a)
'''

#Ejercicio3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
'''
nombre = str(input("Cual es tu  nombre? "))

print(f"Hola {nombre}!")
'''

#Ejercicio4
#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética: (3+2/2*5)ˆ2
'''
a = 3 + 2
b = 2 * 5
c = a / b
d = c ** 2

print(d)
# o tambien

print(((3 + 2) / (2 * 5)) ** 2)

'''

#Ejercicio5
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
''''

from cmath import cos
from tracemalloc import start


horas_trabajadas = int(input("Cuantas horas trabajaste? "))
costo_por_hora = int(input("Cuanto cuesta la hora?" ))

if horas_trabajadas == 1:
    print("El costo de las horas trabajadas es de " + str(costo_por_hora) + " pesos")
elif horas_trabajadas < 1:
    print("La respuesta no puede ser inferior a 1, por favor, indique nuevamente las horas trabajadas")
else:
    print("El costo de las horas trabajadas es de " + str(horas_trabajadas*costo_por_hora) + " pesos")

#o tambien

horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = horas * coste
print("Tu paga es", paga)

'''

#Ejercicio6
#Escribir un programa que lea un entero positivo, n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: suma = n(n+1)/2
'''
n = int(input("Ingrese un número: "))
#suma = (n*(n+1)) / 2

for i in range(1,n+1):
    print(i, (i*(i+1)) / 2)

# o tambien

n = int(input("Introduce un número entero: "))
suma = n * (n + 1) / 2
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))
''' 

#Ejercicio7
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("Ingrese su peso: "))
estatura = float(input("Ingrese su estatura: "))

imc = peso / (estatura**2)
redondeo_imc = round(imc, 2)

print("Tu índice de masa corporal es: " + str(redondeo_imc))

#Ejercicio 8
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

num1 = int(input("Dividendo: "))
num2 = int(input("Divisor: "))

print(str(num1) + " entre " + str(num2) + " da un cociente " + str(int(num1) // int(num2)) + " y un resto " + str(int(num1) % int(num2)))