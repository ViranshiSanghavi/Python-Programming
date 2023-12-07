#Write a python program to check if each string starts with a capital letter
# Input string
input_string = input("Enter a string: ")

# Check if the first character is a capital letter
if input_string[0].isupper():
    print("The string starts with a capital letter.")
else:
    print("The string does not start with a capital letter.")
