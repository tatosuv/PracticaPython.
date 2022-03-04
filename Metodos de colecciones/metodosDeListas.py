lista = ["Jose", "María", "Pedro", "Jose"]
lista.append("Marcos") #agrego a Marcos a la lista
#lista.clear() #nos borra toda la lista
lista2= ["Rosario", "Anibal", "Antonio"]
lista.extend(lista2) #agrega los nuevos nombres a la lista. una lista se agrega a otra lista
lista.insert(0, "Hola") # le digo que en el índice 0 me agregue "Hola"
lista.reverse() #nos muestra la lista al reves

print(lista)
print(lista.count("Jose")) #contar cuantas veces aparece José en la lista
print(lista.index("Pedro")) #sobre que índice se encuentra José en la lista


