# Your game should have a game loop that updates the game's state, draws the game on the screen, and handles input events.

import pygame
from Stuff import paddle
from Stuff import EventHandler
from sys import exit
from Stuff import pong

def gameLoop(screen, screenColor, paddle_surface):
    # while loop to keep the window available until quit
    while True:
    # get events from the queue & handle events every frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # display screen until quit
        pygame.display.update()

        # calling the paddle movement function
        EventHandler.move_rect(paddle_surface)

        # calling the ball movement function
        pong.move_ball(pong.ball_surface)

        # draw the ball
        pygame.draw.rect(screen, pong.ball_color, pong.ball_surface)

        # applying color on the display screen
        screen.fill(screenColor)

        # draw at the initial position and redraw the paddle at the position at which it is moved
        pygame.draw.rect(screen, paddle.paddleColor, paddle_surface)