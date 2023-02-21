# Your game should have a view that displays the game on the screen.
# Updating Screen: Your game should update the screen after each iteration of the game loop.

import pygame
#from Stuff import paddle

# Define Screen Size
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
screenColor = ('white')

# pygame module to initialize a window or screen for display
#screen = pygame.display.set_mode(SCREEN_SIZE)

#screen.fill(screenColor)
#paddle.paddleDraw(SCREEN_HEIGHT, screen)

def drawDisplay():
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.fill(screenColor)
    return screen

def shareScreenColor():
    return screenColor