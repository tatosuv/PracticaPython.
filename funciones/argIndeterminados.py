def infinito(*args):
    print(args)

infinito("Hola", 20, 10.0, [1,2,3])

def infinito1(*args):
    for arg in args: #va a iterar sobre cada uno de los elementos y los va a imprimir de a uno en pantalla
        print(args)

infinito1("Hola", 20, 10.0, [1,2,3])

def infinito2(**kwargs):
    print(kwargs)

infinito2(a = "Hola", b = 20, c = ["María", "Pedro", "José"])

def infinito3(**kwargs):
    for kwarg in kwargs:
        print(kwarg)

infinito3(a = "Hola", b = 20, c = ["María", "Pedro", "José"])

def infinito4(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "--->", kwargs[kwarg])

infinito4(a = "Hola", b = 20, c = ["María", "Pedro", "José"])