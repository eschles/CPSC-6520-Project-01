# View: Your game should have a view that displays the game on the screen.
# Updating Screen: Your game should update the screen after each iteration of the game loop.

import pygame

# Define Screen Size
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
# Define Screen Color
screenColor = ('white')

# Function for creating display
def drawDisplay():
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.fill(screenColor)
    return screen

def shareScreenColor():
    return screenColor

def defineFont():
    # Set the font for the scores
    font = pygame.font.SysFont('comicsans', 20)
    return font