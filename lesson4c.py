# A for loop can also be used to iterate through a list, tuple, string or even a dictionary..
name = "Karl"

for letter in name:
    if letter == "r" :
        print("The letter is r")
    else:
        print(letter)

print("=================")
# Below is a list of counties
counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]

print(counties)

for county in counties:
    print(county)


print("========================")

for county in counties:
    if county == "Nakuru" :
        print("county found")
        break
    else:
        print("county not found")

print("========================")


player = {
    "name" : "Mbape",
    "age" : 25,
    "teams" : ["PSG", "Monaco", "France"],
    "nationality": "French"
}


for values in player.values() :
    print(values)


print("========================")
# loop through the teams the player has played for

for team in player["teams"]:
    print(team)

print(player["teams"])
