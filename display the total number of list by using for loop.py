'''Write a program to display the total number of list by using for loop
l1=[2,4,8,10,12,14,16,18,20]
'''

l1 = [2, 4, 8, 10, 12, 14, 16, 18, 20]
count = 0

for element in l1:
    count += 1

print(f"The total number of elements in the list is: {count}")
