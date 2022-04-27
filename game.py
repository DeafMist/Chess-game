import pygame
import os

from Chess.Chessboard import *

WIDTH = 660
HEIGHT = 661

COLOR = (255, 222, 173)
WHITE = (255, 255, 255)


class Characters(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        #        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(center=pos)


class Figure:
    def __init__(self, img_name, pos):
        self.img_name = img_name
        self.pos = pos


def placement(figures):
    for figure in figures:
        tmp_img = pygame.image.load(os.path.join(img_folder, figure.img_name)).convert_alpha()
        tmp_rect = tmp_img.get_rect(center=figure.pos)
        screen.blit(tmp_img, tmp_rect)
    pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')
pygame.display.set_icon(pygame.image.load('icon.bmp'))
screen.fill(COLOR)
pygame.display.flip()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

chessboard_img = pygame.image.load(os.path.join(img_folder, 'chessboard1.jpg')).convert()
chessboard_img.set_colorkey(WHITE)
chessboard_rect = chessboard_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

screen.blit(chessboard_img, chessboard_rect)
pygame.display.update()

figures = [Figure('kingWhite.png', (367.5, 578.5)), Figure('kingBlack.png', (367.5, 89.5)),
           Figure('queenWhite.png', (298.5, 578.5)), Figure('queenBlack.png', (298.5, 89.5)),
           Figure('bishopWhite.png', (229.5, 578.5)), Figure('bishopWhite.png', (436.5, 578.5)),
           Figure('bishopBlack.png', (229.5, 89.5)), Figure('bishopBlack.png', (436.5, 89.5)),
           Figure('knightWhite.png', (160.5, 578.5)), Figure('knightWhite.png', (505.5, 578.5)),
           Figure('knightBlack.png', (160.5, 89.5)), Figure('knightBlack.png', (505.5, 89.5)),
           Figure('rookWhite.png', (91.5, 578.5)), Figure('rookWhite.png', (574.5, 578.5)),
           Figure('rookBlack.png', (91.5, 89.5)), Figure('rookBlack.png', (574.5, 89.5)),
           Figure('pawnWhite.png', (367.5, 509.5)), Figure('pawnWhite.png', (298.5, 509.5)),
           Figure('pawnWhite.png', (229.5, 509.5)), Figure('pawnWhite.png', (436.5, 509.5)),
           Figure('pawnWhite.png', (160.5, 509.5)), Figure('pawnWhite.png', (505.5, 509.5)),
           Figure('pawnWhite.png', (91.5, 509.5)), Figure('pawnWhite.png', (574.5, 509.5)),
           Figure('pawnBlack.png', (367.5, 158.5)), Figure('pawnBlack.png', (298.5, 158.5)),
           Figure('pawnBlack.png', (229.5, 158.5)), Figure('pawnBlack.png', (436.5, 158.5)),
           Figure('pawnBlack.png', (160.5, 158.5)), Figure('pawnBlack.png', (505.5, 158.5)),
           Figure('pawnBlack.png', (91.5, 158.5)), Figure('pawnBlack.png', (574.5, 158.5)), ]

placement(figures)

chessboard = Chessboard()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.ACTIVEEVENT:
            pass
        elif True:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 0 < event.pos[0] < 57 or 0 < event.pos[1] < 55:
                continue

            i_start = (event.pos[0] - 57) // 69
            j_start = (event.pos[1] - 55) // 69

            if chessboard.board[i_start][j_start].chessman is None:
                continue

            for event_2 in pygame.event.get():
                if event_2.type == pygame.MOUSEBUTTONDOWN:
                    if 0 < event.pos[0] < 57 or 0 < event.pos[1] < 55:
                        continue

                    i_final = (event.pos[0] - 57) // 69
                    j_final = (event.pos[1] - 55) // 69

                    if chessboard.board[i_final][j_final].chessman.color == chessboard.board[i_start][j_start].chessman.color:
                        continue

                    if chessboard.board[i_start][j_start].chessman.move([i_final, j_final], chessboard) is False:
                        continue

                    chessboard.update((i_start, j_start), (i_final, j_final),
                                      chessboard.board[i_start][j_start].chessman,
                                      screen, chessboard_img, chessboard_rect)
                    pygame.display.update()
                    break

        pygame.display.update()

pygame.quit()
