#Iitialize Boards#
#Create 2D list (rows and cols) filled with blanks for both base board and player board
def initialize_board(rows, cols, fill=" "):
    return [[fill for idx in range(rows)] for idy in range (cols)]

# Base board: contains mines and numbers
base_board = initialize_board(rows, cols)

# Player board: what the user sees (hidden cells)
player_board = initialize_board(rows, cols, fill="-")