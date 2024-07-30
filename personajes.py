import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Mi primer Juego")

BACKGROUND_COLOR = (0, 0, 0)  # Suponiendo que el color de fondo del laberinto es negro
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_image = pygame.Surface((WIDTH, HEIGHT))
background_image = pygame.image.load("fondojuego.jpg").convert() # convierte la imagen para el tamaño que elegí

background_rect = background_image.get_rect()

# clase para personajes
class Player:
    def __init__(self, x, y):  # Constructor
        self.x = x
        self.y = y
        self.width = 44
        self.height = 80
        self.velocity = 5
        self.image = pygame.image.load("jugador.png")  # Ruta corregida
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Enemy:
    def __init__(self, x, y):  # Constructor
        self.x = x
        self.y = y
        self.width = 80
        self.height = 80
        self.velocity = 2
        self.direction = 1
        self.image = self.ontener_imagen_enemigo()

    def update(self):
        self.x += self.velocity * self.direction
        if self.x < 0 or self.x + self.width > WIDTH:
            self.direction *= -1

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def ontener_imagen_enemigo(self):
        enemy_images = [
            pygame.image.load("perso02.png"),  # Rutas corregidas
            pygame.image.load("perso03.png"),
            pygame.image.load("perso05.png"),
            pygame.image.load("perso06.png")
        ]
        return random.choice(enemy_images)
    #Funcion que verifica que las imagenes se toquen, si se toca devuelve true sino false
    def check_collision_with_background(x, y, width, height):
        for i in range(x, x + width):
            for j in range(y, y + height):
                if background_image.get_at((i, j)) == BACKGROUND_COLOR:
                    return True
        return False
    
    def colision(obj1,obj2):
        if obj1.x<obj2.x+obj2.width and obj1.x+obj1.width>obj2.x and obj1.y<obj2.y+obj2.height and obj1.y +obj1.height>obj2.y:
            return True
        else:
            return False
    

