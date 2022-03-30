def devuelve_paises(*paises): #con el * le decimos que queremos poner todos los paises que queramos
    for elemento in paises:
        for subelemento in elemento:
            yield subelemento #yield nos va a mostrar lo que está iterando en paises

paises_devuelta = devuelve_paises("Argentina", "Brasil", "Peru", "Chile")
print(next(paises_devuelta)) #me muestra de a 1
print(next(paises_devuelta))