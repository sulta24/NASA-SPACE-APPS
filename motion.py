
from pygame import *


def actual_motion(self, event, width, height):
    if event.type == KEYDOWN:
        if event.key == K_LEFT and self.rect.x > 5:
            self.rect.x -= 10
        elif event.key == K_RIGHT and self.rect.x + 80 < width - 5:
            self.rect.x += 10
        elif event.key == K_UP and self.rect.y > 0:
            self.rect.y -= 10
        elif event.key == K_DOWN and self.rect.y + 115 < height - 5:
            self.rect.y += 10

    if event.type == KEYUP:
        if event.key == K_LEFT and self.rect.x > 5:
            self.rect.x -= 0
        elif event.key == K_RIGHT and self.rect.x + 80 < width - 5:
            self.rect.x += 0
        elif event.key == K_UP and self.rect.y > 0:
            self.rect.y -= 0
        elif event.key == K_DOWN and self.rect.y + 115 < height - 5:
            self.rect.y += 0