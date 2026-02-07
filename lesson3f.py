


# Create a python program that is able to determine  whether a person can donate blood on the age and weight of a person. if the weight is greater than 50 kgs and age is above 18, can be able to donate blood, else not possible.

age = int(input("Enter age"))
weight = int(input("Enter weight"))

if age >= 18 and weight >= 50 :
    print("Can donate blood")
else :
    print("can't donate") 