import pygame
import sys
import os
from Gamesprite import GameSprite
from motion import actual_motion
from Animation import animation
# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width = 1200
height = 700
window_size = (width, height)

# Create the window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Visualize")


def anim_print(self):
    self.name.image = pygame.transform.scale(pygame.image.load(self.images[self.counter]), (self.name.size_x, self.name.size_y))
    self.rect = self.name.image.get_rect()
    self.rect.x = self.name.rect.x
    self.rect.y = self.name.rect.y
    if self.counter == self.anim_count:
        self.counter = 0
    else:
        self.counter += 1









test_sprite = GameSprite(screen, 'Num1.jpeg', 200, 100, 80, 115)
test_sprite_anim = animation(test_sprite, [
    'Num1.jpeg',
    'Num2.jpeg',
    'Num3.jpeg'

], 3)
test_rat = GameSprite(screen, 'rat.png', 1000, 500, 100, 50)
scintist_room = [test_rat]

fps = 10
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
    for i in scintist_room:
        i.reset()
    anim_print(test_sprite_anim)
    test_sprite.reset()




    # Update the display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
