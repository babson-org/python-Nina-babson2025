#Holds the following functions:
#place_random_mines
#check_mines

#Place Random Mines#
#Import tools necessary
import random
from globals import MINE

#Computer randomly chooses where to place mines for player
def place_random_mines(board,num_mines):
    rows = 5
    cols = 5
    placed = 0
    while placed < num_mines:
        r = random.randint(0, rows-1)
        c = random.randint (0, rows-1)
        if board [r][c] != MINE:
            board [r][c] = MINE
            place += 1

#Check if cell has mine
#Return True if cell has a mine
def check_cell():
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return board[row][col] == MINE
    return False
