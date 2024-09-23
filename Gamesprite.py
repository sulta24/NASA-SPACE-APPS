import pygame

from pygame import *
pygame.init()

class GameSprite(pygame.sprite.Sprite):
    # конструктор класса
    #arguments initilisation
    def __init__(self, screen, player_image, player_x, player_y, size_x, size_y):
        # Вызываем конструктор класса (Sprite):
        pygame.sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.screen = screen

    # метод, отрисовывающий героя на окне
    def reset(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

