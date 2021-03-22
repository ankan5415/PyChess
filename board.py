
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
    """
  def __init__(self, position: Position, width: int, piece: Piece=None, filled: bool=False, location:tuple = None):

    self.position = position
    self.width = width
    self.piece = piece
    self.filled = filled
    self.location = location
  
  def getMoves(self):
    loc = self.location
    moves = []
    for i in grid:
      for j in i:
        # print(j.piece)
        pass
    if self.piece:
      if self.piece.name == "ROOK":
        for i in range(loc[0]-1, 0):
          if grid[i][loc[1]].piece or not 0 <= i <= 8:
            print(grid[i][loc[1]].piece.name)
            break
          moves.append((i, loc[1]))
        for i in range(loc[0]+1, 8): 
          if grid[i][loc[1]].piece or not 0 <= i <= 8:
            print(grid[i][loc[1]].piece.name)
            break
          moves.append((i,loc[1]))
        for i in range(loc[1]-1, 0):
          if grid[loc[0]][i].piece or not 0 <= i <= 8:
            print(grid[loc[0]][i].piece.name)
            break
          moves.append((loc[0][i]))
        for i in range(loc[1]+1, 8):
          if grid[loc[0]][i].piece or not 0 <= i <= 8:
            print(grid[loc[0]][i].piece.name)
            break
          moves.append((loc[0],[i]))
    print(moves)
