from os import lseek
import os.path
from ayuda import *
from tkinter import *
from PIL import Image, ImageTk
from opciones import Opciones
from tkinter import messagebox
from tkinter import filedialog
from datos import Datos
    
from pygame import * 
import sys, pygame
from pygame.draw import line
from pygame.font import SysFont

############################# Bienvenida ####################################
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
        self.label_imagen = ''
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
        #self.label_imagen = Label(imagenFrame, background=self.colorFondo)
        #self.label_imagen.grid(column=0, row=2, sticky=N)
        
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
        
        Label(tiempo, text="minutos:", font=("verdana", 14), background=self.colorFondo).grid(column=0, row=1, sticky="we")
        minutosBox = ttk.Spinbox(tiempo, from_=0, to=4, increment=1, state="readonly", width=4, font=("verdana", 14), textvariable=self.minutos)
        minutosBox.grid(column=0, row=2, sticky='n', pady=5)
        
        self.segundos = StringVar()
        #self.segundos.set('0')
        
        Label(tiempo, text="segundos:", font=("verdana", 14), background=self.colorFondo).grid(column=1, row=1, sticky="we")
        segundosBox = ttk.Spinbox(tiempo, from_=0, to=59, increment=1, state="readonly", width=4, font=("verdana", 14), textvariable=self.segundos)
        segundosBox.grid(column=1, row=2, sticky='n', pady=5)
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
        botonAgregar = Button(self.root, text="Agregar imagen  ", image=imgAgregar, compound="right",
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
            imagenEntrada = imagenEntrada.resize((640, 240))  # 128x48
            ImagenEntrada = ImageTk.PhotoImage(imagenEntrada)
            self.label_imagen = Label(imagenFrame, background=self.colorFondo)
            #imagenOriginal = Label(imagenFrame, image=ImagenEntrada)
            self.label_imagen.config(image = ImagenEntrada)
            self.label_imagen.image = ImagenEntrada
            self.label_imagen.grid(column=0, row=2, sticky=N)
            self.label_imagen.config(relief="solid")
            self.imagen_ruta = archivo

    def cargarMenus(self):
        miMenu = Menu(self.root)
        miMenu.add_command(label="Ayuda", command=ventanaAyuda)
        miMenu.add_command(label="Acerca de", command=self.informacion)

    def informacion(self):
        messagebox.showinfo("Pantalla RGB", "Acerca de.\nInterfaz para configurar tablero RGB.\n\nVersión: ......")

    def destruir(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()

    def agregar(self):
        if (self.imagen_ruta == '' or self.opcion_efecto.get() == 'None' or self.minutos.get() == '' or self.segundos.get() == ''):
            messagebox.showwarning("Pantalla RGB", "Debe llenar todos los campos.")
        else:
            tiempo = (int(self.minutos.get()) * 60) + int(self.segundos.get())
            print(f'Imagen: {self.imagen_ruta}\n Efecto: {self.opcion_efecto.get()}\n Tiempo: {tiempo}')
            datos = Datos(len(lista_configuracion), self.imagen_ruta, self.opcion_efecto.get(), tiempo)
            lista_configuracion.append(datos)
            #print(lista_configuracion)
            self.limpiar_configuracion()
    
    def nombre_efecto(self, nombre):
        if (nombre == 'Instantaneo'):
            return 'Instantaneo.py'
        elif (nombre == 'De abajo a arriba'):
            return 'AbajoArriba.py'
        elif (nombre == 'Aleatorio'):
            return 'Aleatorio.py'
        elif (nombre == 'De derecha a izquierda'):
            return 'DerechaIzquierda.py'
        elif (nombre == 'De arriba a abajo'):
            return 'ArribaAbajo.py'
    
    def regresar(self):
        if len(lista_configuracion) > 0:
            decision = messagebox.askokcancel("Pantalla RGB", "Todos los cambios realizados serán borrados.")
            if(decision == True):
                self.destruir()
                lista_configuracion.clear()
                print(len(lista_configuracion))
                opciones = Opciones()
                opciones.cargar()
                opciones.mostrar()
                
        else:
            self.destruir()
            opciones = Opciones()
            opciones.cargar()
            opciones.mostrar()


    def visualizar(self):
        visualizar = Visualizar()
        visualizar.mostrar()  # Pantalla de visualizar
        pass

    def terminar(self):
        if len(lista_configuracion) == 0:
            messagebox.showwarning("Pantalla RGB", "La lista de configuración está vacía. \n Por favor inserte una configuración.")
        else:
            self.destruir()
            resumen = Resumen()
            resumen.cargar()
            resumen.llenar_tabla()
            resumen.mostrar()

    def limpiar_configuracion(self):
        self.imagen_ruta = ''
        self.label_imagen.config(image = None)
        self.label_imagen.config(relief="flat") 
        self.label_imagen.image = None   
        self.opcion_efecto.set(None)
        self.minutos.set("")
        self.segundos.set("")
    
    
########################Termina Configuración################################# 


########################Resumen#################################
class Resumen:

    def __init__(self):
        self.title = "Letrero RGB"
        self.icon = "./iconos/firefly.ico"
        self.resizable = True
        self.root = "Tk()"
        self.color_fondo = '#E2EFFF'
        self.tabla_frame = ''
        self.color_fondo_tabla = '#C0D5F0'

    def cargar(self):
        self.root = Tk()
        self.root.title(self.title)
        icono = os.path.abspath(self.icon)
        self.root.iconbitmap(icono)
        ancho = 1150
        alto = 800
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2 #winfo da el tamaño de la pantalla en ancho y en alto
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana)+ "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background=self.color_fondo)

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
        Label(self.root, text="", background=self.color_fondo).grid(row=3, column=0, columnspan=5, pady=5)
        
        #ttk.Separator(self.root, orient=HORIZONTAL).grid(row=4, column=0, columnspan=5, sticky="ews")
        
        self.tabla_frame = Frame(self.root, background=self.color_fondo_tabla, pady=20)
        self.tabla_frame.grid(row=5, column=0, columnspan=5, rowspan=2, sticky="nsew")
        opciones_frame = Frame(self.root, background=self.color_fondo, pady=10)
        opcion_editar = StringVar()
        opcion_editar.set(1)
        
        tam_lista = len(lista_configuracion)
        imagen_box = ttk.Spinbox(opciones_frame, from_=1, to=tam_lista, increment=1, state="readonly", width=4, font=("verdana", 12), textvariable=opcion_editar)
        imagen_box.grid(column=0, row=0, sticky="e", padx=10, ipady=4)
        
        #opcion_entry = Entry(opciones_frame, textvariable=opcion_editar, font=("Verdana", 12), width=10)
        #opcion_entry.grid(column=0, row=0, sticky="e", padx=10, ipady=4)
        
        Button(opciones_frame, text="Editar", font=("Verdana", 12), command=lambda: self.editar_opcion(opcion_editar.get())).grid(column=1, row=0, ipadx=10, sticky='w', padx=10)
        Label(opciones_frame, text= "Seleccione una imagen para editar", font=("Verdana", 12), background=self.color_fondo).grid(column=0, row=1, columnspan=2, pady=5)
        Button(opciones_frame, text="Visualizar\nConfiguración", font=("Verdana", 12), command=self.visualizar).grid(ipadx=10, column=3, row=0, rowspan=2, sticky='nes')
        opciones_frame.grid(row=7, column=0, columnspan=5, sticky="ews")
        
        opciones_frame.columnconfigure(0, weight=1)
        opciones_frame.columnconfigure(1, weight=1)
        opciones_frame.columnconfigure(2, weight=1)
        opciones_frame.columnconfigure(3, weight=1)
        opciones_frame.columnconfigure(4, weight=1)
        
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=8, column=0, columnspan=5, sticky="ews")
        
        imgSalir = Image.open("./iconos/quit.jpg")
        imgSalir = imgSalir.resize((30, 30))
        imgSalir = ImageTk.PhotoImage(imgSalir)
        botonSalir = Button(self.root, image=imgSalir, text="Salir   ", compound="right", font=("Verdana", 12), activebackground="#999999")
        botonSalir.grid(row=9, column=0, ipadx=20, padx=15, pady=15, sticky="es")
        botonSalir.image = imgSalir

        imgSave=Image.open("./iconos/save.ico")
        imgSave = imgSave.resize((30, 30))
        imgSave = ImageTk.PhotoImage(imgSave)
        botonSave = Button(self.root, image=imgSave, text="Guardar   ", compound="right", font=("Verdana", 12), activebackground="#999999", command=self.guardar_configuracion)
        botonSave.grid(row=9, column=4, ipadx=20, padx=15, pady=15, sticky="ws")
        botonSave.image = imgSave


        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        #self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
    
    def destruir(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()
        
    def editar_opcion(self, opcion_numero):
        self.destruir()
        configuracion_resumen = ConfiguracionResumen()
        configuracion_resumen.cargar()
        configuracion_resumen.llenar_configuracion(int(opcion_numero))
        configuracion_resumen.mostrar()
        
    def visualizar(self):
        pass
    
    def llenar_tabla(self):
        #print(f"""{lista_configuracion[0]}
        #{lista_configuracion[1]}
        #{lista_configuracion[2]}""")
        
        canvas = Canvas(self.tabla_frame, bg=self.color_fondo_tabla)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        #canvas.grid(column=0, row=0, sticky="ew")
        vsbar = Scrollbar(self.tabla_frame, orient=VERTICAL, command=canvas.yview) 
        vsbar.pack(side=RIGHT, fill=Y)
        #vsbar.grid(column=1, row=0, sticky='ns')
        canvas.configure(yscrollcommand=vsbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion= canvas.bbox("all")))
        
        contenedor_canvas = Frame(canvas, background=self.color_fondo_tabla, padx=150)   
        canvas.create_window((0,0), window=contenedor_canvas)
        #contenedor_canvas.grid(column=0, row=0) 
    
        ttk.Separator(contenedor_canvas, orient=HORIZONTAL).grid(row=0, column=1, columnspan=4, sticky="ews")
        Label(contenedor_canvas, text="Imagen", font=("Verdana", 14, 'bold'), background=self.color_fondo_tabla, padx=65).grid(row=1, column=1, pady=10)
        Label(contenedor_canvas, text="Vista", font=("Verdana", 14, 'bold'), background=self.color_fondo_tabla, padx=65).grid(row=1, column=2, pady=10)
        Label(contenedor_canvas, text="Efecto", font=("Verdana", 14, 'bold'), background=self.color_fondo_tabla, padx=65).grid(row=1, column=3, pady=10)
        Label(contenedor_canvas, text="Tiempo", font=("Verdana", 14, 'bold'), background=self.color_fondo_tabla, padx=65).grid(row=1, column=4, pady=10)
        ttk.Separator(contenedor_canvas, orient=HORIZONTAL).grid(row=2, column=1, columnspan=4, sticky="ews")
        ttk.Separator(contenedor_canvas, orient=VERTICAL).grid(row=1, column=0, sticky="nse", rowspan=2)
        ttk.Separator(contenedor_canvas, orient=VERTICAL).grid(row=1, column=5, sticky="nsw", rowspan=2)
        filas = 2
        for i, item in enumerate(lista_configuracion):
            indice = i + 1
            imagen = item.get_imagen()
            efecto = self.nombre_efecto(item.get_efecto())
            tiempo = self.tiempo_formato(item.get_tiempo())
            
            imagen_muestra = Image.open(imagen) 
            imagen_muestra = imagen_muestra.resize((110,50))
            imagen_muestra = ImageTk.PhotoImage(imagen_muestra)
            #print(f'{indice}  {imagen}  {efecto} {tiempo}')
            Label(contenedor_canvas, text=indice, font=("Verdana", 12), background=self.color_fondo_tabla).grid(column=1, row=indice+filas)
            imagen_label = Label(contenedor_canvas, image=imagen_muestra, width=110, height=50, background=self.color_fondo_tabla)
            imagen_label.grid(column=2, row=indice+filas)
            imagen_label.image = imagen_muestra
            Label(contenedor_canvas, text=efecto, font=("Verdana", 12), background=self.color_fondo_tabla).grid(column=3, row=indice+filas)
            Label(contenedor_canvas, text=tiempo, font=("Verdana", 12), background=self.color_fondo_tabla).grid(column=4, row=indice+filas)
            
            ttk.Separator(contenedor_canvas, orient=VERTICAL).grid(row=indice+filas, column=0, sticky="nse", rowspan=2)
            ttk.Separator(contenedor_canvas, orient=VERTICAL).grid(row=indice+filas, column=5, sticky="nsw", rowspan=2)
            ttk.Separator(contenedor_canvas, orient=HORIZONTAL).grid(row=indice+filas+1, column=1, columnspan=4, sticky="ews")
            filas = filas + 1
            #pass
            contenedor_canvas.grid_columnconfigure(0, weight=1)
            contenedor_canvas.grid_columnconfigure(1, weight=1)
            contenedor_canvas.grid_columnconfigure(2, weight=1)
            contenedor_canvas.grid_columnconfigure(3, weight=1)
            contenedor_canvas.grid_columnconfigure(4, weight=1)
            contenedor_canvas.grid_columnconfigure(5, weight=1)
            
    def nombre_efecto(self, nombre):
        if (nombre == 'Instantaneo.py'):
            return 'Instantaneo'
        elif (nombre == 'AbajoArriba.py'):
            return 'De abajo a arriba'
        elif (nombre == 'Aleatorio.py'):
            return 'Aleatorio'
        elif (nombre == 'DerechaIzquierda.py'):
            return 'De derecha a izquierda'
        elif (nombre == 'ArribaAbajo.py'):
            return 'De arriba a abajo'
        
    def tiempo_formato(self, tiempo):
        minutos = int(tiempo / 60)
        segundos = tiempo % 60
        #print('{:02}:{:02}'.format(minutos, segundos), end='\n')
        return '{:02}:{:02} minutos'.format(minutos, segundos)
        
        
    def guardar_configuracion(self):
        ruta_guardar = filedialog.askdirectory()
        print(ruta_guardar)
        indice = lista_configuracion[0].get_numero()
        imagen = lista_configuracion[0].get_imagen()
        efecto = lista_configuracion[0].get_efecto()
        tiempo = lista_configuracion[0].get_tiempo()
        
        nombre_imagen = ''
        for i in range(len(imagen)):
            if(imagen[-i] == '/'):
                nombre_imagen = imagen[-i+1:]
                print(nombre_imagen)
                break
        
            
        #cv2.imwrite(f'{ruta_guardar}{nombre_imagen}.ppm', img)
                   
