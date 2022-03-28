import sqlite3
conexion = sqlite3.connect("PrimeraBade.db") #Establezco conexión con mi primera base

cursor=conexion.cursor()

#CREAMOS UNA TABLA


cursor.execute("CREATE TABLE usuarios(nombre VARCHAR(50), edad INTEGER, sexo VARCHAR(50))") 

# LE ASIGNAMOS VALORES A LA TABLA

cursor.execute("INSERT INTO usuarios VALUES('Tato', 24, 'Masculino')")


# HACEMOS UNA CONSULTA PARA DESPUES PODER VERLA EN LA TERMINAL

cursor.execute("SELECT * FROM usuarios")
usuario = cursor.fetchone() #hacemos que en una variable se vea la consulta
print(usuario) # de esta forma podemos verla en la terminal


# REALIZAMOS CONSULTA MÚLTIPLE

#agrupamos en tuplas dentro de una lista
usuario = [
    ('Tato', 24, 'M'),
    ('Fulana', 25, 'F'),
    ('Mengano', 26, 'M')
]
cursor.executemany("INSERT INTO usuarios VALUES(?,?,?)", usuario)


cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
print(usuarios)
for i in usuarios:
    print(i)

conexion.commit()

conexion.close() #cerramos la conexión

