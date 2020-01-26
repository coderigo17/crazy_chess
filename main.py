# This file will eventually launch the game

import Board
import Pieces

board = Board.Board()
print(board)
board.make_move((7, 1), (5, 2))
print(board)
board.make_move((0, 1), (2, 2))
print(board)
board.make_move((5, 2), (4, 0))
print(board)
board.make_move((2, 2), (6, 6)) # should ignore
print(board)
board.make_move((2, 2), (4, 3))
print(board)
