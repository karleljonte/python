#Tuple
# A tuple is an immutable type of a list ( it cannot change)
# to introduce a tuple we use brackets

counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")

print(counties)
print(type(counties))

# Slicing of tuples
print(counties[3:])

# Accesing item of a tuple using indexes
print(counties[4])

# Note below will generate an error
counties.append(machakos)
print(counties)