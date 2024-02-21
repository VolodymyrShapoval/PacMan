import pygame

# Розмір кубіка пакмана
CELL_SIZE = 20

# Колір пакмана
YELLOW = (255, 255, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)
        self.direction = LEFT

    def update(self, walls):
        self.rect.move_ip(self.direction[0] * CELL_SIZE, self.direction[1] * CELL_SIZE)
        if pygame.sprite.spritecollide(self, walls, False):
            self.rect.move_ip(-self.direction[0] * CELL_SIZE, -self.direction[1] * CELL_SIZE)
            self.direction = (0, 0)