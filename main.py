# Class Variable
# class variable = Shared among all instances of a class
# Defined outside the constructor
# Allow you to share data among all object created from that class

class Student:

    class_year = 2026
    num_Student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_Student += 1

Student1 = Student("Spongebob", 30)
Student2 = Student("Patrick", 35)
Student3 = Student("DAV", 51)
Student4 = Student("SkyGod", 21)

print(f"My graduating class year of {Student1.class_year} has {Student1.num_Student} students")

print(f"Name: {Student1.name}, age: {Student1.age}")
print(f"Name: {Student2.name}, age: {Student2.age}")
print(f"Name: {Student3.name}, age: {Student3.age}")
print(f"Name: {Student4.name}, age: {Student4.age}")