# Iterates through the loop

# Ball Movement:
# Apply contstant velocity in a single direction
# Upon collision, apply acceleration in another direction

import pygame, sys
import Dummy

# Set the size, starting position, color, and speed of the ball
BALL_SIZE = BALL_WIDTH, BALL_HEIGHT = 15, 15
BALL_POS = BALL_X, BALL_Y = 785, 200
ball_color = ('blue')
ball_speed = 5

# Create the ball surface
ball_surface = pygame.Rect((BALL_X, BALL_Y, BALL_WIDTH, BALL_HEIGHT))

# function for automatic ball movement
def move_ball(ball_surface):
    ball_surface.move_ip(-3, 0)

    # create collider for the ball
    ball_collision = ball_surface.colliderect(Dummy.paddle_surface)

    # create collider for the walls
    wall_collision = ball_surface.colliderect(Dummy.wall_surface)

    if ball_collision:
        print('collision')

