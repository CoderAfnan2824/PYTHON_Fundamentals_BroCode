operator = input("Select any operator ( + - * /): ")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

result = -1

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("Incorrect operand")
    
print(round(result, 2))