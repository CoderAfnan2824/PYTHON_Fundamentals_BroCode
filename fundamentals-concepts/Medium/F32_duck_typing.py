'''

Duck Typing: “If it walks like a duck and quacks like a duck, it is a duck.”
It means you don't have to be same object type. the only thing matters is the same behaviour/property in duck typing

'''


class Animal:
    alive = True

class Dog(Animal):

    def speak(self):
        print("Woof")

class Cat(Animal):

    def speak(self):
        print("MEOW")

# Here Car class is not related to Animal class. But the behaviour(speak) is still there
#   and it's connected to Dog and Cat type. This is called Duck typing
class Car:

    alive = False
    def speak(self):
        print("HONK")


animals = [Dog(), Cat(), Car()]

for i in animals:
    i.speak()
    print(i.alive)