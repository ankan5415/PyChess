import pygame
from pygame import color, sprite
from Square import Square
from decorators import logInit
from config import Position, SQUARE, WIDTH, HEIGHT, Location, sprites



# @logInit
class Board:
    """
    8x8 Matrix Array Consisting of Squares
    """

    grid = []
    mouseClicked = False

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
        sprites.add(square.piece)
        return square.piece
    

    def deletePiece(self, location: Location):
        square = self.getSquare(location)
        square.piece.delete()
        

    def movePiece(self, oldLocation: Location, newLocation: Location):
        oldSquare = self.getSquare(oldLocation)
        name = oldSquare.piece.name
        color = oldSquare.piece.color
        print(oldLocation, name, color)
        self.deletePiece(oldLocation)
        piece = self.addPiece(newLocation, color, name)
        sprites.add(piece)


    def addIndicator(self, location:Location):
        square = self.getSquare(location)
        square.addIndicator()
        sprites.add(square.indicator)
        return square.indicator

    def clearIndicators(self):
        for move in self.moves:
            square = self.getSquare(move)
            square.indicator.kill()
        self.moves = set()
        self.indicatorOrigin = Location(-1, -1)


    def positionToLocation(self, position:Position) -> Location:
        x, y= position
        r = -1
        c = -1
        for row in range(8):
            square = self.getSquare(Location(row, 0))
            if square.pos.y <= y <= square.pos.y + SQUARE:
                r = row
                break
        for col in range(8):
            square = self.getSquare(Location(0, col))
            if square.pos.x <= x <= square.pos.x + SQUARE:
                c = col
                break
        return Location(r, c)


    def getMousePosition(self):
        x, y = pygame.mouse.get_pos()
        self.mouseLocation = self.positionToLocation(Position(x, y))
        return self.mouseLocation
    
    def handleClick(self):
        square = self.getSquare(self.mouseLocation)
        print(self.indicatorOrigin, self.mouseLocation)
        if square.indicator and -1 not in self.indicatorOrigin:
            # print(self.getSquare(self.indicatorOrigin).piece.name)
            self.movePiece(self.indicatorOrigin, self.mouseLocation)
            self.clearIndicators()
        elif square.piece and not square.indicator:
            self.getMoves(self.mouseLocation)
        else:
            self.clearIndicators()
            print("clicked on empty square")
            



    #========== Garbage code starts here. ============

    def getMoves(self, location:Location):
        self.indicatorOrigin = location
        piece = self.getSquare(location).piece
        def checkForPiece(loc: Location) -> bool:
            for i in loc:
                if not 0 <= i <= 7:
                    return False
            square = self.getSquare(loc)
            if not square.piece:
                self.moves.add(loc)
                return False
            else:
                if square.piece.color != piece.color:
                    self.moves.add(loc)
                return True

        self.moves = set()
        row, col = location
        if piece.name == "ROOK":
            for i in range(row - 1, 0):
                if checkForPiece(Location(i, col)):
                    break
            for i in range(row + 1, 8):
                if checkForPiece(Location(i, col)):
                    break
            for i in range(col - 1, 0):
                if checkForPiece(Location(row, i)):
                    break
            for i in range(col + 1, 8):
                if checkForPiece(Location(row, i)):
                    break
        elif piece.name == "KNIGHT":            
            checkForPiece(Location(row + 2, col - 1))
            checkForPiece(Location(row + 2, col + 1))
            checkForPiece(Location(row - 2, col - 1))
            checkForPiece(Location(row - 2, col + 1))
            checkForPiece(Location(row - 1, col + 2))
            checkForPiece(Location(row + 1, col + 2))
            checkForPiece(Location(row - 1, col - 2))
            checkForPiece(Location(row + 1, col - 2))
        elif piece.name == "BISHOP":
            for i in range(8):
                checkForPiece(Location(row + i, col + i))
                checkForPiece(Location(row - i, col + i))
                checkForPiece(Location(row + i, col - i))
                checkForPiece(Location(row - i, col - i))
        elif piece.name == "QUEEN":
            for i in range(8):
                checkForPiece(Location(row + i, col + i))
                checkForPiece(Location(row - i, col + i))
                checkForPiece(Location(row + i, col - i))
                checkForPiece(Location(row - i, col - i))
            for i in range(row - 1, 0):
                if checkForPiece(Location(i, col)):
                    break
            for i in range(row + 1, 8):
                if checkForPiece(Location(i, col)):
                    break
            for i in range(col - 1, 0):
                if checkForPiece(Location(row, i)):
                    break
            for i in range(col + 1, 8):
                if checkForPiece(Location(row, i)):
                    break
        elif piece.name == "KING":
            checkForPiece(Location(row + 1, col + 1))
            checkForPiece(Location(row + 1, col - 1))
            checkForPiece(Location(row - 1, col + 1))
            checkForPiece(Location(row - 1, col - 1))
            checkForPiece(Location(row + 1, col))
            checkForPiece(Location(row - 1, col))
            checkForPiece(Location(row, col + 1))
            checkForPiece(Location(row, col - 1))
        elif piece.name == "PAWN":
            if piece.color == "BLACK":
                checkForPiece(Location(row + 1, col))
                if self.getSquare(Location(row + 1, col + 1)).piece:
                    self.moves.add(Location(row + 1, col + 1))
                if self.getSquare(Location(row + 1, col - 1)).piece:
                    self.moves.add(Location(row + 1, col - 1))
            else:
                checkForPiece(Location(row - 1, col))
                if self.getSquare(Location(row - 1, col + 1)).piece:
                    # print("here")
                    self.moves.add(Location(row - 1, col + 1))
                if self.getSquare(Location(row - 1, col + 1)).piece:
                    # print("here")
                    self.moves.add(Location(row - 1, col - 1))
        else:
            print("Clicked on an invalid chess tile")
        
        for move in self.moves:
            self.addIndicator(move)
        # print(self.moves)



board = Board()