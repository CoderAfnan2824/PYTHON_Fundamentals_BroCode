
age = int(input("Enter your age: "))

while age < 0:
    print("Incorrect age. Enter again:")
    age = int(input())


print(f"My age is {age}")