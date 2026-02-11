#PYTHON FUNCTIONS
# They are a block of code/statement that perform a given task/action. They can e used throughout the program to perform different tasks.
#Functions are defined using the def keyword. (define)
# There are two main types of functions i.e.
#1. IN-Built Functions -> They come preinstalled with the interpretor i.e print(), pop(), range(), append(), del()etc
#2. User defined functions => Are created by a programmer to solve a given task.

#To define functions you need to give it a name followed by a parenthesis.
#For the functions, it is usually indented and to invoke a function we use the function name.


def greetings():
    print("Hello There")
#The defined function will work only when it is called as follows;
greetings()
#Note: Indentation is used to define a code block. When calling a function Do Not indent.

print("=====================================================")
#Addition function      
def Addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is: ", sum)

Addition()

print("=====================================================")
# create a function that  is able to multiply three values
def Multiply():
    num3 = 3
    num4 = 5
    num5 = 2
    Product = num3 * num4 * num5
    print("The product of the numbers is: ", Product)

Multiply()

print("=====================================================")
#Division function      
def Divide():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    quotient = number1 / number2
    print("The quotient of the numbers is: ", quotient)

print("----")
for divide in range(5):
    Divide()

