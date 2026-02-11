# create a python program that prints the leap years in between 2000 and 2024
for year in range(2000, 2025):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
     print(year, "is a leap year")
    else:
        print(year, "is NOT a leap year")

# Using a While Loop Print from 20 to 1 
N = 20
while N >= 1:
    print(N)
    N = N - 1

#2. Create a List of Colors Blue, Green, Red, Pink , Black- Using a for Loop, Loop through the Colors
colors = ["Blue", "Green", "Red", "Pink", "Black"]
print(colors)
print(type(colors))

print("=========================================================")

for c in colors:
    print(c)