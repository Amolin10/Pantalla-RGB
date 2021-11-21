import sys, pygame
from pygame import * 
import sys, pygame
import time
import random


pygame.init()

presentacion_nombre = 'Presentación 1'
presentacion_efecto = 'Aleatorio.py'
presentacion_tiempo = '3:40 minutos'
presentacion_imagen = './recursos/RGB.jpg'


class Visualizar:
    
    def __init__(self):  
        #pygame.init()
        self.size = (1200, 560)
        self.ventana = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Visualizar")
        icono = pygame.image.load("./recursos/firefly.png")
        pygame.display.set_icon(icono)
        
        self.blanco = (255,255,255)
        self.silver = (192,192,192)
        self.negro = (0,0,0)
        self.gray = (128,128,128)
        self.lightblue = (173,216,230)

        uam = pygame.image.load("./recursos/uamazcL.png")
        self.uamAzc = pygame.transform.scale(uam, (300, 80))
        cbi = pygame.image.load("./recursos/cbi.png")
        self.cbiAzc = pygame.transform.scale(cbi, (300, 80))

        prueba = pygame.image.load(presentacion_imagen)
        self.pruebaR = pygame.transform.scale(prueba, (360, 140))

        miFuente = pygame.font.SysFont("Verdana", 30)
        self.text = miFuente.render("Visualización de animación", 0, (self.negro))
        fuente = pygame.font.SysFont("Verdana", 20)
        self.nom_Imagen = fuente.render("Nombre de imagen: ", 0, (self.negro))
        self.nombre_imagen = fuente.render(presentacion_nombre, 0, (self.negro))
        self.nomEfecto = fuente.render("Efecto: ", 0, (self.negro))
        self.nombre_efecto = fuente.render(presentacion_efecto, 0, (self.negro))
        self.tiempo = fuente.render("Tiempo: ", 0, (self.negro))
        self.seg = fuente.render(presentacion_tiempo, 0, (self.negro))

        self.play = Rect(635, 500, 70, 25)
        self.regresar = Rect(1085, 500, 70, 25)
        self.fuente2 = pygame.font.SysFont("Calibri", 20)
        

    def crearBoton(self, screen, boton, mensaje):
        if boton.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.ventana, self.silver, boton)
        else:
            pygame.draw.rect(self.ventana, self.gray, boton)
        texto = self.fuente2.render(mensaje, True, (self.blanco))
        screen.blit(texto, (boton.x+(boton.width-texto.get_width())/2,
        boton.y+(boton.height-texto.get_height())/2)
        )


    def mostrar(self): 

        self.clock = pygame.time.Clock()
        self.FPS = 20

        coordenada_x_inicial = -250
        coordenada_y_inicial = -250


        while True:
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.mostrar_ventana()
            
            if event.type == MOUSEBUTTONDOWN:
                if self.regresar.collidepoint(pygame.mouse.get_pos()):
                    self.salir()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:     #Eventos que suceden con el mouse
                if self.play.collidepoint(pygame.mouse.get_pos()): #and cordXIzq >= 125 and cordXDer <= 615:
                    self.presentar_efecto()        #Acción a realizar cuando se presiona le boton 
                    coordenada_x_inicial = 720
                    coordenada_y_inicial = 250
                
            self.ventana.blit(self.pruebaR, (coordenada_x_inicial, coordenada_y_inicial))


            pygame.display.flip()
            self.clock.tick(self.FPS)
            

    def salir(self):
        pygame.quit()

        
    def mostrar_ventana(self):
        self.ventana.fill(self.blanco)    #Color de fondo
        self.ventana.blit(self.uamAzc, (50, 20))
        self.ventana.blit(self.text, (400,40))
        self.ventana.blit(self.cbiAzc, (850, 20))
        pygame.draw.line(self.ventana, self.negro, (0,120), (1200,120), 5)
        pygame.draw.line(self.ventana, self.negro, (600,120), (600,600), 5)
        pygame.draw.rect(self.ventana, self.silver, (720, 250, 360, 140))
        self.ventana.blit(self.nom_Imagen, (50,150))
        self.ventana.blit(self.nombre_imagen, (280,150))
        self.ventana.blit(self.nomEfecto, (175,220))
        self.ventana.blit(self.nombre_efecto, (280, 220))
        self.ventana.blit(self.tiempo, (165,290))
        self.ventana.blit(self.seg, (280,290))                    

        self.crearBoton(self.ventana, self.play, "Play")
        self.crearBoton(self.ventana, self.regresar, "Salir")
       

    def presentar_efecto(self):
        prueba = pygame.image.load(presentacion_imagen)
        pruebaR = pygame.transform.scale(prueba, (360, 140))
        imagen = pruebaR
        efecto = presentacion_efecto
        
        if efecto == 'Aleatorio.py': #AbajoArriba  Instantaneo   ArribbaAbajo   DerechaIzquierda             
            # x = 60, 6 cuadros
            # y = 35, 4 cuadros
            cuadros_y = [0, 1, 2, 3]
            cuadros_x = [0, 1, 2, 3, 4, 5]
            x = 60
            y = 35 
            
            cuadros_utilizados = []
            for i in range(0, len(cuadros_y)*len(cuadros_x)):
                self.ventana.blit(imagen, (720, 250))
                while True:
                    aleatorio_y = random.randint(0, len(cuadros_y) - 1)
                    aleatorio_x = random.randint(0, len(cuadros_x) - 1)
                    if not [aleatorio_y, aleatorio_x] in cuadros_utilizados:
                        break 
                cuadros_utilizados.append([aleatorio_y, aleatorio_x])
                
                for i in range(0, 4):
                    cord_y = 250 + y * i
                    for j in range(0, 6):
                        cord_x = 720 + x * j 
                        if not ([i, j] in cuadros_utilizados):
                            pygame.draw.rect(self.ventana, self.negro, Rect(cord_x, cord_y, x, y))
                            
                ticks_inicial = pygame.time.get_ticks()
                ticks_final = ticks_inicial + 0.2 * 1000
                while True:
                    ticks_inicial = pygame.time.get_ticks()
                    if ticks_inicial > ticks_final:
                        break
                    pygame.display.flip()

        if efecto == 'AbajoArriba.py':
            cordYDown = 390
            velY = 2
            efecto_DtU = True
            while efecto_DtU:
                cordYDown -= velY
                self.ventana.blit(imagen, (720, cordYDown))
                cuadro = Rect(720, 390, 360, 140)
                pygame.draw.rect(self.ventana, self.blanco, cuadro)
                if cordYDown <= 250:
                    efecto_DtU = False
                pygame.display.flip()
                self.clock.tick(self.FPS)
            
        elif efecto == 'Instantaneo.py':
            ticks_inicial = pygame.time.get_ticks()
            ticks_final = ticks_inicial + 2 * 1000
            while True:
                ticks_inicial = pygame.time.get_ticks()
                self.ventana.blit(imagen, (720, 250))
                if ticks_inicial > ticks_final:
                    break
                pygame.display.flip()
            
        elif efecto == 'ArribaAbajo.py':
            cordYUp = 110
            velY = 2
            efecto_UtD = True
            while efecto_UtD:
                cordYUp += velY
                self.ventana.blit(imagen, (720, cordYUp))
                cuadro = Rect(720, 110, 360, 140)
                pygame.draw.rect(self.ventana, self.blanco, cuadro)
                pygame.draw.line(self.ventana, self.negro, (0,120), (1200,120), 5)
                if cordYUp >= 250:
                    efecto_UtD = False
                pygame.display.flip()
                self.clock.tick(self.FPS)
        
        elif efecto == 'DerechaIzquierda.py':
            cordXDer = 1080
            velX = 4
            efecto_DI = True
            while efecto_DI:
                cordXDer -= velX
                self.ventana.blit(imagen, (cordXDer, 250))
                cuadro = Rect(1080, 250, 120, 140)
                pygame.draw.rect(self.ventana, self.blanco, cuadro)
                if cordXDer <= 720:
                    efecto_DI = False
                pygame.display.flip()
                self.clock.tick(self.FPS)
                   
        print(presentacion_efecto)

ver = Visualizar()
ver.mostrar()