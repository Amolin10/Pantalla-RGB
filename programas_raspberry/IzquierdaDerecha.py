#!/usr/bin/env python
import time
import threading
from samplebase import SampleBase
from rgbmatrix import graphics
from PIL import Image
import sys
from random import randrange

#Clase principal en donde se define los argumentos (datos) requeridos para presentar un efecto
class ImageScroller(SampleBase):
    def __init__(self, *args, **kwargs):
        super(ImageScroller, self).__init__(*args, **kwargs)
        self.parser.add_argument("-i", "--image", help="The image to display", default="../../examples-api-use/runtext.ppm")
        self.parser.add_argument("-t", "--time", help="Time execution. Default: 3", default=3, type=int)
            
    #Función para presentar un efecto 
    def run(self):
        #Si no se indicó la ruta de una imagen en los parámetros, se tomará una por defecto.
        if not 'image' in self.__dict__:
            self.image = Image.open(self.args.image).convert('RGB')
        self.image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)

        #Configura el buffer para la pantalla y obtiene los pixeles de ancho y alto
        double_buffer = self.matrix.CreateFrameCanvas()
        img_width, img_height = self.image.size
       
        #Toma el valor del tiempo de los argumentos
        tiempo = self.parser.parse_args().time
        
        #La posición inicial de los pixeles de la imagen se encuentran vitualmente a la derecha de la pantalla
        xpos = -img_width
        
        #Mientras los pixeles no lleguen a la posición 0 en el eje "x" la imagen se desplazará a la derecha pixel a pixel
        while xpos < 0:

            double_buffer.SetImage(self.image, xpos, 0)
            double_buffer = self.matrix.SwapOnVSync(double_buffer)
            
            xpos += 1
            time.sleep(0.02)
        #Tiempo que se congelará la imagen en la pantalla 
        time.sleep(tiempo)

#Llama a la función principal para que se pueda ejecutar 
if __name__ == "__main__":
    image_scroller = ImageScroller()
    if (not image_scroller.process()):
        image_scroller.print_help()
