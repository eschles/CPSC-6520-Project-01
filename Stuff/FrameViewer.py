# View --> Updates the screen

import pygame
from sys import exit

# Define Screen Size
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()