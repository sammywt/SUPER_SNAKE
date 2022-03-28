import pygame
from pygame.locals import *


def draw_head():
        surface.fill((194, 178, 128))
        surface.blit(head, (head_x, head_y))
        pygame.display.flip()

# initializes pygame module
if __name__ == "__main__":
    pygame.init()

    

    # initializes game window (pixel dimensions) and color (.fill)
    surface = pygame.display.set_mode((1000, 1000))
    surface.fill((194, 178, 128))
    # importing image as snake head and resizing it
    head = pygame.image.load("img/snake_head_block.png").convert()
    default_head_size = (25, 25)
    head = pygame.transform.scale(head, default_head_size)
    # setting the default position for the head and rendering it on the surface
    head_x = 500
    head_y = 500
    surface.blit(head, (head_x, head_y))
    # update the screen
    pygame.display.flip()

# setting game up to run and giving keystrokes functionality
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    head_y -= 20
                    draw_head()
                if event.key == K_DOWN:
                    head_y += 20
                    draw_head()
                if event.key == K_LEFT:
                    head_x -= 20
                    draw_head()
                if event.key == K_RIGHT:
                    head_x += 20
                    draw_head()
            elif event.type == QUIT:
                running = False
