
from os import cpu_count
from tkinter import *
from tkinter import ttk
import os.path
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
from ayuda import *
from principal import *


def ventanaPrincipal():
    bienvenida.cerrar()
    programa.cargar()
    programa.cargarMenus()
    programa.mostrar()

class Bienvenida:

    def __init__(self):
        self.title = "Letrero RGB Inicio"
        self.icon = "./iconos/firefly.ico"
        self.resizable = True
        self.root = Tk()

    def cargar(self):
        self.root.title(self.title)
        icono = os.path.abspath(self.icon)
        self.root.iconbitmap(icono)
        ancho = 600
        alto = 400
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2 #winfo da el tamaño de la pantalla en ancho y en alto
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana)+ "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background='white')

        if self.resizable:
            self.root.resizable(0, 0)
        else:
            self.root.resizable(1, 1)

        uama = Image.open("./recursos/uamazcL.png")
        uama= uama.resize((180, 60))
        uama = ImageTk.PhotoImage(uama)
        uamA = Label(self.root, image=uama, width=180, height=80, background='white')
        uamA.image = uama
        uamA.grid(row=0, column=0, sticky=W+S+N+E)

        cbi = Image.open("./recursos/cbi.png")
        cbi= cbi.resize((160, 60))
        cbi = ImageTk.PhotoImage(cbi)
        CBI = Label(self.root, image=cbi, width=160, height=80, background='white')
        CBI.image = cbi
        CBI.grid(row=0, column=2,sticky=W+S+N+E)

        titulo = Label(self.root, text="Insertar título", padx=60, font=("Verdana", 16), background='white').grid(row=0, column=1)

        self.root.grid_columnconfigure(0,weight=1)
        self.root.grid_columnconfigure(1,weight=1)
        self.root.grid_columnconfigure(2,weight=1)
        #self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_rowconfigure(1,weight=1)


        fondo = Frame(self.root, width=480, height=320, bg='lightblue')
        fondo.grid_propagate(False) #El frame no se ajusta al contenido
        fondo.grid(row=1, column=0, columnspan=3, sticky=W+S+N+E)

        rgbImagen = Image.open("./recursos/micro.jpg")
        #rgbImagen= rgbImagen.resize((800, 800))
        rgbImagen = ImageTk.PhotoImage(rgbImagen)
        fondoRGB = Label(fondo, image=rgbImagen, background='white')
        fondoRGB.image = rgbImagen
        fondoRGB.grid(row=0, column=0, rowspan=5, columnspan=3, sticky="ewns")

        fondo.winfo_height
        fondo.winfo_width

        fondo.grid_columnconfigure(0,weight=1)
        fondo.grid_columnconfigure(1,weight=1)
        fondo.grid_columnconfigure(2,weight=1)
        fondo.grid_rowconfigure(0,weight=1)
        fondo.grid_rowconfigure(1,weight=1)
        fondo.grid_rowconfigure(2,weight=1)
        fondo.grid_rowconfigure(3,weight=1)
        fondo.grid_rowconfigure(4,weight=1)

        imgAyuda=Image.open("./iconos/interrogacion.png")
        imgAyuda = imgAyuda.resize((20, 20))
        imgAyuda = ImageTk.PhotoImage(imgAyuda)
        botonAyuda = Button(fondo, image=imgAyuda, text="Ayuda  ", compound="right", command=ventanaAyuda)
        botonAyuda.grid(row=4, column=0, ipadx=10)
        botonAyuda.image = imgAyuda

        imgContinuar=Image.open("./iconos/arrow.png")
        imgContinuar = imgContinuar.resize((20, 20))
        imgContinuar = ImageTk.PhotoImage(imgContinuar)
        botonContinuar = Button(fondo, image=imgContinuar, text="Continuar  ", compound="right", command=ventanaPrincipal)
        botonContinuar.grid(row=4, column=1)
        botonContinuar.image = imgContinuar

        imgQuit=Image.open("./iconos/quit.jpg")
        imgQuit = imgQuit.resize((20, 20))
        imgQuit = ImageTk.PhotoImage(imgQuit)
        botonSalir = Button(fondo, image=imgQuit, text="Salir  ", compound="right", command=self.cerrar)
        botonSalir.grid(row=4, column=2, ipadx=10)
        botonSalir.image = imgQuit


    def cerrar(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()


bienvenida = Bienvenida()

bienvenida.cargar()
bienvenida.mostrar()
