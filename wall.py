import pygame


maze_map = [
    "xxxxxxxxxxxxxxxxxxxx",
    "x                  x",
    "x  xxxxx  xxxxx  xxx",
    "x  xxxxx  xxxxx  xxx",
    "x                  x",
    "x  xxxxx  xxxxx  xxx",
    "x  xxxxx  xxxxx  xxx",
    "x  xxxxx  xxxxx  xxx",
    "x  xxxxx  xxxxx  xxx",
    "x  xxxxx  xxxxx  xxx",
    "x                  x",
    "x     xxxxxxxxx    x",
    "x     xxxxxxxxx    x",
    "x                  x",
    "x     xxxxxxxxx    x",
    "x     xxxxxxxxx    x",
    "x                  x",
    "x xxxxx x xxxxx xxxx",
    "x xxxxx x xxxxx xxxx",
    "x                  x",
    "xxxxxxxxxxxxxxxxxxxx"
]

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


    for y, row in enumerate(maze_map):
        for x, char in enumerate(row):
            if char == "x":
                wall = Wall(x, y)
                all_sprites.add(wall)


    return all_sprites