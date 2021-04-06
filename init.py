from globals import grid, WIN, WIDTH, HEIGHT
from piece import drawPiece
from board import BoardSquare, Position
import colors
import pygame
class InitializeBoard:
    def __init__(self) -> None:
        WIN.fill(colors.BACKGROUND_BLACK)
        self.drawBoard()
        self.initPieces()
        pygame.display.update()
    
    def initPieces(self):
        drawPiece(color="BLACK", name="ROOK", position=(0,0))
        drawPiece(color="BLACK", name="KNIGHT", position=(0,1))
        drawPiece(color="BLACK", name="BISHOP", position=(0,2))
        drawPiece(color="BLACK", name="QUEEN", position=(0,3))
        drawPiece(color="BLACK", name="KING",position=(0,4))
        drawPiece(color="BLACK", name="BISHOP", position=(0,5))
        drawPiece(color="BLACK", name="KNIGHT", position=(0,6))
        drawPiece(color="BLACK", name="ROOK", position=(0,7))
        for i in range(8):
            drawPiece(color="BLACK", name="PAWN", position=(1,i))
        drawPiece(color="WHITE", name="ROOK", position=(7,0))
        drawPiece(color="WHITE", name="KNIGHT", position=(7,1))
        drawPiece(color="WHITE", name="BISHOP", position=(7,2))
        drawPiece(color="WHITE", name="QUEEN", position=(7,3))
        drawPiece(color="WHITE", name="KING",position=(7,4))
        drawPiece(color="WHITE", name="BISHOP", position=(7,5))
        drawPiece(color="WHITE", name="KNIGHT", position=(7,6))
        drawPiece(color="WHITE", name="ROOK",  position=(7,7))
        for i in range(8):
            drawPiece(color="WHITE", name="PAWN", position=(6,i))

    def drawBoard(self, squareSize=100):
        widthOffset = (WIDTH - squareSize*8)/2 
        heightOffset = (HEIGHT- squareSize*8)/2 
        black=True
        for row in range(8):
            black = not black
            for col in range(8):
                pos = Position(left=widthOffset + squareSize*col, top = heightOffset+squareSize*row )
                square = BoardSquare(position=pos, width=squareSize, piece=None, filled=None, location=(row, col))
                grid[row][col] = square
                rect = pygame.Rect(square.position.left, square.position.top, 100, 100)
                if black:
                    pygame.draw.rect(WIN, colors.BOARD_GREEN, rect)
                else: 
                    pygame.draw.rect(WIN, colors.BOARD_WHITE, rect)

                black = not black