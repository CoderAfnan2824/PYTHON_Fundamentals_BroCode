'''
Docstring for fundamentals-concepts.Hard.F47_filterfun
Filter() is a built-in function in Python that filters elements from an iterable (like a list) based on a given function that returns True or False. The filter() function returns an iterator that yields the elements for which the function returns True.

The syntax for the filter() function is: filter(function, iterable)
'''

grades = [85, 92, 78, 90, 88]

def is_passing(grade):
    return grade >= 80

passing_grades = list(filter(is_passing, grades))

print(passing_grades) # Output: [85, 92, 90, 88]