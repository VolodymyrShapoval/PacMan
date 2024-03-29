import pygame
from maze import maze_map
import random
from fruit import *
from screen_settings import *
from enemy import *

CELL_SIZE = 30

# Колір кубіків
BLUE = (0, 0, 255)

class Wall(pygame.sprite.Sprite):
    """
    Клас, що представляє стіну в грі Pacman.

    Атрибути:
    - x (int): Координата x лівого верхнього кута стіни в клітинах.
    - y (int): Координата y лівого верхнього кута стіни в клітинах.
    - border_radius (int): Радіус закруглення кутів стіни.
    - image (pygame.Surface): Зображення стіни.
    - rect (pygame.Rect): Прямокутник, що обмежує зображення стіни.

    Методи:
    - __init__(self, x, y, border_radius=5): Конструктор класу. Ініціалізує об'єкт Wall з вказаними параметрами.
    """

    def __init__(self, x, y, border_radius=5):
        """
        Конструктор класу Wall.

        Параметри:
        - x (int): Координата x лівого верхнього кута стіни в клітинах.
        - y (int): Координата y лівого верхнього кута стіни в клітинах.
        - border_radius (int): Радіус закруглення кутів стіни (за замовчуванням 5).
        """
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        pygame.draw.rect(self.image, BLUE, (0, 0, CELL_SIZE, CELL_SIZE), border_radius=border_radius)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)

def draw_maze():
    """
    Функція для створення лабіринту та створення груп спрайтів.

    Повертає:
    - all_sprites (pygame.sprite.Group): Група всіх спрайтів.
    - walls (pygame.sprite.Group): Група спрайтів стін.
    - fruits (pygame.sprite.Group): Група спрайтів фруктів.
    - enemies (pygame.sprite.Group): Група спрайтів ворогів.
    """
    all_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    fruits = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    for y, row in enumerate(maze_map):
        for x, char in enumerate(row):
            if char == "x":
                wall = Wall(x, y)
                all_sprites.add(wall)
                walls.add(wall)
            elif char == " ":
                possible_spawn = True
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if maze_map[y + dy][x + dx] == "x":
                            possible_spawn = False
                            break
                    if not possible_spawn:
                        break
                if possible_spawn:
                    enemy = Enemy(x, y, 15, "/img/ghosts/blinky.png")  # Шлях до зображення призрака
                    all_sprites.add(enemy)
                    enemies.add(enemy)
                    if random.randint(1, 10) == 1:  # Шанс появлення фрукта
                        fruit = Fruit(x, y, CELL_SIZE)
                        all_sprites.add(fruit)
                        fruits.add(fruit)

    return all_sprites, walls, fruits, enemies

