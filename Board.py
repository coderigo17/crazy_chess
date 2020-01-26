import Pieces

class Board():

    def __init__(self):
        self.game_over = False
        self.turn = 0 # even turn -> white, odd turn -> black
        self.board = [["----------"]*8 for i in range(8)]
        self.set_up_pieces()

    # Setting up the board for a new game
    def set_up_pieces(self):
        self.board[0] = [
                         Pieces.Rook("Black", (0, 0)),
                         Pieces.Knight("Black", (0, 1)),
                         Pieces.Bishop("Black", (0, 2)),
                         Pieces.Queen("Black", (0, 3)),
                         Pieces.King("Black", (0, 4)),
                         Pieces.Bishop("Black", (0, 5)),
                         Pieces.Knight("Black", (0, 6)),
                         Pieces.Rook("Black", (0, 7))
                         ]
        self.board[1] = [Pieces.Pawn("Black", (1, i)) for i in range(8)]
        self.board[6] = [Pieces.Pawn("White", (6, i)) for i in range(8)]
        self.board[7] = [
                         Pieces.Rook("White", (7, 0)),
                         Pieces.Knight("White", (7, 1)),
                         Pieces.Bishop("White", (7, 2)),
                         Pieces.Queen("White", (7, 3)),
                         Pieces.King("White", (7, 4)),
                         Pieces.Bishop("White", (7, 5)),
                         Pieces.Knight("White", (7, 6)),
                         Pieces.Rook("White", (7, 7))
                         ]

    # String representation of the board
    def __str__(self):
        s = "\n\n"
        for row in self.board:
            for col in row:
                s += f"{str(col)} "
            s += "\n\n"
        return s
