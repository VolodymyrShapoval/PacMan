import math
import pygame
import random
from maze import *
from screen_settings import *
from maze import maze_map


MAX_VISION_DISTANCE = 200
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, size, image_path, pacman_rect):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = ((x + 0.5) * CELL_SIZE, (y + 0.5) * CELL_SIZE)  # Центр клетки
        self.speed = 2  # Скорость перемещения призрака
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])  # Начальное направление движения
        self.last_seen_position = None  # Последнее место, где видел Пакмана

    def update(self, walls, pacman):
        if self.can_see_pacman(pacman):
            self.move_towards_pacman(walls, pacman)
        else:
            self.random_movement(walls)


    def can_see_pacman(self, pacman):
        # Проверка, видим ли Пакмана из текущего положения призрака
        delta_x = pacman.rect.centerx - self.rect.centerx
        delta_y = pacman.rect.centery - self.rect.centery
        distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
        if distance <= MAX_VISION_DISTANCE:
            # Проверяем, есть ли препятствие между призраком и Пакманом
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
                    # Если выходит за границы лабиринта, значит не видит
                    return False
                if maze_map[tile_y][tile_x] == "x":
                    # Если на пути есть стена, значит не видит
                    return False
            # Если дошел до конечной точки и не было препятствий, значит видит
            return True
        return False

    def move_towards_pacman(self, walls, pacman):
        # Если призрак видит Пакмана, двигаемся к его текущему положению
        delta_x = pacman.rect.centerx - self.rect.centerx
        delta_y = pacman.rect.centery - self.rect.centery
        distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
        if distance != 0:
            step_x = delta_x / distance
            step_y = delta_y / distance
            self.rect.x += step_x * self.speed
            self.rect.y += step_y * self.speed

    def random_movement(self, walls):
        # Случайное движение призрака, если не видит Пакмана
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        # Проверка столкновений со стенами
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                # Отменяем движение при столкновении
                self.rect.x -= self.direction[0] * self.speed
                self.rect.y -= self.direction[1] * self.speed
                # Выбираем новое направление
                self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
