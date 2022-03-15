from tkinter import *

#creo las funciones

def mostrar():
    if opciones.get() ==1:
        label2.config(text="Has elegido Masculino")
    elif opciones.get() ==2:
        label2.config(text="Has elegido Femenino")
    else:
        label2.config(text="Has elegido otro")

#una vez que creo las funciones, debo asignarselas a cada radiobutton.

root = Tk()

opciones = IntVar() #nos dice que son enteros


label1 = Label(root, text="Elije un género")
label1.pack()
label1.config(bd=5, bg="blue")
Radiobutton(root, text="Masculino", variable=opciones, value=1, command=mostrar).pack() #le digo que si se elije este radiobutton, la opción es la 1
Radiobutton(root, text="Femenino", variable=opciones, value=2, command=mostrar).pack() #tienen valor diferente, por ende cada radiobutton es independiente del otro
Radiobutton(root, text="Otro", variable=opciones, value=3, command=mostrar).pack() #tienen valor diferente, por ende cada radiobutton es independiente del otro

label2=Label(root)
label2.pack()
label2.config(bg="yellow", fg="black")




root.mainloop()