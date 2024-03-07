import math
import pygame
import random
from screen_settings import *
from maze import maze_map


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, size, image_path, pacman_rect):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * CELL_SIZE, y * CELL_SIZE)
        self.speed = 1  # Швидкість переміщення призрака
        self.target_direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])  # Початковий напрямок руху
        self.direction = [0, 0]  # Поточний напрямок руху
        self.pacman_rect = pacman_rect  # Додаємо прямокутник пакмана

    def get_cells(self,x, y):
        cells=[]
        pacman_size=10
        ind_X = x//CELL_SIZE # 1.5 => int(1.5) => 1
        ind_Y = y//CELL_SIZE # 2.5 => int(2.5) => 2
        cells.append((ind_Y,ind_X))
        if len(maze_map)*CELL_SIZE%(x+pacman_size)>0:
            cells.append((ind_Y+1,ind_X))
        if len(maze_map)*CELL_SIZE%(y+pacman_size)>0:
            cells.append((ind_Y,ind_X+1))
        return cells

    def check_walls(self,x,y):
        pacman_cells = self.get_cells(x,y)
        enemy_cells = self.get_cells(self.rect.topleft[0],self.rect.topleft[1])
        if len(enemy_cells)>1:
            return True, (0,0)
        isRow=False
        isColumn=False
        for pacman_cell in pacman_cells:
            if pacman_cell[0]==(enemy_cells[0])[0]:
                isRow=True
            elif pacman_cell[1]==(enemy_cells[0])[1]:
                isColumn=True
        if isRow:
            row=(enemy_cells[0])[0]
            if ((pacman_cells[0])[1]-(enemy_cells[0])[1]>1):
                return False, (0,0)
            for i in maze_map[row]:
                if i=='x':
                   return True, (0,0)
            freeDirection=(1,0)
        elif isColumn:
            column=(enemy_cells[0])[1]
            if ((pacman_cells[0])[0]-(enemy_cells[0])[0]>1):
                return False, (0,0)
            for i in maze_map:
                if i[column]=='x':
                   return True, (0,0)
            freeDirection=(0,1)
        return False, freeDirection
            
    def update(self, walls, pacman_rect, time_delta):
        VISIBLE_SIZE = 100
        direction_vector = [pacman_rect.x - self.rect.x, pacman_rect.y - self.rect.y]
        length = math.sqrt(direction_vector[0] ** 2 + direction_vector[1] ** 2)
        isWalls,freeDirection=self.check_walls(self.rect.topleft[0],self.rect.topleft[1])
        if isWalls:
            direction=[0,0]
        else:
            if freeDirection==(1,0):
                self.direction=[direction_vector[0]/abs(direction_vector[0]),0]
            else:
                self.direction=[0,direction_vector[1]/abs(direction_vector[1])]
        self.rect.x += (self.direction[0] * self.speed)
        self.rect.y += (self.direction[1] * self.speed)
        #self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)


        # if length != 0:
        #     normalized_direction = (direction_vector[0] / length, direction_vector[1] / length)
        # else:
        #     normalized_direction = (0, 0)

        # self.direction = direction_vector

        # # Рухаємо ворога у визначений напрямок з врахуванням часового кроку
        # self.rect.x += (self.direction[0] * self.speed)
        # self.rect.y += (self.direction[1] * self.speed)

        # # Перевірка столкновення із стінами
        # for wall in walls:
        #     if self.rect.colliderect(wall.rect):
        #         self.rect.x += (-self.direction[0] * self.speed * time_delta)
        #         self.rect.y += (-self.direction[1] * self.speed * time_delta)
        
        
        # print(f"Direction: {self.direction}, Position: ({self.rect.x}, {self.rect.y})")