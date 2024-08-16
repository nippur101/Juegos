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
playerHeight=45
playerWidth=45

contBasuraCargada=0 #contado de basura que lleva el robot
#basura
basuraWidth=75
basuraHeight=75


#Tachos
T1_posY = 260
T1_posX = 150

T2_posY = 450
T2_posX = 460

#NPC Game TWO(2)
N2_posY = 15
N2_posX = 250

#NPC Game TREE(3)
N3_posY = 300
N3_posX = 700

#NPC Game four(4)
N4_posY = 500
N4_posX = 30

#Basura verde
V1_posY = 100
V1_posX = 100

V2_posY = 200
V2_posX = 200

V3_posY = 150
V3_posX = 300

V4_posY = 250
V4_posX = 300



# ARBOLES=====
A1_posY = 480
A1_posX = 265

A2_posY = 150
A2_posX = 120

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
    imgUAIBOT=robots[0]                                              #robot elegido
    imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))  # Cambia (50, 50) al tamaño deseado
    #Tachos===============================================
    imgTacho = pygame.image.load("tacho-de-basura.png")
    imgTacho = pygame.transform.scale(imgTacho, (100,100))
    imgTacho2 = pygame.image.load ("tacho-de-basura2.png")
    imgTacho2 = pygame.transform.scale (imgTacho2, (100,100))
    #basura===============================================
    imgBasuraN1 = pygame.image.load ("Bolsa negra.png")
    imgBasuraN1 = pygame.transform.scale(imgBasuraN1, (75,75))
    imgBasuraN2 = pygame.image.load ("Bolsa negra.png")
    imgBasuraN2= pygame.transform.scale(imgBasuraN2, (75,75))
    imgBasuraN3 = pygame.image.load ("Bolsa negra.png")
    imgBasuraN3 = pygame.transform.scale(imgBasuraN3, (75,75))
    imgBasuraV1 = pygame.image.load ("Bolsa verde.png")
    imgBasuraV1= pygame.transform.scale (imgBasuraV1, (75,75))
    imgBasuraV2 = pygame.image.load ("Bolsa verde.png")
    imgBasuraV2= pygame.transform.scale (imgBasuraV2, (75,75))
    imgBasuraV3 = pygame.image.load ("Bolsa verde.png")
    imgBasuraV3= pygame.transform.scale (imgBasuraV3, (75,75))
    imgBasuraV4 = pygame.image.load ("Bolsa verde.png")
    imgBasuraV4= pygame.transform.scale (imgBasuraV4, (75,75))
   
    
   #fondo complementos===============================================
    imgArbol = pygame.image.load ("arbol.png")
    imgArbol = pygame.transform.scale (imgArbol, (110,110))
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
def colision_basuraN(x1, y1):
        for i, basura in enumerate(basurasN):
            x2 = basura["posX"]
            y2 = basura["posY"]
            if x1 < x2 + basuraWidth and x1 + playerWidth > x2 and y1 < y2 + basuraHeight and y1 + playerHeight > y2:
                return i
        return None

def colision_basuraV(x1, y1):
        for i, basura in enumerate(basurasV):
            x2 = basura["posX"]
            y2 = basura["posY"]
            if x1 < x2 + basuraWidth and x1 + playerWidth > x2 and y1 < y2 + basuraHeight and y1 + playerHeight > y2:
                return i
        return None


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
    screen.blit(avatar, avatar_rect)
    
def preview1():
    pygame.draw.rect(screen, Grey, (250, 10, 500, 400)) #Contenedor.
    #pygame.draw.rect(screen, White, (200)) #Descripcion del Juego.

def dibujartachos():
    global imgTacho
    screen.blit(imgTacho, (T1_posX, T1_posY))
    global imgTacho2
    screen.blit(imgTacho2, (T2_posX, T2_posY))
"""
def dibujarbasuras():
    #negras
    global imgBasuraN1
    screen.blit(imgBasuraN1, (N2_posX, N2_posY ))
    global imgBasuraN2
    screen.blit(imgBasuraN2, (N3_posX, N3_posY ))
    global imgBasuraN3
    screen.blit(imgBasuraN3, (N4_posX, N4_posY ))
    #verdes
    global imgBasuraV1
    screen.blit(imgBasuraV1, (V1_posX, V1_posY ))
    global imgBasuraV2
    screen.blit(imgBasuraV2, (V2_posX, V2_posY ))
    global imgBasuraV3
    screen.blit(imgBasuraV3, (V3_posX, V3_posY )) 
    global imgBasuraV4
    screen.blit(imgBasuraV4, (V4_posX, V4_posY ))
"""

def dibujarbasurasV():
    for basura in basurasV:
        screen.blit(basura["img"], (basura["posX"], basura["posY"]))

def dibujarbasurasN():
    for basura in basurasN:
        screen.blit(basura["img"], (basura["posX"], basura["posY"]))

def dibujararboles():
    global imgArbol
    screen.blit(imgArbol, (A1_posX, A1_posY))
    screen.blit(imgArbol, (A2_posX, A2_posY))

# Lista de posiciones de las basuras negras y verdes
basurasN = [
    {"img": imgBasuraN1, "posX": N2_posX, "posY": N2_posY},
    {"img": imgBasuraN2, "posX": N3_posX, "posY": N3_posY},
    {"img": imgBasuraN3, "posX": N4_posX, "posY": N4_posY}
    ]

basurasV =[{"img": imgBasuraV1, "posX": V1_posX, "posY": V1_posY},
    {"img": imgBasuraV2, "posX": V2_posX, "posY": V2_posY},
    {"img": imgBasuraV3, "posX": V3_posX, "posY": V3_posY},
    {"img": imgBasuraV4, "posX": V4_posX, "posY": V4_posY}]

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
    
    colision_idx = colision_basuraN(new_x, new_y)
    if colision_idx is not None:
        #print("tocando basura")
        del basurasN[colision_idx]

    colision_idx = colision_basuraV(new_x, new_y)
    if colision_idx is not None:
        #print("tocando basura")
        del basurasV[colision_idx]
        


    

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
    dibujarbasurasV()
    dibujarbasurasN()
    dibujararboles()
    pygame.display.update()
            
pygame.quit()            