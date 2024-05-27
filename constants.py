import pygame

BOARD_SIZE = 800
SQUARE_SIZE = BOARD_SIZE // 8
LABEL_SIZE = SQUARE_SIZE // 6

WHITE = (253, 232, 182)
BLACK = (80, 9, 9)
LABEL_COLOR = (150, 150, 150)

# Highlight color for the selected square
HIGHLIGHT_COLOR = (173, 216, 230)

# Scale factor for the pieces
PIECE_SCALE_FACTOR = 0.9

# Offset to shift the pieces upwards
PIECE_OFFSET_Y = SQUARE_SIZE // 12

# Offset to shift the labels downwards
LABEL_OFFSET_Y = LABEL_SIZE // 4

PIECES = {
    "r": pygame.transform.scale(
        pygame.image.load("assets/black_rook.png"),
        (int(SQUARE_SIZE * PIECE_SCALE_FACTOR), int(SQUARE_SIZE * PIECE_SCALE_FACTOR)),
    ),
    "n": pygame.transform.scale(
        pygame.image.load("assets/black_knight.png"),
        (int(SQUARE_SIZE * PIECE_SCALE_FACTOR), int(SQUARE_SIZE * PIECE_SCALE_FACTOR)),
    ),
    "b": pygame.transform.scale(
        pygame.image.load("assets/black_bishop.png"),
        (int(SQUARE_SIZE * PIECE_SCALE_FACTOR), int(SQUARE_SIZE * PIECE_SCALE_FACTOR)),
    ),
    "q": pygame.transform.scale(
        pygame.image.load("assets/black_queen.png"),
        (int(SQUARE_SIZE * PIECE_SCALE_FACTOR), int(SQUARE_SIZE * PIECE_SCALE_FACTOR)),
    ),
    "k": pygame.transform.scale(
        pygame.image.load("assets/black_king.png"),
        (int(SQUARE_SIZE * PIECE_SCALE_FACTOR), int(SQUARE_SIZE * PIECE_SCALE_FACTOR)),
    ),
    "p": pygame.transform.scale(
        pygame.image.load("assets/black_pawn.png"),
        (int(SQUARE_SIZE * PIECE_SCALE_FACTOR), int(SQUARE_SIZE * PIECE_SCALE_FACTOR)),
    ),
    "R": pygame.transform.scale(
        pygame.image.load("assets/white_rook.png"),
        (int(SQUARE_SIZE * PIECE_SCALE_FACTOR), int(SQUARE_SIZE * PIECE_SCALE_FACTOR)),
    ),
    "N": pygame.transform.scale(
        pygame.image.load("assets/white_knight.png"),
        (int(SQUARE_SIZE * PIECE_SCALE_FACTOR), int(SQUARE_SIZE * PIECE_SCALE_FACTOR)),
    ),
    "B": pygame.transform.scale(
        pygame.image.load("assets/white_bishop.png"),
        (int(SQUARE_SIZE * PIECE_SCALE_FACTOR), int(SQUARE_SIZE * PIECE_SCALE_FACTOR)),
    ),
    "Q": pygame.transform.scale(
        pygame.image.load("assets/white_queen.png"),
        (int(SQUARE_SIZE * PIECE_SCALE_FACTOR), int(SQUARE_SIZE * PIECE_SCALE_FACTOR)),
    ),
    "K": pygame.transform.scale(
        pygame.image.load("assets/white_king.png"),
        (int(SQUARE_SIZE * PIECE_SCALE_FACTOR), int(SQUARE_SIZE * PIECE_SCALE_FACTOR)),
    ),
    "P": pygame.transform.scale(
        pygame.image.load("assets/white_pawn.png"),
        (int(SQUARE_SIZE * PIECE_SCALE_FACTOR), int(SQUARE_SIZE * PIECE_SCALE_FACTOR)),
    ),
}
