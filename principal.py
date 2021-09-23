from os import cpu_count
from tkinter import *
from tkinter import ttk
import os.path
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
from ayuda import *
from resumen import *
#from agregar import Agregar


class Interfaz:

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
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2 #winfo da el tamaño de la pantalla en ancho y en alto
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana)+ "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background=self.colorFondo)

        if self.resizable:
            self.root.resizable(1, 1)
        else:
            self.root.resizable(0, 0)           

        uama = Image.open("./recursos/uamazc.jpg")
        uama= uama.resize((280, 110))
        uama = ImageTk.PhotoImage(uama)
        uamA = Label(self.root, image=uama, width=260, height=80, padx=100, background='white')
        uamA.image = uama
        uamA.grid(row=0, column=0, sticky='ewns')

        electronica = Image.open("./recursos/electronica.jpg")
        electronica= electronica.resize((240, 120))
        electronica = ImageTk.PhotoImage(electronica)
        electronicaLabel = Label(self.root, image=electronica, width=220, height=80, padx=100, background='white')
        electronicaLabel.image = electronica
        electronicaLabel.grid(row=0, column=1, columnspan=3, sticky='ewns')

        cbi = Image.open("./recursos/cbi.png")
        cbi= cbi.resize((240, 120))
        cbi = ImageTk.PhotoImage(cbi)
        CBI = Label(self.root, image=cbi, width=220, height=80, padx=100, background='white')
        CBI.image = cbi
        CBI.grid(row=0, column=4, sticky='ewns')

        titulo = Label(self.root, text="Insertar título", font=("Verdana", 28), relief="groove", background='#184B6C', fg='white').grid(row=1, column=0, columnspan=5, sticky='ewns')
        texto = Label(self.root, text="Configurar imagen para mostrar en la pantalla RGB", relief='groove',font=("Verdana", 22), background='#2980B9')
        texto.grid(row=2, column=0, columnspan=5, sticky="ewns")
        Label(self.root, text="", background=self.colorFondo).grid(row=3, column=0, columnspan=5, pady=5)
        
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=4, column=0, columnspan=5, sticky="ews")
        ttk.Separator(self.root, orient=VERTICAL).grid(row=5, column=2, rowspan=5, sticky="ns")
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=7, column=3, columnspan=2, sticky="ewn")
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=10, column=0, columnspan=5, sticky="ewn")


        imagenFrame = Frame(self.root, background=self.colorFondo, pady=10)
        Label(imagenFrame, text="Selecciona una imagen para\nmostrar en la pantalla RGB", font=("verdana", 18), padx=10, background=self.colorFondo).grid(row=0, column=0, sticky="n")
        imgImagen = Image.open("./iconos/imagen.png")
        imgImagen = imgImagen.resize((30, 30))
        imgImagen = ImageTk.PhotoImage(imgImagen)
        botonCargar = Button(imagenFrame, text="Cargar imagen   ", image=imgImagen, compound="right", font=("verdana", 14), command=lambda:self.selecImagen(imagenFrame))
        botonCargar.grid(row=1, column=0, pady=30)
        botonCargar.image = imgImagen

        Label(imagenFrame, height=16, width=100, background=self.colorFondo).grid(column=0, row=2, sticky=N)

        imagenFrame.grid_columnconfigure(0,weight=1)
        #imagenFrame.rowconfigure(0, weight=1)
        imagenFrame.rowconfigure(1, weight=1)
        imagenFrame.rowconfigure(2, weight=1)
        imagenFrame.grid(row=6, column=0, columnspan=2, rowspan=5, sticky="ns", pady=20)



        parametros = Frame(self.root, background=self.colorFondo)
        ########Poner una variable a los radiobutons##########################
        Label(parametros, text="Selecciona el efecto de entrada de la imagen", font=("Verdana", 18), background=self.colorFondo).grid(column=0, row=0, columnspan=3)
        Radiobutton(parametros, text="Instantaneo", font=("verdana", 14), background=self.colorFondo).grid(column=0 , row=1,)
        Radiobutton(parametros, text="De abajo a arriba", font=("verdana", 14), background=self.colorFondo, padx=20).grid(column=1 , row=1, sticky="ew")
        Radiobutton(parametros, text="Aleatorio", font=("verdana", 14), background=self.colorFondo).grid(column=2, row=1, sticky="e")
        Radiobutton(parametros, text="De derecha a izquierda", font=("verdana", 14), background=self.colorFondo).grid(column=0, row=2, sticky="e")
        Radiobutton(parametros, text="De arriba a abajo", font=("verdana", 14), background=self.colorFondo).grid(column=2, row=2, sticky="w")
        Label(parametros, text="", background=self.colorFondo).grid(column=0, row=3, columnspan=3)
        parametros.rowconfigure(0, weight=1)
        parametros.rowconfigure(1, weight=1)
        parametros.rowconfigure(2, weight=1)
        parametros.rowconfigure(3, weight=1)
        parametros.grid(column=3, row=5, columnspan=2, rowspan=2, sticky='ns')
        
        

        tiempo = Frame(self.root, background=self.colorFondo)
        Label(tiempo, text="Seleccione el tiempo de desplegado de la imagen", font=("Verdana", 18), pady=14, background=self.colorFondo).grid(column=0, row=0, columnspan=2)
        Label(tiempo, text="minutos:", font=("verdana", 14), background=self.colorFondo).grid(column=0, row=1, sticky="w")
        listaMinutos = self.llenarListaMinutos() 
        minutosBox = ttk.Combobox(tiempo, values=listaMinutos, state="readonly", font=("verdana", 14))
        minutosBox.grid(column=0, row=2, sticky='wn', pady=5)
        listaSegundos = self.llenarListaSegundos()
        Label(tiempo, text="segundos:", font=("verdana", 14), background=self.colorFondo).grid(column=1, row=1, sticky="w")
        segundosBox = ttk.Combobox(tiempo, values=listaSegundos, state="readonly", font=("verdana", 14), )
        segundosBox.grid(column=1, row=2, sticky='wn', pady=5)
        #Label(tiempo, text="", background="white").grid(column=0, row=3, columnspan=3)
        tiempo.grid(row=8, column=3, columnspan=2, rowspan=2, sticky="ns")
        tiempo.grid_rowconfigure(0,weight=1)
        tiempo.grid_rowconfigure(1,weight=1)
        tiempo.grid_rowconfigure(2,weight=1)
        
        imgRegresar= Image.open("./iconos/arrow.png")
        imgRegresar= imgRegresar.resize((30, 30))
        imgRegresar= ImageTk.PhotoImage(imgRegresar)
        botonRegresar = Button(self.root, text="Regresar  ", image=imgRegresar, compound="right", font=("verdana", 14), command=self.regresar)
        botonRegresar.grid(column=4, row=11, pady=15, sticky='n')
        botonRegresar.image = imgRegresar
    
        imgAgregar= Image.open("./iconos/imagen.png")
        imgAgregar= imgAgregar.resize((30, 30))
        imgAgregar= ImageTk.PhotoImage(imgAgregar)
        botonAgregar = Button(self.root, text="Agregar otra imagen  ", image=imgAgregar, compound="right", font=("verdana", 14), command=self.agregar)
        botonAgregar.grid(column=4, row=11, pady=15, sticky='n')
        botonAgregar.image = imgAgregar

        imgVisualizar= Image.open("./iconos/imagen.png")
        imgVisualizar= imgAgregar.resize((30, 30))
        imgVisualizar= ImageTk.PhotoImage(imgAgregar)
        botonAgregar = Button(self.root, text="Visualizar  ", image=imgAgregar, compound="right", font=("verdana", 14), command=self.agregar)
        botonAgregar.grid(column=4, row=11, pady=15, sticky='n')
        botonAgregar.image = imgAgregar

        imgTerminar= Image.open("./iconos/arrow.png")
        imgTerminar= imgTerminar.resize((30, 30))
        imgTerminar= ImageTk.PhotoImage(imgTerminar)
        botonTerminar = Button(self.root, text="Terminar  ", image=imgTerminar, compound="right", font=("verdana", 14), command=self.terminar)
        botonTerminar.grid(column=4, row=11, pady=15, sticky='n')
        botonTerminar.image = imgTerminar


        
        self.root.grid_columnconfigure(0,weight=1)
        self.root.grid_columnconfigure(1,weight=1)
        #self.root.grid_columnconfigure(2,weight=1)
        self.root.grid_columnconfigure(3,weight=1)
        self.root.grid_columnconfigure(4,weight=1)

        self.root.grid_rowconfigure(0,weight=1)
        #self.root.grid_rowconfigure(1,weight=1)
        #self.root.grid_rowconfigure(2,weight=1)
        #self.root.grid_rowconfigure(3,weight=1)
        self.root.grid_rowconfigure(6,weight=1)
        self.root.grid_rowconfigure(5,weight=1)
        self.root.grid_rowconfigure(8,weight=1)
        #self.root.grid_rowconfigure(9,weight=1)

    
    def selecImagen(self, imagenFrame):
        archivo = filedialog.askopenfilename(filetypes=[('Archivos de imagen', '*.jpg')])

        if archivo is not None:
            #Imagen de entrada
            imagenEntrada = Image.open(archivo)
            ancho, alto = imagenEntrada.size
            imagenEntrada = imagenEntrada.resize((640, 240)) #128x48
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

    def agregar():
        pass

    def regresar():
        self.destruir()
        from opciones import *
        
    
    def terminar(self):
        self.destruir()
        resumen = Resumen()
        resumen.cargar()
        resumen.mostrar()

    def llenarListaMinutos(self):
        lista = []
        for i in range (5):
            lista.append(str(i))
        return lista
            
    def llenarListaSegundos(self):
        lista = []
        for i in range (60):
            lista.append(str(i))
        return lista

programa = Interfaz()
programa.cargar()
programa.cargarMenus()
programa.mostrar()

