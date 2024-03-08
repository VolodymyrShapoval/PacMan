import pygame
from screen_settings import *

class Fruit(pygame.sprite.Sprite):
    """
    Клас, що представляє фрукт в грі Pacman.

    Атрибути:
    - x (int): Координата x фрукта в логічних одиницях.
    - y (int): Координата y фрукта в логічних одиницях.
    - size (int): Розмір фрукта.

    Методи:
    - __init__(self, x, y, size): Конструктор класу. Ініціалізує об'єкт Fruit з вказаними координатами та розміром.
    """

    def __init__(self, x, y, size):
        """
        Конструктор класу Fruit.

        Параметри:
        - x (int): Координата x фрукта в логічних одиницях.
        - y (int): Координата y фрукта в логічних одиницях.
        - size (int): Розмір фрукта.
        """
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 255, 0))  # Зелений колір фрукта
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * size, y * size)

