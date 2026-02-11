#Qn 1: Function Without Parameters
#Create a function that:
#• Takes no parameters
#• Uses arithmetic operators to calculate the area of a rectangle
#• Prints the result

def Area():
    L = 20
    W = 10
    A = L * W
    print("The Area of the rectangle is: ", A)
Area()

#Qn 2: Function With Parameters
#Create a function that:
#• Accepts two numbers as parameters
#• Returns their sum, difference, product, and division

print("============================================================")
def N(x, y):
    sum = x + y
    difference = x - y
    product = x * y
    quotient = x / y
    print(f"The sum of the numbers is:", sum)
    print(f"The difference of the numbers is:", difference)
    print(f"The product of the numbers is:", product)
    print(f"The quotient of the numbers is:", quotient)
N(100,4)


#Qn 3: Control Statement (if...elif...else)
#Write a function that:
#• Accepts a number (use input function)
#• Checks whether the number is:
#• Positive
#• Negative
#• Zero

print("============================================================")
def Control():
    Number = int(input("Enter Number: "))
    if Number > 0:
        print("Positive")
    elif Number < 0:
        print("Negative")
    else:
        print("Zero")
Control()

#Qn 4: Loop with Arithmetic
#Write a function that:
#• Accepts a number n
#• Uses a for loop
#• Calculates the sum of numbers from 1 to n

def num(n):
    start = 0
    for loop in range(n+1):
         Total = start + loop
    return Total
       
print(num(1))

print("================================================")
#Qn 5: While Loop
#Write a function that:
#• Accepts a number (Use input() function)
#• Uses a while loop
#• Calculates the square of numbers from 1 up to that number

def square():
    z = int(input("Enter a number: "))
    
    n_square = 1
    while n_square <= z:
        print(n_square * n_square)
        n_square += 1

square()


