
name = input("Enter your name: ")

if len(name) > 12:
    print("UserName is more than 12 characters. Not allowed")
elif name.find(' ') != -1:
    print(f"Username should not contain any spaces. space at {name.find(' ')}")
elif not name.isalpha():
    print("UserName should not containd any digits")

