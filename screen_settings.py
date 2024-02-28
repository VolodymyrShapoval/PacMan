import pygame

# Налаштування дисплею
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")

icon = pygame.image.load("img/Pac_man_logo01.png")
pygame.display.set_icon(icon)

pygame.mixer.init()
background_sound = pygame.mixer.Sound("sounds/pacman_chomp.wav")
background_sound.set_volume(0.15)
background_sound.play(loops=-1)