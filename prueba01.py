import pygame
import time

play: bool = True
playin = 1
GamePreview = 0 #Poner en Cero(0) por Defecto

clock=pygame.time.Clock()
#pantalla
HEIGHT=600
WIDTH=800
BACKGROUND_COLOR=(99,155,255) #color del Rio
#Player Position
playerId=0
posY = 550
posX = 400
Speed = 0.2
playerHeight=40
playerWidth=40
#NPC Game ONE(1)
N1_posY = 260
N1_posX = 150

#NPC Game TWO(2)
N2_posY = 15
N2_posX = 250

#NPC Game TREE(3)
N3_posY = 300
N3_posX = 700

#NPC Game four(4)
N4_posY = 500
N4_posX = 30

#NPC Game five(5)
N5_posY = 100
N5_posX = 100

#NPC Game six(6)
N6_posY = 200
N6_posX = 200

#NPC Game seven(7)
N7_posY = 450
N7_posX = 460

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OFIRCA Olimpiadas")

# Cargo los recursos
try:
    robots = [
            pygame.image.load("UAIBOT.png"),  
            pygame.image.load("UAIBOTA.png"),
            pygame.image.load("UAIBOTINA.png"),
            pygame.image.load("UAIBOTINO.png")
        ]
    
    imgFondo = pygame.image.load('fondojuegodefi.png').convert()
    imgFondo = pygame.transform.scale(imgFondo, (WIDTH, HEIGHT))
    imgUAIBOT=robots[0]
    #imgUAIBOT = pygame.image.load("UAIBOT.png")
    imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))  # Cambia (50, 50) al tamaño deseado
    imgTacho = pygame.image.load("tacho-de-basura.png")
    imgTacho = pygame.transform.scale(imgTacho, (100,100))
    imgBasura = pygame.image.load ("Bolsa negra.png")
    imgBasura = pygame.transform.scale(imgBasura, (75,75))
    imgTacho2 = pygame.image.load ("tacho-de-basura2.png")
    imgTacho2 = pygame.transform.scale (imgTacho2, (100,100))
    imgBasura2 = pygame.image.load ("Bolsa verde.png")
    imgBasura2= pygame.transform.scale (imgBasura2, (75,75))
except pygame.error as e:
    print(f"Error al cargar las imágenes: {e}")


#personaje pa
nombrePersonaje = 'UAIBOT'
avatar = imgUAIBOT
avatar_rect = avatar.get_rect()
posY = 205
posX = 375
Speed = 0.8

#Colores
White = (255,255,255)
Black = (0, 0, 0)
Green = (0, 255, 0)
Grey = (50, 50, 50)

#Funciones
def cambiar_player(id):
    time.sleep(0.200)
    if(id==3):
        return 0
    else:
        id+=1
        return id
    
def colision_fondo_infraqueable(x, y, width, height):
    x = int(x)
    y = int(y)
    width = int(width)
    height = int(height)
    for i in range(x, x + width):
        for j in range(y, y + height):
            if imgFondo.get_at((i, j)) == BACKGROUND_COLOR:
                return True
    return False


def Inicio():
    screen.blit(imgFondo, (0, 0))
    
def dibujarJugador():
    global avatar
    screen.blit(avatar, (posX, posY)) #Movimiento a la imagen del robot
    #screen.blit(avatar, avatar_rect)
    
def preview1():
    pygame.draw.rect(screen, Grey, (250, 10, 500, 400)) #Contenedor.
    #pygame.draw.rect(screen, White, (200)) #Descripcion del Juego.

def dibujartachos():
    global imgTacho
    screen.blit(imgTacho, (N1_posX, N1_posY))
    global imgTacho2
    screen.blit(imgTacho2, (N7_posX, N7_posY))

def dibujarbasuras():
    global imgBasura
    screen.blit(imgBasura, (N2_posX, N2_posY ))
    screen.blit(imgBasura, (N3_posX, N3_posY ))
    screen.blit(imgBasura, (N4_posX, N4_posY ))
    global imgBasura2
    screen.blit(imgBasura2, (N5_posX, N5_posY ))
    screen.blit(imgBasura2, (N6_posX, N6_posY ))

    
    




while play:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    keys = pygame.key.get_pressed()
    new_x, new_y = posX, posY

    if keys[pygame.K_LEFT]:
        new_x -= Speed
    if keys[pygame.K_RIGHT]:
        new_x += Speed
    if keys[pygame.K_UP]:
        new_y -= Speed
    if keys[pygame.K_DOWN]:
        new_y += Speed
        
        
    if keys[pygame.K_c]:
        playerId=cambiar_player(playerId)
        print(playerId)
        imgUAIBOT=robots[playerId]
        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
        avatar = imgUAIBOT
        
    # Verificar colisiones con el color de fondo
    if not colision_fondo_infraqueable(new_x, new_y, playerWidth, playerHeight):
        posX = new_x
        posY = new_y

    #Colocando limites en los bordes
    if posX<0:
        posX=0
    if posX+playerWidth>WIDTH:
        posX=WIDTH-playerWidth
    if posY<0:
        posY=0
    if posY+playerHeight>HEIGHT:
        posY=HEIGHT-playerHeight
    

    #Visualizacion
    if playin == 1:
        Inicio()
        
    if GamePreview == 1:
        preview1()

    dibujarJugador() 
    dibujartachos()
    dibujarbasuras()
    pygame.display.update()
            
pygame.quit()            