'''
Collections: It's a single "variable" used to store multiple values
1. List: [] Ordered and changeable, duplicates work
2. Set:  {} unordered and immutable, but you can add/remove. Duplicates not allowed
3. Tuple: () Ordered and unchangable, duplicates work, but they are faster than List
'''

#Use print(help(fruits)) to know more about many methods for List

# 1. LIST
fruits = ["apple","banana","coconut"] # List

print(fruits)
print(fruits[0])
print(fruits[::])
print(fruits[::-1])
print("apple" in fruits)    # It checks if apple in fruits. True if present.Else returns False

#methods in list
fruits.append("pineapple")  # add element at last
fruits.remove("apple")      # remove mentioned element
fruits.insert(1,"mango")    # insert Mango at index 1 and move all elements from 1 to right shift
fruits.sort()               # sorts alphabetically
fruits.reverse()            # Reverse order of the list
fruits.clear()              # Clear whole list
#fruits.index("apple")       # returns first occurance of given element
#fruits.count("apple")       # returns the no of times apple is present


for fruit in fruits:
    print(fruit)

# 2. Tuple

names = ("afn", "sam", "abhi")  # Tuple
print(len(names))

#Restrictions in tuple
names[0] = "krish"  # Tuple are immutable, meaning you can't change anything, but add/remove allowed





