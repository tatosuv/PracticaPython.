import tkinter as tk
from tkinter.colorchooser import askcolor
from turtle import title

#Como cambiar el color de la ventana en el momento

root = tk.Tk()
root.title("Tkinter Color")
root.geometry("300x150")

def cambiarColor():
    colores = askcolor(title="tkinter colores")
    root.configure(bg=colores[1])

tk.Button(
    root,
    text="Cambiar color",
    command=cambiarColor).pack(expand=True)







root.mainloop()