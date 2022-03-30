# def generaPares(limite):
#     num=1
#     miLista=[]
#     while num<limite:
#         miLista.append(num*2)
#         num= num+1
#     return miLista

# print(generaPares(10))

def generaPares(limite): #este es el metodo yield
    num=1
    miLista=[]
    while num<limite:
        yield num*2
        num = num+1
    
devuelvePares = generaPares(10)
for i in devuelvePares:
    print(i)