#Tuple
#A tuple is an immutable type of list (It cannot change)
#To introduce a tuple, we use the parenthesis ()
counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")

print(counties)
print(type(counties))

#slicing of tuples
print(counties[3:])

#Accessing items of a tuple by the use of the indexes
print(counties[5])

#Note: Below will generate an error
#Attribute error
counties.append("Kakamega")
print(counties)