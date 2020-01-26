# Every piece has a type, value, and belongs to a player
class Piece():

    def __init__(self, player, position, type, value):
        self.player = player
        self.position = position
        self.type = type
        self.value = value

    # Each piece has its own rules for legal moves
    def move(self, target):
        pass

    # String representation of each piece
    def __str__(self):
        return f"{self.type} ({self.player[0]})"

class Pawn(Piece):

    def __init__(self, player, position):
        super().__init__(player, position, "Pawn  ", 1)

    def move(self, target):
        pass

class Rook(Piece):

    def __init__(self, player, position):
        super().__init__(player, position, "Rook  ", 5)

    def move(self, target):
        pass

class Knight(Piece):

    def __init__(self, player, position):
        super().__init__(player, position, "Knight", 3)

    def move(self, target):
        pass

class Bishop(Piece):

    def __init__(self, player, position):
        super().__init__(player, position, "Bishop", 3)

    def move(self, target):
        pass

class Queen(Piece):

    def __init__(self, player, position):
        super().__init__(player, position, "Queen ", 9)

    def move(self, target):
        pass

class King(Piece):

    def __init__(self, player, position):
        super().__init__(player, position, "King  ", 1000)

    def move(self, target):
        pass
