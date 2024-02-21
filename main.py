import pygame
import sys
from wall import *
from pacman import Pacman

# Initialize Pygame
pygame.init()

# Налаштування дисплею
WIDTH, HEIGHT = 1200, 900
CELL_SIZE = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")

# Задній фон
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    # Створення карти
    all_sprites, walls, fruits = draw_maze()

    #Створення пакмана    
    pacman = Pacman(60, 60, speed=5)  # Начальная позиция пакмана в пикселях
    all_sprites.add(pacman)

    #Таблиця рахунку
    score = 0
    last_fruit_spawn_time = pygame.time.get_ticks()  # Time of the last fruit spawn
    fruit_spawn_interval = 4000  # 4 seconds

    font = pygame.font.SysFont(None, 30)

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

            # Check if it's time to spawn a new fruit
        current_time = pygame.time.get_ticks()
        if current_time - last_fruit_spawn_time >= fruit_spawn_interval:
            last_fruit_spawn_time = current_time
            if not fruits:  # Spawn a fruit only if there are none on the field
                possible_spawns = [(x, y) for y, row in enumerate(maze_map) for x, char in enumerate(row) if char == " "]
                if possible_spawns:
                    x, y = random.choice(possible_spawns)
                    fruit = Fruit(x, y)
                    all_sprites.add(fruit)
                    fruits.add(fruit)

        # Check collision with fruits
        fruit_collisions = pygame.sprite.spritecollide(pacman, fruits, True)
        score += len(fruit_collisions)

        # Update text
        score_text = font.render(f"Score: {score}", True, WHITE)

        pacman.update(walls)

        WIN.fill(BLACK)
        all_sprites.draw(WIN)
        WIN.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))
        pygame.display.flip()


        clock.tick(48)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
