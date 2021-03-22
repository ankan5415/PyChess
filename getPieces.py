import os
import pygame
def getPath(fileName):
  return os.path.join('assets/board_pieces', fileName)

def getBoardPieces():
  pieces = ["bishop", "king", "knight", "pawn", "queen", "rook"]
  res = {}
  for piece in pieces:
    res[f"BLACK_{piece.upper()}"] = pygame.image.load(getPath(f"b_{piece}.png"))
  for piece in pieces:
    res[f"WHITE_{piece.upper()}"] = pygame.image.load(getPath(f"w_{piece}.png"))
  return res
