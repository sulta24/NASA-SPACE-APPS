import pygame
import sys
import os
from Gamesprite import GameSprite
from motion import actual_motion
# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width = 1200
height = 700
window_size = (width, height)

# Create the window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Visualize")



test_sprite = GameSprite(screen, 'Num1.jpeg', 200, 100, 80, 115)

fps = 60
clock = pygame.time.Clock()


running = True
while running:
    clock.tick(fps)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    actual_motion(test_sprite, event, width, height)
    screen.fill((0, 0, 0))
    test_sprite.reset()





    # Update the display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
