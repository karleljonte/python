# Python lists
# A list is a collection of items that ordered in a certain way.
# A list is introduced by the use of the square brackets 
# The items of a list are stored inside of indexes. N ote: In programming we start counting from index Zero (0). bmw, benze, haince...
# A list is mutable i.  the contents of a list can changed


cars = ["BMW", "Benze", "Hiance", "Prado", "Probox", "Mclaren", "Range"]

print(cars)
print(type(cars))

# Accesing items from a list 
print(cars[2])

print(cars[4])

# list sclicing - This is creating a list from a given bigger list
print(cars[4:])

print(cars[:4])

print(cars[2:5])

# List mutability
# We use the function apppend to add an item at the end of a list

cars.append("mercedes")
print(cars)

cars.append("subaru")
print(cars)

print(cars[4:])

# we can use index to add items to list
cars[5] = "Pajero" 
print(cars)

# we can sort function to sort items in alphabetical order
cars.sort()
print(cars)

# we can use the sort function to sort out items in alphabetical order
cars.sort(reverse=True)
print(cars)
del cars[4]
print(cars)
cars.pop(4)
print(cars)

cars.remove("BMW")
print(cars)