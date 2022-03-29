import pygame
import time
import random
# importing keystrokes
from pygame.locals import *


# default block size
size = 45

class Food:
    def __init__(self, main_screen):
        cheese = pygame.image.load("img/chez.png").convert_alpha()
        default_cheese_size = (40, 40)
        self.image = pygame.transform.scale(cheese, default_cheese_size)
        self.main_screen = main_screen
        self.cheese_x = size * 3
        self.cheese_y = size * 3

    def draw_cheese(self):
        self.main_screen.blit(self.image, (self.cheese_x, self.cheese_y))
        pygame.display.flip()
# method to create new cheese in a new position when previous cheese is collided with
    def new_food(self):
        self.cheese_x = random.randint(0, 20) * size
        self.cheese_y = random.randint(0, 20) * size

class Poison:
    def __init__(self, main_screen):
        apple = pygame.image.load("img/poison_apple.webp").convert_alpha()
        default_apple_size = (40, 40)
        self.poison = pygame.transform.scale(apple, default_apple_size)
        self.main_screen = main_screen
        self.poison_x = size * 10
        self.poison_y = size * 10

    def draw_poison(self):
        self.main_screen.blit(self.poison, (self.poison_x, self.poison_y))
        pygame.display.flip()


class Rat:
    def __init__(self, main_screen, length):
        self.main_screen = main_screen
        self.length = length

    # importing image and resizing it
        image = pygame.image.load("img/pixel_mouse.gif").convert_alpha()
        default_image_size = (size*2, size*2)
        self.rat = pygame.transform.scale(image, default_image_size)

    # setting the default position for the rat and rendering it on the surface, using array to hold subsequent blocks accumulated
        self.rat_x = [size] * length
        self.rat_y = [size] * length

    # creating a direction for the rat to move continuously
        self.direction = 'down'

# method to render rat responsive to movement
    def draw_rat(self):
        self.main_screen.fill((0, 0, 205)) 
        for i in range(self.length):
            self.main_screen.blit(self.rat, (self.rat_x[i], self.rat_y[i]))
        pygame.display.flip()

# method to increase number of rats when cheese is eaten (adding to end of array)
    def grow(self):
        self.length += 1
        self.rat_x.append(-1)
        self.rat_y.append(-1)

# functions to move i a direction based on keystrokes
    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'


    def walk(self):
    # Move accumulated rats to position in front of it (current blocks old position is previous blocks new position)
        time.sleep(0.2)
        for i in range(self.length-1, 0, -1):
            self.rat_x[i] = self.rat_x[i-1]
            self.rat_y[i] = self.rat_y[i-1]
    # move rat continuously based on direction one full block size on each movement
        if self.direction == 'up':
            self.rat_y[0] -= size
        if self.direction == 'down':
            self.rat_y[0] += size
        if self.direction == 'left':
            self.rat_x[0] -= size
        if self.direction == 'right':
            self.rat_x[0] += size
        self.draw_rat()
        
class Game:
    def __init__(self):
     # initializes pygame module
        pygame.init()

    # initializes game window (pixel dimensions) and color (.fill)
        self.surface = pygame.display.set_mode((1000, 1000))
        self.surface.fill((0, 0, 205))

    # creating the rat inside of the game by using the Rat class (expects main_screen value)
        self.rat = Rat(self.surface, 1)
        self.rat.draw_rat()

    # initializing the cheese inside of the game
        self.food = Food(self.surface)
        self.food.draw_cheese()

        self.poison = Poison(self.surface)
        self.poison.draw_poison()

    def collide(self, x1, y1, x2, y2):
        # if the coordinates of rat are within the coordinates of cheese, collision is true 
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False


    def play(self):
    # rendering rat walk
        self.rat.walk()
    # to ensure that when screen is rendered, food isn't wiped off
        self.food.draw_cheese() 

        self.poison.draw_poison()

        self.keep_score()
        pygame.display.flip()
    # passing rat coordinates and cheese coordinates as x/y 1 and 2 values from collide method
        if self.collide(self.rat.rat_x[0], self.rat.rat_y[0], self.food.cheese_x, self.food.cheese_y):
            self.food.new_food()
        # when rat collides, increase length and add a block to the array
            self.rat.grow()


    def keep_score(self):
        font = pygame.font.SysFont('arial', 40)
        score = font.render(f"{self.rat.length -1}", True, (0, 0, 0))
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
        

if __name__ == "__main__":
    game = Game()
    game.run_game()


