
#Class variable: they are common to all the objects and created outside constructor
# They are used to store common info like number of objects, common date

# It's good practice to always refer class variable using class instead of objects

class Student:

    number_of_students = 0
    class_year = 2024

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.number_of_students += 1


student1 = Student("Afnan", 25)
student2 = Student("Sam", 24)
student3 = Student("Abhi", 23)

print(f"The number of students graduating from class {Student.class_year} are {Student.number_of_students}")