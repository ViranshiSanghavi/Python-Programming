#Write down a function which calculate the square root and power of a number (user input)
# Take user input for a number
number = float(input("Enter a number: "))

# Calculate and display the square root
square_root = number ** 0.5
print(f"Square root of {number} is: {square_root}")

# Take user input for the exponent
exponent = int(input("Enter an exponent for power calculation: "))

# Calculate and display the result of raising the number to the power of the exponent
power_result = number ** exponent
print(f"{number} raised to the power of {exponent} is: {power_result}")

'''
Enter a number: 9
Square root of 9.0 is: 3.0
Enter an exponent for power calculation: 2
9.0 raised to the power of 2 is: 81.0
'''
