import pygame
import sys
from wall import *
from pacman import Pacman
from pacman import walk_down, walk_left, walk_right, walk_up

# Initialize Pygame
pygame.init()

# Налаштування дисплею
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")

icon = pygame.image.load("img/Pac_man_logo01.png")
pygame.display.set_icon(icon)

background_sound = pygame.mixer.Sound("sounds/background_music.mp3")
background_sound.set_volume(0.15)
background_sound.play()

# Задній фон
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    # Створення карти
    all_sprites, walls, fruits = draw_maze()

    #Створення пакмана    
    pacman = Pacman(40, 40, speed=5)  # Начальная позиция пакмана в пикселях
    all_sprites.add(pacman)

    #Таблиця рахунку
    score = 0
    last_fruit_spawn_time = pygame.time.get_ticks()  # Time of the last fruit spawn
    fruit_spawn_interval = 4000  # 4 seconds

    font = pygame.font.SysFont(None, 30)

    clock = pygame.time.Clock()

    running = True
    player_anim_count = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            pacman.direction = (-1, 0)
            pacman.image = walk_left[player_anim_count]
        elif keys[pygame.K_RIGHT]:
            pacman.direction = (1, 0)
            pacman.image = walk_right[player_anim_count]
        elif keys[pygame.K_UP]:
            pacman.direction = (0, -1)
            pacman.image = walk_up[player_anim_count]
        elif keys[pygame.K_DOWN]:
            pacman.direction = (0, 1)
            pacman.image = walk_down[player_anim_count]
        
        if player_anim_count == 2:
            player_anim_count = 0
        else: 
            player_anim_count += 1

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


        clock.tick(15)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
