# Initial test file 

import pygame
from sys import exit
import pygame.time

# Define Screen Size
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
screenColor = (255, 230, 210)

# Set the size and position of the paddle
paddle_width = 16
paddle_height = 100
paddle_x = 0
paddle_y = (SCREEN_HEIGHT - paddle_height) / 2
paddleColor = (0, 0, 0)

# Initializing the game
pygame.init()

# pygame module to initialize a window or screen for display
screen = pygame.display.set_mode(SCREEN_SIZE)

# Create the paddle surface
paddle_surface = pygame.Rect((paddle_x, paddle_y, paddle_width, paddle_height))

#Assigning initial speed by which paddle will be moved
paddle_speed = 1

# Update the screen to show the changes
#pygame.display.flip()

#Defining clock and delt_time to make the paddle movement smooth
clock = pygame.time.Clock()
delta_time = clock.tick(100) / 1000.0

#function for keyboard input for paddle up and down
def move_rect(paddle_surface):
    keys = pygame.key.get_pressed()
    paddle_surface.y += paddle_speed * delta_time
    
    #when Up arrow key or down arrow key is pressed to move the paddle
    if keys[pygame.K_UP] and paddle_surface.y > 0:
        paddle_surface.move_ip(0, -paddle_speed)
    elif keys[pygame.K_DOWN] and paddle_surface.y < SCREEN_HEIGHT - paddle_height:
        paddle_surface.move_ip(0, paddle_speed)


# while loop to keep the window available until quit
while True:
    # get events from the queue & handle events every frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # display screen until quit
    pygame.display.update()

    #calling the paddle movement function
    move_rect(paddle_surface)

    # filling the portion of the display screen when the paddle is moved
    screen.fill(screenColor)
    #redrawing the paddle at the position at which it is moved
    pygame.draw.rect(screen, paddleColor, paddle_surface)

    # Update the screen to show the changes
    pygame.display.flip()
