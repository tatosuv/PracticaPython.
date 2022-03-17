from tkinter import *
from tkinter import messagebox #importo los popups

#vamos a crear un par de POPUPS, para ello haremos las funciones correspondientes a cada caso

def salir():
    i = messagebox.askquestion("Salir", "Está seguro que desea salir?") # definimos una variable en la cual el popup será con una pregunta. lo primero que ponemos es el título, y segundo el mensaje
    if i == "yes":
        root.destroy() # hace que salgamos por completo del programa


def acerca():
    messagebox.showinfo("Información", "Creado por Tato") # título + mensaje. el showinfo sirve para eso, para mostrar alguna información, tambien podemos aplicarle un showwarning

def licencia():
    messagebox.showinfo("Licencia", "Producto licenciado hasta 2025")


def error():
    messagebox.showerror("Error", "Que haces máquina? no apretés acá que se rompe todo!!")

def borrar():
    messagebox.askquestion("Estas seguro?", "Desea borrar todo?")

root = Tk()

# vamos a crear un menú

barraMenu = Menu(root) #creo una variable, del tipo Menu, que está dentro de nuestra raiz (root)
root.config(menu=barraMenu) #a la raiz le decimos que el menú es barraMenu

#vamos a crear la primer barra

archivoMenu = Menu(barraMenu, tearoff=0) #lo de tearoff es para que no me aparezca ninguna linea molesta
barraMenu.add_cascade(label="Archivo", menu=archivoMenu) #agrego la ventana "Archivo"
archivoMenu.add_command(label="Nuevo archivo") #Agrego las subventanas
archivoMenu.add_command(label="Nueva ventana", command=error)
archivoMenu.add_separator() #crea una línea divisoria entre ambas opciones, como si fuesen módulos diferentes
archivoMenu.add_command(label="Salir", command=salir)

# vamos con otra barra menú

archivoEditar = Menu(barraMenu) #le digo que mi archivo editar se situa en mi barra menú
barraMenu.add_cascade(label="Editar", menu=archivoEditar) #le digo que pertenece a mi menú de "archivoEditar"
archivoEditar.add_command(label="Editar archivo")
archivoEditar.add_command(label="Rehacer")
archivoEditar.add_command(label="Borrar", command=borrar)

# vamos con la última barra

archivoAyuda= Menu(barraMenu)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label="Acerca de...", command=acerca)
archivoAyuda.add_command(label="Licencia", command=licencia)
archivoAyuda.add_separator()
archivoAyuda.add_command(label="Ayuda")



root.mainloop()