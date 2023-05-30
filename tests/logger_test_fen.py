import sys
sys.path.append('..')

from src.logger import Move_Logger

import chess
import chess.pgn


# Create a new chess board
board = chess.Board()

# Make some moves
board.push_san("e4")  # White's move
board.push_san("e5")  # Black's move
board.push_san("Nf3") # White's move

# Create a new board with the current position
game = chess.Board(board.fen())
ml = Move_Logger(game)

ml.make_move("b8c6")
ml.make_move("f1b5")
ml.add_eval(0.1)
ml.take_move_back()

ml.make_move("f1c4")
ml.add_eval(0.2)

print (ml.get_pgn())

FEN ="rnb1k2r/p5pp/2pq4/1p1p4/4p1nK/1B2P3/PPPP1PP1/RNBQ1R2 b - - 5 13"
game = chess.Board(FEN)
ml = Move_Logger(game)

ml.make_move("h8g8")