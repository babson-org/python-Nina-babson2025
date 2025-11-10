#Run Minesweeper Game (hopefully)#

from initialize_board import initialize_board
from mines import place_random_mines
from print_board import print_board
from update_board import update_board
from get_valid_input import get_valid_input
from game_over import game_won

def play_minesweeper():
    print(" Welcome to the Minesweeper Game - Try tp uncover all the cells without digging up a mine. If you hit a mine, you lose! If you can uncover all the cells without hitting a mine, you win! Use the surrounding cells as hints...good luck.")
    rows = int(input("Enter a number 1-5 for your row: ")) #Choose Row
    cols = int(input("Enter a number 1-5 for your columns: ")) #Choose Cols
    num_mines = int(input("Enter number of mines: "))

    base_board = initialize_board(rows, cols) #Creates board with mines
    place_random_mines(base_board, num_mines)
    player_board = initialize_board(rows, cols, fill= "+") #Hides mines for player board

    while True:
        print_board(player_board)
        r, c = get_valid_input(rows, cols)

        hit_mine = update_board(base_board, player_board, r, c) #Game Lost
        if hit_mine:
            print_board(base_board)
            print("💥 You hit a mine! Game over.") 
            break

        if game_won(base_board, player_board): #Game Wom
            print_board(player_board)
            print("🎉 You win! All safe cells revealed.")
            break
