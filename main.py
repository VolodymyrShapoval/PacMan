import pygame
import pygame_gui
import sys
import random
from configuration import Configuration
from wall import *
from pacman import Pacman
from pacman_animation import *
from screen_settings import *
from enemies_types import *

# Змінні для встановлення кольорів
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Рівень складності
selected_difficulty = None
enemies_count = None

# Глобальні змінні для гри
WIN = None  # Вікно гри
clock = None  # Глобальний об'єкт для відстеження часу
background_sound = None  # Об'єкт для відтворення фонової музики

# Ініціалізація гри
def initialize():
    global WIN, clock, background_sound
    
    pygame.init()
    
    # Налаштування дисплею
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pacman")

    icon = pygame.image.load("img/Pac_man_logo01.png")
    pygame.display.set_icon(icon)

    pygame.mixer.init()
    background_sound = pygame.mixer.Sound("sounds/background_music.mp3")
    background_sound.set_volume(0.5)
    background_sound.play(loops=-1)

    clock = pygame.time.Clock()

# Вибір рівня складності
def choose_difficulty_level():
    global enemies_count

    config = Configuration()
    config.set_difficulty()
    selected_difficulty = config.get_difficulty()

    if selected_difficulty == "easy": enemies_count = 5
    elif selected_difficulty == "medium": enemies_count = 8
    elif selected_difficulty == "hard": enemies_count = 12
    print(f"Обраний рівень складності: {selected_difficulty}")
    return selected_difficulty

# Основна функція гри
def main():
    global enemies_count, WIN, clock, background_sound, selected_difficulty
    
    initialize()

    # Создание карты
    all_sprites, walls, fruits, enemies = draw_maze()

    # Визначення кількості ворогів в залежності від рівня складності
    if selected_difficulty == "easy": enemies_count = 5
    elif selected_difficulty == "medium": enemies_count = 8
    elif selected_difficulty == "hard": enemies_count = 12

    # Создание Пакмана
    pacman = Pacman(40, 40, speed=5)
    all_sprites.add(pacman)

    # Таблица счета
    score = 0
    last_fruit_spawn_time = pygame.time.get_ticks()  # Время последнего появления фрукта
    fruit_spawn_interval = 4000  # 4 секунды
    last_enemy_spawn_time = pygame.time.get_ticks()
    enemy_spawn_interval = 1000  # 10 секунд

    font = pygame.font.SysFont(None, 30)

    clock = pygame.time.Clock()

    paused = False  # Переменная для отслеживания состояния паузы
    pause_text = font.render("Paused", True, WHITE)
    last_pause_time = 0  # Время последней паузы

    gui_manager = None  # Ініціалізація менеджера GUI
    volume_slider = None  # Ініціалізація слайдера гучності
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
                        # Создание менеджера GUI и слайдера громкости при паузе
                        gui_manager = pygame_gui.UIManager((WIDTH, HEIGHT))
                        volume_slider = pygame_gui.elements.UIHorizontalSlider(
                            relative_rect=pygame.Rect((200, 400), (200, 20)),
                            start_value=background_sound.get_volume(),
                            value_range=(0.0, 1.0),
                            manager=gui_manager,
                        )
                        background_sound.stop() 
                        last_pause_time = pygame.time.get_ticks()
                    else:
                        # Очистка менеджера GUI при виході з паузи
                        gui_manager = None
                        volume_slider = None
                        background_sound.play(loops=-1)
                        last_fruit_spawn_time += pygame.time.get_ticks() - last_pause_time

            # Обробка подій GUI
            if gui_manager:
                gui_manager.process_events(event)

        # Оновлення гучності музики в залежності від значення слайдера
        if volume_slider:
            background_sound.set_volume(volume_slider.get_current_value())

        if not paused:
            # Перевірка зіткнення Пакмана з ворогами
            if pygame.sprite.spritecollideany(pacman, enemies):
                dead = font.render("Game Over", True, WHITE)
                WIN.blit(dead, (WIDTH // 2 - dead.get_width() // 2, HEIGHT // 2 - dead.get_height() // 2))
                print("Game Over! You lost!")
                all_sprites.remove(pacman)
                # Скидання рахунку
                score = 0
                # Видалення всіх фруктів
                fruits.empty()
                # Видалення всіх ворогів
                enemies.empty()
                # Створення карти знову
                all_sprites, walls, fruits, enemies = draw_maze()
                all_sprites.add(pacman)
                # Переміщуємо Пакмана в початкове положення
                pacman.rect.topleft = (40, 40)

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
                        fruit = Fruit(x, y, CELL_SIZE)
                        all_sprites.add(fruit)
                        fruits.add(fruit)

            if current_time - last_enemy_spawn_time >= enemy_spawn_interval:
                last_enemy_spawn_time = current_time
                if len(enemies) < enemies_count:
                    possible_spawns = [(x, y) for y, row in enumerate(maze_map) for x, char in enumerate(row) if char == " "]
                    if possible_spawns:
                        x, y = random.choice(possible_spawns)
                        enemy = Enemy(x, y, 15, enemies_types[random.randint(0, len(enemies_types)-1)], pacman.rect)
                        all_sprites.add(enemy)
                        enemies.add(enemy)

            fruit_collisions = pygame.sprite.spritecollide(pacman, fruits, True)
            score += len(fruit_collisions)

            pacman.update(walls)
            
            # Оновлення положення ворогів і передача позиції Пакмана для визначення видимості
            for enemy in enemies:
                enemy.update(walls, pacman)

        WIN.fill(BLACK)
        all_sprites.draw(WIN)
        score_text = font.render(f"Score: {score}", True, WHITE)
        WIN.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))

        if paused:
            WIN.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2 - pause_text.get_height() // 2))
            # Рисуємо GUI тільки під час паузи, якщо він існує
            if gui_manager:
                gui_manager.update(time_delta)
                gui_manager.draw_ui(WIN)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    choose_difficulty_level()
    main()

# Завершення документації
