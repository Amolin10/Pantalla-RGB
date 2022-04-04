import socket
import struct
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED

from os import lseek
import os.path

#librerías para interfaces
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog

#Librerías para visualizaciones
from pygame import * 
import sys, pygame
from pygame.draw import line
from pygame.font import SysFont
from pygame import * 
import time
import random

############################ Datos #########################################
#Esta clase es una estructura para almacenar y obtener los parámetros para presentar una imagen en la pantalla informativa.
#   Los parámetros son: 
#       Número de imagen
#       Ruta de imagen
#       Efecto de entrada
#       Tiempo de presentación
class Datos:
    def __init__(self, numero, imagen, efecto, tiempo):
        self.numero = numero
        self.imagen = imagen
        self.efecto = efecto
        self.tiempo = tiempo
        
    def set_numero(self, numero):
        self.numero = numero    

    def get_numero(self):
        return self.numero
    
    def set_imagen(self, imagen):
        self.imagen = imagen
    
    def get_imagen(self):
        return self.imagen
    
    def set_efecto(self, efecto):
        self.efecto = efecto
    
    def get_efecto(self):
        return self.efecto
    
    def set_tiempo(self, tiempo):
        self.tiempo = tiempo 

    def get_tiempo(self):
        return self.tiempo
    
    def __repr__(self):
        return str(self.__dict__)
############################ Datos #########################################

############################# Bienvenida ####################################
#Ventana de bienvenida. Contiene los botones Ayuda y Continuar.
class Bienvenida:    
    def __init__(self):
        self.title = "Monitor de Productividad para Procesos Industriales (MPPI)"
        self.icon = "./iconos/main.ico"
        self.resizable = True
        self.root = Tk()

    #Función para cargar los elementos de la ventana
    def cargar(self):
        self.root.title(self.title)
        icono = os.path.abspath(self.icon)
        self.root.iconbitmap(icono)
        ancho = 660
        alto = 400
        # winfo da el tamaño de la pantalla en ancho y en alto
        #Colocar la ventana en el centro de la pantalla
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2  
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana) + "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background='white')

        #Permitir el redimensionamiento de la pantalla
        if self.resizable:
            self.root.resizable(0, 0)
        else:
            self.root.resizable(1, 1)

        #Cargar la imagen y colocarla en el encabezado de la ventana, del lado izquierdo.
        uama = Image.open("./recursos/uamazcL.png")
        uama = uama.resize((180, 60))
        uama = ImageTk.PhotoImage(uama)
        uamA = Label(self.root, image=uama, width=180, height=60, background='white')
        uamA.image = uama
        uamA.grid(row=0, column=0, sticky=W + S + N + E)

        #Cargar la imagen y colocarla en el encabezado de la ventana, del lado derecho.
        cbi = Image.open("./recursos/cbi.png")
        cbi = cbi.resize((180, 60))
        cbi = ImageTk.PhotoImage(cbi)
        CBI = Label(self.root, image=cbi, width=180, height=60, background='white')
        CBI.image = cbi
        CBI.grid(row=0, column=2, sticky=W + S + N + E)

        #Título del proyecto en el centro del encabezado.
        titulo = Label(self.root, text="Monitor de Productividad \n para Procesos Industriales \n MPPI", padx=15, font=("Verdana", 14), background='white').grid(row=0, column=1)

        #Establecer importancia de las filas y columnas de la pantalla.
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        #Color del fondo de la ventana
        fondo = Frame(self.root, width=480, height=320, bg='lightblue')
        fondo.grid_propagate(False)  
        #El frame no se ajusta al contenido
        fondo.grid(row=1, column=0, columnspan=3, sticky=W + S + N + E)

        #Imagen de fondo 
        rgbImagen = Image.open("./recursos/bienvenida.jpg")
        rgbImagen = rgbImagen.resize((660, 600))
        rgbImagen = ImageTk.PhotoImage(rgbImagen)
        fondoRGB = Label(fondo, image=rgbImagen, background='white')
        fondoRGB.image = rgbImagen
        fondoRGB.grid(row=0, column=0, rowspan=5, columnspan=3, sticky="ewns")

        #Establecer importancia de las filas y columnas de la pantalla.
        fondo.grid_columnconfigure(0, weight=1)
        fondo.grid_columnconfigure(1, weight=1)
        fondo.grid_columnconfigure(2, weight=1)
        fondo.grid_rowconfigure(0, weight=1)
        fondo.grid_rowconfigure(1, weight=1)
        fondo.grid_rowconfigure(2, weight=1)
        fondo.grid_rowconfigure(3, weight=1)
        fondo.grid_rowconfigure(4, weight=1)

        #Cargar imagen y colocarla en un botón
        imgAyuda = Image.open("./iconos/signo-de-interrogacion.png")
        imgAyuda = imgAyuda.resize((20, 20))
        imgAyuda = ImageTk.PhotoImage(imgAyuda)
        botonAyuda = Button(fondo, image=imgAyuda, text="Ayuda  ", compound="right", command=""" ventanaAyuda """)
        botonAyuda.grid(row=4, column=0, ipadx=10)
        botonAyuda.image = imgAyuda

        #Cargar imagen y colocarla en un botón
        imgContinuar = Image.open("./iconos/next.png")
        imgContinuar = imgContinuar.resize((20, 20))
        imgContinuar = ImageTk.PhotoImage(imgContinuar)
        botonContinuar = Button(fondo, image=imgContinuar, text="Continuar  ", compound="right", command=self.continuarOpciones)
        botonContinuar.grid(row=4, column=1)
        botonContinuar.image = imgContinuar

        #Cargar imagen y colocarla en un botón
        imgQuit = Image.open("./iconos/cancelar.png")
        imgQuit = imgQuit.resize((20, 20))
        imgQuit = ImageTk.PhotoImage(imgQuit)
        botonSalir = Button(fondo, image=imgQuit, text="Salir  ", compound="right", command=self.cerrar)
        botonSalir.grid(row=4, column=2, ipadx=10)
        botonSalir.image = imgQuit

    #Función para cerrar y destruir la ventana
    def cerrar(self):
        self.root.destroy()
    
    #Función para mostrar el contenido de la pantalla
    def mostrar(self):
        self.root.mainloop()

    #Función para avanzar a la siguiente ventana.
    def continuarOpciones(self):
        self.cerrar()
        opciones = Opciones()
        opciones.cargar()
        opciones.mostrar()
#######################Termina Bienvenida################################


#######################Inicia Opciones###################################      
#Ventana de opciones. Contine los botones para:
#   Crear una nueva configuración
#   Abrir una configuración desde los archivos de la computadora
#   Regresar a la ventana anterior
class Opciones:
    def __init__(self):
        self.title = "Monitor de Productividad para Procesos Industriales (MPPI)"
        self.icon = "./iconos/main.ico"
        self.resizable = True
        self.root = Tk()
        self.colorFondo = '#E2EFFF'

    #Función para cargar los elementos de la ventana
    def cargar(self):
        self.root.title(self.title)
        icono = os.path.abspath(self.icon)
        self.root.iconbitmap(icono)
        ancho = 770
        alto = 300
        # winfo da el tamaño de la pantalla en ancho y en alto
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2  
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana) + "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background=self.colorFondo)

        #Permitir el redimensionamiento de la ventana.
        if self.resizable:
            self.root.resizable(0, 0)
        else:
            self.root.resizable(1, 1)

        #Cargar imagen y colocarla en un botón
        imgNuevo = Image.open("./iconos/nuevo-documento.png")
        imgNuevo = imgNuevo.resize((40, 40))
        imgNuevo = ImageTk.PhotoImage(imgNuevo)
        botonNuevo = Button(self.root, image=imgNuevo, text="Nuevo  ", compound="right", width=350,
                            font=("Verdana", 14), background='white', activebackground="#999999",
                            command=self.ventanaPrincipal)
        botonNuevo.grid(row=0, column=0, padx=15, sticky="ws")
        botonNuevo.image = imgNuevo

        #Cargar imagen y colocarla en un botón
        imgConfig = Image.open("./iconos/engrane.png")
        imgConfig = imgConfig.resize((40, 40))
        imgConfig = ImageTk.PhotoImage(imgConfig)
        botonConfig = Button(self.root, image=imgConfig, text="Cargar configuración  ", width=350, compound="right",
                             background='white', command=self.abrir_archivo, activebackground="#999999", font=("Verdana", 14))
        botonConfig.grid(row=1, column=0, padx=50, sticky="w")
        botonConfig.image = imgConfig

        #Cargar imagen y colocarla en un botón
        imgSalir= Image.open('./iconos/deshacer.png')
        imgSalir= imgSalir.resize((40, 40))
        imgSalir= ImageTk.PhotoImage(imgSalir)
        botonSalir = Button(self.root, image=imgSalir, text="Regresar  ", width=350, compound="right",
                          background="white", activebackground="#999999", font=("Verdana", 14), command=self.salir)
        botonSalir.grid(row=2, column=0, padx=80, sticky="wn")
        botonSalir.image = imgSalir
        
        #Cargar una imagen y colocarla en la ventana
        fondoImagen = Image.open("./recursos/computadora.png")
        fondoImagen = fondoImagen.resize((200, 200))
        fondoImagen = ImageTk.PhotoImage(fondoImagen)
        fondoOpciones = Label(self.root, image=fondoImagen, background=self.colorFondo)
        fondoOpciones.image = fondoImagen
        fondoOpciones.grid(row=0, column=1, rowspan=3, sticky="wns")

        #Establecer importancia de las filas y columnas de la pantalla.
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

    #Función para cerrar y destruir la ventana.
    def cerrar(self):
        self.root.destroy()

    #Función para mostrar el contenido de la ventana.
    def mostrar(self):
        self.root.mainloop()

    #Función para avanzar a la siguiente ventana (crear una configuración nueva).
    def ventanaPrincipal(self):
        self.cerrar()
        configuracion = Configuracion()
        configuracion.cargar()
        configuracion.mostrar()

    #Función para regresar a la ventana anterior (ventana de Bienvenida)
    def salir(self):
        self.cerrar()
        bienvenida = Bienvenida()
        bienvenida.cargar()
        bienvenida.mostrar()
        
    #Función para leer una configuración desde un archivo de la computadora
    def abrir_archivo(self): 
        #Solicitar al usuario que indique la carpeta o directorio donde se encuentra la configuración que se desea abrir, utilizando el explorador de archivos del Sistema Operativo
        ruta_configuracion = filedialog.askdirectory()
        
        #Comprobar si la ruta indicada contiene los archivos necesarios para leer una configuración
        #Si existen, se leen todas las líneas del archivo 'configuracion.txt' y se guardan en la variable
        #lineas_archivo
        if os.path.exists(f'{ruta_configuracion}/configuracion.txt'):
            archivo = open (f'{ruta_configuracion}/configuracion.txt','r')  
            lineas_archivo = archivo.readlines()
            archivo.close()

            #Quitar el último caracter a cada línea del archivo, eliminando el salto de línea
            for i in range(len(lineas_archivo)):
                lineas_archivo[i] = lineas_archivo[i][:-1]
        
            #De cada conjunto de 4 líneas, se toman los siguientes datos:
            #   número de imagen
            #   ruta de imagen
            #   efecto de entrada
            #   tiempo de presentación
            numero_datos = 0
            for i in range(0, len(lineas_archivo), 4):
                indice = numero_datos
                efecto = lineas_archivo[i+1]
                imagen = ruta_configuracion + '/Imagenes/' + lineas_archivo[i+2]
                tiempo = lineas_archivo[i+3]
                
                #Con los datos obtenidos para cada imagen y sus parámetros de desplegado, se crea una variable de tipo Datos, la cual se añade a la lista de configuración. 
                #NOTA: lista_configuracion es una variable global, en la cual se almacenan las imágenes y sus respectivos parámetros de desplegado de cada imagen
                datos_temp = Datos(indice, imagen, efecto, tiempo)
                lista_configuracion.append(datos_temp)
                
                numero_datos += 1
                
            print(lista_configuracion)
            self.cerrar()
            resumen = Resumen()
            resumen.estado_guardar(True)
            resumen.establecer_ruta(ruta_configuracion)
            resumen.cargar()
            resumen.llenar_tabla()
            resumen.mostrar() 
            
        #Si no se elige ninguna ruta o si se cancela la operación, no se realiza ninguna acción.
        elif ruta_configuracion == '': 
            pass
        #Si la ruta indicada por el usuario no contiene el archivo de configuración, se muestra un mensaje de error.
        else: 
            messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "Error al cargar la configuración. \nSeleccione una ruta correta.")         

