# 2d Collections store data in row and columns
# it stores individual list as a row

fruits = ["apple","banana", "coconut"]
vegies = ["carrot", "tomato"]
others = ["milk", "maggie", "chicken", "curd"]

# 2d List: stores each list as a row
groceries = [fruits, vegies, others]

# Accessing elements in 2d
fruits[0] = "custard-apple"
groceries[0][1] =  "mango"

# Iterating thru 2d List
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()