'''
Class: It's a blueprint based on which we create objects. The attributes and methods 
        we define in class remain same for all objects

Objects: It's a real world entity which has it values for attributes and method definition

About self: represents the current object instance of the class. Without it, 
            python doesn't know which object variable you are referring to

instance variables: They are defined inside the constructor, 
                    and they are specific to each object and are not shared among objects

Class Variables: They are shared among objects and common. They are defined outside constructor
'''

from car import Car

car1 = Car("BMW", 2025, "Blue", False)
car2 = Car("Benz", 2020, "Olive", True)

print(car1) # prints address of this object
print(car1.model)   # prints model of car1

print(car1.drive("kia")) # the value you gave here doesn't copied in car1 instance's model
