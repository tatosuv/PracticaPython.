from itertools import product
from tkinter import *
from turtle import width

root= Tk()
root.geometry("400x400")

productos=Label(root, text="Productos")
productos.pack()

#funciones
def agregar():
    listaProductos.insert(END, entrada.get()) #el END le indica que cada elemento que coloque el usuario, se agregue al final

def eliminar():
    listaProductos.delete(entrada.get()) 


listaProductos=Listbox(root,width=50) # le paso la lista de productos, a listaProductos le digo que es un Listbox
listaProductos.insert(0, "Carne") #en el índice 0 va la carne
listaProductos.insert(1, "Pollo") 
listaProductos.insert(2, "Verdura") 
listaProductos.insert(3, "Jugo") 
listaProductos.pack()

#eliminar productos

#listaProductos.delete(0) #pongo el índice del que quiero eliminar

#necesito un entry y un boton, para que el usuario pueda agregar el producto

entrada=Entry(root, bd=10)
entrada.pack()

boton = Button(root, text="Agregar producto", command=agregar)
boton.pack()

boton2 = Button(root, text="Eliminar producto", command=eliminar)
boton2.pack()






root.mainloop()