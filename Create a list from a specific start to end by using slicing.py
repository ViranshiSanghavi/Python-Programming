#Create a list from a specific start to end by using slicing
# Get user input for the start and end values
start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

# Create a list using slicing
my_list = list(range(start, end + 1))

# Print the list
print(my_list)
