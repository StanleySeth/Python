#Boolean - This is datatype that evaluates either true or false

israining = False
print(israining)
print(type(israining))

paidloan = True
print(paidloan)
print(type(paidloan))

#Comparison operators: They are used to compare two or more statements and they usually return a boolean answer 

number1 =  2
number2 = 5

print("Is number1 greater than number2?", number1 > number2)
print("Is number1 less than number2?", number1 < number2)
print("Is number1 greater than or equal to number2?", number1 >= number2)
print("Is number1 less than or equal to number2?", number1 <= number2)
print("Is number1 equal to number2?", number1 == number2)
print("Is number1 not equal to number2?", number1 != number2)
print("====================================")
#Logical operators
#Logical AND
#It returns if and only if the condition/statements evaluates to true
print((3 > 1) and (7 > 6))

#Logical OR
#It evaluates to true if one of the statement/conditions is true
print((3 > 1) or (7 > 6) or (10 > 5))

#Logical NOT
#It is used to negate a statement/codition
print(not(90 > 70))