# loops -> sometimes, we may need to do a piece of work a number of repeated times in such cases we may use loops.
# A loop is a control stuctuer that allows us to execute a block of code repeatedly until a certain condition is met.
# Below is the syntax of a for loop in python:

"""
for variable in range (n):
       # bllock of code to be executed
"""

# print("Hello Karl")

for greeting in range(5):
    print("hello Karl", greeting)




print("======================================")

for number in range(10, 20) :
    print(number)



print("==============")

# find te even number in the range of 50 to 71

for number in range(50, 71, 2):
    print(number)

print("==================")

# print a py program that print odd numbers from 100 to 150
for number in range(101, 150, 2): 
    print(number)

print("=================")


 # create a program that prints the multiples of 3 starting from 201 to 150

for number in range(201, 149, -3):
   print(number)


# create a python program that prints the leap years in between 2000 and 2024

for number in range(2000, 2024, -4):
    print(number)