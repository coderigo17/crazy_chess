import chess
import pygame
from constants import (
    BLACK,
    BOARD_SIZE,
    HIGHLIGHT_COLOR,
    LABEL_COLOR,
    LABEL_OFFSET_Y,
    LABEL_SIZE,
    PIECE_OFFSET_Y,
    PIECES,
    SQUARE_SIZE,
    WHITE,
)


def draw_board(screen, selected_square=None):
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(
                    col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE
                ),
            )

            # Highlight the selected square
            if selected_square is not None and selected_square == chess.square(
                col, 7 - row
            ):
                pygame.draw.rect(
                    screen,
                    HIGHLIGHT_COLOR,
                    pygame.Rect(
                        col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE
                    ),
                    5,
                )


def draw_pieces(screen, board):
    for row in range(8):
        for col in range(8):
            piece = board.piece_at(chess.square(col, 7 - row))
            if piece:
                piece_image = PIECES[piece.symbol()]
                x = col * SQUARE_SIZE + (SQUARE_SIZE - piece_image.get_width()) // 2
                y = (
                    row * SQUARE_SIZE
                    + (SQUARE_SIZE - piece_image.get_height()) // 2
                    - PIECE_OFFSET_Y
                )
                screen.blit(piece_image, (x, y))


def draw_labels(screen, font):
    # Draw row numbers
    for row in range(8):
        label = font.render(str(8 - row), True, LABEL_COLOR)
        screen.blit(label, (5, row * SQUARE_SIZE + SQUARE_SIZE // 3))

    # Draw column letters
    for col in range(8):
        label = font.render(chr(ord("a") + col), True, LABEL_COLOR)
        screen.blit(
            label,
            (
                col * SQUARE_SIZE + SQUARE_SIZE // 3,
                BOARD_SIZE - LABEL_SIZE + LABEL_OFFSET_Y,
            ),
        )
