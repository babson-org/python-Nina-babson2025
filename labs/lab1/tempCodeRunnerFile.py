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