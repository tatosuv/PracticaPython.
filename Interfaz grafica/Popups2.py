from tkinter import *
from tkinter import filedialog 

#vamos a intentar abrir un archivo por medio de la interfaz gráfica

root=Tk()

def abrir():
    archivo = filedialog.askopenfilename(title="Abrir", initialdir="Desktop", filetypes=(("Documento Python", ".py"),("Archivo Excell",".xlsx"))) # con el initialdir le indico desde qué ubicación debe buscar el archivo, y filetypes es un filtro
    print(archivo)

Button(root, text="Archivos", command=abrir).pack()


root.mainloop()