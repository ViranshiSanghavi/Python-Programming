#Q. Create a class in which we store student details(Roll no, Class, Div, Name)
class Student:
    def __init__(self, roll_no, student_class, division, name):
        self.roll_no = roll_no
        self.student_class = student_class
        self.division = division
        self.name = name

    def display_details(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Class: {self.student_class}")
        print(f"Division: {self.division}")
        print(f"Name: {self.name}")

# Get user input for student details
roll_no = input("Enter Roll No: ")
student_class = input("Enter Class: ")
division = input("Enter Division: ")
name = input("Enter Name: ")

# Create a Student object
student = Student(roll_no, student_class, division, name)

# Display student details
student.display_details()
