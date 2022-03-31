import pygame
import random
# importing keystrokes
from pygame.locals import *

size = 45

class Poison:
    def __init__(self, main_screen):
        apple = pygame.image.load("img/poison_apple.webp").convert_alpha()
        default_apple_size = (40, 40)
        self.poison = pygame.transform.scale(apple, default_apple_size)
        self.main_screen = main_screen
        self.poison_x = random.randint(0, 20) * size
        self.poison_y = random.randint(0, 20) * size

    def draw_poison(self):
        self.main_screen.blit(self.poison, (self.poison_x, self.poison_y))
        pygame.display.flip()

    def new_poison(self):
        self.poison_x = random.randint(0, 20) * size
        self.poison_y = random.randint(0, 20) * size

class Poison_2:
    def __init__(self, main_screen):
        apple = pygame.image.load("img/poison_apple.webp").convert_alpha()
        default_apple_size = (30, 30)
        self.poison = pygame.transform.scale(apple, default_apple_size)
        self.main_screen = main_screen
        self.poison_x = random.randint(0, 20) * size
        self.poison_y = random.randint(0, 20) * size

    def draw_poison(self):
        self.main_screen.blit(self.poison, (self.poison_x, self.poison_y))
        pygame.display.flip()

    def new_poison(self):
        self.poison_x = random.randint(0, 20) * size
        self.poison_y = random.randint(0, 20) * size