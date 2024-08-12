import pygame
import random
from personajes import *

pygame.init()

# Configuración de pantalla y variables
WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)  # Suponiendo que el color de fondo del laberinto es negro
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_image = pygame.Surface((WIDTH, HEIGHT))
background_image = pygame.image.load("fondojuego.jpg").convert() # convierte la imagen para el tamaño que elegí

background_rect = background_image.get_rect()
#background_image.fill(BACKGROUND_COLOR)  # Rellenar con color de fondo

player = Player(100, 300)
enemies = []

for _ in range(5):
    enemy = Enemy(random.randint(0, WIDTH - 50), random.randint(10, 500))
    enemies.append(enemy)

running = True
clock = pygame.time.Clock()

def check_collision_with_background(x, y, width, height):
    """ Verifica si la posición del jugador colide con el color de fondo. """
    for i in range(x, x + width):
        for j in range(y, y + height):
            if background_image.get_at((i, j)) == BACKGROUND_COLOR:
                return True
    return False

while running:  # Bucle principal
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))  # Coloca y refresca el fondo

    player.draw()
    for enemy in enemies:
        enemy.update()
        enemy.draw()

    #----------------------Moviendo el personaje-------------------------------------------------
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

    # Verificar colisiones con el color de fondo
    if not check_collision_with_background(new_x, new_y, player.width, player.height):
        player.x = new_x
        player.y = new_y

    pygame.display.flip()
#ljlslnks
pygame.quit()
