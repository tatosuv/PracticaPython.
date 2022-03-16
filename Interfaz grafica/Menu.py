from tkinter import *

root = Tk()

# vamos a crear un menú

barraMenu = Menu(root) #creo una variable, del tipo Menu, que está dentro de nuestra raiz (root)
root.config(menu=barraMenu) #a la raiz le decimos que el menú es barraMenu

#vamos a crear la primer barra

archivoMenu = Menu(barraMenu, tearoff=0) #lo de tearoff es para que no me aparezca ninguna linea molesta
barraMenu.add_cascade(label="Archivo", menu=archivoMenu) #agrego la ventana "Archivo"
archivoMenu.add_command(label="Nuevo archivo") #Agrego las subventanas
archivoMenu.add_command(label="Nueva ventana")
archivoMenu.add_separator() #crea una línea divisoria entre ambas opciones, como si fuesen módulos diferentes
archivoMenu.add_command(label="Guardar como")

# vamos con otra barra menú

archivoEditar = Menu(barraMenu) #le digo que mi archivo editar se situa en mi barra menú
barraMenu.add_cascade(label="Editar", menu=archivoEditar) #le digo que pertenece a mi menú de "archivoEditar"
archivoEditar.add_command(label="Editar archivo")
archivoEditar.add_command(label="Rehacer")
archivoEditar.add_command(label="Borrar")

# vamos con la última barra

archivoAyuda= Menu(barraMenu)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label="Información de contacto")
archivoAyuda.add_command(label="Legales")
archivoAyuda.add_separator()
archivoAyuda.add_command(label="Ayuda")



root.mainloop()