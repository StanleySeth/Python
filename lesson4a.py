#Nested if Statements
#Is an if statement inside another if statement.

age = 20
weight = 60

if age > 15:
    if weight > 50:
        print("Can Donate Blood")
    else:
        print("Can't Donate blood because of your weight")
else:
    print("Can't Donate blood because of your age")