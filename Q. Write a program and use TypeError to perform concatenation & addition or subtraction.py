#Q. Write a program and use TypeError to perform concatenation & addition or subtraction
def perform_operation(a, b):
    try:
        result = a + b
        return result
    except TypeError as e:
        return str(e)

# Get user input for a and b
a = input("Enter a value for 'a': ")
b = input("Enter a value for 'b': ")

# Convert inputs to appropriate types (string by default)
try:
    a = int(a)
except ValueError:
    try:
        a = float(a)
    except ValueError:
        pass

try:
    b = int(b)
except ValueError:
    try:
        b = float(b)
    except ValueError:
        pass

# Perform the operation
result = perform_operation(a, b)

# Display the result or error message
print("Result:", result)

