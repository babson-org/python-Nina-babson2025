from classes.week00.second_class.utils import clear_screen
'''
# 1

Write down the steps a program would need to make a cup of tea. Then implement a Python 
function make_tea() that prints each step.
'''
def make_tea():
    steps = ["1.Boil water",
             "2.Place tea a mug",
             "3.Pour water into mug",
             "4.Let tea sit in water for two minutes",
             "5.Remove tea bag",
             "6.Add personalized extras if desired and enjoy"
    ]

make_tea(steps)
print(steps)


pause=input('pause')
clear_screen()
'''
#2

Given a list [2, 4, 6, 8, 10], write a program that prints the next three numbers in the list.  
(the ones after 10)
'''
for i in range(0, 17, 2):
    print(i)

pause=input('pause')
clear_screen()
'''
#3

Write a program that asks the user for their first and last name, then prints a greeting:
"Hello, <first name> <last name>!"
'''
def greet_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    #first_name = first_name.capitalize() #These lines just capitalize the first and last name
    #last_name = last_name.capitalize()
    print(f"Hi {first_name} {last_name}")

greet_user()


pause=input('pause')
clear_screen()
'''
#4
#UNFAIR QUESTION!!
Write a program that prints your Python version and platform using the sys and platform modules.
'''
import sys
import platform
import pprint

#pprint.pprint(dir(sys))
#See what is in sys

#print.(type(sys.version))
#See what type sys is -> string

#pprint.pprint(dir(sys))
print(type(sys.version))
print(sys.version, sys.platform)

pause=input('pause')
clear_screen()
'''
#5

Ask the user to input two numbers. Calculate and print their sum, difference, product, 
and division (both / and //).
'''
txt = "please enter an integer: "
while True:
    try:
        x = int(input(txt))
        break
    except ValueError:
        txt = "follow directions, enter a number"

txt = "please enter an integer: "
while True:
    try:
        y = int(input(txt))
        break
    except ValueError:
        txt = "follow directions, enter a number"

total = x + y
diff = x - y
prod = x * y
div = x / y
flr = x // y

print(total, diff, prod, div, flr)

pause=input('pause')
clear_screen()
'''
#6

Ask the user to input a sentence. Print it in uppercase, lowercase, with the first letter 
capitalized, and split it into words.
'''
txt = input("please enter some text: ")
print(txt.upper()) #All caps
print(txt.lower()) #all lowercase
print(txt.capitalize()) #First letter of sentence is caps
print(txt.split()) #split by word (default is space - but can split by letter in ""


pause=input('pause')
clear_screen()
'''
#7

Calculate the result of the following without parentheses and then with parentheses:
10 + 2 * 5 / 2 - 3 ** 2
'''
print(10 + 2 * 5 / 2 - 3 ** 2) # = 6

x = (10 + 2 * 5) / (2 - 3 ** 2) # = -2.86
print(x)

#Exponents calculate right to left!!
x = 2**3**2 # = 512 NOT 64
print(x)

print(x)

x = 2**3**2
print(x)
pause=input('pause')
clear_screen()
'''
#8

Create a list of your three favorite foods. Replace the second item with a new one, 
then print the list.
'''
myList = ["ice cream, berries, cake"]
myList[1] = "pineapple"
print(myList)


pause=input('pause')
clear_screen()
'''
#9

Create a tuple with four numbers. Try to change the first number (observe the error) 
and then print the tuple.
'''
# enter your code here


pause=input('pause')
clear_screen()
'''
#10

Create a dictionary representing a student (name, age). Update the age. Create a list of 
favorite numbers and add a new number.
'''
# enter your code here


pause=input('pause')
clear_screen()
'''
#11

Ask the user to input their favorite quote. Save it to a file quotes.txt 
and read it back to print it.
'''
quote = input("enter your fav quote: ")
with open("quote.txt", "w") as f:
    f.write(quote)
with open("quote.txt", "r") as f:
    saved_quote = f.read()
print("Your quote: ", saved_quote)


pause=input('pause')
clear_screen()
'''
#12
Ask the user to input 5 numbers (one at a time), store them in a list, and print the sum and average.
'''
# enter your code here


pause=input('pause')
clear_screen()