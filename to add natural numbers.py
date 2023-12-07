# Write a program to add natural numbers
# Take user input for the limit of natural numbers
limit = int(input("Enter a positive integer: "))

# Initialize variables
sum_of_numbers = 0
numbers_added = []

# Calculate the sum of natural numbers and track the numbers being added
for num in range(1, limit + 1):
    numbers_added.append(num)
    sum_of_numbers += num

# Display the sum and the numbers being added
numbers_str = " + ".join(map(str, numbers_added))
print(f"The sum of natural numbers from 1 to {limit} is: {numbers_str} = {sum_of_numbers}")


