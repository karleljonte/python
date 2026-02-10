# Python functions
# They are a block of code/statement that perfoms a given task/action. They can be rescued through out the program to perfom different tasks.
# functions are deffined using the def keyword. (define)
# We have two main types of functions i.e :
#1. inbuilt functions-> They come preintslled with the interprater i,e print(), pop(), range(), append( etc...)
# 2. User defined functions => They are created by a programer to solve a given task.
# To define a function you need to give it a name followed ny parenthesis.
#For he funtions, it os usually indented and to involve a function we use the function name.

def greetings():
    print("Hello, how are you?")

#Below we call the function by use of its name
greetings()


print("=============================================")
# Adition function
def addition():
    num1 = 40
    num2 = 50
    sum = num2 + num2
    print("The sum of the number is: ", sum)

addition()

print("=============================================")

# create a function that  is able to multiply three values

def multiplication():
    number1 = 3
    number2 = 3
    number3 = 3
    miltiply = number1 * number2 * number3
    print("the mutltiplication is", miltiply)

multiplication()


print("=============================================")
# Below is a division function
def divide():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    quotient = number1 / number2
    print("The answer is", quotient)


for i in range(5):
    print(f"\nCalculation number {i + 1}")
    divide()
    print("------------------")
