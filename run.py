from gomoku import Player, RandomPlayer
from process import gomoku
from main import AIPlayer 

#Juan = RandomPlayer('X')
opp = AIPlayer('O')
Juan = Player('X')

#gomoku(Juan, opp)
gomoku(opp, Juan)
