def hola(): #declaramos la funcion
    print("Hola Mundo") #le damos el cuerpo a la funcion

hola() #llamamos a la funcion

i = 20

def sumar():
    i = 10 #la variable que declaremos por dentro del def va a ser completamente independiente de la que declaremos por fuera
    print(i)

sumar()
print(i)

def suma():
    x = 10
    y = 10
    resultado = x+y
    print(f"El resultado de tu suma es : {resultado}")

suma()