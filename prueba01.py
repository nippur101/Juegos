import pygame
import time

play: bool = True
playin = 1
GamePreview = 0 #Poner en Cero(0) por Defecto

clock=pygame.time.Clock()
#pantalla
HEIGHT=600
WIDTH=800
RIVER_COLOR=(99,155,255) #color del Rio
ROAD_COLOR=(138,111,48)#color del camino
BRIDGE_COLOR=(102,57,49)

#Player Position
playerId=0
playerHeight=45
playerWidth=45

contBasuraCargadaN=0 #contado de basura que lleva el robot
contBasuraCargadaV=0
tomarBasura=True
#basura
basuraWidth=40
basuraHeight=40


#Tachos
tacho_width=70
tacho_height=70

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
A1_posX = 270

A2_posY = 360
A2_posX = 605

A3_posY = 335
A3_posX = 145

A4_posY = 150
A4_posX = 720

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OFIRCA Olimpiadas")

# Inicializa la fuente
font = pygame.font.Font(None, 36)  # None para la fuente predeterminada, 36 es el tamaño de la fuente
score = 0  # Variable para el puntaje

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
    imgTacho = pygame.transform.scale(imgTacho, (tacho_width,tacho_height))
    imgTacho2 = pygame.image.load ("tacho-de-basura2.png")
    imgTacho2 = pygame.transform.scale (imgTacho2, (tacho_width,tacho_height))
    #basura===============================================
    imgBasuraN1 = pygame.image.load ("Bolsa negra.png")
    imgBasuraN1 = pygame.transform.scale(imgBasuraN1, (basuraWidth,basuraHeight))
    imgBasuraN2 = pygame.image.load ("Bolsa negra.png")
    imgBasuraN2= pygame.transform.scale(imgBasuraN2, (basuraWidth,basuraHeight))
    imgBasuraN3 = pygame.image.load ("Bolsa negra.png")
    imgBasuraN3 = pygame.transform.scale(imgBasuraN3, (basuraWidth,basuraHeight))
    imgBasuraV1 = pygame.image.load ("Bolsa verde.png")
    imgBasuraV1= pygame.transform.scale (imgBasuraV1, (basuraWidth,basuraHeight))
    imgBasuraV2 = pygame.image.load ("Bolsa verde.png")
    imgBasuraV2= pygame.transform.scale (imgBasuraV2, (basuraWidth,basuraHeight))
    imgBasuraV3 = pygame.image.load ("Bolsa verde.png")
    imgBasuraV3= pygame.transform.scale (imgBasuraV3, (basuraWidth,basuraHeight))
    imgBasuraV4 = pygame.image.load ("Bolsa verde.png")
    imgBasuraV4= pygame.transform.scale (imgBasuraV4, (basuraWidth,basuraHeight))
   
    
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
            if imgFondo.get_at((i, j)) == RIVER_COLOR:
                return True
    return False

def colision_camino(x, y, width, height):
    x = int(x)
    y = int(y)
    width = int(width/2)
    height = int(height/2)
    for i in range(x, x + width):
        for j in range(y, y + height):
            if imgFondo.get_at((i, j)) == ROAD_COLOR or  imgFondo.get_at((i, j)) == BRIDGE_COLOR :
                return 1.5
            else:
                return 0.8
    


def Inicio():
    screen.blit(imgFondo, (0, 0))
    
def dibujarJugador():
    global avatar
    screen.blit(avatar, (posX, posY)) #Movimiento a la imagen del robot
    screen.blit(avatar, avatar_rect)
    
def preview1():
    pygame.draw.rect(screen, Grey, (250, 10, 500, 400)) #Contenedor.
    

def dibujartachos():
    global imgTacho
    screen.blit(imgTacho, (T1_posX, T1_posY))
    global imgTacho2
    screen.blit(imgTacho2, (T2_posX, T2_posY))
    
