# Your game should have a game loop that updates the game's state, draws the game on the screen, and handles input events.
import pygame
from sys import exit
from Stuff import pong

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

        # calling the ball movement function
        pong.move_ball(pong.ball_surface)

        # draw the ball
        pygame.draw.rect(screen, pong.ball_color, pong.ball_surface)

        # applying color on the display screen
        screen.fill(screenColor)