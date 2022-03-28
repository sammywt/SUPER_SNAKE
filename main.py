from glob import escape
import pygame
# import all possible variables from pygame.locals (this is where keystrokes are coming from) SEE DETAILS @ https://www.pygame.org/docs/ref/locals.html
from pygame.locals import *

# initializes pygame module
if __name__ == "__main__":
    pygame.init()
    # initializes game window (pixel dimensions)
    surface = pygame.display.set_mode((1000, 1000))
    #fill the background with an RGB color (sand)
    surface.fill((194, 178, 128))
    # importing the image to use for the snake block with pygame image model and setting it to block variable
    block = pygame.image.load("img/snake_head_block.png").convert()

    default_head_size = (25, 25)

    block = pygame.transform.scale(block, default_head_size)
    # draw the block variable on the background(surface) in specified position
    surface.blit(block, (500, 500))
    # update the screen with whatever properties you defined (fill screen color)
    pygame.display.flip()

    # event loop listening for escape to close window (while loop)
    running = True
        # infinite loop, on certain keystrokes, cancel/exit the loop
    while running: 
        # event is built in to pygame- for the event in this function do something
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # if the escape key is pressed, stop running the game
                    running = False
            # if the user selects quit, stop running the game
            elif event.type == QUIT:
                running = False
