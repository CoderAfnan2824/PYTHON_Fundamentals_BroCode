# variables

item = input("what item did you buy? ")
price = float(input("Enter the price: $"))
quantity = int(input("Enter the no of items you buy: "))

total = price * quantity

print(f"You bought {quantity} {item} for ${total} dollars")