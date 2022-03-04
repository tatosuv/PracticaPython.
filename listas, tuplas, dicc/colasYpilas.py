cola = ["Jose", "Martin", "Brian", "Marcelo"]
cola.append("Paola")
cola.append("Romina")
print(cola)
# para sacar un elemento vamos a hacer el .pop

i = cola.pop(0) #elimina al primero, supongamos que a josé lo llamó el doctor y está siendo atendido
i = cola.pop(0) #ahora lo llamaron a Martin (porque al irse josé, el que pasa a ser el índice 0 es Martin)
print(f"Estan atendiendo a {i}")

