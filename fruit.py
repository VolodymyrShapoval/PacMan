import pygame
from wall import *

class Fruit(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * size, y * size)