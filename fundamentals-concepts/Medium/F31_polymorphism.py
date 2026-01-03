#Polymorphism: Same method name, but different behaviour depending on the type of object


from abc import abstractmethod

#abc: abstract class; abstractmethod ensures child classes must implement certain methods.
#Abstraction must enforce you to define method(implement) in their child classes. Else you get error.



class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle:

    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    

class Square:

    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2 

class Triangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return 0.5 * self.length * self.breadth
    

shapes = [Circle(5), Square(5), Triangle(5,5)]

for i in shapes:
    print(i.area())