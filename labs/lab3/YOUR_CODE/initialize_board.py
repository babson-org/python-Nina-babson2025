#Initialize Boards#
#Create 2D list (rows and cols) filled with blanks for both base board and player board
def initialize_board(rows=5, cols=5, fill=" "):
    return [[fill for _ in range(cols)] for _ in range(rows)]


# Base board: contains mines and numbers
from labs.lab3.YOUR_CODE.place_random_mines import place_random_mines

base_board = initialize_board(rows=5, cols=5)  # Create empty board
place_random_mines(base_board, num_mines=5)     # Add 5 mines randomly
print(base_board)

# Player board: what the user sees (hidden cells)
player_board = initialize_board(rows=5, cols=5, fill="+")
