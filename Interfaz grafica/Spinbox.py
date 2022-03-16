from faulthandler import disable
from telnetlib import STATUS
from tkinter import *

root=Tk()
root.geometry("400x300")

label1 = Label(text="Elegí tu lenguaje favorito:")
label1.pack()

w = Spinbox(root, values=("Python", "SQL", "Java", "Javascript"))
w.pack()

label2 = Label(text="Elegí tu gusto de empanada:")
label2.pack()

e = Spinbox(root, values=("Pollo", "Jamon y Queso", "Verdura", "Carne"))
e.pack()


root.mainloop()