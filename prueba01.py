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


#Tachos posicion
tacho_width=60
tacho_height=60

TN_posY = 260
TN_posX = 150

TV_posY = 450
TV_posX = 460

#Basura negra posicion
N2_posY = 50
N2_posX = 250

N3_posY = 300
N3_posX = 700

N4_posY = 500
N4_posX = 30

#Basura verde posicion
V1_posY = 100
V1_posX = 100

V2_posY = 500
V2_posX = 600

V3_posY = 150
V3_posX = 300

V4_posY = 50
V4_posX = 700



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
font2 = pygame.font.Font(None, 72) 
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
    imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))  
    #Tachos===============================================
    imgTachoN = pygame.image.load("tacho-de-basura.png")
    imgTachoN = pygame.transform.scale(imgTachoN, (tacho_width,tacho_height))
    imgTachoV = pygame.image.load ("tacho-de-basura2.png")
    imgTachoV = pygame.transform.scale (imgTachoV, (tacho_width,tacho_height))
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
    imgPantallaInicio = pygame.image.load("portada800x600.jpg")
    imgPantallaReglas = pygame.image.load("portadaReglas800x600.jpg")
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

def mostrarPantallaFinal(score):
    imgGanaste = pygame.image.load("ganaste.jpg").convert()
    imgGanaste = pygame.transform.scale(imgGanaste, (WIDTH, HEIGHT))
    screen.blit(imgGanaste, (0, 0)) 
    texto_final = font2.render(f"Score Final: {score}", True, Grey)
    screen.blit(texto_final, (WIDTH // 2 - texto_final.get_width() // 2, HEIGHT // 2 - texto_final.get_height() // 2))
    esperandoInicio=True
    pygame.display.flip()
    while esperandoInicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

def temporizador():
    # Calcula el tiempo transcurrido en segundos
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000

    seconds = min(elapsed_time, 60)

    tiempo_texto = font.render(f"Tiempo: {seconds:02}", True, White)
    
    text_rect = tiempo_texto.get_rect(center=(WIDTH // 2, 20))
    
    screen.blit(tiempo_texto, text_rect)
    return seconds
    
    
def mostrarPantallaInicio(imgPantallaInicio):
    screen.blit(imgPantallaInicio, (0, 0))
    pygame.display.flip()

    esperandoInicio = True
    while esperandoInicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                esperandoInicio = False
def mostrarPantallaInicio(imgPantallaInicio):
    screen.blit(imgPantallaInicio, (0, 0))
    pygame.display.flip()

    esperandoInicio = True
    while esperandoInicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                esperandoInicio = False



def cambioImagenesBotsBolsas(playerId,contBasuraCargadaN,contBasuraCargadaV):
    match playerId:
        case 0:
            if(contBasuraCargadaN==0 and contBasuraCargadaV==0):
                avatar=robots[playerId]                                              #robot elegido
                avatar = pygame.transform.scale(avatar, (playerHeight, playerWidth)) 
            elif(contBasuraCargadaN==1 and contBasuraCargadaV==0):
                avatar = cargarImagenTomandoBolsas("UAIBOT 1 bolsa negra.png")

            elif(contBasuraCargadaN==2):
                avatar = cargarImagenTomandoBolsas("UAIBOT 2 bolsas negras.png")

            elif(contBasuraCargadaN==1 and contBasuraCargadaV==1):                        
                avatar = cargarImagenTomandoBolsas("UAIBOT 2 bolsas negra y verde.png")

            elif(contBasuraCargadaV==1 and contBasuraCargadaN==0):                       
                avatar = cargarImagenTomandoBolsas("UAIBOT 1 bolsa verde.png")

            elif(contBasuraCargadaV==2):                        
                avatar = cargarImagenTomandoBolsas("UAIBOT 2 bolsas verdes.png")
          

        case 1:
            if(contBasuraCargadaN==0 and contBasuraCargadaV==0):
                avatar = robots[playerId]
                avatar = pygame.transform.scale(avatar, (playerHeight, playerWidth)) 
            elif(contBasuraCargadaN==1 and contBasuraCargadaV==0):                        
                avatar = cargarImagenTomandoBolsas("UAIBOTA 1 bolsa negra.png")

            elif(contBasuraCargadaN==2):                       
                avatar = cargarImagenTomandoBolsas("UAIBOTA 2 bolsas negras.png")

            elif(contBasuraCargadaN==1 and contBasuraCargadaV==1):                       
                        avatar = cargarImagenTomandoBolsas("UAIBOTA 2 bolsas negra y verde.png")

            elif(contBasuraCargadaV==1 and contBasuraCargadaN==0):
                avatar = cargarImagenTomandoBolsas("UAIBOTA 1 bolsa verde.png")

            elif(contBasuraCargadaV==2):                        
                avatar = cargarImagenTomandoBolsas("UAIBOTA 2 bolsas verdes.png")

        case 2:
            if(contBasuraCargadaN==0 and contBasuraCargadaV==0):
                avatar = robots[playerId]
                avatar = pygame.transform.scale(avatar, (playerHeight, playerWidth))

            elif(contBasuraCargadaN==1 and contBasuraCargadaV==0):                        
                avatar = cargarImagenTomandoBolsas("UAIBOTINA 1 bolsa negra.png")

            elif(contBasuraCargadaN==0 and contBasuraCargadaV==1):
                avatar = cargarImagenTomandoBolsas("UAIBOTINA 1 bolsa verde.png")

            elif(contBasuraCargadaN==1 and contBasuraCargadaV==1):                        
                avatar = cargarImagenTomandoBolsas("UAIBOTINA 2 bolsas negra y verde.png")

        case 3:
            if(contBasuraCargadaN==0 and contBasuraCargadaV==0):
                avatar = robots[playerId]
                avatar = pygame.transform.scale(avatar, (playerHeight, playerWidth))

            elif(contBasuraCargadaN==1 and contBasuraCargadaV==0):                        
                avatar = cargarImagenTomandoBolsas("UAIBOTINO 1 bolsa negra.png")

            elif(contBasuraCargadaN==0 and contBasuraCargadaV==1):                       
                avatar = cargarImagenTomandoBolsas("UAIBOTINO 1 bolsa verde.png")

            elif(contBasuraCargadaN==1 and contBasuraCargadaV==1):                        
                avatar = cargarImagenTomandoBolsas("UAIBOTINO 2 bolsas negra y verde.png")

    return avatar


def cargarImagenTomandoBolsas(imageName):
    #print(imageName)
    imgUAIBOT=pygame.image.load(imageName)
    imgUAIBOT = pygame.transform.scale(imgUAIBOT, (playerHeight, playerWidth))
    avatar = imgUAIBOT
    return avatar

def colision_TachoN(x1, y1):        
    x2 = TN_posX
    y2 = TN_posY
    if x1 < x2 + tacho_width and x1 + playerWidth > x2 and y1 < y2 + tacho_height and y1 + playerHeight > y2:
        return True
    return False

def colision_TachoV(x1, y1):        
    x2 = TV_posX
    y2 = TV_posY
    if x1 < x2 + tacho_width and x1 + playerWidth > x2 and y1 < y2 + tacho_height and y1 + playerHeight > y2:
        return True
    return False

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

def colision_camino(x, y, width, height,playerId):
    x = int(x)
    y = int(y)
    velocity=0.8
    width = int(width/2)
    height = int(height/2)
    for i in range(x, x + width):
        for j in range(y, y + height):
            if imgFondo.get_at((i, j)) == ROAD_COLOR or  imgFondo.get_at((i, j)) == BRIDGE_COLOR :
                if(playerId==0 or playerId==1):
                    velocity= 1.5
                elif(playerId==2 or playerId==3):
                    velocity= 2.5
            else:
                if(playerId==0 or playerId==1):
                    velocity= 0.8
                else:                    
                    velocity= 1.5                
                    
    return velocity
    


def Inicio():
    screen.blit(imgFondo, (0, 0))
    
    
def dibujarJugador():
    global avatar
    screen.blit(avatar, (posX, posY)) #Movimiento a la imagen del robot
    screen.blit(avatar, avatar_rect)
    
def preview1():
    pygame.draw.rect(screen, Grey, (250, 10, 500, 400)) #Contenedor.
    

def dibujartachos():
    global imgTachoN
    screen.blit(imgTachoN, (TN_posX, TN_posY))
    global imgTachoV
    screen.blit(imgTachoV, (TV_posX, TV_posY))
    
def dibujarpuntaje(playerId):
    if(playerId==0):
        name="UAIBOT"
    elif(playerId==1):
        name="UAIBOTA"
    elif(playerId==2):
        name="UAIBOTINA"
    elif(playerId==3):
        name="UAIBOTINO"
    texto = font.render(f"{name} Score: {score}", True, White)
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
mostrarPantallaInicio(imgPantallaInicio)
mostrarPantallaInicio(imgPantallaReglas)
bandera=True
segundos=0
while play:
    if(bandera==True):#para que arranque el tiempo cuando empieza el juego
        start_time = pygame.time.get_ticks()
        bandera=False
        
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    keys = pygame.key.get_pressed()
    new_x, new_y = posX, posY

    Speed=colision_camino(new_x,new_y,playerWidth,playerHeight,playerId)
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

    #print(colision_TachoN(new_x,new_y))

    if(colision_TachoN(new_x,new_y)):
        if(contBasuraCargadaN==1):
             contBasuraCargadaN=0
             score+=100
             #sumar Score
        elif(contBasuraCargadaN==2):
             contBasuraCargadaN=0
             score+=200
             #sumar Score
        tomarBasura=True
        if(contBasuraCargadaV!=2):
            avatar=cambioImagenesBotsBolsas(playerId,contBasuraCargadaN,contBasuraCargadaV)

    if(tomarBasura):    
        colision_idx = colision_basuraN(new_x, new_y) #Colision con basura Negra
        if colision_idx is not None:
            #print("tocando basura")
            del basurasN[colision_idx]
            
            contBasuraCargadaN+=1
            #print("Negra:",contBasuraCargadaN)
            avatar=cambioImagenesBotsBolsas(playerId,contBasuraCargadaN,contBasuraCargadaV)
            

    if(colision_TachoV(new_x,new_y)):
        if(contBasuraCargadaV==1):
            contBasuraCargadaV=0
            score+=120
             #sumar Score
        elif(contBasuraCargadaV==2):
            contBasuraCargadaV=0
            score+=240
             #sumar Score
        tomarBasura=True
        if(contBasuraCargadaN!=2):
            avatar=cambioImagenesBotsBolsas(playerId,contBasuraCargadaN,contBasuraCargadaV)

    if(tomarBasura):
        colision_idx = colision_basuraV(new_x, new_y)#Colision con basura Verde
        if colision_idx is not None:
            #print("tocando basura")
            del basurasV[colision_idx]
           
            contBasuraCargadaV+=1
            #print("Verde:",contBasuraCargadaV)
            avatar=cambioImagenesBotsBolsas(playerId,contBasuraCargadaN,contBasuraCargadaV)

        
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
    
    segundos=temporizador()
    dibujarJugador() 
    dibujartachos()
    dibujarbasurasV()
    dibujarbasurasN()
    dibujararboles()
    dibujarpuntaje(playerId)
    if segundos >=60 or score==780:
        play = False
        score=score+10*(60-segundos)  
        mostrarPantallaFinal(score)
    pygame.display.update()
#=======================================================================================================================

pygame.quit()           