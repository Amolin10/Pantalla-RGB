#!/usr/bin/env python
import time
from samplebase import SampleBase
from rgbmatrix import graphics
from PIL import Image
import random

#Clase principal en donde se define los argumentos (datos) requeridos para presentar un efecto
class ImageScroller(SampleBase):
    def __init__(self, *args, **kwargs):
        super(ImageScroller, self).__init__(*args, **kwargs)
        self.parser.add_argument("-i", "--image", help="The image to display", default="../../examples-api-use/uam2.ppm")
        self.parser.add_argument("-t", "--time", help="Time execution. Default: 3", default=3, type=int)

    #Función para presentar un efecto 
    def run(self):
        #Si no se indica la ruta de una imagen en los parámetros, se toma una por defecto.
        if not 'image' in self.__dict__:
            self.image = Image.open(self.args.image).convert('RGB')
        self.image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
        
        #Configura el buffer para la pantalla y obtiene los pixeles de ancho y alto
        double_buffer = self.matrix.CreateFrameCanvas()
        img_width, img_height = self.image.size
        pixeles_imagen = self.image.load()
       
        #Toma el valor del tiempo de los argumentos
        tiempo=self.parser.parse_args().time
        
        #Configura el buffer para la pantalla 
        double_buffer = self.matrix.SwapOnVSync(double_buffer)
        
        #Crea un arreglo de x pixeles 
        x = 128 / 2
        pixels_x = []
        for i in range(0, int(x)):
            pixels_x.append(i)
        
        #Crea un arreglo de y pixeles 
        y = 48 / 2
        pixels_y = []
        for i in range(0, int(y)):
            pixels_y.append(i)
        
        #Matriz de pixeles X,Y
        pixeles_utilizados = []
        
        #Ciclo para llenar y mostrar cada coordenada de pixeles en la pantalla 
        for i in range(0, len(pixels_x) * len(pixels_y)):
            #Obtener un par de pixeles X, Y de forma aleatoria
            while True:
                aleatorio_x = 2 * random.randint(0, len(pixels_x) - 1)
                aleatorio_y = 2 * random.randint(0, len(pixels_y) - 1)
                if not ([aleatorio_x, aleatorio_y] in pixeles_utilizados):
                    break
                    
            #Añadir el par de pixeles a una lista para que no se repitan
            pixeles_utilizados.append([aleatorio_x, aleatorio_y])
            
            #Enciende los led's de la pantalla de 4 en 4, según las coordenadas obtenidas aleatoriamente
            for i in range (0, 2):
                for j in range(0, 2):
                    #Obtiene los colores RGB del pixel (x, y)
                    r, g, b = pixeles_imagen[aleatorio_x + i, aleatorio_y + j]
                    #Enciende en la pantalla el pixel indicado con los colores obtenidos
                    self.matrix.SetPixel(aleatorio_x + i, aleatorio_y + j, r, g, b)
            time.sleep(0.005)
        
        #Actualiza el buffer de la pantalla.
        double_buffer = self.matrix.SwapOnVSync(double_buffer)
        
        #Muestra la imagen completa
        double_buffer.SetImage(self.image, 0, 0)
        double_buffer = self.matrix.SwapOnVSync(double_buffer)
        #Tiempo que se congelará la imagen en la pantalla 
        time.sleep(tiempo)

#Tiempo que se congelará la imagen en la pantalla 
if __name__ == "__main__":
    image_scroller = ImageScroller()
    if (not image_scroller.process()):
        image_scroller.print_help()
