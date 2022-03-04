set_conjunto1 = set({1,2,3,4})
print(set_conjunto1)
set_conjunto1.add(22) #agrego un número
print(set_conjunto1)

set_conjunto = set({1.0, "Auto", True})
otro_conjunto = set_conjunto.copy() #copio
set_conjunto == otro_conjunto
print(otro_conjunto)

paquete = set({"Hola", 2,3,5})
print(paquete)
paquete.discard("Hola") #descarto el hola, tambien podemos usar el REMOVE
print(paquete)

