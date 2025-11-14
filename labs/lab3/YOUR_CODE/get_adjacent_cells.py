#Checking cells around selected cell to show how many mines are nearby
def adjust_cell(r,c,ROWS,COLS):
    adj = []
    for idx in [-1, 0, 1]: #although in player board it will show up as positive integers, this tells base board where to go
        for idy in [-1, 0, 1]:
            if idx == 0 and idy == 0:
                continue
            new_r, new_c = r+idx, c+idy
            if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                adj.append((new_r, new_c))
    return adj