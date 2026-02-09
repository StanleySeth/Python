#Loops -> Sometimes we may need to do a piece of work a numbe of repeated items in such cases we may use loops.
#a loop is a control structure that allows us to execute a block of code repeatedly until a certain condition is met.
# There are two types of loops in python i.e While and For loops

#Below is the syntax of a for loop in python
"""
for variable in range(n)
    #block of code to be executed
"""

for greeting in range(10):
    print("Hello There", greeting)
print("==================================")

for number in range(10, 21):
    print(number)

print("====================================")
#Find the even numbers in the range of 50 to 71

for number in range(50, 71, 3):
    print(number)

print("====================================")
#Create a python program that prints the odd numbers from 100 to 150

for number in range(101, 150, 2):
    print(number)

    print("====================================")
#Create a python program that prints the multiples of 3 starting from 201 to 150

for number in range(201, 149, -3):
    print(number)

print("====================================")