########################Termina Resumen#################################


########################Configuracion Resumen#################################
class ConfiguracionResumen:
    def __init__(self):
        self.imagen_ruta = ''
        self.label_imagen = ''
        self.imagenFrame = 0
        self.opcion_efecto = None
        self.minutos = 0
        self.segundos = 0
        self.numero_imagen_editar = 0
        
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

        self.imagenFrame = Frame(self.root, background=self.colorFondo, pady=10)
        Label(self.imagenFrame, text="Selecciona una imagen para\nmostrar en la pantalla RGB", font=("verdana", 18), padx=10,
              background=self.colorFondo).grid(row=0, column=0, sticky="n")
        #self.label_imagen = Label(imagenFrame, background=self.colorFondo)
        #self.label_imagen.grid(column=0, row=2, sticky=N)
        
        imgImagen = Image.open("./iconos/imagen.png")
        imgImagen = imgImagen.resize((30, 30))
        imgImagen = ImageTk.PhotoImage(imgImagen)
        botonCargar = Button(self.imagenFrame, text="Cargar imagen   ", image=imgImagen, compound="right",
                             font=("verdana", 14), command=lambda: self.selecImagen(self.imagenFrame))
        botonCargar.grid(row=1, column=0, pady=30)
        botonCargar.image = imgImagen

        Label(self.imagenFrame, height=16, width=100, background=self.colorFondo).grid(column=0, row=2, sticky=N)

        self.imagenFrame.grid_columnconfigure(0, weight=1)
        # imagenFrame.rowconfigure(0, weight=1)
        self.imagenFrame.rowconfigure(1, weight=1)
        self.imagenFrame.rowconfigure(2, weight=1)
        self.imagenFrame.grid(row=6, column=0, columnspan=2, rowspan=5, sticky="ns", pady=20)

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
        
        Label(tiempo, text="minutos:", font=("verdana", 14), background=self.colorFondo).grid(column=0, row=1, sticky="we")
        minutosBox = ttk.Spinbox(tiempo, from_=0, to=4, increment=1, state="readonly", width=4, font=("verdana", 14), textvariable=self.minutos)
        minutosBox.grid(column=0, row=2, sticky='n', pady=5)
        
        self.segundos = StringVar()
        #self.segundos.set('0')
        
        Label(tiempo, text="segundos:", font=("verdana", 14), background=self.colorFondo).grid(column=1, row=1, sticky="we")
        segundosBox = ttk.Spinbox(tiempo, from_=0, to=59, increment=1, state="readonly", width=4, font=("verdana", 14), textvariable=self.segundos)
        segundosBox.grid(column=1, row=2, sticky='n', pady=5)
        # Label(tiempo, text="", background="white").grid(column=0, row=3, columnspan=3)
        tiempo.grid(row=8, column=3, columnspan=2, rowspan=2, sticky="ns")
        tiempo.grid_rowconfigure(0, weight=1)
        tiempo.grid_rowconfigure(1, weight=1)
        tiempo.grid_rowconfigure(2, weight=1)

        """
        imgRegresar = Image.open("./iconos/regresar.png")
        imgRegresar = imgRegresar.resize((30, 30))
        imgRegresar = ImageTk.PhotoImage(imgRegresar)
        botonRegresar = Button(self.root, text="Regresar  ", image=imgRegresar, compound="right", font=("verdana", 14),
                               command=self.regresar)
        botonRegresar.grid(column=0, row=11, pady=15, sticky='n')
        botonRegresar.image = imgRegresar
        """

        imgAgregar = Image.open("./iconos/imagen.png")
        imgAgregar = imgAgregar.resize((30, 30))
        imgAgregar = ImageTk.PhotoImage(imgAgregar)
        botonAgregar = Button(self.root, text="Guardar cambios ", image=imgAgregar, compound="right",
                              font=("verdana", 14), command=self.guardar_cambios)
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
        botonTerminar = Button(self.root, text="Regresar al resumen  ", image=imgTerminar, compound="right", font=("verdana", 14),
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
            imagenEntrada = imagenEntrada.resize((640, 240))  # 128x48
            ImagenEntrada = ImageTk.PhotoImage(imagenEntrada)
            self.label_imagen = Label(imagenFrame, background=self.colorFondo)
            #imagenOriginal = Label(imagenFrame, image=ImagenEntrada)
            self.label_imagen.config(image = ImagenEntrada)
            self.label_imagen.image = ImagenEntrada
            self.label_imagen.grid(column=0, row=2, sticky=N)
            self.label_imagen.config(relief="solid")
            self.imagen_ruta = archivo

    def cargarMenus(self):
        miMenu = Menu(self.root)
        miMenu.add_command(label="Ayuda", command=ventanaAyuda)
        miMenu.add_command(label="Acerca de", command=self.informacion)

    def informacion(self):
        messagebox.showinfo("Pantalla RGB", "Acerca de. \nInterfaz para configurar tablero RGB.\n\nVersión: ......")

    def destruir(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()

    def guardar_cambios(self):
        numero_imagen = self.numero_imagen_editar
        tiempo = (int(self.minutos.get()) * 60) + int(self.segundos.get())
        lista_configuracion[numero_imagen].set_imagen(self.imagen_ruta)
        lista_configuracion[numero_imagen].set_efecto(self.opcion_efecto.get())
        lista_configuracion[numero_imagen].set_tiempo(tiempo)
        
        #print(f'Imagen: {self.imagen_ruta}\n Efecto: {self.opcion_efecto}\n Tiempo: {tiempo}')
        #lista_configuracion.append(datos)
        #print(lista_configuracion)
        #self.limpiar_configuracion()
        messagebox.showinfo("Pantalla RGB", "Se han guardado los cambios con éxito")
        
    def set_imagen(self, archivo):
        #archivo = filedialog.askopenfilename(filetypes=[('Archivos de imagen', '*.jpg *.png *.jpeg *.ppm')])
        if archivo is not None:
            # Imagen de entrada
            imagenEntrada = Image.open(archivo)
            imagenEntrada = imagenEntrada.resize((640, 240))  # 128x48
            ImagenEntrada = ImageTk.PhotoImage(imagenEntrada)
            self.label_imagen = Label(self.imagenFrame, background=self.colorFondo)
            #imagenOriginal = Label(imagenFrame, image=ImagenEntrada)
            self.label_imagen.config(image = ImagenEntrada)
            self.label_imagen.image = ImagenEntrada
            self.label_imagen.grid(column=0, row=2, sticky=N)
            self.label_imagen.config(relief="solid")
            self.imagen_ruta = archivo

    def llenar_configuracion(self, numero_imagen):
        self.numero_imagen_editar = numero_imagen - 1
        datos_editar = lista_configuracion[self.numero_imagen_editar]
        datos_numero = datos_editar.get_numero()
        datos_imagen = datos_editar.get_imagen()
        datos_efecto = datos_editar.get_efecto()
        datos_tiempo = datos_editar.get_tiempo()
        
        minutos = int(datos_tiempo / 60)
        segundos = datos_tiempo % 60
        
        self.set_imagen(datos_imagen)
        self.opcion_efecto.set(datos_efecto)
        self.minutos.set(minutos)
        self.segundos.set(segundos)


    def visualizar(self):
        visualizar = Visualizar()
        visualizar.mostrar()  # Pantalla de visualizar
        pass

    def terminar(self):
        self.destruir()
        resumen = Resumen()
        resumen.cargar()
        resumen.llenar_tabla()
        resumen.mostrar()

    def limpiar_configuracion(self):
        self.imagen_ruta = ''
        self.label_imagen.config(image = None)
        self.label_imagen.config(relief="flat") 
        self.label_imagen.image = None   
        self.opcion_efecto.set(None)
        self.minutos.set("")
        self.segundos.set("")
    
########################Termina Configuracion Resumen#################################


########################Visualizar#################################
class Visualizar:    
    def mostrar(self): 
        pygame.init()

        size = (1200, 560)

        ventana = pygame.display.set_mode(size)

        blanco = (255,255,255)
        silver = (192,192,192)
        negro = (0,0,0)
        gray = (128,128,128)
        lightblue = (173,216,230)

        #Imagen de ventana y título
        pygame.display.set_caption("Visualizar")
        icono = pygame.image.load("./recursos/firefly.png")
        pygame.display.set_icon(icono)


        uam = pygame.image.load("./recursos/uamazcL.png")
        uamAzc = pygame.transform.scale(uam, (300, 80))
        cbi = pygame.image.load("./recursos/cbi.png")
        cbiAzc = pygame.transform.scale(cbi, (300, 80))

        prueba = pygame.image.load("./recursos/RGB.jpg")
        pruebaR = pygame.transform.scale(prueba, (360, 140))

        miFuente = pygame.font.SysFont("Verdana", 30)
        text = miFuente.render("Visualización de animación", 0, (negro))
        fuente = pygame.font.SysFont("Verdana", 20)
        nomImagen = fuente.render("Nombre de imagen: ", 0, (negro))
        nomEfecto = fuente.render("Efecto: ", 0, (negro))
        tiempo = fuente.render("Tiempo: ", 0, (negro))
        seg = fuente.render("segundos.", 0, (negro))

        play = Rect(660, 380, 80, 25)
        pause = Rect(860, 380, 80, 25)
        stop = Rect(1060, 380, 80, 25)
        regresar = Rect(1060, 500, 80, 25)
        vel1 = Rect(635, 430, 130, 25)
        vel2 = Rect(835, 430, 130, 25)
        vel4 = Rect(1037, 430, 130, 25)

        fuente2 = pygame.font.SysFont("Calibri", 20)

        def crearBoton(screen, boton, mensaje):
            if boton.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(ventana, silver, boton)
            else:
                pygame.draw.rect(ventana, gray, boton)
            texto = fuente2.render(mensaje, True, (blanco))
            screen.blit(texto, (boton.x+(boton.width-texto.get_width())/2,
            boton.y+(boton.height-texto.get_height())/2)
            )

        clock = pygame.time.Clock()
        FPS = 17

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            ventana.fill(blanco)    #Color de fondo
            ventana.blit(uamAzc, (50, 20))
            ventana.blit(text, (400,40))
            ventana.blit(cbiAzc, (850, 20))
            pygame.draw.line(ventana, negro, (0,120), (1200,120), 5)
            pygame.draw.line(ventana, negro, (600,120), (600,600), 5)
            pygame.draw.rect(ventana, silver, (720, 200, 360, 140))
            ventana.blit(pruebaR, (720, 200))
            ventana.blit(nomImagen, (50,150))
            ventana.blit(nomEfecto, (50,220))
            ventana.blit(tiempo, (50,290))
            ventana.blit(seg, (230,290))

            if event.type == MOUSEBUTTONDOWN:
                if regresar.collidepoint(pygame.mouse.get_pos()):
                    self.salir()
                    pass

            crearBoton(ventana, play, "Play")
            crearBoton(ventana, pause, "Pause")
            crearBoton(ventana, stop, "Stop")
            crearBoton(ventana, regresar, "Salir")
            crearBoton(ventana, vel1, "Velocidad  x1")
            crearBoton(ventana, vel2, "Velocidad  x2")
            crearBoton(ventana, vel4, "Velocidad  x4")

            pygame.display.flip()
            clock.tick(FPS)
            
    def salir(self):
        pygame.quit()
########################Termina Visualizar#################################


########################Main###########################

lista_configuracion = []
datos1 = Datos(0, './recursos/micro.jpg', 'Aleatorio.py', 61)
datos2 = Datos(1, './recursos/RGB.jpg', 'DerechaIzquierda.py', 40)
datos3 = Datos(2, './recursos/electronica.jpg', 'Instantaneo.py', 51)
datos4 = Datos(3, './recursos/electronica.jpg', 'AbajoArriba.py', 122)
datos5 = Datos(4, './recursos/electronica.jpg', 'ArribaAbajo.py', 179)

lista_configuracion.append(datos1)
lista_configuracion.append(datos2)
lista_configuracion.append(datos3)
lista_configuracion.append(datos4)
lista_configuracion.append(datos5)
lista_configuracion.append(datos1)
lista_configuracion.append(datos2)
lista_configuracion.append(datos3)
lista_configuracion.append(datos4)
lista_configuracion.append(datos5)
lista_configuracion.append(datos1)
lista_configuracion.append(datos2)
lista_configuracion.append(datos3)
lista_configuracion.append(datos4)
lista_configuracion.append(datos5)

#bienvenida = Bienvenida()
#bienvenida.cargar()
#bienvenida.mostrar()#

#configuracion = Configuracion()
#configuracion.cargar()
#configuracion.mostrar()#

resumen = Resumen()
resumen.cargar()
resumen.llenar_tabla()
resumen.mostrar()
resumen.llenar_tabla()#