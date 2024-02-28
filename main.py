import pygame
import pygame_gui
import sys
import random
from wall import *
from pacman import Pacman
from pacman_animation import *
from screen_settings import *

# Initialize Pygame
pygame.init()

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

    paused = False  # Переменная для отслеживания состояния паузы
    pause_text = font.render("Paused", True, WHITE)
    last_pause_time = 0  # Время последней паузы

    gui_manager = None  # Инициализация менеджера GUI
    volume_slider = None  # Инициализация ползунка громкости
    running = True
    player_anim_count = 0
    while running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                    if paused:
                        # Создание менеджера GUI и ползунка для громкости при паузе
                        gui_manager = pygame_gui.UIManager((WIDTH, HEIGHT))
                        volume_slider = pygame_gui.elements.UIHorizontalSlider(
                            relative_rect=pygame.Rect((200, 400), (200, 20)),
                            start_value=background_sound.get_volume(),  # Используем текущий уровень громкости как начальное значение
                            value_range=(0.0, 1.0),
                            manager=gui_manager,
                        )
                        background_sound.stop() 
                        last_pause_time = pygame.time.get_ticks()  
                    else:
                        # Очистка менеджера GUI при выходе из паузы
                        gui_manager = None
                        volume_slider = None
                        background_sound.play(loops=-1)  
                        last_fruit_spawn_time += pygame.time.get_ticks() - last_pause_time  
            
            # Обработка событий GUI
            if gui_manager:
                gui_manager.process_events(event)

        # Обновление громкости музыки в зависимости от значения ползунка
        if volume_slider:
            background_sound.set_volume(volume_slider.get_current_value())

        if not paused:  
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

            current_time = pygame.time.get_ticks()
            if current_time - last_fruit_spawn_time >= fruit_spawn_interval:
                last_fruit_spawn_time = current_time
                if not fruits:  
                    possible_spawns = [(x, y) for y, row in enumerate(maze_map) for x, char in enumerate(row) if char == " "]
                    if possible_spawns:
                        x, y = random.choice(possible_spawns)
                        fruit = Fruit(x, y)
                        all_sprites.add(fruit)
                        fruits.add(fruit)

            fruit_collisions = pygame.sprite.spritecollide(pacman, fruits, True)
            score += len(fruit_collisions)

            pacman.update(walls)

        WIN.fill(BLACK)
        all_sprites.draw(WIN)
        score_text = font.render(f"Score: {score}", True, WHITE)
        WIN.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))

        if paused:  
            WIN.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2 - pause_text.get_height() // 2))
            # Рисуем GUI только во время паузы, если он существует
            if gui_manager:
                gui_manager.update(time_delta)
                gui_manager.draw_ui(WIN)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
