# Controller: Your game should have a controller that controls the game's logic and handles input events.
# Inputs: Your game should handle inputs from the player, such as keyboard or mouse events.
# Event Queue: Your game should have an event queue that stores and processes input events.

from Stuff import paddle
from Stuff import FrameViewer
from Stuff import pong
import pygame.time

p_var = paddle
f_var = FrameViewer
po_var = pong

# function for keyboard input for paddle up and down
def move_rect(paddle_surface):
    #Defining clock and delt_time to make the paddle movement smooth
    clock = pygame.time.Clock()
    delta_time = clock.tick(100) / 1000.0
    #paddle_speed = 10

    #defining key press
    keys = pygame.key.get_pressed()
    paddle_surface.y += p_var.paddle_speed * delta_time
    
    #when Up arrow key or down arrow key is pressed to move the paddle
    if keys[pygame.K_UP] and paddle_surface.y > 0:
        paddle_surface.move_ip(0, -p_var.paddle_speed)
    elif keys[pygame.K_DOWN] and paddle_surface.y < f_var.SCREEN_HEIGHT - p_var.PADDLE_HEIGHT:
        paddle_surface.move_ip(0, p_var.paddle_speed)

# function for automatic ball movement
# def move_ball(ball_surface):
#     ball_surface.move_ip(-3, 0)

#     # create collider for the ball
#     ball_collision = ball_surface.colliderect(Dummy.paddle_surface)

#     # create collider for the walls
#     wall_collision = ball_surface.colliderect(Dummy.wall_surface)

#     if ball_collision:
#         print('collision')

#def updateBallPosition(pongBall, ball_velocity_x, ball_velocity_y, paddle_surface):
def updateBallPosition(pongBall, paddle_surface):
    # Update ball position based on velocity
    ball_velocity_x = po_var.ball_velocity_x
    ball_velocity_y = po_var.ball_velocity_y
    pongBall.x += ball_velocity_x
    pongBall.y += ball_velocity_y

    # Check if ball hits a wall and reverse direction if necessary
    if pongBall.y < pong.BALL_RADIUS or pongBall.y > f_var.SCREEN_HEIGHT - pong.BALL_RADIUS:
        ball_velocity_y = -(ball_velocity_y)
        print("ball_velocity_y =", ball_velocity_y)
    if pongBall.x < pong.BALL_RADIUS or pongBall.x > f_var.SCREEN_WIDTH - pong.BALL_RADIUS:
        ball_velocity_x = -(ball_velocity_x)
        print("ball_velocity_x", ball_velocity_x)

    # Check if ball hits paddle and reverse direction if necessary
    if pongBall.y > f_var.SCREEN_HEIGHT - pong.BALL_RADIUS and pongBall.x > paddle_surface.x and pongBall.x < paddle_surface.x + 128:
        ball_velocity_y = -(ball_velocity_y)
    
    return (pongBall.x, pongBall.y)