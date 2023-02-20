# Initial test file 

import pygame
from sys import exit
import pygame.time

# Define Screen Size
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
screenColor = ('white')

# Set the size, starting position, color, and speed of the paddle
PADDLE_SIZE = PADDLE_WIDTH, PADDLE_HEIGHT = 16, 100
PADDLE_POS = PADDLE_X, PADDLE_Y = 0, (SCREEN_HEIGHT - PADDLE_HEIGHT) / 2
paddleColor = ('black')
paddle_speed = 10

# Set the size, starting position, color, and speed of the ball
BALL_SIZE = BALL_WIDTH, BALL_HEIGHT = 15, 15
BALL_POS = BALL_X, BALL_Y = 785, 200
ball_color = ('blue')
ball_speed = 5

# Initializing the game
pygame.init()

# pygame module to initialize a window or screen for display
screen = pygame.display.set_mode(SCREEN_SIZE)

# Create the paddle surface
paddle_surface = pygame.Rect((PADDLE_X, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT))

# Create the ball surface
ball_surface = pygame.Rect((BALL_X, BALL_Y, BALL_WIDTH, BALL_HEIGHT))

# Create the gameboard surface
wall_surface = pygame.Rect((SCREEN_SIZE), (SCREEN_SIZE))

#Defining clock and delt_time to make the paddle movement smooth
clock = pygame.time.Clock()
delta_time = clock.tick(100) / 1000.0

# function for keyboard input for paddle up and down
def move_rect(paddle_surface):
    keys = pygame.key.get_pressed()
    paddle_surface.y += paddle_speed * delta_time
    
    #when Up arrow key or down arrow key is pressed to move the paddle
    if keys[pygame.K_UP] and paddle_surface.y > 0:
        paddle_surface.move_ip(0, -paddle_speed)
    elif keys[pygame.K_DOWN] and paddle_surface.y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        paddle_surface.move_ip(0, paddle_speed)

# function for automatic ball movement
def move_ball(ball_surface):
    ball_surface.move_ip(-3, 0)

    # create collider for the ball
    ball_collision = ball_surface.colliderect(paddle_surface)

    # create collider for the walls
    wall_collision = ball_surface.colliderect(wall_surface)

    if ball_collision:
        print('collision')

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
    move_rect(paddle_surface)

    # calling the ball movement function
    move_ball(ball_surface)

    # filling the portion of the display screen when the paddle is moved
    screen.fill(screenColor)

    # redrawing the paddle at the position at which it is moved
    pygame.draw.rect(screen, paddleColor, paddle_surface)

    # draw the ball
    pygame.draw.rect(screen, ball_color, ball_surface)

    # Update the screen to show the changes
    pygame.display.flip()