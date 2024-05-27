import chess
import pygame
from constants import BOARD_SIZE, LABEL_SIZE
from drawing import draw_board, draw_labels, draw_pieces
from events import get_square_under_mouse

# Initialize pygame
pygame.init()

# Initialize the screen
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
pygame.display.set_caption("Crazy Chess!")

# Define font for labels
pygame.font.init()
font = pygame.font.SysFont(None, LABEL_SIZE)


def main():
    board = chess.Board()
    selected_square = None
    selected_piece = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                square, piece = get_square_under_mouse(board)
                if selected_square is None:
                    if piece:
                        selected_square = square
                        selected_piece = piece
                else:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                    selected_square = None
                    selected_piece = None

        draw_board(screen, selected_square)
        draw_pieces(screen, board)
        draw_labels(screen, font)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
