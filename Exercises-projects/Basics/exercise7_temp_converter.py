
type = input("Enter type of conversion ( C or F): ")

temp = float(input("Enter the amount of temperature: "))

if type == 'C':
    ans = (temp - 32) * 5/9
    t = 'F'
elif type == 'F':
    ans = ((temp * 9)/5) + 32
    t = 'C'
else:
    print(f"{type} is wrong type of unit measurement")

print(f"{temp} {t} converted as {ans} {type}")