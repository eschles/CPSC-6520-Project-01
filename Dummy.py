# Initial test file 

import pygame
from sys import exit

# Define Screen Size
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400

# Set the size and position of the paddle
paddle_width = 16
paddle_height = 100
paddle_x = 0
paddle_y = (SCREEN_HEIGHT - paddle_height) / 2

# Initializing the game
pygame.init()

# pygame module to initialize a window or screen for display
screen = pygame.display.set_mode(SCREEN_SIZE)

# Create the paddle surface
paddle_surface = pygame.Surface((paddle_width, paddle_height))
paddle_surface.fill((255, 255, 255))  # Set the color of the paddle

# Draw the paddle on the screen
screen.blit(paddle_surface, (paddle_x, paddle_y))

# while loop to keep the window available until quit
while True:
    # get events from the queue & handle events every frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # display screen until quit
    pygame.display.update()

