import pygame
import time
from pygame.locals import *

class Game:
    def __init__(self):
     # initializes pygame module
        pygame.init()

    # initializes game window (pixel dimensions) and color (.fill)
        self.surface = pygame.display.set_mode((1000, 1000))
        self.surface.fill((194, 178, 128))

    # creating the snake inside of the game by using the snake class (expects main_screen value)
        self.snake = Snake(self.surface, 8)
        self.snake.draw_head()

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

            # method with timer to delay snake head auto move
            self.snake.walk()
            time.sleep(0.1)

size = 25

class Snake:
    def __init__(self, main_screen, length):
        self.main_screen = main_screen
        self.length = length

    # importing image as snake head and resizing it
        face = pygame.image.load("img/snake_head_block.png").convert()
        default_head_size = (25, 25)
        self.head = pygame.transform.scale(face, default_head_size)

    # setting the default position for the head and rendering it on the surface, using array to hold subsequent blocks accumulated
        self.head_x = [size] * length
        self.head_y = [size] * length

    # creating a direction for the snake to move continuously
        self.direction = 'down'

# function to render head according to keystroke
    def draw_head(self):
        self.main_screen.fill((194, 178, 128)) 
        for i in range(self.length):
            self.main_screen.blit(self.head, (self.head_x[i], self.head_y[i]))
        pygame.display.flip()

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

   
if __name__ == "__main__":
    game = Game()
    game.run_game()


