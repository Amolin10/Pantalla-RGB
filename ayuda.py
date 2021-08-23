from os import cpu_count
from tkinter import *
from tkinter import ttk
import os.path
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog


def ayudaClose():
    ayuda.cerrar()

def ventanaAyuda():
    ayuda.cargar()
    ayuda.mostrar()

class Ayuda:

    def __init__(self):
        self.title = "Letrero RGB Ayuda"
        self.icon = "firefly.ico"
        self.resizable = True

    def cargar(self):
        root = Tk()
        self.root = root
        root.title(self.title)
        icono = os.path.abspath(self.icon)
        root.iconbitmap(icono)
        ancho = 600
        alto = 300
        xVentana = root.winfo_screenwidth() // 2 - ancho // 2 #winfo da el tamaño de la pantalla en ancho y en alto
        yVentana = root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana)+ "+" + str(yVentana)
        root.geometry(posicion)

        if self.resizable:
            root.resizable(0, 0)
        else:
            root.resizable(1, 1)

        continuarAyuda = Button(root, text='Ok', command=ayudaClose).grid(row=0)

    def cerrar(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()

ayuda = Ayuda()