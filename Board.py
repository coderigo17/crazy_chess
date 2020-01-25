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
                         Pieces.Rook("Black"),
                         Pieces.Knight("Black"),
                         Pieces.Bishop("Black"),
                         Pieces.Queen("Black"),
                         Pieces.King("Black"),
                         Pieces.Bishop("Black"),
                         Pieces.Knight("Black"),
                         Pieces.Rook("Black")
                         ]
        self.board[1] = [Pieces.Pawn("Black")]*8
        self.board[6] = [Pieces.Pawn("White")]*8
        self.board[7] = [
                         Pieces.Rook("White"),
                         Pieces.Knight("White"),
                         Pieces.Bishop("White"),
                         Pieces.Queen("White"),
                         Pieces.King("White"),
                         Pieces.Bishop("White"),
                         Pieces.Knight("White"),
                         Pieces.Rook("White")
                         ]

    # String representation of the board
    def __str__(self):
        s = "\n\n"
        for row in self.board:
            for col in row:
                s += f"{str(col)} "
            s += "\n\n"
        return s
