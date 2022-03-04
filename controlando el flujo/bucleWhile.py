#ejemplo 1

i = 0

while i <=10:
    print("Hola mundo", i)
    i+=1
else:
    print("Finalizó el rograma")

#ejemplo 2

edad = int(input("Ingrese su edad: "))

while edad <0:
    print("Has introducido una edad incorrecta. Vuelve a intentarlo")
    edad = int(input("Ingrese su edad: "))
else:
    print("Muchas gracias, finalizó el programa.")

#break y continue

j = 0
while j <=5:
    print(j)
    j+=1
    if j ==3:
        print("Rompemos todo")
        break
