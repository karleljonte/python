# A dictionary is a data type that stores data in terms of key - value pair.
# It is introduced by the use of curly baces {}
# The values stored inside of a dictionary can be any data type.
# To access the values in a dictionary we use the keys

Phonebook = {
    "Benson" : "254764737292",
    "Mary" : "25472827373",
    "Stephen" : "254839893832"
}

print(Phonebook)

print(type(Phonebook))

# Print out benson's number

print(Phonebook["Benson"])

player = {
    "Name": "Messi",
    "age": 40,
    "teams": ["PSG", "Barcelona", "Argentina"]
}
# second club
print(player["teams"][1])

# research on if ... else statements in pytho