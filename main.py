import pygame
from pygame.locals import *

class Game:
    def __init__(self):
     # initializes pygame module
        pygame.init()
    # initializes game window (pixel dimensions) and color (.fill)
        self.surface = pygame.display.set_mode((1000, 1000))
        self.surface.fill((194, 178, 128))
    # creating the snake inside of the game by using the snake class (expects main_screen value)
        self.snake = Snake(self.surface)
        self.snake.draw_head()
    def run_game(self):
# setting game up to run and giving keystrokes functionality
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


class Snake:
    def __init__(self, main_screen):
        self.main_screen = main_screen
    # importing image as snake head and resizing it
        face = pygame.image.load("img/snake_head_block.png").convert()
        default_head_size = (25, 25)
        self.head = pygame.transform.scale(face, default_head_size)
    # setting the default position for the head and rendering it on the surface
        self.head_x = 500
        self.head_y = 500
# function to render head according to keystroke
    def draw_head(self):
        self.main_screen.fill((194, 178, 128)) 
        self.main_screen.blit(self.head, (self.head_x, self.head_y))
        pygame.display.flip()
# functions to move head on keystrokes
    def move_left(self):
        self.head_x -= 20
        self.draw_head()

    def move_right(self):
        self.head_x += 20
        self.draw_head()

    def move_up(self):
        self.head_y -= 20
        self.draw_head()

    def move_down(self):
        self.head_y += 20
        self.draw_head()

   
if __name__ == "__main__":
    game = Game()
    game.run_game()


