#COMPUTATIONAL THINKING#
#Here is my thinking and breakdown of the puzzle

#Initialize board (give board parameters - hard code lack of user error)
    #player_board is user board (everything is diamond)
    #base_board is hidden mines board (everything is numbers or mines)

#Computer randomly places mines
    #mines.py containes funtions:
    #place_random_mines which places mines randomly (if not already there) places mines in base_board
    #check_cell checks if there is a mine present or not

#User input coordinates for row and column
    #use chooses integer 1-5 for row and column

#Check mine
    #check_cell checks if there is a mine already there

#re-print player_board for player to see new board

#check if game is lost or won
    #If the player chooses a cell with a mine, check_cell will see bomb and print "You Lost"
    #If the player chooses an open cell, the game will continue
    #If the player chooses all open cells (Hidden cells = # of mines) the game ends and prints "You Won"

#Questions for prof
#Change rows and cols to all caps
#fix the 3D board
#ROWS and COLS underlined