# Your game should have a game loop that updates the game's state, draws the game on the screen, and handles input events.

import pygame
#from Stuff import paddle
from Stuff import Controller
from sys import exit
from Stuff import pong

def gameLoop(screen, screenColor, paddle_surface, paddleColor, pongBall, pongColor):
    # while loop to keep the window available until quit
    while True:
    # get events from the queue & handle events every frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # calling the paddle movement function
        Controller.move_rect(paddle_surface)

        # calling the ball movement function
        #pong.move_ball(pong.ball_surface)

        # applying color on the display screen
        screen.fill(screenColor)

        # redraw the paddle at the position at which it is moved
        pygame.draw.rect(screen, paddleColor, paddle_surface)

        #fetch the new position of the ball as it moves
        #ballNewPos = Controller.updateBallPosition(pongBall, pong.ball_velocity_x, pong.ball_velocity_y, paddle_surface)
        ballNewPos = Controller.updateBallPosition(pongBall, paddle_surface)

        # draw the ball
        #pygame.draw.rect(screen, pong.ball_color, pong.ball_surface)
        pygame.draw.circle(screen, pongColor, ballNewPos, pong.BALL_RADIUS)

        # display screen until quit
        pygame.display.update()