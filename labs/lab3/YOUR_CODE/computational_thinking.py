#COMPUTATIONAL THINKING#
#Initialize board (give board parameters - hard code lack of user error)
    #user_board is user board (everything is diamond)
    #base_board is hidden mines board (everything is numbers or mines)

#Computer chooses random mines
    #Random numbers
    #Count = 0
    #while count > x, col = rand.randint(0,globalcols-1)
    #print board

#User input coordinates for row and column
    #pop? stack.pop?
    #append coordinates to stack
    #

#user input

#Imports
#import globals
#import utils
#from initialize_board import initialize_board
#from print_board import print_board
#from game_over import game_over
#from get_validated_input import get_validated_input
#from is_bomb_at import is_bomb_at
#from update_board import update_board

def get_validated_input(txt1, txt2, low_int, high_int):
"""
Prompt the user for an integer input within a specified range.

Continuously prompts the user using `txt1` until a valid integer within
the range [`start`, `finish`] is entered. If the input is invalid,
`txt2` is shown in subsequent prompts until valid input is received.

Parameters:
txt1 (str) : Initial prompt message for user input.
txt2 (str) : Prompt message shown after invalid input.
low_int (int) : Minimum acceptable value (inclusive).
high_int (int): Maximum acceptable value (inclusive).

Returns:
int: A validated integer input from the user within the specified range.
"""
txt = txt1
while True:
    try:
        value = int(input(txt))
    if not (low_int <= value <= high_int): raise ValueError:
    break
except ValueError:
txt = txt2

return value
