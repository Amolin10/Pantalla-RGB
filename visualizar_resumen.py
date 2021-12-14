import pygame
from pygame import * 
import random

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

lista_configuracion = [] 

datos1 = Datos(1, './recursos/RGB.jpg', 'Aleatorio.py', 40)
datos2 = Datos(2, './recursos/computadora.png', 'DerechaIzquierda.py', 40)
datos3 = Datos(3, './recursos/electronica.jpg', 'Instantaneo.py', 51)
datos4 = Datos(4, './recursos/micro.jpg', 'AbajoArriba.py', 122)
datos5 = Datos(5, './recursos/uamazcL.png', 'ArribaAbajo.py', 179)

lista_configuracion.append(datos1)
lista_configuracion.append(datos2)
lista_configuracion.append(datos3)
lista_configuracion.append(datos4)
lista_configuracion.append(datos5)

pygame.init()
class VisualizarResumen:
    
    def __init__(self):
        pygame.init()
        
        self.numero_presentacion = 0
        
        self.presentacion_nombre = str(lista_configuracion[self.numero_presentacion].get_numero())
        self.presentacion_imagen = lista_configuracion[self.numero_presentacion].get_imagen()
        self.presentacion_efecto = lista_configuracion[self.numero_presentacion].get_efecto()
        self.presentacion_tiempo = str(lista_configuracion[self.numero_presentacion].get_tiempo())
        
        self.size = (1200, 560)
        self.ventana = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Visualizar")
        icono = pygame.image.load("./recursos/firefly.png")
        pygame.display.set_icon(icono)
        
        self.cargar_elementos()        
        
    def cargar_elementos(self):
        self.blanco = (255,255,255)
        self.silver = (192,192,192)
        self.negro = (0,0,0)
        self.gray = (128,128,128)
        self.lightblue = (173,216,230)

        uam = pygame.image.load("./recursos/uamazcL.png")
        self.uamAzc = pygame.transform.scale(uam, (300, 80))
        cbi = pygame.image.load("./recursos/cbi.png")
        self.cbiAzc = pygame.transform.scale(cbi, (300, 80))

        #prueba = pygame.image.load(self.presentacion_imagen)
        #self.pruebaR = pygame.transform.scale(prueba, (360, 140))

        miFuente = pygame.font.SysFont("Verdana", 30)
        self.text = miFuente.render("Visualización de animación", 0, (self.negro))
        fuente = pygame.font.SysFont("Verdana", 20)
        
        #prueba = pygame.image.load(self.presentacion_imagen)
        #self.pruebaR = pygame.transform.scale(prueba, (360, 140))
        #self.nom_Imagen = fuente.render("Número de imagen: ", 0, (self.negro))
        #self.nombre_imagen = fuente.render(self.presentacion_nombre, 0, (self.negro))
        #self.nomEfecto = fuente.render("Efecto: ", 0, (self.negro))
        #self.nombre_efecto = fuente.render(self.presentacion_efecto, 0, (self.negro))
        #self.tiempo = fuente.render("Tiempo: ", 0, (self.negro))
        #self.seg = fuente.render(self.presentacion_tiempo, 0, (self.negro))

        self.play = Rect(630, 500, 80, 25)
        self.regresar = Rect(1085, 500, 80, 25)
        self.siguiente = Rect(1085, 450, 80, 25)
        self.anterior = Rect(630, 450, 80, 25)
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

            if event.type == MOUSEBUTTONDOWN:
                if self.siguiente.collidepoint(pygame.mouse.get_pos()):
                    if self.numero_presentacion >= len(lista_configuracion) -1 :
                        pass
                    else:
                        self.siguiente_presentacion()
                        self.mostrar_ventana()
                        self.presentar_efecto()
                        coordenada_x_inicial = 720
                        coordenada_y_inicial = 250
                    
            if event.type == MOUSEBUTTONDOWN:
                if self.anterior.collidepoint(pygame.mouse.get_pos()):
                    if self.numero_presentacion <= 0:
                        pass
                    else:
                        self.anterior_presentacion()
                        self.mostrar_ventana()
                        self.presentar_efecto()
                        coordenada_x_inicial = 720
                        coordenada_y_inicial = 250

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

     
    def siguiente_presentacion(self):
    
        self.numero_presentacion += 1
        self.presentacion_nombre = str(lista_configuracion[self.numero_presentacion].get_numero())
        self.presentacion_imagen = lista_configuracion[self.numero_presentacion].get_imagen()
        self.presentacion_efecto = lista_configuracion[self.numero_presentacion].get_efecto()
        self.presentacion_tiempo = str(lista_configuracion[self.numero_presentacion].get_tiempo())
        
    def anterior_presentacion(self):
        
            self.numero_presentacion -= 1
            self.presentacion_nombre = str(lista_configuracion[self.numero_presentacion].get_numero())
            self.presentacion_imagen = lista_configuracion[self.numero_presentacion].get_imagen()
            self.presentacion_efecto = lista_configuracion[self.numero_presentacion].get_efecto()
            self.presentacion_tiempo = str(lista_configuracion[self.numero_presentacion].get_tiempo())
        
    def mostrar_ventana(self):
        self.ventana.fill(self.blanco)    #Color de fondo
        self.ventana.blit(self.uamAzc, (50, 20))
        self.ventana.blit(self.text, (400,40))
        self.ventana.blit(self.cbiAzc, (850, 20))
        pygame.draw.line(self.ventana, self.negro, (0,120), (1200,120), 5)
        pygame.draw.line(self.ventana, self.negro, (600,120), (600,600), 5)
        pygame.draw.rect(self.ventana, self.silver, (720, 250, 360, 140))
                
        miFuente = pygame.font.SysFont("Verdana", 30)
        self.text = miFuente.render("Visualización de animación", 0, (self.negro))
        fuente = pygame.font.SysFont("Verdana", 20)

        self.nom_Imagen = fuente.render("Número de imagen: ", 0, (self.negro))
        self.nombre_imagen = fuente.render(self.presentacion_nombre, 0, (self.negro))
        self.nomEfecto = fuente.render("Efecto: ", 0, (self.negro))
        self.nombre_efecto = fuente.render(self.presentacion_efecto, 0, (self.negro))
        self.tiempo = fuente.render("Tiempo: ", 0, (self.negro))
        self.seg = fuente.render(self.presentacion_tiempo, 0, (self.negro))

        self.ventana.blit(self.nom_Imagen, (50,150))
        self.ventana.blit(self.nombre_imagen, (280,150))
        self.ventana.blit(self.nomEfecto, (175,220))
        self.ventana.blit(self.nombre_efecto, (280, 220))
        self.ventana.blit(self.tiempo, (165,290))
        self.ventana.blit(self.seg, (280,290))                    

        prueba = pygame.image.load(self.presentacion_imagen)
        self.pruebaR = pygame.transform.scale(prueba, (360, 140))
        
        self.crearBoton(self.ventana, self.play, "Play")
        self.crearBoton(self.ventana, self.regresar, "Salir")
        self.crearBoton(self.ventana, self.siguiente, "Siguiente")
        self.crearBoton(self.ventana, self.anterior, "Anterior")
       

    def presentar_efecto(self):
        pygame.draw.rect(self.ventana, self.silver, (720, 250, 360, 140))
        prueba = pygame.image.load(self.presentacion_imagen)
        pruebaR = pygame.transform.scale(prueba, (360, 140))
        imagen = pruebaR
        efecto = self.presentacion_efecto
        
        if efecto == 'Aleatorio.py': #AbajoArriba  Instantaneo   ArribbaAbajo   DerechaIzquierda                        
            # y = 10, 14 cuadros
            # x = 15, 24 cuadros
            # tiempo = 0.01
            cuadros_y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            cuadros_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
            y = 10 
            x = 15
            
            cuadros_utilizados = []
            for i in range(0, len(cuadros_y)*len(cuadros_x)):
                self.ventana.blit(imagen, (720, 250))
                while True:
                    aleatorio_y = random.randint(0, len(cuadros_y) - 1)
                    aleatorio_x = random.randint(0, len(cuadros_x) - 1)
                    if not [aleatorio_y, aleatorio_x] in cuadros_utilizados:
                        break 
                cuadros_utilizados.append([aleatorio_y, aleatorio_x])
                
                for i in range(0, len(cuadros_y)):
                    cord_y = 250 + y * i
                    for j in range(0, len(cuadros_x)):
                        cord_x = 720 + x * j 
                        if not ([i, j] in cuadros_utilizados):
                            pygame.draw.rect(self.ventana, self.negro, Rect(cord_x, cord_y, x, y))
                            
                ticks_inicial = pygame.time.get_ticks()
                ticks_final = ticks_inicial + 0.01 * 1000
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
                   
        print(self.presentacion_efecto)

ver = VisualizarResumen()
ver.mostrar()