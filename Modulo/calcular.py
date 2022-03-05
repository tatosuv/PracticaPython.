# import calculadora #importamos el módulo que queremos para poder utilizarlo en este archivo.

# calculadora.sumar(2,5) #aca lo que hacemos es llamar a la función que está en el archivo "calculadora"
# calculadora.dividir(2,4)

from calculadora import sumar #lo que hacemos acá es importar solamente la función "sumar" del archivo calculadora

sumar(2,5) #gracias a esto, puedo llamar a la función esribiéndola directamente

#si le paso dividir() me va a tirar error, debería ponerlo en el import

from calculadora import * # lo que hacemos aca es importar tooooodo lo que tenemos en "calculadora"

sumar(2,4)
dividir(4,2)
restar(2,1)




