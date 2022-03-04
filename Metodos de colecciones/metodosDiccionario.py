diccionario = {
    "Clave1":123,
    "Clave2":True,
    "Clave3":[1,2,3]
}

print(type(diccionario["Clave1"]))
print(type(diccionario["Clave2"]))
print(type(diccionario["Clave3"]))

print(diccionario.keys()) #nos da una lista con el nombre de las claves que creamos en el diccionario
print(diccionario.values()) #nos da una lista con el nombre de los valores que creamos en el diccionario
print(diccionario.items()) #nos da los ítems

for i,c in diccionario.items(): #para cada clave(i) y para cada valor(c) dentro de los items del diccionario...
    print(i,c) #imprimime cada clave con cada valor
