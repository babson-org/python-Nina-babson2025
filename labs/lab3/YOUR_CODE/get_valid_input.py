#Ask user for valid inputs for row and cell
def get_valid_input(rows, cols):
    while True:
        try:
            user_input = input("Enter row and column (a number 1-5)").split
            r,c = map(int, user_input)
            if 0 <= r < rows and 0 <= c < cols:
                return r,c
            else:
                print("Coordinates out of range - try again")
        except ValueError:
            print("Invalid input - please choose two integers between 1 and 5")
            

        