#Update player board
#Reveal a cell. If blank (0 mines nearby), reveal neighbors recursively.
#Returns True if a mine was hit, otherwise False.

from globals import HIDDEN, BLANK, MINE
from get_adjacent_cells import get_adjacent_cells

def update_board(base_board, player_board, row, col):
    if base_board[row][col] == MINE:
        player_board[row][col] = MINE
        return True  # hit a mine

    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        if player_board[r][c] != HIDDEN:
            break
