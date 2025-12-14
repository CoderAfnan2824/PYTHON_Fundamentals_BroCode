'''
Collections: It's a single "variable" used to store multiple values
1. List: [] Ordered and changeable, duplicates work
2. Set:  {} unordered and immutable, but you can add/remove. Duplicates not allowed
3. Tuple: () Ordered and unchangable, duplicates work, but they are faster than List
'''

# Set creation
fruits = {"apple","banana","coconut"}

# Set length
print(len(fruits))

#methods for SET
fruits.add("mango")             # add mango to the SET
fruits.remove("apple")          # remove appple from SET
fruits.clear()                  # Clear whole SET
fruits.pop()                    # Remove random element from the SET
fruits_copy = fruits.copy()     # Shallow copy the set into another
set_difference = fruits.difference(fruits_copy)         # provide difference between SETs
set_intersection = fruits.intersection(fruits_copy)     # provide intersection(common) between SETs
set_union = fruits.union(fruits_copy)                   # provide A+B between SETs

# Set Restrictions
#print(help(fruits))

print(fruits[0])    # throws error as indexing not allowed in SETS (immutable)

