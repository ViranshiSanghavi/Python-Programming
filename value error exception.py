#Write a program the user to input the integer and raise a value error exception
#of the input the is not a valid integer
try:
    user_input = input("Enter an integer: ")
    user_integer = int(user_input)
    print("You entered:", user_integer)
except ValueError:
    print("Error: Please enter a valid integer.")

#Output: abc (Error: Please enter a valid integer.) OR
#Output: 4(You entered:4)
