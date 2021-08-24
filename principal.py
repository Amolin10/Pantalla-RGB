from os import cpu_count
from tkinter import *
from tkinter import ttk
import os.path
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
from ayuda import *


class Interfaz:

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
        ancho = 1500
        alto = 800
        xVentana = self.root.winfo_screenwidth() // 2 - ancho // 2 #winfo da el tamaño de la pantalla en ancho y en alto
        yVentana = self.root.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(xVentana)+ "+" + str(yVentana)
        self.root.geometry(posicion)
        self.root.config(background='white')

        if self.resizable:
            self.root.resizable(1, 1)
        else:
            self.root.resizable(0, 0)           

        uama = Image.open("./recursos/uamazc.jpg")
        uama= uama.resize((260, 100))
        uama = ImageTk.PhotoImage(uama)
        uamA = Label(self.root, image=uama, width=260, height=100, padx=100, background='whitesmoke')
        uamA.image = uama
        uamA.grid(row=0, column=0, sticky='ewns')

        electronica = Image.open("./recursos/electronica.jpg")
        electronica= electronica.resize((220, 100))
        electronica = ImageTk.PhotoImage(electronica)
        electronicaLabel = Label(self.root, image=electronica, width=220, height=100, padx=100, background='whitesmoke')
        electronicaLabel.image = electronica
        electronicaLabel.grid(row=0, column=1, columnspan=3, sticky='ewns')

        cbi = Image.open("./recursos/cbi.png")
        cbi= cbi.resize((220, 100))
        cbi = ImageTk.PhotoImage(cbi)
        CBI = Label(self.root, image=cbi, width=220, height=100, padx=100, background='whitesmoke')
        CBI.image = cbi
        CBI.grid(row=0, column=4, sticky='ewns')

        titulo = Label(self.root, text="Insertar título", font=("Verdana", 28), background='white').grid(row=1, column=0, columnspan=5, sticky='ewns', pady=25)
        texto = Label(self.root, text="Seleccionar una imagen, tipo y tiempo de animación para mostrar en la pantalla RGB.", font=("Verdana", 22), background='white')
        texto.grid(row=2, column=0, columnspan=5)
        Label(self.root, text="", background="white").grid(row=3, column=0, columnspan=5, pady=5)
        
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=4, column=0, columnspan=5, sticky="ew")
        ttk.Separator(self.root, orient=VERTICAL).grid(row=5, column=2, rowspan=3, sticky="ns")
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=8, column=0, columnspan=5, sticky="ewn")
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=6, column=3, columnspan=2, sticky="ewn")

        imagenFrame = Frame(self.root, background='white', pady=10)
        Label(imagenFrame, text="Selecciona una imagen para\nmostrar en la pantalla RGB", font=("Verdana", 16), padx=10, pady=20, background='white').grid(row=0, column=0)
        imgImagen = Image.open("./iconos/imagen.png")
        imgImagen = imgImagen.resize((20, 20))
        imgImagen = ImageTk.PhotoImage(imgImagen)
        botonCargar = Button(imagenFrame, text="Cargar imagen", image=imgImagen, compound="right", font=("Verdana", 14), command=lambda:self.selecImagen(imagenFrame))
        botonCargar.grid(row=1, column=0)
        botonCargar.image = imgImagen
        imagenFrame.grid(row=5, column=0, columnspan=2, rowspan=3, sticky="n")

        parametros = Frame(self.root, background='white')
        ########Poner una variable a los radiobutons##########################
        Label(parametros, text="Selecciona el efecto para aplicar a la imagen", font=("Verdana", 18), pady=14, background='white').grid(column=0, row=0, columnspan=3)
        Radiobutton(parametros, text="Instantaneo", font=("Verdana", 14), background='white').grid(column=0 , row=1,)
        Radiobutton(parametros, text="De abajo a arriba", font=("Verdana", 14), background='white', padx=20).grid(column=1 , row=1, sticky="ew")
        Radiobutton(parametros, text="Aleatorio", font=("Verdana", 14), background='white').grid(column=2, row=1, sticky="e")
        Radiobutton(parametros, text="De derecha a izquierda", font=("Verdana", 14), background='white').grid(column=0, row=2, sticky="e")
        Radiobutton(parametros, text="De arriba a abajo", font=("Verdana", 14), background='white').grid(column=2, row=2, sticky="w")
        Label(parametros, text="", background="white").grid(column=0, row=3, columnspan=3)
        parametros.grid(column=3, row=5, columnspan=2, sticky='n', pady=10)

        

        tiempo = Frame(self.root, background='white')
        Label(tiempo, text="Elija el tiempo de permanencia de la imagen", font=("Verdana", 18), background="white", pady=14).grid(column=0, row=0, columnspan=2)
        Label(tiempo, text="minutos:", font=("Verdana", 14), background='white').grid(column=0, row=1, sticky="w")
        minutosEntry = Entry(tiempo)
        minutosEntry.grid(column=0, row=2, sticky='w', pady=5)
        
        Label(tiempo, text="segundos:", font=("Verdana", 14), background="white").grid(column=1, row=1, sticky="w")
        segundosEntry = Entry(tiempo)
        segundosEntry.grid(column=1, row=2, sticky='w', pady=5)
        
        tiempo.grid(row=7, column=3, columnspan=2, sticky="n", pady=10)
    
        

        """
        botonesFrame = Frame(self.root, background='white', pady=5)
        
        choice = OptionMenu(botonesFrame, "opción 1", "opción 2")
        choice.config(width=15)
        choice.grid(column=0, row=0, columnspan=2, padx=20, pady=25)

        imgAñadir = Image.open("./iconos/añadir.png")
        imgAñadir = imgAñadir.resize((20, 20))
        imgAñadir = ImageTk.PhotoImage(imgAñadir)
        botonAñadir = Button(botonesFrame, text="Añadir", image=imgAñadir, compound="right", font=("Verdana", 14))
        botonAñadir.grid(column=0, row=1, padx=30)
        botonAñadir.image = imgAñadir

        imgEliminar = Image.open("./iconos/quit.jpg")
        imgEliminar = imgEliminar.resize((20, 20))
        imgEliminar = ImageTk.PhotoImage(imgEliminar)
        botonEliminar = Button(botonesFrame, text="Eliminar", image=imgEliminar, compound="right", font=("Verdana", 14))
        botonEliminar.grid(column=1, row=1, padx=30)
        botonEliminar.image = imgEliminar

        Label(botonesFrame, text="", padx=130, background="white").grid(row=0, column=2)

        imgNuevo = Image.open("./iconos/nuevo.jpg")
        imgNuevo = imgNuevo.resize((20, 20))
        imgNuevo = ImageTk.PhotoImage(imgNuevo)
        botonNuevo = Button(botonesFrame, text="Nuevo", image=imgNuevo, compound="right", font=("Verdana", 14))
        botonNuevo.grid(column=3, row=0, rowspan=2, padx=35)
        botonNuevo.image = imgNuevo

        imgVis = Image.open("./iconos/visualizar.png")
        imgVis = imgVis.resize((20, 20))
        imgVis = ImageTk.PhotoImage(imgVis)
        botonVis = Button(botonesFrame, text="Visualizar", image=imgVis, compound="right", font=("Verdana", 14))
        botonVis.grid(column=4, row=0, rowspan=2, padx=35)
        botonVis.image = imgVis

        imgSave = Image.open("./iconos/save.ico")
        imgSave = imgSave.resize((20, 20))
        imgSave = ImageTk.PhotoImage(imgSave)
        botonSave = Button(botonesFrame, text="Guardar", image=imgSave, compound="right", font=("Verdana", 14))
        botonSave.grid(column=5, row=0, rowspan=2, padx=35)
        botonSave.image = imgSave
        

        botonesFrame.grid(column=0, row=4, columnspan=5)
        botonesFrame.grid_rowconfigure(0,weight=1)
        botonesFrame.grid_rowconfigure(1,weight=1)
        botonesFrame.grid_columnconfigure(0,weight=1)
        botonesFrame.grid_columnconfigure(1,weight=1)
        botonesFrame.grid_columnconfigure(2,weight=1)
        botonesFrame.grid_columnconfigure(3,weight=1)
        botonesFrame.grid_columnconfigure(4,weight=1)
        botonesFrame.grid_columnconfigure(5,weight=1)

        """
        
        
        self.root.grid_columnconfigure(0,weight=1)
        self.root.grid_columnconfigure(1,weight=1)
        #self.root.grid_columnconfigure(2,weight=1)
        self.root.grid_columnconfigure(3,weight=1)
        self.root.grid_columnconfigure(4,weight=1)
        #self.root.grid_rowconfigure(0,weight=1)
        #self.root.grid_rowconfigure(1,weight=1)
        #self.root.grid_rowconfigure(2,weight=1)
        #self.root.grid_rowconfigure(3,weight=1)
        #self.root.grid_rowconfigure(4,weight=1)

    
    def selecImagen(self, imagenFrame):
        archivo = filedialog.askopenfilename(filetypes=[('Archivos de imagen', '*.jpg')])

        if archivo is not None:
            #Imagen de entrada
            imagenEntrada = Image.open(archivo)
            ancho, alto = imagenEntrada.size
            imagenEntrada = imagenEntrada.resize((480, 180))
            ImagenEntrada = ImageTk.PhotoImage(imagenEntrada)
            imagenOriginal = Label(imagenFrame, image=ImagenEntrada)
            imagenOriginal.image = ImagenEntrada
            imagenOriginal.grid(column=0, row=2, sticky=N, pady=20)

    def cargarMenus(self):

        miMenu = Menu(self.root)
        self.root.config(menu=miMenu)
        archivo = Menu(miMenu, tearoff=0)
        archivo.add_command(label="Nuevo", font=("Verdana", 11))
        archivo.add_command(label="Abrir", font=("Verdana", 11))
        archivo.add_separator()
        archivo.add_command(label="Guardar", font=("Verdana", 11))
        archivo.add_command(label="Guardar como", font=("Verdana", 11))
        archivo.add_separator()
        archivo.add_command(label="Salir", font=("Verdana", 11), command=self.root.destroy)

        miMenu.add_cascade(label="Archivo", menu=archivo)
        miMenu.add_command(label="Ayuda", command=ventanaAyuda)
        miMenu.add_command(label="Información", command=self.informacion)  

    def informacion():
        messagebox.showinfo("Información", "Interfaz para configurar tablero RGB.\n\nVersión: ......")       
    
    def destruir(self):
        self.root.destroy()

    def mostrar(self):
        self.root.mainloop()


programa = Interfaz()
programa.cargar()
programa.cargarMenus()
programa.mostrar()