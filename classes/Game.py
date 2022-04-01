import pygame
import time
import random

# importing keystrokes
from pygame.locals import *
from classes.Rat import Rat
from classes.Food import Food
from classes.Bomb import Bomb
from classes.Cat import Cat
from classes.Poisons import Poison, Poison_2

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
        # self.rat.draw_rat()

    # initializing the cheese inside of the game
        self.food = Food(self.surface)
        # self.food.draw_cheese()

        self.cat = Cat(self.surface)
        # self.cat.draw_cat()
        
        self.poison = Poison(self.surface)
        # self.poison.draw_poison()

        self.poison_2 = Poison_2(self.surface)
        # self.poison_2.draw_poison()

        self.bomb = Bomb(self.surface)
        # self.bomb.draw_bomb()

    def collide(self, x1, y1, x2, y2):
        # if the coordinates of rat are within the coordinates of cheese, collision is true 
        if x1 >= x2 and x1 <= x2 + size:
            if y1 >= y2 and y1 <= y2 + size:
                return True
        return False


    def play(self):
    # rendering rat walk
        self.rat.walk()
    # to ensure that when screen is rendered, food isn't wiped off
        self.food.draw_cheese() 

        self.cat.move()

        self.poison.draw_poison()
        self.poison_2.draw_poison()

        self.bomb.draw_bomb()

        self.keep_score()
        pygame.display.flip()

    # passing rat coordinates and cheese coordinates as x/y 1 and 2 values from collide method
        if self.collide(self.rat.rat_x[0], self.rat.rat_y[0], self.food.cheese_x, self.food.cheese_y):
            self.food.new_food()
        # when rat collides, increase length and add a block to the array
            self.rat.grow()

    # snake colliding with self
        for i in range(3, self.rat.length):
            if self.collide(self.rat.rat_x[0], self.rat.rat_y[0], self.rat.rat_x[i], self.rat.rat_y[i]):
                # print("game_over")
                # exit(0)
                raise "Game Over"



    # POISON 1
    # handling contact for all rats before the initial rat
        if self.rat.length > 1:
            for i in range(len(self.rat.rat_x)-1 and len(self.rat.rat_y)-1):
                if self.collide(self.rat.rat_x[i], self.rat.rat_y[i], self.poison.poison_x, self.poison.poison_y):
                    self.poison.new_poison()
                    self.rat.shrink()
    # handling contact for the first rat
        elif self.rat.length == 1:
             if self.collide(self.rat.rat_x[0], self.rat.rat_y[0], self.poison.poison_x, self.poison.poison_y):
                    raise "Game Over"

    # POISON 2
        if self.rat.length > 1:
            for i in range(len(self.rat.rat_x)-1 and len(self.rat.rat_y)-1):
                if self.collide(self.rat.rat_x[i], self.rat.rat_y[i], self.poison_2.poison_x, self.poison_2.poison_y):
                    self.poison_2.new_poison()
                    self.rat.shrink()
    # handling contact for the first rat
        elif self.rat.length == 1:
             if self.collide(self.rat.rat_x[0], self.rat.rat_y[0], self.poison_2.poison_x, self.poison_2.poison_y):
                    raise "Game Over"

    # BOMB
        if self.rat.length > 1:
            for i in range(len(self.rat.rat_x)-1 and len(self.rat.rat_y)-1):
                if self.collide(self.rat.rat_x[i], self.rat.rat_y[i], self.bomb.bomb_x, self.bomb.bomb_y):
                    raise "Game Over"
    # handling contact for the first rat
        elif self.rat.length == 1:
             if self.collide(self.rat.rat_x[0], self.rat.rat_y[0], self.bomb.bomb_x, self.bomb.bomb_y):
                    raise "Game Over"

    # CAT
        if self.rat.length > 1:
            for i in range(len(self.rat.rat_x)-1 and len(self.rat.rat_y)-1):
                if self.collide(self.rat.rat_x[i], self.rat.rat_y[i], self.cat.cat_x, self.cat.cat_y):
                    raise "Game Over"
    # handling contact for the first rat
        elif self.rat.length == 1:
            if self.collide(self.rat.rat_x[0], self.rat.rat_y[0], self.cat.cat_x, self.cat.cat_y):
                raise "Game Over"

# keeping score based on the length of the array containing the rats
    def keep_score(self):
        font = pygame.font.SysFont('arial', 40)
        score = font.render(f"{self.rat.length -1}", True, (255, 255, 255))
        self.surface.blit(score, (950, 15))

    def show_game_over(self):
        self.surface.fill((100, 100, 100))
        font = pygame.font.SysFont('arial', 20)
        line1 = font.render(f"GAME OVER", True, (255, 255, 255))
        self.surface.blit(line1, (100, 150))
        line2 = font.render(f"SCORE: {self.rat.length}", True, (255, 255, 255))
        self.surface.blit(line2, (100, 250))
        line3 = font.render("press enter to play again", True, (255, 255, 255))
        self.surface.blit(line3, (100, 350))
        line4 = font.render("press esc to exit", True, (255, 255, 255))
        self.surface.blit(line4, (100, 450))
        pygame.display.flip()

    def reset_game(self):
        self.rat = Rat(self.surface, 1)
        self.food = Food(self.surface)
        self.cat = Cat(self.surface)
        self.poison = Poison(self.surface)
        self.poison_2 = Poison_2(self.surface)
        self.bomb = Bomb(self.surface)

# setting game up to run and giving keystrokes functionality        
    def run_game(self):
        running = True
        pause = False
        while running: 
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_UP:
                            self.rat.move_up()

                        if event.key == K_DOWN:
                            self.rat.move_down()

                        if event.key == K_LEFT:
                            self.rat.move_left()
                            
                        if event.key == K_RIGHT:
                            self.rat.move_right()
                       
                elif event.type == QUIT:
                    running = False


            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset_game()


            time.sleep(0.15)