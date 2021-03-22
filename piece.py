from board import Piece
from globals import grid, WIN
import pygame


def updatePieces():
    for row in grid:
        for square in row:
            if square.filled:
                width = int(square.width*0.8)
                scaledPiece = pygame.transform.scale(square.piece.image, (width, width))
                position = (square.position.left + square.width*0.1, square.position.top + square.width*0.1)
                WIN.blit(scaledPiece, position)
    pygame.display.update()

def drawPiece(color, name, location):
    square = grid[location[0]][location[1]]
    square.piece = Piece(color=color, name=name)
    square.filled = True

def deletePiece(location):
    square = grid[location[0]][location[1]]
    square.piece = None
    square.filled = False
