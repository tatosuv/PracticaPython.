import sqlite3

conexion = sqlite3.connect("Productos.db")

cursor = conexion.cursor()

# cursor.execute("SELECT * FROM productos WHERE seccion_p='Panadería'")
# productos = cursor.fetchall()
# print(productos)


#ACTUALIZO LA TABLA CAMBIANDOLE UN NOMBRE

# cursor.execute("UPDATE productos SET seccion_p ='PANADERIA' WHERE seccion_p='Panadería'")


#ELIMINAR EL ID
cursor.execute("DELETE FROM productos WHERE ID = 2")


conexion.commit()
conexion.close()