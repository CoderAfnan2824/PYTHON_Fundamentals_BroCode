
type = input("Enter type of weight: K or L: ")

weight = float(input("Enter the amount of weight: "))

if type == 'K':
    print(f"Weight of {weight} kgs is {weight * 2.20462} lbs")
elif type == 'L':
    print(f"Weight of {weight} lbs is {weight / 2.20462} kgs")
else:
    print("Enter correct weight type")