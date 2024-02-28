import pygame
from maze import maze_map
import random
from fruit import *
from enemy import *

# Розмір кубіка
CELL_SIZE = 30

# Колір кубіків
BLUE = (0, 0, 255)

# Wall class
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, border_radius = 5):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        pygame.draw.rect(self.image, BLUE, (0, 0, CELL_SIZE, CELL_SIZE), border_radius=border_radius)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)

# Draw the maze and create sprites
def draw_maze():
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
                    enemy = Enemy(x, y, 15, "/img/ghosts/blinky.png")
                    all_sprites.add(enemy)
                    enemies.add(enemy)
                    if random.randint(1, 10) == 1:  # Chance of spawning a fruit
                        fruit = Fruit(x, y, CELL_SIZE)
                        all_sprites.add(fruit)
                        fruits.add(fruit)

    return all_sprites, walls, fruits, enemies
