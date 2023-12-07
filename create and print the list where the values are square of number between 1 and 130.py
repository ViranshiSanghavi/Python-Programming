# Write a function to create and print the list where the values are square of number between 1 and 130

def generate_square_list():
    square_list = [x**2 for x in range(1, 131)]
    return square_list

def print_square_list(square_list):
    for num in square_list:
        print(num)

# Generate the list of squares
squares = generate_square_list()

# Print the list of squares
print_square_list(squares)

''' user
def generate_square_list(start, end):
    square_list = [x**2 for x in range(start, end + 1)]
    return square_list

def print_square_list(square_list):
    for num in square_list:
        print(num)

# Get user input for the range of numbers
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# Generate the list of squares
squares = generate_square_list(start, end)

# Print the list of squares
print_square_list(squares)

'''

