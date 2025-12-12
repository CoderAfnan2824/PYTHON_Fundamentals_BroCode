age = int(input("Enter your age: "))

if age < 0:
    print("You ain't born")
elif age < 18:
    print("You are a boy")
elif(age >18 and age < 50):
    print("you are young")
elif( age < 100):
    print("You are old")
else:
    print("not eligible")
