# Every piece has a type, value, and belongs to a player
class Piece():

    def __init__(self, type, value, player):
        self.type = type
        self.value = value
        self.player = player

    # Each piece has its own rules for legal moves
    def move(self, start, end):
        pass

    # String representation of each piece
    def __str__(self):
        return f"{self.type} ({self.player[0]})"

class Pawn(Piece):

    def __init__(self, player):
        super().__init__("Pawn  ", 1, player)

    def move(self, start, end):
        pass

class Rook(Piece):

    def __init__(self, player):
        super().__init__("Rook  ", 5, player)

    def move(self, start, end):
        pass

class Knight(Piece):

    def __init__(self, player):
        super().__init__("Knight", 3, player)

    def move(self, start, end):
        pass

class Bishop(Piece):

    def __init__(self, player):
        super().__init__("Bishop", 3, player)

    def move(self, start, end):
        pass

class Queen(Piece):

    def __init__(self, player):
        super().__init__("Queen ", 10, player)

    def move(self, start, end):
        pass

class King(Piece):

    def __init__(self, player):
        super().__init__("King  ", 1000, player)

    def move(self, start, end):
        pass
