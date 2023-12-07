# Write a program to iterate through a list using indexing 
user_input = input("Enter a list of items separated by spaces: ")
my_list = user_input.split()
for i in range(len(my_list)):
    item = my_list[i]
    print(f"Item at index {i}: {item}")
