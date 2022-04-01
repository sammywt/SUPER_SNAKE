import pygame
import time
import random
# importing keystrokes
from pygame.locals import *


size = 45

class Food:
    def __init__(self, main_screen):
        cheese = pygame.image.load("img/pxl_cheese.png").convert_alpha()
        default_cheese_size = (size, size)
        self.image = pygame.transform.scale(cheese, default_cheese_size)
        self.main_screen = main_screen
        self.cheese_x = random.randint(0, 20) * size
        self.cheese_y = random.randint(0, 20) * size

    def draw_cheese(self):
        self.main_screen.blit(self.image, (self.cheese_x, self.cheese_y))
        pygame.display.flip()
# method to create new cheese in a new position when previous cheese is collided with
    def new_food(self):
        self.cheese_x = random.randint(0, 20) * size
        self.cheese_y = random.randint(0, 20) * size