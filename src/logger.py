import chess
import chess.pgn

import sys

# Specify the path to the local library/module
library_path = "/Users/littlecapa/GIT/python/stack/src"

# Add the library path to the system path
sys.path.append(library_path)

from stack import Stack

class Move_Logger:

  def __init__(self, board):
    self.game = chess.pgn.Game()
    self.game.setup(board)
    self.start_halfmove_number = 2*board.fullmove_number
    if board.turn == chess.WHITE:
      self.start_halfmove_number -= 1
    
    self.node_stack = Stack()
    print(self.start_halfmove_number)

  def make_move(self, move):
    move = str(move)
    if self.node_stack.is_empty():
      node = self.game.add_variation(chess.Move.from_uci(move))
    else:
      node = self.node_stack.top().add_variation(chess.Move.from_uci(move))
    self.node_stack.push(node)

  def add_eval(self, eval):
    self.node_stack.top().comment = "Eval: " + str(eval)

  def take_move_back(self):
    self.node_stack.pop()

  def get_pgn(self):
    return str(self.game)