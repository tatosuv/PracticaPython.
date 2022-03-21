import tkinter as tk
from tkinter import ttk

#root ventana

root = tk.Tk()
root.geometry('300x120')
root.title('Barra de Progreso')

root.grid()

bd= ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=280)

bd.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

boton_iniciar = ttk.Button(root, text="Iniciar", command=bd.start)

boton_iniciar.grid(column=0,row=1,padx=10,pady=10, sticky=tk.E) # la E es de East

boton_parar = ttk.Button(root, text="Parar", command=bd.stop)

boton_parar.grid(column=1,row=1,padx=10,pady=10, sticky=tk.W) # La W es de West

root.mainloop()