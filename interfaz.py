
from os import cpu_count
from tkinter import *
import os.path
from PIL import Image,ImageTk
from tkinter import messagebox
#from tkinter import filedialog
from tkinter import filedialog


def ayuda4():
    ayuda.cerrar()
    #programa.cargar()
    #programa.cargarMenus()
    #programa.mostrar()

def ayuda3():
    ayuda.cargar()
    ayuda.mostrar()

def ayuda2():
    #bienvenida.cerrar()
    ayuda.cargar()
    ayuda.mostrar()

def ventana2():
    bienvenida.cerrar()
    programa.cargar()
    programa.cargarMenus()
    programa.mostrar()

def informacion():
    messagebox.showinfo("Información", "Interfaz para configurar tablero RGB.\n\nCreado por: ......")
    #info.cargar()
    #info.mostrar()

class Bienvenida:

    def __init__(self):
        self.title = "Letrero RGB Inicio"
        self.icon = "firefly.ico"
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
            self.root.resizable(1, 1)
        else:
            self.root.resizable(0, 0)

        uama = Image.open("uamazcL.png")
        uama= uama.resize((180, 60))
        uama = ImageTk.PhotoImage(uama)
        uamA = Label(self.root, image=uama, width=180, height=80, background='white')
        uamA.image = uama
        uamA.grid(row=0, column=0, sticky=W+S+N+E)


        cbi = Image.open("cbi.png")
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

        rgbImagen = Image.open("micro.jpg")
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
        botonAyuda = Button(fondo, image=imgAyuda, text="Ayuda  ", compound="right", command=ayuda2)
        botonAyuda.grid(row=4, column=0, ipadx=10)
        botonAyuda.image = imgAyuda

        imgContinuar=Image.open("./iconos/arrow.png")
        imgContinuar = imgContinuar.resize((20, 20))
        imgContinuar = ImageTk.PhotoImage(imgContinuar)
        botonContinuar = Button(fondo, image=imgContinuar, text="Continuar  ", compound="right", command=ventana2)
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

        continuarAyuda = Button(root, text='Ok', command=ayuda4).grid(row=0)

    def cerrar(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()

class Interfaz:

    def __init__(self):
        self.title = "Letrero RGB"
        self.icon = "firefly.ico"
        self.resizable = True
        self.root = "Tk()"

    def cargar(self):
        self.root = Tk()
        self.root.title(self.title)
        icono = os.path.abspath(self.icon)
        self.root.iconbitmap(icono)
        ancho = 800
        alto = 600
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2 #winfo da el tamaño de la pantalla en ancho y en alto
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana)+ "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background='white')

        if self.resizable:
            self.root.resizable(1, 1)
        else:
            self.root.resizable(0, 0)

        uama = Image.open("uamazc.jpg")
        uama= uama.resize((180, 80))
        uama = ImageTk.PhotoImage(uama)
        uamA = Label(self.root, image=uama, width=180, height=80, background='whitesmoke')
        uamA.image = uama
        uamA.grid(row=0, column=0, sticky='ewns')

        cbi = Image.open("cbi.png")
        cbi= cbi.resize((180, 80))
        cbi = ImageTk.PhotoImage(cbi)
        CBI = Label(self.root, image=cbi, width=180, height=80, background='whitesmoke')
        CBI.image = cbi
        CBI.grid(row=0, column=2, sticky='ewns')

        titulo = Label(self.root, text="Insertar título", font=("Verdana", 16), background='whitesmoke', padx=100).grid(row=0, column=1, sticky='ewns')
        
        Label(self.root, text="Seleccionar una imagen, tipo y tiempo de animación para mostrar en la pantalla RGB.", font=("Verdana", 10), pady=10, background='white').grid(row=1, column=0,columnspan=3)

        Label(self.root, text="Selecciona una imagen", font=("Verdana", 12), background='white').grid(row=2, column=0)
        Button(self.root, text="Cargar", command=self.selecImagen).grid(row=2, column=1, sticky=W)

        self.root.grid_columnconfigure(0,weight=1)
        self.root.grid_columnconfigure(1,weight=1)
        self.root.grid_columnconfigure(2,weight=1)
        #self.root.grid_rowconfigure(0,weight=1)
        #self.root.grid_rowconfigure(1,weight=1)
        #self.root.grid_rowconfigure(2,weight=1)
        self.root.grid_rowconfigure(3,weight=1)
        self.root.grid_rowconfigure(4,weight=1)



    
    def selecImagen(self):
        archivo = filedialog.askopenfilename(filetypes=[('Archivos de imagen', '*.jpg')])

        if archivo is not None:
            #Imagen de entrada
            imagenEntrada = Image.open(archivo)
            ancho, alto = imagenEntrada.size
            imagenEntrada = imagenEntrada.resize((360, 140))
            ImagenEntrada = ImageTk.PhotoImage(imagenEntrada)
            imagenOriginal = Label(self.root, image=ImagenEntrada)
            imagenOriginal.image = ImagenEntrada
            imagenOriginal.grid(row=3, column=1, sticky=N)

    def cargarMenus(self):

        miMenu = Menu(self.root)
        self.root.config(menu=miMenu)
        archivo = Menu(miMenu, tearoff=0)
        archivo.add_command(label="Nuevo")
        archivo.add_command(label="Abrir")
        archivo.add_separator()
        archivo.add_command(label="Guardar")
        archivo.add_command(label="Guardar como")
        archivo.add_separator()
        archivo.add_command(label="Salir", command=self.root.destroy)

        miMenu.add_cascade(label="Archivo", menu=archivo)
        miMenu.add_command(label="Ayuda", command=ayuda3)
        miMenu.add_command(label="Información", command=informacion)

    def destruir(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()



bienvenida = Bienvenida()
programa = Interfaz()
ayuda = Ayuda()
#info = Info()


bienvenida.cargar()
bienvenida.mostrar()
