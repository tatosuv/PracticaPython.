from multiprocessing import context
import sqlite3

# TODO LO QUE HAGAMOS A CONTINUACIÓN ES PARA USAR EN SQLITE, DB BROWSER FOR SQLITE

conexion = sqlite3.connect("Productos.db") #BBDD de productos que tenga diferentes productos

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE productos(codigo_p VARCHAR(10)PRIMARY KEY,
    nombre_p VARCHAR(20),
    seccion_p VARCHAR(20))
''')
productos = [
    ('AR1', 'Leche', 'Lacteos'),
    ('AR2', 'Facturas', 'Panadería'),
    ('AR3', 'Lomo', 'Carnicería')
]

cursor.executemany("INSERT INTO productos VALUES(?,?,?)", productos)

conexion.commit()
conexion.close()

