from Indicator import Indicator
from config import Colors, Location, Position, WIN
import pygame
from pygame.locals import *
from Piece import Piece
from decorators import logInit

# @logInit
class Square:
    """
    A single square on the board
    """

    def __init__(
        self, color: str, position: Position, piece: Piece = None, width: int = 100, indicator: Indicator=None
    ):
        self.indicator = indicator
        self.color = color
        self.rgb = getattr(Colors, self.color)
        self.center = Position(position.x + width / 2, position.y + width / 2)
        self.pos = position
        self.piece = piece
        self.width = width
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.width)
        self.update()

    def addPiece(self, color, name):
        self.piece = Piece(color, name, self.center)
        # self.piece.update(self.center)

    def update(self):
        pygame.draw.rect(WIN, self.rgb, self.rect)
    
    def addIndicator(self):
        self.indicator = Indicator(center = self.center)