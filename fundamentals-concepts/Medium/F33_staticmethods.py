'''

Static methods: The method that belongs to class than the instance of that class
        and used for general utility functions

instance methods: Best for operations on the instance of the class
Static method: best for utility functions that don't need access to class data
'''

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_into(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod   # This is static method. self not needed for static method
    def is_valid_pos(position):     # called using the class only
        existing_pos = ["Manager", "Cashier", "Cook"]

        return position in existing_pos
    

e1 = Employee("Afnan", "Manager")
e2 = Employee("Sam", "Engineer")

print(e1.get_into())    
print(e2.get_into())    

print(Employee.is_valid_pos("Cook"))
print(Employee.is_valid_pos(e2.position)) 

