'''
c = int(input("Ingrese un valor: "))
c/0
'''
#si hago la división, el programa se me rompe porque no se puede dividir por 0, debo meter todo adentro de un try

try:
    c = int(input("Ingrese un valor: "))
    c/0
except ValueError: 
    print("Error, ingrese un número")
except Exception as c:
    print(type(c).__name__)