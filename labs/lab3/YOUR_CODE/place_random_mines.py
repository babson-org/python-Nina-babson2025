#Holds the following functions:
#place_random_mines
#check_mines

#Place Random Mines#
#Import tools necessary
import random

#Computer randomly chooses where to place mines for player
def place_random_mines(board,num_mines):
    ROWS = 5
    COLS = 5
    placed = 0
    while placed < num_mines:
        r = random.randint(0, ROWS-1)
        c = random.randint (0, ROWS-1)
        if board [r][c] != globals.MINE:
            board [r][c] = globals.MINE
            placed += 1

#Check if cell has mine
#Return True if cell has a mine
def check_cell(board, ROW, COL):
    if 0 <= ROW < len(board) and 0 <= COL < len(board[0]):
        return board[ROW][COL] == globals.MINE
    return False
