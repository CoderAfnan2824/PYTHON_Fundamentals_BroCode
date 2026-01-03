'''
Magic methods: They are dunder methods which allows objects to behave like built-in types
'''


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Below is magic method to print object
# called by: print(object)
    def __str__(self):  
        return f"Name: {self.name}, Age: {self.age}"

# Below is magic method to print object
# called by: object (no need of print)
    def __repr__(self):
        return f"Name: {self.name}, : {self.age}"
    
# Below is magic method for equal case
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
# below is magic method for less than case
    def __lt__(self, other):    # __gt__ is for greater than scenario
        return self.age < other.age

# below is magic method for add, sub, mul
    def __add__(self, other):
        return self.age + other.age
    
    '''
    other example: __sub__, __mul__
    '''


s1 = Student("Afnan", 25)
s2 = Student("Afnan", 23)
print(s1)
s1

print(s1==s2)

print(s1<s2)

print(s1+s2)