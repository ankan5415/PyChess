from decorators import logInit
import pygame
from config import Location, Position, WIN, WIDTH, HEIGHT, Colors, sprites
from Board import board
from Piece import Piece
from functions import createBoardPieces
from Indicator import Indicator

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Chess")

FPS = 1
BACKGROUND = Colors.BACKGROUND_BLACK
PIECE_DIM = int(min((WIDTH, HEIGHT)) / 12)
WIN.fill(BACKGROUND)

# @logInit
def main():
    createBoardPieces()
    board.getMoves(Location(0,7))
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #update
        sprites.update()
        #draw
        WIN.fill(BACKGROUND)
        board.drawBoard()
        sprites.draw(WIN)
        pygame.display.flip()
        board.clearIndicators()
        # board.movePiece(Location(1,1), Location(2,2))
    pygame.quit()


if __name__ == "__main__":
    main()