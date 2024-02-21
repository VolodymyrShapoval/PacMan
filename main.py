import pygame
import sys
from wall import draw_maze
from pacman import Pacman

# Initialize Pygame
pygame.init()

# Налаштування дисплею
WIDTH, HEIGHT = 1200, 1080
CELL_SIZE = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")

# Задній фон
BLACK = (0, 0, 0)

def main():
    # Створення карти
    all_sprites, walls = draw_maze()

    #Створення пакмана    
    pacman = Pacman(3, 3)
    all_sprites.add(pacman)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pacman.direction = (-1, 0)
        elif keys[pygame.K_RIGHT]:
            pacman.direction = (1, 0)
        elif keys[pygame.K_UP]:
            pacman.direction = (0, -1)
        elif keys[pygame.K_DOWN]:
            pacman.direction = (0, 1)
        else:
            pacman.direction = (0, 0)

        pacman.update(walls)

        WIN.fill(BLACK)
        all_sprites.draw(WIN)
        pygame.display.flip()

        clock.tick(48)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()