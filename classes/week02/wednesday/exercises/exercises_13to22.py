
from classes.week00.second_class.utils import clear_screen
'''
#13 - Conditional Logic
Ask the user for a number and print whether it is positive, negative, or zero.
'''
txt = "please enter a number: "
while True:
    try:
        num = int(input(txt))
        i = 1
        while i < 6:
            print(i)
    except ValueError:
        txt = "a number: "
        


#MY CODE
txt = "please enter a number: "
x = int(input(txt))
if x > 0:
    print("number is positive")
elif x < 0:
    print("number is negative")
else:
    print("number is zero")


pause=input('pause')
clear_screen()

'''
#14 - Even/Odd Check
Ask the user for a number and print if it is even or odd.
'''

txt = "input a number: "
x = int(input(txt))
if x % 2 == 0:
    print("number is even")
else:
    print("number is odd")


pause=input('pause')
clear_screen()

'''
#15 - Boolean Operators
Ask the user for two numbers and check if both are positive, either is positive, or none is positive.
'''
txt = "input number: "
x = int(input(txt))
if x > 0:
    print("number is positive")
elif x < 0:
    print("number is negative")
else:
    print("number is neither positive or negative")

txt = "input number: "
y = int(input(txt))
if y > 0:
    print("number is positive")
elif y < 0:
    print("number is negative")
else:
    print("number is neither positive or negative")


pause=input('pause')
clear_screen()

'''
#16 - For Loop
Print all numbers from 1 to 20, skipping multiples of 3.
'''
for i in range(0,22,3):
    print(i)

pause=input('pause')
clear_screen()

'''
#17 - While Loop
Ask the user to guess a secret number (hardcoded) until they get it right.
'''

txt = "Guess the secret number! "
y = 5
x = int(input(txt))
while x == y:
    print("Congrats! You did it!")
else:
    print("Oops try again!")

pause=input('pause')
clear_screen()

'''
#18 - Break / Continue
Print numbers 1-10 but stop printing when you reach 7 and skip 3.
'''
for i in range(0,11):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)


pause=input('pause')
clear_screen()

'''
#19 - Function Definition
Write a function square(x) that returns the square of a number and test it.
'''
txt = "enter number: "
x = int(input(txt))
y = x**2
print(y)

pause=input('pause')
clear_screen()

'''
#20 - Function with Mutable Argument
Write a function add_item(lst, item) that appends item to lst and observe the effect on the original list.
'''
# enter code here



pause=input('pause')
clear_screen()

'''
#21 - Comments / Documentation
Write a function greet(name) with single-line and multi-line comments explaining each step.
'''
# enter code here



pause=input('pause')
clear_screen()

'''
#22 - Combining Tools
Ask the user to enter 5 names. Store them in a list, capitalize each name, sort the list, and print it.
'''
# enter code here



pause=input('pause')
clear_screen()

