# Player inputs their choice
# Choice is reflected on the board (replaced instead of the cell number)

def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    
    prompt = "Select an empty cell (1-9): "
    while True:
        try:
            # TODO: Convert input to integer
            move = int(input(prompt)) - 1 # -1 because we want the number input to match the number on the board (not the index)
            if move < 0 or move > 8:
                prompt = "Invalid input, try again - Select a number 1-9"
            # TODO: Validate move is in range and not taken
            if abs(board[move]) == 10:
                prompt = "That spot has already been selected, try again - Select a number 1-9"
                continue

            # TODO: Assign score['player'] to the selected cell on the board
            board[move] = score["player"]
            break
        
        except ValueError:
            prompt = "Invalid input. Try again (1-9): "

pass