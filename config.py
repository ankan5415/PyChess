import os
from collections import namedtuple
import pygame

WIDTH, HEIGHT = 900, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
SQUARE = 100
PIECE_SCALE_FACTOR = 0.6
BOARD_INVERTED = False
INDICATOR_RADIUS = 25
INDICATOR_TRANSPARENCY = 80 #between 0 and 100


sprites = pygame.sprite.Group()

_Position = namedtuple("Position", ["x", "y"])
_Location = namedtuple("Location", ["row", "col"])  # row and column


class Position(_Position):
    """
    A cartesian coordinate on the screen

    values ->  x and y (top and left)
    """

    pass


class Location(_Location):
    """
    A location on the board grid

    values -> row and col
    """

    pass


class Colors:
    # WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    # RED = (255, 0, 0)
    # GREEN = (0, 255, 0)
    # BLUE = (0, 0, 255)
    GRAY = (150, 150, 150)
    # GRAY_SEMI = (150, 150, 150, 0.1)
    GREEN = (119, 149, 86)
    WHITE = (235, 236, 208)
    BACKGROUND_BLACK = (49, 46, 43)


def getBoardPieces():
    def getPath(fileName):
        return os.path.join("assets/board_pieces", fileName)

    pieces = ["bishop", "king", "knight", "pawn", "queen", "rook"]
    res = {}
    for piece in pieces:
        res[f"BLACK_{piece.upper()}"] = pygame.image.load(getPath(f"b_{piece}.png"))
    for piece in pieces:
        res[f"WHITE_{piece.upper()}"] = pygame.image.load(getPath(f"w_{piece}.png"))
    return res


boardSprites = getBoardPieces()