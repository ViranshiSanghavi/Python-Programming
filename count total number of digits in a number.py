#Count total number of digits in a number
num = int(input("Enter a number:"))
count = 0
while num > 0:  
    num //= 10
    count += 1
print("Total number of digits is:", count)
