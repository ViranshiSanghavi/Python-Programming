#Write a program to check if the first and last number of a list is same
user_input = input("Enter a list of numbers separated by spaces: ")
user_list = [int(item) for item in user_input.split()]

if user_list and user_list[0] == user_list[-1]:
    print("The first and last number are the same")
else:
    print("The first and last number are not the same")
