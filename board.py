from pygame import sprite
from Square import Square
from decorators import logInit
from config import Position, SQUARE, WIDTH, HEIGHT, Location, sprites



# @logInit
class Board:
    """
    8x8 Matrix Array Consisting of Squares
    """

    grid = []

    def __init__(self):
        self.drawBoard()

    def drawBoard(self):
        # print("drawing board")
        if self.grid != []:
            for row in range(8):
                for col in range(8):
                    square = self.getSquare(Location(row, col))
                    square.update()
        else:
            widthOffset = (WIDTH - SQUARE * 8) / 2
            heightOffset = (HEIGHT - SQUARE * 8) / 2
            isWhite = False
            for row in range(8):
                temp = []
                for col in range(8):
                    pos = Position(
                        widthOffset + SQUARE * col,
                        heightOffset + SQUARE * row,
                    )
                    color = "WHITE" if isWhite else "GREEN"
                    temp.append(Square(color=color, position=pos))
                    isWhite = not isWhite
                self.grid.append(temp)
                isWhite = not isWhite
            del temp

    def getSquare(self, location: Location) -> Square:
        return self.grid[location.row][location.col]

    def addPiece(self, location: Location, color, name):

        square = self.getSquare(location)
        square.addPiece(color, name)
        return square.piece

    def deletePiece(self, location: Location):
        square = self.getSquare(location)
        square.piece.delete()

    def movePiece(self, oldLocation: Location, newLocation: Location):
        oldSquare = self.getSquare(oldLocation)
        name = oldSquare.piece.name
        color = oldSquare.piece.color
        self.deletePiece(oldLocation)
        piece = self.addPiece(newLocation, color, name)
        sprites.add(piece)
