import pygame
import time
import random
# importing keystrokes
from pygame.locals import *


# default block size
size = 45

class Food:
    def __init__(self, main_screen):
        mouse = pygame.image.load("img/pixel_mouse.gif").convert()
        default_mouse_size = (60, 80)
        self.image = pygame.transform.scale(mouse, default_mouse_size)
        self.main_screen = main_screen
        self.mouse_x = size * 5
        self.mouse_y = size * 5

    def draw_mouse(self):
        self.main_screen.blit(self.image, (self.mouse_x, self.mouse_y))
        pygame.display.flip()
# method to create a new mouse in a new position when previous mouse is collided with
    def new_food(self):
        self.mouse_x = random.randint(0, 20) * size
        self.mouse_y = random.randint(0, 20) * size

class Snake:
    def __init__(self, main_screen, length):
        self.main_screen = main_screen
        self.length = length

    # importing image as snake head and resizing it
        face = pygame.image.load("img/snake_head_block.png").convert()
        default_head_size = (size, size)
        self.head = pygame.transform.scale(face, default_head_size)

    # setting the default position for the head and rendering it on the surface, using array to hold subsequent blocks accumulated
        self.head_x = [size] * length
        self.head_y = [size] * length

    # creating a direction for the snake to move continuously
        self.direction = 'down'

# method to render head responsive to movement
    def draw_head(self):
        self.main_screen.fill((194, 178, 128)) 
        for i in range(self.length):
            self.main_screen.blit(self.head, (self.head_x[i], self.head_y[i]))
        pygame.display.flip()

# method to increase size of snake when a mouse is eaten (adding to end of array)
    def grow(self):
        self.length += 1
        self.head_x.append(-1)
        self.head_y.append(-1)

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
    # Move accumulated blocks to position of block in front of it (current block position is previous blocks position)
        time.sleep(0.2)
        for i in range(self.length-1, 0, -1):
            self.head_x[i] = self.head_x[i-1]
            self.head_y[i] = self.head_y[i-1]
    # move snake continuously based on direction one full block size on each movement
        if self.direction == 'up':
            self.head_y[0] -= size
        if self.direction == 'down':
            self.head_y[0] += size
        if self.direction == 'left':
            self.head_x[0] -= size
        if self.direction == 'right':
            self.head_x[0] += size
        self.draw_head()
        
class Game:
    def __init__(self):
     # initializes pygame module
        pygame.init()

    # initializes game window (pixel dimensions) and color (.fill)
        self.surface = pygame.display.set_mode((1000, 1000))
        self.surface.fill((194, 178, 128))

    # creating the snake inside of the game by using the snake class (expects main_screen value)
        self.snake = Snake(self.surface, 1)
        self.snake.draw_head()

    # initializing the mouse inside of the game
        self.food = Food(self.surface)
        self.food.draw_mouse()


    def collide(self, x1, y1, x2, y2):
        # if the coordinates of snake are within the coordinates of mouse, collision is true 
        if x1 >= x2 and x1 <= x2 + size:
            if y1 >= y2 and y1 <= y2 + size:
                return True
        return False


    def play(self):
    # rendering snake walk
        self.snake.walk()
    # to ensure that when screen is rendered, food isn't wiped off
        self.food.draw_mouse() 
    # passing snake coordinates and mouse coordinates as x/y 1 and 2 values from collide method
        if self.collide(self.snake.head_x[0], self.snake.head_y[0], self.food.mouse_x, self.food.mouse_y):
            self.food.new_food()
        # when snake collides, increase length and add a block to the array
            self.snake.grow()

# setting game up to run and giving keystrokes functionality        
    def run_game(self):
        running = True
        while running: 
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                        # head_y -= 20
                        # draw_head()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                        # head_y += 20
                        # draw_head()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                        # head_x -= 20
                        # draw_head()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        # head_x += 20
                        # draw_head()
                elif event.type == QUIT:
                    running = False

            self.play()
        

if __name__ == "__main__":
    game = Game()
    game.run_game()


