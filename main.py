import pygame
import sys
from wall import draw_maze

# Initialize Pygame
pygame.init()

# Налаштування дисплею
WIDTH, HEIGHT = 1000, 1000
CELL_SIZE = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")

# Задній фон
BLACK = (0, 0, 0)

def main():
    # Створення карти
    all_sprites = draw_maze()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        WIN.fill(BLACK)
        all_sprites.draw(WIN)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
