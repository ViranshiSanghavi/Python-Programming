#Write a program to display students marks from record
student_records = {}
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}: ")
    marks = float(input(f"Enter the marks for {name}: "))
    student_records[name] = marks
print("Student Marks:")
for name, marks in student_records.items():
    print(f"Name: {name}, Marks: {marks}")

