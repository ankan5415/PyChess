import getPieces
import pygame
WIDTH, HEIGHT = 900, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
grid = [[None]*8 for i in range(8)]
prevState = [[None]*8 for i in range(8)]
# prevState = grid
boardPieces = getPieces.getBoardPieces()
