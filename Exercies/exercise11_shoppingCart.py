food = []
prices = []
total = 0

while True:
    item = input("Enter the food item ( q to quit): ")
    if item.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price amount for {item}: "))
        food.append(item)
        prices.append(price)

print("--- Items added to card ---")
for i in food:
    print(i,end=" ")

print()
for i in prices:
    total += i

print(f"Total bill amount: Rs {total}")