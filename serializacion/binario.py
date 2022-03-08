import pickle #todo esto fue serialización con la librería PICKLE

lista = ["María", "Pedro", "José", "Antonio"]

fichero = open("lista_nombres", "wb") #"wb" es escritura en modo binario
pickle.dump(lista,fichero)

fichero.close()

#si quiero recuperar lo que había en lista, hago lo siguiente:

# fichero = open("lista_nombres", "rb") # "rb" es read en modo binario

# lista = pickle.load(fichero) #el load es para cargar el archivo

# print(lista)