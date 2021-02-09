# Minimax AI Game Algorithm

Gomoku game AI player implementation using minimax adversarial algorithm. 
In this project I have implemented an AI player to play Gomoku strategically on a reduced board (10 x 10). 

If you are not familiar with Gomoku but know about Four-Connect or Tic-Tac-Toe, you can view Gomoku as a variant of those two games. Besides the number of checkers required to form a line to win, the differences between Gomoku and the Four-Connect is that you can place your checker anywhere on the Gomoku board instead of stacking them. Compared to Tic-Tac-Toe, the Gomoku has a wider board and thus more complicated.

1) Intialize two players:

```
>>>joe = Player('X')
>>>dummy = RandomPlayer('O')
```
  
2) Start the game:

```
>>>gomoku(joe, dummy)
```

```
Welcome to Gomoku!

| | | | | | | | | | | 0
| | | | | | | | | | | 1
| | | | | | | | | | | 2
| | | | | | | | | | | 3
| | | | | | | | | | | 4
| | | | | | | | | | | 5
| | | | | | | | | | | 6
| | | | | | | | | | | 7
| | | | | | | | | | | 8
| | | | | | | | | | | 9
-----------------------
 0 1 2 3 4 5 6 7 8 9

Player: X's turn
Enter a position: 
```

3) Joe input the coordinates of her first step: 4 5 (Note that the input row and column is separated by whitespace.)
Dummy put its checker "O" randomly at 6 5

```
Enter a position: 4 5

| | | | | | | | | | | 0
| | | | | | | | | | | 1
| | | | | | | | | | | 2
| | | | | | | | | | | 3
| | | | | |X| | | | | 4
| | | | | | | | | | | 5
| | | | | | | | | | | 6
| | | | | | | | | | | 7
| | | | | | | | | | | 8
| | | | | | | | | | | 9
-----------------------
 0 1 2 3 4 5 6 7 8 9
```

```
Player: O's turn

| | | | | | | | | | | 0
| | | | | | | | | | | 1
| | | | | | | | | | | 2
| | | | | | | | | | | 3
| | | | | |X| | | | | 4
| | | | | | | | | | | 5
| | | | | |O| | | | | 6
| | | | | | | | | | | 7
| | | | | | | | | | | 8
| | | | | | | | | | | 9
-----------------------
 0 1 2 3 4 5 6 7 8 9

```

```
Player: X's turn

Enter a position: 
```

4) Joe and Dummy place their checkers alternatingly until there is a winner or the board being full (tie).

Example of end of game:  

```
Player: X wins in 5 moves.
Congratulations!
| | | | | | | | | | | 0
| | | | | | |O| | | | 1
| | | | | | | | | | | 2
| | | | | | | | | | | 3
| | | |X|X|X|X|X| | | 4
| | | | | | |O| | | | 5
| | | | | |O| | | | | 6
| | | |O| | | | | | | 7
| | | | | | | | | | | 8
| | | | | | | | | | | 9
-----------------------
 0 1 2 3 4 5 6 7 8 9
 ```
