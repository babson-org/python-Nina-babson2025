#Run Minesweeper Game (hopefully)#

from initialize_board import initialize_board
from place_random_mines import place_random_mines
from check_cell import check_cell
from print_board import print_board
#from update_board import update_board
from get_valid_input import get_valid_input
#from game_over import game_won

def play_minesweeper():

    board = initialize_board()

    print(" Welcome to the Minesweeper Game - Try tp uncover all the cells without digging up a mine. If you hit a mine, you lose! If you can uncover all the cells without hitting a mine, you win! Use the surrounding cells as hints...good luck.")
    ROWS = int(input("Enter a number 1-5 for your rows: ")) #Choose Row
    COLS = int(input("Enter a number 1-5 for your columns: ")) #Choose Cols
    num_mines = int(input("Enter number of mines: "))

   
'''
    while True:
        print_board(board, 1)
        r, c = get_valid_input(ROWS, COLS)

        hit_mine = update_board(base_board, player_board, r, c) #Game Lost
        if hit_mine:
            print_board(base_board)
            print("💥 You hit a mine! Game over.") 
            break

        if game_won(base_board, player_board): #Game Wom
            print_board(player_board)
            print("🎉 You win! All safe cells revealed.")
            break
'''
play_minesweeper()