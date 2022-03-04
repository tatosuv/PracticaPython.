#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

#1

curso = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(curso)

#2
'''
curso = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print("Yo estudio", curso[0])
print("Yo estudio", curso[1])
print("Yo estudio", curso[2])
print("Yo estudio", curso[3])
print("Yo estudio", curso[4])
'''

# respuesta del profe
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for subject in subjects:
    print("Yo estudio " + subject)

#3
'''
nota = float(input("Nota que has sacado: "))
print("En ", curso[0], "has sacado ", nota)
nota = float(input("Nota que has sacado: "))
print("En ", curso[1], "has sacado ", nota)
nota = float(input("Nota que has sacado: "))
print("En ", curso[2], "has sacado ", nota)
nota = float(input("Nota que has sacado: "))
print("En ", curso[3], "has sacado ", nota)
nota = float(input("Nota que has sacado: "))
print("En ", curso[4], "has sacado ", nota)
'''
#respuesta del profe

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])