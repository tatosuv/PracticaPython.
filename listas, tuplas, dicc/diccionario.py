#son otro tipo de colección, guardan clave/valor
#no puede haber claves duplicadas

diccionario = {"Martin": "Gonzalez", "Pedro": "Sosa", "Pepe" : "Rojas", "Brian": {"Edad": 25,"Pais": "Argentina"}} #puedo agregar un diccionario dentro de otro diccionario
diccionario["Jorge"] = "Paez" #agrego una clave/valor
diccionario["Jorge"] = "PAEZ" #modifico lo anterior
del(diccionario["Martin"]) #elimino un registro
print(diccionario)
print(diccionario["Pepe"]) #me da el valor de Pepe
