import pygame


# Задній фон
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Налаштування дисплею
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")

# Іконка
icon = pygame.image.load("img/Pac_man_logo01.png")
pygame.display.set_icon(icon)

# Звук
pygame.mixer.init()
background_sound = pygame.mixer.Sound("sounds/pacman_chomp.wav")
background_sound.set_volume(0.5)
background_sound.play(loops=-1)

