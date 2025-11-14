#Update player board
#Reveal a cell. If blank (0 mines nearby), reveal neighbors recursively.
#Returns True if a mine was hit, otherwise False.

from globals import HIDDEN, BLANK, MINE
from get_adjacent_cells import get_adjacent_cells

def update_board(base_board, player_board, ROWS, COLS):
    if base_board[ROWS][COLS] == MINE:
        player_board[ROWS][COLS] = MINE
        return True  # hit a mine

    stack = [(ROWS, COLS)]
    while stack:
        r, c = stack.pop()
        if player_board[r][c] != HIDDEN:
            break
