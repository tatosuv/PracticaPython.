import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x300')
root.title("Páginas")

#creamos un cuadro madre

cuadroMadre = ttk.Notebook(root)
cuadroMadre.pack(pady=10, expand=True)

frame1 = ttk.Frame(cuadroMadre, width=400, height=280)
frame2 = ttk.Frame(cuadroMadre, width=400, height=280)
frame1.pack(fill="both", expand=True) # le decimos que se expanda tanto a la derecha como a la izquierda
frame2.pack(fill="both", expand=True)

#agregamos los frames a nuestro cuadro madre

cuadroMadre.add(frame1, text='Información General')
cuadroMadre.add(frame2, text='Perfiles')


boton = ttk.Button(frame1, text='Boton')
boton.pack()

root.mainloop()