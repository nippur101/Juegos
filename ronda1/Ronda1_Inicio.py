import os
import pygame

# Cambiar al directorio donde se encuentra el script
script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

# Definir la función de pantalla
def damePantalla():
    pygame.init()
    pygame.display.set_caption("OFIRCA 2024 - Ronda 1 - Inicio")
    pantalla = pygame.display.set_mode((1152, 648))         
    return pantalla

pantalla = damePantalla()
pygame.font.init()
tipografia = pygame.font.SysFont('Arial', 18)
tipografiaGrande = pygame.font.SysFont('Arial', 24)
tipografiaMuyGrande = pygame.font.SysFont('Arial', 32)
colorVerde, colorAzul, colorBlanco, colorNegro, colorNaranja, colorBordeaux = (11, 102, 35), (0, 0, 255), (255, 255, 255), (0, 0, 0), (239, 27, 126), (102, 41, 53)

# Variables de bucle de juego
ticksAlComenzar = pygame.time.get_ticks()
clock = pygame.time.Clock()
juegoEnEjecucion = True

# Cargo los recursos
try:
    imgFondo = pygame.image.load("fondo.png")
    imgUAIBOT = pygame.transform.scale(pygame.image.load("UAIBOT.png").convert_alpha(), (pantalla.get_width() // 12, pantalla.get_height() // 12))
    imgBolsaVerde = pygame.transform.scale(pygame.image.load("BolsaVerde.png").convert_alpha(), (pantalla.get_width() // 12, pantalla.get_height() // 12))
    imgBolsaGrisOscuro = pygame.transform.scale(pygame.image.load("BolsaGrisOscuro.png").convert_alpha(), (pantalla.get_width() // 12, pantalla.get_height() // 12))
    imgCestoNegro = pygame.transform.scale(pygame.image.load("cestonegro.png").convert_alpha(), (pantalla.get_width() // 12, pantalla.get_height() // 12))
    imgCestoVerde = pygame.transform.scale(pygame.image.load("cestoverde.png").convert_alpha(), (pantalla.get_width() // 12, pantalla.get_height() // 12))
except pygame.error as e:
    print(f"Error al cargar las imágenes: {e}")

# Datos de personaje
nombrePersonaje = 'UAIBOT'
avatar = imgUAIBOT
avatar_rect = avatar.get_rect()
avatar_rect.x = 100
avatar_rect.y = 500
rapidezPersonaje = 10

# Operaciones de renderización 
def dibujarFondo():
    pantalla.blit(imgFondo, (0, 0))

def dibujarTexto(texto, tipografia, colorTexto, anchoRecuadro, altoRecuadro, colorRecuadro, posX, posY ):
    textoReglas = tipografia.render(texto, False, colorTexto)
    pygame.draw.rect(pantalla, colorRecuadro, (posX, posY, anchoRecuadro, altoRecuadro))
    pantalla.blit(textoReglas, (posX + 5, posY + 5, anchoRecuadro, altoRecuadro))

def dibujarUIyFondo():
    dibujarFondo()
    dibujarTexto('Elige a tu personaje con la tecla C y muévelo con las flechas para recolectar residuos y llevarlos a sus cestos correspondientes.', tipografia, colorBlanco, 820, 30, colorBordeaux, 15, 3)

def dibujarBasuraYTachos():
    pantalla.blit(imgBolsaGrisOscuro, (100, 300))
    pantalla.blit(imgBolsaGrisOscuro, (400, 500))
    pantalla.blit(imgBolsaVerde, (400, 200))
    pantalla.blit(imgCestoNegro, (900, 400))
    pantalla.blit(imgCestoVerde, (900, 200))

def dibujarJugador():
    global avatar
    pantalla.blit(avatar, avatar_rect)

def dibujarTodo():  
    dibujarUIyFondo()
    dibujarBasuraYTachos() 
    dibujarJugador()   

def iniciarJuego():
    global ticksAlComenzar, rapidezPersonaje
    ticksAlComenzar = pygame.time.get_ticks()
    rapidezPersonaje = 10   

iniciarJuego()

# Bucle de juego
while juegoEnEjecucion:        
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            juegoEnEjecucion = False
                                 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        avatar_rect.y -= rapidezPersonaje 
    
    clock.tick(60) 
    
    dibujarTodo()
    pygame.display.flip()
          
pygame.quit()
