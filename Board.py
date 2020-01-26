import Pieces

class Board():

    def __init__(self):
        self.board = [["----------"]*8 for i in range(8)]
        self.game_over = False
        self.players = ["White", "Black"]
        self.turn = 0 # even turn -> white, odd turn -> black
        self.set_up_pieces()

    # Setting up the board for a new game
    def set_up_pieces(self):
        self.board[0] = [
                         Pieces.Rook(self.players[1]),
                         Pieces.Knight(self.players[1]),
                         Pieces.Bishop(self.players[1]),
                         Pieces.Queen(self.players[1]),
                         Pieces.King(self.players[1]),
                         Pieces.Bishop(self.players[1]),
                         Pieces.Knight(self.players[1]),
                         Pieces.Rook(self.players[1])
                         ]
        self.board[1] = [Pieces.Pawn(self.players[1]) for _ in range(8)]
        self.board[6] = [Pieces.Pawn(self.players[0]) for _ in range(8)]
        self.board[7] = [
                         Pieces.Rook(self.players[0]),
                         Pieces.Knight(self.players[0]),
                         Pieces.Bishop(self.players[0]),
                         Pieces.Queen(self.players[0]),
                         Pieces.King(self.players[0]),
                         Pieces.Bishop(self.players[0]),
                         Pieces.Knight(self.players[0]),
                         Pieces.Rook(self.players[0])
                         ]

    def make_move(self, start, end):
        """start and end are tuples referring to board positions: (row, column)"""
        # Determine whose turn it is
        player = self.players[self.turn % 2]

        # Ensure the player is actually trying to move one of their pieces on the board
        if (start[0] < 0 or start[0] > 7 or start[1] < 0 or start[1] > 7
                or end[0] < 0 or end[0] > 7 or end[1] < 0 or end[1] > 7
                or self.board[start[0]][start[1]] == "----------"
                or self.board[start[0]][start[1]].player != player):
            return

        # Determine which piece the player is trying to move
        piece = self.board[start[0]][start[1]]

        # Each piece has a particular moveset...
        move = (end[0] - start[0], end[1] - start[1])
        if piece.type == "Pawn  ":
            pass
        elif piece.type == "Rook  ":
            pass
        elif piece.type == "Knight":
            # Determine whether move attempt is a legal knight move
            m = (abs(move[0]), abs(move[1]))
            if m != (2, 1) and m != (1, 2):
                return

            # Determine whether move endpoint is open
            if (self.board[end[0]][end[1]] != "----------"
                    and self.board[end[0]][end[1]].player == player):
                return
            elif self.board[end[0]][end[1]] != "----------":
                pass # TODO: handle the case where an opponent's piece is captured
            else:
                self.board[start[0]][start[1]], self.board[end[0]][end[1]] = \
                self.board[end[0]][end[1]], self.board[start[0]][start[1]]

        elif piece.type == "Bishop":
            pass
        elif piece.type == "Queen ":
            pass
        elif piece.type == "King  ":
            pass

        self.turn += 1

    # String representation of the board
    def __str__(self):
        s = "\n\n"
        for row in self.board:
            for col in row:
                s += f"{str(col)} "
            s += "\n\n"
        return s
