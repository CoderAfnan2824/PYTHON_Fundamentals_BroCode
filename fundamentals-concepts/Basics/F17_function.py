# Function: It's a block of code which can be reused when called

def myFunction(name, age):
    print(f"Happy Birthday {name}")
    print(f"You are {age} years old")
    return age + 10


age1 = myFunction("afnan", 26)

print(f"My age after 10 years is {age1}")


#Default functions

def calculator(p, r = 0.05, t = 1):
    return p*pow((1-r),1/t)


print(f"Total value: {calculator(100,0.6,2)}")
print(f"Total value: {calculator(100)}")