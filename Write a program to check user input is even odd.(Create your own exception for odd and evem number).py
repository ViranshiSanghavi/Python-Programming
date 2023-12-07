#Q. Write a program to check user input is even odd.(Create your own exception for odd and evem number)
# Custom exception for odd numbers
class OddNumberError(Exception):
    pass

# Custom exception for even numbers
class EvenNumberError(Exception):
    pass

try:
    # Get user input as an integer
    number = int(input("Enter a number: "))
    
    # Check if the number is even or odd
    if number % 2 == 0:
        raise EvenNumberError("Even number detected.")
    else:
        raise OddNumberError("Odd number detected.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except EvenNumberError as e:
    print(e)
except OddNumberError as e:
    print(e)
