#Es parecida al filter
'''
def doblar(numero):
    return numero*2

numeros = [2,5,10,23,50,33]

i = map(doblar, numeros)
print(list(i)) #me da la lista con los numeros doblados en valor

'''

#Podemos hacerlo con Lambda

def doblar(numero):
    return numero*2

numeros2 = [2,5,10,23,50,33]
a = [1,2,3,4,5]
b= [6,7,8,9,10]

i= map(lambda x,y: x*y, a,b)
print(list(i))