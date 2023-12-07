#Write a program to print the fibonacci series
nterms = int(input("How many terms?"))
n1 = 0
n2 = 1
count = 2
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1, ",", n2, sep='', end='')
    while count < nterms:
        nth = n1 + n2
        print(",", nth, sep='', end='')
        n1 = n2
        n2 = nth
        count += 1
    print()
