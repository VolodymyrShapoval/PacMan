import pygame
from maze import maze_map

# Розмір кубіка
CELL_SIZE = 30

# Колір кубіків
BLUE = (0, 0, 255)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)

def draw_maze():
    all_sprites = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    for y, row in enumerate(maze_map):
        for x, char in enumerate(row):
            if char == "x":
                wall = Wall(x, y)
                all_sprites.add(wall)
                walls.add(wall)

    return all_sprites, walls