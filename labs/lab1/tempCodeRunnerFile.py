while True:
    try:
        height = int(input("Enter an odd number: "))
        if height % 2 == 1: 
            break
        else:
            print("The number must be odd. Try again: ")
    except ValueError:
            print("Refer to directions, please try again")

### Top half of diamond ###
# Define middle of diamond parameters in terms of height #
middle = height//2  # // divides diamond laterally

# Setting spacing before and between stars - middle+1 makes sure formatting is mirrored longitudinally#
for idx in range (middle, -1, -1):
    before = " "*idx
    between = " " * ((middle-idx)*2-1)
    if (middle-idx)*2-1 == -1:
        print(before+"*")
    else:
        print(before + "*" + between + "*")

### Bottom half of code ###
for idx in range (1, middle+1):
    before = " " * idx
    between = " " * ((middle-idx)*2-1)
    if (middle-idx)*2-1 == -1:
        print(before+"*")
    else:
        print(before + "*" + between + "*")