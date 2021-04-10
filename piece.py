import pygame
from config import Colors, HEIGHT, Position, WIDTH, boardSprites, PIECE_SCALE_FACTOR


class Piece(pygame.sprite.Sprite):
    def __init__(self, color: str = None, name: str = None, center: Position = None):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.name = name
        raw = boardSprites[f"{color}_{name}"].convert()
        raw.set_colorkey((255,255,255))
        rawSize = raw.get_size()
        self.image = pygame.transform.scale(raw, (int(rawSize[0]*PIECE_SCALE_FACTOR), int(rawSize[1]*PIECE_SCALE_FACTOR)))
        # self.image = pygame.Surface((100, 100))
        # self.image.fill((Colors.GRAY))
        self.rect = self.image.get_rect()
        self.rect.center = (center.x, center.y)
        # pygame.sprite.Sprite.kill(self)

    # def update(self):
    #     if self.rect.y >= 600:
    #         self.delete()

    def delete(self):
        # print("killin")
        self.kill()
        # return True