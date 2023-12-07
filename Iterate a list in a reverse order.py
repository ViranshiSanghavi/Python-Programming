#Iterate a list in a reverse order
# Get user input for a list of items (comma-separated)
user_input = input("Enter a list of items separated by commas: ")

# Split the input into a list
my_list = user_input.split(',')

# Iterate through the list in reverse order
for item in reversed(my_list):
    print(item)
