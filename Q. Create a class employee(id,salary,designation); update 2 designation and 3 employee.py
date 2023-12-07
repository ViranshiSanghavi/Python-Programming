#Q. Create a class employee(id,salary,designation);
#update 2 designation and 3 employee
class Employee:
    def __init__(self, id, salary, designation):
        self.id = id
        self.salary = salary
        self.designation = designation

    def update_designation(self, new_designation):
        self.designation = new_designation

employees = [
    Employee(input("Enter ID: "), input("Enter Salary: "), input("Enter Designation: ")) for _ in range(3)
]

for i in range(2):
    employees[i].update_designation(input(f"Update designation for Employee {i + 1}: "))

for employee in employees:
    print(f"Employee {employee.id} - ID: {employee.id}, Salary: {employee.salary}, Designation: {employee.designation}")
