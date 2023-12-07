#Write a program to calculate the sum of all numbers from one to given number
n = int(input("Enter a number: "))
sum_of_numbers = 0

for i in range(1, n + 1):
    sum_of_numbers += i

print(f"The sum of all numbers from 1 to {n} is: {sum_of_numbers}")
