class Empleado:
    def __init__(self,ocupacion,salario,vacaciones):
        self.__ocupacion = ocupacion
        self.__salario = salario
        self.__vacaciones = vacaciones

    def datosEmpleado(self):
        print(f"Su ocupación es: {self.__ocupacion}")
        print(f"Tiene un salario de {self.__salario} pesos")
        print(f"Y sus días de vacaciones son {self.__vacaciones}")


