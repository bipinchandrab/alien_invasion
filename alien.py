import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.ico')
        self.rect = pygame.Rect(0,0,10,10)

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
