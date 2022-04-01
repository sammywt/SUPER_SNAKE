import pygame
import time
import random
# importing keystrokes
from pygame.locals import *

size = 45


class Cat:


    def __init__(self, main_screen):
        image = pygame.image.load("img/pxl_cat.png").convert_alpha()
        default_cat_size = (size, size)
        self.cat = pygame.transform.scale(image, default_cat_size)
        self.main_screen = main_screen
        self.cat_x = random.randint(0, 20) * size
        self.cat_y = random.randint(0, 20) * size
        
        # self.position = vec(self.cat_x, self.cat_y) 
        # self.velocity = vec(5, 0)
        # self.acceleration = vec(0, 0)


    def draw_cat(self):
        self.main_screen.blit(self.cat, (self.cat_x, self.cat_y))
        # pygame.display.flip()


    def move(self):
        self.cat_x += random.randint(-50, 50)
        self.cat_y += random.randint(-50, 50)
        if self.cat_x >= 950:
            self.cat_x -= 50
        elif self.cat_x <= 50:
            self.cat_x += 50

        if self.cat_y >= 950:
            self.cat_y -= 50
        elif self.cat_y <= 50:
            self.cat_y += 50


        self.draw_cat()

    
            