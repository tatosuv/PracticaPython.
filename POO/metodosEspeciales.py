class Coche:
    def __init__(self, marca, kilometros, año):
        self.marca = marca
        self.kilometros = kilometros
        self.año = año
        print(f"Se ha creado un auto {self.marca}, con {self.kilometros} km.")
    
    def __del__(self): #esta funcion/metodo es para eliminar este auto
        print(f"Se ha vendido el auto {self.marca}")

    def __str__(self):
        return "El auto es un {}, tiene {} km, y es del año {}".format(self.marca, self.kilometros, self.año)

miCoche = Coche('Audi', 0, 2022) #mi primera instancia/objeto
# del(miCoche)

print(str(miCoche))

