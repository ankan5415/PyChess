import pygame
import colors
from board import BoardSquare, Position
from init import InitializeBoard
from piece import drawCircle, updatePieces
from globals import grid, boardPieces, WIN, WIDTH, HEIGHT
import time
FPS = 60
BACKGROUND = colors.BACKGROUND_BLACK
PIECE_DIM = int(min((WIDTH, HEIGHT))/ 12)

pygame.init()
pygame.display.set_caption("Chess")


def main():
    clock = pygame.time.Clock()
    run = True
    InitializeBoard()
    grid[6][2].highlighted = False
    # initPieces(boardPieces=boardPieces)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        updatePieces()
        grid[6][2].highlighted = not grid[6][2].highlighted
        print(grid[6][2].highlighted)




    pygame.quit()

if __name__ == "__main__":
    main()