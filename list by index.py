#Print a list by using index
# Get user input for a list (comma-separated values)
user_input = input("Enter a list of numbers separated by commas: ")

# Split the user input into a list of integers
my_list = [int(item.strip()) for item in user_input.split(',')]

# Print the list by using indices
for i in range(len(my_list)):
    print(f"Element at index {i}: {my_list[i]}")
