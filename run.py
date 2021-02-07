from pa2_gomoku import Player, RandomPlayer
from pa2_process import gomoku
from pa2 import AIPlayer 

#Juan = RandomPlayer('X')
opp = AIPlayer('O')
Juan = Player('X')

#gomoku(Juan, opp)
gomoku(opp, Juan)