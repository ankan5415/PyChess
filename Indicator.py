import pygame
from config import Position, SQUARE, WIN, Colors
from config import INDICATOR_TRANSPARENCY as transparency
class Indicator(pygame.sprite.Sprite):
    def __init__ (self, center:Position):
        pygame.sprite.Sprite.__init__(self)
        self.center = center
        self.image = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
        self.image.set_colorkey((0, 0, 0))
        self.image.set_alpha(transparency / 100 * 255)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, (Colors.GRAY), (50,50), 25)
        self.rect.center = center
