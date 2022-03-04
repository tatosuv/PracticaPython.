productos = ["Carne", "Pastas", "Vino", "Pan", "Postres", True, False, 20, 1.0["Maria", "Pedro"]]

print(productos)
print(len(productos)) #longitud

#slicing: consultas a travez de índices

print(productos[9][0]) #accedo al índice 9 de mi lista, y a su vez al índice 0 de esa sublista (Maria)

print(productos.index("Vino")) #consulta a ver en que índice se encuentra vino

productos.insert(1,"Tato") #lo que hago es agregar un indice en el lugar de otro

print(productos)