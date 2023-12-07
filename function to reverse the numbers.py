#Write a function that reverse the user defined value
def findReverse(n):
    reverse = 0
    while n != 0:
        remainder = n % 10
        reverse = reverse * 10 + remainder
        n = n // 10
    return reverse

num = int(input("Enter the number:"))
reverse = findReverse(num)
print("The reverse number is =", reverse)
