import pygame
import time
import random
# importing keystrokes
from pygame.locals import *
from objects.Rat import Rat
from objects.Food import Food
from objects.Poisons import Poison, Poison_2

size = 45

        
class Game:
    def __init__(self):
     # initializes pygame module
        pygame.init()

    # initializes game window (pixel dimensions) and color (.fill)
        self.surface = pygame.display.set_mode((1000, 1000))
        self.surface.fill((0, 0, 0))

    # creating the rat inside of the game by using the Rat class (expects main_screen value)
        self.rat = Rat(self.surface, 1)
        self.rat.draw_rat()

    # initializing the cheese inside of the game
        self.food = Food(self.surface)
        self.food.draw_cheese()

        self.poison = Poison(self.surface)
        self.poison.draw_poison()

        self.poison_2 = Poison_2(self.surface)
        self.poison_2.draw_poison()

    def collide(self, x1, y1, x2, y2):
        # if the coordinates of rat are within the coordinates of cheese, collision is true 
        if x1 >= x2 and x1 <= x2 + size:
            if y1 >= y2 and y1 <= y2 + size:
                return True
        return False

    def poison_collide(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + size:
            if y1 >= y2 and y1 <= y2 + size:
                return True
        return False        

    def play(self):
    # rendering rat walk
        self.rat.walk()
    # to ensure that when screen is rendered, food isn't wiped off
        self.food.draw_cheese() 

        self.poison.draw_poison()
        self.poison_2.draw_poison()

        self.keep_score()
        pygame.display.flip()
    # passing rat coordinates and cheese coordinates as x/y 1 and 2 values from collide method
        if self.collide(self.rat.rat_x[0], self.rat.rat_y[0], self.food.cheese_x, self.food.cheese_y):
            self.food.new_food()
        # when rat collides, increase length and add a block to the array
            self.rat.grow()

        if self.poison_collide(self.rat.rat_x[0], self.rat.rat_y[0], self.poison.poison_x, self.poison.poison_y):
            self.poison.new_poison()
            self.rat.shrink()

        if self.poison_collide(self.rat.rat_x[0], self.rat.rat_y[0], self.poison_2.poison_x, self.poison_2.poison_y):
            self.poison_2.new_poison()
            self.rat.shrink()


    def keep_score(self):
        font = pygame.font.SysFont('arial', 40)
        score = font.render(f"{self.rat.length -1}", True, (255, 255, 255))
        self.surface.blit(score, (950, 15))

# setting game up to run and giving keystrokes functionality        
    def run_game(self):
        running = True
        while running: 
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.rat.move_up()
                        # head_y -= 20
                        # draw_head()
                    if event.key == K_DOWN:
                        self.rat.move_down()
                        # head_y += 20
                        # draw_head()
                    if event.key == K_LEFT:
                        self.rat.move_left()
                        # head_x -= 20
                        # draw_head()
                    if event.key == K_RIGHT:
                        self.rat.move_right()
                        # head_x += 20
                        # draw_head()
                elif event.type == QUIT:
                    running = False

            self.play()