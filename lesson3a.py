# Boolean this is a data type that evaluates either true or faulse 

is_raining = False

print(is_raining)
print(type(is_raining))

paidloan = True

print(paidloan)
print(type(paidloan))

# comparison operations: they are used to compare two or more statements and they ussually return a boolean answer

number1 = 2
number2 = 5

print("Is number one grather than number 2?", number1 > number2)
print("Is number one less than number 2?", number1 < number2)
print("Is number one grather or equal to number 2?", number1 >= number2)
print("Is number one less than or equal to number 2?", number1 <= number2)
print("Is number one equal to  number 2?", number1 == number2)
print("Is number one not equal to number 2?", number1 != number2)
# Logical operators 
# logical And
# it returns if the conditions/statement are true

print((3 > 1) and (7 > 6))

# logical or
# it evaluates to true if one the staments/conditions is true

print((3 > 1) or (7 < 6))


#logical not
# it is used to negate a statement/condition
print(not(90 > 70))