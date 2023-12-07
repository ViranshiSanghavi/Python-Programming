# Write a program to find the sum of all the numbers stored in a list
numbers = input("Enter numbers separated by spaces: ")
numbers_list = [int(x) for x in numbers.split()]
total = sum(numbers_list)
print("The sum of the numbers is:", total)
