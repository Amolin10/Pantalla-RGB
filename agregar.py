from os import cpu_count
from tkinter import *
from tkinter import ttk
import os.path
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
from ayuda import *
#from principal import Interfaz
from visualizar import * 
from resumen import *

class Agregar:

    def __init__(self):
        self.title = "Letrero RGB"
        self.icon = "./iconos/firefly.ico"
        self.resizable = True
        self.root = Tk()

    def cargar(self):
        self.root.title(self.title)
        icono = os.path.abspath(self.icon)
        self.root.iconbitmap(icono)
        ancho = 720
        alto = 300
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2 #winfo da el tamaño de la pantalla en ancho y en alto
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana)+ "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background='#E2EFFF')

        if self.resizable:
            self.root.resizable(0, 0)
        else:
            self.root.resizable(1, 1)

        
        imgAgregar=Image.open("./iconos/imagen.png")
        imgAgregar = imgAgregar.resize((40, 40))
        imgAgregar = ImageTk.PhotoImage(imgAgregar)
        botonAgregar = Button(self.root, image=imgAgregar, text="Agregar imagen ", compound="right", width=300, font=("Verdana", 14), background='white', activebackground="#999999" , command=self.ventanaPrincipal)
        botonAgregar.grid(row=0, column=0, padx=15, sticky="ws")
        botonAgregar.image = imgAgregar

        imgVizualizar=Image.open("./iconos/visualizar.png")
        imgVizualizar = imgVizualizar.resize((40, 40))
        imgVizualizar = ImageTk.PhotoImage(imgVizualizar)
        botonVizualizar = Button(self.root, image=imgVizualizar, text="Visualizar  ", compound="right", width=300, background='white', activebackground="#999999", font=("Verdana", 14), command=self.visualizar)
        botonVizualizar.grid(row=1, column=0, padx=50, sticky="w")
        botonVizualizar.image = imgVizualizar

        imgTerminar=Image.open('./iconos/arrow.png')
        imgTerminar = imgTerminar.resize((40, 40))
        imgTerminar = ImageTk.PhotoImage(imgTerminar)
        botonTerminar = Button(self.root, image=imgTerminar, text="Terminado  ", compound="right", width=300, background="white", activebackground="#999999", font=("Verdana", 14), command=self.resumen)
        botonTerminar.grid(row=2, column=0, padx=80, sticky="wn")
        botonTerminar.image = imgTerminar


        fondoImagen = Image.open("./recursos/computadora.png")
        fondoImagen= fondoImagen.resize((200, 200))
        fondoImagen = ImageTk.PhotoImage(fondoImagen)
        fondoOpciones = Label(self.root, image=fondoImagen, background='#E2EFFF')
        fondoOpciones.image = fondoImagen
        fondoOpciones.grid(row=0, column=1, rowspan=3, sticky="wns")


        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

    def cerrar(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()
    
    def visualizar(self):
        self.root.destroy()
        mostrar()

    def resumen(self):
        self.cerrar()
        resumen = Resumen()
        resumen.cargar()
        resumen.mostrar()

    def ventanaPrincipal(self):
        from principal import Interfaz
        self.cerrar()
        programa = Interfaz()
        programa.cargar()
        programa.cargarMenus()
        programa.mostrar()

#agregar = Agregar()
#agregar.cargar()
#agregar.mostrar()


#lista = [0, 1, 2, 3, 4]
#for count, value in enumerate(lista):
#    Label(self.root, text=count).grid(row=count)
#    Label(self.root, image=value.getImagen()).grid(row=count)
#    Label(self.root, text=value.getEfecto()).grid(row=count)
