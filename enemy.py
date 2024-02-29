import pygame
import random
from screen_settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, size, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)
        self.speed = 2  # Скорость перемещения призрака
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])  # Начальное направление движения

    def update(self, walls):
        # Перемещаем призрака в его текущем направлении
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

        # Проверяем столкновения с стенами и меняем направление, если столкнулись
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                # Отменяем последнее перемещение
                self.rect.x -= self.direction[0] * self.speed
                self.rect.y -= self.direction[1] * self.speed
                # Выбираем новое случайное направление
                self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

        # Проверяем, чтобы призрак оставался в пределах экрана
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))
