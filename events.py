import chess
import pygame
from constants import SQUARE_SIZE


def get_square_under_mouse(board):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    col = mouse_x // SQUARE_SIZE
    row = mouse_y // SQUARE_SIZE
    if col >= 0 and col < 8 and row >= 0 and row < 8:
        square = chess.square(col, 7 - row)
        piece = board.piece_at(square)
        return square, piece
    return None, None
