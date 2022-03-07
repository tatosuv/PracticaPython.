from paquete.DatosPersonas import *
from paquete.empleado import *

i = Persona("María",22,"Femenino")
i.datosPersonales()

print("")

i = Empleado("Cocinero/a",15000,30)
i.datosEmpleado()