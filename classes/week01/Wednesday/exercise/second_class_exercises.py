
#1 print 'hello' 5 times using an arithmetic operator
print("hello "*5)

#2 print 'hello' 5 times using a loop
for i in range(0, 5):
  print("hello "*5)

#3 print 'hello' 5 times on the same line using a loop
for i in range(0, 5):
  print("hello "*5)

#4  using nested loops print the following:
'''
00 01 02
10 11 12
20 21 22

'''
for row in range(3):
    for col in range(3):
        print(str(row)+str(col), end = " ")
    print() #prints col
print() #prints row

#5 define txt and input some text from the keyboard into it
def txt():
   print("good morning")
print(txt())

#6 print each letter in txt
def txt():
   print("good morning")
print(txt())

for letter in txt():
  print(letter)



#7 assign the variable letter to the first letter in txt




#8 print out all the letters in txt that are equal to the first letter

'''
say txt = 'the cat in the hat was read today'
't' is the first letter

result: tttt
'''




'''
#9 suppose we had a list of n elements. create a new list that
  shifts the elements by 3

    myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
      shifted_list = ['pear', 'blueberry', 'peach', 'apple', 'orange']

        Hints:
             1) use len(), %, enumerate
             2) also assign shifted_list = [None] * length  (you'll need to determine 
                the length variable)
             3) shift inside the for loop
             4) print out the printed list outside the for loop
'''



                                    
                                    