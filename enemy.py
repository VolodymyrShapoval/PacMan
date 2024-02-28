import pygame
from pacman_animation import *
import random
from maze import *

# Розмір кубіка
CELL_SIZE = 10

# Колір
YELLOW = (255, 255, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, size, speed, img):
        super().__init__()
        original_image = pygame.image.load(img) # Set the appropriate image for the enemy (e.g., from your animation)
        self.image = pygame.transform.scale(original_image, (2 * CELL_SIZE, 2 * CELL_SIZE))
        self.rect = self.image.get_rect()
        # flag = False
        # while(flag == False):
        #     x = random.randint(0*size, len(maze_map)-1*size)
        #     y = random.randint(0*size, len(maze_map)-1*size)
        #     if(maze_map[x][y] != 'x'):
        self.rect.topleft = (x * size, y * size)  # Initial position of the enemy in pixels
                # flag = True        
        self.direction = LEFT  # Initial direction of the enemy
        self.speed = speed  # Set the speed of the enemy

    def update(self, walls):
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)  # Consider the speed
        if pygame.sprite.spritecollide(self, walls, False):
            self.rect.move_ip(-self.direction[0] * self.speed, -self.direction[1] * self.speed)  # Move the enemy back if it collides with an obstacle
            self.direction = (0, 0)  # Stop its movement
