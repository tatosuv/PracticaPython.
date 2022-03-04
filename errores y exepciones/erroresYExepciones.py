def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplicar(num1, num2):
    return num1*num2

def dividir(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError: #esto lo hacemos porque cuando dividimos por cero nos da este error, lo ponemos como excepción
        print("No se puede dividir entre 0")
        return "Operación no válida"

#lo del try/except evita que el programa se caiga a pedazos

op1 = int(input("Introduce el primer valor: "))
op2 = int(input("Introduce el segundo valor: "))

operacion = input("Introduce la operación a realizar (suma, resta, multiplicacion, dividir): ")

if operacion == "suma":
    print(suma(op1,op2))
elif operacion =="resta":
    print(resta(op1,op2))
elif operacion == "multiplicar":
    print(multiplicar(op1,op2))
elif operacion == "dividir":
    print(dividir(op1,op2))
else:
    print("Error, algo está mal")

print("Ejecutando")