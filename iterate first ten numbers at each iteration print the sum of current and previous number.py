#Write a program to iterate first ten numbers at each iteration print the sum of current and previous number.

previous_number = 0
for current_number in range(1, 11):
    sum_of_numbers = current_number + previous_number
    print(f"Current number: {current_number}, Previous number: {previous_number}, Sum: {sum_of_numbers}")
    previous_number = current_number
