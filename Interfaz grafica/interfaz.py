from tkinter import * #el tkinter ya vino con la instalación de Python

#para hacer nuestra primer ventana utilizamos "root." +título, pero para eso antes tenemos que crear la ventana
root = Tk() #esta es nuestra primer ventana


root.title("Tato") #Le damos un título
root.resizable(0,0) #el 0 indica false y el 1 true. Si le pongo 0 no puedo moverlo ni para arriba ni para los costados.
root.iconbitmap("limon.ico") #esto sirve para agregar un ícono al lado del título

root.mainloop() #con esto decimos que la ventana se mantenga abierta hasta que nosotros la cerremos, si ejecutamos algun programa sin el mainloop lo que pasará es que se va a abrir y cerrar enseguida, no tendremos tiempo a visualizarla. SIEMPRE tiene que estar por debajo del contenido que nosotros pongamos dentro.s