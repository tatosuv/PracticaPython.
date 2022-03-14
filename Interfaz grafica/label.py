from pydoc import text
from tkinter import *

root = Tk()
root.title("Bienvenidos")
root.config(width=400, height=300)
#Para crear una label lo pimero que tenemos que hacer es crear una variable que se llame "label" y la igualo con Label (que pertenece a la librería de tkinter) y establecemos dónde se va a ubicar esa label

label = Label(root, text="Aguante") #establecemos que nuestra label se va a situar en nuestra raiz que se llama root y su texto
#si lo ejecutamos no nos aparecerá nada, pues tenemos que empaquetarlo

label.place(x=100, y=50) #le indicamos con coordenada dónde queremos nuestro Label
label.config(bg="blue", fg="black", font=("Curier", 20))


label = Label(root, text="Boca!")
label.place(x=200, y=60)
label.config(bg="yellow", fg="black", font=("Curier", 20))


root.mainloop()