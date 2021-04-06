from board import BoardSquare, Piece, Position
from globals import HEIGHT, WIDTH, grid, WIN, prevState
import pygame
import colors
from copy import copy, deepcopy
# prevState = grid
def updatePieces():
    global prevState
    if grid != prevState:
        prevState = copy(grid)
        for row in grid:
            for square in row:
                if square.filled:
                    width = int(square.width*0.8)
                    scaledPiece = pygame.transform.scale(square.piece.image, (width, width))
                    position = (square.position.left + square.width*0.1, square.position.top + square.width*0.1)
                    WIN.blit(scaledPiece, position)
                if square.highlighted:
                    drawCircle(square.location)
        pygame.display.update()

def drawPiece(color, name, position):
    square = grid[position[0]][position[1]]
    square.piece = Piece(color=color, name=name)
    square.filled = True

def deletePiece(position):
    square = grid[position[0]][position[1]]
    square.piece = None
    square.filled = False

def drawCircle(position):
    transparency = 80
    row, col = position
    square = grid[row][col]
    location = square.position
    squareWidth = square.width
    surface = pygame.Surface((100, 100))
    surface.set_colorkey((0,0,0))
    surface.set_alpha(transparency/100*255)
    pygame.draw.circle(surface, color=colors.GRAY, center=(50,50), radius=squareWidth*0.6/2)
    WIN.blit(surface, (location.left, location.top))
    pygame.display.update()

