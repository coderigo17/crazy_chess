# Every piece has a type, value, and belongs to a player
class Piece():

    def __init__(self, player, type, value):
        self.player = player
        self.type = type
        self.value = value

    # String representation of each piece
    def __str__(self):
        return f"{self.type} ({self.player[0]})"

class Pawn(Piece):

    def __init__(self, player):
        super().__init__(player, "Pawn  ", 1)

class Rook(Piece):

    def __init__(self, player):
        super().__init__(player, "Rook  ", 5)

class Knight(Piece):

    def __init__(self, player):
        super().__init__(player, "Knight", 3)

class Bishop(Piece):

    def __init__(self, player):
        super().__init__(player, "Bishop", 3)

class Queen(Piece):

    def __init__(self, player):
        super().__init__(player, "Queen ", 9)

class King(Piece):

    def __init__(self, player):
        super().__init__(player, "King  ", 1000)