########################Termina Opciones#####################################


########################Inicia Configuración#################################
#Ventana de para crear una nueva configuración
class Configuracion:

    #Variables para almacenar los parámetros de presentación de una imagen
    #   Ruta de la imagen
    #   Nombre del efecto de entrada
    #   Tiempo: minutos y segundos
    def __init__(self):
        self.imagen_ruta = ''
        self.label_imagen = ''
        self.opcion_efecto = None
        self.minutos = 0
        self.segundos = 0
        
        self.title = "Monitor de Productividad para Procesos Industriales (MPPI)"
        self.icon = "./iconos/main.ico"
        self.resizable = True
        self.root = "Tk()"
        self.colorFondo = '#E2EFFF'
        
    #Función para cargar los elementos de la ventana
    def cargar(self):
        self.root = Tk()
        self.root.title(self.title)
        icono = os.path.abspath(self.icon)
        self.root.iconbitmap(icono)
        ancho = 1450
        alto = 830
        # winfo da el tamaño de la pantalla en ancho y en alto
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2  
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        #Colocar la ventana en el centro de la pantalla
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana) + "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background=self.colorFondo)

        if self.resizable:
            self.root.resizable(1, 1)
        else:
            self.root.resizable(0, 0)

        #Cargar imagen y colocarla en el encabezado de la ventana.
        uama = Image.open("./recursos/uamazc.jpg")
        uama = uama.resize((280, 110))
        uama = ImageTk.PhotoImage(uama)
        uamA = Label(self.root, image=uama, width=260, height=80, padx=100, background='white')
        uamA.image = uama
        uamA.grid(row=0, column=0, sticky='ewns')

        #Cargar imagen y colocarla en el encabezado de la ventana.
        electronica = Image.open("./recursos/electronica.jpg")
        electronica = electronica.resize((240, 120))
        electronica = ImageTk.PhotoImage(electronica)
        electronicaLabel = Label(self.root, image=electronica, width=220, height=80, padx=100, background='white')
        electronicaLabel.image = electronica
        electronicaLabel.grid(row=0, column=1, columnspan=3, sticky='ewns')

        #Cargar imagen y colocarla en el encabezado de la ventana.
        cbi = Image.open("./recursos/cbi.png")
        cbi = cbi.resize((240, 120))
        cbi = ImageTk.PhotoImage(cbi)
        CBI = Label(self.root, image=cbi, width=220, height=80, padx=100, background='white')
        CBI.image = cbi
        
        #Establecer una configuración de rejilla (filas y columnas) para la ventana
        CBI.grid(row=0, column=4, sticky='ewns')

        #Colocar e título en el encabezado de la ventana.
        titulo = Label(self.root, text="Monitor de Productividad para Procesos Industriales (MPPI)", font=("Verdana", 28), relief="groove", background='#184B6C',
                       fg='white').grid(row=1, column=0, columnspan=5, sticky='ewns')
        texto = Label(self.root, text="Configurar imagen para mostrar en la pantalla RGB", relief='groove',
                      font=("Verdana", 22), background='#2980B9')
        texto.grid(row=2, column=0, columnspan=5, sticky="ewns")
        Label(self.root, text="", background=self.colorFondo).grid(row=3, column=0, columnspan=5, pady=5)

        #Líneas horizontales y verticales para hacer separadores
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=4, column=0, columnspan=5, sticky="ews")
        ttk.Separator(self.root, orient=VERTICAL).grid(row=5, column=2, rowspan=5, sticky="ns")
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=7, column=3, columnspan=2, sticky="ewn")
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=10, column=0, columnspan=5, sticky="ewn")

        #Frame dedicado para colocar la imagen seleccionada por el usuario
        imagenFrame = Frame(self.root, background=self.colorFondo, pady=10)
        Label(imagenFrame, text="Selecciona una imagen para\nmostrar en la pantalla RGB", font=("verdana", 18), padx=10,
              background=self.colorFondo).grid(row=0, column=0, sticky="n")
      
        #Cargar imagen y colocarla en un botón
        imgImagen = Image.open("./iconos/cargar-imagen.png")
        imgImagen = imgImagen.resize((30, 30))
        imgImagen = ImageTk.PhotoImage(imgImagen)
        
        #Al dar click en el botón, se ejecuta la función 'self.selectImagen(imagenFrame)' a la que se le envía como parámetro la imagen que fue seleccionada previamente por el usuario 
        #command=lambda: 'function' indica la definición de una función, por lo que dicha función NO se ejecutará al enviarla como parámetro.
        botonCargar = Button(imagenFrame, text="Cargar imagen   ", image=imgImagen, compound="right",
                             font=("verdana", 14), command=lambda: self.selecImagen(imagenFrame))
        botonCargar.grid(row=1, column=0, pady=30)
        botonCargar.image = imgImagen

        Label(imagenFrame, height=16, width=100, background=self.colorFondo).grid(column=0, row=2, sticky=N)

        #Establecer la importancia de las filas y columnas
        imagenFrame.grid_columnconfigure(0, weight=1)
        imagenFrame.rowconfigure(1, weight=1)
        imagenFrame.rowconfigure(2, weight=1)
        imagenFrame.grid(row=6, column=0, columnspan=2, rowspan=5, sticky="ns", pady=20)

        #Frame para la selección del efecto de entrada
        parametros = Frame(self.root, background=self.colorFondo)

        #La variable 'self.opcion_efecto' almacena la opción de efecto seleccionada por el usuario y se encuentra vacía al principio
        self.opcion_efecto = StringVar()
        self.opcion_efecto.set(None)

        #Los efectos de entradda se colocan en botones de selección, el usuario puede seleccionar sólo un efecto y esta selección se almacena en la variable 'self.opcion_efecto'
        Label(parametros, text="Selecciona el efecto de entrada de la imagen", font=("Verdana", 18), background=self.colorFondo).grid(column=0, row=0, columnspan=3)
        
        #Botón de selección para efecto 'Instanteneo'
        Radiobutton(parametros, text="Instantaneo", font=("verdana", 14), variable=self.opcion_efecto, value='Instantaneo.py', background=self.colorFondo).grid(column=0, row=1)
        #Botón de selección para efecto 'De abajo a arriba'
        Radiobutton(parametros, text="De abajo a arriba", font=("verdana", 14), variable=self.opcion_efecto, value='AbajoArriba.py', background=self.colorFondo, padx=20).grid(column=1, row=1, sticky="ew")
        #Botón de selección para efecto 'Aleatorio'
        Radiobutton(parametros, text="Aleatorio", font=("verdana", 14), variable=self.opcion_efecto, value='Aleatorio.py', background=self.colorFondo).grid(column=2, row=1, sticky="e")
        #Botón de selección para efecto 'De derecha a izquierda'
        Radiobutton(parametros, text="De derecha a izquierda", font=("verdana", 14), variable=self.opcion_efecto, value = 'DerechaIzquierda.py', background=self.colorFondo).grid(column=0, row=2, sticky="e")
        #Botón de selección para efecto 'De arriba a abajo'
        Radiobutton(parametros, text="De arriba a abajo", font=("verdana", 14), variable=self.opcion_efecto, value='ArribaAbajo.py', background=self.colorFondo).grid(column=2, row=2, sticky="w")
        
        Label(parametros, text="", background=self.colorFondo).grid(column=0, row=3, columnspan=3)
        
        #Establecer la importancia de las filas y columnas
        parametros.rowconfigure(0, weight=1)
        parametros.rowconfigure(1, weight=1)
        parametros.rowconfigure(2, weight=1)
        parametros.rowconfigure(3, weight=1)
        parametros.grid(column=3, row=5, columnspan=2, rowspan=2, sticky='ns')

        #Frame para la selección del tiempo de presentación
        tiempo = Frame(self.root, background=self.colorFondo)
        Label(tiempo, text="Seleccione el tiempo de desplegado de la imagen", font=("Verdana", 18), pady=14,
              background=self.colorFondo).grid(column=0, row=0, columnspan=2)
        
        #La variable 'self.minutos' almacena el tiempo en minutos, indicado por el usuario
        self.minutos = StringVar()
        
        #La selección del tiempo en minutos se hace a través de una caja que recibe valores numéricos
        Label(tiempo, text="minutos:", font=("verdana", 14), background=self.colorFondo).grid(column=0, row=1, sticky="we")
        minutosBox = ttk.Spinbox(tiempo, from_=0, to=4, increment=1, width=4, font=("verdana", 14), textvariable=self.minutos)
        minutosBox.grid(column=0, row=2, sticky='n', pady=5)
        
        #La variable 'self.segundos' almacena el tiempo en segundos, indicado por el usuario
        self.segundos = StringVar()
        
        #La selección del tiempo en segundos se hace a través de una caja que recibe valores numéricos
        Label(tiempo, text="segundos:", font=("verdana", 14), background=self.colorFondo).grid(column=1, row=1, sticky="we")
        segundosBox = ttk.Spinbox(tiempo, from_=0, to=59, increment=1, width=4, font=("verdana", 14), textvariable=self.segundos)
        segundosBox.grid(column=1, row=2, sticky='n', pady=5)
        
        #Establecer el orden e importancia de las filas y columnas de la ventana
        tiempo.grid(row=8, column=3, columnspan=2, rowspan=2, sticky="ns")
        tiempo.grid_rowconfigure(0, weight=1)
        tiempo.grid_rowconfigure(1, weight=1)
        tiempo.grid_rowconfigure(2, weight=1)
        
        #Cargar imagen y colocarla en un botón
        imgRegresar = Image.open("./iconos/deshacer.png")
        imgRegresar = imgRegresar.resize((30, 30))
        imgRegresar = ImageTk.PhotoImage(imgRegresar)
        botonRegresar = Button(self.root, text="Regresar  ", image=imgRegresar, compound="right", font=("verdana", 14),
                               command=self.regresar)
        botonRegresar.grid(column=0, row=11, pady=15, sticky='n')
        botonRegresar.image = imgRegresar

        #Cargar imagen y colocarla en un botón
        imgAgregar = Image.open("./iconos/anadir-imagen.png")
        imgAgregar = imgAgregar.resize((30, 30))
        imgAgregar = ImageTk.PhotoImage(imgAgregar)
        botonAgregar = Button(self.root, text="Agregar imagen  ", image=imgAgregar, compound="right",
                              font=("verdana", 14), command=self.agregar)
        botonAgregar.grid(column=1, row=11, pady=15, sticky='n')
        botonAgregar.image = imgAgregar

        #Cargar imagen y colocarla en un botón
        imgVisualizar = Image.open("./iconos/play.png")
        imgVisualizar = imgVisualizar.resize((30, 30))
        imgVisualizar = ImageTk.PhotoImage(imgVisualizar)
        botonVisualizar = Button(self.root, text="Visualizar  ", image=imgVisualizar, compound="right",
                                 font=("verdana", 14), command=self.visualizar)
        botonVisualizar.grid(column=3, row=11, pady=15, sticky='n')
        botonVisualizar.image = imgVisualizar

        #Cargar imagen y colocarla en un botón
        imgTerminar = Image.open("./iconos/next.png")
        imgTerminar = imgTerminar.resize((30, 30))
        imgTerminar = ImageTk.PhotoImage(imgTerminar)
        botonTerminar = Button(self.root, text="Resumen de la configuración  ", image=imgTerminar, compound="right", font=("verdana", 14),
                               command=self.terminar)
        botonTerminar.grid(column=4, row=11, pady=15, sticky='n')
        botonTerminar.image = imgTerminar

        #Establecer la importancia de las filas y columnas
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(8, weight=1)
    
    #Función para seleccionar la imagen que desea agrgarse a la configuración 
    def selecImagen(self, imagenFrame):
        #Solicitud para que el usuario seleccione una imagen utilizando el explorador de archivos del Sistema Operativo
        archivo = filedialog.askopenfilename(filetypes=[('Archivos de imagen', '*.jpg *.png *.jpeg *.ppm')])

        #Si el archivo seleccionado es válido, se abre el archivo, se redimensiona y se coloca en el freame que corresponde. La imagen se redimensiona a 640x240 unicamente para mostrarse en la ventana
        # La ruta de la imagen se almacena en la variable 'self.imagen_ruta'
        if archivo is not None:
            imagenEntrada = Image.open(archivo)
            imagenEntrada = imagenEntrada.resize((640, 240))
            ImagenEntrada = ImageTk.PhotoImage(imagenEntrada)
            self.label_imagen = Label(imagenFrame, background=self.colorFondo)
            self.label_imagen.config(image = ImagenEntrada)
            self.label_imagen.image = ImagenEntrada
            self.label_imagen.grid(column=0, row=2, sticky=N)
            self.label_imagen.config(relief="solid")
            self.imagen_ruta = archivo

    #Función para cerrar y destruir la ventana.
    def destruir(self):
        self.root.destroy()

     #Función para mostrar el contenido de la ventana.
    def mostrar(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    #Función para agregar una imagen y sus parámetros de presentación a la configuración
    def agregar(self):
        #Si no se selecciona algún parámetro, se muestra un mensaje de error
        if (self.imagen_ruta == '' or self.opcion_efecto.get() == 'None' or self.minutos.get() == '' or self.segundos.get() == ''):
            messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "Debe llenar todos los campos.")
        #Si el valor del tiempo en minutos es mayor a 4, se muestra un mensaje de error
        elif (int(self.minutos.get()) > 4):
                messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "El valor de los minutos debe ser menor a 5.")
        #Si el valor del tiempo en segundos es mayor a 59, se muestra un mensaje de error        
        elif (int(self.segundos.get()) > 59):
                messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "El valor de los segundos debe ser menor a 60.")
        #Si se colocan todos los parámetros de manera correcta, se agrega la imagen y sus parámetros a la lista de configuración
        else:
            #Se convierte el valor del tiempo a segundos 
            tiempo = (int(self.minutos.get()) * 60) + int(self.segundos.get())
            print(f'Imagen: {self.imagen_ruta}\n Efecto: {self.opcion_efecto.get()}\n Tiempo: {tiempo}')
            datos = Datos(len(lista_configuracion), self.imagen_ruta, self.opcion_efecto.get(), tiempo)
            lista_configuracion.append(datos)
            self.limpiar_configuracion()
    
    #Función para intercambiar los nombres de los efectos, por los nombres de archivo en Python 
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
    
    #Función para regresar a la ventana anterior
    def regresar(self):
        #Si la lista de configuración tiene datos, se pregunta al usuario si desea regresar, ya que los cambios en la lista se perderán
        if len(lista_configuracion) > 0:
            decision = messagebox.askokcancel("Monitor de Productividad para Procesos Industriales (MPPI)", "Todos los cambios realizados serán borrados.")
            if(decision == True):
                self.destruir()
                #Limpia la lista de configuración 
                lista_configuracion.clear()
                opciones = Opciones()
                opciones.cargar()
                opciones.mostrar()   
        #Si no se hizo ningún cambio, solo se regresa a la ventana anterior             
        else:
            self.destruir()
            opciones = Opciones()
            opciones.cargar()
            opciones.mostrar()
        
    #Al cerrar la ventana, si la lista de configuración tiene datos, se pregunta al usuario si desea regresar, ya que los cambios en la lista se perderán
    def on_closing(self):
        if len(lista_configuracion) > 0:
            decision = messagebox.askokcancel("Monitor de Productividad para Procesos Industriales (MPPI)", "Todos los cambios realizados serán borrados.")
            if(decision == True):
                self.destruir()
        else:   
            self.destruir()

    #Función para mostrar la ventana de visualización de la imagen con los parámetros indicados en ese momento
    def visualizar(self):
        #Si no se selecciona algún parámetro, se muestra un mensaje de error
        if (self.imagen_ruta == '' or self.opcion_efecto.get() == 'None' or self.minutos.get() == '' or self.segundos.get() == ''):
            messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "Debe llenar todos los campos.")
        #Si el valor del tiempo en minutos es mayor a 4, se muestra un mensaje de error
        elif (int(self.minutos.get()) > 4):
                messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "El valor de los minutos debe ser menor a 5.")
        #Si el valor del tiempo en segundos es mayor a 59, se muestra un mensaje de error  
        elif (int(self.segundos.get()) > 59):
                messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "El valor de los segundos debe ser menor a 60.")
        #Si se colocan todos los parámetros de manera correcta, se agrega la imagen y sus parámetros a la lista de configuración
        else:
            tiempo = (int(self.minutos.get()) * 60) + int(self.segundos.get())
            print(f'Imagen: {self.imagen_ruta}\n Efecto: {self.opcion_efecto.get()}\n Tiempo: {tiempo}')
            #Se construye una variable de tipo datos con la imagen y parámetros seleccionados en la ventana
            datos = Datos(len(lista_configuracion)+1, self.imagen_ruta, self.opcion_efecto.get(), tiempo)
            #Envía los parámetros a la venta de visualización y se muestra
            visualizar = Visualizar(datos)
            visualizar.mostrar()

    #Función para avanzar a la ventana de resumen 
    def terminar(self):
        #Si la lista está vacía, se muestra un mensaje de error 
        if len(lista_configuracion) == 0:
            messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "La lista de configuración está vacía. \n Por favor inserte una configuración.")
        #Si la lista no está vacía, se envía la lista a la ventana de Resumen y se muestra. 
        else:
            self.destruir()
            resumen = Resumen()
            resumen.cargar()
            resumen.llenar_tabla()
            resumen.mostrar()

    #Se limpian todos los campos de la ventana, incluyendo la imagen 
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
#Ventana para mostrar las imágenes de la lista de configuración y sus parámetros
class Resumen:
    def __init__(self):
        self.title = "Monitor de Productividad para Procesos Industriales (MPPI)"
        self.icon = "./iconos/main.ico"
        self.resizable = True
        self.root = "Tk()"
        self.color_fondo = '#E2EFFF'
        self.tabla_frame = ''
        self.color_fondo_tabla = '#C0D5F0'
        self.estado_guardado = False
        self.ruta_guardar = ''

    #Función para cargar los elementos de la ventana
    def cargar(self):
        self.root = Tk()
        self.root.title(self.title)
        icono = os.path.abspath(self.icon)
        self.root.iconbitmap(icono)
        ancho = 1150
        alto = 800
        #winfo da el tamaño de la pantalla en ancho y en alto
        #Colocar la ventana en el centro de la pantalla
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2 
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana)+ "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background=self.color_fondo)

        #Permitir o no el redimensionamiento de la pantalla
        if self.resizable:
            self.root.resizable(0, 0)
        else:
            self.root.resizable(1, 1)           

        #Cargar la imagen y colocarla en el encabezado de la ventana, del lado izquierdo.
        uama = Image.open("./recursos/uamazc.jpg")
        uama= uama.resize((260, 100))
        uama = ImageTk.PhotoImage(uama)
        uamA = Label(self.root, image=uama, width=260, height=100, padx=100, background='white')
        uamA.image = uama
        uamA.grid(row=0, column=0, sticky='ewns')

        #Cargar la imagen y colocarla en el encabezado de la ventana.
        electronica = Image.open("./recursos/electronica.jpg")
        electronica= electronica.resize((220, 100))
        electronica = ImageTk.PhotoImage(electronica)
        electronicaLabel = Label(self.root, image=electronica, width=220, height=100, padx=100, background='white')
        electronicaLabel.image = electronica
        electronicaLabel.grid(row=0, column=1, columnspan=3, sticky='ewns')

        #Cargar la imagen y colocarla en el encabezado de la ventana, del lado derecho.
        cbi = Image.open("./recursos/cbi.png")
        cbi= cbi.resize((220, 100))
        cbi = ImageTk.PhotoImage(cbi)
        CBI = Label(self.root, image=cbi, width=220, height=100, padx=100, background='white')
        CBI.image = cbi
        CBI.grid(row=0, column=4, sticky='ewns')

        #Título del proyecto en el centro del encabezado.
        titulo = Label(self.root, text="Monitor de Productividad para Procesos Industriales (MPPI)", font=("Verdana", 28), relief="groove", background='#184B6C', fg='white').grid(row=1, column=0, columnspan=5, sticky='ewns')
        texto = Label(self.root, text="Resumen de la configuración", relief='groove',font=("Verdana", 22), background='#2980B9')
        texto.grid(row=2, column=0, columnspan=5, sticky="ewns")
        Label(self.root, text="", background=self.color_fondo).grid(row=3, column=0, columnspan=5, pady=5)
        
        #Se crea la tabla donde se mostrarán los datos de la lista
        self.tabla_frame = Frame(self.root, background=self.color_fondo_tabla, pady=20)
        self.tabla_frame.grid(row=5, column=0, columnspan=5, rowspan=2, sticky="nsew")
        opciones_frame = Frame(self.root, background=self.color_fondo, pady=10)
        opcion_editar = StringVar()
        opcion_editar.set(1)
        tam_lista = len(lista_configuracion)
        imagen_box = ttk.Spinbox(opciones_frame, from_=1, to=tam_lista, increment=1, state="readonly", width=4, font=("verdana", 12), textvariable=opcion_editar)
        imagen_box.grid(column=0, row=0, sticky="e", padx=10, ipady=4)
        
        #Botón para seleccionar la imagen que se desea editar
        Button(opciones_frame, text="Editar", font=("Verdana", 12), command=lambda: self.editar_opcion(opcion_editar.get())).grid(column=1, row=0, ipadx=10, sticky='w', padx=10)
        Label(opciones_frame, text= "Seleccione una imagen para editar", font=("Verdana", 12), background=self.color_fondo).grid(column=0, row=1, columnspan=2, pady=5)
        
        #Botón para mostrar la venta de visualización de la configuración completa 
        Button(opciones_frame, text="Visualizar\nConfiguración", font=("Verdana", 12), command=self.visualizar_resumen).grid(ipadx=10, padx=15, column=4, row=0, rowspan=2, sticky='ns')
        opciones_frame.grid(row=7, column=0, columnspan=5, sticky="ews")
        
        #Establecer la importancia de las filas y columnas
        opciones_frame.columnconfigure(0, weight=1)
        opciones_frame.columnconfigure(1, weight=1)
        opciones_frame.columnconfigure(2, weight=1)
        opciones_frame.columnconfigure(3, weight=1)
        opciones_frame.columnconfigure(4, weight=1)
        
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=8, column=0, columnspan=5, sticky="ews")
        
        #Cargar imagen y colocarla en un botón
        imgSalir = Image.open("./iconos/deshacer.png")
        imgSalir = imgSalir.resize((30, 30))
        imgSalir = ImageTk.PhotoImage(imgSalir)
        botonSalir = Button(self.root, image=imgSalir, text="Salir   ", compound="right", font=("Verdana", 12), activebackground="#999999", command=self.salir)
        botonSalir.grid(row=9, column=0, ipadx=20, padx=15, pady=15, sticky="es")
        botonSalir.image = imgSalir

        #Cargar imagen y colocarla en un botón
        imgSave=Image.open("./iconos/upload.png")
        imgSave = imgSave.resize((30, 30))
        imgSave = ImageTk.PhotoImage(imgSave)
        botonSave = Button(self.root, image=imgSave, text="Envíar configuración   ", compound="right", font=("Verdana", 12), activebackground="#999999", command=self.enviar_configuracion)
        botonSave.grid(row=9, column=3, ipadx=15, padx=10, pady=15, sticky="es")
        botonSave.image = imgSave

        #Cargar imagen y colocarla en un botón
        imgSave=Image.open("./iconos/save.png")
        imgSave = imgSave.resize((30, 30))
        imgSave = ImageTk.PhotoImage(imgSave)
        botonSave = Button(self.root, image=imgSave, text="Guardar  ", compound="right", font=("Verdana", 12), activebackground="#999999", command=self.guardar_configuracion)
        botonSave.grid(row=9, column=4, ipadx=15, padx=15, pady=15, sticky="s")
        botonSave.image = imgSave

        #Establecer la importancia de las filas y columnas
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
    
    #Función para cerrar y destruir la ventana
    def destruir(self):
        self.root.destroy()

    #Función para mostrar el contenido de la pantalla
    def mostrar(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    #Función para ir a la pantalla de configuración y editar los parametros o imagen de una opción de la lista
    def editar_opcion(self, opcion_numero):
        self.destruir()
        configuracion_resumen = ConfiguracionResumen()
        configuracion_resumen.cargar()
        configuracion_resumen.llenar_configuracion(int(opcion_numero))
        configuracion_resumen.mostrar()

    #Función para cambiar el estado de guardado de la lista de configuración
    def estado_guardar(self, estado):
        self.estado_guardado = estado
        
    #Función para mostrar la ventana de visualización de la lista de configuración
    def visualizar_resumen(self):
        vis = VisualizarResumen()
        vis.mostrar()
    
    #Función para llenar la tabla de configuración 
    def llenar_tabla(self):
        #Se crea un lienzo para colocar la tabla y el Scrollbar vertical
        canvas = Canvas(self.tabla_frame, bg=self.color_fondo_tabla)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        vsbar = Scrollbar(self.tabla_frame, orient=VERTICAL, command=canvas.yview) 
        vsbar.pack(side=RIGHT, fill=Y)
        #Se asocia el Scrollbar a la tabla de configuración
        canvas.configure(yscrollcommand=vsbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion= canvas.bbox("all")))
        contenedor_canvas = Frame(canvas, background=self.color_fondo_tabla, padx=150)   
        canvas.create_window((0,0), window=contenedor_canvas)
    
        #Se dibujan las columnas de la tabla de configuración
        ttk.Separator(contenedor_canvas, orient=HORIZONTAL).grid(row=0, column=1, columnspan=4, sticky="ews")
        Label(contenedor_canvas, text="Imagen", font=("Verdana", 14, 'bold'), background=self.color_fondo_tabla, padx=65).grid(row=1, column=1, pady=10)
        Label(contenedor_canvas, text="Vista", font=("Verdana", 14, 'bold'), background=self.color_fondo_tabla, padx=65).grid(row=1, column=2, pady=10)
        Label(contenedor_canvas, text="Efecto", font=("Verdana", 14, 'bold'), background=self.color_fondo_tabla, padx=65).grid(row=1, column=3, pady=10)
        Label(contenedor_canvas, text="Tiempo", font=("Verdana", 14, 'bold'), background=self.color_fondo_tabla, padx=65).grid(row=1, column=4, pady=10)
        ttk.Separator(contenedor_canvas, orient=HORIZONTAL).grid(row=2, column=1, columnspan=4, sticky="ews")
        ttk.Separator(contenedor_canvas, orient=VERTICAL).grid(row=1, column=0, sticky="nse", rowspan=2)
        ttk.Separator(contenedor_canvas, orient=VERTICAL).grid(row=1, column=5, sticky="nsw", rowspan=2)
        filas = 2
        
        #Ciclo para colocar las imagenes y sus argumentos en cada fila de la tabla
        for i, item in enumerate(lista_configuracion):
            #Se obtienen los datos de cada item de la lista de configuración 
            indice = i + 1
            imagen = item.get_imagen()
            efecto = self.nombre_efecto(item.get_efecto())
            tiempo = self.tiempo_formato(item.get_tiempo())
            
            #Se carga la imagen, se redimensiona y se coloca junto con los datos de presentación en la fila correspondiente
            imagen_muestra = Image.open(imagen) 
            imagen_muestra = imagen_muestra.resize((110,50))
            imagen_muestra = ImageTk.PhotoImage(imagen_muestra)
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

            #Establecer importancia de las filas y columnas de la pantalla.
            contenedor_canvas.grid_columnconfigure(0, weight=1)
            contenedor_canvas.grid_columnconfigure(1, weight=1)
            contenedor_canvas.grid_columnconfigure(2, weight=1)
            contenedor_canvas.grid_columnconfigure(3, weight=1)
            contenedor_canvas.grid_columnconfigure(4, weight=1)
            contenedor_canvas.grid_columnconfigure(5, weight=1)
    
    #Función para intercambiar los nombres de los efectos, por los nombres de archivo en Python         
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
     
     #Función para transformar el formato de tiempo. De munutos:segundos a solo segundos.   
    def tiempo_formato(self, tiempo):
        minutos = int(int(tiempo) / 60)
        segundos = int(tiempo) % 60
        return '{:02}:{:02} minutos'.format(minutos, segundos)
     
    #Se almacena en la variable 'self.ruta_guardar' la ruta del archivo de configuración
    def establecer_ruta(self, ruta):
        self.ruta_guardar = ruta
        
    #Función para enviar la configuración a la raspberry a través de un servidor LAN. 
    #Esta función, opera como el cliente, mientras que el servidor se encuentra alojado en la raspberry
    def enviar_configuracion(self):
        #Si aún no se ha guardado la configuración, se solicita al usuario guardarla.
        if self.ruta_guardar == '':
            self.guardar_configuracion()
        else:
            #La variable dir_zip indica el directorio de un archivo comprimido (.zip)
            #En este archivo se almacenará el archivo 'configuración.txt' y la carpeta con las imágenes necesarias
            dir_zip = self.ruta_guardar[:-13] + './config.zip'
            dir_config = ZipFile(dir_zip, 'w')
            print('ruta de enviar: ' + self.ruta_guardar)
            #Ciclo para recorrer el directorio donde se encuentra guardada la configuración
            for folder, subfolders, files in os.walk(f'{self.ruta_guardar}'):
                #Pora cada archivo con extensión .txt o .ppm dentro del directorio o subdirectorios, se añade al archivo comprimido 
                for file in files:
                    if file.endswith('.txt') or file.endswith('.ppm'):
                        #Obtener una ruta relativa para almacenar los archivos de configuración en el archivo comprimido.
                        #Al usar la ruta relativa, se evita colocar toda la cadena de carpetas hasta llegar al archivo deseado
                        dir_config.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), dir_zip), compress_type = ZIP_DEFLATED)
            dir_config.close()
           
            #Función para enviar el archivo de configuración a la raspberry 
            def send_file(sck: socket.socket, filename):
                # Obtener el tamaño del archivo a enviar.
                filesize = os.path.getsize(filename)
                # Informar primero al servidor la cantidad
                # de bytes que serán enviados. 
                sck.sendall(struct.pack("<Q", filesize))  
                # Enviar el archivo en bloques de 1024 bytes.
                with open(filename, "rb") as f:
                    while read_bytes := f.read(1024):
                        sck.sendall(read_bytes)

            #Intentar conectarse con el servidor de la raspberry
            try:
                #Si se logra la conexión, se envía el archivo
                with socket.create_connection(("192.168.1.110", 6190)) as conn:
                    print("Conectado al servidor.")
                    print("Enviando archivo...")
                    send_file(conn, dir_zip)
                    print("Enviado.")

                print("Conexión cerrada.")
                messagebox.showinfo("Monitor de Productividad para Procesos Industriales (MPPI)", "Se ha enviado la configuracion")
            #Si no se logra establecer conexión con el servidor, se muestra un mensaje de error.
            except:
                messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "No se ha podido establecer conexión")

    #Función para guardar la configuración hecha por el usuario
    def guardar_configuracion(self):
        #Solicirar al usuarioi una ruta sonde se guardará la configuración
        self.ruta_guardar = filedialog.askdirectory()
        
        #Si el directorio indicado es válido, se guarda la configuración
        if self.ruta_guardar != '':
            print(self.ruta_guardar)
            #Si no existen las carpetas de 'Configuracion' y 'Configuración/Imagenes', se crean
            if not os.path.exists(f'{self.ruta_guardar}/Configuracion/Imagenes'):
                os.mkdir(f'{self.ruta_guardar}/Configuracion')
                os.mkdir(f'{self.ruta_guardar}/Configuracion/Imagenes')
                #Se crea el archivo 'configuracion.txt'
            archivo_configuracion = open (f'{self.ruta_guardar}/Configuracion/configuracion.txt','w')          
            self.ruta_guardar = self.ruta_guardar + '/Configuracion'
            print('ruta_guardar = ' , self.ruta_guardar)
            
            configuracion_completa = ''
            
            #Ciclo para recorrer todos los elementos de la lista de configuración
            for i in lista_configuracion:
                #Para cada elemento de la lista, se obtiene la ruta de las imagen y los parámetros de desplegado de la imagen
                indice = int(i.get_numero()) + 1
                imagen_ruta = i.get_imagen()
                efecto = i.get_efecto()
                tiempo = i.get_tiempo()
                
                nombre_imagen = self.imagen_nombre(imagen_ruta)
                
                #Se abre la imagen y se redimensiona a 128x48 pixeles
                img = Image.open(imagen_ruta)
                img = img.resize((128,48))
                #Se almacena la imagen con extendión '.ppm' en la carpeta de Imagenes
                img.save(f'{self.ruta_guardar}/Imagenes/{nombre_imagen}.ppm')
                
                #Con los datos del elemento de la lista de configuración, se forma una cadena de texto, utilizando el formato específico
                configuracion_datos = f'Datos{indice}\n{efecto}\n{nombre_imagen}.ppm\n{tiempo}\n'
                
                #Se añade a la variable 'configuración_completa' la cadena de texto formada para cada elemento de la lista
                configuracion_completa = configuracion_completa + configuracion_datos
            
            print(lista_configuracion)
            #Se escribe en el archivo 'configuracion.txt' la cadena de texto con el formato específico
            archivo_configuracion.write(configuracion_completa)
            archivo_configuracion.close()
            messagebox.showinfo("Monitor de Productividad para Procesos Industriales (MPPI)", "Se han guardado la configuracion")
            self.estado_guardado = True
        else:
            pass
        
    #Función para obtener el nombre de una imagen a partir de la ruta del archivo
    def imagen_nombre(self, imagen):
        #Se recorre de forma inversa la ruta de una imagen
        for i in range(len(imagen)):
            #Al enncontrar el caracter '/', se corta la ruta de la imagen
            if(imagen[-i] == '/'):
                nombre_imagen = imagen[-i+1:]
                break
        #De la misma forma, ahora se elimina la extensión
        #Se recorre de forma inversa la ruta
        for i in range(len(nombre_imagen)):
            #Al encontrar un punto, se corta el la extension para obtener solo el nombre de la imagen
            if(nombre_imagen[-i] == '.'):
                nombre_imagen = nombre_imagen[:-i]
                print(nombre_imagen)
                break    
        
        #La función regresa una cadena de texto con el nombre de la imagen sin extensión
        return nombre_imagen

    #Función para ceerar la ventana de Resumen
    def salir(self):
        #Si la lista de configuración tiene datos, se pregunta al usuario si desea regresar, ya que los cambios en la lista se perderán
        if self.estado_guardado == False:
            decision = messagebox.askokcancel("Monitor de Productividad para Procesos Industriales (MPPI)", "Está a punto de cerrar el programa.\n Todos los cambios realizados serán borrados.\n¿Desea continuar?")
            if(decision == True):
                self.destruir()
        #Si no se hizo ningún cambio, se puede cerrar la ventana
        else:
            self.destruir()
            
    def on_closing(self):
        self.salir()         
