# ==============================
# Main Program
# ==============================
def main():
    while True:
        print("Lab 1 - Python Basics")
        print("1. Draw Diamond")
        print("2. Text Analysis")
        print("3. Caesar Cipher")
        choice = input("Select part to run (1-3): ")
        
        if choice == "1":
            draw_diamond()
        elif choice == "2":
            text_analysis()
        elif choice == "3":
            caesar_cipher()
        else:
            exit()

"""
Lab 1 - Python Basics
Author: Nina Krishna
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""

# ==============================
# Part 1: Draw a Diamond
# ==============================
def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric diamond of that height.
    """

    # TODO: Prompt user for an odd number

    # TODO: Draw the top half of the diamond

    # TODO: Draw the bottom half of the diamond
# Uncomment to test Part 1
# ============MY COMPUTATIONAL THINKING ======================
### Ensure user inputs an odd number ###
# 




# =============== MY CODE ===========================
# draw_diamond()
### Ensure user inputs an odd number and define height ###
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
middle = height//2

# Setting spacing before and between stars - middle+1 makes sure formatting is mirrored longitudinally#
for idx in range (middle, -1, -1):
    before = " "*idx
    between = " " * ((middle-idx)*2-1)
    if (middle-idx*2-1 == -1):
        print(before+"*")
    else:
        print(before + "*" + between + "*")

### Bottom half of code ###
for idx in range (1, middle+1 ):
    before = " " * idx
    between = " " * ((middle-idx)*2-1)
    if (middle-idx*2-1 == -1):
        print(before+"*")
    else:
        print(before + "*" + between + "*")

# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
### Type out actual steps of what im gonna do, what functions, any exceptions, etc ###

def text_analysis():
    """
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """
    print("you have some work todo!, text_analysis")

    # TODO: Get user input
    text = input("Enter some text: ")

    # TODO: Count letters
    letters = 0

    # TODO: Count words

    # TODO: Count sentences

    # TODO: Print the results
    print(f"Letters: {letters}")
    print(f"Words: {0}")        # replace 0
    print(f"Sentences: {0}")    # replace 0
# Uncomment to test Part 2
# text_analysis()
# ============MY COMPUTATIONAL THINKING ======================





# =============== MY CODE ===========================
### Letters starts at 0, words starts at 1 since the last word in sentence doesn't get counted, sentences is 0 ###
letters = 0
words = 1
sentences = 0

### txt = "nina actually enter text and test" ###
txt = input("enter text").strip()
for char in txt:
    if char.isalpha(): letters += 1
    elif char == " ": words += 1
    elif char in (".", "!", "?"): sentences += 1

# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """

    print("you have some work todo!, caesar_cypher")

    # TODO: Get user input text
    text = input("Enter text: ")

    # TODO: Get shift value
    shift = int(input("Enter shift value (integer): "))

    # TODO: Ask user whether to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    # TODO: Implement encryption and decryption logic
    result = ""

    # TODO: Print the final result
    print("Result:", result)

# Uncomment to test Part 3
# caesar_cipher()
# ============MY COMPUTATIONAL THINKING ======================
### What is the caesar cipher - give explanation and usage ###




# ================= MY CODE =============================
### Create an array called alpha that has whole lowercase alphabet --> always shifting left ###
text = input("Enter a message you want to encrypt:")
alphabet = []
for idx in range(97, 97+26):
    alphabet.append(chr(idx))   #append adds stuff to the end of the list
print(alphabet)

### Create shifted alphabet where user enters shift ###
shift = int(input("Enter shift:"))

#check that 0 < int < 26 --> 26 shifts alphabet all the way back to square 1
shifted_alphabet = [None] * 26

result = ""
for char in text:
    for char in alphabet:
        idx = alphabet.index(char)
        new_idx = (idx-shift)%26
        result += shifted_alphabet[new_idx]
    else:
        encrypt += char



if __name__ == "__main__":
    main()