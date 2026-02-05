# Python lists
# A list in python is a collection of items that are ordered in a certain way
# A list is introduced by the use of the square brackets[].
#The items of a list are stored inside of indexes. Note: In programming we start counting from index Zero(0)
# A list is mutable i.e the contents of a list can be changed.

cars = ["BMW", "Benz", "hiance", "Prado", "Probox", "Mazda", "Mclaren"]
print(cars)
print(type(cars))

#Accessing items of a list
print(cars[2])
print("The car on index four is: ", cars[4])
#List slicing - This is creating a list from a given bigger list
print(cars[4:])

#printing from index zero ondex three
print(cars[:4])

#printing from hiance to probox
print(cars[2:5])

#list mutability
#we use the function append to add an item at the end of a list
cars.append("subaru")
print(cars)

cars.append("Mercedes")
print(cars)

#We use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

#we can use an index to add items to a list
cars[5] = "Jeep"
print(cars)

#we can use the sort function to sort our items in alphabetical order
cars.sort()
print(cars)
