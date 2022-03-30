import pygame
import time
import random
# importing keystrokes
from pygame.locals import *

# default block size
size = 45

class Rat:
    def __init__(self, main_screen, length):
        self.main_screen = main_screen
        self.length = length

    # importing image and resizing it
        self.image = pygame.image.load("img/pixel_mouse.gif").convert_alpha()
        self.default_image_size = (size*2, size*2)
        

    # setting the default position for the rat and rendering it on the surface, using array to hold subsequent blocks accumulated
        self.rat_x = [size] * length
        self.rat_y = [size] * length

    # creating a direction for the rat to move continuously
        self.direction = 'down'

        self.angle = 0
        
# method to render rat responsive to movement
    def draw_rat(self):
        self.rat = pygame.transform.scale(self.image, self.default_image_size)
        self.rat = pygame.transform.rotate(self.rat, self.angle)
        self.main_screen.fill((0, 0, 0)) 
        
        if self.direction == 'up':
            self.rat = pygame.transform.flip(self.rat, False, False)
        if self.direction == 'down':
            self.rat = pygame.transform.flip(self.rat, False, False)
        if self.direction == 'left':
            self.rat = pygame.transform.flip(self.rat, True, False)
        if self.direction == 'right':
            self.rat = pygame.transform.flip(self.rat, False, False)

        for i in range(self.length):
            self.main_screen.blit(self.rat, (self.rat_x[i], self.rat_y[i]))
        pygame.display.flip()

# method to increase number of rats when cheese is eaten (adding to end of array)
    def grow(self):
        self.length += 1
        self.rat_x.append(-1)
        self.rat_y.append(-1)

    def shrink(self):
        self.length -= 1
        self.rat_x.pop()
        self.rat_y.pop()

# functions to move i a direction based on keystrokes
    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'
        # new_rat = pygame.transform.rotate(self.rat, 90)
        # self.main_screen.blit(new_rat, (self.rat_x, self.rat_y))
        # pygame.display.flip()
    def move_down(self):
        self.direction = 'down'


    def walk(self):
    # Move accumulated rats to position in front of it (current blocks old position is previous blocks new position)
        # rotated_img = pygame.transform.rotate(self.rat, 90)
        time.sleep(0.2)
        for i in range(self.length-1, 0, -1):
            self.rat_x[i] = self.rat_x[i-1]
            self.rat_y[i] = self.rat_y[i-1]
    # move rat continuously based on direction one full block size on each movement
        if self.direction == 'up':
            self.rat_y[0] -= size
            self.angle = 90
        if self.direction == 'down':
            self.rat_y[0] += size
            self.angle = 270
        if self.direction == 'left':
            self.rat_x[0] -= size
            self.angle = 0
        if self.direction == 'right':
            self.rat_x[0] += size
            self.angle = 0
        self.draw_rat()
        