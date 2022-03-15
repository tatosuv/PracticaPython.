from tkinter import *

#creo funciones para asignarle a los botones

def sumar():
    resultado.set(int(var1.get())+ int(var2.get())) #set: lo que va a recibir, get: va a rescatar lo que recibe 

def restar():
    resultado.set(int(var1.get())- int(var2.get())) #set: lo que va a recibir,al resultado le seteo la ecuación. get: va a rescatar lo que recibe 

root = Tk()

frame= Frame(root)
frame.pack()

#asigno variables
var1= StringVar()
var2= StringVar()
resultado= StringVar()


#Creación de una calculadora
entrada1= Entry(frame)
entrada1.pack()
entrada1.config(bd=10, font="Curier, 20", textvariable=var1)

entrada2= Entry(frame)
entrada2.pack()
entrada2.config(bd=10, font="Curier, 20", textvariable=var2)

entrada3= Entry(frame)
entrada3.pack()
entrada3.config(bd=10, font="Curier, 20", state="disable", textvariable=resultado) #el disable es para que no se pueda manipular esa parte

boton1= Button(frame, text="Sumar") # creo el boton asignandole Button a un parámetro, le digo que el boton va a estar en el frame y que se va a llamar "Sumar"
boton1.pack()
boton1.config(bd=5, font="Curier, 10", command=sumar) #con el command llamo a la función


boton2= Button(frame, text="Restar")
boton2.pack()
boton2.config(bd=5, font="Curier, 10")

root.mainloop()