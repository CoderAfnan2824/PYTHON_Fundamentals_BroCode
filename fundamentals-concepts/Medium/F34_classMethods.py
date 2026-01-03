'''
Class methods are used when you are working on class data.
Always use cls instead of class name for calling class methods. 
class methods doesn't break when you call methods either using child/parent classes.

Static methods behave like normal methods

If you need class data → @classmethod
If you need nothing from class/instance → @staticmethod

'''

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        count = 0
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += self.gpa

    
    def get_info(self):
        return f"{self.name} : {self.gpa}"
    
    #this is a class method
    @classmethod
    def get_count(cls):
        return Student.count

    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa of {Student.count} students is {cls.total_gpa/cls.count:.2f}"
    


student1 = Student("Afnan", 8.6)
student2 = Student("Sam", 9)

print(Student.get_avg_gpa())
print(student2.get_avg_gpa())
print(student2.get_info())