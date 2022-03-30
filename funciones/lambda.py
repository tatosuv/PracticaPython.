#Definir una función sin definirla con el def

def suma(x,y):
    return(x+y)

print(suma(2,5)) #forma tradicional


i = lambda x,y: x+y #forma de hacerlo con lambda, es mas simplificado
print(i(2,3))

impar = lambda numero: numero/2 != 0 #a lambda le paso un numero
print(impar(5))

revertir = lambda cadena: cadena[::-1] # para poner de reversa #a lambda le paso una cadena
print(revertir("Python"))

doblar = lambda numero: numero*2
print(doblar(2))