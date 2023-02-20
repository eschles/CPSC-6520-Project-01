# Loop
import pygame
from sys import exit

def gameLoop(screen, screenColor):
    # while loop to keep the window available until quit
    while True:
    # get events from the queue & handle events every frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # display screen until quit
        pygame.display.update()

        # applying color on the display screen
        screen.fill(screenColor)