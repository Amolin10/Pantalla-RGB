from os import lseek
import os.path
from ayuda import *
#from opciones import Opciones
from tkinter import *
from PIL import Image, ImageTk
from opciones import Opciones
from tkinter import messagebox
from tkinter import filedialog
from datos import Datos

#############################Bienvenida####################################
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
        ancho = 620
        alto = 400
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2  # winfo da el tamaño de la pantalla en ancho y en alto
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana) + "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background='white')

        if self.resizable:
            self.root.resizable(0, 0)
        else:
            self.root.resizable(1, 1)

        uama = Image.open("./recursos/uamazcL.png")
        uama = uama.resize((180, 60))
        uama = ImageTk.PhotoImage(uama)
        uamA = Label(self.root, image=uama, width=180, height=60, background='white')
        uamA.image = uama
        uamA.grid(row=0, column=0, sticky=W + S + N + E)

        cbi = Image.open("./recursos/cbi.png")
        cbi = cbi.resize((180, 60))
        cbi = ImageTk.PhotoImage(cbi)
        CBI = Label(self.root, image=cbi, width=180, height=60, background='white')
        CBI.image = cbi
        CBI.grid(row=0, column=2, sticky=W + S + N + E)

        titulo = Label(self.root, text="Insertar título", padx=55, font=("Verdana", 16), background='white').grid(row=0, column=1)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        # self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        fondo = Frame(self.root, width=480, height=320, bg='lightblue')
        fondo.grid_propagate(False)  # El frame no se ajusta al contenido
        fondo.grid(row=1, column=0, columnspan=3, sticky=W + S + N + E)

        rgbImagen = Image.open("./recursos/micro.jpg")
        # rgbImagen= rgbImagen.resize((800, 800))
        rgbImagen = ImageTk.PhotoImage(rgbImagen)
        fondoRGB = Label(fondo, image=rgbImagen, background='white')
        fondoRGB.image = rgbImagen
        fondoRGB.grid(row=0, column=0, rowspan=5, columnspan=3, sticky="ewns")

        # fondo.winfo_height
        # fondo.winfo_width

        fondo.grid_columnconfigure(0, weight=1)
        fondo.grid_columnconfigure(1, weight=1)
        fondo.grid_columnconfigure(2, weight=1)
        fondo.grid_rowconfigure(0, weight=1)
        fondo.grid_rowconfigure(1, weight=1)
        fondo.grid_rowconfigure(2, weight=1)
        fondo.grid_rowconfigure(3, weight=1)
        fondo.grid_rowconfigure(4, weight=1)

        imgAyuda = Image.open("./iconos/interrogacion.png")
        imgAyuda = imgAyuda.resize((20, 20))
        imgAyuda = ImageTk.PhotoImage(imgAyuda)
        botonAyuda = Button(fondo, image=imgAyuda, text="Ayuda  ", compound="right", command=ventanaAyuda)
        botonAyuda.grid(row=4, column=0, ipadx=10)
        botonAyuda.image = imgAyuda

        imgContinuar = Image.open("./iconos/arrow.png")
        imgContinuar = imgContinuar.resize((20, 20))
        imgContinuar = ImageTk.PhotoImage(imgContinuar)
        botonContinuar = Button(fondo, image=imgContinuar, text="Continuar  ", compound="right", command=self.continuarOpciones)
        botonContinuar.grid(row=4, column=1)
        botonContinuar.image = imgContinuar

        imgQuit = Image.open("./iconos/quit.jpg")
        imgQuit = imgQuit.resize((20, 20))
        imgQuit = ImageTk.PhotoImage(imgQuit)
        botonSalir = Button(fondo, image=imgQuit, text="Salir  ", compound="right", command=self.cerrar)
        botonSalir.grid(row=4, column=2, ipadx=10)
        botonSalir.image = imgQuit

    def cerrar(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()

    def continuarOpciones(self):
        self.cerrar()
        opciones = Opciones()
        opciones.cargar()
        opciones.mostrar()
#######################Termina Bienvenida################################


#######################Inicia Opciones###################################        
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

        imgSalir= Image.open('./iconos/regresar.png')
        imgSalir= imgSalir.resize((40, 40))
        imgSalir= ImageTk.PhotoImage(imgSalir)
        botonSalir = Button(self.root, image=imgSalir, text="Regresar  ", width=350, compound="right",
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
        #from configuracion import Configuracion
        configuracion = Configuracion()
        configuracion.cargar()
        configuracion.cargarMenus()
        configuracion.mostrar()

    def salir(self):
        self.cerrar()
        bienvenida = Bienvenida()
        bienvenida.cargar()
        bienvenida.mostrar()
########################Termina Opciones#####################################


########################Inicia Configuración#################################
class Configuracion:

    def __init__(self):
        self.imagen_ruta = ''
        self.opcion_efecto = None
        self.minutos = 0
        self.segundos = 0
        
        self.title = "Letrero RGB"
        self.icon = "./iconos/firefly.ico"
        self.resizable = True
        self.root = "Tk()"
        self.colorFondo = '#E2EFFF'
        

    def cargar(self):
        self.root = Tk()
        self.root.title(self.title)
        icono = os.path.abspath(self.icon)
        self.root.iconbitmap(icono)
        ancho = 1450
        alto = 830
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2  # winfo da el tamaño de la pantalla en ancho y en alto
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana) + "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background=self.colorFondo)

        if self.resizable:
            self.root.resizable(1, 1)
        else:
            self.root.resizable(0, 0)

        uama = Image.open("./recursos/uamazc.jpg")
        uama = uama.resize((280, 110))
        uama = ImageTk.PhotoImage(uama)
        uamA = Label(self.root, image=uama, width=260, height=80, padx=100, background='white')
        uamA.image = uama
        uamA.grid(row=0, column=0, sticky='ewns')

        electronica = Image.open("./recursos/electronica.jpg")
        electronica = electronica.resize((240, 120))
        electronica = ImageTk.PhotoImage(electronica)
        electronicaLabel = Label(self.root, image=electronica, width=220, height=80, padx=100, background='white')
        electronicaLabel.image = electronica
        electronicaLabel.grid(row=0, column=1, columnspan=3, sticky='ewns')

        cbi = Image.open("./recursos/cbi.png")
        cbi = cbi.resize((240, 120))
        cbi = ImageTk.PhotoImage(cbi)
        CBI = Label(self.root, image=cbi, width=220, height=80, padx=100, background='white')
        CBI.image = cbi
        CBI.grid(row=0, column=4, sticky='ewns')

        titulo = Label(self.root, text="Insertar título", font=("Verdana", 28), relief="groove", background='#184B6C',
                       fg='white').grid(row=1, column=0, columnspan=5, sticky='ewns')
        texto = Label(self.root, text="Configurar imagen para mostrar en la pantalla RGB", relief='groove',
                      font=("Verdana", 22), background='#2980B9')
        texto.grid(row=2, column=0, columnspan=5, sticky="ewns")
        Label(self.root, text="", background=self.colorFondo).grid(row=3, column=0, columnspan=5, pady=5)

        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=4, column=0, columnspan=5, sticky="ews")
        ttk.Separator(self.root, orient=VERTICAL).grid(row=5, column=2, rowspan=5, sticky="ns")
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=7, column=3, columnspan=2, sticky="ewn")
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=10, column=0, columnspan=5, sticky="ewn")

        imagenFrame = Frame(self.root, background=self.colorFondo, pady=10)
        Label(imagenFrame, text="Selecciona una imagen para\nmostrar en la pantalla RGB", font=("verdana", 18), padx=10,
              background=self.colorFondo).grid(row=0, column=0, sticky="n")
        imgImagen = Image.open("./iconos/imagen.png")
        imgImagen = imgImagen.resize((30, 30))
        imgImagen = ImageTk.PhotoImage(imgImagen)
        botonCargar = Button(imagenFrame, text="Cargar imagen   ", image=imgImagen, compound="right",
                             font=("verdana", 14), command=lambda: self.selecImagen(imagenFrame))
        botonCargar.grid(row=1, column=0, pady=30)
        botonCargar.image = imgImagen

        Label(imagenFrame, height=16, width=100, background=self.colorFondo).grid(column=0, row=2, sticky=N)

        imagenFrame.grid_columnconfigure(0, weight=1)
        # imagenFrame.rowconfigure(0, weight=1)
        imagenFrame.rowconfigure(1, weight=1)
        imagenFrame.rowconfigure(2, weight=1)
        imagenFrame.grid(row=6, column=0, columnspan=2, rowspan=5, sticky="ns", pady=20)

        parametros = Frame(self.root, background=self.colorFondo)
       
        ########Poner una variable a los radiobutons##########################

        self.opcion_efecto = StringVar()
        self.opcion_efecto.set(None)

        Label(parametros, text="Selecciona el efecto de entrada de la imagen", font=("Verdana", 18), background=self.colorFondo).grid(column=0, row=0, columnspan=3)
        
        Radiobutton(parametros, text="Instantaneo", font=("verdana", 14), variable=self.opcion_efecto, value='Instantaneo.py', background=self.colorFondo).grid(column=0, row=1)
        Radiobutton(parametros, text="De abajo a arriba", font=("verdana", 14), variable=self.opcion_efecto, value='AbajoArriba.py', background=self.colorFondo, padx=20).grid(column=1, row=1, sticky="ew")
        Radiobutton(parametros, text="Aleatorio", font=("verdana", 14), variable=self.opcion_efecto, value='Aleatorio.py', background=self.colorFondo).grid(column=2, row=1, sticky="e")
        Radiobutton(parametros, text="De derecha a izquierda", font=("verdana", 14), variable=self.opcion_efecto, value = 'DerechaIzquierda.py', background=self.colorFondo).grid(column=0, row=2, sticky="e")
        Radiobutton(parametros, text="De arriba a abajo", font=("verdana", 14), variable=self.opcion_efecto, value='ArribaAbajo.py', background=self.colorFondo).grid(column=2, row=2, sticky="w")
        
        Label(parametros, text="", background=self.colorFondo).grid(column=0, row=3, columnspan=3)
        parametros.rowconfigure(0, weight=1)
        parametros.rowconfigure(1, weight=1)
        parametros.rowconfigure(2, weight=1)
        parametros.rowconfigure(3, weight=1)
        parametros.grid(column=3, row=5, columnspan=2, rowspan=2, sticky='ns')

        tiempo = Frame(self.root, background=self.colorFondo)
        Label(tiempo, text="Seleccione el tiempo de desplegado de la imagen", font=("Verdana", 18), pady=14,
              background=self.colorFondo).grid(column=0, row=0, columnspan=2)
        
        self.minutos = StringVar()
        #self.minutos.set('0')
        
        Label(tiempo, text="minutos:", font=("verdana", 14), background=self.colorFondo).grid(column=0, row=1, sticky="w")
        minutosBox = ttk.Spinbox(tiempo, from_=0, to=4, increment=1, state="readonly", font=("verdana", 14), textvariable=self.minutos)
        minutosBox.grid(column=0, row=2, sticky='wn', pady=5)
        
        self.segundos = StringVar()
        #self.segundos.set('0')
        
        Label(tiempo, text="segundos:", font=("verdana", 14), background=self.colorFondo).grid(column=1, row=1, sticky="w")
        segundosBox = ttk.Spinbox(tiempo, from_=0, to=59, increment=1, state="readonly", font=("verdana", 14), textvariable=self.segundos)
        segundosBox.grid(column=1, row=2, sticky='wn', pady=5)
        # Label(tiempo, text="", background="white").grid(column=0, row=3, columnspan=3)
        tiempo.grid(row=8, column=3, columnspan=2, rowspan=2, sticky="ns")
        tiempo.grid_rowconfigure(0, weight=1)
        tiempo.grid_rowconfigure(1, weight=1)
        tiempo.grid_rowconfigure(2, weight=1)

        imgRegresar = Image.open("./iconos/regresar.png")
        imgRegresar = imgRegresar.resize((30, 30))
        imgRegresar = ImageTk.PhotoImage(imgRegresar)
        botonRegresar = Button(self.root, text="Regresar  ", image=imgRegresar, compound="right", font=("verdana", 14),
                               command=self.regresar)
        botonRegresar.grid(column=0, row=11, pady=15, sticky='n')
        botonRegresar.image = imgRegresar

        imgAgregar = Image.open("./iconos/imagen.png")
        imgAgregar = imgAgregar.resize((30, 30))
        imgAgregar = ImageTk.PhotoImage(imgAgregar)
        botonAgregar = Button(self.root, text="Agregar otra imagen  ", image=imgAgregar, compound="right",
                              font=("verdana", 14), command=self.agregar)
        botonAgregar.grid(column=1, row=11, pady=15, sticky='n')
        botonAgregar.image = imgAgregar

        imgVisualizar = Image.open("./iconos/visualizar.png")
        imgVisualizar = imgVisualizar.resize((30, 30))
        imgVisualizar = ImageTk.PhotoImage(imgVisualizar)
        botonVisualizar = Button(self.root, text="Visualizar  ", image=imgVisualizar, compound="right",
                                 font=("verdana", 14), command=self.visualizar)
        botonVisualizar.grid(column=3, row=11, pady=15, sticky='n')
        botonVisualizar.image = imgVisualizar

        imgTerminar = Image.open("./iconos/arrow.png")
        imgTerminar = imgTerminar.resize((30, 30))
        imgTerminar = ImageTk.PhotoImage(imgTerminar)
        botonTerminar = Button(self.root, text="Resumen de la configuración  ", image=imgTerminar, compound="right", font=("verdana", 14),
                               command=self.terminar)
        botonTerminar.grid(column=4, row=11, pady=15, sticky='n')
        botonTerminar.image = imgTerminar

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        # self.root.grid_columnconfigure(2,weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)

        self.root.grid_rowconfigure(0, weight=1)
        # self.root.grid_rowconfigure(1,weight=1)
        # self.root.grid_rowconfigure(2,weight=1)
        # self.root.grid_rowconfigure(3,weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(8, weight=1)
        # self.root.grid_rowconfigure(9,weight=1)

    def selecImagen(self, imagenFrame):
        archivo = filedialog.askopenfilename(filetypes=[('Archivos de imagen', '*.jpg *.png *.jpeg *.ppm')])

        if archivo is not None:
            # Imagen de entrada
            imagenEntrada = Image.open(archivo)
            ancho, alto = imagenEntrada.size
            imagenEntrada = imagenEntrada.resize((640, 240))  # 128x48
            ImagenEntrada = ImageTk.PhotoImage(imagenEntrada)
            imagenOriginal = Label(imagenFrame, image=ImagenEntrada)
            imagenOriginal.image = ImagenEntrada
            imagenOriginal.grid(column=0, row=2, sticky=N)
            imagenOriginal.config(relief="solid")
            self.imagen_ruta = archivo

    def cargarMenus(self):

        miMenu = Menu(self.root)

        miMenu.add_command(label="Ayuda", command=ventanaAyuda)
        miMenu.add_command(label="Acerca de", command=self.informacion)

    def informacion(self):
        messagebox.showinfo("Acerca de", "Interfaz para configurar tablero RGB.\n\nVersión: ......")

    def destruir(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()

    def agregar(self):
        tiempo = (int(self.minutos.get()) * 60) + int(self.segundos.get())
        print(f'Imagen: {self.imagen_ruta}\n Efecto: {self.opcion_efecto.get()}\n Tiempo: {tiempo}')
        datos = Datos(len(lista_configuracion), self.imagen_ruta, self.opcion_efecto.get(), tiempo)
        lista_configuracion.append(datos)
        print(lista_configuracion)

    def regresar(self):
        self.destruir()
        opciones = Opciones()
        opciones.cargar()
        opciones.mostrar()


    def visualizar(self):
        #visualizar = Visualizar()
        #visualizar.mostrar()  # Pantalla de visualizar
        pass

    def terminar(self):
        self.destruir()
        resumen = Resumen()
        resumen.cargar()
        resumen.mostrar()

    def llenarListaMinutos(self):
        lista = []
        for i in range(5):
            lista.append(str(i))
        return lista

    def llenarListaSegundos(self):
        lista = []
        for i in range(60):
            lista.append(str(i))
        return lista
########################Termina Configuración################################# 


########################Resumen#################################
class Resumen:

    def __init__(self):
        self.title = "Letrero RGB"
        self.icon = "./iconos/firefly.ico"
        self.resizable = True
        self.root = "Tk()"

    def cargar(self):
        self.root = Tk()
        self.root.title(self.title)
        icono = os.path.abspath(self.icon)
        self.root.iconbitmap(icono)
        ancho = 1000
        alto = 650
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2 #winfo da el tamaño de la pantalla en ancho y en alto
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana)+ "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background='#E2EFFF')

        if self.resizable:
            self.root.resizable(1, 1)
        else:
            self.root.resizable(0, 0)           

        uama = Image.open("./recursos/uamazc.jpg")
        uama= uama.resize((260, 100))
        uama = ImageTk.PhotoImage(uama)
        uamA = Label(self.root, image=uama, width=260, height=100, padx=100, background='white')
        uamA.image = uama
        uamA.grid(row=0, column=0, sticky='ewns')

        electronica = Image.open("./recursos/electronica.jpg")
        electronica= electronica.resize((220, 100))
        electronica = ImageTk.PhotoImage(electronica)
        electronicaLabel = Label(self.root, image=electronica, width=220, height=100, padx=100, background='white')
        electronicaLabel.image = electronica
        electronicaLabel.grid(row=0, column=1, columnspan=3, sticky='ewns')

        cbi = Image.open("./recursos/cbi.png")
        cbi= cbi.resize((220, 100))
        cbi = ImageTk.PhotoImage(cbi)
        CBI = Label(self.root, image=cbi, width=220, height=100, padx=100, background='white')
        CBI.image = cbi
        CBI.grid(row=0, column=4, sticky='ewns')

        titulo = Label(self.root, text="Insertar título", font=("Verdana", 28), relief="groove", background='#184B6C', fg='white').grid(row=1, column=0, columnspan=5, sticky='ewns')
        texto = Label(self.root, text="Resumen de la configuración", relief='groove',font=("Verdana", 22), background='#2980B9')
        texto.grid(row=2, column=0, columnspan=5, sticky="ewns")
        Label(self.root, text="", background='#E2EFFF').grid(row=3, column=0, columnspan=5, pady=5)
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=4, column=0, columnspan=5, sticky="ews")

        resumenFrame = LabelFrame(self.root, text='Resumen de la configuración', background='white')
        resumenFrame.grid(row=5, column=0, rowspan=5, columnspan=5)

        imgUSB=Image.open("./iconos/usb.jpg")
        imgUSB = imgUSB.resize((30, 30))
        imgUSB = ImageTk.PhotoImage(imgUSB)
        botonUSB = Button(self.root, image=imgUSB, text="Guardar en dispositivo\nde almacenamiento", compound="bottom", font=("Verdana", 12), background='white', activebackground="#999999")
        botonUSB.grid(row=9, column=2,  padx=15, pady=15, sticky="ws")
        botonUSB.image = imgUSB

        imgSave=Image.open("./iconos/save.ico")
        imgSave = imgSave.resize((30, 30))
        imgSave = ImageTk.PhotoImage(imgSave)
        botonSave = Button(self.root, image=imgSave, text="Guardar", compound="bottom", font=("Verdana", 12), background='white', activebackground="#999999")
        botonSave.grid(row=9, column=4, ipadx=20, padx=15, pady=15, sticky="ws")
        botonSave.image = imgSave


        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        #self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        self.root.grid_rowconfigure(6,weight=1)
    
    def destruir(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()
########################Termina Resumen#################################


########################Configuracion Resumen#################################
class ConfiguracionResumen:
    
    def __init__(self):
        self.title = "Letrero RGB"
        self.icon = "./iconos/firefly.ico"
        self.resizable = True
        self.root = "Tk()"
        self.colorFondo = '#E2EFFF'

    def cargar(self):
        self.root = Tk()
        self.root.title(self.title)
        icono = os.path.abspath(self.icon)
        self.root.iconbitmap(icono)
        ancho = 1450
        alto = 830
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2  # winfo da el tamaño de la pantalla en ancho y en alto
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana) + "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background=self.colorFondo)

        if self.resizable:
            self.root.resizable(1, 1)
        else:
            self.root.resizable(0, 0)

        uama = Image.open("./recursos/uamazc.jpg")
        uama = uama.resize((280, 110))
        uama = ImageTk.PhotoImage(uama)
        uamA = Label(self.root, image=uama, width=260, height=80, padx=100, background='white')
        uamA.image = uama
        uamA.grid(row=0, column=0, sticky='ewns')

        electronica = Image.open("./recursos/electronica.jpg")
        electronica = electronica.resize((240, 120))
        electronica = ImageTk.PhotoImage(electronica)
        electronicaLabel = Label(self.root, image=electronica, width=220, height=80, padx=100, background='white')
        electronicaLabel.image = electronica
        electronicaLabel.grid(row=0, column=1, columnspan=3, sticky='ewns')

        cbi = Image.open("./recursos/cbi.png")
        cbi = cbi.resize((240, 120))
        cbi = ImageTk.PhotoImage(cbi)
        CBI = Label(self.root, image=cbi, width=220, height=80, padx=100, background='white')
        CBI.image = cbi
        CBI.grid(row=0, column=4, sticky='ewns')

        titulo = Label(self.root, text="Insertar título", font=("Verdana", 28), relief="groove", background='#184B6C',
                       fg='white').grid(row=1, column=0, columnspan=5, sticky='ewns')
        texto = Label(self.root, text="Configurar imagen para mostrar en la pantalla RGB", relief='groove',
                      font=("Verdana", 22), background='#2980B9')
        texto.grid(row=2, column=0, columnspan=5, sticky="ewns")
        Label(self.root, text="", background=self.colorFondo).grid(row=3, column=0, columnspan=5, pady=5)

        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=4, column=0, columnspan=5, sticky="ews")
        ttk.Separator(self.root, orient=VERTICAL).grid(row=5, column=2, rowspan=5, sticky="ns")
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=7, column=3, columnspan=2, sticky="ewn")
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=10, column=0, columnspan=5, sticky="ewn")

        imagenFrame = Frame(self.root, background=self.colorFondo, pady=10)
        Label(imagenFrame, text="Selecciona una imagen para\nmostrar en la pantalla RGB", font=("verdana", 18), padx=10,
              background=self.colorFondo).grid(row=0, column=0, sticky="n")
        imgImagen = Image.open("./iconos/imagen.png")
        imgImagen = imgImagen.resize((30, 30))
        imgImagen = ImageTk.PhotoImage(imgImagen)
        botonCargar = Button(imagenFrame, text="Cargar imagen   ", image=imgImagen, compound="right",
                             font=("verdana", 14), command=lambda: self.selecImagen(imagenFrame))
        botonCargar.grid(row=1, column=0, pady=30)
        botonCargar.image = imgImagen

        Label(imagenFrame, height=16, width=100, background=self.colorFondo).grid(column=0, row=2, sticky=N)

        imagenFrame.grid_columnconfigure(0, weight=1)
        # imagenFrame.rowconfigure(0, weight=1)
        imagenFrame.rowconfigure(1, weight=1)
        imagenFrame.rowconfigure(2, weight=1)
        imagenFrame.grid(row=6, column=0, columnspan=2, rowspan=5, sticky="ns", pady=20)

        parametros = Frame(self.root, background=self.colorFondo)
        ########Poner una variable a los radiobutons##########################
        Label(parametros, text="Selecciona el efecto de entrada de la imagen", font=("Verdana", 18),
              background=self.colorFondo).grid(column=0, row=0, columnspan=3)
        Radiobutton(parametros, text="Instantaneo", font=("verdana", 14), background=self.colorFondo).grid(column=0,
                                                                                                           row=1, )
        Radiobutton(parametros, text="De abajo a arriba", font=("verdana", 14), background=self.colorFondo,
                    padx=20).grid(column=1, row=1, sticky="ew")
        Radiobutton(parametros, text="Aleatorio", font=("verdana", 14), background=self.colorFondo).grid(column=2,
                                                                                                         row=1,
                                                                                                         sticky="e")
        Radiobutton(parametros, text="De derecha a izquierda", font=("verdana", 14), background=self.colorFondo).grid(
            column=0, row=2, sticky="e")
        Radiobutton(parametros, text="De arriba a abajo", font=("verdana", 14), background=self.colorFondo).grid(
            column=2, row=2, sticky="w")
        Label(parametros, text="", background=self.colorFondo).grid(column=0, row=3, columnspan=3)
        parametros.rowconfigure(0, weight=1)
        parametros.rowconfigure(1, weight=1)
        parametros.rowconfigure(2, weight=1)
        parametros.rowconfigure(3, weight=1)
        parametros.grid(column=3, row=5, columnspan=2, rowspan=2, sticky='ns')

        tiempo = Frame(self.root, background=self.colorFondo)
        Label(tiempo, text="Seleccione el tiempo de desplegado de la imagen", font=("Verdana", 18), pady=14,
              background=self.colorFondo).grid(column=0, row=0, columnspan=2)
        
        Label(tiempo, text="minutos:", font=("verdana", 14), background=self.colorFondo).grid(column=0, row=1,                                                                                      sticky="w")
        minutosBox = ttk.Spinbox(tiempo, from_=0, to=4, increment=1, state="readonly", font=("verdana", 14))
        minutosBox.grid(column=0, row=2, sticky='wn', pady=5)
        
        Label(tiempo, text="segundos:", font=("verdana", 14), background=self.colorFondo).grid(column=1, row=1, sticky="w")
        segundosBox = ttk.Spinbox(tiempo, from_=0, to=59, increment=1, state="readonly", font=("verdana", 14))
        segundosBox.grid(column=1, row=2, sticky='wn', pady=5)
        # Label(tiempo, text="", background="white").grid(column=0, row=3, columnspan=3)
        tiempo.grid(row=8, column=3, columnspan=2, rowspan=2, sticky="ns")
        tiempo.grid_rowconfigure(0, weight=1)
        tiempo.grid_rowconfigure(1, weight=1)
        tiempo.grid_rowconfigure(2, weight=1)

        imgVisualizar = Image.open("./iconos/visualizar.png")
        imgVisualizar = imgVisualizar.resize((30, 30))
        imgVisualizar = ImageTk.PhotoImage(imgVisualizar)
        botonVisualizar = Button(self.root, text="Visualizar  ", image=imgVisualizar, compound="right",
                                 font=("verdana", 14), command=self.visualizar)
        botonVisualizar.grid(column=3, row=11, pady=15, sticky='n')
        botonVisualizar.image = imgVisualizar

        imgTerminar = Image.open("./iconos/arrow.png")
        imgTerminar = imgTerminar.resize((30, 30))
        imgTerminar = ImageTk.PhotoImage(imgTerminar)
        botonTerminar = Button(self.root, text="Resumen de la configuración  ", image=imgTerminar, compound="right", font=("verdana", 14),
                               command=self.terminar)
        botonTerminar.grid(column=4, row=11, pady=15, sticky='n')
        botonTerminar.image = imgTerminar

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        # self.root.grid_columnconfigure(2,weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)

        self.root.grid_rowconfigure(0, weight=1)
        # self.root.grid_rowconfigure(1,weight=1)
        # self.root.grid_rowconfigure(2,weight=1)
        # self.root.grid_rowconfigure(3,weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(8, weight=1)
        # self.root.grid_rowconfigure(9,weight=1)

    def selecImagen(self, imagenFrame):
        archivo = filedialog.askopenfilename(filetypes=[('Archivos de imagen', '*.jpg *.png *.jpeg *.ppm')])

        if archivo is not None:
            # Imagen de entrada
            imagenEntrada = Image.open(archivo)
            ancho, alto = imagenEntrada.size
            imagenEntrada = imagenEntrada.resize((640, 240))  # 128x48
            ImagenEntrada = ImageTk.PhotoImage(imagenEntrada)
            imagenOriginal = Label(imagenFrame, image=ImagenEntrada)
            imagenOriginal.image = ImagenEntrada
            imagenOriginal.grid(column=0, row=2, sticky=N)
            imagenOriginal.config(relief="solid")

    def cargarMenus(self):

        miMenu = Menu(self.root)

        miMenu.add_command(label="Ayuda", command=ventanaAyuda)
        miMenu.add_command(label="Acerca de", command=self.informacion)

    def informacion(self):
        messagebox.showinfo("Acerca de", "Interfaz para configurar tablero RGB.\n\nVersión: ......")

    def destruir(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()

    def agregar(self):
        print("Hola")

    def regresar(self):
        self.destruir()
        opciones = Opciones()
        opciones.cargar()
        opciones.mostrar()

    def visualizar(self):
        #visualizar = Visualizar()
        #visualizar.mostrar()  # Pantalla de visualizar
        pass

    def terminar(self):
        self.destruir()
        resumen = Resumen()
        resumen.cargar()
        resumen.mostrar()

    def llenarListaMinutos(self):
        lista = []
        for i in range(5):
            lista.append(str(i))
        return lista

    def llenarListaSegundos(self):
        lista = []
        for i in range(60):
            lista.append(str(i))
        return lista
########################Termina Configuracion Resumen#################################


########################Main###########################

#bienvenida = Bienvenida()
#bienvenida.cargar()
#bienvenida.mostrar()

lista_configuracion = []

configuracion = Configuracion()
configuracion.cargar()
configuracion.mostrar()


