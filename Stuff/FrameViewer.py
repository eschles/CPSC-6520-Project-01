# Your game should have a view that displays the game on the screen.
# Updating Screen: Your game should update the screen after each iteration of the game loop.

import pygame
#from sys import exit

# Define Screen Size
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
screenColor = ('white')

# Initializing the game
pygame.init()

# pygame module to initialize a window or screen for display
screen = pygame.display.set_mode(SCREEN_SIZE)

# while loop to keep the window available until quit
# while True:
#     # get events from the queue & handle events every frame
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#     # display screen until quit
#     pygame.display.update()

#     # applying color on the display screen
#     screen.fill(screenColor)