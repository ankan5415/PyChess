from pygame.key import name
from Piece import Piece
from config import Location
from decorators import logInit
from Board import board
from config import BOARD_INVERTED
@logInit
def createBoardPieces():
    c1, c2 = "BLACK", "WHITE"
    if BOARD_INVERTED:
        c1, c2 = c2, c1

    board.addPiece(location=Location(0,0), color=c1, name="ROOK")
    board.addPiece(location=Location(0,1), color=c1, name="KNIGHT")
    board.addPiece(location=Location(0,2), color=c1, name="BISHOP")
    board.addPiece(location=Location(0,3), color=c1, name="KING")
    board.addPiece(location=Location(0,4), color=c1, name="QUEEN")
    board.addPiece(location=Location(0,5), color=c1, name="BISHOP")
    board.addPiece(location=Location(0,6), color=c1, name="KNIGHT")
    board.addPiece(location=Location(0,7), color=c1, name="ROOK")
    # for i in range(8):
    #     board.addPiece(location=Location(1,i), color=c1, name="PAWN")
    
    board.addPiece(location=Location(7,0), color=c2, name="ROOK")
    board.addPiece(location=Location(7,1), color=c2, name="KNIGHT")
    board.addPiece(location=Location(7,2), color=c2, name="BISHOP")
    board.addPiece(location=Location(7,3), color=c2, name="KING")
    board.addPiece(location=Location(7,4), color=c2, name="QUEEN")
    board.addPiece(location=Location(7,5), color=c2, name="BISHOP")
    board.addPiece(location=Location(7,6), color=c2, name="KNIGHT")
    board.addPiece(location=Location(7,7), color=c2, name="ROOK")
    for i in range(8):
        board.addPiece(location=Location(6,i), color=c2, name="PAWN")