#Check if the first and last number of list is same(user input)

user_input = input("Enter a list of numbers separated by spaces: ")
user_numbers = user_input.split()
numbers = [int(num) for num in user_numbers]
if len(numbers) >= 2 and numbers[0] == numbers[-1]:
    print("The first and last numbers in the list are the same.")
else:
    print("The first and last numbers in the list are different.")


'''user input
numbers = [5, 2, 7, 8, 3, 6, 5]  # Replace this list with your numbers

if len(numbers) >= 2 and numbers[0] == numbers[-1]:
    print("The first and last numbers in the list are the same.")
else:
    print("The first and last numbers in the list are different.")
'''
