import math
import pygame
import random
from maze import *
from screen_settings import *
from maze import maze_map

MAX_VISION_DISTANCE = 200

class Enemy(pygame.sprite.Sprite):
    """
    Клас, що представляє ворога (призрака) в грі Pacman.

    Атрибути:
    - x (int): Координата x ворога в логічних одиницях.
    - y (int): Координата y ворога в логічних одиницях.
    - size (int): Розмір ворога.
    - image_path (str): Шлях до зображення ворога.
    - pacman_rect (pygame.Rect): Прямокутник, що визначає положення Пакмана.

    Методи:
    - __init__(self, x, y, size, image_path, pacman_rect): Конструктор класу. Ініціалізує об'єкт Enemy з вказаними параметрами.
    - update(self, walls, pacman): Оновлює положення ворога залежно від руху Пакмана та стану лабіринту.
    - can_see_pacman(self, pacman): Перевіряє, чи видно ворогові Пакмана з його поточного положення.
    - move_towards_pacman(self, walls, pacman): Рухає ворога в напрямку Пакмана, якщо той видимий.
    - random_movement(self, walls): Здійснює випадковий рух ворога, якщо Пакман невидимий.
    """

    def __init__(self, x, y, size, image_path, pacman_rect):
        """
        Конструктор класу Enemy.

        Параметри:
        - x (int): Координата x ворога в логічних одиницях.
        - y (int): Координата y ворога в логічних одиницях.
        - size (int): Розмір ворога.
        - image_path (str): Шлях до зображення ворога.
        - pacman_rect (pygame.Rect): Прямокутник, що визначає положення Пакмана.
        """
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = ((x + 0.5) * CELL_SIZE, (y + 0.5) * CELL_SIZE)  # Центр клітинки
        self.speed = 2  # Швидкість руху ворога
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])  # Початковий напрямок руху
        self.last_seen_position = None  # Останнє місце, де був бачений Пакман

    def update(self, walls, pacman):
        """
        Оновлює положення ворога залежно від руху Пакмана та стану лабіринту.

        Параметри:
        - walls (pygame.sprite.Group): Група стін лабіринту.
        - pacman (Pacman): Об'єкт Пакмана.
        """
        if self.can_see_pacman(pacman):
            self.move_towards_pacman(walls, pacman)
        else:
            self.random_movement(walls)

    def can_see_pacman(self, pacman):
        """
        Перевіряє, чи видно ворогові Пакмана з його поточного положення.

        Параметри:
        - pacman (Pacman): Об'єкт Пакмана.

        Повертає:
        - bool: Чи видно ворогові Пакмана.
        """
        delta_x = pacman.rect.centerx - self.rect.centerx
        delta_y = pacman.rect.centery - self.rect.centery
        distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
        if distance <= MAX_VISION_DISTANCE:
            step_x = delta_x / distance
            step_y = delta_y / distance
            x = self.rect.centerx
            y = self.rect.centery
            for _ in range(int(distance)):
                x += step_x
                y += step_y
                tile_x = int(x / CELL_SIZE)
                tile_y = int(y / CELL_SIZE)
                if (tile_x < 0 or tile_x >= len(maze_map[0])) or (tile_y < 0 or tile_y >= len(maze_map)):
                    return False
                if maze_map[tile_y][tile_x] == "x":
                    return False
            return True
        return False

    def move_towards_pacman(self, walls, pacman):
        """
        Рухає ворога в напрямку Пакмана, якщо той видимий.

        Параметри:
        - walls (pygame.sprite.Group): Група стін лабіринту.
        - pacman (Pacman): Об'єкт Пакмана.
        """
        delta_x = pacman.rect.centerx - self.rect.centerx
        delta_y = pacman.rect.centery - self.rect.centery
        distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
        if distance != 0:
            step_x = delta_x / distance
            step_y = delta_y / distance
            self.rect.x += step_x * self.speed
            self.rect.y += step_y * self.speed

    def random_movement(self, walls):
        """
        Здійснює випадковий рух ворога, якщо Пакман невидимий.

        Параметри:
        - walls (pygame.sprite.Group): Група стін лабіринту.
        """
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                self.rect.x -= self.direction[0] * self.speed
                self.rect.y -= self.direction[1] * self.speed
                self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

