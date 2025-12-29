# Dictionary: It's a collection of {key:value} pair
# Its ordered and changeable. But no duplicates allowed


capitals = {"Telangana":"Hyderabad",
            "Karnataka":"Bengaluru",
            "Maharastra":"Mumbai"}


print(capitals.get("Karnataka"))
print(capitals.get("Kerala")) # return None

if capitals.get("Telangana"):
    print("Key exists")
else:
    print("Key doesn't exists")


# Update existing key or insert new key
capitals.update({"Japan":"Tokyo"})
capitals.update({"Karnataka":"BLR"})

print(capitals)

#remove items
capitals.pop("Karnataka")   # Removes karnataka key
capitals.popitem()  #   Removes latest item inserted into this dictionary

print(capitals)

#capitals.clear()

# Obtain list of keys
keys = capitals.keys()

for value in capitals.values():
    print(value)


items = capitals.items()

print(items)