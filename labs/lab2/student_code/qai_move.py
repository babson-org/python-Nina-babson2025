def ai_move(board: list[int]):
    """
        Simple AI that selects the first available cell.
        Remember board is a list that starts with items 1 - 9
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        after two moves with X choosing 1 and O choosing 5 the board looks like:
        [10, 2, 3, 4, -10, 6, 7, 8, 9]
        
        so in this case your function should return 2
    """
    # TODO: Loop through board
    # Create board and identify who is player and computer
    # Make sure computer knows how to react to player input - how does computer know need three in a row
board = [str(i) for i in range(1, 10)]
def create_board(board):
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print(f"{board[6]} | {board[7]} | {board[8]}")

create_board(board)

    # TODO: Find the first index where abs(cell) != 10
    # Loop to correlate user input to grid

    # TODO: Return that index as the AI's move
    # Where is computer putting next move
    # Print computer output, "Your turn"
    # Have outputs correlate to grid (make sure x/o changing on grid)
    
    pass