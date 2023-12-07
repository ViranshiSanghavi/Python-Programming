#Q. Write a program or create a class with a (name,age,class), init(), myfunction()
class Student:
    def __init__(self, name, age, student_class):
        self.name = name
        self.age = age
        self.student_class = student_class

    def myfunction(self):
        print(f"Name: {self.name}, Age: {self.age}, Class: {self.student_class}")

# Get user input for student details
name = input("Enter name: ")
age = int(input("Enter age: "))
student_class = input("Enter class: ")

# Create a Student object
student = Student(name, age, student_class)

# Display student details
student.myfunction()

