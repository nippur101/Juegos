import pygame
import time
play: bool = True
playin = 1
GamePreview = 0 #Poner en Cero(0) por Defecto

robots = [r"img\Robots\UAIBOT.png", r"img\Robots\UAIBOTA.png"]
fase = 0
robot_1 = pygame.image.load(robots[0])
robot_2 = pygame.image.load(robots[1])
jugador_imagen = robots[fase]
espera = False

#Player Position
posY = 200
posX = 100
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
pygame.display.set_caption("The World - OFIRCA Olimpiadas")

#Colores
White = (255,255,255)
Black = (0, 0, 0)
Green = (0, 255, 0)
Grey = (50, 50, 50)

#Funciones
def Inicio():
    screen.fill(Green)
    NPC1 = pygame.draw.circle(screen, Black, (N1_posX, N1_posY), 20)
    NPC2 = pygame.draw.circle(screen, Black, (N2_posX, N2_posY), 20)
    NPC3 = pygame.draw.circle(screen, Black, (N3_posX, N3_posY), 20)
    
def preview1():
    pygame.draw.rect(screen, Grey, (250, 10, 400, 400)) #Contenedor.
    #pygame.draw.rect(screen, White, (200)) #Descripcion del Juego.

while play:

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

    if keys[pygame.K_c] and espera == False:
        espera = True
        if fase < 1:
            fase += 1
        else:
            fase = 0

    #Visualizacion
    if playin == 1:
        Inicio()

    if fase == 0:
        jugador_imagen = screen.blit(robot_1, (posX, posY))
    elif fase == 1:
        jugador_imagen = screen.blit(robot_2, (posX, posY))
        
    if GamePreview == 1:
        preview1()
            
    espera = False
    pygame.display.update()
            
pygame.quit()            