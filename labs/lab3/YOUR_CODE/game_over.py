#Both functions for game over

#Game Won#
#Player selected all cells that do not have a mine
#Return True if all non-mine cells have been revealed

from globals import HIDDEN, MINE

def game_won(base_board, player_board):
    for r in range(len(base_board)):
        for c in range(len(base_board[0])):
            if base_board[r][c] != MINE and player_board[r][c] == HIDDEN:
                return False
    return True

#Game Lost#
#Player selected a mine
#Check if the player selected a cell containing a mine
#bool: True if the selected cell is a mine, otherwise False
from globals import MINE

def game_lost(base_board, row, col):
    return base_board[row][col] == MINE
