# Model: Your game should have a model that represents the game's data and the current state of the game.
# State of the game: Your game should keep track of the state of the game and update it based on input events and other events.

# Controller: Your game should have a controller that controls the game's logic and handles input events.
# Inputs: Your game should handle inputs from the player, such as keyboard or mouse events.
# Event Queue: Your game should have an event queue that stores and processes input events.

from Stuff import paddle
from Stuff import FrameViewer
import pygame.time

p_var = paddle

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
    elif keys[pygame.K_DOWN] and paddle_surface.y < FrameViewer.SCREEN_HEIGHT - p_var.PADDLE_HEIGHT:
        paddle_surface.move_ip(0, p_var.paddle_speed)
