#Q. Create a two list with even and odd numbers from one list
# Get user input for numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Split the input into a list of integers
numbers = [int(num) for num in user_input.split()]

# Separate even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the lists of even and odd numbers
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
