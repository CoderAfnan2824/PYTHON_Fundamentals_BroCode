
menu = {"pizza":"100",
        "burger":"70",
        "sandwich":"70",
        "chat":"50"}

cart = []
price = 0

while True:
    item = input("Enter the menu items(q to quit): ")
    if item == 'q':
        break
    elif menu.get(item) is not None:
        cart.append(item)

for food in cart:
    price += int(menu.get(food))
    print(food,end=" ")

print()
print("---------")
print(f"Final Bill: {price}")
