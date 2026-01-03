#supers(): It's a function used in child class to call the method from the inherited class
# It allows you to extend the functionality of the inherited method

class Shape():

    def __init__(self, name, color):
        self.name = name
        self.color = color
        print(f"child went to parent")

    def describe(self):
        print(f"This is a {self.name}")

class Circle(Shape):

    def __init__(self, name, color, radius):
        super().__init__(name, color)  
        # is similar to Shape.__init__(self, name, color)
        # Above if we use super, we don't have to use "self" for reference
        self.radius = radius
        print(f"{self} inherited from {super}")
    

    #Method Overriding: The below method modifies the parent method

    def describe(self):
        super().describe()
        print(f"This class is a {self.name}, It's inherited from {super}")
    

class Square(Shape):

    def __init__(self, name, color, width):
        Shape.__init__(self, name, color) #if we don't use super(), this is how we have to call parent constructor each time
        # super().__init__() will replace above line
        self.width = width
        

square = Square("square", "blue", 5)

circle = Circle("circle", "red", 10)

square.describe()
circle.describe()
