from cgitb import text
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__() #La función super() se usa en la clase hija con herencia múltiple para acceder a la función de la siguiente clase padre o superclase.

        #Configuramos nuestra ventana
        self.title("Mi aplicación")
        self.geometry("300x50")

        #label
        self.label = ttk.Label(self, text="Hola Mundo")
        self.label.pack()

        #boton

        self.boton = ttk.Button(self, text="Haz click")
        self.boton["command"] = self.boton_accion
        self.boton.pack()

    def boton_accion(self):
        showinfo(title="Información", message="Hola Mundo!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
