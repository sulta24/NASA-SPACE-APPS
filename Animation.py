import pygame
from Gamesprite import *

pygame.init()

class animation():
    def __init__(self, name,anim_images, anim_count):
        self.images = anim_images
        self.counter = 0
        self.anim_count = anim_count - 1
        self.name = name
