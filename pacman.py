import pygame
from pacman_animation import *

# Розмір кубіка пакмана
CELL_SIZE = 10

# Колір пакмана
YELLOW = (255, 255, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        original_image = walk_right[0]
        self.image = pygame.transform.scale(original_image, (2 * CELL_SIZE, 2 * CELL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Начальная позиция пакмана в пикселях
        self.direction = LEFT
        self.dead = False
        self.speed = speed  # Устанавливаем скорость пакмана

    def update(self, walls):
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)  # Учитываем скорость
        if pygame.sprite.spritecollide(self, walls, False):
            self.rect.move_ip(-self.direction[0] * self.speed, -self.direction[1] * self.speed)  # Возвращаем пакмана, если он столкнулся с препятствием
            self.direction = (0, 0)  # Останавливаем его движение