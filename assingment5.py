# Q 1: Create a function that: 
# • Takes no parameters 
# • Uses arithmetic operators to calculate the area of a rectangle 
# • Prints the result 


def rectangle_area():
    length = 10
    width = 5
    area = length * width
    print("The area of the rectangle is:", area)

rectangle_area()


# Q 2: Create a function that: 
# • Accepts two numbers as parameters 
# • Returns their sum, difference, product, and division

def calculate(a, b):
    sum_ = a + b
    difference = a - b
    product = a * b
    division = a / b

    return sum_, difference, product, division

results = calculate(10, 5)
print(results)


# Q 3: Write a function that: 
# • Accepts a number (use input function) 
# • Checks whether the number is: 
# • Positive 
# • Negative 
# • Zero

def check_number():
    num = int(input("Enter a number: "))

    if num > 0:
        print("The number is Positive")
    elif num < 0:
        print("The number is Negative")
    else:
        print("The number is Zero")

check_number()


# Q 4: Write a function that: 
# • Accepts a number n 
# • Uses a for loop 
# • Calculates the sum of numbers from 1 to n 

def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum_to_n(5))


# Q 5: Write a function that: 
# • Accepts a number (Use input() function) 
# • Uses a while loop 
# • Calculates the square of numbers from 1 up to that number

def squares_up_to_n():
    n = int(input("Enter a number: "))
    i = 1

    while i <= n:
        print(i, "squared is", i * i)
        i += 1

squares_up_to_n()
