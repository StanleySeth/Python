#A dictionary is a data type that stores data in terms of key - value pair.
#It is introduced by the use of curly braces {}
#The values stored inside of a dictionary can be of any data type.
#To access the values in a dictionary we use the keys


phonebook = {
    "Benson" : "+254712345678",
    "Mary" : "+2547187654321",
    "Stephen" : "+254723145678"
}

#showing the entire dictionary
print(phonebook)
print(type(phonebook))

#print out benson's number
print(phonebook["Benson"])

print("===============================================")

player = {
    "name" : "Messi",
    "age" : 40,
    "teams" : ["PSG", "Barcelona", "Argentina"],
    "more" : {
        "children" : 3,
        "residence" : "US",
        "phone" : "12345678", "87654321", "56734218"
    }
}

#print Barcelona
print(player["teams"][1])

#print Messi;s second number 
print(player[more[phone[1]]])