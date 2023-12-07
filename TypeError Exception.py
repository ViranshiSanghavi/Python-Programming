#Write a program that prompts the user to input two number and raises a TypeError
#exception of the inputs are not numerical
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = num1 + num2
    
    print("Sum:", result)
except ValueError:
    print("Error: Please enter valid numerical values.")
