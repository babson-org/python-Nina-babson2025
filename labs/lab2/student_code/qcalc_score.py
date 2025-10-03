def calc_score(board: list[int]):
    """
        Determines if there's a winner on the board.
        Returns 30 if X wins, -30 if O wins, 0 otherwise.
         
        there are 8 ways to win: 3 rows, 3 columns, 2 diagnols
        if the cells in a row, column or diagnol add up to 30 return 30
        if they add upto -30 return -30
        else return 0
    """
    total = board[a] + board[b] + board[c]
    def line_sum(a, b, c):
        '''
            line_sum takes 3 numbers and if the sum is either 30
            or -30 returns that sum otherwise do not return
        '''         
         
        # TODO: Sum the values at board[a], board[b], board[c]
        # Sum player's turn1, turn2, turn3
        # Sum computer's turn1, turn2, turn3

    if total == 30:
        return 30
    elif total == -30:
        return -30
    return None


        # TODO: Return 30 if X wins, -30 if O wins otherwise do not return
pass
     
    # TODO: For each of the 8 ways to win
    # 8 if stmts?
    # Each possible turn/outcome
winning_line = [
    (0,1,2),
    (3,4,5),
    (6,7,8),
    (0,3,6),
    (1,4,7),
    (2,5,8),
    (0,4,8),
    (2,4,6),]


    # TODO: Check the cells in each row, column, or diagonal using line_sum    
    # TODO: Return 0 if line_sum() didn't return 30 or -30
for a,b,c in winning_line:
    result = line_sum(a,b,c)
if result is not None:
    return result
if line_sum != 30 or -30:
    return 0

pass