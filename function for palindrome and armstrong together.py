#Write a function to check the input value is Armstrong and also write the function for Palindrome
def armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num, "is an armstrong number")
    else:
        print(num, "is not an armstrong number")

def palindrome(num):
    n = num
    rev = 0
    while num != 0:
        rev = rev * 10
        rev = rev + int(num % 10)
        num = int(num / 10)
    if n == rev:
        print(n, "is a palindrome number")
    else:
        print(n, "is not a palindrome number")

num = int(input("Enter a number to check if it is a palindrome: "))
palindrome(num)

num = int(input("Enter a number to check if it is an armstrong number: "))
armstrong(num)

#Output -  1 is an armstrong number
#Output - 2 is a palindrome number (reads same front back)(151,44,11,232)(civic, radar, level, rotor)
#Armstrong numbers:  0, 1, 153, 370, 371, 407
