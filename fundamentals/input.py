
# basic input: always returns string type
name = input("Enter your name: ")
print(name)

# change return type of input
age = int(input("Enter your age: "))
print(f"My age is {age}")

# Enter multiple inputs
a, b = input("enter 2 values: ").split()
print(a+" "+b)

# Type cast multiple inputs
aa, bb = map(int, input().split())
print(f"1st value: {aa}. 2nd value: {bb}")