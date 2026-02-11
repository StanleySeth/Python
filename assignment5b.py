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
