#A for loop can also be used to iterate through a list, tuple, string or even a dictionary.
name = "Name"

for letter in name:
   if letter == "m":
      print("The letter is m")
   else:
      print(letter)
    
print("======================================")
#below is a list of counties
counties = ["Nairobi", "Mombasa", "Kisumu", "Eldoret", "kajiado", "Machakos", "Meru", "Embu"]
print(counties)

for county in counties:
   print(county)

print("======================================")

##counties= (input("Enter County:"))

   #print("County included")    
#else:
   #print("County Not Found")

#print("======================================")

#The for loop can also be used to create through a dictionary

player = {
   "name": "Mbappe",
   "age": 25,
   "teams": ["PSG", "Monaco", "France"],
   "nationality": "French"
}

for key in player:
   print(key)

print("======================================")
for value in player:
   print(player[value])
#Show the loop of the teams
print("======================================")
for team in player["teams"]:
   print(team)