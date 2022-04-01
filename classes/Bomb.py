import pygame
import random
# importing keystrokes
from pygame.locals import *

size = 45

class Bomb:
    def __init__(self, main_screen):
        bomb = pygame.image.load("img/pxl_bomb.png").convert_alpha()
        default_bomb_size = (size, size)
        self.bomb = pygame.transform.scale(bomb, default_bomb_size)
        self.main_screen = main_screen
        self.bomb_x = random.randint(0, 20) * size
        self.bomb_y = random.randint(0, 20) * size

    def draw_bomb(self):
        self.main_screen.blit(self.bomb, (self.bomb_x, self.bomb_y))
        pygame.display.flip()

    def new_bomb(self):
        self.bomb_x = random.randint(0, 20) * size
        self.bomb_y = random.randint(0, 20) * size