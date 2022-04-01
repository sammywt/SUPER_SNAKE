import pygame
import time
import random
# importing keystrokes
from pygame.locals import *

size = 45
vec = pygame.Vector2()
direction = 1
speed_x = 2
speed_y = 3

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
        pygame.display.flip()


    def move(self):
        self.cat_x += size
        self.cat_y += size
        self.draw_cat()

    # def walk(self):


        
    
    #     run = True
    #     while run:

    #         # starting position already set
    #         # generate random int, either 1 or 2
    #         # if 1, move a size down
    #         # if 2, move a size up
    #         # if a 3, move a size left
    #         # if a 4, move a size right
    #         # re render image in new position
    #         # if cat_x or cat_y exceed boundary, set values to new position on screen
    #         # if game over, exit loop
    #         # call loop again
           
    #         direction = random.randint(0, 4)
    #         if direction == 1:
    #             cat_y += size
    #         elif direction == 2: 
    #             cat_y -= size
    #         elif direction == 3:
    #             cat_x -= size
    #         elif direction == 4:
    #             cat_x += size
            

    #         pygame.display.flip()
    #         self.walk()
        

            
            
            