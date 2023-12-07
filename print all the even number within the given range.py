# Write a program to print all the even number within the given range
start = 1 
end = 20   

print(f"Even numbers between {start} and {end} are:")
for number in range(start, end + 1):
    if number % 2 == 0:
        print(number)



'''
user input

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Even numbers between {start} and {end} are:")
for number in range(start, end + 1):
    if number % 2 == 0:
        print(number)
'''
