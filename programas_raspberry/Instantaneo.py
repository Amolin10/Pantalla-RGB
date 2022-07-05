#!/usr/bin/env python
import time
from samplebase import SampleBase
from PIL import Image

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

        #Toma el valor del tiempo de los argumentos
        time_wait=self.parser.parse_args().time
        
        #Establece la imagen completa en la pantalla RGB
        double_buffer.SetImage(self.image, 0, 0)
        double_buffer = self.matrix.SwapOnVSync(double_buffer)
        
        #Tiempo que se congelará la imagen en la pantalla 
        time.sleep(time_wait)
        
#Llama a la función principal para que se pueda ejecutar 
if __name__ == "__main__":
    image_scroller = ImageScroller()
    if (not image_scroller.process()):
        image_scroller.print_help()
