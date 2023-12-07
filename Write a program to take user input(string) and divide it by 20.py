#Q. Write a program to take user input(string) and divide it by 20
# Get user input as a string
user_input = input("Enter a number (as a string): ")

try:
    # Convert the user input to a float (decimal number)
    number = float(user_input)
    
    # Check if the number is 0 to avoid division by zero
    if number == 0:
        print("Division by zero is not allowed.")
    else:
        # Perform the division
        result = number / 20
        print(f"Result of {number} divided by 20 is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid numeric string.")
