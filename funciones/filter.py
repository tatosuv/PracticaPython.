edades = [12,11,25,44,6,10,15,16,18,20,26,66,79]

def mayores(edad):
    return edad >=18

entrar = list(filter(mayores,edades)) #nos permite filtrar una lista
print(entrar)