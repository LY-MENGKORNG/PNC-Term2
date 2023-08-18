total = 0

# Function definition is here
def sum( arg1, arg2 ):
    total = arg1 + arg2
    print("Inside the function local total : ", total)


sum(10,20);
print("Outside the function global total : ", total)