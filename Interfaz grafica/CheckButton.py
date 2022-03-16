from tkinter import *
from turtle import left

root=Tk()
root.config(bd=20, bg="goldenrod3")
root.title("Casa de comidas") #título


def orden():
    lista=""
    if(aceite.get()):
        lista += "Con aceite"
    else:
        lista += "Sin aceite"

    if (tomate.get()):
        lista +=  "  y con tomate"
    else:
        lista += " y sin tomate"

    imprimir.config(text=lista)


aceite = IntVar()
tomate = IntVar()


#imagen = PhotoImage(file="ensalada.gif")
#Label(root, image=imagen).pack(side=LEFT)

frame = Frame(root)
frame.pack(side=RIGHT)
frame.config(bg="goldenrod3")

Label(frame, text="Cómo quieres tu ensalada?", bg="goldenrod3", font="Curier 15").pack(anchor="w")
Checkbutton(frame, text="Con aceite", variable=aceite, onvalue=1, offvalue=0, bg="goldenrod3", font="Curier 15", command=orden).pack(anchor="w") 
Checkbutton(frame, text="Con tomate", variable=tomate, onvalue=1, offvalue=0,bg="goldenrod3", font="Curier 15", command=orden).pack(anchor="w")

imprimir = Label(frame, bg="goldenrod3")
imprimir.pack()
imprimir.config(font="Curier 20")

root.mainloop()