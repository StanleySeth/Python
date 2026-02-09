#Python While Loop.
#While loop executes a block of code repeatedly as long as a certain condition is true. The syntax of a while loop in python is as follows:

"""
Initialization of a variable
while keyword,
foolowed by the condition/statement to be evaluated.
followed by a full colon(:),
code to be printed,
increment/decrement
"""

number = 0
while number < 8:
    print("Hello There", number)
    number = number + 1

print('==============================')
# create a python program that prints the even numbers from 50 to 70 using while loop
num = 50
while num < 71:
    print(num)
    num = num + 2

#Below is a decrement example
print('==============================')
num = 200
while num >= 150:
    print(num)
    num = num - 3