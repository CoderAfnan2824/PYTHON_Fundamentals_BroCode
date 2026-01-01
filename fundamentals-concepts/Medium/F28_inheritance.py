
#Inheritance: This property allows you to reuse code and extend properties from parent class
# This property allows to create parent-child relationship

class Animal:

    number_of_animals = 0

    def __init__(self, name, color):
        self.name = name
        self.color = color
        Animal.number_of_animals += 1


class Dog(Animal): # It's a way we define child using parent
    Animal.number_of_animals = 10 #First this runs, then parent constructor runs

class Cat(Animal):
    pass


dog1 = Dog("bruno", "Brown")
print(f"dog: {Dog.number_of_animals}")
cat1 = Cat("Tom", "Blue")
parrot = Animal("Chotu", "Green")

print(Cat.number_of_animals)

print(Animal.number_of_animals)

print(parrot) # It references to Parent class