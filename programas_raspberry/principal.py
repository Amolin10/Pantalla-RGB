#!/usr/bin/env python
import time
from samplebase import SampleBase
from PIL import Image
import os, sys
import subprocess
import filecmp


#Tiempo necesario para que la Raspberry detecte si tiene una USB conectada
time.sleep(30)

#Directorios en donde se encuentran los archivos necesarios para poder presentar los efectos 
ruta_efectos = "/home/pi/Desktop/ProgramaInicial/rpi-rgb-led-matrix/python/samples/"
ruta_var= "/var/www/html/UploadServer/upload/Configuracion/"
ruta_imagenes = "/var/www/html/UploadServer/upload/Configuracion/Imagenes/"

#Verifica si tiene una USB conectada 
if len(os.listdir("/media/pi/")) != 0:
    os.system('sudo mount /dev/sda1 /media/pidrive')
    ruta_var = "/media/pidrive/Configuracion/"
    ruta_imagenes = "/media/pidrive/Configuracion/Imagenes/"

#Abre el archivo de configuración y lee el contenido 
archivo = open(ruta_var + "configuracion.txt", "r")
content = archivo.read().splitlines()

#Ciclo para repetir la configuración indefinidamente
while True:

    #Variables para separar los campos de cada presentación de la configuración
    contador = 0
    diccionario = {}
    for line in content:
        if contador == 0:
            key = line
            diccionario[key]=[]
        else:
            diccionario[key].append(line)
        contador+=1
        if contador==4:
            contador=0
    numero_imagenes = (len(content)/4)+1

    #Obtener los datos de efecto e imagen para cada presentación
    for num_date in range(1, int(numero_imagenes)):
        archivo_comprobar = open(ruta_var + "configuracion.txt", "r")
        content_comprobar = archivo_comprobar.read().splitlines()
        datos = "Datos"+str(num_date)
        efecto = diccionario[datos][0]
        imagen = ruta_imagenes + diccionario[datos][1]
    
    #Verificar la ruta de donde se está obteniendo el contenido. El dispositivo USB tiene la mayor prioridad para presentar la configuración que contiene
        #Verifica si se conenctó una USB, si es así se reinicia la Raspberry    
        if (len(os.listdir("/media/pi/")) != 0) and ruta_var == "/var/www/html/UploadServer/upload/Configuracion/":
            os.system('reboot')
        #Si había una USB conectada y se desconectó, se reinicia la Raspberry
        if (len(os.listdir("/media/pi/")) == 0) and ruta_var == "/media/pidrive/Configuracion/":
            os.system('reboot')
        #Si se envía un nuevo archivo por el servidor WEB se reinicia la Raspberry 
        #Comprueba el tamaño de los archivos para verificar si el tamaño es diferente
        if len(content) != len(content_comprobar):
            os.system('reboot')
            #En caso de tener el mismo tamaño, se compara línea por línea
        else:
            for i in range(len(content)):
                if(content[i] != content_comprobar[i]):
                    os.system('reboot')
        #Se cierra el archivo 
        archivo_comprobar.close()   
        
        #Ejecuta el programa de efecto correspondiente 
        os.system("sudo python3 " + ruta_efectos + efecto + " -i " + imagen + " -t " + diccionario[datos][2])
        
        time.sleep(0.1)
    
