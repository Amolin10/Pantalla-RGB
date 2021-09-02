from os import cpu_count
from tkinter import *
from tkinter import ttk
import os.path
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
from ayuda import *


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


#resumen = Resumen()
#resumen.cargar()
#resumen.mostrar()

