#Print multiplication table of a given number
num = int(input("Enter a number:"))
print("Multiplication Table")
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')
