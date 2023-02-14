# Initial test file 

import pygame
from sys import exit

# Define Screen Size
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400

# Initializing the game
pygame.init()

# pygame module to initialize a window or screen for display
screen = pygame.display.set_mode(SCREEN_SIZE)

# while loop to keep the window available until quit
while True:
    # get events from the queue & handle events every frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # display screen until quit
    pygame.display.update()