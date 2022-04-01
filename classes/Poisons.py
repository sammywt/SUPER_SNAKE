import pygame
import random
# importing keystrokes
from pygame.locals import *

size = 45

class Poison:
    def __init__(self, main_screen):
        apple = pygame.image.load("img/pxl_poison_apple.png").convert_alpha()
        default_apple_size = (size, size)
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
        apple = pygame.image.load("img/pxl_poison_apple.png").convert_alpha()
        default_apple_size = (size, size)
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