def dibujarpuntaje():
    texto = font.render(f"Score: {score}", True, White)
    screen.blit(texto, (50,10))

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
    screen.blit(imgArbol, (A3_posX, A3_posY))
    screen.blit(imgArbol, (A4_posX, A4_posY))

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
#================Bucle del Juego=========================================================================================
while play:

    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    keys = pygame.key.get_pressed()
    new_x, new_y = posX, posY

    Speed=colision_camino(new_x,new_y,playerWidth,playerHeight)
    #print(Speed)
    if keys[pygame.K_LEFT]:
        new_x -= Speed
    if keys[pygame.K_RIGHT]:
        new_x += Speed
    if keys[pygame.K_UP]:
        new_y -= Speed
    if keys[pygame.K_DOWN]:
        new_y += Speed
        
        
    if keys[pygame.K_c] and (posX==375 and posY==205):#bloqueo de cambio de personaje luego de comenzado el juego
        playerId=cambiar_player(playerId)
        #print(playerId)
        imgUAIBOT=robots[playerId]
        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
        avatar = imgUAIBOT
        
    # Verificar colisiones con el color de fondo
    if not colision_fondo_infraqueable(new_x, new_y, playerWidth, playerHeight):
        posX = new_x
        posY = new_y

    
    if(playerId==0 or playerId==1): 
        if(contBasuraCargadaN!=2 and contBasuraCargadaV!=2 and (contBasuraCargadaV+contBasuraCargadaN)!=2): #permite cargar solo 2 basuras como maximo
            tomarBasura=True
        else:   
            tomarBasura=False
    
    if(playerId==2 or playerId==3): 
        if( contBasuraCargadaN!=1 and contBasuraCargadaV!=1): #permite cargar solo 1 basuras como maximo
            tomarBasura=True
        else:
            tomarBasura=False

    if(tomarBasura):    
        colision_idx = colision_basuraN(new_x, new_y) #Colision con basura Negra
        if colision_idx is not None:
            #print("tocando basura")
            del basurasN[colision_idx]
            score+=100
            contBasuraCargadaN+=1
            print("Negra:",contBasuraCargadaN)
            match playerId:
                case 0:
                    if(contBasuraCargadaN==1 and contBasuraCargadaV==0):
                        imgUAIBOT=pygame.image.load("UAIBOT 1 bolsa negra.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT
                    elif(contBasuraCargadaN==2):
                        imgUAIBOT=pygame.image.load("UAIBOT 2 bolsas negras.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT
                    elif(contBasuraCargadaN==1 and contBasuraCargadaV==1):
                        imgUAIBOT=pygame.image.load("UAIBOT 2 bolsas negra y verde.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT


                case 1:
                    if(contBasuraCargadaN==1 and contBasuraCargadaV==0):
                        imgUAIBOT=pygame.image.load("UAIBOTA 1 bolsa negra.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT
                    elif(contBasuraCargadaN==2):
                        imgUAIBOT=pygame.image.load("UAIBOTA 2 bolsas negras.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT
                    elif(contBasuraCargadaN==1 and contBasuraCargadaV==1):
                        imgUAIBOT=pygame.image.load("UAIBOTA 2 bolsas negra y verde.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT
                case 2:
                    if(contBasuraCargadaN==1):
                        imgUAIBOT=pygame.image.load("UAIBOTINA 1 bolsa negra.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT
                case 3:
                    if(contBasuraCargadaN==1):
                        imgUAIBOT=pygame.image.load("UAIBOTINO 1 bolsa negra.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT
            
    if(tomarBasura):
        colision_idx = colision_basuraV(new_x, new_y)#Colision con basura Verde
        if colision_idx is not None:
            #print("tocando basura")
            del basurasV[colision_idx]
            score+=120
            contBasuraCargadaV+=1
            print("Verde:",contBasuraCargadaV)
            match playerId:
                case 0:
                    if(contBasuraCargadaV==1 and contBasuraCargadaN==0):
                        imgUAIBOT=pygame.image.load("UAIBOT 1 bolsa verde.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT
                    elif(contBasuraCargadaV==2):
                        imgUAIBOT=pygame.image.load("UAIBOT 2 bolsas verdes.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT
                    elif(contBasuraCargadaN==1 and contBasuraCargadaV==1):
                        imgUAIBOT=pygame.image.load("UAIBOT 2 bolsas negra y verde.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT

                case 1:
                    if(contBasuraCargadaV==1 and contBasuraCargadaN==0):
                        imgUAIBOT=pygame.image.load("UAIBOTA 1 bolsa verde.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT
                    elif(contBasuraCargadaV==2):
                        imgUAIBOT=pygame.image.load("UAIBOTA 2 bolsas verdes.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT
                    elif(contBasuraCargadaN==1 and contBasuraCargadaV==1):
                        imgUAIBOT=pygame.image.load("UAIBOTA 2 bolsas negra y verde.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT
                case 2:
                    if(contBasuraCargadaV==1):
                        imgUAIBOT=pygame.image.load("UAIBOTINA 1 bolsa verde.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT
                case 3:
                    if(contBasuraCargadaV==1):
                        imgUAIBOT=pygame.image.load("UAIBOTINO 1 bolsa verde.png")
                        imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
                        avatar = imgUAIBOT

        
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
    dibujarpuntaje()
    pygame.display.update()
#=======================================================================================================================

pygame.quit()           