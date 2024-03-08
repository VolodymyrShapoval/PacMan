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
    """
    Клас, що представляє Пакмана в грі Pacman.

    Атрибути:
    - x (int): Координата x Пакмана в пікселях.
    - y (int): Координата y Пакмана в пікселях.
    - speed (int): Швидкість руху Пакмана.
    - original_image (pygame.Surface): Оригінальне зображення Пакмана.
    - image (pygame.Surface): Зображення Пакмана, змінене відповідно до напрямку руху.
    - rect (pygame.Rect): Прямокутник, що обмежує зображення Пакмана.
    - direction (tuple): Напрямок руху Пакмана (LEFT, RIGHT, UP, DOWN).
    - isDead (bool): Прапорець, що вказує на стан Пакмана (живий чи мертвий).

    Методи:
    - __init__(self, x, y, speed): Конструктор класу. Ініціалізує об'єкт Pacman з вказаними параметрами.
    - update(self, walls): Оновлює положення Пакмана відповідно до його напрямку руху та перешкод.

    Константи:
    - CELL_SIZE (int): Розмір кубіка Пакмана.
    - YELLOW (tuple): Колір Пакмана у форматі RGB.
    - UP (tuple): Константа, що представляє напрямок вгору.
    - DOWN (tuple): Константа, що представляє напрямок вниз.
    - LEFT (tuple): Константа, що представляє напрямок вліво.
    - RIGHT (tuple): Константа, що представляє напрямок вправо.
    """

    def __init__(self, x, y, speed):
        """
        Конструктор класу Pacman.

        Параметри:
        - x (int): Координата x Пакмана в пікселях.
        - y (int): Координата y Пакмана в пікселях.
        - speed (int): Швидкість руху Пакмана.
        """
        super().__init__()
        original_image = walk_right[0]
        self.image = pygame.transform.scale(original_image, (2 * CELL_SIZE, 2 * CELL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Начальна позиція Пакмана в пікселях
        self.direction = LEFT
        self.isDead = False
        self.speed = speed  # Установлюємо швидкість Пакмана

    def update(self, walls):
        """
        Оновлює положення Пакмана відповідно до його напрямку руху та перешкод.

        Параметри:
        - walls (pygame.sprite.Group): Група перешкод.

        Змінює:
        - rect (pygame.Rect): Положення Пакмана в пікселях.
        - direction (tuple): Напрямок руху Пакмана.
        - isDead (bool): Стан Пакмана (живий чи мертвий).
        """
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)  # Ураховуємо швидкість
        if pygame.sprite.spritecollide(self, walls, False):
            self.rect.move_ip(-self.direction[0] * self.speed, -self.direction[1] * self.speed)  # Повертаємо Пакмана, якщо він стикається з перешкодою
            self.direction = (0, 0)  # Зупиняємо його рух

