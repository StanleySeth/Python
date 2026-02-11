#Python Modules
#A python module is a file that contains python definitions, statements and/or funcions

def add():
    num1 = 20
    num2 = 30
    sum = num1 + num2
    print("The answer is", sum)

def subtract():
    x = 45
    y = 30
    difference = x - y
    print("The answer is", difference)

def rectangulrarea():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    
    area = length * width
    print("The answer is", area)

#The above functions can be called in another file