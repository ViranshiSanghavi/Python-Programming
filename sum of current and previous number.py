#To iterate first ten number and after iteration print sum of current and previous number
print("Iterating over numbers from 1 to 10:")
l = []
for i in range(1, 11):
    l.append(i)
    if len(l) >= 2:
        previous_number = l[-2]
        current_number = l[-1]
        sum_of_previous_and_current = previous_number + current_number
        print(f"Current number: {current_number}, Previous number: {previous_number}, Sum: {sum_of_previous_and_current}")


'''
user input
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

print(f"Iterating over numbers from {start} to {end}:")
l = []
for i in range(start, end + 1):
    l.append(i)
    if len(l) >= 2:
        previous_number = l[-2]
        current_number = l[-1]
        sum_of_previous_and_current = previous_number + current_number
        print(f"Current number: {current_number}, Previous number: {previous_number}, Sum: {sum_of_previous_and_current}")

'''
