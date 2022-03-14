from tkinter import *

root= Tk()

frame = Frame(root, width=500, height=400)
frame.pack()

entrada = Entry(frame) #Nuestro entry va a estar en nuestro frame, nos permite escribir
entrada.pack()


label = Label(frame, text="Nombre")
label.pack()





root.mainloop()