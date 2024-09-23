import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width = 1200
height = 700
window_size = (width, height)

# Create the window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Visualize")






fps = 10
clock = pygame.time.Clock()


running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





    # Update the display
    pygame.display.flip()
    clock.tick(fps)


# Quit Pygame
pygame.quit()
sys.exit()