########################Termina Resumen#################################


########################Configuracion Resumen#################################
#Esta clase es una copia de la ventana de Configuración, con algunas adaptaciones para tener un comportamiendo limitado
class ConfiguracionResumen:
    #Variables para almacenar los parámetros de presentación de una imagen
    #   Ruta de la imagen
    #   Nombre del efecto de entrada
    #   Tiempo: minutos y segundos
    def __init__(self):
        self.imagen_ruta = ''
        self.label_imagen = ''
        self.imagenFrame = 0
        self.opcion_efecto = None
        self.minutos = 0
        self.segundos = 0
        self.numero_imagen_editar = 0
        
        self.title = "Monitor de Productividad para Procesos Industriales (MPPI)"
        self.icon = "./iconos/main.ico"
        self.resizable = True
        self.root = "Tk()"
        self.colorFondo = '#E2EFFF'
        
    #Función para cargar los elementos de la ventana
    def cargar(self):
        self.root = Tk()
        self.root.title(self.title)
        icono = os.path.abspath(self.icon)
        self.root.iconbitmap(icono)
        ancho = 1450
        alto = 830
        # winfo da el tamaño de la pantalla en ancho y en alto
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2  
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        #Colocar la ventana en el centro de la pantalla
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana) + "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background=self.colorFondo)


        if self.resizable:
            self.root.resizable(1, 1)
        else:
            self.root.resizable(0, 0)

        #Cargar imagen y colocarla en el encabezado de la ventana.
        uama = Image.open("./recursos/uamazc.jpg")
        uama = uama.resize((280, 110))
        uama = ImageTk.PhotoImage(uama)
        uamA = Label(self.root, image=uama, width=260, height=80, padx=100, background='white')
        uamA.image = uama
        uamA.grid(row=0, column=0, sticky='ewns')

        #Cargar imagen y colocarla en el encabezado de la ventana.
        electronica = Image.open("./recursos/electronica.jpg")
        electronica = electronica.resize((240, 120))
        electronica = ImageTk.PhotoImage(electronica)
        electronicaLabel = Label(self.root, image=electronica, width=220, height=80, padx=100, background='white')
        electronicaLabel.image = electronica
        electronicaLabel.grid(row=0, column=1, columnspan=3, sticky='ewns')

        #Cargar imagen y colocarla en el encabezado de la ventana.
        cbi = Image.open("./recursos/cbi.png")
        cbi = cbi.resize((240, 120))
        cbi = ImageTk.PhotoImage(cbi)
        CBI = Label(self.root, image=cbi, width=220, height=80, padx=100, background='white')
        CBI.image = cbi
        #Establecer una configuración de rejilla (filas y columnas) para la ventana
        CBI.grid(row=0, column=4, sticky='ewns')

        #Colocar e título en el encabezado de la ventana.
        titulo = Label(self.root, text="Monitor de Productividad para Procesos Industriales (MPPI)", font=("Verdana", 28), relief="groove", background='#184B6C',
                       fg='white').grid(row=1, column=0, columnspan=5, sticky='ewns')
        texto = Label(self.root, text="Configurar imagen para mostrar en la pantalla RGB", relief='groove',
                      font=("Verdana", 22), background='#2980B9')
        texto.grid(row=2, column=0, columnspan=5, sticky="ewns")
        Label(self.root, text="", background=self.colorFondo).grid(row=3, column=0, columnspan=5, pady=5)

        #Líneas horizontales y verticales para hacer separadores
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=4, column=0, columnspan=5, sticky="ews")
        ttk.Separator(self.root, orient=VERTICAL).grid(row=5, column=2, rowspan=5, sticky="ns")
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=7, column=3, columnspan=2, sticky="ewn")
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=10, column=0, columnspan=5, sticky="ewn")

        #Frame dedicado para colocar la imagen seleccionada por el usuario
        self.imagenFrame = Frame(self.root, background=self.colorFondo, pady=10)
        Label(self.imagenFrame, text="Selecciona una imagen para\nmostrar en la pantalla RGB", font=("verdana", 18), padx=10,
              background=self.colorFondo).grid(row=0, column=0, sticky="n")
        
        #Cargar imagen y colocarla en un botón
        imgImagen = Image.open("./iconos/cargar-imagen.png")
        imgImagen = imgImagen.resize((30, 30))
        imgImagen = ImageTk.PhotoImage(imgImagen)
        
        #Al dar click en el botón, se ejecuta la función 'self.selectImagen(imagenFrame)' a la que se le envía como parámetro la imagen que fue seleccionada previamente por el usuario 
        #command=lambda: 'function' indica la definición de una función, por lo que dicha función NO se ejecutará al enviarla como parámetro.
        botonCargar = Button(self.imagenFrame, text="Cargar imagen   ", image=imgImagen, compound="right",
                             font=("verdana", 14), command=lambda: self.selecImagen(self.imagenFrame))
        botonCargar.grid(row=1, column=0, pady=30)
        botonCargar.image = imgImagen

        Label(self.imagenFrame, height=16, width=100, background=self.colorFondo).grid(column=0, row=2, sticky=N)

        #Establecer la importancia de las filas y columnas
        self.imagenFrame.grid_columnconfigure(0, weight=1)
        # imagenFrame.rowconfigure(0, weight=1)
        self.imagenFrame.rowconfigure(1, weight=1)
        self.imagenFrame.rowconfigure(2, weight=1)
        self.imagenFrame.grid(row=6, column=0, columnspan=2, rowspan=5, sticky="ns", pady=20)

        #Frame para la selección del efecto de entrada
        parametros = Frame(self.root, background=self.colorFondo)
       
        #La variable 'self.opcion_efecto' almacena la opción de efecto seleccionada por el usuario y se encuentra vacía al principio
        self.opcion_efecto = StringVar()
        self.opcion_efecto.set(None)

        #Los efectos de entradda se colocan en botones de selección, el usuario puede seleccionar sólo un efecto y esta selección se almacena en la variable 'self.opcion_efecto'
        Label(parametros, text="Selecciona el efecto de entrada de la imagen", font=("Verdana", 18), background=self.colorFondo).grid(column=0, row=0, columnspan=3)
        
        #Botón de selección para efecto 'Instanteneo'
        Radiobutton(parametros, text="Instantaneo", font=("verdana", 14), variable=self.opcion_efecto, value='Instantaneo.py', background=self.colorFondo).grid(column=0, row=1)
        #Botón de selección para efecto 'De abajo a arriba'
        Radiobutton(parametros, text="De abajo a arriba", font=("verdana", 14), variable=self.opcion_efecto, value='AbajoArriba.py', background=self.colorFondo, padx=20).grid(column=1, row=1, sticky="ew")
        #Botón de selección para efecto 'Aleatorio'
        Radiobutton(parametros, text="Aleatorio", font=("verdana", 14), variable=self.opcion_efecto, value='Aleatorio.py', background=self.colorFondo).grid(column=2, row=1, sticky="e")
        #Botón de selección para efecto 'De derecha a izquierda'
        Radiobutton(parametros, text="De derecha a izquierda", font=("verdana", 14), variable=self.opcion_efecto, value = 'DerechaIzquierda.py', background=self.colorFondo).grid(column=0, row=2, sticky="e")
        #Botón de selección para efecto 'De arriba a abajo'
        Radiobutton(parametros, text="De arriba a abajo", font=("verdana", 14), variable=self.opcion_efecto, value='ArribaAbajo.py', background=self.colorFondo).grid(column=2, row=2, sticky="w")
        
        Label(parametros, text="", background=self.colorFondo).grid(column=0, row=3, columnspan=3)
        
        #Establecer la importancia de las filas y columnas
        parametros.rowconfigure(0, weight=1)
        parametros.rowconfigure(1, weight=1)
        parametros.rowconfigure(2, weight=1)
        parametros.rowconfigure(3, weight=1)
        parametros.grid(column=3, row=5, columnspan=2, rowspan=2, sticky='ns')

        #Frame para la selección del tiempo de presentación
        tiempo = Frame(self.root, background=self.colorFondo)
        Label(tiempo, text="Seleccione el tiempo de desplegado de la imagen", font=("Verdana", 18), pady=14,
              background=self.colorFondo).grid(column=0, row=0, columnspan=2)
        
        #La variable 'self.minutos' almacena el tiempo en minutos, indicado por el usuario
        self.minutos = StringVar()
        
        #La selección del tiempo en minutos se hace a través de una caja que recibe valores numéricos
        Label(tiempo, text="minutos:", font=("verdana", 14), background=self.colorFondo).grid(column=0, row=1, sticky="we")
        minutosBox = ttk.Spinbox(tiempo, from_=0, to=4, increment=1, width=4, font=("verdana", 14), textvariable=self.minutos)
        minutosBox.grid(column=0, row=2, sticky='n', pady=5)
        
        #La variable 'self.segundos' almacena el tiempo en segundos, indicado por el usuario
        self.segundos = StringVar()
        
        #La selección del tiempo en segundos se hace a través de una caja que recibe valores numéricos
        Label(tiempo, text="segundos:", font=("verdana", 14), background=self.colorFondo).grid(column=1, row=1, sticky="we")
        segundosBox = ttk.Spinbox(tiempo, from_=0, to=59, increment=1, width=4, font=("verdana", 14), textvariable=self.segundos)
        segundosBox.grid(column=1, row=2, sticky='n', pady=5)
        
        #Establecer el orden e importancia de las filas y columnas de la ventana
        tiempo.grid(row=8, column=3, columnspan=2, rowspan=2, sticky="ns")
        tiempo.grid_rowconfigure(0, weight=1)
        tiempo.grid_rowconfigure(1, weight=1)
        tiempo.grid_rowconfigure(2, weight=1)

        #Cargar imagen y colocarla en un botón
        imgAgregar = Image.open("./iconos/anadir-imagen.png")
        imgAgregar = imgAgregar.resize((30, 30))
        imgAgregar = ImageTk.PhotoImage(imgAgregar)
        botonAgregar = Button(self.root, text="Guardar cambios ", image=imgAgregar, compound="right",
                              font=("verdana", 14), command=self.guardar_cambios)
        botonAgregar.grid(column=1, row=11, pady=15, sticky='n')
        botonAgregar.image = imgAgregar

        #Cargar imagen y colocarla en un botón
        imgVisualizar = Image.open("./iconos/play.png")
        imgVisualizar = imgVisualizar.resize((30, 30))
        imgVisualizar = ImageTk.PhotoImage(imgVisualizar)
        botonVisualizar = Button(self.root, text="Visualizar  ", image=imgVisualizar, compound="right",
                                 font=("verdana", 14), command=self.visualizar)
        botonVisualizar.grid(column=3, row=11, pady=15, sticky='n')
        botonVisualizar.image = imgVisualizar

        #Cargar imagen y colocarla en un botón
        imgTerminar = Image.open("./iconos/next.png")
        imgTerminar = imgTerminar.resize((30, 30))
        imgTerminar = ImageTk.PhotoImage(imgTerminar)
        botonTerminar = Button(self.root, text="Regresar al resumen  ", image=imgTerminar, compound="right", font=("verdana", 14),
                               command=self.terminar)
        botonTerminar.grid(column=4, row=11, pady=15, sticky='n')
        botonTerminar.image = imgTerminar

        #Establecer la importancia de las filas y columnas
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(8, weight=1)
    
    #Función para seleccionar la imagen que desea agrgarse a la configuración 
    def selecImagen(self, imagenFrame):
        
        #Solicitud para que el usuario seleccione una imagen utilizando el explorador de archivos del Sistema Operativo
        archivo = filedialog.askopenfilename(filetypes=[('Archivos de imagen', '*.jpg *.png *.jpeg *.ppm')])

        #Si el archivo seleccionado es válido, se abre el archivo, se redimensiona y se coloca en el freame que corresponde. La imagen se redimensiona a 640x240 unicamente para mostrarse en la ventana
        # La ruta de la imagen se almacena en la variable 'self.imagen_ruta'
        if archivo is not None:
            imagenEntrada = Image.open(archivo)
            imagenEntrada = imagenEntrada.resize((640, 240)) 
            ImagenEntrada = ImageTk.PhotoImage(imagenEntrada)
            self.label_imagen = Label(imagenFrame, background=self.colorFondo)
            self.label_imagen.config(image = ImagenEntrada)
            self.label_imagen.image = ImagenEntrada
            self.label_imagen.grid(column=0, row=2, sticky=N)
            self.label_imagen.config(relief="solid")
            self.imagen_ruta = archivo

    #Función para cerrar y destruir la ventana.
    def destruir(self):
        self.root.destroy()

    #Función para mostrar el contenido de la ventana.
    def mostrar(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    #Función para guardar los cambios realizados en la lista de configuración
    def guardar_cambios(self):
        #Si no se selecciona algún parámetro, se muestra un mensaje de error
        if (self.imagen_ruta == '' or self.opcion_efecto.get() == 'None' or self.minutos.get() == '' or self.segundos.get() == ''):
            messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "Debe llenar todos los campos.")
        #Si el valor del tiempo en minutos es mayor a 4, se muestra un mensaje de error
        elif (int(self.minutos.get()) > 4):
                messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "El valor de los minutos debe ser menor a 5.")
        #Si el valor del tiempo en segundos es mayor a 59, se muestra un mensaje de error 
        elif (int(self.segundos.get()) > 59):
                messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "El valor de los segundos debe ser menor a 60.")
        #Si se colocan todos los parámetros de manera correcta, se agrega la imagen y sus parámetros a la lista de configuración
        else:
            numero_imagen = self.numero_imagen_editar
            tiempo = (int(self.minutos.get()) * 60) + int(self.segundos.get())
            lista_configuracion[numero_imagen].set_numero(self.numero_imagen_editar)
            lista_configuracion[numero_imagen].set_imagen(self.imagen_ruta)
            lista_configuracion[numero_imagen].set_efecto(self.opcion_efecto.get())
            lista_configuracion[numero_imagen].set_tiempo(tiempo)
            messagebox.showinfo("Monitor de Productividad para Procesos Industriales (MPPI)", "Se han guardado los cambios con éxito")        
    
    #Función para colocar en la ventana, la imagen correspondiente al número de la lista que se seleccinó para editar desde la ventana de Resumen
    def set_imagen(self, archivo):
        #Si el archivo seleccionado es válido, se abre el archivo, se redimensiona y se coloca en el freame que corresponde. La imagen se redimensiona a 640x240 unicamente para mostrarse en la ventana
        # La ruta de la imagen se almacena en la variable 'self.imagen_ruta'
        if archivo is not None:
            imagenEntrada = Image.open(archivo)
            imagenEntrada = imagenEntrada.resize((640, 240))
            ImagenEntrada = ImageTk.PhotoImage(imagenEntrada)
            self.label_imagen = Label(self.imagenFrame, background=self.colorFondo)
            self.label_imagen.config(image = ImagenEntrada)
            self.label_imagen.image = ImagenEntrada
            self.label_imagen.grid(column=0, row=2, sticky=N)
            self.label_imagen.config(relief="solid")
            self.imagen_ruta = archivo

    #Función para llenar los campos la ventana con los datos de la imagen seleccionada para editar desde la ventana de Resumen
    def llenar_configuracion(self, numero_imagen):
        #Se obtiene el índice de la imagen seleccionada para editar
        self.numero_imagen_editar = numero_imagen - 1
        #Se obitne el elemento de la lista, utilizando el índice
        datos_editar = lista_configuracion[self.numero_imagen_editar]
        #Se obtienen los parámetros de desplegado
        datos_numero = datos_editar.get_numero()
        datos_imagen = datos_editar.get_imagen()
        datos_efecto = datos_editar.get_efecto()
        datos_tiempo = datos_editar.get_tiempo()
        
        #Se transforman los tipos de dato de las variables minutos y segundos a tipo entero
        minutos = int(int(datos_tiempo) / 60)
        segundos = int(datos_tiempo) % 60
        
        #Indicar a las variables propias de la clase, los parámetros de la imagen
        self.set_imagen(datos_imagen)
        self.opcion_efecto.set(datos_efecto)
        self.minutos.set(minutos)
        self.segundos.set(segundos)

    #Función para mostrar la ventana de visualización de la imagen con los parámetros indicados en ese momento
    def visualizar(self):
        #Si no se selecciona algún parámetro, se muestra un mensaje de error
        if (self.imagen_ruta == '' or self.opcion_efecto.get() == 'None' or self.minutos.get() == '' or self.segundos.get() == ''):
            messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "Debe llenar todos los campos.")
        #Si el valor del tiempo en minutos es mayor a 4, se muestra un mensaje de error
        elif (int(self.minutos.get()) > 4):
                messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "El valor de los minutos debe ser menor a 5.")
        #Si el valor del tiempo en segundos es mayor a 59, se muestra un mensaje de error  
        elif (int(self.segundos.get()) > 59):
                messagebox.showwarning("Monitor de Productividad para Procesos Industriales (MPPI)", "El valor de los segundos debe ser menor a 60.")
        #Si se colocan todos los parámetros de manera correcta, se agrega la imagen y sus parámetros a la lista de configuración        
        else:
            tiempo = (int(self.minutos.get()) * 60) + int(self.segundos.get())
            print(f'Imagen: {self.imagen_ruta}\n Efecto: {self.opcion_efecto.get()}\n Tiempo: {tiempo}')
            #Se construye una variable de tipo datos con la imagen y parámetros seleccionados en la ventana
            datos = Datos(len(lista_configuracion), self.imagen_ruta, self.opcion_efecto.get(), tiempo)
            #Envía los parámetros a la venta de visualización y se muestra
            visualizar = Visualizar(datos)
            visualizar.mostrar()

    #Función para avanzar a la ventana de resumen 
    def terminar(self):
        self.destruir()
        resumen = Resumen()
        resumen.estado_guardar(False)
        resumen.cargar()
        resumen.llenar_tabla()
        resumen.mostrar()

    #Se limpian todos los campos de la ventana, incluyendo la imagen 
    def limpiar_configuracion(self):
        self.imagen_ruta = ''
        self.label_imagen.config(image = None)
        self.label_imagen.config(relief = "flat") 
        self.label_imagen.image = None   
        self.opcion_efecto.set(None)
        self.minutos.set("")
        self.segundos.set("")
    
    
    def on_closing(self):
        decision = messagebox.askokcancel("Monitor de Productividad para Procesos Industriales (MPPI)", "Todos los cambios realizados serán borrados.")
        if(decision == True):
            self.destruir()    
