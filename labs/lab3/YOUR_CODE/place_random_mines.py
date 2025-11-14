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
        
        c = random.randint (0, COLS-1)

        
        if board [r][c] == ():
            board [r][c] = ('*', '+')
            placed += 1
    
    
    return board
