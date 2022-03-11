from tkinter import * 

root = Tk() 


root.title("Tato") 
root.resizable(1,1) 
root.iconbitmap("podio.ico") 
#root.geometry("600x350") #podemos cambiarle el ancho y largo que viene por default
miFrame = Frame(root) # le estoy indicando que nuestro FRAME va a estar adentro de nuestro root
miFrame.pack()
miFrame.config(width=400, height=300)
miFrame.config(cursor="pirate")

root.mainloop() 