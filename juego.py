import pygame
import random
from personajes import *


pygame.init()

# Inicializa la fuente
font = pygame.font.Font(None, 36)  # None para la fuente predeterminada, 36 es el tamaño de la fuente
score = 0  # Variable para el puntaje

player=Player(100,300)#Posicion inicial del Player
enemies=[]

#----Genera 5 neemigos en posiciones aleatorias-----
for _ in range(5):
    enemy=Enemy(random.randint(0,WIDTH-50),random.randint(10,500))
    enemies.append(enemy)

running=True

clock=pygame.time.Clock()

def check_collision_with_background(x, y, width, height):
    """Verifica si la posición del jugador colisiona con el color de fondo."""
    for i in range(x, x + width):
        for j in range(y, y + height):
            if background_image.get_at((i, j)) == BACKGROUND_COLOR:
                return True
    return False

while running:  # Bucle principal, se ejecuta mientras la variable 'running' sea True
    clock.tick(FPS) #detiene el juego para darle la velocidad en fotogramas deseada
    

    for event in pygame.event.get():  # Bucle que recorre todos los eventos pygame ocurridos
        if event.type == pygame.QUIT:  # Si el tipo de evento es cerrar la ventana
            running = False  # Cambia la variable 'running' a False para salir del bucle principal
    screen.blit(background_image,background_rect) #coloca y refresca el fondo

    player.draw()
    for enemy in enemies:
        enemy.update()
        enemy.draw()
        #if Enemy.colision(player,enemy):
         #   pass

#----------------------Moviendo el personaje, arriba - abajo - izquierda - derecha-------------------------------------------------
    keys = pygame.key.get_pressed()
    new_x, new_y = player.x, player.y

    if keys[pygame.K_LEFT]:
        new_x -= player.velocity
    if keys[pygame.K_RIGHT]:
        new_x += player.velocity
    if keys[pygame.K_UP]:
        new_y -= player.velocity
    if keys[pygame.K_DOWN]:
        new_y += player.velocity
        
    #----Verifica el tamaño de la imagen del personaje para las colisiones-----
    if player.x<0:
        player.x=0
    if player.x+player.width>WIDTH:
        player.x=WIDTH-player.width
    if player.y<0:
        player.y=0
    if player.y+player.height>HEIGHT:
        player.y=HEIGHT-player.height
#---verifica la posion del personaje con el fondo color negro ----
    if not check_collision_with_background(new_x, new_y, player.width, player.height):
        player.x = new_x
        player.y = new_y
    
    
    # Dibuja el puntaje
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))  # Renderiza el texto del puntaje en color blanco
    score_rect = score_text.get_rect(center=(WIDTH // 2, 20))  # Centra el texto en la parte superior
    screen.blit(score_text, score_rect)  # Dibuja el texto del puntaje en la pantalla
    
    pygame.display.flip()  # Actualiza la pantalla para mostrar los cambios
   

pygame.quit()  # Cuando se sale del bucle principal (cuando 'running' es False), se sale de pygame