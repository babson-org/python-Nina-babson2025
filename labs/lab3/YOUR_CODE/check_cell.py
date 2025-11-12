#Check if cell has mine
#Return True if cell has a mine
def check_cell(board, ROW, COL):
    if 0 <= ROW < len(board) and 0 <= COL < len(board[0]):
        return board[ROW][COL] == globals.MINE
    return False