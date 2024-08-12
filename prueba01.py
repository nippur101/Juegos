import pygame
play: bool = True
playin = 1
GamePreview = 0 #Poner en Cero(0) por Defecto

clock=pygame.time.Clock()

#Player Position
posY = 550
posX = 400
Speed = 0.2

#NPC Game ONE(1)
N1_posY = 30
N1_posX = 50

#NPC Game TWO(2)
N2_posY = 30
N2_posX = 120

#NPC Game TREE(3)
N3_posY = 30
N3_posX = 190

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("OFIRCA Olimpiadas")

# Cargo los recursos
imgFondo = pygame.image.load("fondo.png")
imgUAIBOT = pygame.image.load("UAIBOT.png")
    

#personaje pa
nombrePersonaje = 'UAIBOT'
avatar = imgUAIBOT
avatar_rect = avatar.get_rect()
posY = 550
posX = 400
Speed = 0.2

#Colores
White = (255,255,255)
Black = (0, 0, 0)
Green = (0, 255, 0)
Grey = (50, 50, 50)

#Funciones
def Inicio():
    screen.blit(imgFondo, (0, 0))
    NPC1 = pygame.draw.circle(screen, Black, (N1_posX, N1_posY), 20)
    NPC2 = pygame.draw.circle(screen, Black, (N2_posX, N2_posY), 20)
    NPC3 = pygame.draw.circle(screen, Black, (N3_posX, N3_posY), 20)

def dibujarJugador():
    global avatar
    screen.blit(avatar, avatar_rect)
    
def preview1():
    pygame.draw.rect(screen, Grey, (250, 10, 400, 400)) #Contenedor.
    #pygame.draw.rect(screen, White, (200)) #Descripcion del Juego.

while play:

    clock.tick(500)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        posY += Speed
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        posY -= Speed
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        posX += Speed
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        posX -= Speed
    
    

    #Visualizacion
    if playin == 1:
        Inicio()
        
    if GamePreview == 1:
        preview1()

    dibujarJugador()    
    pygame.display.update()
            
pygame.quit()            