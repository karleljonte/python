# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.

def simple_interst (p, r, t):
    calculation = p * r * (t/100)
    print("The simple interest is ", calculation)


simple_interst(45000, 7, 8)

print("==============")


def simple_interst (p, r, t):
    calculation = p * r * (t/100)
    print("The simple interest is ", calculation)

for x in range(2):
    simple_interst(55000, 8, 9)
    simple_interst(60000, 5, 10)