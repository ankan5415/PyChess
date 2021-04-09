import pygame
from config import Colors, HEIGHT, Position, WIDTH


class Piece(pygame.sprite.Sprite):
    def __init__(self, color: str = None, name: str = None, center: Position = None):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.name = name
        # self.image = boardSprites[f"{color}_{name}"]
        self.image = pygame.Surface((100, 100))
        self.image.fill((Colors.GRAY))
        self.rect = self.image.get_rect()
        self.rect.center = (center.x, center.y)
        # pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.rect.y >= 600:
            self.delete()

    def delete(self):
        # print("killin")
        self.kill()
        # return True