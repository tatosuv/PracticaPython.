import tkinter as tk # el AS funciona para asignar un alias
from tkinter import ttk

#vamos a crear botones utilizando ttk, se imprimirá en la terminal en vez de la interfaz gráfica

root = tk.Tk()


def seleccionar(opcion):
    print(opcion)


ttk.Button(root,text="Python", command=lambda:seleccionar("Python")).pack()  #el lambda se utiliza cuando tenemos un argumento en la función, si no tuviesemos ningun argumento, ponemos directamente la función
ttk.Button(root,text="Java", command=lambda:seleccionar("Java")).pack()
ttk.Button(root,text="Javascript", command=lambda:seleccionar("Javascript")).pack()

#lo que el usuario elija, se imprimirá en la terminal


root.mainloop()