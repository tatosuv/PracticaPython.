from tkinter import *

#luego de crear los botones (están mas abajo), creo las funcionalidades que les voy a dar

i=0 #variable global

def click(valor): #lo que hace es que a medida que voy escribiendo/oprimiendo los botones, se va llenando en orden 
    global i
    entrada.insert(i,valor) #lo que recibimos nosotros por entrada
    i+=1 # que i se incremente en 1

def borrar():
    entrada.delete(0, END) # desde el índice 0 hasta el final, se borra todo
    i=0 #la i se reinicia a 0

#en vez de crear una función por cada boton (sumar restar, etc), uso el EVAL

def operaciones():
    operacion = entrada.get() #va a recibir lo que pongamos
    resultado = eval(operacion)
    entrada.delete(0, END)
    entrada.insert(0, resultado)
    i = 0



root= Tk()
root.title("Calculadora")
root.resizable(0,0) #hola

# Entrada
entrada = Entry(root, font=("Curier 20"))
entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=5) #el columnspan=4 nos dice que el grid tendrá hasta 4 columnas

#Botones

boton1 = Button(root,text="1", width=3, height=3, command=lambda:click(1)) #el lambda lo que hace es escribir la funcion en una sola línea y ademas nos deja pasar argumentos
boton2 = Button(root,text="2", width=3, height=3, command=lambda:click(2))
boton3 = Button(root,text="3", width=3, height=3, command=lambda:click(3))
boton4 = Button(root,text="4", width=3, height=3, command=lambda:click(4))
boton5 = Button(root,text="5", width=3, height=3, command=lambda:click(5))
boton6 = Button(root,text="6", width=3, height=3, command=lambda:click(6))
boton7 = Button(root,text="7", width=3, height=3, command=lambda:click(7))
boton8 = Button(root,text="8", width=3, height=3, command=lambda:click(8))
boton9 = Button(root,text="9", width=3, height=3, command=lambda:click(9))
boton0 = Button(root,text="0", width=11, height=3, command=lambda:click(0))

# Boton borrar, parentesis y el punto

botonBorrar = Button(root,text="AC", width=3, height=3, command=lambda:borrar()) # le asigno la funcion de borrar
botonParentesis1 = Button(root,text="(", width=3, height=3, command=lambda:click("("))
botonParentesis2 = Button(root,text=")", width=3, height=3, command=lambda:click(")"))
botonPunto = Button(root,text=".", width=3, height=3, command=lambda:click("."))

# Boton de suma, resta, multiplicación, división e igual

botonSuma = Button(root,text="+", width=3, height=3, command=lambda:click("+"))
botonResta = Button(root,text="-", width=3, height=3, command=lambda:click("-"))
botonMultiplicacion = Button(root,text="x", width=3, height=3, command=lambda:click("*"))
botonDivision = Button(root,text="/", width=3, height=3, command=lambda:click("/"))
botonIgual = Button(root,text="=", width=3, height=3, command=lambda:operaciones())

#Colocar botones en el grid

# Row 1
botonBorrar.grid(row=1, column=0,padx=5, pady=5)
botonParentesis1.grid(row=1, column=1,padx=5, pady=5)
botonParentesis2.grid(row=1, column=2,padx=5, pady=5)
botonDivision.grid(row=1, column=3,padx=5, pady=5)

# Row 2
boton7.grid(row=2, column=0,padx=5, pady=5)
boton8.grid(row=2, column=1,padx=5, pady=5)
boton9.grid(row=2, column=2,padx=5, pady=5)
botonMultiplicacion.grid(row=2, column=3,padx=5, pady=5)

# Row 3
boton4.grid(row=3, column=0,padx=5, pady=5)
boton5.grid(row=3, column=1,padx=5, pady=5)
boton6.grid(row=3, column=2,padx=5, pady=5)
botonResta.grid(row=3, column=3,padx=5, pady=5)

# Row 4
boton1.grid(row=4, column=0,padx=5, pady=5)
boton2.grid(row=4, column=1,padx=5, pady=5)
boton3.grid(row=4, column=2,padx=5, pady=5)
botonSuma.grid(row=4,column=3, padx=5, pady=5) 

# Row 5
boton0.grid(row=5, column=0,columnspan=2 ,padx=5, pady=5) #el columnspan=2 es para que el boton 0 ocupe 2 columnas
botonPunto.grid(row=5, column=2,padx=5, pady=5)
botonIgual.grid(row=5, column=3,padx=5, pady=5)





root.mainloop()