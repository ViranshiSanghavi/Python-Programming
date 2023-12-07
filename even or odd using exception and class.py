#write a program to check with user input is even or odd
class NotANumberError(Exception):
    pass

def check_even_or_odd(num):
    try:
        if not num.isdigit():
            raise NotANumberError("Input is not a valid number.")
        
        num = int(num)
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"
    except NotANumberError as e:
        return str(e)

try:
    user_input = input("Enter a number: ")
    result = check_even_or_odd(user_input)
    print(f"The number is {result}.")
except KeyboardInterrupt:
    print("\nProgram terminated by user.")



#OR USING EXCEPTION WITHOUT CLASS [ITS IN THE COMMENT, SO WONT BE EXECUTED :)]
'''
try:
    user_input = int(input("Enter a number: "))
    if user_input % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
except ValueError:
    print("Error: Please enter a valid number.")
'''
