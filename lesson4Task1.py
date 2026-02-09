# create a python program that prints the leap years in between 2000 and 2024
for year in range(2000, 2025):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
     print(year, "is a leap year")
    else:
        print(year, "is NOT a leap year")