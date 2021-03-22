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
        drawPiece(color="BLACK", name="ROOK", location=(0,0))
        drawPiece(color="BLACK", name="KNIGHT", location=(0,1))
        drawPiece(color="BLACK", name="BISHOP", location=(0,2))
        drawPiece(color="BLACK", name="QUEEN", location=(0,3))
        drawPiece(color="BLACK", name="KING",location=(0,4))
        drawPiece(color="BLACK", name="BISHOP", location=(0,5))
        drawPiece(color="BLACK", name="KNIGHT", location=(0,6))
        drawPiece(color="BLACK", name="ROOK", location=(0,7))
        # for i in range(8):
        #     drawPiece(color="BLACK", name="PAWN", location=(1,i))
        drawPiece(color="WHITE", name="ROOK", location=(7,0))
        drawPiece(color="WHITE", name="KNIGHT", location=(7,1))
        drawPiece(color="WHITE", name="BISHOP", location=(7,2))
        drawPiece(color="WHITE", name="QUEEN", location=(7,3))
        drawPiece(color="WHITE", name="KING",location=(7,4))
        drawPiece(color="WHITE", name="BISHOP", location=(7,5))
        drawPiece(color="WHITE", name="KNIGHT", location=(7,6))
        drawPiece(color="WHITE", name="ROOK",  location=(7,7))
        for i in range(8):
            drawPiece(color="WHITE", name="PAWN", location=(6,i))

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