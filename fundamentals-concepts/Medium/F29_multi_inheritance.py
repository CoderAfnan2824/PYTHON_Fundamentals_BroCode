'''
Multiple Inheritane: this property allows child class to have properties from multiple parents
        Eg: fish Class can have properties of Parents(Animal, organism)

Multi-level inheritance: when a class becomes a child and a parent, this is known as multi-level inheritance
        Eg: c(M3) <- c(BWM) <- C(Car)
'''


class Animal:

    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):

    def run(self):
        print(f"{self.name} is running")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): # This is example of multiple inheritance
    pass

#   c(Hawk) <- c(Predator) <- c(Animal)
#   Above is example of multi-level inheritance

rabbit = Rabbit("Buggy")
hawk = Hawk("SRH")
fish = Fish("Nemo")

fish.eat()
fish.hunt()
fish.run()

#hawk.run() # error; it didn't inherit prey

