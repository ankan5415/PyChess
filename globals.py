import getPieces
import pygame
WIDTH, HEIGHT = 900, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
grid = [[None]*8 for i in range(8)]
boardPieces = getPieces.getBoardPieces()
