import os
import numpy
import pygame

from Chess.chessmen.Bishop import Bishop
from Chess.chessmen.King import King
from Chess.chessmen.Knight import Knight
from Chess.chessmen.Pawn import Pawn
from Chess.chessmen.Queen import Queen
from Chess.chessmen.Rook import Rook


class Cell:
    def __init__(self, chessman, center):
        self.chessman = chessman
        self.center = center


class Chessboard:
    def start_pos(self, i, j, chessman):
        self.board[i][j].chessman = chessman

    def __init__(self):
        self.board = [[None] * 8] * 8

        cords = (91.5, 89.5)
        for i in range(8):
            for j in range(8):
                self.board[i][j] = Cell(None, cords)
                if j == 7:
                    tmp = (91.5, cords[1] + 69)
                    cords = tmp
                else:
                    tmp = (cords[0] + 69, cords[1])

        figures = [Rook((0, 0), 'black', 'rookBlack.png'), Knight((0, 1), 'black', 'knightBlack.png'),
                   Bishop((0, 2), 'black', 'bishopBlack.png'), Queen((0, 3), 'black', 'queenBlack.png'),
                   King((0, 4), 'black', 'kingBlack.png'), Bishop((0, 5), 'black', 'bishopBlack.png'),
                   Knight((0, 6), 'black', 'knightBlack.png'), Rook((0, 7), 'black', 'rookBlack.png'),
                   Pawn((1, 0), 'black', 'pawnBlack.png'), Pawn((1, 1), 'black', 'pawnBlack.png'),
                   Pawn((1, 2), 'black', 'pawnBlack.png'), Pawn((1, 3), 'black', 'pawnBlack.png'),
                   Pawn((1, 4), 'black', 'pawnBlack.png'), Pawn((1, 5), 'black', 'pawnBlack.png'),
                   Pawn((1, 6), 'black', 'pawnBlack.png'), Pawn((1, 7), 'black', 'pawnBlack.png'),
                   Rook((7, 0), 'white', 'rookWhite.png'), Knight((7, 1), 'white', 'knightWhite.png'),
                   Bishop((7, 2), 'white', 'bishopWhite.png'), Queen((7, 3), 'white', 'queenWhite.png'),
                   King((7, 4), 'white', 'kingWhite.png'), Bishop((7, 5), 'white', 'bishopWhite.png'),
                   Knight((7, 6), 'white', 'knightWhite.png'), Rook((7, 7), 'white', 'rookWhite.png'),
                   Pawn((6, 0), 'white', 'pawnWhite.png'), Pawn((6, 1), 'white', 'pawnWhite.png'),
                   Pawn((6, 2), 'white', 'pawnWhite.png'), Pawn((6, 3), 'white', 'pawnWhite.png'),
                   Pawn((6, 4), 'white', 'pawnWhite.png'), Pawn((6, 5), 'white', 'pawnWhite.png'),
                   Pawn((6, 6), 'white', 'pawnWhite.png'), Pawn((6, 7), 'white', 'pawnWhite.png')]

        for figure in figures:
            self.start_pos(figure.field[0], figure.field[1], figure)

    def update(self, start, final, chessman, screen, chessboard_img, chessboard_rect):
        self.board[start[0]][start[1]].chessman = None
        self.board[final[0]][final[1]].chessman = chessman

        screen.clear()
        screen.blit(chessboard_img, chessboard_rect)

        for elem in self.board:
            if elem.chessman is not None:
                tmp_img = pygame.image.load(
                    os.path.join('C:\\Users\\romap\\PythonProjects\\Chess\\images',
                                 elem.chessman.img_name)).convert_alpha()
                tmp_rect = tmp_img.get_rect(center=self.board[final[0]][final[1]].center)
                screen.blit(tmp_img, tmp_rect)
