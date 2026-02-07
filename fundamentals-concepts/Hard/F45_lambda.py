'''
Docstring for fundamentals-concepts.Hard.F45_lambda

Lambda Functions: are anonymous functions that can have any number of arguments but only one expression.
They are often used for short, simple functions that are not reused elsewhere in the code. 
The syntax for a lambda function is: lambda arguments: expression

When to use lambda functions:
1. When you need a simple function for a short period of time and don't want to define
2. When you want to pass a function as an argument to another function (e.g., in higher-order functions like map, filter, and reduce)
3. When you want to create a small function on the fly without cluttering your code with

When not to use lambda functions:
1. When the function is complex and requires multiple lines of code, it's better to define a
2. When you need to reuse the function in multiple places in your code, it's better to define a regular function with a name.
3. When you want to include documentation or comments for the function, it's better to define a
4. When you want to use features that are not supported in lambda functions, such as multiple expressions, statements, or annotations, it's better to define a regular function.

'''

ls = [1, 2, 3, 4, 5]

ls1 = list(map(lambda x: x**2, ls))
print(ls1) # Output: [1, 4, 9, 16, 25]