#son desordenados, se agregan como aleatoriamente
#en los conjuntos no pueden haber elementos duplicados

conjunto = set() #el set sirve a la hora de crear un conjunto, lo tenemos que poner por encima
conjunto = {2, "Python", True, 1.0, 20, "Python"}
conjunto.add(16) #agregamos un 16
conjunto.discard(2) #eliminamos el 2
conjunto.clear() #vaciamos todo
print(conjunto)
print(20 in conjunto) #le pregunto si 20 se encuentra en nuestro conjunto