########################Termina Configuracion Resumen#################################


########################Visualizar#################################
#Ventana para visualizar los efectos de entrada de las imágenes
class Visualizar:
    
    #Recibe como parámetro una variable de tipo Datos.
    def __init__(self, datos):
        #Iniciar el proceso 'pygame'
        pygame.init()
        
        #Variables para almacenar los datos necesarios para desplegar una imagen
        self.presentacion_nombre = str(datos.get_numero())
        self.presentacion_imagen = datos.get_imagen()
        self.presentacion_efecto = datos.get_efecto()
        self.presentacion_tiempo = str(datos.get_tiempo())
        
        #Tamaño de la ventana
        self.size = (1200, 560)
        self.ventana = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Monitor de Productividad para Procesos Industriales (MPPI)")
        icono = pygame.image.load("./iconos/main.png")
        pygame.display.set_icon(icono)
        
        self.cargar_elementos()        
        
    #Función para cargar los elemntos de la ventana
    def cargar_elementos(self):
        self.blanco = (255,255,255)
        self.silver = (192,192,192)
        self.negro = (0,0,0)
        self.gray = (128,128,128)
        self.lightblue = (173,216,230)

        #Cargar imagen y colocarla en el encabezado
        uam = pygame.image.load("./recursos/uamazcL.png")
        self.uamAzc = pygame.transform.scale(uam, (300, 80))
        #Cargar imagen y colocarla en el encabezado
        cbi = pygame.image.load("./recursos/cbi.png")
        self.cbiAzc = pygame.transform.scale(cbi, (300, 80))

        #Variable para colocar la imagen 
        prueba = pygame.image.load(self.presentacion_imagen)
        self.pruebaR = pygame.transform.scale(prueba, (360, 140))

        #Colocar los elementos en la ventana 
        miFuente = pygame.font.SysFont("Verdana", 30)
        self.text = miFuente.render("Visualización de animación", 0, (self.negro))
        fuente = pygame.font.SysFont("Verdana", 25)
        self.nom_Imagen = fuente.render("Número de imagen: ", 0, (self.negro))
        self.nombre_imagen = fuente.render(self.presentacion_nombre, 0, (self.negro))
        self.nomEfecto = fuente.render("Efecto: ", 0, (self.negro))
        self.letrero_efecto = fuente.render(self.nombre_efecto(self.presentacion_efecto), 0, (self.negro))
        self.tiempo = fuente.render("Tiempo(segundos): ", 0, (self.negro))
        self.seg = fuente.render(self.presentacion_tiempo, 0, (self.negro))

        #Creación de botones de 'Play' y 'Regresar'
        self.play = Rect(635, 500, 70, 25)
        self.regresar = Rect(1085, 500, 70, 25)
        self.fuente2 = pygame.font.SysFont("Calibri", 20)
        

    #Función para crear un botón utilizando un rectángulo
    def crearBoton(self, screen, boton, mensaje):
        #Si el cursor está colocado sobre el botón, este cambia de color
        if boton.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.ventana, self.silver, boton)
        else:
            pygame.draw.rect(self.ventana, self.gray, boton)
        texto = self.fuente2.render(mensaje, True, (self.blanco))
        screen.blit(texto, (boton.x+(boton.width-texto.get_width())/2,
        boton.y+(boton.height-texto.get_height())/2)
        )


    #Función para mostar el contenido de la ventana
    def mostrar(self): 

        #El contenido de la ventana se actualiza a 20 frame por segundo (FPS)
        self.clock = pygame.time.Clock()
        self.FPS = 20

        coordenada_x_inicial = -250
        coordenada_y_inicial = -250

        #Ciclo para mostrar constantemente el contenido de la ventana
        while True:
           #Cuando se desea cerrar la ventana, se termina el proceso 'pygame'  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.mostrar_ventana()
            
            #Cuando se oprime el botón de salir, se termina el proceso 'pygame'
            if event.type == MOUSEBUTTONDOWN:
                if self.regresar.collidepoint(pygame.mouse.get_pos()):
                    self.salir()

            #Cuando se selecciona el botón 'Play', se ejecuta la función para desplegar la animación
            if event.type == MOUSEBUTTONDOWN and event.button == 1:     
                if self.play.collidepoint(pygame.mouse.get_pos()): 
                    self.presentar_efecto()     
                    coordenada_x_inicial = 720
                    coordenada_y_inicial = 250
            
            #Dejar la imagen fija en la ventana después de realizar el efecto de desplegado
            self.ventana.blit(self.pruebaR, (coordenada_x_inicial, coordenada_y_inicial))

            #Actualizar contenido de la ventana
            pygame.display.flip()
            self.clock.tick(self.FPS)
            
    #Función para terminar el proceso 'pygame'
    def salir(self):
        pygame.quit()

    #Mostrar los elementos en la ventana
    def mostrar_ventana(self):
        #Color de fondo, imagenes, separadores y letreros
        self.ventana.fill(self.blanco)    
        self.ventana.blit(self.uamAzc, (50, 20))
        self.ventana.blit(self.text, (400,40))
        self.ventana.blit(self.cbiAzc, (850, 20))
        pygame.draw.line(self.ventana, self.negro, (0,120), (1200,120), 5)
        pygame.draw.line(self.ventana, self.negro, (600,120), (600,600), 5)
        pygame.draw.rect(self.ventana, self.silver, (720, 250, 360, 140))           
        self.ventana.blit(self.nom_Imagen, (130,225))
        self.ventana.blit(self.nombre_imagen, (400,225))
        self.ventana.blit(self.nomEfecto, (130,295))
        self.ventana.blit(self.letrero_efecto, (240, 295))
        self.ventana.blit(self.tiempo, (130,365))
        self.ventana.blit(self.seg, (385,365))          

        #Botones
        self.crearBoton(self.ventana, self.play, "Play")
        self.crearBoton(self.ventana, self.regresar, "Salir")
      
    #Función para obtener el nombre de un efecto a partir del nombre del archivo en Python
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

    #Función para desplegar una imagen en la pantalla, utilizando alguno de los efectos disponibles
    def presentar_efecto(self):
        #Cargar imaagen 
        prueba = pygame.image.load(self.presentacion_imagen)
        #Se redimensiona la imagen a 360x140 pixeles para mostrarla en la ventana 
        pruebaR = pygame.transform.scale(prueba, (360, 140))
        imagen = pruebaR
        efecto = self.presentacion_efecto
        
        #Efecto Aleatorio
        #Para realizar este efecto, Se crean varios cuadros pequeños que en conjunto cubren la imagen, de forma aleatoria, los cuadros desaparecen uno a uno hasta descubrir la imagen completamente
        if efecto == 'Aleatorio.py':                      
            #Se llenan dos arreglos, uno de tamaño 24 para el eje X, y tamaño 14 para el eje Y.
            cuadros_y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            cuadros_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
            #Tamaño de los cuadros
            y = 10 
            x = 15
            
            #La variable 'cuadros utilizados' almacena las coordenadas de los cuadros que se han eliminado para descubrir una parte de la imagen
            cuadros_utilizados = []
            #Colocar la imagen al fondo
            for i in range(0, len(cuadros_y)*len(cuadros_x)):
                self.ventana.blit(imagen, (720, 250))
                while True:
                    #Obtener dos números aleatorios, que se usan como coordenadas de una cuadricula
                    aleatorio_y = random.randint(0, len(cuadros_y) - 1)
                    aleatorio_x = random.randint(0, len(cuadros_x) - 1)
                    #Si las coordenadas ya han sido utilizadas, deneter el procedimiento y repetir
                    if not [aleatorio_y, aleatorio_x] in cuadros_utilizados:
                        break 

                #Agregar las coordenadas a la variable de 'cuadros_utilizados' para evitar dibujar nuevamente ese cuadro
                cuadros_utilizados.append([aleatorio_y, aleatorio_x])
                
                #Ciclo para colocar todos los cuadros 
                for i in range(0, len(cuadros_y)):
                    cord_y = 250 + y * i
                    for j in range(0, len(cuadros_x)):
                        cord_x = 720 + x * j 
                        #Dibujar todos los cuadros que no estén en la lista de 'cuadros_utilizados'
                        if not ([i, j] in cuadros_utilizados):
                            pygame.draw.rect(self.ventana, self.negro, Rect(cord_x, cord_y, x, y))
                
                #Tiempo de espera para reiniciar el ciclo      
                ticks_inicial = pygame.time.get_ticks()
                ticks_final = ticks_inicial + 0.01 * 1000
                while True:
                    ticks_inicial = pygame.time.get_ticks()
                    if ticks_inicial > ticks_final:
                        break
                    pygame.display.flip()

        #Efecto de 'Abajo a Arriba'
        if efecto == 'AbajoArriba.py':
            #Coordenada inicial de la imagen (donde aún no es visible)
            cordYDown = 390
            #Número de pixeles que se va a desplazar la imagen en cada iteración
            velY = 2
            #Condición de paro
            efecto_DtU = True
            
            #Desplaza la imagen hacia abajo hasta que llega a la posición final (coordenada 250 en Y)
            while efecto_DtU:
                cordYDown -= velY
                #Muestra la imagen
                self.ventana.blit(imagen, (720, cordYDown))
                #Rectángulo que oculta a la imagen fuera del área de animación
                cuadro = Rect(720, 390, 360, 140)
                pygame.draw.rect(self.ventana, self.blanco, cuadro)
                if cordYDown <= 250:
                    efecto_DtU = False
                pygame.display.flip()
                self.clock.tick(self.FPS)
        
        #Efecto 'Instantaneo'
        elif efecto == 'Instantaneo.py':
            #Variables para medir el tiempo que se presenta la imagen
            ticks_inicial = pygame.time.get_ticks()
            ticks_final = ticks_inicial + 2 * 1000
            while True:
                ticks_inicial = pygame.time.get_ticks()
                self.ventana.blit(imagen, (720, 250))
                if ticks_inicial > ticks_final:
                    break
                pygame.display.flip()
            
        #Efecto 'Arriba a Abajo'    
        elif efecto == 'ArribaAbajo.py':
            #Coordenada inicial de la imagen (donde aún no es visible)
            cordYUp = 110
            #Número de pixeles que se va a desplazar la imagen en cada iteración
            velY = 2
            #Condición de paro
            efecto_UtD = True
            #Desplaza la imagen hacia abajo hasta que llega a la posición final (coordenada 250 en Y)
            while efecto_UtD:
                cordYUp += velY
                #Muestra la imagen
                self.ventana.blit(imagen, (720, cordYUp))
                #Rectángulo que oculta a la imagen fuera del área de animación
                cuadro = Rect(720, 110, 360, 140)
                pygame.draw.rect(self.ventana, self.blanco, cuadro)
                pygame.draw.line(self.ventana, self.negro, (0,120), (1200,120), 5)
                if cordYUp >= 250:
                    efecto_UtD = False
                pygame.display.flip()
                self.clock.tick(self.FPS)
        
        #Efecto 'Derecha a Izquierda'
        elif efecto == 'DerechaIzquierda.py':
            #Coordenada inicial de la imagen (donde aún no es visible)
            cordXDer = 1080
            #Número de pixeles que se va a desplazar la imagen en cada iteración
            velX = 4
            #Condición de paro
            efecto_DI = True
            #Desplaza la imagen hacia abajo hasta que llega a la posición final (coordenada 720 en X)
            while efecto_DI:
                cordXDer -= velX
                #Muestra la imagen
                self.ventana.blit(imagen, (cordXDer, 250))
                #Rectángulo que oculta a la imagen fuera del área de animación
                cuadro = Rect(1080, 250, 120, 140)
                pygame.draw.rect(self.ventana, self.blanco, cuadro)
                if cordXDer <= 720:
                    efecto_DI = False
                pygame.display.flip()
                self.clock.tick(self.FPS)
                   
        print(self.presentacion_efecto)

