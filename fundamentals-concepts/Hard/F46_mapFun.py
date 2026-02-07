'''
Docstring for fundamentals-concepts.Hard.F46_mapFun
Map() is a built-in function in Python that applies a given function to each item of an iterable (like a list) and returns an iterator that yields the results. The syntax for the map() function is: map(function, iterable)

'''

ls = [1, 2, 3, 4, 5]

def double(x):
    return x * 2

doubled_list = list(map(double, ls))
print(doubled_list) # Output: [2, 4, 6, 8, 10]