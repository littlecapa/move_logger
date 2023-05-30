import sys
sys.path.append('..')

from src.logger import Move_Logger

import chess
import chess.pgn


board = chess.Board()
ml = Move_Logger(board)

ml.make_move("d2d4")
ml.make_move("d7d5")
ml.make_move("c2c4")
ml.add_eval(0.7)
ml.take_move_back()

ml.make_move("g1f3")
ml.add_eval(0.6)
ml.take_move_back()

ml.make_move("c1f4")
ml.add_eval(0.3)
ml.take_move_back()
ml.take_move_back()

ml.make_move("g8f6")
ml.make_move("c2c4")
ml.add_eval(0.1)
ml.take_move_back()

ml.make_move("g1f3")
ml.add_eval(0.2)

print (ml.get_pgn())