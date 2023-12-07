#Q. To change a given string to new string where first
#and last character have been exchanged
# Input string
input_string = input("Enter a string: ")

# Check if the string has at least two characters
if len(input_string) >= 2:
    # Exchange the first and last characters
    new_string = input_string[-1] + input_string[1:-1] + input_string[0]
    print("New string with first and last characters exchanged:", new_string)
else:
    print("The input string is too short to perform the exchange.")
