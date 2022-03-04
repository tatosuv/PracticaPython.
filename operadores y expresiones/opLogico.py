# Operador not

print(not True) # Niega lo que tiene a la derecha

# Operador and

print(True and False) #ambas condiciones tienen que coincidir

#Operador or

print(True or False)

c= "Python"
print(len(c) < 8 or c [0 == "f"])


print("Sistema de becas 2022")

kil = int(input("A cuantos kilometros se encuentra de la escuela: "))
her = int(input("Cuantos hermanos tiene en la escuela: "))
ing = int(input("De cuanto es el ingreso en su casa?: "))

if kil < 10 and her < 2 or ing > 2000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")