#las tuplas, a diferencia de las listas, no son modificables


tupla = (20, 'Hola Mundo', True, [1,2,3,4])

print(tupla)
print(tupla[0])
print(tupla[1:])
print(tupla[2:])
print(tupla[-1])
print(tupla[3][1])

print(tupla.index(20)) #lo que nos va a devolver es en que índice se encuentra este elemento
print(tupla.index(21)) #da error porque no se encuentra en la tupla

print(tupla.count(20)) #le oreguntamos cuantas veces se encuentra 20 en nuestra tupla

print(len(tupla)) #longitud de nuestra tupla