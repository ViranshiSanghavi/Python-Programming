'''Create a string which contains all the vowels and
check the user input whether it contains vowel or not(use if else)'''
# String containing all vowels
vowels = "aeiouAEIOU"

# Take user input
user_input = input("Enter a string: ")

# Check if the user input contains vowels
contains_vowels = any(char in vowels for char in user_input)

# Display the result
if contains_vowels:
    print("The input contains vowels.")
else:
    print("The input does not contain vowels.")
