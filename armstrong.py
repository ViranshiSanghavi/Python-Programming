#Armstrong
def armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        return True
    else:
        return False
num = int(input("Enter a number: "))
if armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")



#0,1,153,370,371,407
