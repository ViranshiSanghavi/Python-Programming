#Write a program to calculate the sum of odd number with user defined range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
sum_of_odd_numbers = 0

print(f"Odd numbers between {start} and {end} are:")
for number in range(start, end + 1):
    if number % 2 != 0:
        print(number)
        sum_of_odd_numbers += number

print(f"The sum of odd numbers between {start} and {end} is: {sum_of_odd_numbers}")

