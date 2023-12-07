#Q. Return a count of a given substring from a string
# Get user input for the string
input_string = input("Enter a string: ")

# Get user input for the substring to count
substring = input("Enter the substring to count: ")

# Count the occurrences of the substring (case-insensitive)
count = input_string.lower().count(substring.lower())

# Print the count
print(f"The substring '{substring}' appears {count} times in the input string.")
