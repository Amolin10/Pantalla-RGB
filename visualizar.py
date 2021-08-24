
from tkinter import font
from pygame import * 
import sys, pygame
from pygame.draw import line
from pygame.font import SysFont


pygame.init()

size = (1200, 560)

ventana = pygame.display.set_mode(size)

blanco = (255,255,255)
silver = (192,192,192)
negro = (0,0,0)
gray = (128,128,128)
lightblue = (173,216,230)

#Imagen de ventana y título
pygame.display.set_caption("Visualizar")
icono = pygame.image.load("./recursos/firefly.png")
pygame.display.set_icon(icono)


uam = pygame.image.load("./recursos/uamazcL.png")
uamAzc = pygame.transform.scale(uam, (300, 80))
cbi = pygame.image.load("./recursos/cbi.png")
cbiAzc = pygame.transform.scale(cbi, (300, 80))

prueba = pygame.image.load("./recursos/RGB.jpg")
pruebaR = pygame.transform.scale(prueba, (360, 140))

miFuente = pygame.font.SysFont("Verdana", 30)
text = miFuente.render("Visualización de animación", 0, (negro))
fuente = pygame.font.SysFont("Verdana", 20)
nomImagen = fuente.render("Nombre de imagen: ", 0, (negro))
nomEfecto = fuente.render("Efecto: ", 0, (negro))
tiempo = fuente.render("Tiempo: ", 0, (negro))
seg = fuente.render("segundos.", 0, (negro))

play = Rect(660, 420, 80, 25)
pause = Rect(860, 420, 80, 25)
stop = Rect(1060, 420, 80, 25)
salir = Rect(1060, 500, 80, 25)
vel1 = Rect(35, 420, 130, 25)
vel2 = Rect(235, 420, 130, 25)
vel4 = Rect(435, 420, 130, 25)

fuente2 = pygame.font.SysFont("Calibri", 20)

def crearBoton(screen, boton, mensaje):
    if boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(ventana, silver, boton)
    else:
        pygame.draw.rect(ventana, gray, boton)
    texto = fuente2.render(mensaje, True, (blanco))
    screen.blit(texto, (boton.x+(boton.width-texto.get_width())/2,
    boton.y+(boton.height-texto.get_height())/2)
    )

clock = pygame.time.Clock()
FPS = 17


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ventana.fill(blanco)    #Color de fondo
    ventana.blit(uamAzc, (50, 20))
    ventana.blit(text, (400,40))
    ventana.blit(cbiAzc, (850, 20))
    pygame.draw.line(ventana, negro, (0,120), (1200,120), 5)
    pygame.draw.line(ventana, negro, (600,120), (600,600), 5)
    pygame.draw.rect(ventana, silver, (720, 200, 360, 140))
    ventana.blit(pruebaR, (720, 200))
    ventana.blit(nomImagen, (50,150))
    ventana.blit(nomEfecto, (50,220))
    ventana.blit(tiempo, (50,290))
    ventana.blit(seg, (230,290))

    crearBoton(ventana, play, "Play")
    crearBoton(ventana, pause, "Pause")
    crearBoton(ventana, stop, "Stop")
    crearBoton(ventana, salir, "Salir")
    crearBoton(ventana, vel1, "Velocidad  x1")
    crearBoton(ventana, vel2, "Velocidad  x2")
    crearBoton(ventana, vel4, "Velocidad  x4")

    pygame.display.flip()
    clock.tick(FPS)