def dame_un_texto():
    return "Texto" #cuando llega al return, ahi la función culmina y ya sale de la funcion
    print("Hola mundo") # esto no va a salir, porque la función terminó antes con el return

print(dame_un_texto())

def dame_un_texto2():
    return 123 

print(dame_un_texto2())

def dame_un_texto3():
    return [1,2,3] #lista

print(dame_un_texto3())


def dame_un_texto4():
    return {"Comida":"Asado", "Auto":"Audi","Mate":"Dulce" } #diccionario

print(dame_un_texto4())

def dame_un_texto5():
    return ("Marta", 20, "Hola mundo", ["Hola", "Si"]) #tupla

print(dame_un_texto5())