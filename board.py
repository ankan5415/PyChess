
from globals import boardPieces, grid

class Piece:
  def __init__(self, name:str, color: str) -> None:
      self.name = name
      self.color = color
      self.image = boardPieces[f"{self.color}_{self.name}"]

class Position:
  def __init__(self, left: int, top: int) -> None:
      self.top = top
      self.left = left
class BoardSquare:

  """
    Attributes:
    position: Position class
    width: int
    piece: Piece class
    filled: bool
    moves: set of positions
    """
  moves = set()
  def __init__(self, position: Position, width: int, piece: Piece=None, filled: bool=False, location:tuple = None):

    self.position = position
    self.width = width
    self.piece = piece
    self.filled = filled
    self.location = location

  def checkForPiece(self, position: tuple) -> bool:
    for i in position:
      if not 0 <= i <= 7:
        return False
    if not grid[position[0]][position[1]].piece:
      self.moves.add(position)
      return False
    else:
      return True
  
  def getMoves(self):
    row, col = self.location
    for i in grid:
      for j in i:
        # print(j.piece)
        pass
    if self.piece:
      if self.piece.name == "ROOK":
        for i in range(row-1, 0):
          if self.checkForPiece((i, col)):
            break 
        for i in range(row+1, 8): 
          if self.checkForPiece((i, col)):
            break 
        for i in range(col-1, 0):
          if self.checkForPiece((row, i)):
            break 
        for i in range(col+1, 8):
          if self.checkForPiece((row, i)):
            break 
      elif self.piece.name == "KNIGHT":
        self.checkForPiece((row+2, col-1))
        self.checkForPiece((row+2, col+1))
        self.checkForPiece((row-2, col-1))
        self.checkForPiece((row-2, col+1))
        self.checkForPiece((row-1, col+2))
        self.checkForPiece((row+1, col+2))
        self.checkForPiece((row-1, col-2))
        self.checkForPiece((row+1, col-2))
      elif self.piece.name == "BISHOP":
        for i in range(8):
          self.checkForPiece((row+i, col+i))
          self.checkForPiece((row-i, col+i))
          self.checkForPiece((row+i, col-i))
          self.checkForPiece((row-i, col-i))
      elif self.piece.name == "QUEEN":
        for i in range(8):
          self.checkForPiece((row+i, col+i))
          self.checkForPiece((row-i, col+i))
          self.checkForPiece((row+i, col-i))
          self.checkForPiece((row-i, col-i))
        for i in range(row-1, 0):
          if self.checkForPiece((i, col)):
            break 
        for i in range(row+1, 8): 
          if self.checkForPiece((i, col)):
            break 
        for i in range(col-1, 0):
          if self.checkForPiece((row, i)):
            break 
        for i in range(col+1, 8):
          if self.checkForPiece((row, i)):
            break 
      elif self.piece.name == "KING":
        self.checkForPiece((row+1, col+1))
        self.checkForPiece((row+1, col-1))
        self.checkForPiece((row-1, col+1))
        self.checkForPiece((row-1, col-1))
        self.checkForPiece((row+1, col))
        self.checkForPiece((row-1, col))
        self.checkForPiece((row, col+1))
        self.checkForPiece((row, col-1))
      elif self.piece.name == "PAWN":
        if self.piece.color == "BLACK":
          self.checkForPiece((row+1, col))
          if grid[row+1][col+1].piece:
            self.moves.add((row+1, col+1))
          if grid[row+1][col-1].piece:
            self.moves.add((row+1, col-1))
        else:
          self.checkForPiece((row-1, col))
          if grid[row-1][col+1].piece:
            print("here")
            self.moves.add((row-1, col+1))
          if grid[row-1][col+1].piece:
            print("here")
            self.moves.add((row-1, col-1))
      else:
        print("Clicked on an invalid chess tile")
    print(self.moves)
