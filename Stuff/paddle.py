# Based on user input
# Entities (Things): Your game should have entities that represent things in the game, such as the player character or objects in the game world.
# Player Character: Your game should have a player character that the player can control.

import pygame
from Stuff import FrameViewer

displayScreen = FrameViewer

#Defining specifics of Paddle
PADDLE_SIZE = PADDLE_WIDTH, PADDLE_HEIGHT = 16, 100
PADDLE_POS = PADDLE_X, PADDLE_Y = 0, (displayScreen.SCREEN_HEIGHT - PADDLE_HEIGHT) / 2
paddleColor = ('black')
paddle_speed = 10

# Create the paddle surface
paddle_surface = pygame.Rect((PADDLE_X, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT))

def paddleDraw(screen):
    paddle = pygame.draw.rect(screen, paddleColor, paddle_surface)
    return paddle

def sharePaddleColor():
    return paddleColor