#Initialize Boards#
from place_random_mines import place_random_mines
#Create 3D list (rows and cols) filled with blanks for both base board and player board using 0 and 1
ROWS, COLS = 5,5 #hard code 5x5 grid

def initialize_board():
    '''
    initialize_board = [
    (["+" for _ in range(COLS)] for _ in range(ROWS)),
    ([" " for _ in range(COLS)] for _ in range(ROWS)) ]
    '''
    board = []
    for row in range(ROWS):
        board.append([])
        for col in range(COLS):
            board[row].append(())


    board = place_random_mines(board, 5)
    

           
            
    print(board)
    exit
    return board

# Base board: contains mines and numbers
'''
    base_board = initialize_board(ROWS, COLS) #Creates board with mines
    place_random_mines(base_board, num_mines)
    player_board = initialize_board(ROWS, COLS, fill= "+") 
'''


# Player board: what the user sees (hidden cells)
#player_board = initialize_board(rows=5, cols=5, fill="+")
##player_board = initialize_board(base_board,1)


#base_board = initialize_board(rows=5, cols=5)  # Layer 0 board with mines
#place_random_mines(base_board, num_mines=5)     # Layer 1 board with hidden mines (player board)

#print(initialize_board)