import globals


def print_board(board: list, level: int):

    board = [
        [(' ♦', '💣'), (' ♦', '💣'), (' ♦', 1),
         (' ♦', '   '), (' ♦', '   '), (' ♦', '   ')],
        [(' ♦', 2), (' ♦', 2), (' ♦', 1),
         (' ♦', '   '), (' ♦', '   '), (' ♦', '   ')],
        [(' ♦', '   '), (' ♦', '   '), (' ♦', '   '),
         (' ♦', '   '), (' ♦', '   '), (' ♦', '   ')],
    ]

    level = 0 #resets the level to 0 and will always print the first item of each tuple

    line_hash = '|-----'

    print('      ', end='')
    for idx in range(globals.COLS): #prints column headers
        print(f'   {idx}  ', end='') #spaces for alignment

    print(f'\n      {line_hash * globals.COLS}|') 

    for row in range(globals.ROWS):
        print(f'  {row}   ', end='')
        for col in range(globals.COLS):
            symbol = board[row][col][level]

            if symbol == '💣':
                print(f'| {symbol:3}', end='')
            else:
                print(f'| {symbol:3} ', end='')
        print('|')

        print(f'      {line_hash * globals.COLS}|')


print_board([], 4)
