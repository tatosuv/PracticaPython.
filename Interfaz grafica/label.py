from pydoc import text
from tkinter import *

root = Tk()
root.title("Bienvenidos")
root.config(width=400, height=300)
#Para crear una label lo pimero que tenemos que hacer es crear una variable que se llame "label" y la igualo con Label (que pertenece a la librería de tkinter) y establecemos dónde se va a ubicar esa label

label = Label(root, text="Hola mundo!") #establecemos que nuestra label se va a situar en nuestra raiz que se llama root y su texto
#si lo ejecutamos no nos aparecerá nada, pues tenemos que empaquetarlo

label.pack()


label = Label(root, text="Bienvenidos")
label.pack()



root.mainloop()