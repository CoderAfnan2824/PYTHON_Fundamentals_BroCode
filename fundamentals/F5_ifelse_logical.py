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


# ternary operation: shortcut one-liner for if-else code

print("even " if age % 2 == 0 else "odd")

# there are three logical expresiions: and, or, not

gender = 'male'
vote = 18
if gender == 'male' and age > 18:
    print('man')
elif gender == 'male' or age > 18:
    print("male or young")

if not age >= vote:
    print("cant vote")