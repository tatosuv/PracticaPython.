from tkinter import *

root= Tk()

frame = Frame(root, width=500, height=400)
frame.pack()

entrada = Entry(frame) #Nuestro entry va a estar en nuestro frame, nos permite escribir
entrada.grid(row=0, column=1) # lo posicionamos mediante GRID
entrada.config(justify="center", state="normal")

entrada2 = Entry(frame)
entrada2.grid(row=1, column=1)
entrada2.config(justify="center", show="*")  #le digo que me muestre el texto en formato contraseña


label1 = Label(frame, text="Nombre:")
label1.grid(row=0, column=0)

label2 = Label(frame, text="Password:")
label2.grid(row=1, column=0)


root.mainloop()