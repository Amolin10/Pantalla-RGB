from os import cpu_count
#from principal import *
from tkinter import *
from tkinter import ttk
import os.path
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
from ayuda import *
#from interfaz import Bienvenida


class Opciones:
    def __init__(self):
        self.title = "Letrero RGB"
        self.icon = "./iconos/firefly.ico"
        self.resizable = True
        self.root = Tk()
        self.colorFondo = '#E2EFFF'

    def cargar(self):
        self.root.title(self.title)
        icono = os.path.abspath(self.icon)
        self.root.iconbitmap(icono)
        ancho = 770
        alto = 300
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2  # winfo da el tamaño de la pantalla en ancho y en alto
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana) + "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background=self.colorFondo)

        if self.resizable:
            self.root.resizable(0, 0)
        else:
            self.root.resizable(1, 1)

        imgNuevo = Image.open("./iconos/nuevo.jpg")
        imgNuevo = imgNuevo.resize((40, 40))
        imgNuevo = ImageTk.PhotoImage(imgNuevo)
        botonNuevo = Button(self.root, image=imgNuevo, text="Nuevo  ", compound="right", width=350,
                            font=("Verdana", 14), background='white', activebackground="#999999",
                            command=self.ventanaPrincipal)
        botonNuevo.grid(row=0, column=0, padx=15, sticky="ws")
        botonNuevo.image = imgNuevo

        imgConfig = Image.open("./iconos/engrane.png")
        imgConfig = imgConfig.resize((40, 40))
        imgConfig = ImageTk.PhotoImage(imgConfig)
        botonConfig = Button(self.root, image=imgConfig, text="Cargar configuración  ", width=350, compound="right",
                             background='white', activebackground="#999999", font=("Verdana", 14))
        botonConfig.grid(row=1, column=0, padx=50, sticky="w")
        botonConfig.image = imgConfig

        imgSalir= Image.open('./iconos/quit.jpg')
        imgSalir= imgSalir.resize((40, 40))
        imgSalir= ImageTk.PhotoImage(imgSalir)
        botonSalir = Button(self.root, image=imgSalir, text="Salir  ", width=350, compound="right",
                          background="white", activebackground="#999999", font=("Verdana", 14), command=self.salir)
        botonSalir.grid(row=2, column=0, padx=80, sticky="wn")
        botonSalir.image = imgSalir

        fondoImagen = Image.open("./recursos/computadora.png")
        fondoImagen = fondoImagen.resize((200, 200))
        fondoImagen = ImageTk.PhotoImage(fondoImagen)
        fondoOpciones = Label(self.root, image=fondoImagen, background=self.colorFondo)
        fondoOpciones.image = fondoImagen
        fondoOpciones.grid(row=0, column=1, rowspan=3, sticky="wns")

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

        # self.root.columnconfigure(0, weight=1)
        # self.root.columnconfigure(1, weight=1)
        # self.root.columnconfigure(2, weight=1)

    def cerrar(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()

    def ventanaPrincipal(self):
        self.cerrar()
        from principal import Interfaz
        programa = Interfaz()
        programa.cargar()
        programa.cargarMenus()
        programa.mostrar()

    def salir(self):
        self.cerrar()

#opciones = Opciones()
#opciones.cargar()
#opciones.mostrar()