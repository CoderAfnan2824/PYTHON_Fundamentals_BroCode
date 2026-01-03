'''
Property Decorator: It's used to define additional logic while modifying attributes of the object
Using it, you can use method like an attribute.
Also, you can encapsulate the attribute

We use property decoroator To add logic, validation, or calculation without changing how the attribute is used

'''

class Student:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property    # It lets the method behave like an attribute
    def age(self):
        return self._age
    # we retuen self._age instead of self.age. Because if we call self.age, it causes
    #   and infinite loop
    
    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            self._age= -100
    


s1 = Student("Afnan", 25)
print(s1.age)

s1.age = -9

print(s1.age)
