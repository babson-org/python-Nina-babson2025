#Initialize Boards#
#Create 3D list (rows and cols) filled with blanks for both base board and player board
initialize_board = [
    [["+" for _ in range(cols)] for _ in range(rows)],  # Layer 0 = player board
    [[" " for _ in range(cols)] for _ in range(rows)]   # Layer 1 = hidden (mine) board
]

rows, cols = 5,5 #hard code 5x5 grid
board = initialize_board(rows, cols)


# Base board: contains mines and numbers
from place_random_mines import place_random_mines
base_board = board[1]


#base_board = initialize_board(rows=5, cols=5)  # Layer 1 board with mines
#place_random_mines(base_board, num_mines=5)     # Layer 0 board with hidden mines (player board)
#print(base_board)

# Player board: what the user sees (hidden cells)
#player_board = initialize_board(rows=5, cols=5, fill="+")
player_board = board[0]

print(board)