from tkinter import *
from turtle import right 

root = Tk() 


root.title("Tato") 
root.resizable(1,1) 
root.iconbitmap("podio.ico") 
#root.geometry("600x350") #podemos cambiarle el ancho y largo que viene por default
miFrame = Frame(root) # le estoy indicando que nuestro FRAME va a estar adentro de nuestro root (la raiz)

# miFrame.pack(side=LEFT, anchor="n") #le digo donde quiero que esté mi frame. La "n" significa norte, puedo elegir "s" que es SUR, o las demas.
miFrame.pack(fill = "both", expand=1) # lo que hace la "x" es que el frame siga a lo largo a la raiz pero no en lo alto, la "y" hace lo contrario, el expand debería seguirlo en ambos

miFrame.config(width=400, height=300)
miFrame.config(cursor="pirate") #cambio de cursor, también tenemos la opción "boat"
miFrame.config(bg="red") #background rojo
miFrame.config(bd="20") #borde
miFrame.config(relief="sunken") #ahora vemos el borde de 20, tambien tenemos la opción "ridge"

#se puede hacer lo mismo pero poniendo el root

root.config(cursor="boat") #cambio de cursor, también tenemos la opción "boat"
root.config(bg="blue") #background rojo
root.config(bd="25") #borde
root.config(relief="sunken") #ahora vemos el borde de 20, tambien tenemos la opción "ridge"


root.mainloop() 