# Write a program that accept a string and calculate the number of digit and letter

input_string = input("Enter a string: ")

letter_count = 0
digit_count = 0

for char in input_string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print(f"Number of letters in the string: {letter_count}")
print(f"Number of digits in the string: {digit_count}")

''' NOT USER INPUT code:
input_string = "i am devanshi, my roll number is 170"

letter_count = 0
digit_count = 0

for char in input_string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1 

print(f"Number of letters in the string: {letter_count}")
print(f"Number of digits in the string: {digit_count}")
'''
