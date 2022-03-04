import sys
if len(sys.argv) ==3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for i in range(repeticiones):
        print(texto)
else:
    print("Error: introdujo uno (1) o mas de dos (2) argumentos")
    print("Solución: Introduce los argumentos correctamente")
    print("Solución ejemplo: entrada_argumentos.py 'texto ' 10")