# functions with parameters
# parameters: They are values that get passed as argument given to a funtion inside of the parenthesis


def greetings(name):
    print(f"{name}, How are you? Hope everything is fine.")

greetings("Karl")
greetings("Wambo")
greetings("Val")

print("============================================")
def message (name):
    print(f"Hello {name} We shall be having a general meeting on date....... Please avail yourself")

message("Joy")
message("Stephen")

print("=========================================================")
# Create function that accepts parameter to add two numbers

def  addition(x, y):
   sum = x + y
   print("The sum of the numbers is: ", sum)


addition(67, 67)