########################Termina Visualizar#################################


#######################Visualización Resumen#################################
#Ventana para visualizar los efectos de entrada de las imágenes 
class VisualizarResumen:
    
    #No recibe un objeto de tipo 'Datos' ya que utiliza la lista de configuración 
    def __init__(self):
        #Inicia el proceso de 'pygame'
        pygame.init()
        
        #Variables para almacenar los datos necesarios para desplegar una imagen
        self.numero_presentacion = 0
        self.presentacion_nombre = str(lista_configuracion[self.numero_presentacion].get_numero() + 1)
        self.presentacion_imagen = lista_configuracion[self.numero_presentacion].get_imagen()
        self.presentacion_efecto = lista_configuracion[self.numero_presentacion].get_efecto()
        self.presentacion_tiempo = str(lista_configuracion[self.numero_presentacion].get_tiempo())
        
        #Tamaño de la ventana 
        self.size = (1200, 560)
        self.ventana = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Monitor de Productividad para Procesos Industriales (MPPI)")
        icono = pygame.image.load("./iconos/main.png")
        pygame.display.set_icon(icono)

        self.cargar_elementos()     
           
    #Función para cargar los elemntos de la ventana
    def cargar_elementos(self):
        self.blanco = (255,255,255)
        self.silver = (192,192,192)
        self.negro = (0,0,0)
        self.gray = (128,128,128)
        self.lightblue = (173,216,230)

        #Cargar imagen y colocarla en el encabezado
        uam = pygame.image.load("./recursos/uamazcL.png")
        self.uamAzc = pygame.transform.scale(uam, (300, 80))
        #Cargar imagen y colocarla en el encabezado
        cbi = pygame.image.load("./recursos/cbi.png")
        self.cbiAzc = pygame.transform.scale(cbi, (300, 80))

        #Colocar los elementos en la ventana 
        miFuente = pygame.font.SysFont("Verdana", 30)
        self.text = miFuente.render("Visualización de animación", 0, (self.negro))
        fuente = pygame.font.SysFont("Verdana", 20)

        #Creación de botones de 'Play', 'Regresar, 'Siguiente' y 'Anterior'
        self.play = Rect(630, 500, 80, 25)
        self.regresar = Rect(1085, 500, 80, 25)
        self.siguiente = Rect(1085, 450, 80, 25)
        self.anterior = Rect(630, 450, 80, 25)
        self.fuente2 = pygame.font.SysFont("Calibri", 20)
        
    #Función para crear un botón utilizando un rectángulo
    def crearBoton(self, screen, boton, mensaje):
        #Si el cursor está colocado sobre el botón, este cambia de color
        if boton.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.ventana, self.silver, boton)
        else:
            pygame.draw.rect(self.ventana, self.gray, boton)
        texto = self.fuente2.render(mensaje, True, (self.blanco))
        screen.blit(texto, (boton.x+(boton.width-texto.get_width())/2,
        boton.y+(boton.height-texto.get_height())/2)
        )

    #Función para mostar el contenido de la ventana
    def mostrar(self): 

        #El contenido de la ventana se actualiza a 20 frame por segundo (FPS)
        self.clock = pygame.time.Clock()
        self.FPS = 20

        coordenada_x_inicial = -250
        coordenada_y_inicial = -250
        
        #Variable para iniciar el primer efecto
        primer_presentacion = True
        
        #Ciclo para mostrar constantemente el contenido de la ventana
        while True:
            #Cuando se desea cerrar la ventana, se termina el proceso 'pygame'
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.mostrar_ventana()
            
            #Condición para visualizar el efecto sin presionar el botón de 'Play'
            if primer_presentacion:
                self.presentar_efecto()
                coordenada_x_inicial = 720
                coordenada_y_inicial = 250
                primer_presentacion = False
            
            #Mostrar imagen
            self.ventana.blit(self.pruebaR, (coordenada_x_inicial, coordenada_y_inicial))
            
             #Cuando se oprime el botón de salir, se termina el proceso 'pygame'         
            if event.type == MOUSEBUTTONDOWN:
                if self.regresar.collidepoint(pygame.mouse.get_pos()):
                    self.salir()

            #Cuando se selecciona el botón 'Presentar efecto', se ejecuta la función para desplegar la animación
            if event.type == MOUSEBUTTONDOWN:
                if self.siguiente.collidepoint(pygame.mouse.get_pos()):
                    #Si se presiona el botón de 'Siguiente' y ya se encuentra en la última imagen, no se realiza la acción
                    if self.numero_presentacion >= len(lista_configuracion) - 1:
                        pass
                    #De lo contrario se cargan los datos de la 'Siguiente' presentación, y muestra la animación
                    else:
                        self.siguiente_presentacion()
                        self.mostrar_ventana()
                        self.presentar_efecto()
                        coordenada_x_inicial = 720
                        coordenada_y_inicial = 250
            
            #Si se presiona el botón de 'Anterior' y ya se encuentra en la primer imagen, no se realiza la acción
            if event.type == MOUSEBUTTONDOWN:
                if self.anterior.collidepoint(pygame.mouse.get_pos()):
                    if self.numero_presentacion <= 0:
                        pass
                    #De lo contrario se cargan los datos de la 'Anterior' presentación, y muestra la animación
                    else:
                        self.anterior_presentacion()
                        self.mostrar_ventana()
                        self.presentar_efecto()
                        coordenada_x_inicial = 720
                        coordenada_y_inicial = 250

            #Cuando se selecciona el botón 'Play', se ejecuta la función para desplegar la animación
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.play.collidepoint(pygame.mouse.get_pos()):
                    self.presentar_efecto()
                    coordenada_x_inicial = 720
                    coordenada_y_inicial = 250
            
            #Dejar la imagen fija en la ventana después de realizar el efecto de desplegado
            self.ventana.blit(self.pruebaR, (coordenada_x_inicial, coordenada_y_inicial))

            #Actualizar contenido de la ventana
            pygame.display.flip()
            self.clock.tick(self.FPS)
            
    #Función para terminar el proceso 'pygame'
    def salir(self):
        pygame.quit()

    #Recupera en las variables la información de la siguiente animación 
    def siguiente_presentacion(self):
        self.numero_presentacion += 1
        self.presentacion_nombre = str(lista_configuracion[self.numero_presentacion].get_numero() + 1)
        self.presentacion_imagen = lista_configuracion[self.numero_presentacion].get_imagen()
        self.presentacion_efecto = lista_configuracion[self.numero_presentacion].get_efecto()
        self.presentacion_tiempo = str(lista_configuracion[self.numero_presentacion].get_tiempo())
        
    #Recupera en las variables la información de la anterior animación 
    def anterior_presentacion(self):
            self.numero_presentacion -= 1
            self.presentacion_nombre = str(lista_configuracion[self.numero_presentacion].get_numero() + 1)
            self.presentacion_imagen = lista_configuracion[self.numero_presentacion].get_imagen()
            self.presentacion_efecto = lista_configuracion[self.numero_presentacion].get_efecto()
            self.presentacion_tiempo = str(lista_configuracion[self.numero_presentacion].get_tiempo())
    
    #Color de fondo, imagenes, separadores, botones, letreros y datos de la animación 
    def mostrar_ventana(self):
        self.ventana.fill(self.blanco)
        self.ventana.blit(self.uamAzc, (50, 20))
        self.ventana.blit(self.text, (400,40))
        self.ventana.blit(self.cbiAzc, (850, 20))
        pygame.draw.line(self.ventana, self.negro, (0,120), (1200,120), 5)
        pygame.draw.line(self.ventana, self.negro, (600,120), (600,600), 5)
        pygame.draw.rect(self.ventana, self.silver, (720, 250, 360, 140))
                
        miFuente = pygame.font.SysFont("Verdana", 30)
        self.text = miFuente.render("Visualización de animación", 0, (self.negro))
        fuente = pygame.font.SysFont("Verdana", 25)

        self.nom_Imagen = fuente.render("Número de imagen: ", 0, (self.negro))
        self.nombre_imagen = fuente.render(self.presentacion_nombre, 0, (self.negro))
        self.nomEfecto = fuente.render("Efecto: ", 0, (self.negro))
        self.letrero_efecto = fuente.render(self.nombre_efecto(self.presentacion_efecto), 0, (self.negro))
        self.tiempo = fuente.render("Tiempo(segundos): ", 0, (self.negro))
        self.seg = fuente.render(self.presentacion_tiempo, 0, (self.negro))

        self.ventana.blit(self.nom_Imagen, (130,225))
        self.ventana.blit(self.nombre_imagen, (400,225))
        self.ventana.blit(self.nomEfecto, (130,295))
        self.ventana.blit(self.letrero_efecto, (240, 295))
        self.ventana.blit(self.tiempo, (130,365))
        self.ventana.blit(self.seg, (385,365))                    

        prueba = pygame.image.load(self.presentacion_imagen)
        self.pruebaR = pygame.transform.scale(prueba, (360, 140))
        
        self.crearBoton(self.ventana, self.play, "Play")
        self.crearBoton(self.ventana, self.regresar, "Salir")
        self.crearBoton(self.ventana, self.siguiente, "Siguiente")
        self.crearBoton(self.ventana, self.anterior, "Anterior")
       
    #Función para desplegar una imagen en la pantalla, utilizando alguno de los efectos disponibles
    def presentar_efecto(self):
        pygame.draw.rect(self.ventana, self.silver, (720, 250, 360, 140))
        prueba = pygame.image.load(self.presentacion_imagen)
        pruebaR = pygame.transform.scale(prueba, (360, 140))
        imagen = pruebaR
        efecto = self.presentacion_efecto
        
        #Efecto Aleatorio
        #Para realizar este efecto, Se crean varios cuadros pequeños que en conjunto cubren la imagen, de forma aleatoria, los cuadros desaparecen uno a uno hasta descubrir la imagen completamente
        if efecto == 'Aleatorio.py': 
            #Se llenan dos arreglos, uno de tamaño 24 para el eje X, y tamaño 14 para el eje Y.
            cuadros_y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            cuadros_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
            #Tamaño de los cuadros
            y = 10 
            x = 15
            
            #La variable 'cuadros utilizados' almacena las coordenadas de los cuadros que se han eliminado para descubrir una parte de la imagen
            cuadros_utilizados = []
            #Colocar la imagen al fondo
            for i in range(0, len(cuadros_y)*len(cuadros_x)):
                self.ventana.blit(imagen, (720, 250))
                while True:
                    #Obtener dos números aleatorios, que se usan como coordenadas de una cuadricula
                    aleatorio_y = random.randint(0, len(cuadros_y) - 1)
                    aleatorio_x = random.randint(0, len(cuadros_x) - 1)
                    #Si las coordenadas ya han sido utilizadas, deneter el procedimiento y repetir
                    if not [aleatorio_y, aleatorio_x] in cuadros_utilizados:
                        break 
                
                #Agregar las coordenadas a la variable de 'cuadros_utilizados' para evitar dibujar nuevamente ese cuadro
                cuadros_utilizados.append([aleatorio_y, aleatorio_x])
                
                #Ciclo para colocar todos los cuadros
                for i in range(0, len(cuadros_y)):
                    cord_y = 250 + y * i
                    for j in range(0, len(cuadros_x)):
                        cord_x = 720 + x * j 
                        #Dibujar todos los cuadros que no estén en la lista de 'cuadros_utilizados'
                        if not ([i, j] in cuadros_utilizados):
                            pygame.draw.rect(self.ventana, self.negro, Rect(cord_x, cord_y, x, y))
                
                #Tiempo de espera para reiniciar el ciclo            
                ticks_inicial = pygame.time.get_ticks()
                ticks_final = ticks_inicial + 0.01 * 1000
                while True:
                    ticks_inicial = pygame.time.get_ticks()
                    if ticks_inicial > ticks_final:
                        break
                    pygame.display.flip()

        #Efecto de 'Abajo a Arriba'
        if efecto == 'AbajoArriba.py':
            #Coordenada inicial de la imagen (donde aún no es visible)
            cordYDown = 390
            #Número de pixeles que se va a desplazar la imagen en cada iteración
            velY = 2
            #Condición de paro
            efecto_DtU = True
            #Desplaza la imagen hacia abajo hasta que llega a la posición final (coordenada 250 en Y)
            while efecto_DtU:
                cordYDown -= velY
                #Muestra la imagen
                self.ventana.blit(imagen, (720, cordYDown))
                #Rectángulo que oculta a la imagen fuera del área de animación
                cuadro = Rect(720, 390, 360, 140)
                pygame.draw.rect(self.ventana, self.blanco, cuadro)
                if cordYDown <= 250:
                    efecto_DtU = False
                pygame.display.flip()
                self.clock.tick(self.FPS)

        #Efecto 'Instantaneo'   
        elif efecto == 'Instantaneo.py':
            #Variables para medir el tiempo que se presenta la imagen
            ticks_inicial = pygame.time.get_ticks()
            ticks_final = ticks_inicial + 2 * 1000
            while True:
                ticks_inicial = pygame.time.get_ticks()
                self.ventana.blit(imagen, (720, 250))
                if ticks_inicial > ticks_final:
                    break
                pygame.display.flip()
        
        #Efecto 'Arriba a Abajo'
        elif efecto == 'ArribaAbajo.py':
            #Coordenada inicial de la imagen (donde aún no es visible)
            cordYUp = 110
            #Número de pixeles que se va a desplazar la imagen en cada iteración
            velY = 2
            #Condición de paro
            efecto_UtD = True
            #Desplaza la imagen hacia abajo hasta que llega a la posición final (coordenada 250 en Y)
            while efecto_UtD:
                cordYUp += velY
                #Muestra la imagen
                self.ventana.blit(imagen, (720, cordYUp))
                #Rectángulo que oculta a la imagen fuera del área de animación
                cuadro = Rect(720, 110, 360, 140)
                pygame.draw.rect(self.ventana, self.blanco, cuadro)
                pygame.draw.line(self.ventana, self.negro, (0,120), (1200,120), 5)
                if cordYUp >= 250:
                    efecto_UtD = False
                pygame.display.flip()
                self.clock.tick(self.FPS)
        
        #Efecto 'Derecha a Izquierda'
        elif efecto == 'DerechaIzquierda.py':
            #Coordenada inicial de la imagen (donde aún no es visible)
            cordXDer = 1080
            #Número de pixeles que se va a desplazar la imagen en cada iteración
            velX = 4
            #Condición de paro
            efecto_DI = True
            #Desplaza la imagen hacia abajo hasta que llega a la posición final (coordenada 720 en X)
            while efecto_DI:
                cordXDer -= velX
                #Muestra la imagen
                self.ventana.blit(imagen, (cordXDer, 250))
                #Rectángulo que oculta a la imagen fuera del área de animación
                cuadro = Rect(1080, 250, 120, 140)
                pygame.draw.rect(self.ventana, self.blanco, cuadro)
                if cordXDer <= 720:
                    efecto_DI = False
                pygame.display.flip()
                self.clock.tick(self.FPS)
                   
        print(self.presentacion_efecto)
    
    #Función para obtener el nombre de un efecto a partir del nombre del archivo en Python
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

#######################Termina visualización Resumen#################################


########################Main###########################

#Lista de tipo Datos donde se almacenan todas las imágenes y sus parámetros de desplegado.
lista_configuracion = []
#Función principal para inicializar la interfaz 
def main():    
    bienvenida = Bienvenida()
    bienvenida.cargar()
    bienvenida.mostrar()

#Ejecuta SOLO la función 'main'
if __name__ == "__main__":
    main()
